#!/usr/bin/env python3
"""
scripts/partner_dossier.py — Partner-facing evidence dossier generator.

Combines opportunity briefs, endpoint memos, and claim evidence into a
single exportable package for partner meetings, diligence, and collaboration.

Usage:
    python scripts/partner_dossier.py --disease ckd --partner "Acme Pharma"
    python scripts/partner_dossier.py --disease fip --format pdf --output dossier.pdf

Usage (imported):
    from partner_dossier import generate_dossier
    dossier = generate_dossier("ckd", partner_name="Acme Pharma")
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional

VAULT_ROOT = Path(__file__).parent.parent

# Import business decision tools
from claim_evidence import evaluate_claim, ClaimEvidenceCard
from endpoint_decision import generate_endpoint_memo, EndpointDecisionMemo
from opportunity_brief import generate_opportunity_brief, OpportunityBrief
from source_inventory import format_source_inventory, get_source_inventory


@dataclass
class DossierSection:
    """A section of the partner dossier."""
    title: str
    content: str
    source_type: str  # opportunity_brief, endpoint_memo, claim_evidence, custom


@dataclass
class PartnerDossier:
    """Complete partner-facing evidence dossier."""
    disease: str
    partner_name: str
    prepared_date: str
    maturity_level: str
    source_count: int
    extraction_status: str

    executive_summary: str
    sections: list[DossierSection]
    source_appendix: list[str]
    boundary_warnings: list[str]
    next_steps: list[str]

    # Metadata
    claims_verified: int
    claims_supported: int
    claims_partial: int
    claims_unsupported: int


def generate_executive_summary(
    disease: str,
    brief: OpportunityBrief,
    memo: EndpointDecisionMemo,
    maturity_info: dict,
) -> str:
    """Generate executive summary from available artifacts."""
    lines = [
        f"# Executive Summary: {disease.upper()} Opportunity",
        "",
        f"**Prepared for:** Partner review",
        f"**Date:** {date.today().isoformat()}",
        f"**Evidence maturity:** {maturity_info.get('maturity', 'Unknown')} ({maturity_info.get('sources', 0)} sources, {maturity_info.get('extraction', 'unknown')} extraction)",
        "",
        "## Key Findings",
        "",
    ]

    # Add opportunity assessment
    go_no_go = getattr(brief, 'go_no_go', '') or getattr(brief, 'go_no_go_implication', '')
    if go_no_go:
        lines.append(f"**Strategic Assessment:** {go_no_go[:200]}...")
        lines.append("")

    # Add endpoint readiness
    if memo.core_endpoints:
        endpoint_names = [e.name for e in memo.core_endpoints[:3]]
        lines.append(f"**Core Endpoints:** {', '.join(endpoint_names)}")
        lines.append("")

    # Add evidence gaps
    missing = getattr(brief, 'missing_evidence', []) or []
    if missing:
        lines.append("**Evidence Gaps:**")
        for gap in missing[:3]:
            lines.append(f"- {gap}")
        lines.append("")

    return "\n".join(lines)


def generate_dossier(
    disease: str,
    partner_name: str = "Partner",
    key_claims: Optional[list[str]] = None,
    include_source_cards: bool = False,
) -> PartnerDossier:
    """
    Generate a complete partner-facing dossier.

    Args:
        disease: Disease code (ckd, fip, etc.)
        partner_name: Name for document header
        key_claims: Optional list of claims to verify
        include_source_cards: Whether to include full source card content

    Returns:
        PartnerDossier with all sections
    """
    disease_lower = disease.lower()
    inventory = get_source_inventory(VAULT_ROOT, disease_lower)
    maturity_info = {
        "sources": inventory["total"],
        "extraction": "inventory_only",
        "maturity": format_source_inventory(inventory),
    }

    sections = []
    all_sources = set()
    boundary_warnings = []

    # Automatic opportunity generation is disabled. A specific Research Case
    # must provide the branch, explicit claims, and human review.
    brief = None
    sections.append(DossierSection(
        title="Legacy Opportunity Brief",
        content=(
            "_Automatic opportunity generation is disabled. Admit explicit "
            "sources and claims into a Research Case for human review._"
        ),
        source_type="legacy_unreviewed",
    ))

    # Generate endpoint memo
    try:
        memo = generate_endpoint_memo(disease_lower, use_case="general")
        sections.append(DossierSection(
            title="Endpoint Decision Memo",
            content=_format_endpoint_section(memo),
            source_type="endpoint_memo",
        ))
        all_sources.update(memo.source_appendix)
        boundary_warnings.extend(memo.boundary)
    except Exception as e:
        memo = None
        sections.append(DossierSection(
            title="Endpoint Decision Memo",
            content=f"_Endpoint memo not available: {e}_",
            source_type="endpoint_memo",
        ))

    # Retrieve candidate evidence if explicit claims are provided.
    claims_verified = 0
    claims_supported = 0
    claims_partial = 0
    claims_unsupported = 0

    if key_claims:
        claim_section_lines = [
            "## Candidate Evidence Retrieval",
            "",
            "> Candidate retrieval only. Human review is required.",
            "",
        ]
        for claim in key_claims:
            try:
                card = evaluate_claim(disease_lower, claim)
                claims_verified += 1
                verdict = card.verdict if isinstance(card.verdict, str) else card.verdict.value

                if verdict == "candidate_matches_found":
                    icon = "CANDIDATES"
                else:
                    icon = "NO MATCHES"

                claim_section_lines.append(f"### [{icon}] {claim[:60]}{'...' if len(claim) > 60 else ''}")
                claim_section_lines.append("")
                claim_section_lines.append(f"**Candidate status:** {verdict}")
                claim_section_lines.append(f"**Candidate sources:** {', '.join(card.key_sources[:3])}")
                claim_section_lines.append("")
                all_sources.update(card.key_sources)

            except Exception as e:
                claim_section_lines.append(f"### ⚠️ {claim[:60]}...")
                claim_section_lines.append(f"_Could not verify: {e}_")
                claim_section_lines.append("")

        sections.append(DossierSection(
            title="Candidate Evidence Retrieval",
            content="\n".join(claim_section_lines),
            source_type="claim_evidence",
        ))

    # Generate executive summary
    # Create minimal fallback objects if needed
    fallback_brief = None
    if brief is None:
        # Create a minimal dict-like object for the summary generator
        class MinimalBrief:
            go_no_go_implication = ""
            missing_evidence = []
        fallback_brief = MinimalBrief()

    fallback_memo = None
    if memo is None:
        class MinimalMemo:
            core_endpoints = []
        fallback_memo = MinimalMemo()

    exec_summary = generate_executive_summary(
        disease,
        brief or fallback_brief,
        memo or fallback_memo,
        maturity_info,
    )

    # Generate next steps
    next_steps = []
    if brief and brief.missing_evidence:
        next_steps.append(f"Fill evidence gaps: {len(brief.missing_evidence)} gaps identified")
    if claims_verified > 0:
        next_steps.append(f"Human-review candidate evidence for {claims_verified} claims")
    next_steps.append("Review source-depth distribution; inventory count is not readiness")

    return PartnerDossier(
        disease=disease.upper(),
        partner_name=partner_name,
        prepared_date=date.today().isoformat(),
        maturity_level=maturity_info.get("maturity", "Unknown"),
        source_count=maturity_info.get("sources", 0),
        extraction_status=maturity_info.get("extraction", "unknown"),
        executive_summary=exec_summary,
        sections=sections,
        source_appendix=sorted(list(all_sources)),
        boundary_warnings=boundary_warnings,
        next_steps=next_steps,
        claims_verified=claims_verified,
        claims_supported=claims_supported,
        claims_partial=claims_partial,
        claims_unsupported=claims_unsupported,
    )


def _format_brief_section(brief: OpportunityBrief) -> str:
    """Format opportunity brief as dossier section."""
    lines = [
        "## Opportunity Brief",
        "",
        f"**Disease Branch:** {brief.disease}",
        f"**Maturity:** {brief.maturity}",
        "",
        "### Executive Summary",
        "",
        brief.executive_summary or "_Not available_",
        "",
        "### Evidence Backbone",
        "",
    ]

    for item in brief.evidence_backbone[:5]:
        if isinstance(item, dict):
            lines.append(f"- {item.get('finding', str(item))}")
        else:
            lines.append(f"- {item}")

    lines.extend([
        "",
        "### Regulatory Notes",
        "",
    ])

    if isinstance(brief.regulatory_notes, dict):
        for key, value in list(brief.regulatory_notes.items())[:3]:
            lines.append(f"- **{key}:** {value}")
    else:
        lines.append(brief.regulatory_notes or "_Not assessed_")

    lines.extend([
        "",
        "### Automated Decision Status",
        "",
        f"**{brief.go_no_go}**" if brief.go_no_go else "_Not assessed_",
        "",
    ])

    return "\n".join(lines)


def _format_endpoint_section(memo: EndpointDecisionMemo) -> str:
    """Format endpoint memo as dossier section."""
    lines = [
        "## Endpoint Decision Memo",
        "",
        f"**Disease:** {memo.disease}",
        f"**Use Case:** {memo.use_case}",
        f"**Maturity:** {memo.maturity}",
        "",
        "### Primary Recommendation",
        "",
        memo.primary_recommendation or "_Not available_",
        "",
        "### Secondary Recommendations",
        "",
    ]

    for rec in memo.secondary_recommendations[:3]:
        lines.append(f"- {rec}")

    lines.extend([
        "",
        "### Core Endpoints",
        "",
    ])

    if memo.core_endpoints:
        lines.append("| Endpoint | Primary Use |")
        lines.append("|----------|-------------|")
        for ep in memo.core_endpoints[:5]:
            lines.append(f"| {ep.name} | {ep.primary_use[:50]}... |")
    else:
        lines.append("_No core endpoints defined_")

    return "\n".join(lines)


def format_dossier_markdown(dossier: PartnerDossier) -> str:
    """Format the complete dossier as markdown."""
    lines = [
        f"# Partner Dossier: {dossier.disease}",
        "",
        "---",
        "",
        f"**Prepared for:** {dossier.partner_name}",
        f"**Date:** {dossier.prepared_date}",
        f"**Evidence Maturity:** {dossier.maturity_level} ({dossier.source_count} sources, {dossier.extraction_status} extraction)",
        "",
        "---",
        "",
        dossier.executive_summary,
        "",
        "---",
        "",
    ]

    # Add all sections
    for section in dossier.sections:
        lines.append(section.content)
        lines.append("")
        lines.append("---")
        lines.append("")

    # Boundary warnings
    if dossier.boundary_warnings:
        lines.append("## Boundary Warnings")
        lines.append("")
        lines.append("_These limitations should be disclosed in partner communications:_")
        lines.append("")
        for warning in dossier.boundary_warnings[:5]:
            lines.append(f"- {warning}")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Next steps
    if dossier.next_steps:
        lines.append("## Recommended Next Steps")
        lines.append("")
        for i, step in enumerate(dossier.next_steps, 1):
            lines.append(f"{i}. {step}")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Claim summary
    if dossier.claims_verified > 0:
        lines.append("## Claim Verification Summary")
        lines.append("")
        lines.append(f"- **Verified:** {dossier.claims_verified}")
        lines.append(f"- **Claims searched:** {dossier.claims_verified}")
        lines.append("- **Semantic dispositions:** not assessed")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Source appendix
    lines.append("## Source Appendix")
    lines.append("")
    lines.append(f"This dossier draws from {len(dossier.source_appendix)} source cards:")
    lines.append("")
    for src in dossier.source_appendix[:20]:
        lines.append(f"- `{src}`")
    if len(dossier.source_appendix) > 20:
        lines.append(f"- _... and {len(dossier.source_appendix) - 20} more_")

    lines.extend([
        "",
        "---",
        "",
        "_Generated by Feline Research OS. Evidence is traceable to source cards._",
    ])

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate partner-facing evidence dossiers.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--disease", "-d",
        required=True,
        help="Disease code (ckd, fip, hcm, etc.)",
    )
    parser.add_argument(
        "--partner", "-p",
        default="Partner",
        help="Partner name for document header",
    )
    parser.add_argument(
        "--claims", "-c",
        nargs="+",
        help="Key claims to verify",
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path (default: outputs/dossiers/<disease>-dossier-<date>.md)",
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output as JSON instead of markdown",
    )
    args = parser.parse_args()

    dossier = generate_dossier(
        disease=args.disease,
        partner_name=args.partner,
        key_claims=args.claims,
    )

    if args.json:
        output = {
            "disease": dossier.disease,
            "partner_name": dossier.partner_name,
            "prepared_date": dossier.prepared_date,
            "maturity_level": dossier.maturity_level,
            "source_count": dossier.source_count,
            "extraction_status": dossier.extraction_status,
            "executive_summary": dossier.executive_summary,
            "sections": [{"title": s.title, "content": s.content, "source_type": s.source_type} for s in dossier.sections],
            "source_appendix": dossier.source_appendix,
            "boundary_warnings": dossier.boundary_warnings,
            "next_steps": dossier.next_steps,
            "claims_verified": dossier.claims_verified,
            "claims_supported": dossier.claims_supported,
            "claims_partial": dossier.claims_partial,
            "claims_unsupported": dossier.claims_unsupported,
        }
        text = json.dumps(output, indent=2)
    else:
        text = format_dossier_markdown(dossier)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(text, encoding="utf-8")
        print(f"Dossier written to {args.output}")
    else:
        # Default output path
        out_dir = VAULT_ROOT / "outputs" / "dossiers"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{args.disease.lower()}-dossier-{date.today().isoformat()}.md"
        out_path.write_text(text, encoding="utf-8")
        print(f"Dossier written to {out_path.relative_to(VAULT_ROOT)}")
        print()
        print(text)


if __name__ == "__main__":
    main()
