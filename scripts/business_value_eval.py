#!/usr/bin/env python3
"""
scripts/business_value_eval.py — Evaluate business artifacts for completeness.

Tests that legacy business artifacts meet containment requirements:
- Candidate evidence cards disclose their non-semantic authority boundary
- Opportunity briefs disable automated decisions
- Source IDs exist and are valid
- Boundaries exist
- Next actions exist
- No unsupported claims (claims without source IDs)

Usage:
    python scripts/business_value_eval.py [--verbose]
    python scripts/business_value_eval.py --artifact outputs/business/some-brief.md
"""

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

VAULT_ROOT = Path(__file__).parent.parent

# Required sections for each artifact type
OPPORTUNITY_BRIEF_REQUIRED = [
    "Executive Summary",
    "Evidence Backbone",
    "Endpoint Maturity",
    "Regulatory Path",
    "Missing Evidence",
    "Automated Decision Status",
    "Source Appendix",
]

CLAIM_CARD_REQUIRED = [
    "Retrieval Status",
    "Key Sources",
    "Evidence Depth",
    "Boundary",
]

ENDPOINT_MEMO_REQUIRED = [
    "Primary Recommendation",
    "Endpoint Hierarchy",
    "Key-Claim Traceability",
    "Boundary",
    "Source Appendix",
]


@dataclass
class EvalResult:
    """Result of evaluating a single artifact."""
    artifact_path: str
    artifact_type: str
    passed: bool
    score: float  # 0.0 to 1.0
    checks: list[dict] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


@dataclass
class EvalSummary:
    """Summary of all evaluations."""
    total_artifacts: int
    passed: int
    failed: int
    overall_score: float
    results: list[EvalResult]


def _parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}
    end = content.find("\n---", 3)
    if end == -1:
        return {}

    fm = {}
    for line in content[3:end].splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip().strip("\"'")
            fm[key] = val
    return fm


def _extract_source_ids(content: str) -> list[str]:
    """Extract all source IDs mentioned in the content."""
    # Match patterns like src-ckd-001, src-fip-002, etc.
    pattern = r'\bsrc-[a-z]+-\d{3}\b'
    return list(set(re.findall(pattern, content, re.IGNORECASE)))


def _check_section_exists(content: str, section_name: str) -> bool:
    """Check if a section (heading) exists in the content."""
    patterns = [
        f"## {section_name}",
        f"### {section_name}",
        f"# {section_name}",
    ]
    for pattern in patterns:
        if pattern.lower() in content.lower():
            return True
    return False


def _validate_source_ids(source_ids: list[str]) -> tuple[list[str], list[str]]:
    """Check which source IDs exist as actual files."""
    valid = []
    invalid = []
    papers_dir = VAULT_ROOT / "raw" / "papers"
    regulations_dir = VAULT_ROOT / "raw" / "regulations"

    for src_id in source_ids:
        if src_id.lower().startswith("src-reg-"):
            matches = list(regulations_dir.glob(f"{src_id}-*.md")) + list(regulations_dir.glob(f"{src_id}.md"))
            src_path = matches[0] if matches else regulations_dir / f"{src_id}.md"
        else:
            src_path = papers_dir / f"{src_id}.md"
        if src_path.exists():
            valid.append(src_id)
        else:
            invalid.append(src_id)

    return valid, invalid


def _check_claim_traceability_table(content: str) -> tuple[int, int, list[str]]:
    """
    Check Key-Claim Traceability tables for claims without source IDs.
    Returns (total_claims, claims_with_sources, unsupported_claims).
    """
    total = 0
    with_sources = 0
    unsupported = []

    # Find table rows that look like claim entries
    # Pattern: | ClaimID | Claim text | Level | Sources |
    lines = content.splitlines()
    in_claim_table = False

    for line in lines:
        if "Key-Claim Traceability" in line or "Claim ID" in line:
            in_claim_table = True
            continue

        if in_claim_table and line.startswith("|"):
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) >= 4 and "---" not in line:
                # Skip header rows
                if cells[0].lower() in ["claim id", "id"]:
                    continue

                total += 1
                claim_text = cells[1] if len(cells) > 1 else ""
                sources_cell = cells[3] if len(cells) > 3 else ""

                # Check if sources cell has valid source IDs
                source_ids = re.findall(r'src-[a-z]+-\d{3}', sources_cell, re.IGNORECASE)
                if source_ids:
                    with_sources += 1
                else:
                    # Check if it references a memo instead
                    if "memo" in sources_cell.lower() or sources_cell.strip():
                        with_sources += 1  # Memo references count
                    else:
                        unsupported.append(claim_text[:50])

        elif in_claim_table and line.startswith("## "):
            # New section, end of table
            in_claim_table = False

    return total, with_sources, unsupported


