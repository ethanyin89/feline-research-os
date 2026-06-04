#!/usr/bin/env python3
"""
scripts/opportunity_brief.py — Opportunity Brief Generator for feline research OS.

Automatically generates opportunity briefs by combining:
- Claim evidence evaluation
- Endpoint decision memos
- Regulatory route memos
- Gap analysis

Usage:
    python scripts/opportunity_brief.py --disease ckd --branch "phosphorus control"
    python scripts/opportunity_brief.py --disease fip --branch "GS-441524 treatment"

Usage (imported):
    from opportunity_brief import generate_opportunity_brief
    brief = generate_opportunity_brief("ckd", "phosphorus control")
"""

import argparse
import json
import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional

# Import sibling modules
try:
    from claim_evidence import evaluate_claim, ClaimEvidenceCard
    from endpoint_decision import generate_endpoint_memo, EndpointDecisionMemo
except ImportError:
    from .claim_evidence import evaluate_claim, ClaimEvidenceCard
    from .endpoint_decision import generate_endpoint_memo, EndpointDecisionMemo

VAULT_ROOT = Path(__file__).parent.parent

# Disease maturity levels
DISEASE_MATURITY = {
    "ckd": {"sources": 24, "extraction": "full", "maturity": "Mature"},
    "fip": {"sources": 24, "extraction": "full", "maturity": "Mature"},
    "hcm": {"sources": 24, "extraction": "full", "maturity": "Mature"},
    "ibd": {"sources": 24, "extraction": "full", "maturity": "Mature"},
    "fcv": {"sources": 24, "extraction": "full", "maturity": "Mature"},
    "diabetes": {"sources": 118, "extraction": "partial", "maturity": "Developing"},
    "obesity": {"sources": 87, "extraction": "partial", "maturity": "Developing"},
    "cancer": {"sources": 102, "extraction": "partial", "maturity": "Developing"},
}

# Regulatory jurisdiction info
JURISDICTIONS = ["FDA / USA", "EMA / EU", "VMD / UK", "China"]


@dataclass
class GapItem:
    """Evidence gap for intake queue."""
    gap_id: str
    description: str
    impact: str
    priority: str
    suggested_search: str


@dataclass
class OpportunityBrief:
    """Complete opportunity brief structure."""
    disease: str
    branch: str
    business_question: str
    executive_summary: str
    go_no_go: str
    evidence_backbone: list[dict]
    key_claims: list[dict]
    endpoint_memo: Optional[EndpointDecisionMemo]
    regulatory_notes: dict
    missing_evidence: list[str]
    gaps: list[GapItem]
    source_appendix: list[str]
    generated_at: str
    maturity: str


def _find_route_memo(disease: str, branch: str) -> Optional[str]:
    """Find relevant route memo for a disease branch."""
    system_dir = VAULT_ROOT / "system" / "indexes"
    if not system_dir.exists():
        return None

    # Search for route memos matching disease and branch keywords
    branch_tokens = set(branch.lower().split())
    best_match = None
    best_score = 0

    for memo_path in system_dir.glob(f"{disease.lower()}-*-route-memo.md"):
        name = memo_path.stem.lower()
        # Score by keyword overlap
        score = sum(1 for token in branch_tokens if token in name)
        if score > best_score:
            best_score = score
            best_match = memo_path

    if best_match:
        try:
            return best_match.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            return None

    return None


def _extract_regulatory_notes(route_memo: Optional[str]) -> dict:
    """Extract regulatory jurisdiction notes from a route memo."""
    notes = {j: {"readiness": "Unknown", "first_question": "", "blocker": ""} for j in JURISDICTIONS}

    if not route_memo:
        return notes

    # Look for jurisdiction table
    in_table = False
    for line in route_memo.splitlines():
        if "Jurisdiction" in line and "First Practical Question" in line:
            in_table = True
            continue

        if in_table and line.startswith("|"):
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) >= 4 and "---" not in line:
                jurisdiction = cells[0]
                for j in JURISDICTIONS:
                    if j.split("/")[0].strip().lower() in jurisdiction.lower():
                        notes[j] = {
                            "readiness": "Medium" if "medium" in cells[2].lower() else "Low" if "low" in cells[2].lower() else "High",
                            "first_question": cells[1][:100],
                            "blocker": cells[3][:100] if len(cells) > 3 else "",
                        }
                        break

        if in_table and line.startswith("## ") and "Jurisdiction" not in line:
            break

    return notes


