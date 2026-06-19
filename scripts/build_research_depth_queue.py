#!/usr/bin/env python3
"""Build a cross-disease queue of source cards needing deeper extraction."""

from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from research_mode import (  # noqa: E402
    SourceCard,
    _is_placeholder_content,
    is_research_ready_source,
    load_disease_sources,
    rank_depth_queue_sources,
)


DISEASES = ["ckd", "hcm", "fip", "diabetes", "ibd", "obesity", "fcv", "cancer"]


def reason_for(card: SourceCard) -> str:
    status = (card.status or "").strip()
    verification = (card.verification_status or "").strip()
    reasons: list[str] = []
    if verification:
        reasons.append(f"verification_status={verification}")
    if status:
        reasons.append(f"status={status}")
    if not card.supported_conclusions and not card.quoted_facts:
        reasons.append("missing extracted claim fields")
    if not card.one_line_summary:
        reasons.append("missing one-line summary")
    combined_text = " ".join([
        card.one_line_summary or "",
        *(card.quoted_facts or []),
        *(card.supported_conclusions or []),
        *(card.llm_inferences or []),
    ])
    if _is_placeholder_content(combined_text):
        reasons.append("placeholder or first-pass triage text present")
    if not reasons:
        reasons.append("not research-ready")
    return "; ".join(reasons)


def row_for(disease: str, rank: int, card: SourceCard) -> dict[str, str]:
    return {
        "disease": disease,
        "rank": str(rank),
        "source_id": card.id,
        "title": card.title,
        "year": str(card.year or ""),
        "journal": card.journal or "",
        "doi": card.doi or "",
        "pmid": card.pmid or "",
        "status": card.status or "",
        "verification_status": card.verification_status or "",
        "reason": reason_for(card),
    }


def build_rows(per_disease: int) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for disease in DISEASES:
        cards = load_disease_sources(disease)
        queue = rank_depth_queue_sources(cards, top_n=per_disease)
        for rank, card in enumerate(queue, 1):
            if is_research_ready_source(card):
                continue
            rows.append(row_for(disease, rank, card))
    return rows


def write_csv(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "disease",
        "rank",
        "source_id",
        "title",
        "year",
        "journal",
        "doi",
        "pmid",
        "status",
        "verification_status",
        "reason",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Research Depth Queue",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "These records should not be treated as reader-facing evidence until abstract/full-text extraction is completed.",
        "",
    ]
    by_disease: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_disease.setdefault(row["disease"], []).append(row)
    for disease in DISEASES:
        disease_rows = by_disease.get(disease, [])
        if not disease_rows:
            continue
        lines.extend([f"## {disease.upper()}", ""])
        for row in disease_rows:
            locator = row["doi"] or (f"PMID {row['pmid']}" if row["pmid"] else "no DOI/PMID")
            lines.append(
                f"{row['rank']}. `{row['source_id']}` {row['title']} ({row['year'] or 'undated'})"
            )
            lines.append(f"   - Locator: {locator}")
            lines.append(f"   - Reason: {row['reason']}")
        lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--per-disease", type=int, default=10)
    parser.add_argument(
        "--csv",
        default="system/indexes/research-depth-queue.csv",
        help="Output CSV path",
    )
    parser.add_argument(
        "--md",
        default="system/indexes/research-depth-queue.md",
        help="Output Markdown path",
    )
    args = parser.parse_args()

    rows = build_rows(max(1, args.per_disease))
    write_csv(rows, ROOT / args.csv)
    write_markdown(rows, ROOT / args.md)
    print(f"Wrote {len(rows)} queue rows")
    print(args.csv)
    print(args.md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