def evaluate_claim_card(content: str, path: str) -> EvalResult:
    """Evaluate a claim evidence card."""
    result = EvalResult(
        artifact_path=path,
        artifact_type="claim_card",
        passed=True,
        score=1.0,
        checks=[],
        errors=[],
        warnings=[],
    )

    total_checks = 0
    passed_checks = 0

    # Check 1: Discloses candidate-only status
    total_checks += 1
    candidate_only = (
        "candidate retrieval only" in content.lower()
        and "semantic confidence" in content.lower()
        and "not_assessed" in content.lower()
    )
    result.checks.append({"name": "candidate_only_disclosure", "passed": candidate_only})
    if candidate_only:
        passed_checks += 1
    else:
        result.errors.append("Missing candidate-only authority disclosure")

    # Check 2: Has key sources
    total_checks += 1
    source_ids = _extract_source_ids(content)
    has_sources = len(source_ids) > 0
    result.checks.append({"name": "has_key_sources", "passed": has_sources, "count": len(source_ids)})
    if has_sources:
        passed_checks += 1
    else:
        result.errors.append("No source IDs found in claim card")

    # Check 3: Source IDs are valid
    if source_ids:
        total_checks += 1
        valid, invalid = _validate_source_ids(source_ids)
        all_valid = len(invalid) == 0
        result.checks.append({
            "name": "source_ids_valid",
            "passed": all_valid,
            "valid": valid,
            "invalid": invalid
        })
        if all_valid:
            passed_checks += 1
        else:
            result.warnings.append(f"Invalid source IDs: {invalid}")

    # Check 4: Has boundary section
    total_checks += 1
    has_boundary = _check_section_exists(content, "Boundary")
    result.checks.append({"name": "has_boundary", "passed": has_boundary})
    if has_boundary:
        passed_checks += 1
    else:
        result.errors.append("Missing boundary section")

    # Check 5: Has next action
    total_checks += 1
    has_next_action = "next_action" in content.lower() or "next action" in content.lower()
    result.checks.append({"name": "has_next_action", "passed": has_next_action})
    if has_next_action:
        passed_checks += 1
    else:
        result.warnings.append("Missing next action field")

    # Check 6: Has evidence depth
    total_checks += 1
    has_depth = _check_section_exists(content, "Evidence Depth")
    result.checks.append({"name": "has_evidence_depth", "passed": has_depth})
    if has_depth:
        passed_checks += 1
    else:
        result.warnings.append("Missing evidence depth section")

    # Calculate score
    result.score = passed_checks / total_checks if total_checks > 0 else 0.0
    result.passed = len(result.errors) == 0 and result.score >= 0.8

    return result


def evaluate_opportunity_brief(content: str, path: str) -> EvalResult:
    """Evaluate an opportunity brief."""
    result = EvalResult(
        artifact_path=path,
        artifact_type="opportunity_brief",
        passed=True,
        score=1.0,
        checks=[],
        errors=[],
        warnings=[],
    )

    total_checks = 0
    passed_checks = 0

    # Check 1: Required sections exist
    for section in OPPORTUNITY_BRIEF_REQUIRED:
        total_checks += 1
        has_section = _check_section_exists(content, section)
        result.checks.append({"name": f"has_{section.lower().replace(' ', '_')}", "passed": has_section})
        if has_section:
            passed_checks += 1
        else:
            result.errors.append(f"Missing required section: {section}")

    # Check 2: Has source IDs
    total_checks += 1
    source_ids = _extract_source_ids(content)
    has_sources = len(source_ids) >= 3  # Briefs should have multiple sources
    result.checks.append({"name": "has_source_ids", "passed": has_sources, "count": len(source_ids)})
    if has_sources:
        passed_checks += 1
    else:
        result.errors.append(f"Insufficient source IDs (found {len(source_ids)}, need at least 3)")

    # Check 3: Source IDs are valid
    if source_ids:
        total_checks += 1
        valid, invalid = _validate_source_ids(source_ids)
        valid_ratio = len(valid) / len(source_ids) if source_ids else 0
        mostly_valid = valid_ratio >= 0.8
        result.checks.append({
            "name": "source_ids_valid",
            "passed": mostly_valid,
            "valid_count": len(valid),
            "invalid": invalid
        })
        if mostly_valid:
            passed_checks += 1
        else:
            result.warnings.append(f"Some invalid source IDs: {invalid}")

    # Check 4: Automated decision authority is disabled
    total_checks += 1
    decision_disabled = (
        "automated decision disabled" in content.lower()
        and "unreviewed legacy output" in content.lower()
    )
    result.checks.append({"name": "automated_decision_disabled", "passed": decision_disabled})
    if decision_disabled:
        passed_checks += 1
    else:
        result.errors.append("Missing automated-decision containment notice")

    # Check 5: Key-Claim Traceability has sources
    total_checks += 1
    total_claims, with_sources, unsupported = _check_claim_traceability_table(content)
    if total_claims > 0:
        claim_coverage = with_sources / total_claims
        claims_ok = claim_coverage >= 0.9
        result.checks.append({
            "name": "claims_have_sources",
            "passed": claims_ok,
            "total": total_claims,
            "with_sources": with_sources,
            "unsupported": unsupported
        })
        if claims_ok:
            passed_checks += 1
        else:
            result.errors.append(f"Unsupported claims found: {unsupported}")
    else:
        # No claim table is a warning, not an error for briefs
        result.checks.append({"name": "claims_have_sources", "passed": True, "note": "No claim table found"})
        passed_checks += 1
        result.warnings.append("No Key-Claim Traceability table found")

    # Check 6: Has missing evidence section with content
    total_checks += 1
    has_missing = _check_section_exists(content, "Missing Evidence")
    has_gaps = "gap" in content.lower() or "missing" in content.lower()
    missing_ok = has_missing and has_gaps
    result.checks.append({"name": "has_missing_evidence", "passed": missing_ok})
    if missing_ok:
        passed_checks += 1
    else:
        result.warnings.append("Missing evidence section may be incomplete")

    # Calculate score
    result.score = passed_checks / total_checks if total_checks > 0 else 0.0
    result.passed = len(result.errors) == 0 and result.score >= 0.7

    return result


