#!/usr/bin/env python3
"""
scripts/v2_quality_gates.py
Quality gate functions for V2 field extraction.

Usage:
    python3 scripts/v2_quality_gates.py --test                    # Run test suite
    python3 scripts/v2_quality_gates.py --check raw/papers/src-hcm-001.md  # Check single card
    python3 scripts/v2_quality_gates.py --grade raw/papers/src-hcm-001.md  # Full grade with details
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

SCRIPTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))


# ============================================================================
# Signal Patterns
# ============================================================================

STANCE_VERBS_ZH = [
    "是", "无法", "需要", "不能", "优于", "导致", "仍是", "表明", "证明",
    "支持", "提示", "揭示", "确认", "反映", "显示", "预测", "决定"
]
STANCE_VERBS_EN = [
    "is", "are", "cannot", "remains", "requires", "demonstrates", "shows",
    "proves", "fails", "lacks", "provides", "predicts", "determines",
    "indicates", "reveals", "confirms", "reflects", "suggests"
]

TOPIC_MARKERS = [
    "这篇论文", "这项研究", "本研究", "本文", "本综述",
    "this paper", "this study", "the study", "this review", "the review"
]

CONTRAST_MARKERS_ZH = [
    "但", "然而", "而不是", "相反", "真正", "实际上", "事实上", "却"
]
CONTRAST_MARKERS_EN = [
    "but", "however", "actually", "instead", "contrary", "real value",
    "truly", "in fact", "whereas"
]

PRAISE_ONLY_MARKERS = [
    "重要", "有价值", "全面", "comprehensive", "important", "valuable",
    "worth reading", "interesting", "useful", "significant"
]

DESIGN_TERMS_ZH = [
    "横断面", "回顾性", "前瞻性", "单中心", "多中心", "随机", "对照",
    "队列", "病例系列", "叙述性综述", "系统性综述", "荟萃分析"
]
DESIGN_TERMS_EN = [
    "cross-sectional", "retrospective", "prospective", "single-center",
    "multi-center", "randomized", "controlled", "cohort", "case series",
    "case-control", "narrative review", "systematic review", "meta-analysis"
]

BOILERPLATE_PHRASES = [
    "需要更多研究", "进一步研究", "更多研究", "样本量有限",
    "more research needed", "further research", "limitations exist",
    "future studies", "future research", "more studies are needed"
]

# Interpretation markers that shouldn't be in quoted_fact
INTERPRETATION_MARKERS = [
    "支持", "表明这意味着", "这提示", "可能会", "应该",
    "suggests that", "implies", "should be", "might lead to",
    "supports keeping", "belongs in", "branch", "module"
]

# Specific entities that indicate grounded content
SPECIFIC_ENTITIES_RE = re.compile(
    r'\d+%?|mg/kg|mg/mL|ACVIM|HCM|CKD|FIP|IBD|FCV|NT-proBNP|SDMA|cTnI|'
    r'BNP|GFR|UPC|SAA|TP53|c-KIT|BRCA|Fig\.|Table|图|表'
)


# ============================================================================
# Data Structures
# ============================================================================

@dataclass
class FieldGrade:
    """Grade for a single V2 field."""
    grade: str  # A, B, C, F
    score: int  # 3, 2, 1, 0
    reason: str
    field_name: str


@dataclass
class V2QualityReport:
    """Full quality report for a V2 extraction."""
    core_argument: FieldGrade
    title_gap: FieldGrade
    evidence_boundary: FieldGrade
    hard_data_score: int  # 0-2
    coherence_score: int  # 0-1
    total_score: int  # 0-12
    overall_grade: str  # A, B, C, F
    issues: list[str] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)

    @property
    def should_block(self) -> bool:
        return self.overall_grade == "F"

    @property
    def needs_review(self) -> bool:
        return self.overall_grade == "C"

    def to_dict(self) -> dict:
        return {
            "core_argument": {"grade": self.core_argument.grade, "reason": self.core_argument.reason},
            "title_gap": {"grade": self.title_gap.grade, "reason": self.title_gap.reason},
            "evidence_boundary": {"grade": self.evidence_boundary.grade, "reason": self.evidence_boundary.reason},
            "hard_data_score": self.hard_data_score,
            "coherence_score": self.coherence_score,
            "total_score": self.total_score,
            "overall_grade": self.overall_grade,
            "issues": self.issues,
            "recommendations": self.recommendations,
        }


# ============================================================================
# Individual Field Checks
# ============================================================================

def grade_to_score(grade: str) -> int:
    """Convert letter grade to numeric score."""
    return {"A": 3, "B": 2, "C": 1, "F": 0}.get(grade, 0)


def check_core_argument(text: str | None) -> FieldGrade:
    """
    Grade core_argument field.

    A: Specific falsifiable claim with conditions
    B: Complete claim, imprecise conditions
    C: Topic description, not a claim
    F: Empty, generic, or wrong
    """
    if not text or len(text.strip()) < 15:
        return FieldGrade("F", 0, "empty or too short (<15 chars)", "core_argument")

    text = text.strip()
    text_lower = text.lower()

    # Check for topic description pattern (grade C)
    for marker in TOPIC_MARKERS:
        if text_lower.startswith(marker.lower()):
            return FieldGrade("C", 1, "topic description, not a claim", "core_argument")

    # Check for generic filler
    if any(filler in text_lower for filler in ["important research", "重要研究", "综合研究"]):
        if len(text) < 60:
            return FieldGrade("F", 0, "generic filler without substance", "core_argument")

    # Check for stance verbs
    has_stance_zh = any(v in text for v in STANCE_VERBS_ZH)
    has_stance_en = any(v in text_lower for v in STANCE_VERBS_EN)
    has_stance = has_stance_zh or has_stance_en

    # Check for specific entities
    has_specifics = bool(SPECIFIC_ENTITIES_RE.search(text))

    # Check for conditions/qualifications (good sign)
    has_conditions = bool(re.search(r'——|—|如果|当|在.*情况下|when|if|in cases of', text))

    if has_stance and has_specifics:
        if has_conditions:
            return FieldGrade("A", 3, "specific claim with conditions", "core_argument")
        return FieldGrade("A", 3, "specific claim with entity reference", "core_argument")
    elif has_stance and len(text) > 50:
        return FieldGrade("B", 2, "complete claim, imprecise conditions", "core_argument")
    elif has_specifics:
        return FieldGrade("B", 2, "has specifics but weak claim structure", "core_argument")
    else:
        return FieldGrade("C", 1, "no clear stance or claim", "core_argument")


def check_title_gap(text: str | None) -> FieldGrade:
    """
    Grade title_gap field.

    A: Specific contrast with intellectual tension
    B: Points out hidden value, weak tension
    C: Restates abstract, no real contrast
    F: Generic praise or title repetition
    """
    if not text or len(text.strip()) < 10:
        return FieldGrade("F", 0, "empty or too short (<10 chars)", "title_gap")

    text = text.strip()
    text_lower = text.lower()

    # Check for contrast markers
    has_contrast_zh = any(m in text for m in CONTRAST_MARKERS_ZH)
    has_contrast_en = any(m in text_lower for m in CONTRAST_MARKERS_EN)
    has_contrast = has_contrast_zh or has_contrast_en

    # Check for praise-only (bad if no contrast)
    praise_count = sum(1 for m in PRAISE_ONLY_MARKERS if m in text or m in text_lower)
    is_praise_heavy = praise_count >= 2 or (praise_count == 1 and len(text) < 50)

    if is_praise_heavy and not has_contrast:
        return FieldGrade("F", 0, "generic praise without specific contrast", "title_gap")

    # Check for specific references (figures, tables, numbers)
    has_evidence_ref = bool(re.search(r'图|表|Figure|Table|Fig\.|Tab\.|数据|data|\d+%|\d+/\d+', text))

    # Check for "标题说X，但Y" pattern (ideal)
    has_title_but_pattern = bool(re.search(r'标题.{0,20}但|title.{0,20}but', text_lower))

    if has_contrast and has_evidence_ref:
        return FieldGrade("A", 3, "specific contrast with evidence reference", "title_gap")
    elif has_title_but_pattern and has_contrast:
        return FieldGrade("A", 3, "clear title-gap pattern with contrast", "title_gap")
    elif has_contrast:
        return FieldGrade("B", 2, "contrast present but lacks specific evidence", "title_gap")
    elif has_evidence_ref:
        return FieldGrade("B", 2, "has specifics but no clear contrast", "title_gap")
    else:
        return FieldGrade("C", 1, "no clear contrast or intellectual tension", "title_gap")


def check_evidence_boundary(text: str | None) -> FieldGrade:
    """
    Grade evidence_boundary field.

    A: Methodology-based specific limitation
    B: States limitation without methodology link
    C: Vague limitation
    F: Empty or pure boilerplate
    """
    if not text or len(text.strip()) < 10:
        return FieldGrade("F", 0, "empty or too short (<10 chars)", "evidence_boundary")

    text = text.strip()
    text_lower = text.lower()

    # Check for pure boilerplate (short + boilerplate phrase)
    for phrase in BOILERPLATE_PHRASES:
        if phrase in text_lower:
            if len(text) < 50:
                return FieldGrade("F", 0, "pure boilerplate", "evidence_boundary")

    # Check for design terms (methodology grounding)
    has_design_zh = any(t in text for t in DESIGN_TERMS_ZH)
    has_design_en = any(t in text_lower for t in DESIGN_TERMS_EN)
    has_design = has_design_zh or has_design_en

    # Check for specific impact (named variables, endpoints)
    has_specifics = bool(re.search(
        r'\d+|LACI|NT-proBNP|SDMA|纤维化|thromboembolism|mortality|GFR|UPC|'
        r'预测|因果|causality|predict|subgroup|亚组',
        text
    ))

    # Check for clear limitation structure
    has_limitation_structure = bool(re.search(
        r'无法|不能|未能|未涉及|无法确定|cannot|does not|unable to|did not|'
        r'insufficient|lacking|missing',
        text_lower
    ))

    if has_design and has_specifics:
        return FieldGrade("A", 3, "methodology-grounded specific limitation", "evidence_boundary")
    elif has_design and has_limitation_structure:
        return FieldGrade("A", 3, "methodology-grounded limitation", "evidence_boundary")
    elif has_design or has_specifics:
        return FieldGrade("B", 2, "limitation stated, partial grounding", "evidence_boundary")
    elif has_limitation_structure:
        return FieldGrade("B", 2, "limitation stated, needs grounding", "evidence_boundary")
    else:
        return FieldGrade("C", 1, "vague limitation", "evidence_boundary")


# ============================================================================
# Additional Checks
# ============================================================================

def check_hard_data(quoted_facts: list[str] | None) -> int:
    """
    Check if quoted_facts contain hard data (numbers, p-values, sample sizes).
    Returns 0-2 score.
    """
    if not quoted_facts:
        return 0

    hard_data_pattern = re.compile(
        r'\d+\s*%|\d+/\d+|n\s*=\s*\d+|p\s*[<>=]\s*0?\.\d+|'
        r'\d+\s*(?:mg|kg|mL|days?|weeks?|months?|years?|cats?|cases?)|'
        r'AUC\s*(?:of\s*)?\d+\.\d+|kappa\s*=\s*\d+\.\d+',
        re.I
    )

    hard_data_count = sum(1 for fact in quoted_facts if hard_data_pattern.search(fact))

    if hard_data_count >= 2:
        return 2
    elif hard_data_count >= 1:
        return 1
    return 0


def check_coherence(fields: dict) -> tuple[int, list[str]]:
    """
    Check if V2 fields are internally coherent.
    Returns (0-1 score, list of issues).
    """
    issues = []

    # Check quoted_fact discipline
    quoted_facts = fields.get("quoted_fact", [])
    if isinstance(quoted_facts, list):
        for fact in quoted_facts:
            if any(marker in fact for marker in INTERPRETATION_MARKERS):
                issues.append(f"quoted_fact contains interpretation: '{fact[:50]}...'")

    # Check for mis-ingestion warning
    study_design = fields.get("study_design", "")
    if study_design and "误收录警告" in study_design:
        issues.append("mis-ingestion warning detected in study_design")

    # Check that core_argument and evidence_boundary aren't contradictory
    # (basic check: evidence_boundary shouldn't repeat core_argument claims)
    core_arg = fields.get("core_argument", "")
    evidence_bound = fields.get("evidence_boundary", "")
    if core_arg and evidence_bound:
        # If evidence_boundary contains same strong claims as core_argument, that's odd
        if len(core_arg) > 50 and core_arg[:30] in evidence_bound:
            issues.append("evidence_boundary may overlap with core_argument")

    return (0 if issues else 1), issues


# ============================================================================
# Full Grading
# ============================================================================

def grade_v2_extraction(fields: dict) -> V2QualityReport:
    """
    Grade a complete V2 extraction.

    Args:
        fields: Dict containing V2 fields from evidence_policy

    Returns:
        V2QualityReport with grades, scores, and recommendations
    """
    # Grade individual fields
    core_grade = check_core_argument(fields.get("core_argument"))
    gap_grade = check_title_gap(fields.get("title_gap"))
    bound_grade = check_evidence_boundary(fields.get("evidence_boundary"))

    # Additional scores
    hard_data = check_hard_data(fields.get("quoted_fact"))
    coherence, coherence_issues = check_coherence(fields)

    # Calculate total
    total = (
        core_grade.score +
        gap_grade.score +
        bound_grade.score +
        hard_data +
        coherence
    )

    # Determine overall grade
    if total >= 10:
        overall = "A"
    elif total >= 7:
        overall = "B"
    elif total >= 4:
        overall = "C"
    else:
        overall = "F"

    # Collect issues
    issues = coherence_issues.copy()
    if core_grade.grade in ("C", "F"):
        issues.append(f"core_argument: {core_grade.reason}")
    if gap_grade.grade in ("C", "F"):
        issues.append(f"title_gap: {gap_grade.reason}")
    if bound_grade.grade in ("C", "F"):
        issues.append(f"evidence_boundary: {bound_grade.reason}")

    # Generate recommendations
    recommendations = []
    if core_grade.grade in ("C", "F"):
        recommendations.append(
            "Rewrite core_argument as a specific falsifiable claim with stance verb"
        )
    if gap_grade.grade in ("C", "F"):
        recommendations.append(
            "Rewrite title_gap with '标题说X，但真正发现是Y' pattern"
        )
    if bound_grade.grade in ("C", "F"):
        recommendations.append(
            "Ground evidence_boundary in specific methodology limitations"
        )
    if hard_data == 0:
        recommendations.append(
            "Add quoted_fact entries with hard data (numbers, p-values, sample sizes)"
        )

    return V2QualityReport(
        core_argument=core_grade,
        title_gap=gap_grade,
        evidence_boundary=bound_grade,
        hard_data_score=hard_data,
        coherence_score=coherence,
        total_score=total,
        overall_grade=overall,
        issues=issues,
        recommendations=recommendations,
    )


# ============================================================================
# File Parsing
# ============================================================================

def extract_v2_fields_from_file(path: Path) -> dict:
    """Extract V2 fields from a source card file."""
    content = path.read_text(encoding="utf-8")

    # Find frontmatter
    if not content.startswith("---"):
        return {}

    end = content.find("\n---", 3)
    if end == -1:
        return {}

    fm = content[3:end]

    fields = {}

    # Extract simple fields
    for field_name in ["study_design", "core_argument", "implicit_premise",
                       "title_gap", "evidence_boundary", "unexpected_finding"]:
        match = re.search(rf'{field_name}:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
        if match:
            fields[field_name] = match.group(1).strip().strip("\"'")

    # Extract quoted_fact list
    quoted_facts = []
    in_quoted_fact = False
    for line in fm.splitlines():
        if line.strip().startswith("quoted_fact:"):
            in_quoted_fact = True
            continue
        if in_quoted_fact:
            if re.match(r'^\s{4}-\s+', line):
                fact = re.sub(r'^\s{4}-\s+', '', line).strip().strip("\"'")
                if fact:
                    quoted_facts.append(fact)
            elif re.match(r'^\s{2}\w', line) or re.match(r'^\w', line):
                in_quoted_fact = False

    if quoted_facts:
        fields["quoted_fact"] = quoted_facts

    return fields


# ============================================================================
# Test Suite
# ============================================================================

def run_tests():
    """Run quality gate test suite."""
    print("Running V2 quality gate tests...\n")
    passed = 0
    failed = 0

    # Test core_argument
    tests = [
        # (input, expected_grade, test_name)
        ("", "F", "core_argument: empty"),
        ("short", "F", "core_argument: too short"),
        ("这篇论文研究了 HCM 生物标志物的相关研究进展和应用前景", "C", "core_argument: topic description"),
        ("这是一篇关于猫疾病的重要研究值得阅读和参考", "F", "core_argument: generic"),
        ("猫 HCM 是最常见的心肌病之一，影响约 15% 的猫", "A", "core_argument: claim with specifics"),
        (
            "轻中度左心室肥厚在猫中无法仅靠超声心动图确诊——仍是排除性诊断",
            "A",
            "core_argument: specific with conditions"
        ),
        (
            "NT-proBNP combined with cTnI provides better stratification than either alone",
            "A",
            "core_argument: specific claim EN"
        ),
    ]

    for text, expected, name in tests:
        result = check_core_argument(text)
        if result.grade == expected:
            passed += 1
            print(f"  PASS: {name}")
        else:
            failed += 1
            print(f"  FAIL: {name} - expected {expected}, got {result.grade} ({result.reason})")

    # Test title_gap
    tests = [
        ("", "F", "title_gap: empty"),
        ("这是一篇非常重要的有价值的研究", "F", "title_gap: praise only"),
        ("内容比标题更加详细，覆盖范围更广", "C", "title_gap: no contrast"),
        ("标题强调机制研究，但本文也讨论了临床含义", "A", "title_gap: contrast with title pattern"),
        (
            "标题说 prevalence，但真正价值是发现了表3中40%脱落率数据",
            "A",
            "title_gap: specific contrast"
        ),
    ]

    for text, expected, name in tests:
        result = check_title_gap(text)
        if result.grade == expected:
            passed += 1
            print(f"  PASS: {name}")
        else:
            failed += 1
            print(f"  FAIL: {name} - expected {expected}, got {result.grade} ({result.reason})")

    # Test evidence_boundary
    tests = [
        ("", "F", "evidence_boundary: empty"),
        ("需要更多研究来进一步验证结论", "F", "evidence_boundary: boilerplate"),
        ("样本量有限，需要更大规模研究来验证", "F", "evidence_boundary: short boilerplate"),
        ("本研究未涉及长期预后和生存率分析，未评估治疗持久性", "B", "evidence_boundary: limitation no design"),
        ("回顾性设计无法确定治疗与结局之间的因果关系", "A", "evidence_boundary: design + limitation"),
        (
            "横断面设计无法确定 LACI-ED 变化是否预测临床恶化",
            "A",
            "evidence_boundary: full methodology grounding"
        ),
    ]

    for text, expected, name in tests:
        result = check_evidence_boundary(text)
        if result.grade == expected:
            passed += 1
            print(f"  PASS: {name}")
        else:
            failed += 1
            print(f"  FAIL: {name} - expected {expected}, got {result.grade} ({result.reason})")

    # Test hard_data
    tests = [
        ([], 0, "hard_data: empty"),
        (["Some general statement"], 0, "hard_data: no numbers"),
        (["Sample included 50% male cats"], 1, "hard_data: one number"),
        (["n=91 cats", "p<0.05"], 2, "hard_data: multiple numbers"),
    ]

    for facts, expected, name in tests:
        result = check_hard_data(facts)
        if result == expected:
            passed += 1
            print(f"  PASS: {name}")
        else:
            failed += 1
            print(f"  FAIL: {name} - expected {expected}, got {result}")

    # Test full grading
    good_fields = {
        "core_argument": "轻中度左心室肥厚在猫中无法仅靠超声心动图确诊——仍是排除性诊断",
        "title_gap": "标题是 HCM 综述，但真正发现是诊断边界问题——表3显示66%阳性预测值",
        "evidence_boundary": "横断面设计无法确定 LACI-ED 变化是否预测临床恶化",
        "quoted_fact": ["n=91 cats with HCM", "p<0.001 for correlation"],
    }
    result = grade_v2_extraction(good_fields)
    if result.overall_grade == "A":
        passed += 1
        print(f"  PASS: full grading: A-grade card")
    else:
        failed += 1
        print(f"  FAIL: full grading: A-grade card - expected A, got {result.overall_grade}")

    bad_fields = {
        "core_argument": "这篇论文研究了 HCM",
        "title_gap": "内容详细",
        "evidence_boundary": "需要更多研究",
        "quoted_fact": [],
    }
    result = grade_v2_extraction(bad_fields)
    if result.overall_grade == "F":
        passed += 1
        print(f"  PASS: full grading: F-grade card")
    else:
        failed += 1
        print(f"  FAIL: full grading: F-grade card - expected F, got {result.overall_grade}")

    print(f"\n{'=' * 50}")
    print(f"Tests: {passed + failed} | Passed: {passed} | Failed: {failed}")
    return 0 if failed == 0 else 1


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="V2 field quality gates")
    parser.add_argument("--test", action="store_true", help="Run test suite")
    parser.add_argument("--check", type=str, help="Check a single source card file")
    parser.add_argument("--grade", type=str, help="Full grade with details")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.test:
        return run_tests()

    if args.check or args.grade:
        path = Path(args.check or args.grade)
        if not path.is_absolute():
            path = PROJECT_ROOT / path
        if not path.exists():
            print(f"ERROR: File not found: {path}")
            return 1

        fields = extract_v2_fields_from_file(path)
        if not fields.get("core_argument"):
            print(f"No V2 fields found in {path.name}")
            return 1

        report = grade_v2_extraction(fields)

        if args.json:
            import json
            print(json.dumps(report.to_dict(), indent=2, ensure_ascii=False))
        else:
            print(f"File: {path.name}")
            print(f"Overall Grade: {report.overall_grade} (score: {report.total_score}/12)")
            print(f"  core_argument: {report.core_argument.grade} - {report.core_argument.reason}")
            print(f"  title_gap: {report.title_gap.grade} - {report.title_gap.reason}")
            print(f"  evidence_boundary: {report.evidence_boundary.grade} - {report.evidence_boundary.reason}")
            print(f"  hard_data: {report.hard_data_score}/2")
            print(f"  coherence: {report.coherence_score}/1")
            if report.issues:
                print(f"\nIssues:")
                for issue in report.issues:
                    print(f"  - {issue}")
            if report.recommendations:
                print(f"\nRecommendations:")
                for rec in report.recommendations:
                    print(f"  - {rec}")

        return 0 if report.overall_grade in ("A", "B") else 1

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
