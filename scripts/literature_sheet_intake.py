#!/usr/bin/env python3
"""Build a reviewable literature intake manifest from a two-column CSV.

The script intentionally stops at classification. It does not create source cards.
That keeps sheet intake reviewable before evidence-bearing files are written.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path


DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>]+", re.IGNORECASE)


@dataclass
class ExistingSource:
    source_id: str
    title: str
    doi: str
    path: Path


@dataclass
class IntakeRow:
    sheet_row: int
    title: str
    locator: str
    normalized_doi: str
    segment: str
    classification: str
    matched_source_id: str
    note: str


def normalize_title(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().rstrip(".")).casefold()


def normalize_doi(value: str) -> str:
    match = DOI_RE.search(value.strip())
    if not match:
        return ""
    return match.group(0).rstrip(".,;)").casefold()


def parse_frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*\"?([^\"\n]+)\"?\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def load_existing_sources(repo_root: Path) -> list[ExistingSource]:
    sources: list[ExistingSource] = []
    for path in sorted((repo_root / "raw").glob("**/src-*.md")):
        text = path.read_text(encoding="utf-8")
        source_id = parse_frontmatter_value(text, "id") or path.stem
        title = parse_frontmatter_value(text, "title")
        doi = normalize_doi(parse_frontmatter_value(text, "doi"))
        if not doi:
            doi = normalize_doi(text)
        sources.append(ExistingSource(source_id=source_id, title=title, doi=doi, path=path))
    return sources


def read_sheet_rows(csv_path: Path) -> list[tuple[int, str, str]]:
    rows: list[tuple[int, str, str]] = []
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        for index, row in enumerate(reader, start=1):
            title = row[0].strip() if len(row) > 0 else ""
            locator = row[1].strip() if len(row) > 1 else ""
            if not title and not locator:
                continue
            rows.append((index, title, locator))
    return rows


def segment_for_row(
    sheet_row: int,
    title: str,
    obesity_marker_row: int | None,
    default_segment: str,
) -> str:
    if default_segment:
        return default_segment
    if title.strip().casefold() == "feline obesity":
        return "section-label"
    if obesity_marker_row is not None and sheet_row > obesity_marker_row:
        return "obesity"
    return "diabetes"


def classify_rows(
    sheet_rows: list[tuple[int, str, str]],
    existing_sources: list[ExistingSource],
    default_segment: str = "",
    section_labels: set[str] | None = None,
    exclude_title_patterns: list[re.Pattern[str]] | None = None,
) -> list[IntakeRow]:
    by_doi = {source.doi: source for source in existing_sources if source.doi}
    by_title = {normalize_title(source.title): source for source in existing_sources if source.title}
    seen_dois: Counter[str] = Counter()
    seen_titles: Counter[str] = Counter()
    obesity_marker = next(
        (sheet_row for sheet_row, title, _ in sheet_rows if title.strip().casefold() == "feline obesity"),
        None,
    )
    section_labels = section_labels or {"feline obesity"}
    exclude_title_patterns = exclude_title_patterns or []

    classified: list[IntakeRow] = []
    for sheet_row, title, locator in sheet_rows:
        norm_title = normalize_title(title)
        doi = normalize_doi(locator)
        segment = segment_for_row(sheet_row, title, obesity_marker, default_segment)
        is_section_label = title.strip().casefold() in section_labels
        is_excluded = any(pattern.search(title) for pattern in exclude_title_patterns)
        matched = by_doi.get(doi) if doi else None
        if matched is None and norm_title:
            matched = by_title.get(norm_title)

        if is_section_label:
            segment = "section-label"
            classification = "section-label"
            note = "Section marker, not a source."
        elif is_excluded:
            classification = "out-of-scope"
            note = "Excluded by title pattern before source-card creation."
        elif not locator.strip():
            classification = "incomplete-locator"
            note = "Title-only row; recover URL, DOI, PubMed ID, or other locator before source-card creation."
        elif matched is not None:
            classification = "existing"
            if segment != "section-label" and f"-{segment}-" not in matched.source_id:
                classification = "shared-existing"
            note = f"Matches existing {matched.source_id}."
        elif doi and seen_dois[doi] > 0:
            classification = "duplicate-in-sheet"
            note = "Same normalized DOI appeared earlier in this sheet."
        elif not doi and norm_title and seen_titles[norm_title] > 0:
            classification = "duplicate-in-sheet"
            note = "Same normalized title appeared earlier in this sheet."
        elif segment == "obesity":
            classification = "new-obesity"
            note = "Candidate for obesity source index."
        elif segment == "diabetes":
            classification = "new-diabetes"
            note = "Candidate for extended diabetes source index."
        else:
            classification = f"new-{segment}"
            note = f"Candidate for {segment} source index."

        classified.append(
            IntakeRow(
                sheet_row=sheet_row,
                title=title,
                locator=locator,
                normalized_doi=doi,
                segment=segment,
                classification=classification,
                matched_source_id=matched.source_id if matched else "",
                note=note,
            )
        )
        if doi:
            seen_dois[doi] += 1
        elif norm_title:
            seen_titles[norm_title] += 1
    return classified


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render_manifest(rows: list[IntakeRow], source_label: str, manifest_id: str = "") -> str:
    counts = Counter(row.classification for row in rows)
    segment_counts = Counter(row.segment for row in rows)
    today = date.today().isoformat()
    manifest_id = manifest_id or f"feline-literature-intake-manifest-{today.replace('-', '')}"

    lines = [
        "---",
        f"id: {manifest_id}",
        "type: system",
        "topic: content-pipeline",
        "question_type: intake-manifest",
        "language: zh",
        f"last_compiled_at: {today}",
        "verification_status: generated",
        "decision_grade: no",
        "owner: codex",
        "status: pending-review",
        "---",
        "",
        f"# Feline Literature Intake Manifest, {today}",
        "",
        f"Source: `{source_label}`",
        "",
        "## Summary",
        "",
        f"- Rows classified: `{len(rows)}`",
    ]
    for key, value in sorted(segment_counts.items()):
        lines.append(f"- {key.title()} segment rows: `{value}`")
    lines.extend(
        [
            "",
        "| Classification | Count |",
        "|---|---:|",
        ]
    )
    for key, value in sorted(counts.items()):
        lines.append(f"| `{key}` | {value} |")

    lines.extend(
        [
            "",
            "## Intake Table",
            "",
            "| Row | Segment | Classification | Existing ID | Normalized DOI | Title | Locator | Note |",
            "|---:|---|---|---|---|---|---|---|",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row.sheet_row),
                    f"`{row.segment}`",
                    f"`{row.classification}`",
                    f"`{row.matched_source_id}`" if row.matched_source_id else "",
                    f"`{row.normalized_doi}`" if row.normalized_doi else "",
                    markdown_escape(row.title),
                    markdown_escape(row.locator),
                    markdown_escape(row.note),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Use",
            "",
            "- Review `new-*` and `shared-existing` rows before creating source cards.",
            "- Do not deep-extract every row by default.",
            "- Promote only guideline, broad review, backbone mechanism, treatment-control, or high-reuse boundary sources.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", required=True, type=Path, help="Two-column CSV exported from Google Sheets.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Repository root.")
    parser.add_argument("--out", type=Path, help="Manifest markdown path. Defaults to stdout.")
    parser.add_argument("--source-label", default="", help="Human-readable sheet/source label.")
    parser.add_argument(
        "--segment",
        default="",
        help="Treat every non-section row as this disease/topic segment, e.g. fcv or cancer.",
    )
    parser.add_argument(
        "--section-label",
        action="append",
        default=[],
        help="Title value that should be treated as a section label instead of a source. May repeat.",
    )
    parser.add_argument("--manifest-id", default="", help="Stable id to write in the manifest frontmatter.")
    parser.add_argument(
        "--exclude-title-regex",
        action="append",
        default=[],
        help="Regex for titles that should be classified out-of-scope before card creation. May repeat.",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    section_labels = {"feline obesity", *[value.casefold() for value in args.section_label]}
    exclude_title_patterns = [re.compile(value, re.IGNORECASE) for value in args.exclude_title_regex]
    rows = classify_rows(
        read_sheet_rows(args.csv),
        load_existing_sources(repo_root),
        default_segment=args.segment.strip().casefold(),
        section_labels=section_labels,
        exclude_title_patterns=exclude_title_patterns,
    )
    manifest = render_manifest(rows, args.source_label or str(args.csv), args.manifest_id)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(manifest, encoding="utf-8")
    else:
        print(manifest, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