def evaluate_endpoint_memo(content: str, path: str) -> EvalResult:
    """Evaluate an endpoint decision memo."""
    result = EvalResult(
        artifact_path=path,
        artifact_type="endpoint_decision_memo",
        passed=True,
        score=1.0,
        checks=[],
        errors=[],
        warnings=[],
    )

    total_checks = 0
    passed_checks = 0

    # Check 1: Required sections exist
    for section in ENDPOINT_MEMO_REQUIRED:
        total_checks += 1
        has_section = _check_section_exists(content, section)
        result.checks.append({"name": f"has_{section.lower().replace(' ', '_').replace('-', '_')}", "passed": has_section})
        if has_section:
            passed_checks += 1
        else:
            result.errors.append(f"Missing required section: {section}")

    # Check 2: Has endpoint hierarchy tiers (Core, Support, Context)
    total_checks += 1
    has_core = "Core Tier" in content or "Core (" in content
    has_support = "Support Tier" in content or "Support (" in content
    has_context = "Context Tier" in content or "Context (" in content
    has_tiers = has_core and (has_support or has_context)
    result.checks.append({"name": "has_endpoint_tiers", "passed": has_tiers})
    if has_tiers:
        passed_checks += 1
    else:
        result.errors.append("Missing endpoint hierarchy tiers (need Core + Support/Context)")

    # Check 3: Has source IDs
    total_checks += 1
    source_ids = _extract_source_ids(content)
    has_sources = len(source_ids) >= 3  # Memos should have multiple sources
    result.checks.append({"name": "has_source_ids", "passed": has_sources, "count": len(source_ids)})
    if has_sources:
        passed_checks += 1
    else:
        result.errors.append(f"Insufficient source IDs (found {len(source_ids)}, need at least 3)")

    # Check 4: Source IDs are valid
    if source_ids:
        total_checks += 1
        valid, invalid = _validate_source_ids(source_ids)
        valid_ratio = len(valid) / len(source_ids) if source_ids else 0
        mostly_valid = valid_ratio >= 0.8
        result.checks.append({
            "name": "source_ids_valid",
            "passed": mostly_valid,
            "valid_count": len(valid),
            "invalid": invalid
        })
        if mostly_valid:
            passed_checks += 1
        else:
            result.warnings.append(f"Some invalid source IDs: {invalid}")

    # Check 5: Key-Claim Traceability has sources
    total_checks += 1
    total_claims, with_sources, unsupported = _check_claim_traceability_table(content)
    if total_claims > 0:
        claim_coverage = with_sources / total_claims
        claims_ok = claim_coverage >= 0.9
        result.checks.append({
            "name": "claims_have_sources",
            "passed": claims_ok,
            "total": total_claims,
            "with_sources": with_sources,
            "unsupported": unsupported
        })
        if claims_ok:
            passed_checks += 1
        else:
            result.errors.append(f"Unsupported claims found: {unsupported}")
    else:
        result.checks.append({"name": "claims_have_sources", "passed": True, "note": "No claim table found"})
        passed_checks += 1
        result.warnings.append("No Key-Claim Traceability table found")

    # Check 6: Has use case specified
    total_checks += 1
    fm = _parse_frontmatter(content)
    has_use_case = fm.get("use_case") or "Use Case" in content
    result.checks.append({"name": "has_use_case", "passed": has_use_case})
    if has_use_case:
        passed_checks += 1
    else:
        result.warnings.append("No use case specified in frontmatter or content")

    # Calculate score
    result.score = passed_checks / total_checks if total_checks > 0 else 0.0
    result.passed = len(result.errors) == 0 and result.score >= 0.7

    return result


