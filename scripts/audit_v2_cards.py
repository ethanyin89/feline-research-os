#!/usr/bin/env python3
"""
scripts/audit_v2_cards.py
Audit V2 field quality across the source card corpus.

Usage:
    python3 scripts/audit_v2_cards.py                    # Full audit summary
    python3 scripts/audit_v2_cards.py --sample 50        # Stratified sample for manual review
    python3 scripts/audit_v2_cards.py --disease hcm      # Audit single disease
    python3 scripts/audit_v2_cards.py --problems         # Show only C/F grade cards
    python3 scripts/audit_v2_cards.py --json             # JSON output
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

SCRIPTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from v2_quality_gates import (
    extract_v2_fields_from_file,
    grade_v2_extraction,
    V2QualityReport,
)

DISEASES = ["ckd", "fip", "hcm", "ibd", "diabetes", "fcv", "obesity", "cancer"]


@dataclass
class CardAuditResult:
    """Audit result for a single card."""
    path: Path
    source_id: str
    disease: str
    evidence_level: str
    has_v2_fields: bool
    report: Optional[V2QualityReport] = None

    @property
    def overall_grade(self) -> str:
        if not self.has_v2_fields:
            return "N/A"
        return self.report.overall_grade if self.report else "N/A"

    def to_dict(self) -> dict:
        result = {
            "path": str(self.path.relative_to(PROJECT_ROOT)),
            "source_id": self.source_id,
            "disease": self.disease,
            "evidence_level": self.evidence_level,
            "has_v2_fields": self.has_v2_fields,
            "overall_grade": self.overall_grade,
        }
        if self.report:
            result["report"] = self.report.to_dict()
        return result


@dataclass
class DiseaseAuditSummary:
    """Summary for a single disease."""
    disease: str
    total_cards: int
    cards_with_v2: int
    grade_counts: dict[str, int] = field(default_factory=dict)
    score_distribution: list[int] = field(default_factory=list)

    @property
    def coverage_pct(self) -> float:
        return (self.cards_with_v2 / self.total_cards * 100) if self.total_cards else 0

    @property
    def avg_score(self) -> float:
        return sum(self.score_distribution) / len(self.score_distribution) if self.score_distribution else 0

    def to_dict(self) -> dict:
        return {
            "disease": self.disease,
            "total_cards": self.total_cards,
            "cards_with_v2": self.cards_with_v2,
            "coverage_pct": round(self.coverage_pct, 1),
            "avg_score": round(self.avg_score, 2),
            "grade_counts": self.grade_counts,
        }


@dataclass
class AuditReport:
    """Full audit report."""
    card_results: list[CardAuditResult] = field(default_factory=list)
    disease_summaries: dict[str, DiseaseAuditSummary] = field(default_factory=dict)
    total_cards: int = 0
    total_with_v2: int = 0
    overall_grade_counts: dict[str, int] = field(default_factory=dict)
    problems: list[CardAuditResult] = field(default_factory=list)  # C and F grades

    def to_dict(self) -> dict:
        return {
            "total_cards": self.total_cards,
            "total_with_v2": self.total_with_v2,
            "coverage_pct": round(self.total_with_v2 / self.total_cards * 100, 1) if self.total_cards else 0,
            "overall_grade_counts": self.overall_grade_counts,
            "disease_summaries": {d: s.to_dict() for d, s in self.disease_summaries.items()},
            "problem_count": len(self.problems),
        }


def extract_frontmatter(path: Path) -> dict:
    """Extract frontmatter from a source card."""
    import re
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    end = content.find("\n---", 3)
    if end == -1:
        return {}
    fm = content[3:end]

    result = {}
    for line in fm.splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip("\"'")
    return result


def audit_card(path: Path) -> CardAuditResult:
    """Audit a single source card."""
    fm = extract_frontmatter(path)
    source_id = fm.get("id", path.stem)

    # Extract disease from ID (src-disease-nnn)
    disease = "unknown"
    if source_id.startswith("src-"):
        parts = source_id.split("-")
        if len(parts) >= 2:
            disease = parts[1]

    evidence_level = fm.get("evidence_level", "unknown")

    # Check for V2 fields
    v2_fields = extract_v2_fields_from_file(path)
    has_v2 = bool(v2_fields.get("core_argument"))

    report = None
    if has_v2:
        report = grade_v2_extraction(v2_fields)

    return CardAuditResult(
        path=path,
        source_id=source_id,
        disease=disease,
        evidence_level=evidence_level,
        has_v2_fields=has_v2,
        report=report,
    )


def run_audit(diseases: list[str] | None = None) -> AuditReport:
    """Run audit across all or specified diseases."""
    papers_dir = PROJECT_ROOT / "raw" / "papers"
    target_diseases = diseases or DISEASES

    report = AuditReport()

    for disease in target_diseases:
        cards = sorted(papers_dir.glob(f"src-{disease}-*.md"))
        summary = DiseaseAuditSummary(disease=disease, total_cards=len(cards), cards_with_v2=0)

        for card_path in cards:
            result = audit_card(card_path)
            report.card_results.append(result)
            report.total_cards += 1

            if result.has_v2_fields:
                summary.cards_with_v2 += 1
                report.total_with_v2 += 1

                grade = result.overall_grade
                summary.grade_counts[grade] = summary.grade_counts.get(grade, 0) + 1
                report.overall_grade_counts[grade] = report.overall_grade_counts.get(grade, 0) + 1

                if result.report:
                    summary.score_distribution.append(result.report.total_score)

                if grade in ("C", "F"):
                    report.problems.append(result)

        report.disease_summaries[disease] = summary

    return report


def stratified_sample(report: AuditReport, sample_size: int = 50) -> list[CardAuditResult]:
    """
    Generate stratified sample for manual review.

    Strata:
    - High score (10+): ~20% of sample
    - Medium score (6-9): ~40% of sample
    - Low score (<6): ~40% of sample
    """
    # Only cards with V2 fields
    v2_cards = [r for r in report.card_results if r.has_v2_fields and r.report]

    # Stratify by score
    high = [r for r in v2_cards if r.report.total_score >= 10]
    medium = [r for r in v2_cards if 6 <= r.report.total_score < 10]
    low = [r for r in v2_cards if r.report.total_score < 6]

    # Calculate sample sizes
    high_n = max(1, int(sample_size * 0.2))
    medium_n = max(1, int(sample_size * 0.4))
    low_n = sample_size - high_n - medium_n

    # Sample from each stratum
    sample = []
    sample.extend(random.sample(high, min(high_n, len(high))))
    sample.extend(random.sample(medium, min(medium_n, len(medium))))
    sample.extend(random.sample(low, min(low_n, len(low))))

    # Ensure disease diversity (at least 2 per disease if possible)
    by_disease = defaultdict(list)
    for r in sample:
        by_disease[r.disease].append(r)

    # Fill gaps
    remaining = sample_size - len(sample)
    if remaining > 0:
        not_sampled = [r for r in v2_cards if r not in sample]
        random.shuffle(not_sampled)
        for r in not_sampled[:remaining]:
            sample.append(r)

    return sample


def print_summary(report: AuditReport):
    """Print audit summary to console."""
    print(f"\n{'=' * 60}")
    print(f"V2 Field Quality Audit Report")
    print(f"{'=' * 60}\n")

    print(f"Total source cards: {report.total_cards}")
    print(f"Cards with V2 fields: {report.total_with_v2} ({report.total_with_v2 / report.total_cards * 100:.1f}%)")
    print(f"\nOverall Grade Distribution:")
    for grade in ["A", "B", "C", "F"]:
        count = report.overall_grade_counts.get(grade, 0)
        pct = count / report.total_with_v2 * 100 if report.total_with_v2 else 0
        bar = "#" * int(pct / 2)
        print(f"  {grade}: {count:3d} ({pct:5.1f}%) {bar}")

    print(f"\n{'─' * 60}")
    print(f"Per-Disease Breakdown:\n")
    print(f"{'Disease':<12} {'Cards':<8} {'V2':<6} {'Cov%':<8} {'AvgScore':<10} {'A':<4} {'B':<4} {'C':<4} {'F':<4}")
    print(f"{'─' * 12} {'─' * 8} {'─' * 6} {'─' * 8} {'─' * 10} {'─' * 4} {'─' * 4} {'─' * 4} {'─' * 4}")

    for disease in DISEASES:
        if disease not in report.disease_summaries:
            continue
        s = report.disease_summaries[disease]
        print(f"{disease:<12} {s.total_cards:<8} {s.cards_with_v2:<6} {s.coverage_pct:<8.1f} {s.avg_score:<10.2f} "
              f"{s.grade_counts.get('A', 0):<4} {s.grade_counts.get('B', 0):<4} "
              f"{s.grade_counts.get('C', 0):<4} {s.grade_counts.get('F', 0):<4}")

    if report.problems:
        print(f"\n{'─' * 60}")
        print(f"Problem Cards (C/F grades): {len(report.problems)}\n")
        for r in report.problems[:20]:
            grade = r.overall_grade
            score = r.report.total_score if r.report else 0
            issues = ", ".join(r.report.issues[:2]) if r.report else ""
            print(f"  [{grade}] {r.source_id:<18} score={score:2d}  {issues[:50]}")
        if len(report.problems) > 20:
            print(f"  ... and {len(report.problems) - 20} more")


def print_sample(sample: list[CardAuditResult]):
    """Print stratified sample for manual review."""
    print(f"\n{'=' * 60}")
    print(f"Stratified Sample for Manual Review ({len(sample)} cards)")
    print(f"{'=' * 60}\n")

    # Group by disease for review assignment
    by_disease = defaultdict(list)
    for r in sample:
        by_disease[r.disease].append(r)

    for disease in sorted(by_disease.keys()):
        print(f"\n## {disease.upper()}\n")
        for r in by_disease[disease]:
            grade = r.overall_grade
            score = r.report.total_score if r.report else 0
            level = r.evidence_level
            print(f"- [{grade}] {r.source_id} (score={score}, level={level})")
            print(f"  path: {r.path.relative_to(PROJECT_ROOT)}")
            if r.report and r.report.issues:
                for issue in r.report.issues[:2]:
                    print(f"  issue: {issue}")


def main():
    parser = argparse.ArgumentParser(description="Audit V2 field quality")
    parser.add_argument("--disease", type=str, help="Audit single disease")
    parser.add_argument("--sample", type=int, help="Generate stratified sample of N cards")
    parser.add_argument("--problems", action="store_true", help="Show only C/F grade cards")
    parser.add_argument("--json", action="store_true", help="JSON output")

    args = parser.parse_args()

    diseases = [args.disease] if args.disease else None
    report = run_audit(diseases)

    if args.json:
        output = report.to_dict()
        if args.problems:
            output["problems"] = [r.to_dict() for r in report.problems]
        if args.sample:
            sample = stratified_sample(report, args.sample)
            output["sample"] = [r.to_dict() for r in sample]
        print(json.dumps(output, indent=2, ensure_ascii=False))
        return 0

    if args.sample:
        sample = stratified_sample(report, args.sample)
        print_sample(sample)
        return 0

    if args.problems:
        print(f"\nProblem Cards (C/F grades): {len(report.problems)}\n")
        for r in report.problems:
            grade = r.overall_grade
            score = r.report.total_score if r.report else 0
            print(f"[{grade}] {r.source_id:<20} score={score:2d}")
            if r.report:
                for issue in r.report.issues:
                    print(f"    - {issue}")
        return 0 if not report.problems else 1

    print_summary(report)
    return 0 if not report.problems else 1


if __name__ == "__main__":
    sys.exit(main())
