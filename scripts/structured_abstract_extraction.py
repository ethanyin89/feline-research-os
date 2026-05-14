#!/usr/bin/env python3
"""Create conservative structured-abstract worksheets for selected source cards.

This is the Level 3 sample step after source metadata checks. It uses Crossref
abstract text when available, but it does not store full abstracts, write topic
claims, or promote cards beyond `abstract_weighted`.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from source_metadata_check import (
    CrossrefCheck,
    check_source,
    load_source_card,
    md_escape,
    selected_source_cards,
    short,
)


SECTION_LABELS = [
    "objective",
    "aim",
    "background",
    "animals",
    "methods",
    "procedures",
    "results",
    "conclusions",
    "clinical relevance",
    "practical relevance",
]

ENDPOINT_TERMS = [
    "insulin",
    "glucose",
    "remission",
    "survival",
    "quality of life",
    "safety",
    "effectiveness",
    "weight",
    "body condition",
    "obesity",
    "overweight",
    "risk factor",
    "pathology",
    "microbiota",
    "activity",
    "prevention",
]


@dataclass
class AbstractWorksheet:
    check: CrossrefCheck
    path: Path


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def detect_sections(abstract: str) -> list[str]:
    lower = abstract.casefold()
    return [label for label in SECTION_LABELS if re.search(rf"\b{re.escape(label)}\b", lower)]


def detect_endpoints(text: str) -> list[str]:
    lower = text.casefold()
    return [term for term in ENDPOINT_TERMS if term in lower]


def detect_population(abstract: str) -> str:
    match = re.search(r"\b(\d{1,4})\s+(?:client-owned\s+)?cats?\b", abstract, re.I)
    if match:
        return f"{match.group(1)} cats"
    match = re.search(r"\b(\d{1,4})\s+(?:client-owned\s+)?(?:diabetic|obese|overweight)\s+cats?\b", abstract, re.I)
    if match:
        return f"{match.group(1)} cats"
    if re.search(r"\bcats?\b", abstract, re.I):
        return "cats mentioned; count not mechanically extracted"
    return "not mechanically extracted"


def infer_source_family(title: str, abstract: str) -> str:
    combined = f"{title} {abstract}".casefold()
    if "guideline" in combined or "consensus" in combined:
        return "guideline / consensus"
    if "review" in combined:
        return "review"
    if "prospective" in combined or "study" in combined or "animals" in combined:
        return "original study"
    return "unclear from abstract metadata"


def abstract_scope_line(check: CrossrefCheck) -> str:
    sections = detect_sections(check.abstract)
    endpoints = detect_endpoints(f"{check.title} {check.abstract}")
    parts = [
        f"family={infer_source_family(check.title or check.source.title, check.abstract)}",
        f"population={detect_population(check.abstract)}",
    ]
    if sections:
        parts.append("sections=" + ", ".join(sections[:8]))
    if endpoints:
        parts.append("signals=" + ", ".join(endpoints[:8]))
    return "; ".join(parts)


def render_worksheet(check: CrossrefCheck) -> str:
    today = date.today().isoformat()
    source_id = check.source.source_id
    title = check.title or check.source.title
    sections = detect_sections(check.abstract)
    endpoints = detect_endpoints(f"{title} {check.abstract}")
    family = infer_source_family(title, check.abstract)
    population = detect_population(check.abstract)
    abstract_lead = short(check.abstract, 120)

    return f"""---
id: {source_id}-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [{source_id}]
language: zh
last_compiled_at: {today}
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# {source_id} Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref metadata and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `{source_id}` |
| Title | {md_escape(title)} |
| DOI | `{check.source.doi}` |
| Container | {md_escape(check.container)} |
| Year | {check.year} |
| Current card status | `{check.source.verification_status}` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | {md_escape(family)} |
| Population / sample signal | {md_escape(population)} |
| Detected section labels | {md_escape(", ".join(sections) if sections else "none mechanically detected")} |
| Endpoint / theme signals | {md_escape(", ".join(endpoints) if endpoints else "none mechanically detected")} |