def detect_artifact_type(content: str, path: str) -> str:
    """Detect the type of artifact from content or path."""
    fm = _parse_frontmatter(content)

    # Check frontmatter first
    if fm.get("artifact_kind") == "opportunity_brief":
        return "opportunity_brief"
    if fm.get("artifact_kind") == "endpoint_decision_memo":
        return "endpoint_decision_memo"
    if fm.get("type") == "business" and "brief" in path.lower():
        return "opportunity_brief"

    # Check content patterns
    if "Candidate Evidence Matches" in content or "Claim Evidence Card" in content:
        return "claim_card"
    if "Opportunity Brief" in content or "Automated Decision Status" in content:
        return "opportunity_brief"
    if "Endpoint Decision Memo" in content or "Endpoint Hierarchy" in content:
        return "endpoint_decision_memo"

    # Check path
    if "brief" in path.lower():
        return "opportunity_brief"
    if "claim" in path.lower():
        return "claim_card"
    if "endpoint" in path.lower() and "decision" in path.lower():
        return "endpoint_decision_memo"

    return "unknown"


def evaluate_artifact(path: Path) -> Optional[EvalResult]:
    """Evaluate a single artifact file."""
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        return EvalResult(
            artifact_path=str(path),
            artifact_type="unknown",
            passed=False,
            score=0.0,
            errors=[f"Could not read file: {e}"]
        )

    artifact_type = detect_artifact_type(content, str(path))

    if artifact_type == "opportunity_brief":
        return evaluate_opportunity_brief(content, str(path))
    elif artifact_type == "claim_card":
        return evaluate_claim_card(content, str(path))
    elif artifact_type == "endpoint_decision_memo":
        return evaluate_endpoint_memo(content, str(path))
    else:
        return None


def evaluate_all_business_artifacts() -> EvalSummary:
    """Evaluate all business artifacts in outputs/business/."""
    business_dir = VAULT_ROOT / "outputs" / "business"
    results = []

    if business_dir.exists():
        for md_file in business_dir.glob("*.md"):
            result = evaluate_artifact(md_file)
            if result:
                results.append(result)

    passed = sum(1 for r in results if r.passed)
    failed = len(results) - passed
    overall_score = sum(r.score for r in results) / len(results) if results else 0.0

    return EvalSummary(
        total_artifacts=len(results),
        passed=passed,
        failed=failed,
        overall_score=overall_score,
        results=results
    )


def format_result(result: EvalResult, verbose: bool = False) -> str:
    """Format a single eval result for display."""
    status = "PASS" if result.passed else "FAIL"
    lines = [
        f"{status} | {result.artifact_type} | {result.artifact_path} | score={result.score:.2f}"
    ]

    if result.errors:
        for error in result.errors:
            lines.append(f"  ERROR: {error}")

    if verbose:
        if result.warnings:
            for warning in result.warnings:
                lines.append(f"  WARN: {warning}")

        for check in result.checks:
            check_status = "ok" if check.get("passed") else "FAIL"
            lines.append(f"  [{check_status}] {check['name']}")

    return "\n".join(lines)


def format_summary(summary: EvalSummary) -> str:
    """Format the overall summary."""
    lines = [
        "",
        "=" * 60,
        "BUSINESS VALUE EVAL SUMMARY",
        "=" * 60,
        f"Total artifacts: {summary.total_artifacts}",
        f"Passed: {summary.passed}",
        f"Failed: {summary.failed}",
        f"Overall score: {summary.overall_score:.2%}",
        "=" * 60,
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Evaluate business artifacts for completeness.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--artifact", "-a",
        help="Evaluate a specific artifact file",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed check results",
    )
    args = parser.parse_args()

    if args.artifact:
        path = Path(args.artifact)
        if not path.exists():
            print(f"ERROR: File not found: {args.artifact}")
            sys.exit(1)

        result = evaluate_artifact(path)
        if result:
            print(format_result(result, verbose=args.verbose))
            sys.exit(0 if result.passed else 1)
        else:
            print(f"ERROR: Could not detect artifact type for: {args.artifact}")
            sys.exit(1)
    else:
        summary = evaluate_all_business_artifacts()

        for result in summary.results:
            print(format_result(result, verbose=args.verbose))

        print(format_summary(summary))

        sys.exit(0 if summary.failed == 0 else 1)


if __name__ == "__main__":
    main()
