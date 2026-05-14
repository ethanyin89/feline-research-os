#!/usr/bin/env python3
"""Check full-text availability signals for selected source cards.

This is a conservative pre-deep-extraction step. It uses Crossref metadata to
find DOI landing pages, license metadata, and publisher-provided full-text/TDM
links. It does not download articles or promote any source-card status.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from source_metadata_check import (
    SourceCard,
    fetch_crossref,
    first_value,
    issued_year,
    md_escape,
    selected_source_cards,
    short,
)


@dataclass
class AvailabilityCheck:
    source: SourceCard
    found: bool
    title: str = ""
    year: str = ""
    container: str = ""
    doi_url: str = ""
    primary_url: str = ""
    links: list[str] | None = None
    licenses: list[str] | None = None
    probes: list[str] | None = None
    has_abstract: bool = False
    error: str = ""

    @property
    def fulltext_link_count(self) -> int:
        return len(self.links or [])

    @property
    def license_count(self) -> int:
        return len(self.licenses or [])

    @property
    def accessible_probe_count(self) -> int:
        return sum(1 for probe in self.probes or [] if re.search(r"\b(?:200|301|302|303|307|308)\b", probe))

    @property
    def recommendation(self) -> str:
        if not self.found:
            return "metadata failed; manual lookup required"
        if self.fulltext_link_count:
            return "full-text/TDM link present; verify access before deep extraction"
        if self.license_count:
            return "license metadata present; inspect DOI landing page manually"
        return "no Crossref full-text signal; manual access needed"


def unique(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        value = value.strip()
        if value and value not in seen:
            result.append(value)
            seen.add(value)
    return result


def crossref_message(source: SourceCard, timeout: float) -> tuple[dict[str, object] | None, str]:
    if not source.doi:
        return None, "no DOI in source card"
    try:
        payload = fetch_crossref(source.doi, timeout=timeout)
    except Exception as exc:  # noqa: BLE001 - command-line report should preserve fetch error.
        return None, str(exc)
    message = payload.get("message")
    if not isinstance(message, dict):
        return None, "missing Crossref message"
    return message, ""


def extract_links(message: dict[str, object]) -> list[str]:
    raw_links = message.get("link")
    if not isinstance(raw_links, list):
        return []
    rendered: list[str] = []
    for item in raw_links:
        if not isinstance(item, dict):
            continue
        url = str(item.get("URL", "")).strip()
        content_type = str(item.get("content-type", "")).strip()
        application = str(item.get("intended-application", "")).strip()
        if not url:
            continue
        label = ", ".join(part for part in [content_type, application] if part)
        rendered.append(f"{url} ({label})" if label else url)
    return unique(rendered)


def extract_licenses(message: dict[str, object]) -> list[str]:
    raw_licenses = message.get("license")
    if not isinstance(raw_licenses, list):
        return []
    rendered: list[str] = []
    for item in raw_licenses:
        if isinstance(item, dict):
            url = str(item.get("URL", "")).strip()
            if url:
                rendered.append(url)
    return unique(rendered)


def primary_url(message: dict[str, object]) -> str:
    resource = message.get("resource")
    if isinstance(resource, dict):
        primary = resource.get("primary")
        if isinstance(primary, dict):
            url = primary.get("URL")
            if isinstance(url, str):
                return url
    url = message.get("URL")
    return url if isinstance(url, str) else ""


def probe_url(url: str, timeout: float) -> str:
    request = urllib.request.Request(
        url,
        method="HEAD",
        headers={"User-Agent": "feline-research-os-availability-check/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            content_type = response.headers.get("content-type", "")
            content_length = response.headers.get("content-length", "")
            meta = ", ".join(part for part in [content_type, f"len={content_length}" if content_length else ""] if part)
            return f"{url} -> {response.status}" + (f" ({meta})" if meta else "")
    except urllib.error.HTTPError as exc:
        return f"{url} -> HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001 - report should preserve network/protocol failures.
        return f"{url} -> {type(exc).__name__}: {exc}"


def link_url(rendered_link: str) -> str:
    return rendered_link.split(" (", 1)[0].strip()


def check_availability(source: SourceCard, timeout: float, probe_links: bool, probe_limit: int) -> AvailabilityCheck:
    message, error = crossref_message(source, timeout)
    if message is None:
        return AvailabilityCheck(source=source, found=False, error=error)
    links = extract_links(message)
    probes: list[str] = []
    if probe_links:
        for rendered_link in links[:probe_limit]:
            probes.append(probe_url(link_url(rendered_link), timeout))

    return AvailabilityCheck(
        source=source,
        found=True,
        title=first_value(message.get("title")) or source.title,
        year=issued_year(message),
        container=first_value(message.get("container-title")),
        doi_url=str(message.get("URL", "")) or f"https://doi.org/{source.doi}",
        primary_url=primary_url(message),
        links=links,
        licenses=extract_licenses(message),
        probes=probes,
        has_abstract=bool(str(message.get("abstract", "")).strip()),
    )


def inline_list(values: list[str] | None, limit: int = 2) -> str:
    values = values or []
    if not values:
        return ""
    clipped = [short(value, 90) for value in values[:limit]]
    suffix = f"; +{len(values) - limit} more" if len(values) > limit else ""
    return md_escape("; ".join(clipped) + suffix)


def render_report(checks: list[AvailabilityCheck], source_label: str, report_id: str | None) -> str:
    today = date.today().isoformat()
    stable_id = report_id or f"feline-fulltext-availability-{today.replace('-', '')}"
    lines = [
        "---",
        f"id: {stable_id}",
        "type: system",
        "topic: content-pipeline",
        "question_type: fulltext-availability-check",
        "language: zh",
        f"last_compiled_at: {today}",
        "verification_status: generated",
        "decision_grade: no",
        "owner: codex",
        "status: active",
        "---",
        "",
        f"# Feline Full-Text Availability Check, {today}",
        "",
        f"Source set: `{source_label}`",
        "",
        "## Rule",
        "",
        "This report checks full-text availability signals before deep extraction. It does not download articles, create clinical claims, or promote source-card status.",
        "",
        "## Summary",
        "",
        f"- Cards checked: `{len(checks)}`",
        f"- Crossref metadata found: `{sum(1 for check in checks if check.found)}`",
        f"- With Crossref full-text/TDM links: `{sum(1 for check in checks if check.fulltext_link_count)}`",
        f"- With license metadata: `{sum(1 for check in checks if check.license_count)}`",
        f"- With reachable HEAD probes: `{sum(1 for check in checks if check.accessible_probe_count)}`",
        f"- With Crossref abstracts: `{sum(1 for check in checks if check.has_abstract)}`",
        "",
        "## Availability Table",
        "",
        "| Source | Status | DOI | Abstract | Links | License | Reachable Probe | Recommendation |",
        "|---|---|---|---|---:|---:|---:|---|",
    ]
    for check in checks:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{check.source.source_id}`",
                    f"`{check.source.verification_status}`",
                    f"`{check.source.doi}`" if check.source.doi else "",
                    "`yes`" if check.has_abstract else "`no`",
                    str(check.fulltext_link_count),
                    str(check.license_count),
                    str(check.accessible_probe_count),
                    md_escape(check.recommendation),
                ]
            )
            + " |"
        )

    lines.extend(["", "## Link Detail", ""])
    for check in checks:
        lines.append(f"### `{check.source.source_id}`")
        if check.error:
            lines.append("")
            lines.append(f"- Error: {md_escape(check.error)}")
        lines.extend(
            [
                "",
                f"- Title: {md_escape(check.title or check.source.title)}",
                f"- Container/year: {md_escape(check.container)} / {check.year}",
                f"- DOI landing: {md_escape(check.doi_url)}",
                f"- Primary URL: {md_escape(check.primary_url)}",
                f"- Full-text/TDM links: {inline_list(check.links) or 'none in Crossref metadata'}",
                f"- License URLs: {inline_list(check.licenses) or 'none in Crossref metadata'}",
                f"- HEAD probes: {inline_list(check.probes, limit=3) or 'not run'}",
                f"- Next action: {md_escape(check.recommendation)}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--source-ids", help="Comma-separated source IDs.")
    parser.add_argument("--source-id-file", type=Path)
    parser.add_argument("--source-glob", action="append", default=[])
    parser.add_argument(
        "--status",
        action="append",
        choices=["title_only", "abstract_weighted", "source_checked", "deep_extracted", "audited"],
    )
    parser.add_argument("--source-label", default="manual full-text availability check")
    parser.add_argument("--report-id")
    parser.add_argument("--out", type=Path)
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--probe-links", action="store_true", help="HEAD-check the first Crossref full-text/TDM links.")
    parser.add_argument("--probe-limit", type=int, default=2)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    statuses = set(args.status) if args.status else None
    cards = selected_source_cards(repo_root, args.source_ids, args.source_id_file, args.source_glob, statuses)
    if not cards:
        print("No source cards selected.", file=sys.stderr)
        return 2

    checks = [check_availability(card, args.timeout, args.probe_links, args.probe_limit) for card in cards]
    report = render_report(checks, args.source_label, args.report_id)
    if args.out:
        out_path = args.out if args.out.is_absolute() else repo_root / args.out
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report, encoding="utf-8")
    else:
        sys.stdout.write(report)

    print(f"Checked {len(checks)} source cards.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
