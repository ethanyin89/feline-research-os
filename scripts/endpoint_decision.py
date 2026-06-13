#!/usr/bin/env python3
"""
scripts/endpoint_decision.py — Endpoint Decision Memo Generator for feline research OS.

Generates structured endpoint decision memos for diseases, showing:
- Endpoint hierarchy (core, support, context tiers)
- Primary/secondary endpoint recommendations
- Measurement protocols
- Regulatory precedent
- Key-Claim Traceability

Usage:
    python scripts/endpoint_decision.py --disease ckd
    python scripts/endpoint_decision.py --disease fip --use-case trial_design

Usage (imported):
    from endpoint_decision import generate_endpoint_memo
    memo = generate_endpoint_memo("ckd", use_case="monitoring")
"""

import argparse
import json
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional
from source_inventory import format_source_inventory, get_source_inventory

VAULT_ROOT = Path(__file__).parent.parent

SUPPORTED_DISEASES = ("ckd", "fip", "hcm", "ibd", "fcv", "diabetes", "obesity", "cancer")


@dataclass
class Endpoint:
    """Single endpoint definition."""
    name: str
    tier: str  # core, support, context
    primary_use: str
    key_boundary: str
    source_ids: list[str]
    measurement_notes: str = ""
    regulatory_precedent: str = ""


@dataclass
class EndpointDecisionMemo:
    """Structured endpoint decision memo."""
    disease: str
    use_case: str
    maturity: str
    core_endpoints: list[Endpoint]
    support_endpoints: list[Endpoint]
    context_endpoints: list[Endpoint]
    primary_recommendation: str
    secondary_recommendations: list[str]
    key_claims: list[dict]
    boundary: list[str]
    missing_evidence: list[str]
    source_appendix: list[str]


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
            if val.startswith("[") and val.endswith("]"):
                val = [v.strip().strip("\"'") for v in val[1:-1].split(",") if v.strip()]
            fm[key] = val
    return fm


def _extract_endpoints_from_handbook(content: str) -> list[Endpoint]:
    """Extract endpoint definitions from an endpoint handbook page."""
    endpoints = []
    current_tier = "core"
    current_endpoint = None

    lines = content.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]

        # Detect tier changes
        if "Core Tier" in line:
            current_tier = "core"
        elif "Support Tier" in line:
            current_tier = "support"
        elif "Context Tier" in line:
            current_tier = "context"

        # Detect endpoint headers - handle both formats:
        # Format 1: **Endpoint N: Name**
        # Format 2: ### Endpoint N: Name
        endpoint_match = None
        if line.startswith("**Endpoint") and ":" in line:
            endpoint_match = re.search(r'\*\*Endpoint \d+: (.+?)\*\*', line)
        elif line.startswith("### Endpoint") and ":" in line:
            endpoint_match = re.search(r'### Endpoint \d+: (.+)', line)

        if endpoint_match:
            # Save previous endpoint
            if current_endpoint:
                endpoints.append(current_endpoint)

            name = endpoint_match.group(1).strip()
            current_endpoint = Endpoint(
                name=name,
                tier=current_tier,
                primary_use="",
                key_boundary="",
                source_ids=[],
            )

        # Parse endpoint details
        if current_endpoint:
            if line.startswith("Primary use:"):
                current_endpoint.primary_use = line.replace("Primary use:", "").strip()
            elif line.startswith("**Key boundary:**"):
                current_endpoint.key_boundary = line.replace("**Key boundary:**", "").strip()
            elif line.startswith("**Lead sources:**"):
                sources_text = line.replace("**Lead sources:**", "").strip()
                current_endpoint.source_ids = re.findall(r'src-[a-z]+-\d{3}', sources_text)
            # Also check for description paragraph after header (for FIP-style format)
            elif current_endpoint and not current_endpoint.primary_use and line.strip() and not line.startswith("#") and not line.startswith("**") and not line.startswith("|"):
                if "boundary" not in line.lower() and "sources" not in line.lower():
                    current_endpoint.primary_use = line.strip()[:200]

        i += 1

    # Don't forget the last endpoint
    if current_endpoint:
        endpoints.append(current_endpoint)

    return endpoints


def _extract_key_claims(content: str) -> list[dict]:
    """Extract Key-Claim Traceability from content."""
    claims = []
    in_table = False

    for line in content.splitlines():
        if "Key-Claim Traceability" in line:
            in_table = True
            continue

        if in_table and line.startswith("|"):
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) >= 4 and "---" not in line and cells[0].lower() not in ["id", "claim id"]:
                claims.append({
                    "id": cells[0],
                    "claim": cells[1],
                    "level": cells[2],
                    "sources": cells[3],
                    "boundary": cells[4] if len(cells) > 4 else "",
                })
        elif in_table and line.startswith("## ") and "Key-Claim" not in line:
            break

    return claims