def _generate_executive_summary(disease: str, branch: str, claim_cards: list[ClaimEvidenceCard]) -> str:
    """Generate executive summary from claim evaluations."""
    supported = sum(1 for c in claim_cards if c.verdict == "supported")
    partial = sum(1 for c in claim_cards if c.verdict == "partially_supported")
    unsupported = sum(1 for c in claim_cards if c.verdict in ["not_supported", "absent"])

    total = len(claim_cards)

    if total == 0:
        return f"No claims evaluated for {disease.upper()} {branch}. Additional claim evaluation needed."

    if supported > partial + unsupported:
        strength = "strong"
        direction = "Go with caution"
    elif partial >= supported:
        strength = "moderate but incomplete"
        direction = "Conditional Go pending gaps"
    else:
        strength = "weak"
        direction = "Hold until evidence improves"

    return f"""Evidence for {disease.upper()} {branch} is {strength}. Of {total} key claims evaluated: {supported} supported, {partial} partially supported, {unsupported} unsupported/absent.

**Recommendation:** {direction}"""


def _generate_go_no_go(claim_cards: list[ClaimEvidenceCard], endpoint_memo: Optional[EndpointDecisionMemo]) -> str:
    """Generate go/no-go implication."""
    if not claim_cards:
        return "**HOLD** — Insufficient evidence evaluation. Generate claim evidence cards first."

    supported = sum(1 for c in claim_cards if c.verdict == "supported")
    total = len(claim_cards)
    support_ratio = supported / total if total > 0 else 0

    has_endpoints = endpoint_memo and len(endpoint_memo.core_endpoints) >= 3
    has_sources = any(len(c.key_sources) >= 3 for c in claim_cards)

    if support_ratio >= 0.6 and has_endpoints and has_sources:
        return """**CONDITIONAL GO**

Conditions:
1. Address gaps in missing evidence section
2. Validate regulatory path before pivotal investment
3. Position as adjunct/support rather than standalone (unless evidence strengthens)

Kill signals:
- Competitor captures category with stronger label
- Novel biomarker makes current endpoints obsolete
- Regulatory path cannot be resolved in 12 months"""

    elif support_ratio >= 0.3:
        return """**HOLD — Evidence incomplete**

Required before Go:
1. Resolve critical gaps in evidence backbone
2. Add more primary studies to support key claims
3. Clarify regulatory category positioning

Do not invest in pivotal trials until gaps are addressed."""

    else:
        return """**NO GO — Evidence too thin**

Current evidence does not support investment:
- Key claims lack source support
- Endpoint clarity insufficient
- Regulatory path unclear

Revisit after:
1. New primary studies published
2. Systematic evidence synthesis completed
3. Regulatory landscape clarified"""


def _identify_gaps(claim_cards: list[ClaimEvidenceCard], endpoint_memo: Optional[EndpointDecisionMemo], disease: str, branch: str) -> list[GapItem]:
    """Identify evidence gaps from claims and endpoints."""
    gaps = []
    gap_num = 1

    # Gaps from claim cards
    for card in claim_cards:
        if card.verdict in ["partially_supported", "not_supported", "absent"]:
            gaps.append(GapItem(
                gap_id=f"GAP-{disease.upper()[:1]}{gap_num}",
                description=f"Claim '{card.claim[:50]}...' is {card.verdict}",
                impact=f"Weakens {branch} evidence backbone",
                priority="P1" if card.verdict == "absent" else "P2",
                suggested_search=f"Search for {disease} studies on: {' '.join(card.claim.split()[:5])}",
            ))
            gap_num += 1

        for missing in card.missing_evidence[:2]:
            gaps.append(GapItem(
                gap_id=f"GAP-{disease.upper()[:1]}{gap_num}",
                description=missing,
                impact="Reduces claim confidence",
                priority="P2",
                suggested_search=f"Search for primary {disease} studies",
            ))
            gap_num += 1

    # Gaps from endpoint memo
    if endpoint_memo:
        for missing in endpoint_memo.missing_evidence[:2]:
            gaps.append(GapItem(
                gap_id=f"GAP-{disease.upper()[:1]}{gap_num}",
                description=missing,
                impact="Endpoint hierarchy incomplete",
                priority="P2",
                suggested_search=f"Search for {disease} endpoint validation studies",
            ))
            gap_num += 1

    return gaps[:10]  # Limit to top 10 gaps


