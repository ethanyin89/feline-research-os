"""
Integration tests for Gate 6A features:
- RetrievalEvent and SourceSnapshot creation during query flow
- Explicit save of transient records
- Commit manifest creation and integrity verification
- Duplicate checking and version increment logic
"""

import sys
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from datetime import datetime
from unittest.mock import patch, MagicMock

# Add parent directory for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core import (
    ResearchRecord, RecordStore, TaskType, SearchDepth,
    VerificationResult, VerifierStatus
)
from core.schemas import RetrievalEvent, SourceSnapshot
from scripts.query import run_query_core
from scripts.harness_loop import HarnessLoop


def test_gate6a_query_to_save_integration():
    with TemporaryDirectory() as tmp_dir:
        vault_root = Path(tmp_dir)
        
        # Set up a minimal vault structure
        records_dir = vault_root / "system" / "research-records"
        papers_dir = vault_root / "raw" / "papers"
        topics_dir = vault_root / "topics" / "ckd"
        
        records_dir.mkdir(parents=True, exist_ok=True)
        papers_dir.mkdir(parents=True, exist_ok=True)
        topics_dir.mkdir(parents=True, exist_ok=True)
        
        # Create a mock source card
        src_id = "src-ckd-001"
        src_content = """---
id: src-ckd-001
title: "Mock CKD Study"
source_kind: paper
evidence_level: review
species: feline
verification_status: deep_extracted
extraction_depth: full
year: 2024
---
# Mock CKD Study Content
This is some test content for the fingerprint check.
"""
        (papers_dir / f"{src_id}.md").write_text(src_content, encoding="utf-8")
        
        # Create a mock topic page
        topic_content = """---
id: ckd-overview
title: "CKD Overview"
---
# CKD Overview Content
"""
        (topics_dir / "overview.md").write_text(topic_content, encoding="utf-8")
        
        # Create source index dict
        source_index = {
            src_id: papers_dir / f"{src_id}.md"
        }
        
        # Mock LLM API calls in scripts.query
        mock_client = MagicMock()
        
        mock_router_result = {
            "question_type": "overview",
            "disease": "ckd",
            "files_to_load": ["topics/ckd/overview.md"],
            "reasoning": "Loading CKD overview page."
        }
        
        mock_reformulate_result = {
            "refined_query": "feline ckd biomarkers",
            "objectives": ["Identify key CKD biomarkers"],
            "english_search_terms": ["ckd", "biomarkers"]
        }
        
        mock_synthesis_result = (
            "Based on [quoted_fact: src-ckd-001], CKD has markers.",
            []
        )
        
        mock_hop_result = {
            "action": "synthesize",
            "reasoning": "Sufficient context loaded."
        }
        
        with patch("scripts.query.reformulate_query_call", return_value=mock_reformulate_result), \
             patch("scripts.query.router_call", return_value=mock_router_result), \
             patch("scripts.query.hop_call", return_value=mock_hop_result), \
             patch("scripts.query.synthesis_call", return_value=mock_synthesis_result), \
             patch("scripts.query.vault_search", return_value=[{"file": f"raw/papers/{src_id}.md", "id": src_id, "matches": 5}]):
             
            # 1. Run the query core
            result = run_query_core(
                client=mock_client,
                question="What are feline CKD markers?",
                vault_root=vault_root,
                source_index=source_index,
                disease_hint="ckd",
                max_hops=1,
                allow_external_search=False
            )
            
            # Verify the result structure
            assert "retrieval_events" in result
            assert "source_snapshots" in result
            assert len(result["retrieval_events"]) > 0
            assert len(result["source_snapshots"]) > 0
            
            # Verify RetrievalEvent
            event = result["retrieval_events"][0]
            assert isinstance(event, RetrievalEvent)
            assert event.engine == "vault"
            assert src_id in event.retained_ids
            
            # Verify SourceSnapshot
            snapshot = result["source_snapshots"][0]
            assert isinstance(snapshot, SourceSnapshot)
            assert snapshot.source_id == src_id
            assert snapshot.title == "Mock CKD Study"
            assert snapshot.source_family == "paper"
            assert snapshot.study_type == "review"
            assert snapshot.extraction_depth == "full"
            assert snapshot.content_fingerprint == SourceSnapshot.compute_fingerprint(src_content)
            
            # 2. Finalize record through HarnessLoop (pure finalization)
            harness = HarnessLoop(vault_root)
            record = harness.evaluate_query("What are feline CKD markers?")
            
            harness_result = harness.process_query_result(
                record=record,
                answer=result["answer"],
                source_ids=[src_id],
                disease=result["disease"],
                question_type=result["question_type"],
                research_trace=result["research_trace"],
                loaded_source_ids=result["loaded_source_ids"],
                retrieval_events=result["retrieval_events"],
                source_snapshots=result["source_snapshots"]
            )
            
            finalized_record = harness_result["record"]
            assert len(finalized_record.retrieval_events) == 1
            assert len(finalized_record.source_snapshots) == 1
            assert finalized_record.retrieval_events[0].engine == "vault"
            assert finalized_record.source_snapshots[0].source_id == src_id
            
            # 3. Explicit Save and Integrity check
            # Verify record doesn't auto-save
            json_file = records_dir / "json" / f"{finalized_record.record_id}.json"
            assert not json_file.exists()
            
            # Save explicitly
            saved_path = harness.save_record(finalized_record)
            assert json_file.exists()
            
            # Verify commit manifest exists
            manifest_file = records_dir / "manifests" / f"{finalized_record.record_id}.manifest.json"
            assert manifest_file.exists()
            
            # Read manifest
            with open(manifest_file, "r") as f:
                manifest = json.load(f)
            assert manifest["schema_version"] == 2
            assert "json_hash" in manifest
            assert "markdown_hash" in manifest
            
            # Verify integrity
            integrity = harness.record_store.verify_record_integrity(finalized_record.record_id)
            assert integrity["valid"] is True
            assert integrity["version"] == 2
            assert len(integrity["issues"]) == 0
            
            # 4. Duplicate Check & Version Increment
            duplicate_record = harness.evaluate_query("What are feline CKD markers?")
            # Populate duplicate record with same values to test find_equivalent_record
            harness_result_dup = harness.process_query_result(
                record=duplicate_record,
                answer=result["answer"],
                source_ids=[src_id],
                disease=result["disease"],
                question_type=result["question_type"],
                research_trace=result["research_trace"],
                loaded_source_ids=result["loaded_source_ids"],
                retrieval_events=result["retrieval_events"],
                source_snapshots=result["source_snapshots"]
            )
            dup_record = harness_result_dup["record"]
            
            # Find equivalent record
            equivalent = harness.record_store.find_equivalent_record(dup_record)
            assert equivalent is not None
            assert equivalent.record_id == finalized_record.record_id
            
            # Save duplicate as new version
            dup_record.record_version = equivalent.record_version + 1
            dup_record.parent_record_id = equivalent.record_id
            
            dup_saved_path = harness.save_record(dup_record)
            assert dup_saved_path.exists()
            
            # Load and verify duplicate has incremented version and parent link
            loaded_dup = harness.record_store.load(dup_record.record_id)
            assert loaded_dup is not None
            assert loaded_dup.record_version == 2
            assert loaded_dup.parent_record_id == finalized_record.record_id

    print("✓ Integration test: query flow -> RetrievalEvent/SourceSnapshot -> Manifest -> Duplicate Warning -> New Version")


if __name__ == "__main__":
    test_gate6a_query_to_save_integration()