def load_endpoint_handbook(disease: str) -> Optional[str]:
    """Load the endpoint handbook for a disease."""
    handbook_path = VAULT_ROOT / "topics" / disease.lower() / "endpoint-handbook.md"
    if not handbook_path.exists():
        # Try alternate names
        for alt in ["endpoint.md", "endpoints.md"]:
            alt_path = VAULT_ROOT / "topics" / disease.lower() / alt
            if alt_path.exists():
                handbook_path = alt_path
                break

    if not handbook_path.exists():
        return None

    try:
        return handbook_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


def generate_endpoint_memo(disease: str, use_case: str = "general") -> EndpointDecisionMemo:
    """
    Generate an endpoint decision memo for a disease.

    Args:
        disease: Disease code (ckd, fip, hcm, etc.)
        use_case: Context for recommendations (general, trial_design, monitoring, diagnosis)

    Returns:
        EndpointDecisionMemo with structured endpoint recommendations
    """
    disease_lower = disease.lower()
    inventory = get_source_inventory(VAULT_ROOT, disease_lower)
    inventory_label = format_source_inventory(inventory)

    # Load endpoint handbook
    handbook_content = load_endpoint_handbook(disease_lower)

    endpoints = []
    key_claims = []
    source_ids = set()

    if handbook_content:
        endpoints = _extract_endpoints_from_handbook(handbook_content)
        key_claims = _extract_key_claims(handbook_content)

        # Extract source IDs from frontmatter
        fm = _parse_frontmatter(handbook_content)
        if isinstance(fm.get("source_ids"), list):
            source_ids.update(fm["source_ids"])

    # Also collect source IDs from endpoints
    for ep in endpoints:
        source_ids.update(ep.source_ids)

    # Categorize endpoints by tier
    core_endpoints = [e for e in endpoints if e.tier == "core"]
    support_endpoints = [e for e in endpoints if e.tier == "support"]
    context_endpoints = [e for e in endpoints if e.tier == "context"]

    # Generate recommendations based on use case
    if use_case == "trial_design":
        primary = "Use survival/progression as primary if feasible; otherwise, composite of core endpoints"
        secondary = [
            "Creatinine stability or reduction",
            "Proteinuria reduction (UPCR)",
            "Blood pressure control",
        ]
    elif use_case == "monitoring":
        primary = "Creatinine trend from baseline with serial surveillance"
        secondary = [
            "UPCR for proteinuria monitoring",
            "Phosphorus for mineral burden",
            "Blood pressure at each visit",
        ]
    elif use_case == "diagnosis":
        primary = "Creatinine + USG for initial diagnosis"
        secondary = [
            "SDMA as adjunctive early detection aid",
            "UPCR for substaging",
            "Blood pressure for hypertension substaging",
        ]
    else:  # general
        if core_endpoints:
            primary = f"Core operational endpoints: {', '.join(e.name for e in core_endpoints[:3])}"
        else:
            primary = "Core endpoints not yet compiled for this disease"
        secondary = [e.name for e in support_endpoints[:3]] if support_endpoints else ["Support endpoints not yet compiled"]

    # Identify boundaries
    boundary = []
    for ep in core_endpoints:
        if ep.key_boundary:
            boundary.append(f"[{ep.name}] {ep.key_boundary}")

    if not boundary:
        boundary = ["No explicit endpoint boundaries found in compiled sources"]

    # Identify missing evidence
    missing = []
    if not handbook_content:
        missing.append(f"No endpoint handbook found for {disease.upper()}")
    if len(core_endpoints) < 3:
        missing.append(f"Only {len(core_endpoints)} core endpoints defined")
    if inventory["verification_status"]["title_only"] or inventory["verification_status"]["abstract_weighted"]:
        missing.append("Some source cards remain title-only or abstract-weighted")

    return EndpointDecisionMemo(
        disease=disease.upper(),
        use_case=use_case,
        maturity=inventory_label,
        core_endpoints=core_endpoints,
        support_endpoints=support_endpoints,
        context_endpoints=context_endpoints,
        primary_recommendation=primary,
        secondary_recommendations=secondary,
        key_claims=key_claims[:6],  # Top 6 claims
        boundary=boundary[:5],
        missing_evidence=missing,
        source_appendix=sorted(list(source_ids)),
    )


