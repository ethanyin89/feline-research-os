"""
Integration and end-to-end tests for Gate 6B: Claim Selection & Validation,
and Gate 6C: Autoplan Actions & Promoted Claim Store.
"""

import sys
import json
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory
from datetime import datetime

# Add parent directory for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core import (
    ResearchRecord,
    TaskType,
    ValidatedClaimStore,
    ValidatedClaim,
    PromotionManifest,
    build_promotion_draft,
    extract_claim_candidates,
)


def _write_mock_source(root: Path, source_id: str, content: str) -> Path:
    path = root / "raw" / "papers" / f"{source_id}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\n"
        f"id: {source_id}\n"
        "title: Mock Study\n"
        "source_kind: paper\n"
        "verification_status: deep_extracted\n"
        "---\n"
        f"{content}\n",
        encoding="utf-8",
    )
    return path


def test_gate6b_6c_e2e_pipeline():
    with TemporaryDirectory() as tmp_dir:
        vault_root = Path(tmp_dir)
        
        # 1. Create mock sources in vault
        _write_mock_source(vault_root, "src-ckd-001", "Feline kidney tubulointerstitial fibrosis study.")
        _write_mock_source(vault_root, "src-ckd-002", "Proteinuria as key indicator study.")
        
        # 2. Create a mock record with v2 claims (some valid, some llm_inference)
        record = ResearchRecord.create(
            user_request="explain ckd disease model",
            task_type=TaskType.MODEL_EVALUATION,
            disease="ckd"
        )
        record.selected_evidence = ["src-ckd-001", "src-ckd-002"]
        record.final_answer = (
            "Feline CKD is characterized by tubulointerstitial fibrosis. [quoted_fact: src-ckd-001]\n"
            "Proteinuria is a key prognostic marker. [source_supported_conclusion: src-ckd-002]\n"
            "Senescence plays an unproven role. [llm_inference]"
        )
        
        # 3. Extract candidates
        candidates = extract_claim_candidates(record)
        assert len(candidates) == 3
        
        # Validate candidate properties
        assert candidates[0].provenance == "quoted_fact"
        assert candidates[0].source_ids == ["src-ckd-001"]
        assert candidates[1].provenance == "source_supported_conclusion"
        assert candidates[1].source_ids == ["src-ckd-002"]
        assert candidates[2].provenance == "llm_inference"
        assert len(candidates[2].source_ids) == 0
        
        # 4. Build draft with invalid target
        draft_bad_target = build_promotion_draft(
            record=record,
            selected_claim_ids=[candidates[0].claim_id],
            target_page="../escape.md"
        )
        assert draft_bad_target.status == "blocked"
        assert draft_bad_target.ready_for_patch is False
        assert any("Target page must stay inside" in r.message for r in draft_bad_target.validation_results)
        
        # 5. Build draft selecting llm_inference (should be blocked)
        draft_inference = build_promotion_draft(
            record=record,
            selected_claim_ids=[candidates[0].claim_id, candidates[2].claim_id],
            target_page="topics/ckd/validated-claims.md"
        )
        assert draft_inference.status == "blocked"
        assert draft_inference.ready_for_patch is False
        assert any("Inference-only claims cannot be promoted" in r.message for r in draft_inference.validation_results)
        
        # 6. Build a valid draft
        target_page = "topics/ckd/validated-claims.md"
        draft_valid = build_promotion_draft(
            record=record,
            selected_claim_ids=[candidates[0].claim_id, candidates[1].claim_id],
            target_page=target_page
        )
        assert draft_valid.status == "validated"
        assert draft_valid.ready_for_patch is True
        
        # 7. Promote draft
        store = ValidatedClaimStore(vault_root / "system" / "validated-claims")
        res = store.promote_draft(draft_valid, vault_root)
        
        assert len(res["claims"]) == 2
        assert isinstance(res["manifest"], PromotionManifest)
        assert res["target_path"].exists()
        
        # Check written files
        manifest_id = res["manifest"].manifest_id
        assert (store.manifest_path / f"{manifest_id}.json").exists()
        assert (store.manifest_path / f"{manifest_id}.md").exists()
        
        for claim in res["claims"]:
            assert (store.json_path / f"{claim.claim_id}.json").exists()
            assert (store.markdown_path / f"{claim.claim_id}.md").exists()
            
        # Check target page markdown structure
        target_content = res["target_path"].read_text(encoding="utf-8")
        assert "---" in target_content
        assert f"promotion_manifest_id: {manifest_id}" in target_content
        assert "## Key-Claim Traceability" in target_content
        assert candidates[0].claim_id in target_content
        assert candidates[1].claim_id in target_content
        
        # 8. Test Rollback on Failure (e.g. missing source fingerprint)
        # Delete a source card
        (vault_root / "raw" / "papers" / "src-ckd-002.md").unlink()
        
        # Create a new draft
        record_new = ResearchRecord.create("new search", TaskType.ENDPOINT_SELECTION, "ckd")
        record_new.selected_evidence = ["src-ckd-001", "src-ckd-002"]
        record_new.final_answer = "Fibre works. [quoted_fact: src-ckd-001, src-ckd-002]"
        candidates_new = extract_claim_candidates(record_new)
        
        draft_new = build_promotion_draft(record_new, [candidates_new[0].claim_id], "topics/ckd/validated-claims.md")
        assert draft_new.ready_for_patch is True
        
        # Trying to promote should raise ValueError due to missing source src-ckd-002
        try:
            store.promote_draft(draft_new, vault_root)
            promoted = True
        except ValueError as e:
            promoted = False
            assert "source fingerprints could not be resolved" in str(e)
            
        assert promoted is False, "Promotion should have been blocked and rolled back"
        
        # Ensure no manifest or claim JSON files for record_new were written (rollback check)
        new_manifest_id = store._manifest_id(record_new.record_id, "topics/ckd/validated-claims.md")
        assert not (store.manifest_path / f"{new_manifest_id}.json").exists()
        assert not (store.manifest_path / f"{new_manifest_id}.md").exists()
        assert not (store.json_path / f"{candidates_new[0].claim_id}.json").exists()