def generate_opportunity_brief(
    disease: str,
    branch: str,
    key_claims: Optional[list[str]] = None,
) -> OpportunityBrief:
    """
    Generate a complete opportunity brief.

    Args:
        disease: Disease code (ckd, fip, etc.)
        branch: Specific branch/opportunity (e.g., "phosphorus control", "GS-441524")
        key_claims: Optional list of claims to evaluate (auto-generated if None)

    Returns:
        OpportunityBrief with all sections populated
    """
    disease_lower = disease.lower()
    maturity_info = DISEASE_MATURITY.get(disease_lower, {"maturity": "Unknown"})

    # Generate default claims if not provided
    if not key_claims:
        key_claims = [
            f"{branch} has strong evidence support for {disease.upper()}",
            f"{branch} improves outcomes in feline {disease.upper()}",
            f"{branch} is a viable treatment approach for {disease.upper()}",
        ]

    # Evaluate each claim
    claim_cards = []
    for claim in key_claims:
        card = evaluate_claim(disease_lower, claim)
        claim_cards.append(card)

    # Generate endpoint memo
    endpoint_memo = generate_endpoint_memo(disease_lower, use_case="general")

    # Find and parse route memo
    route_memo_content = _find_route_memo(disease_lower, branch)
    regulatory_notes = _extract_regulatory_notes(route_memo_content)

    # Build evidence backbone
    all_sources = set()
    for card in claim_cards:
        all_sources.update(card.key_sources)
    if endpoint_memo:
        all_sources.update(endpoint_memo.source_appendix)

    evidence_backbone = []
    for card in claim_cards:
        evidence_backbone.append({
            "claim": card.claim,
            "verdict": card.verdict,
            "level": card.claim_level,
            "sources": card.key_sources[:3],
        })

    # Build key claims table
    key_claims_table = []
    for i, card in enumerate(claim_cards, 1):
        key_claims_table.append({
            "id": f"KC{i}",
            "claim": card.claim,
            "level": card.claim_level,
            "sources": ", ".join(card.key_sources[:3]),
            "boundary": card.boundary[0] if card.boundary else "",
        })

    # Collect missing evidence
    missing_evidence = []
    for card in claim_cards:
        missing_evidence.extend(card.missing_evidence)
    if endpoint_memo:
        missing_evidence.extend(endpoint_memo.missing_evidence)
    missing_evidence = list(set(missing_evidence))[:5]

    # Identify gaps
    gaps = _identify_gaps(claim_cards, endpoint_memo, disease_lower, branch)

    return OpportunityBrief(
        disease=disease.upper(),
        branch=branch,
        business_question=f"Is feline {disease.upper()} {branch} a viable product opportunity?",
        executive_summary=_generate_executive_summary(disease_lower, branch, claim_cards),
        go_no_go=_generate_go_no_go(claim_cards, endpoint_memo),
        evidence_backbone=evidence_backbone,
        key_claims=key_claims_table,
        endpoint_memo=endpoint_memo,
        regulatory_notes=regulatory_notes,
        missing_evidence=missing_evidence,
        gaps=gaps,
        source_appendix=sorted(list(all_sources)),
        generated_at=date.today().isoformat(),
        maturity=maturity_info.get("maturity", "Unknown"),
    )