def format_memo_markdown(memo: EndpointDecisionMemo) -> str:
    """Format an EndpointDecisionMemo as markdown."""
    lines = [
        f"# Endpoint Decision Memo: {memo.disease}",
        "",
        f"**Disease:** {memo.disease}",
        f"**Use Case:** {memo.use_case}",
        f"**Disease Maturity:** {memo.maturity}",
        "",
        "---",
        "",
        "## Primary Recommendation",
        "",
        f"{memo.primary_recommendation}",
        "",
        "## Secondary Recommendations",
        "",
    ]

    for rec in memo.secondary_recommendations:
        lines.append(f"- {rec}")

    lines.extend([
        "",
        "---",
        "",
        "## Endpoint Hierarchy",
        "",
        "### Core Tier (Operational Endpoints)",
        "",
    ])

    if memo.core_endpoints:
        lines.append("| Endpoint | Primary Use | Boundary | Sources |")
        lines.append("|----------|-------------|----------|---------|")
        for ep in memo.core_endpoints:
            sources = ", ".join(ep.source_ids[:3]) if ep.source_ids else "—"
            lines.append(f"| {ep.name} | {ep.primary_use[:50]}... | {ep.key_boundary[:40]}... | {sources} |")
    else:
        lines.append("_No core endpoints compiled for this disease._")

    lines.extend([
        "",
        "### Support Tier (Early Detection / Adjunctive)",
        "",
    ])

    if memo.support_endpoints:
        lines.append("| Endpoint | Primary Use | Boundary | Sources |")
        lines.append("|----------|-------------|----------|---------|")
        for ep in memo.support_endpoints:
            sources = ", ".join(ep.source_ids[:3]) if ep.source_ids else "—"
            lines.append(f"| {ep.name} | {ep.primary_use[:50]}... | {ep.key_boundary[:40]}... | {sources} |")
    else:
        lines.append("_No support endpoints compiled for this disease._")

    lines.extend([
        "",
        "### Context Tier (Interpretation Markers)",
        "",
    ])

    if memo.context_endpoints:
        lines.append("| Endpoint | Primary Use | Boundary | Sources |")
        lines.append("|----------|-------------|----------|---------|")
        for ep in memo.context_endpoints:
            sources = ", ".join(ep.source_ids[:3]) if ep.source_ids else "—"
            lines.append(f"| {ep.name} | {ep.primary_use[:50]}... | {ep.key_boundary[:40]}... | {sources} |")
    else:
        lines.append("_No context endpoints compiled for this disease._")

    lines.extend([
        "",
        "---",
        "",
        "## Key-Claim Traceability",
        "",
    ])

    if memo.key_claims:
        lines.append("| ID | Claim | Level | Sources |")
        lines.append("|-----|-------|-------|---------|")
        for claim in memo.key_claims:
            lines.append(f"| {claim['id']} | {claim['claim'][:60]}... | {claim['level']} | {claim['sources'][:30]}... |")
    else:
        lines.append("_No key claims compiled for this disease._")

    lines.extend([
        "",
        "---",
        "",
        "## Boundary",
        "",
    ])

    for b in memo.boundary:
        lines.append(f"- {b}")

    if memo.missing_evidence:
        lines.extend([
            "",
            "## Missing Evidence",
            "",
        ])
        for m in memo.missing_evidence:
            lines.append(f"- {m}")

    lines.extend([
        "",
        "---",
        "",
        "## Source Appendix",
        "",
    ])

    if memo.source_appendix:
        for src in memo.source_appendix[:10]:
            lines.append(f"- `{src}`")
        if len(memo.source_appendix) > 10:
            lines.append(f"- _... and {len(memo.source_appendix) - 10} more_")
    else:
        lines.append("_No sources compiled._")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate endpoint decision memos for diseases.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--disease", "-d",
        required=True,
        choices=list(SUPPORTED_DISEASES),
        help="Disease code",
    )
    parser.add_argument(
        "--use-case", "-u",
        choices=["general", "trial_design", "monitoring", "diagnosis"],
        default="general",
        help="Use case context for recommendations",
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output as JSON instead of markdown",
    )
    parser.add_argument(
        "--output", "-o",
        help="Write to file instead of stdout",
    )
    args = parser.parse_args()

    memo = generate_endpoint_memo(args.disease, args.use_case)

    if args.json:
        # Convert to JSON-serializable format
        output = {
            "disease": memo.disease,
            "use_case": memo.use_case,
            "maturity": memo.maturity,
            "primary_recommendation": memo.primary_recommendation,
            "secondary_recommendations": memo.secondary_recommendations,
            "core_endpoints": [asdict(e) for e in memo.core_endpoints],
            "support_endpoints": [asdict(e) for e in memo.support_endpoints],
            "context_endpoints": [asdict(e) for e in memo.context_endpoints],
            "key_claims": memo.key_claims,
            "boundary": memo.boundary,
            "missing_evidence": memo.missing_evidence,
            "source_appendix": memo.source_appendix,
        }
        text = json.dumps(output, indent=2)
    else:
        text = format_memo_markdown(memo)

    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"Written to {args.output}")
    else:
        print(text)


if __name__ == "__main__":
    main()
