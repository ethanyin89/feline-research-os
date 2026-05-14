#!/usr/bin/env python3
"""Check DOI metadata and abstract availability for source cards.

This is the reusable second-pass after sheet intake/source-card bootstrap.
It fetches Crossref metadata for selected source cards, writes a reviewable
report, and can conservatively update cards only when an abstract is present.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date
from pathlib import Path


DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>]+", re.IGNORECASE)
TAG_RE = re.compile(r"<[^>]+>")


@dataclass
class SourceCard:
    source_id: str
    path: Path
    title: str
    doi: str
    verification_status: str


@dataclass
class CrossrefCheck:
    source: SourceCard
    found: bool
    title: str = ""
    year: str = ""
    container: str = ""
    abstract: str = ""
    error: str = ""

    @property
    def abstract_available(self) -> bool:
        return bool(self.abstract.strip())

    @property
    def recommended_status(self) -> str:
        if self.abstract_available:
            return "abstract_weighted"
        return self.source.verification_status or "title_only"


def normalize_doi(value: str) -> str:
    match = DOI_RE.search(value.strip())
    if not match:
        return ""
    return match.group(0).rstrip(".,;)").casefold()


def parse_frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*\"?([^\"\n]+)\"?\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def load_source_card(repo_root: Path, source_id: str) -> SourceCard:
    candidates = sorted((repo_root / "raw").glob(f"**/{source_id}.md"))
    if not candidates:
        raise FileNotFoundError(f"source card not found: {source_id}")
    path = candidates[0]
    text = path.read_text(encoding="utf-8")
    title = parse_frontmatter_value(text, "title")
    doi = normalize_doi(parse_frontmatter_value(text, "doi"))
    if not doi:
        doi = normalize_doi(text)
    return SourceCard(
        source_id=parse_frontmatter_value(text, "id") or source_id,
        path=path,
        title=title,
        doi=doi,
        verification_status=parse_frontmatter_value(text, "verification_status") or "title_only",
    )


def load_source_card_path(path: Path) -> SourceCard:
    text = path.read_text(encoding="utf-8")
    source_id = parse_frontmatter_value(text, "id") or path.stem
    title = parse_frontmatter_value(text, "title")
    doi = normalize_doi(parse_frontmatter_value(text, "doi"))
    if not doi:
        doi = normalize_doi(text)
    return SourceCard(
        source_id=source_id,
        path=path,
        title=title,
        doi=doi,
        verification_status=parse_frontmatter_value(text, "verification_status") or "title_only",
    )


def selected_source_cards(
    repo_root: Path,
    source_ids: str | None,
    source_id_file: Path | None,
    source_globs: list[str],
    statuses: set[str] | None,
) -> list[SourceCard]:
    cards_by_id: dict[str, SourceCard] = {}

    if source_ids:
        for source_id in source_ids.split(","):
            source_id = source_id.strip()
            if source_id:
                card = load_source_card(repo_root, source_id)
                cards_by_id[card.source_id] = card

    if source_id_file:
        id_path = source_id_file if source_id_file.is_absolute() else repo_root / source_id_file
        for line in id_path.read_text(encoding="utf-8").splitlines():
            source_id = line.strip()
            if source_id and not source_id.startswith("#"):
                card = load_source_card(repo_root, source_id)
                cards_by_id[card.source_id] = card

    for pattern in source_globs:
        for path in sorted(repo_root.glob(pattern)):
            if path.is_file():
                card = load_source_card_path(path)
                cards_by_id[card.source_id] = card

    cards = sorted(cards_by_id.values(), key=lambda card: card.source_id)
    if statuses is not None:
        cards = [card for card in cards if card.verification_status in statuses]
    return cards


def strip_jats(value: str) -> str:
    text = TAG_RE.sub(" ", value)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def first_value(value: object) -> str:
    if isinstance(value, list) and value:
        return str(value[0])
    if isinstance(value, str):
        return value
    return ""


def issued_year(message: dict[str, object]) -> str:
    for key in ("published-print", "published-online", "issued", "created"):
        value = message.get(key)
        if isinstance(value, dict):
            parts = value.get("date-parts")
            if isinstance(parts, list) and parts and isinstance(parts[0], list) and parts[0]:
                return str(parts[0][0])
    return ""


def fetch_crossref(doi: str, timeout: float = 20.0) -> dict[str, object]:
    encoded = urllib.parse.quote(doi, safe="")
    url = f"https://api.crossref.org/works/{encoded}"
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "feline-research-os-source-check/1.0 (mailto:local@example.invalid)",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def check_source(source: SourceCard, timeout: float) -> CrossrefCheck:
    if not source.doi:
        return CrossrefCheck(source=source, found=False, error="no DOI in source card")
    try:
        payload = fetch_crossref(source.doi, timeout=timeout)
    except urllib.error.HTTPError as exc:
        return CrossrefCheck(source=source, found=False, error=f"HTTP {exc.code}")
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        return CrossrefCheck(source=source, found=False, error=str(exc))

    message = payload.get("message")
    if not isinstance(message, dict):
        return CrossrefCheck(source=source, found=False, error="missing Crossref message")

    return CrossrefCheck(
        source=source,
        found=True,
        title=first_value(message.get("title")),
        year=issued_year(message),
        container=first_value(message.get("container-title")),
        abstract=strip_jats(str(message.get("abstract", ""))),
    )


def md_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def short(value: str, limit: int = 220) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "..."


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "source-check"


def render_report(checks: list[CrossrefCheck], source_label: str, report_id: str | None = None) -> str:
    today = date.today().isoformat()
    stable_id = report_id or f"feline-source-metadata-check-{today.replace('-', '')}-{slugify(source_label)[:48]}"
    lines = [
        "---",
        f"id: {stable_id}",
        "type: system",
        "topic: content-pipeline",
        "question_type: source-check-report",
        "language: zh",
        f"last_compiled_at: {today}",
        "verification_status: generated",
        "decision_grade: no",
        "owner: codex",
        "status: active",
        "---",
        "",
        f"# Feline Source Metadata Check, {today}",
        "",
        f"Source set: `{source_label}`",
        "",
        "## Rule",
        "",
        "This report is a repeatable second-pass source check. It does not make clinical claims.",
        "",
        "- DOI metadata alone does not upgrade a card.",
        "- Abstract availability can justify `abstract_weighted` only for navigation and extraction priority.",
        "- Full-text or structured worksheet review is still required before `source_checked` or `deep_extracted`.",
        "",
        "## Summary",
        "",
        f"- Cards checked: `{len(checks)}`",
        f"- Crossref metadata found: `{sum(1 for check in checks if check.found)}`",
        f"- Abstract available: `{sum(1 for check in checks if check.abstract_available)}`",
        "",
        "## Check Table",
        "",
        "| Source | Current | Recommended | DOI | Year | Container | Abstract | Error |",
        "|---|---|---|---|---:|---|---|---|",
    ]
    for check in checks:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{check.source.source_id}`",
                    f"`{check.source.verification_status}`",
                    f"`{check.recommended_status}`",
                    f"`{check.source.doi}`" if check.source.doi else "",
                    md_escape(check.year),
                    md_escape(short(check.container, 70)),
                    "`yes`" if check.abstract_available else "`no`",
                    md_escape(short(check.error, 80)),
                ]
            )
            + " |"
        )

    lines.extend(["", "## Abstract Availability Notes", ""])
    for check in checks:
        lines.append(f"### `{check.source.source_id}`")
        if check.abstract_available:
            lines.append("")
            lines.append(f"- Crossref title: {md_escape(check.title or check.source.title)}")
            lines.append(f"- Abstract lead for scope check only: {md_escape(short(check.abstract, 180))}")
            lines.append("- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.")
        elif check.found:
            lines.append("")
            lines.append("- Crossref metadata resolved, but no abstract was available from Crossref.")
            lines.append("- Keep the card at its current status until abstract or full text is read.")
        else:
            lines.append("")
            lines.append(f"- Metadata check failed: {md_escape(check.error)}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def replace_scalar_field(text: str, key: str, value: str) -> str:
    pattern = re.compile(rf"^({re.escape(key)}:\s*).*$", re.MULTILINE)
    replacement = rf"\1{value}"
    if pattern.search(text):
        return pattern.sub(replacement, text, count=1)
    return text


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def ensure_year(text: str, year: str) -> str:
    if not year or re.search(r"^year:\s*", text, re.MULTILINE):
        return text
    return re.sub(r"^(evidence_level:.*)$", rf"\1\nyear: {year}", text, count=1, flags=re.MULTILINE)


def replace_evidence_policy(text: str, check: CrossrefCheck) -> str:
    container = check.container or "not available"
    year = check.year or "not available"
    policy = "\n".join(
        [
            "evidence_policy:",
            "  quoted_fact:",
            f"    - {yaml_quote('Crossref metadata resolves this DOI and reports abstract availability for source scope checking.')}",
            f"    - {yaml_quote(f'Crossref container: {container}; year: {year}.')}",
            "  source_supported_conclusion:",
            f"    - {yaml_quote('This card is abstract-weighted only; it can guide navigation and extraction priority.')}",
            f"    - {yaml_quote('It must not support reader-facing clinical claims until a full abstract extraction or source worksheet is completed.')}",
            "  llm_inference:",
            f"    - {yaml_quote('High-reuse guideline, review, treatment-control, or risk-architecture sources remain candidates for deep extraction.')}",
        ]
    )
    pattern = re.compile(r"^evidence_policy:\n.*?(?=\n---\n)", re.MULTILINE | re.DOTALL)
    if pattern.search(text):
        return pattern.sub(policy, text, count=1)
    return text


def replace_evidence_depth_caveat(text: str) -> str:
    caveat = (
        "## Evidence-Depth Caveat\n\n"
        "This is a second-pass abstract-available source card. It verifies DOI metadata "
        "and Crossref abstract availability for source triage, but it is not a full "
        "abstract extraction or full-text read.\n"
    )
    pattern = re.compile(r"## Evidence-Depth Caveat\n\n.*?(?=\n## )", re.DOTALL)
    if pattern.search(text):
        return pattern.sub(caveat, text, count=1)
    return text


def upsert_source_check_section(text: str, check: CrossrefCheck) -> str:
    today = date.today().isoformat()
    section = [
        f"## Source Check, {today}",
        "",
        "Crossref metadata was checked as a repeatable second-pass intake step.",
        "",
        f"- DOI metadata resolved: {'yes' if check.found else 'no'}",
        f"- Container: {check.container or 'not available'}",
        f"- Year: {check.year or 'not available'}",
        f"- Abstract available in Crossref: {'yes' if check.abstract_available else 'no'}",
        "",
        "Use boundary:",
        "",
        "- This card may guide navigation and extraction priority.",
        "- It must not support reader-facing clinical claims until a full abstract extraction or source worksheet is completed.",
    ]
    if check.abstract_available:
        section.extend(
            [
                "",
                f"Abstract lead for scope check only: {short(check.abstract, 180)}",
            ]
        )
    section_text = "\n".join(section).rstrip() + "\n\n"
    old_section_re = re.compile(r"\n## Source Check, \d{4}-\d{2}-\d{2}\n.*?(?=\n## |\Z)", re.DOTALL)
    if old_section_re.search(text):
        return old_section_re.sub("\n" + section_text, text, count=1)
    marker = "\n## One-Line Summary\n"
    if marker in text:
        return text.replace(marker, "\n" + section_text + marker.lstrip(), 1)
    return text.rstrip() + "\n\n" + section_text


def update_card(check: CrossrefCheck) -> bool:
    if not check.abstract_available:
        return False
    text = check.source.path.read_text(encoding="utf-8")
    updated = replace_scalar_field(text, "verification_status", "abstract_weighted")
    updated = ensure_year(updated, check.year)
    updated = replace_evidence_policy(updated, check)
    updated = replace_evidence_depth_caveat(updated)
    updated = upsert_source_check_section(updated, check)
    if updated == text:
        return False
    check.source.path.write_text(updated, encoding="utf-8")
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--source-ids", help="Comma-separated source IDs to check.")
    parser.add_argument("--source-id-file", type=Path, help="Path with one source ID per line.")
    parser.add_argument(
        "--source-glob",
        action="append",
        default=[],
        help="Repo-relative glob for source cards, e.g. 'raw/papers/src-obesity-*.md'. Can be repeated.",
    )
    parser.add_argument(
        "--status",
        action="append",
        choices=["title_only", "abstract_weighted", "source_checked", "deep_extracted", "audited"],
        help="Only check cards currently at this verification_status. Can be repeated.",
    )
    parser.add_argument("--source-label", default="manual priority sample")
    parser.add_argument("--report-id", help="Stable frontmatter id for the generated report.")
    parser.add_argument("--out", type=Path, help="Write a Markdown report to this path.")
    parser.add_argument("--update-cards", action="store_true", help="Upgrade cards with Crossref abstracts to abstract_weighted.")
    parser.add_argument("--timeout", type=float, default=20.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    statuses = set(args.status) if args.status else None
    cards = selected_source_cards(repo_root, args.source_ids, args.source_id_file, args.source_glob, statuses)
    if not cards:
        print("No source cards selected.", file=sys.stderr)
        return 2
    checks = [check_source(card, args.timeout) for card in cards]
    report = render_report(checks, args.source_label, args.report_id)

    if args.out:
        out_path = args.out if args.out.is_absolute() else repo_root / args.out
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report, encoding="utf-8")
    else:
        sys.stdout.write(report)

    if args.update_cards:
        changed = [check.source.source_id for check in checks if update_card(check)]
        print(f"Updated {len(changed)} source cards: {', '.join(changed) if changed else 'none'}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