def format_brief_markdown(brief: OpportunityBrief) -> str:
    """Format an OpportunityBrief as markdown."""
    lines = [
        "---",
        f"id: business-{brief.disease.lower()}-{brief.branch.replace(' ', '-').lower()}-opportunity-brief-{brief.generated_at.replace('-', '')}",
        "type: business",
        "artifact_kind: opportunity_brief",
        f"disease_branch: {brief.disease} / {brief.branch}",
        f"created_at: {brief.generated_at}",
        "owner: opportunity_brief_generator",
        "status: draft",
        "verification_status: auto_generated",
        "decision_grade: no",
        "---",
        "",
        f"# Opportunity Brief: Feline {brief.disease} {brief.branch.title()}",
        "",
        f"**Date:** {brief.generated_at}",
        f"**Disease Branch:** Feline {brief.disease} — {brief.branch.title()}",
        f"**Business Question:** {brief.business_question}",
        f"**Disease Maturity:** {brief.maturity}",
        "",
        "---",
        "",
        "## Executive Summary",
        "",
        brief.executive_summary,
        "",
        "---",
        "",
        "## Go/No-Go Implication",
        "",
        brief.go_no_go,
        "",
        "---",
        "",
        "## Evidence Backbone",
        "",
        "| Claim | Verdict | Level | Key Sources |",
        "|-------|---------|-------|-------------|",
    ]

    for eb in brief.evidence_backbone:
        sources = ", ".join(eb["sources"])
        lines.append(f"| {eb['claim'][:50]}... | {eb['verdict']} | {eb['level']} | {sources} |")

    lines.extend([
        "",
        "## Key-Claim Traceability",
        "",
        "| ID | Claim | Level | Sources | Boundary |",
        "|----|-------|-------|---------|----------|",
    ])

    for kc in brief.key_claims:
        lines.append(f"| {kc['id']} | {kc['claim'][:40]}... | {kc['level']} | {kc['sources'][:25]}... | {kc['boundary'][:30]}... |")

    lines.extend([
        "",
        "---",
        "",
        "## Endpoint Maturity",
        "",
    ])

    if brief.endpoint_memo:
        lines.append(f"**Primary Recommendation:** {brief.endpoint_memo.primary_recommendation}")
        lines.append("")
        lines.append("**Secondary Recommendations:**")
        for rec in brief.endpoint_memo.secondary_recommendations:
            lines.append(f"- {rec}")
        lines.append("")
        lines.append(f"**Core Endpoints:** {len(brief.endpoint_memo.core_endpoints)}")
        lines.append(f"**Support Endpoints:** {len(brief.endpoint_memo.support_endpoints)}")
    else:
        lines.append("_Endpoint memo not available for this disease._")

    lines.extend([
        "",
        "---",
        "",
        "## Regulatory Path Notes",
        "",
        "| Jurisdiction | Readiness | First Question | Blocker |",
        "|--------------|-----------|----------------|---------|",
    ])

    for j, notes in brief.regulatory_notes.items():
        lines.append(f"| {j} | {notes['readiness']} | {notes['first_question'][:40]}... | {notes['blocker'][:30]}... |")

    lines.extend([
        "",
        "---",
        "",
        "## Missing Evidence",
        "",
    ])

    for me in brief.missing_evidence:
        lines.append(f"- {me}")

    lines.extend([
        "",
        "## Gap-to-Intake Queue",
        "",
        "| Gap ID | Description | Impact | Priority | Suggested Search |",
        "|--------|-------------|--------|----------|------------------|",
    ])

    for gap in brief.gaps[:5]:
        lines.append(f"| {gap.gap_id} | {gap.description[:40]}... | {gap.impact[:30]}... | {gap.priority} | {gap.suggested_search[:30]}... |")

    lines.extend([
        "",
        "---",
        "",
        "## Source Appendix",
        "",
    ])

    for src in brief.source_appendix[:15]:
        lines.append(f"- `{src}`")
    if len(brief.source_appendix) > 15:
        lines.append(f"- _... and {len(brief.source_appendix) - 15} more_")

    lines.extend([
        "",
        "---",
        "",
        "## Document Metadata",
        "",
        "| Field | Value |",
        "|-------|-------|",
        "| Generated by | Opportunity Brief Generator |",
        f"| Generation date | {brief.generated_at} |",
        f"| Disease maturity | {brief.maturity} |",
        "| Decision grade | No — auto-generated, not audited |",
    ])

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate opportunity briefs for disease branches.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--disease", "-d",
        required=True,
        choices=list(DISEASE_MATURITY.keys()),
        help="Disease code",
    )
    parser.add_argument(
        "--branch", "-b",
        required=True,
        help="Branch/opportunity to evaluate (e.g., 'phosphorus control', 'GS-441524')",
    )
    parser.add_argument(
        "--claims", "-c",
        nargs="+",
        help="Specific claims to evaluate (optional)",
    )
    parser.add_argument(
        "--output", "-o",
        help="Write to file instead of stdout",
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output as JSON instead of markdown",
    )
    args = parser.parse_args()

    brief = generate_opportunity_brief(args.disease, args.branch, args.claims)

    if args.json:
        # Convert to JSON-serializable
        output = {
            "disease": brief.disease,
            "branch": brief.branch,
            "business_question": brief.business_question,
            "executive_summary": brief.executive_summary,
            "go_no_go": brief.go_no_go,
            "evidence_backbone": brief.evidence_backbone,
            "key_claims": brief.key_claims,
            "regulatory_notes": brief.regulatory_notes,
            "missing_evidence": brief.missing_evidence,
            "gaps": [{"gap_id": g.gap_id, "description": g.description, "priority": g.priority} for g in brief.gaps],
            "source_appendix": brief.source_appendix,
            "generated_at": brief.generated_at,
            "maturity": brief.maturity,
        }
        text = json.dumps(output, indent=2)
    else:
        text = format_brief_markdown(brief)

    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"Written to {args.output}")
    else:
        print(text)


if __name__ == "__main__":
    main()
