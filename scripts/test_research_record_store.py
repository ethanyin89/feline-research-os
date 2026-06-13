"""
Tests for Research Record persistence.
"""

import sys
from pathlib import Path
from tempfile import TemporaryDirectory

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core import ResearchRecord, RecordStore, TaskType  # noqa: E402


def make_record(question: str = "什么是FIP？", answer: str = "FIP is feline infectious peritonitis.") -> ResearchRecord:
    record = ResearchRecord.create(question, TaskType.QUICK_EXPLANATION, disease="fip")
    record.selected_evidence = ["src-fip-001"]
    record.final_answer = answer
    record.key_decisions = ["Use explicit save boundary"]
    record.uncertainties = ["Answer is brief"]
    record.verifier_status = record.compute_verifier_status()
    return record


def test_save_load_roundtrip_and_duplicate_detection():
    with TemporaryDirectory() as tmp:
        store = RecordStore(Path(tmp) / "records")
        record = make_record()

        out_path = store.save(record)
        assert out_path.exists()
        assert out_path.name.endswith(".json")
        assert (Path(tmp) / "records" / "markdown" / f"{record.record_id}.md").exists()

        loaded = store.load(record.record_id)
        assert loaded is not None
        assert loaded.record_id == record.record_id
        assert loaded.final_answer == record.final_answer
        assert loaded.selected_evidence == record.selected_evidence

        duplicate = make_record()
        duplicate.record_id = ResearchRecord.generate_id()
        equivalent = store.find_equivalent_record(duplicate)
        assert equivalent is not None
        assert equivalent.record_id == record.record_id
    print("✓ Save/load roundtrip and duplicate detection")


def test_filters_and_search():
    with TemporaryDirectory() as tmp:
        store = RecordStore(Path(tmp) / "records")

        fip = make_record(question="什么是FIP？", answer="FIP answer")
        ckd = ResearchRecord.create("猫CKD终点指标", TaskType.ENDPOINT_SELECTION, disease="ckd")
        ckd.final_answer = "CKD endpoint answer"
        ckd.selected_evidence = ["src-ckd-001"]
        ckd.verifier_status = ckd.compute_verifier_status()

        store.save(fip)
        store.save(ckd)

        all_records = store.list_records(limit=10)
        assert len(all_records) == 2

        fip_records = store.list_records(disease="fip", limit=10)
        assert len(fip_records) == 1
        assert fip_records[0].disease == "fip"

        search_hits = store.search("CKD endpoint", limit=10)
        assert len(search_hits) == 1
        assert search_hits[0].record_id == ckd.record_id
    print("✓ Filters and search")


def test_path_containment_rejects_escape():
    with TemporaryDirectory() as tmp:
        store = RecordStore(Path(tmp) / "records")
        record = make_record()
        record.record_id = "../escape"

        try:
            store.save(record)
            raised = False
        except ValueError:
            raised = True

        assert raised, "Path containment should reject escaping record IDs"
    print("✓ Path containment rejects escaping record IDs")


def test_save_rolls_back_on_partial_failure():
    with TemporaryDirectory() as tmp:
        store = RecordStore(Path(tmp) / "records")
        record = make_record()

        original_write = store._atomic_write_text

        def fail_on_markdown(path: Path, content: str) -> None:
            if path.suffix == ".md":
                raise RuntimeError("forced markdown failure")
            return original_write(path, content)

        store._atomic_write_text = fail_on_markdown  # type: ignore[assignment]

        try:
            store.save(record)
            raised = False
        except RuntimeError:
            raised = True

        assert raised, "Forced markdown failure should bubble up"
        assert not (Path(tmp) / "records" / "json" / f"{record.record_id}.json").exists()
        assert not (Path(tmp) / "records" / "markdown" / f"{record.record_id}.md").exists()
    print("✓ Partial save rolls back cleanly")


def run_all_tests():
    test_save_load_roundtrip_and_duplicate_detection()
    test_filters_and_search()
    test_path_containment_rejects_escape()
    test_save_rolls_back_on_partial_failure()
    print("All Research Record store tests passed!")


if __name__ == "__main__":
    run_all_tests()