def test_stale_detection_and_rebuild():
    with TemporaryDirectory() as tmp_dir:
        vault_root = Path(tmp_dir)
        
        src_path = _write_mock_source(vault_root, "src-ckd-001", "Feline kidney tubulointerstitial fibrosis study.")
        
        record = ResearchRecord.create("fibrosis query", TaskType.MODEL_EVALUATION, "ckd")
        record.selected_evidence = ["src-ckd-001"]
        record.final_answer = "Fibrosis is key. [quoted_fact: src-ckd-001]"
        
        candidates = extract_claim_candidates(record)
        draft = build_promotion_draft(record, [candidates[0].claim_id], "topics/ckd/validated-claims.md")
        
        store = ValidatedClaimStore(vault_root / "system" / "validated-claims")
        store.promote_draft(draft, vault_root)
        
        # Confirm claim is current
        current = store.query_validated_claims(vault_root)
        assert len(current) == 1
        assert current[0].status == "current"
        
        # Modify source content to trigger stale fingerprint
        src_path.write_text(
            "---\n"
            "id: src-ckd-001\n"
            "title: Mock Study\n"
            "source_kind: paper\n"
            "verification_status: deep_extracted\n"
            "---\n"
            "Totally different content which changes the SHA256 fingerprint.\n",
            encoding="utf-8"
        )
        
        # Re-querying validated claims should trigger stale status update
        current_after_mod = store.query_validated_claims(vault_root)
        assert len(current_after_mod) == 0
        
        # Verify it went to the stale queue
        assert store.stale_queue_path.exists()
        stale_data = json.loads(store.stale_queue_path.read_text(encoding="utf-8"))
        assert len(stale_data["items"]) == 1
        assert stale_data["items"][0]["claim_id"] == candidates[0].claim_id
        assert stale_data["items"][0]["stale_reason"] == "Source fingerprint changed"
        
        # Verify the target page was updated and now excludes the stale claim
        target_path = vault_root / "topics" / "ckd" / "validated-claims.md"
        assert target_path.exists()
        target_text = target_path.read_text(encoding="utf-8")
        assert "No current validated claims for this target yet" in target_text


if __name__ == "__main__":
    test_gate6b_6c_e2e_pipeline()
    test_stale_detection_and_rebuild()
    print("✓ All Gate 6B and 6C E2E/Integration tests passed successfully!")
