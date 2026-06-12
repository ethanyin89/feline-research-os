"""Claim selection and promotion draft helpers.

This module stays pure in 6B:
- extract candidate claims from a saved research answer
- validate a human-selected promotion draft
- never write to the knowledge base
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, List, Optional

from .schemas import ResearchRecord


CLAIM_TAG_RE = re.compile(
    r"\[(quoted_fact|source_supported_conclusion|llm_inference)(?::\s*([^\]]+))?\]"
)
SAFE_TARGET_PREFIXES = (
    "topics/",
    "system/indexes/",
    "system/synthesis/",
    "entities/",
)


@dataclass
class ResearchClaim:
    claim_id: str
    text: str
    original_answer_span: str
    ordinal: int
    source_ids: list[str] = field(default_factory=list)
    provenance: str = "llm_inference"
    supported_use: str = ""
    boundary: str = ""
    selected_by_human: bool = False


@dataclass
class ClaimValidationResult:
    check_name: str
    passed: bool
    message: str
    severity: str = "medium"


@dataclass
class PromotionDraft:
    record_id: str
    target_page: str
    selected_claims: list[ResearchClaim] = field(default_factory=list)
    validation_results: list[ClaimValidationResult] = field(default_factory=list)
    status: str = "candidate"
    notes: list[str] = field(default_factory=list)

    @property
    def ready_for_patch(self) -> bool:
        return self.status == "validated"


def _split_source_ids(raw: str) -> list[str]:
    ids = []
    for item in re.split(r"[;,]", raw):
        cleaned = item.strip()
        if cleaned:
            ids.append(cleaned)
    return list(dict.fromkeys(ids))


def _strip_tags(text: str) -> str:
    cleaned = CLAIM_TAG_RE.sub("", text)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def extract_claim_candidates(record: ResearchRecord) -> list[ResearchClaim]:
    """Extract claim candidates from the saved answer text."""
    if not record.final_answer.strip():
        return []

    candidates: list[ResearchClaim] = []
    ordinal = 1
    for raw_line in record.final_answer.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        tags = list(CLAIM_TAG_RE.finditer(line))
        if not tags:
            continue

        source_ids: list[str] = []
        provenance = "llm_inference"
        for match in tags:
            tag_type = match.group(1)
            if tag_type != "llm_inference":
                source_ids.extend(_split_source_ids(match.group(2) or ""))
                provenance = tag_type
            elif provenance == "llm_inference":
                provenance = "llm_inference"

        text = _strip_tags(line)
        if not text:
            continue

        source_ids = list(dict.fromkeys(source_ids))
        supported_use = (
            "quoted_fact" if provenance == "quoted_fact"
            else "source_supported_conclusion" if provenance == "source_supported_conclusion"
            else "analysis_only"
        )
        boundary = (
            "Promotable only as source-traced text."
            if provenance != "llm_inference"
            else "Inference-only content cannot be promoted."
        )
        candidates.append(
            ResearchClaim(
                claim_id=f"{record.record_id}-claim-{ordinal:02d}",
                text=text,
                original_answer_span=line,
                ordinal=ordinal,
                source_ids=source_ids,
                provenance=provenance,
                supported_use=supported_use,
                boundary=boundary,
            )
        )
        ordinal += 1

    return candidates


def _validate_target_page(target_page: str) -> ClaimValidationResult:
    normalized = target_page.strip().replace("\\", "/")
    if not normalized:
        return ClaimValidationResult(
            check_name="target_page",
            passed=False,
            message="Target page is required.",
            severity="high",
        )
    if normalized.startswith("/") or ".." in Path(normalized).parts:
        return ClaimValidationResult(
            check_name="target_page",
            passed=False,
            message="Target page must stay inside the vault.",
            severity="critical",
        )
    if not normalized.startswith(SAFE_TARGET_PREFIXES):
        return ClaimValidationResult(
            check_name="target_page",
            passed=False,
            message="Target page is outside the allowed promotion areas.",
            severity="high",
        )
    return ClaimValidationResult(
        check_name="target_page",
        passed=True,
        message="Target page is within the allowed promotion areas.",
        severity="low",
    )


def _validate_claim_against_record(
    claim: ResearchClaim,
    record: ResearchRecord,
) -> list[ClaimValidationResult]:
    results = []
    if not claim.text.strip():
        results.append(ClaimValidationResult(
            check_name=f"{claim.claim_id}:text",
            passed=False,
            message="Claim text is empty.",
            severity="critical",
        ))
    else:
        results.append(ClaimValidationResult(
            check_name=f"{claim.claim_id}:text",
            passed=True,
            message="Claim text is present.",
            severity="low",
        ))

    if claim.provenance == "llm_inference":
        results.append(ClaimValidationResult(
            check_name=f"{claim.claim_id}:provenance",
            passed=False,
            message="Inference-only claims cannot be promoted.",
            severity="critical",
        ))
    else:
        results.append(ClaimValidationResult(
            check_name=f"{claim.claim_id}:provenance",
            passed=True,
            message="Claim is source-traced.",
            severity="low",
        ))

    if not claim.source_ids:
        results.append(ClaimValidationResult(
            check_name=f"{claim.claim_id}:sources",
            passed=False,
            message="Claim has no source IDs.",
            severity="high",
        ))
    else:
        results.append(ClaimValidationResult(
            check_name=f"{claim.claim_id}:sources",
            passed=True,
            message="Claim includes source IDs.",
            severity="low",
        ))

    loaded_sources = set(record.selected_evidence or [])
    if claim.source_ids and loaded_sources and set(claim.source_ids).issubset(loaded_sources):
        results.append(ClaimValidationResult(
            check_name=f"{claim.claim_id}:loaded_sources",
            passed=True,
            message="Claim source IDs are present in the saved record.",
            severity="low",
        ))
    else:
        results.append(ClaimValidationResult(
            check_name=f"{claim.claim_id}:loaded_sources",
            passed=False,
            message="Claim source IDs are not fully covered by the saved record.",
            severity="high",
        ))

    return results


def build_promotion_draft(
    record: ResearchRecord,
    selected_claim_ids: Iterable[str],
    target_page: str,
) -> PromotionDraft:
    """Build a non-persistent promotion draft from a saved record."""
    claim_map = {claim.claim_id: claim for claim in extract_claim_candidates(record)}
    selected_ids = list(dict.fromkeys(selected_claim_ids))
    selected_claims: list[ResearchClaim] = []
    validation_results: list[ClaimValidationResult] = []
    notes: list[str] = []

    target_result = _validate_target_page(target_page)
    validation_results.append(target_result)

    if not selected_ids:
        validation_results.append(ClaimValidationResult(
            check_name="selected_claims",
            passed=False,
            message="Select at least one claim.",
            severity="high",
        ))
        return PromotionDraft(
            record_id=record.record_id,
            target_page=target_page,
            selected_claims=[],
            validation_results=validation_results,
            status="candidate",
            notes=notes,
        )

    for claim_id in selected_ids:
        claim = claim_map.get(claim_id)
        if claim is None:
            validation_results.append(ClaimValidationResult(
                check_name=f"{claim_id}:selection",
                passed=False,
                message="Claim is not available in this record.",
                severity="high",
            ))
            continue

        claim.selected_by_human = True
        selected_claims.append(claim)
        validation_results.extend(_validate_claim_against_record(claim, record))

    if selected_claims:
        if any(not result.passed for result in validation_results):
            status = "blocked"
            notes.append("Resolve the failed checks before promotion.")
        else:
            status = "validated"
            notes.append("Validation draft is ready for human review.")
    else:
        status = "blocked"
        notes.append("No selectable claims were found.")

    return PromotionDraft(
        record_id=record.record_id,
        target_page=target_page,
        selected_claims=selected_claims,
        validation_results=validation_results,
        status=status,
        notes=notes,
    )