Short abstract lead for scope check only:

> {md_escape(abstract_lead)}

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: {md_escape(", ".join(endpoints[:5]) if endpoints else "needs human source review")}
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
"""


def render_index(worksheets: list[AbstractWorksheet], source_label: str, index_id: str | None = None) -> str:
    today = date.today().isoformat()
    stable_id = index_id or f"feline-structured-abstract-sample-{today.replace('-', '')}"
    lines = [
        "---",
        f"id: {stable_id}",
        "type: system",
        "topic: content-pipeline",
        "question_type: structured-abstract-index",
        "language: zh",
        f"last_compiled_at: {today}",
        "verification_status: compiled",
        "decision_grade: no",
        "owner: codex",
        "status: active",
        "---",
        "",
        f"# Feline Structured Abstract Index, {today}",
        "",
        f"Source set: `{source_label}`",
        "",
        "## Rule",
        "",
        "This is a structured abstract worksheet run after source-check. It creates abstract-only worksheets, not full-text deep extractions.",
        "",
        "## Sample Table",
        "",
        "| Source | Worksheet | Metadata |",
        "|---|---|---|",
    ]
    for worksheet in worksheets:
        check = worksheet.check
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{check.source.source_id}`",
                    f"[{worksheet.path.name}]({worksheet.path.name})",
                    md_escape(abstract_scope_line(check)),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- Cards remain `abstract_weighted` unless a later full-text/deep-extraction pass changes them.",
            "- This index can guide branch placement and extraction priority.",
            "- No topic pages should be updated from this sample alone.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--source-ids", help="Comma-separated source IDs.")
    parser.add_argument("--source-id-file", type=Path, help="Path with one source ID per line.")
    parser.add_argument(
        "--source-glob",
        action="append",
        default=[],
        help="Repo-relative glob for source cards. Can be repeated.",
    )
    parser.add_argument(
        "--status",
        action="append",
        choices=["title_only", "abstract_weighted", "source_checked", "deep_extracted", "audited"],
        help="Only select cards currently at this verification_status. Can be repeated.",
    )
    parser.add_argument("--source-label", default="manual structured abstract sample")
    parser.add_argument("--index-id", help="Stable frontmatter id for the generated index.")
    parser.add_argument("--out-dir", type=Path, default=Path("system/indexes"))
    parser.add_argument("--index-out", type=Path, help="Optional sample index path.")
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    out_dir = args.out_dir if args.out_dir.is_absolute() else repo_root / args.out_dir
    statuses = set(args.status) if args.status else None
    if args.source_ids or args.source_id_file or args.source_glob:
        cards = selected_source_cards(repo_root, args.source_ids, args.source_id_file, args.source_glob, statuses)
    else:
        print("No source cards selected.", file=sys.stderr)
        return 2
    worksheets: list[AbstractWorksheet] = []

    for card in cards:
        check = check_source(card, args.timeout)
        if not check.abstract_available:
            reason = check.error or "no Crossref abstract available"
            print(f"Skipping {card.source_id}: {reason}", file=sys.stderr)
            continue
        path = out_dir / f"{card.source_id}-structured-abstract-round1.md"
        worksheets.append(AbstractWorksheet(check=check, path=path))
        if args.write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(render_worksheet(check), encoding="utf-8")

    if args.index_out:
        index_path = args.index_out if args.index_out.is_absolute() else repo_root / args.index_out
        if args.write:
            index_path.parent.mkdir(parents=True, exist_ok=True)
            index_path.write_text(render_index(worksheets, args.source_label, args.index_id), encoding="utf-8")
        else:
            sys.stdout.write(render_index(worksheets, args.source_label, args.index_id))
    elif not args.write:
        sys.stdout.write(render_index(worksheets, args.source_label, args.index_id))

    print(f"Planned {len(worksheets)} structured abstract worksheets.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
