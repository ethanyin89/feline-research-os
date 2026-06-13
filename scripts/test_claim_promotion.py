"""Tests for claim selection and promotion drafts."""

from __future__ import annotations

import sys
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).parent.parent))

from core import ResearchRecord, TaskType  # noqa: E402
from core.claim_promotion import (  # noqa: E402
    build_promotion_draft,
    extract_claim_candidates,
)


def make_record() -> ResearchRecord:
    record = ResearchRecord.create("猫CKD终点指标有哪些", TaskType.ENDPOINT_SELECTION, disease="ckd")
    record.selected_evidence = ["src-ckd-001", "src-ckd-002", "src-ckd-004"]
    record.final_answer = (
        "Feline CKD is a chronic fibrosis-driven disease. [quoted_fact: src-ckd-001]\n"
        "Proteinuria and blood pressure are operational endpoints. [source_supported_conclusion: src-ckd-002, src-ckd-004]\n"
        "No single marker can decide every case. [llm_inference]"
    )
    return record


def test_extract_claim_candidates() -> None:
    record = make_record()
    claims = extract_claim_candidates(record)
    assert len(claims) == 3
    assert claims[0].provenance == "quoted_fact"
    assert claims[0].source_ids == ["src-ckd-001"]
    assert claims[1].provenance == "source_supported_conclusion"
    assert claims[1].source_ids == ["src-ckd-002", "src-ckd-004"]
    assert claims[2].provenance == "llm_inference"


def test_build_promotion_draft_validates_supported_claims() -> None:
    record = make_record()
    claims = extract_claim_candidates(record)
    draft = build_promotion_draft(
        record,
        selected_claim_ids=[claims[0].claim_id, claims[1].claim_id],
        target_page="topics/ckd/validated-claims.md",
    )
    assert draft.status == "validated"
    assert draft.ready_for_patch is True
    assert len(draft.selected_claims) == 2
    assert all(result.passed for result in draft.validation_results)


def test_build_promotion_draft_blocks_inference_and_bad_target() -> None:
    record = make_record()
    claims = extract_claim_candidates(record)
    draft = build_promotion_draft(
        record,
        selected_claim_ids=[claims[2].claim_id],
        target_page="../escape.md",
    )
    assert draft.status == "blocked"
    assert draft.ready_for_patch is False
    assert any(not result.passed for result in draft.validation_results)
    assert any("Target page" in result.message for result in draft.validation_results)
    assert any("Inference-only" in result.message for result in draft.validation_results)


def run_all_tests() -> None:
    test_extract_claim_candidates()
    test_build_promotion_draft_validates_supported_claims()
    test_build_promotion_draft_blocks_inference_and_bad_target()
    print("All claim promotion tests passed!")


if __name__ == "__main__":
    run_all_tests()
