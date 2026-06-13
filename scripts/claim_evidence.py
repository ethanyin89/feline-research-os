#!/usr/bin/env python3
"""
scripts/claim_evidence.py — Candidate evidence retrieval for feline research OS.

Takes a disease + claim text and returns candidate matches with:
- verdict: candidate_matches_found / no_candidate_matches
- key_sources: source IDs with lexical overlap
- evidence_depth: number of sources, extraction level summary
- quoted_facts: direct quotes if available
- source_supported_conclusion: synthesized conclusion from sources
- boundary: what the claim does NOT cover
- next_action: human_review / search_more

Usage (CLI):
    python scripts/claim_evidence.py --disease ckd --claim "SDMA is the best biomarker for early CKD detection"

Usage (imported):
    from claim_evidence import evaluate_claim
    result = evaluate_claim("ckd", "SDMA is the best biomarker for early CKD detection")
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional

# Try relative import first, then absolute
try:
    from search import vault_search
except ImportError:
    try:
        from .search import vault_search
    except ImportError:
        vault_search = None

VAULT_ROOT = Path(__file__).parent.parent

# Evidence levels from claim-audit-protocol.md
CLAIM_LEVELS = {
    "A": "Source-Quoted (direct quote from source)",
    "B": "Source-Supported (inference supported by sources)",
    "C": "Working Inference (model/researcher judgment)",
    "D": "Decision-Grade (verified for high-risk use)",
}

# Verification status weights
VERIFICATION_WEIGHTS = {
    "audited": 1.0,
    "deep_extracted": 0.9,
    "source_checked": 0.7,
    "abstract_weighted": 0.4,
    "title_only": 0.1,
}

# Evidence level scores
EVIDENCE_LEVEL_SCORES = {
    "guideline": 10,
    "regulation": 9,
    "review": 8,
    "original-study": 7,
    "guidance": 6,
    "case-series": 5,
    "case-report": 3,
    "commentary": 2,
}


@dataclass
class SourceEvidence:
    """Evidence extracted from a single source card."""
    source_id: str
    title: str
    evidence_level: str
    verification_status: str
    weight_score: float
    quoted_facts: list[str] = field(default_factory=list)
    source_supported_conclusions: list[str] = field(default_factory=list)
    llm_inferences: list[str] = field(default_factory=list)
    limits: list[str] = field(default_factory=list)


@dataclass
class ClaimEvidenceCard:
    """Candidate retrieval output. It is not a semantic claim verdict."""
    claim: str
    disease: str
    verdict: str  # candidate_matches_found, no_candidate_matches
    verdict_confidence: str  # always not_assessed
    claim_level: str  # always candidate_only
    key_sources: list[str]
    evidence_depth: dict
    quoted_facts: list[dict]  # [{source_id, fact}]
    source_supported_conclusions: list[dict]  # [{source_id, conclusion}]
    boundary: list[str]
    missing_evidence: list[str]
    next_action: str  # human_review, search_more
    verification_path: str


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
            # Handle lists
            if val.startswith("[") and val.endswith("]"):
                val = [v.strip().strip("\"'") for v in val[1:-1].split(",") if v.strip()]
            fm[key] = val
    return fm


def _extract_evidence_policy(content: str) -> dict:
    """Extract evidence_policy from frontmatter."""
    if not content.startswith("---"):
        return {}
    end = content.find("\n---", 3)
    if end == -1:
        return {}

    fm_text = content[3:end]
    policy = {"quoted_fact": [], "source_supported_conclusion": [], "llm_inference": []}

    current_key = None
    for line in fm_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("quoted_fact:"):
            current_key = "quoted_fact"
        elif stripped.startswith("source_supported_conclusion:"):
            current_key = "source_supported_conclusion"
        elif stripped.startswith("llm_inference:"):
            current_key = "llm_inference"
        elif stripped.startswith("- ") and current_key:
            fact = stripped[2:].strip().strip("\"'")
            if fact:
                policy[current_key].append(fact)
        elif stripped and not stripped.startswith("-") and ":" in stripped:
            # New key, reset
            if not any(stripped.startswith(k) for k in ["quoted_fact", "source_supported_conclusion", "llm_inference"]):
                current_key = None

    return policy


def _extract_limits(content: str) -> list[str]:
    """Extract limits/caveats from the source card body."""
    limits = []
    in_limits = False

    for line in content.splitlines():
        if line.startswith("## Limits") or line.startswith("## Caveats"):
            in_limits = True
            continue
        if in_limits:
            if line.startswith("## "):
                break
            if line.startswith("- "):
                limits.append(line[2:].strip())

    return limits


def _compute_weight(evidence_level: str, verification_status: str) -> float:
    """Compute combined weight score for a source."""
    base = EVIDENCE_LEVEL_SCORES.get(evidence_level, 5)
    mult = VERIFICATION_WEIGHTS.get(verification_status, 0.5)
    return base * mult


def _tokenize_claim(claim: str) -> set[str]:
    """Extract key terms from a claim for matching."""
    # Remove common words and punctuation
    stopwords = {
        "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "will", "would", "could",
        "should", "may", "might", "must", "shall", "can", "for", "and", "or",
        "but", "in", "on", "at", "to", "from", "by", "with", "of", "that",
        "this", "it", "as", "if", "when", "than", "so", "no", "not", "only",
        "most", "best", "more", "less", "very", "too", "also", "such", "what",
        "which", "who", "how", "why", "where", "feline", "cat", "cats"
    }

    words = re.findall(r'\b[a-zA-Z0-9]+\b', claim.lower())
    return {w for w in words if w not in stopwords and len(w) > 2}


def _calculate_match_score(claim_tokens: set[str], text: str) -> float:
    """Calculate how well text matches claim tokens."""
    if not claim_tokens or not text:
        return 0.0

    text_lower = text.lower()
    matches = sum(1 for token in claim_tokens if token in text_lower)
    return matches / len(claim_tokens)


def _is_cautionary_evidence(text: str) -> bool:
    """Return true when an evidence sentence limits or qualifies a claim."""
    lowered = text.lower()
    caution_terms = [
        "cannot",
        "not currently",
        "not enough",
        "insufficient",
        "limited",
        "thin",
        "weaker",
        "caution",
        "concern",
        "does not mean",
        "does not support",
        "do not",
        "rather than",
        "not a ",
        "not as ",
        "risk",
    ]
    return any(term in lowered for term in caution_terms)


def _is_contradictory_evidence(text: str) -> bool:
    """Return true when a matching sentence directly pushes against the claim."""
    lowered = text.lower()
    contradiction_terms = [
        "cannot currently be recommended",
        "cannot be recommended",
        "does not support",
        "not strong enough",
        "insufficient evidence",
        "not supported",
        "no evidence",
    ]
    return any(term in lowered for term in contradiction_terms)


def _append_unique(items: list[str], value: str) -> None:
    """Append a non-empty string once, preserving order."""
    value = value.strip()
    if value and value not in items:
        items.append(value)


def load_source_cards(disease: str) -> list[SourceEvidence]:
    """Load all source cards for a disease."""
    sources = []
    papers_dir = VAULT_ROOT / "raw" / "papers"
    regulations_dir = VAULT_ROOT / "raw" / "regulations"

    candidate_paths: list[Path] = []
    if papers_dir.exists():
        candidate_paths.extend(sorted(papers_dir.glob(f"src-{disease.lower()}-*.md")))
    if regulations_dir.exists():
        candidate_paths.extend(sorted(regulations_dir.glob("src-reg-*.md")))

    for path in candidate_paths:
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        fm = _parse_frontmatter(content)
        if not fm.get("id"):
            continue
        if path.parent == regulations_dir:
            diseases = fm.get("diseases", [])
            if isinstance(diseases, str):
                diseases = [diseases]
            disease_matches = any(disease.lower() in str(item).lower() for item in diseases)
            if not disease_matches:
                continue

        policy = _extract_evidence_policy(content)
        limits = _extract_limits(content)

        evidence_level = fm.get("evidence_level", "unknown")
        verification_status = fm.get("verification_status", "unknown")

        sources.append(SourceEvidence(
            source_id=fm["id"],
            title=fm.get("title", ""),
            evidence_level=evidence_level,
            verification_status=verification_status,
            weight_score=_compute_weight(evidence_level, verification_status),
            quoted_facts=policy.get("quoted_fact", []),
            source_supported_conclusions=policy.get("source_supported_conclusion", []),
            llm_inferences=policy.get("llm_inference", []),
            limits=limits,
        ))

    return sources


def _load_claims_from_markdown(path: Path) -> list[dict]:
    """Load Key-Claim Traceability rows from one markdown file."""
    claims = []
    if not path.exists():
        return claims

    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return claims

    # Parse Key-Claim Traceability table
    in_table = False
    headers = []

    for line in content.splitlines():
        if "Key-Claim Traceability" in line:
            in_table = True
            continue

        if in_table:
            if line.startswith("|") and "---" not in line:
                cells = [c.strip() for c in line.split("|")[1:-1]]
                if not headers:
                    headers = cells
                elif len(cells) >= 4:
                    claims.append({
                        "claim_id": cells[0] if len(cells) > 0 else "",
                        "claim": cells[1] if len(cells) > 1 else "",
                        "level": cells[2] if len(cells) > 2 else "",
                        "sources": cells[3] if len(cells) > 3 else "",
                        "source_path": str(path.relative_to(VAULT_ROOT)),
                    })
            elif line.startswith("## ") and "Key-Claim" not in line:
                break

    return claims


def load_topic_claims(disease: str) -> list[dict]:
    """Load Key-Claim Traceability from topic and disease-specific system memos."""
    disease = disease.lower()
    paths = [VAULT_ROOT / "topics" / disease / "synthesis-index.md"]
    paths.extend(sorted((VAULT_ROOT / "system" / "indexes").glob(f"{disease}-*.md")))

    claims = []
    seen = set()
    for path in paths:
        for claim in _load_claims_from_markdown(path):
            key = (claim["claim_id"], claim["claim"], claim["sources"])
            if key not in seen:
                seen.add(key)
                claims.append(claim)

    return claims


def evaluate_claim(disease: str, claim: str, source_ids: Optional[list[str]] = None) -> ClaimEvidenceCard:
    """
    Evaluate a claim against the vault's evidence.

    Args:
        disease: Disease code (ckd, fip, hcm, ibd, diabetes, fcv, obesity, cancer)
        claim: The claim text to verify
        source_ids: Optional list of source IDs to check (if None, searches all)

    Returns:
        ClaimEvidenceCard with verdict and supporting evidence
    """
    claim_tokens = _tokenize_claim(claim)
    sources = load_source_cards(disease)
    topic_claims = load_topic_claims(disease)

    # Filter by source_ids if provided
    if source_ids:
        sources = [s for s in sources if s.source_id in source_ids]

    # Score each source against the claim
    scored_sources: list[tuple[SourceEvidence, float, str, list[str]]] = []

    for source in sources:
        best_score = 0.0
        best_level = "C"
        matching_facts: list[str] = []

        # Check quoted facts (Level A)
        for fact in source.quoted_facts:
            score = _calculate_match_score(claim_tokens, fact)
            if score > 0.3:  # Threshold for relevance
                matching_facts.append(f"[A] {fact}")
                if score > best_score:
                    best_score = score
                    best_level = "A"

        # Check source-supported conclusions (Level B)
        for conclusion in source.source_supported_conclusions:
            score = _calculate_match_score(claim_tokens, conclusion)
            if score > 0.3:
                matching_facts.append(f"[B] {conclusion}")
                if score > best_score:
                    best_score = score
                    if best_level != "A":
                        best_level = "B"

        # Check LLM inferences (Level C)
        for inference in source.llm_inferences:
            score = _calculate_match_score(claim_tokens, inference)
            if score > 0.3:
                matching_facts.append(f"[C] {inference}")
                if score > best_score:
                    best_score = score
                    if best_level not in ["A", "B"]:
                        best_level = "C"

        if best_score > 0.2:
            scored_sources.append((source, best_score, best_level, matching_facts))

    # Sort by score * weight
    scored_sources.sort(key=lambda x: x[1] * x[0].weight_score, reverse=True)

    # Also check existing topic claims for matches
    matching_topic_claims = []
    for tc in topic_claims:
        score = _calculate_match_score(claim_tokens, tc["claim"])
        if score > 0.4:
            matching_topic_claims.append({**tc, "score": score})

    matching_topic_claims.sort(key=lambda tc: tc["score"], reverse=True)

    boundary_notes = []

    # Determine whether lexical candidate matches exist. This is deliberately
    # not a support/contradiction judgment.
    if not scored_sources and not matching_topic_claims:
        verdict = "no_candidate_matches"
        verdict_confidence = "not_assessed"
        claim_level = "candidate_only"
        next_action = "search_more"
    else:
        top_sources = scored_sources[:5]

        # Check if any source-card or compiled-claim evidence.
        has_a_level = any(level == "A" for _, _, level, _ in top_sources)
        has_b_level = any(level == "B" for _, _, level, _ in top_sources)
        has_compiled_b_level = any(str(tc.get("level", "")).strip().upper() == "B" for tc in matching_topic_claims)
        has_compiled_a_level = any(str(tc.get("level", "")).strip().upper() == "A" for tc in matching_topic_claims)
        best_compiled_score = matching_topic_claims[0]["score"] if matching_topic_claims else 0.0

        # Calculate aggregate score
        if top_sources:
            avg_score = sum(s[1] for s in top_sources) / len(top_sources)
            max_score = max(s[1] for s in top_sources)
        else:
            avg_score = 0.0
            max_score = 0.0

        # Check for contradictions and business-use boundaries.
        has_contradiction = False
        for source, score, level, facts in top_sources:
            for fact in facts:
                if _is_cautionary_evidence(fact):
                    if _is_contradictory_evidence(fact):
                        has_contradiction = True
                    _append_unique(boundary_notes, f"[{source.source_id}] {fact[4:] if fact[:3] in {'[A]', '[B]', '[C]'} else fact}")
            for limit in source.limits:
                limit_score = _calculate_match_score(claim_tokens, limit)
                if limit_score > 0.2 or _is_cautionary_evidence(limit):
                    if limit_score > 0.5 and _is_contradictory_evidence(limit):
                        has_contradiction = True
                    _append_unique(boundary_notes, f"[{source.source_id}] {limit}")

        _ = (
            has_a_level,
            has_b_level,
            has_compiled_a_level,
            has_compiled_b_level,
            best_compiled_score,
            avg_score,
            max_score,
            has_contradiction,
        )
        verdict = "candidate_matches_found"
        verdict_confidence = "not_assessed"
        claim_level = "candidate_only"
        next_action = "human_review"

    # Build output
    key_sources = [s[0].source_id for s in scored_sources[:5]]
    for tc in matching_topic_claims[:3]:
        for src in re.findall(r'\bsrc-[a-z]+-\d{3}\b', tc.get("sources", ""), re.IGNORECASE):
            if src not in key_sources:
                key_sources.append(src)

    quoted_facts = []
    source_supported_conclusions = []
    for source, score, level, facts in scored_sources[:5]:
        for fact in facts:
            if fact.startswith("[A]"):
                quoted_facts.append({"source_id": source.source_id, "fact": fact[4:]})
            elif fact.startswith("[B]"):
                source_supported_conclusions.append({"source_id": source.source_id, "conclusion": fact[4:]})

    for tc in matching_topic_claims[:3]:
        if str(tc.get("level", "")).strip().upper() in {"A", "B"}:
            source_supported_conclusions.append({
                "source_id": tc.get("source_path", "compiled-claim"),
                "conclusion": f"{tc.get('claim_id', 'compiled-claim')}: {tc.get('claim', '')} (sources: {tc.get('sources', '')})",
            })

    # Evidence depth summary
    evidence_depth = {
        "total_sources_checked": len(sources),
        "matching_sources": len(scored_sources),
        "matching_compiled_claims": len(matching_topic_claims),
        "a_level_matches": sum(1 for _, _, l, _ in scored_sources if l == "A"),
        "b_level_matches": sum(1 for _, _, l, _ in scored_sources if l == "B"),
        "c_level_matches": sum(1 for _, _, l, _ in scored_sources if l == "C"),
        "deep_extracted": sum(1 for s in sources if s.verification_status == "deep_extracted"),
    }

    # Boundary: what the claim does NOT cover.
    boundary = []
    if boundary_notes:
        boundary.extend(boundary_notes[:3])
    if not boundary:
        for source, _, _, facts in scored_sources[:5]:
            for limit in source.limits:
                _append_unique(boundary, f"[{source.source_id}] {limit}")
                if len(boundary) >= 3:
                    break
            if len(boundary) >= 3:
                break
    if not boundary:
        boundary.append(
            "No source-specific caveat was extracted for the matching sources; treat this card as non-decision-grade until a human source-limit pass is completed."
        )

    # Missing evidence
    missing_evidence = []
    if evidence_depth["a_level_matches"] == 0:
        missing_evidence.append("No direct quotes (Level A) support this claim")
    if evidence_depth["matching_sources"] < 3:
        missing_evidence.append(f"Only {evidence_depth['matching_sources']} sources address this claim")
    if verdict == "no_candidate_matches":
        missing_evidence.append(f"No sources found matching claim in {disease.upper()} corpus")

    # Verification path
    if key_sources:
        verification_path = f"topics/{disease.lower()}/synthesis-index.md -> " + ", ".join(key_sources[:3])
    else:
        verification_path = f"No matching sources in raw/papers/src-{disease.lower()}-*.md"

    return ClaimEvidenceCard(
        claim=claim,
        disease=disease.upper(),
        verdict=verdict,
        verdict_confidence=verdict_confidence,
        claim_level=claim_level,
        key_sources=key_sources,
        evidence_depth=evidence_depth,
        quoted_facts=quoted_facts[:5],
        source_supported_conclusions=source_supported_conclusions[:5],
        boundary=boundary,
        missing_evidence=missing_evidence,
        next_action=next_action,
        verification_path=verification_path,
    )


def format_claim_card_markdown(card: ClaimEvidenceCard) -> str:
    """Format a ClaimEvidenceCard as markdown."""
    lines = [
        "# Candidate Evidence Matches",
        "",
        f"**Disease:** {card.disease}",
        f"**Claim:** {card.claim}",
        "",
        "> Candidate retrieval only. Lexical overlap does not establish support, contradiction, or decision readiness. A human reviewer must inspect the sources.",
        "",
        "## Retrieval Status",
        "",
        f"| Field | Value |",
        f"|-------|-------|",
        f"| Candidate status | **{card.verdict.upper()}** |",
        f"| Semantic confidence | {card.verdict_confidence} |",
        f"| Authority | {card.claim_level} |",
        f"| Next Action | {card.next_action} |",
        "",
        "## Key Sources",
        "",
    ]

    if card.key_sources:
        for src in card.key_sources:
            lines.append(f"- {src}")
    else:
        lines.append("- No matching sources found")

    lines.extend([
        "",
        "## Evidence Depth",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Sources checked | {card.evidence_depth['total_sources_checked']} |",
        f"| Matching sources | {card.evidence_depth['matching_sources']} |",
        f"| Matching compiled claims | {card.evidence_depth.get('matching_compiled_claims', 0)} |",
        f"| Level A (quoted) | {card.evidence_depth['a_level_matches']} |",
        f"| Level B (supported) | {card.evidence_depth['b_level_matches']} |",
        f"| Level C (inference) | {card.evidence_depth['c_level_matches']} |",
        f"| Deep extracted | {card.evidence_depth['deep_extracted']} |",
        "",
    ])

    if card.quoted_facts:
        lines.extend([
            "## Quoted Facts (Level A)",
            "",
        ])
        for qf in card.quoted_facts:
            lines.append(f"- [{qf['source_id']}] \"{qf['fact']}\"")
        lines.append("")

    if card.source_supported_conclusions:
        lines.extend([
            "## Source-Supported Conclusions (Level B)",
            "",
        ])
        for sc in card.source_supported_conclusions:
            lines.append(f"- [{sc['source_id']}] {sc['conclusion']}")
        lines.append("")

    lines.extend([
        "## Boundary",
        "",
    ])
    for b in card.boundary:
        lines.append(f"- {b}")

    if card.missing_evidence:
        lines.extend([
            "",
            "## Missing Evidence",
            "",
        ])
        for me in card.missing_evidence:
            lines.append(f"- {me}")

    lines.extend([
        "",
        "## Verification Path",
        "",
        f"`{card.verification_path}`",
    ])

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Retrieve candidate evidence for human claim review.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--disease", "-d",
        required=True,
        choices=["ckd", "fip", "hcm", "ibd", "diabetes", "fcv", "obesity", "cancer"],
        help="Disease code to search",
    )
    parser.add_argument(
        "--claim", "-c",
        required=True,
        help="The claim used to retrieve candidate evidence",
    )
    parser.add_argument(
        "--sources", "-s",
        help="Comma-separated source IDs to check (optional)",
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output as JSON instead of markdown",
    )
    args = parser.parse_args()

    source_ids = None
    if args.sources:
        source_ids = [s.strip() for s in args.sources.split(",")]

    card = evaluate_claim(args.disease, args.claim, source_ids)

    if args.json:
        print(json.dumps(asdict(card), indent=2))
    else:
        print(format_claim_card_markdown(card))


if __name__ == "__main__":
    main()
