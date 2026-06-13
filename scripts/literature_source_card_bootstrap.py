#!/usr/bin/env python3
"""Bootstrap conservative first-pass source cards from a literature sheet CSV.

This is the write step after `literature_sheet_intake.py`.
It only writes title/locator-level cards for rows classified as new sources.
It does not deep-extract, compile topic claims, or promote reader-facing content.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from literature_sheet_intake import (
    IntakeRow,
    classify_rows,
    load_existing_sources,
    normalize_doi,
    read_sheet_rows,
)


DISEASE_CONFIG = {
    "new-ckd": {
        "prefix": "src-ckd",
        "disease": "CKD",
        "topic": "ckd",
    },
    "new-diabetes": {
        "prefix": "src-diabetes",
        "disease": "diabetes mellitus",
        "topic": "diabetes",
    },
    "new-obesity": {
        "prefix": "src-obesity",
        "disease": "obesity",
        "topic": "obesity",
    },
    "new-fcv": {
        "prefix": "src-fcv",
        "disease": "feline calicivirus",
        "topic": "fcv",
    },
    "new-cancer": {
        "prefix": "src-cancer",
        "disease": "cancer",
        "topic": "cancer",
    },
    "new-fip": {
        "prefix": "src-fip",
        "disease": "FIP",
        "topic": "fip",
    },
    "new-hcm": {
        "prefix": "src-hcm",
        "disease": "HCM",
        "topic": "hcm",
    },
    "new-ibd": {
        "prefix": "src-ibd",
        "disease": "IBD",
        "topic": "ibd",
    },
}


@dataclass
class PlannedCard:
    row: IntakeRow
    source_id: str
    path: Path


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def slug_tags(title: str, topic: str) -> list[str]:
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9-]{2,}", title.lower())
    stop = {
        "and",
        "the",
        "for",
        "with",
        "from",
        "into",
        "cats",
        "feline",
        "canine",
        "diabetes",
        "mellitus",
        "ckd",
        "kidney",
        "renal",
        "chronic",
        "disease",
        "obesity",
        "cancer",
        "tumor",
        "tumour",
        "tumors",
        "tumours",
    }
    tags = [topic]
    for word in words:
        cleaned = word.strip("-")
        if cleaned and cleaned not in stop and cleaned not in tags:
            tags.append(cleaned)
        if len(tags) >= 8:
            break
    return tags


def evidence_level_from_title(title: str) -> str:
    lower = title.casefold()
    if "guideline" in lower or "consensus" in lower:
        return "guideline"
    if (
        "review" in lower
        or "what do we know" in lower
        or "current information" in lower
        or "comparative oncology" in lower
        or "molecular mechanisms" in lower
        or "virotherapy" in lower
    ):
        return "review"
    if "case report" in lower or " cases" in lower:
        return "case-series"
    return "original-study"


def next_number_by_prefix(repo_root: Path, prefix: str) -> int:
    pattern = re.compile(rf"^{re.escape(prefix)}-(\d+)\.md$")
    highest = 0
    for path in (repo_root / "raw" / "papers").glob(f"{prefix}-*.md"):
        match = pattern.match(path.name)
        if match:
            highest = max(highest, int(match.group(1)))
    return highest + 1


def selected_rows(rows: list[IntakeRow], row_numbers: set[int] | None, limit: int | None) -> list[IntakeRow]:
    candidates = [row for row in rows if row.classification in DISEASE_CONFIG]
    if row_numbers is not None:
        candidates = [row for row in candidates if row.sheet_row in row_numbers]
    if limit is not None:
        candidates = candidates[:limit]
    return candidates


def plan_cards(repo_root: Path, rows: list[IntakeRow]) -> list[PlannedCard]:
    next_numbers = {
        config["prefix"]: next_number_by_prefix(repo_root, config["prefix"])
        for config in DISEASE_CONFIG.values()
    }
    planned: list[PlannedCard] = []
    for row in rows:
        config = DISEASE_CONFIG[row.classification]
        prefix = config["prefix"]
        source_id = f"{prefix}-{next_numbers[prefix]:03d}"
        next_numbers[prefix] += 1
        planned.append(
            PlannedCard(
                row=row,
                source_id=source_id,
                path=repo_root / "raw" / "papers" / f"{source_id}.md",
            )
        )
    return planned


def locator_fields(row: IntakeRow) -> tuple[str, str]:
    doi = row.normalized_doi or normalize_doi(row.locator)
    if doi:
        return doi, f"https://doi.org/{doi}"
    return "", row.locator


def render_card(card: PlannedCard) -> str:
    row = card.row
    config = DISEASE_CONFIG[row.classification]
    doi, url = locator_fields(row)
    title = row.title.strip().rstrip(".")
    topic = config["topic"]
    tags = slug_tags(title, topic)
    evidence_level = evidence_level_from_title(title)
    locator_read = doi or url or row.locator

    return f"""---
