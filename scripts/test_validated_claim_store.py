"""Tests for validated claim storage and stale detection."""

from __future__ import annotations

import sys
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).parent.parent))

from core import ResearchRecord, TaskType, build_promotion_draft, extract_claim_candidates, ValidatedClaimStore  # noqa: E402


def _write_source(root: Path, source_id: str, body: str) -> Path:
    path = root / "raw" / "papers" / f"{source_id}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\n"
        f"id: {source_id}\n"
        "title: Test Source\n"
        "source_kind: paper\n"
        "verification_status: deep_extracted\n"
        "doi: 10.1000/example\n"
        "---\n"
        f"{body}\n",
        encoding="utf-8",
    )
    return path


def _make_record() -> ResearchRecord:
    record = ResearchRecord.create("猫CKD终点指标有哪些", TaskType.ENDPOINT_SELECTION, disease="ckd")
    record.selected_evidence = ["src-ckd-001", "src-ckd-002"]
    record.final_answer = (
        "CKD is fibrosis-driven. [quoted_fact: src-ckd-001]\n"
        "Endpoint strategy should distinguish workup from intervention. [source_supported_conclusion: src-ckd-001, src-ckd-002]"
    )
    return record


def test_promote_and_query_current_claims() -> None:
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        _write_source(root, "src-ckd-001", "Body 1")
        _write_source(root, "src-ckd-002", "Body 2")
        store = ValidatedClaimStore(root / "system" / "validated-claims")
        record = _make_record()
        claims = extract_claim_candidates(record)
        draft = build_promotion_draft(
            record,
            [claims[0].claim_id, claims[1].claim_id],
            "topics/ckd/validated-claims.md",
        )
        assert draft.ready_for_patch is True
        result = store.promote_draft(draft, root)
        assert len(result["claims"]) == 2
        assert result["target_path"] is not None
        assert result["target_path"].exists()
        page_text = result["target_path"].read_text(encoding="utf-8")
        assert "Validated Claims for ckd" in page_text
        assert "Promotion Judgment" in page_text
        assert "Key-Claim Traceability" in page_text
        assert claims[0].claim_id in page_text
        current = store.query_validated_claims(root)
        assert len(current) == 2
        assert all(claim.status == "current" for claim in current)
        assert (root / "system" / "validated-claims" / "manifests").exists()


def test_source_change_marks_claim_stale() -> None:
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = _write_source(root, "src-ckd-001", "Body 1")
        _write_source(root, "src-ckd-002", "Body 2")
        store = ValidatedClaimStore(root / "system" / "validated-claims")
        record = _make_record()
        claims = extract_claim_candidates(record)
        draft = build_promotion_draft(
            record,
            [claims[0].claim_id, claims[1].claim_id],
            "topics/ckd/validated-claims.md",
        )
        store.promote_draft(draft, root)

        source.write_text(
            "---\n"
            "id: src-ckd-001\n"
            "title: Test Source\n"
            "source_kind: paper\n"
            "verification_status: deep_extracted\n"
            "doi: 10.1000/example\n"
            "---\n"
            "Body changed\n",
            encoding="utf-8",
        )

        current = store.query_validated_claims(root)
        assert current == []
        target_path = root / "topics" / "ckd" / "validated-claims.md"
        assert target_path.exists()
        page_text = target_path.read_text(encoding="utf-8")
        assert "No current validated claims" in page_text
        assert "Key-Claim Traceability" in page_text
        stale_queue = store.stale_queue_path.read_text(encoding="utf-8")
        assert claims[0].claim_id in stale_queue
        assert claims[1].claim_id in stale_queue


def test_missing_source_blocks_promotion() -> None:
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        _write_source(root, "src-ckd-001", "Body 1")
        store = ValidatedClaimStore(root / "system" / "validated-claims")
        record = _make_record()
        claims = extract_claim_candidates(record)
        draft = build_promotion_draft(
            record,
            [claims[0].claim_id, claims[1].claim_id],
            "topics/ckd/validated-claims.md",
        )
        try:
            store.promote_draft(draft, root)
            raised = False
        except ValueError as exc:
            raised = True
            assert "source fingerprints" in str(exc)
        assert raised, "Missing sources should block promotion"


def run_all_tests() -> None:
    test_promote_and_query_current_claims()
    test_source_change_marks_claim_stale()
    test_missing_source_blocks_promotion()
    print("All validated claim store tests passed!")


if __name__ == "__main__":
    run_all_tests()