id: {card.source_id}
type: source
title: {yaml_quote(title)}
source_kind: paper
species: feline
diseases: [{config["disease"]}]
models: []
endpoints: []
jurisdictions: []
evidence_level: {evidence_level}
status: ingested
extraction_depth: partial
verification_status: title_only
decision_grade: no
language_qa_status: not_applicable
tags: [{", ".join(tags)}]
links:
  doi: {yaml_quote(doi) if doi else '""'}
  url: {yaml_quote(url) if url else '""'}
  local_assets: []
evidence_policy:
  quoted_fact:
    - {yaml_quote(f"The intake sheet lists this title: {title}.")}
    - {yaml_quote(f"The intake sheet locator is: {locator_read}.")}
  source_supported_conclusion:
    - {yaml_quote("This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims.")}
  llm_inference:
    - {yaml_quote("The likely claim-fit must be checked against the abstract or full text before promotion.")}
---

# {title}

## Evidence-Depth Caveat

This is a first-pass title-and-locator source card created from the reviewed literature intake manifest. It verifies that the reference has an owner in the vault, but it does not extract reusable clinical facts from the article body.

## One-Line Summary

Candidate {topic} source from sheet row {row.sheet_row}. Use it for triage until abstract or full-text extraction proves a stronger role.

## Why It Matters For Feline {topic.title()}

This source was included in a reviewed feline literature intake sheet and classified as `{row.classification}` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: {title}.
- The intake sheet locator is: {locator_read}.

### source_supported_conclusion

- This is a first-pass source-card placeholder for triage and queue control.
- It should not support prevalence, diagnostic, treatment, management, or risk-ranking claims yet.

### llm_inference

- The title suggests a possible `{topic}` role, but the actual claim-fit requires abstract or full-text review.

## Claim-Fit Judgment

Strongest safe use:

- intake ownership
- source queue placement
- deduplication and future extraction planning

Must not control yet:

- reader-facing medical advice
- numeric claims
- comparative ranking
- guideline-like recommendations
- mechanism closure

## Image Asset TODO

- figures to capture: unknown until source text is read
- why these matter: tables or figures should remain behind the candidate gate until labels are verified

## Open Follow-Up Questions

- What source family is confirmed by the abstract or article body?
- Which claims, if any, are reusable for the {topic} module?
- Does this source deserve deep extraction, or should it remain queue context?
- Are there tables or figures that change the module structure?

## Linked Entities

- diseases: {config["disease"]}
- models:
- endpoints:
- mechanisms:
- regulations:
"""


def parse_row_numbers(value: str) -> set[int] | None:
    if not value:
        return None
    return {int(part.strip()) for part in value.split(",") if part.strip()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", required=True, type=Path, help="Two-column CSV exported from Google Sheets.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Repository root.")
    parser.add_argument("--rows", default="", help="Comma-separated sheet row numbers to plan/write.")
    parser.add_argument("--limit", type=int, help="Only plan/write the first N new rows after filtering.")
    parser.add_argument(
        "--segment",
        default="",
        help="Treat every non-section row as this disease/topic segment, e.g. fcv or cancer.",
    )
    parser.add_argument(
        "--exclude-title-regex",
        action="append",
        default=[],
        help="Regex for titles that should be classified out-of-scope before card creation. May repeat.",
    )
    parser.add_argument("--write", action="store_true", help="Write source cards. Default is dry-run.")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    rows = classify_rows(
        read_sheet_rows(args.csv),
        load_existing_sources(repo_root),
        default_segment=args.segment.strip().casefold(),
        exclude_title_patterns=[re.compile(value, re.IGNORECASE) for value in args.exclude_title_regex],
    )
    chosen = selected_rows(rows, parse_row_numbers(args.rows), args.limit)
    planned = plan_cards(repo_root, chosen)

    print("| Row | Classification | Source ID | Path | Title |")
    print("|---:|---|---|---|---|")
    for card in planned:
        rel = card.path.relative_to(repo_root)
        print(
            f"| {card.row.sheet_row} | `{card.row.classification}` | `{card.source_id}` | "
            f"`{rel}` | {card.row.title.replace('|', '\\|')} |"
        )

    if args.write:
        for card in planned:
            if card.path.exists():
                raise FileExistsError(f"Refusing to overwrite existing source card: {card.path}")
            card.path.write_text(render_card(card), encoding="utf-8")
        print(f"\nWrote {len(planned)} source cards.")
    else:
        print(f"\nDry run only. Planned {len(planned)} source cards.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
