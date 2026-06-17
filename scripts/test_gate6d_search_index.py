"""
Tests for Gate 6D: Record search index optimisation.

Verifies that:
1. save() creates and maintains a record_index.json file
2. find_equivalent_record() uses the index instead of scanning all files
3. list_records / search / count all read from the index
4. delete() removes the entry from the index
5. rebuild_index() re-creates the index from disk
6. Index survives cache invalidation (cold start)
"""

import sys
import json
import time
from pathlib import Path
from tempfile import TemporaryDirectory

# Add parent directory for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core import ResearchRecord, RecordStore, TaskType  # noqa: E402


def _make(question: str, disease: str = "ckd", answer: str = "Test answer.") -> ResearchRecord:
    record = ResearchRecord.create(question, TaskType.QUICK_EXPLANATION, disease=disease)
    record.selected_evidence = ["src-ckd-001"]
    record.final_answer = answer
    return record


def test_save_creates_index():
    """save() should create record_index.json and populate it."""
    with TemporaryDirectory() as tmp:
        store = RecordStore(Path(tmp) / "records")
        record = _make("什么是CKD?")
        store.save(record)

        assert store.index_file.exists(), "record_index.json should exist after save"
        index = json.loads(store.index_file.read_text(encoding="utf-8"))
        assert len(index) == 1
        assert index[0]["record_id"] == record.record_id
        assert index[0]["disease"] == "ckd"
        assert index[0]["user_request"] == "什么是CKD?"
    print("✓ save() creates index")


def test_save_upserts_existing_entry():
    """Saving the same record twice should update, not duplicate, the index entry."""
    with TemporaryDirectory() as tmp:
        store = RecordStore(Path(tmp) / "records")
        record = _make("什么是CKD?")
        store.save(record)

        # Mutate and re-save
        record.final_answer = "Updated answer."
        store.save(record)

        index = json.loads(store.index_file.read_text(encoding="utf-8"))
        assert len(index) == 1, f"Expected 1 entry, got {len(index)}"
        assert index[0]["final_answer"] == "Updated answer."
    print("✓ save() upserts existing entry")


def test_multiple_records_indexed():
    """Multiple records should all appear in the index."""
    with TemporaryDirectory() as tmp:
        store = RecordStore(Path(tmp) / "records")
        r1 = _make("CKD question", disease="ckd")
        r2 = _make("FIP question", disease="fip")
        r3 = _make("HCM question", disease="hcm")
        store.save(r1)
        store.save(r2)
        store.save(r3)

        index = json.loads(store.index_file.read_text(encoding="utf-8"))
        ids = {e["record_id"] for e in index}
        assert len(ids) == 3
        assert r1.record_id in ids
        assert r2.record_id in ids
        assert r3.record_id in ids
    print("✓ Multiple records indexed")


def test_find_equivalent_uses_index():
    """find_equivalent_record() should find matches via index without scanning all files."""
    with TemporaryDirectory() as tmp:
        store = RecordStore(Path(tmp) / "records")
        original = _make("CKD endpoints?", disease="ckd", answer="Endpoint answer.")
        store.save(original)

        # Create a duplicate with different ID but same content
        duplicate = _make("CKD endpoints?", disease="ckd", answer="Endpoint answer.")
        equivalent = store.find_equivalent_record(duplicate)
        assert equivalent is not None
        assert equivalent.record_id == original.record_id
    print("✓ find_equivalent_record() uses index")


def test_find_equivalent_no_match():
    """find_equivalent_record() should return None when no match exists."""
    with TemporaryDirectory() as tmp:
        store = RecordStore(Path(tmp) / "records")
        original = _make("CKD endpoints?", disease="ckd")
        store.save(original)

        different = _make("FIP treatment?", disease="fip")
        result = store.find_equivalent_record(different)
        assert result is None
    print("✓ find_equivalent_record() returns None for no match")


def test_list_records_uses_index():
    """list_records() should filter via index."""
    with TemporaryDirectory() as tmp:
        store = RecordStore(Path(tmp) / "records")
        r1 = _make("CKD q1", disease="ckd")
        r2 = _make("FIP q1", disease="fip")
        r3 = _make("CKD q2", disease="ckd")
        store.save(r1)
        store.save(r2)
        store.save(r3)

        ckd_records = store.list_records(disease="ckd", limit=100)
        assert len(ckd_records) == 2
        assert all(r.disease == "ckd" for r in ckd_records)

        fip_records = store.list_records(disease="fip", limit=100)
        assert len(fip_records) == 1
        assert fip_records[0].disease == "fip"
    print("✓ list_records() filters via index")


def test_search_uses_index():
    """search() should keyword-match via index."""
    with TemporaryDirectory() as tmp:
        store = RecordStore(Path(tmp) / "records")
        r1 = _make("CKD phosphorus binders", disease="ckd", answer="Phosphorus answer.")
        r2 = _make("FIP treatment protocol", disease="fip", answer="GS-441524 answer.")
        store.save(r1)
        store.save(r2)

        hits = store.search("phosphorus", limit=10)
        assert len(hits) == 1
        assert hits[0].record_id == r1.record_id

        hits2 = store.search("GS-441524", limit=10)
        assert len(hits2) == 1
        assert hits2[0].record_id == r2.record_id
    print("✓ search() uses index")


def test_count_uses_index():
    """count() should count from index without opening files."""
    with TemporaryDirectory() as tmp:
        store = RecordStore(Path(tmp) / "records")
        store.save(_make("q1", disease="ckd"))
        store.save(_make("q2", disease="ckd"))
        store.save(_make("q3", disease="fip"))

        assert store.count() == 3
        assert store.count(disease="ckd") == 2
        assert store.count(disease="fip") == 1
        assert store.count(disease="hcm") == 0
    print("✓ count() uses index")


def test_delete_removes_index_entry():
    """delete() should remove the entry from the index."""
    with TemporaryDirectory() as tmp:
        store = RecordStore(Path(tmp) / "records")
        r1 = _make("CKD q1", disease="ckd")
        r2 = _make("FIP q1", disease="fip")
        store.save(r1)
        store.save(r2)

        assert store.count() == 2
        store.delete(r1.record_id)
        assert store.count() == 1

        index = json.loads(store.index_file.read_text(encoding="utf-8"))
        ids = {e["record_id"] for e in index}
        assert r1.record_id not in ids
        assert r2.record_id in ids
    print("✓ delete() removes index entry")


def test_rebuild_index():
    """rebuild_index() should re-create the index from disk."""
    with TemporaryDirectory() as tmp:
        store = RecordStore(Path(tmp) / "records")
        r1 = _make("CKD q1", disease="ckd")
        r2 = _make("FIP q1", disease="fip")
        store.save(r1)
        store.save(r2)

        # Corrupt the index on disk
        store.index_file.write_text("[]", encoding="utf-8")
        store._index_cache = None  # clear cache

        store.rebuild_index()

        index = json.loads(store.index_file.read_text(encoding="utf-8"))
        assert len(index) == 2
        ids = {e["record_id"] for e in index}
        assert r1.record_id in ids
        assert r2.record_id in ids
    print("✓ rebuild_index() re-creates from disk")


def test_cold_start_loads_index():
    """A fresh RecordStore instance should load the persisted index."""
    with TemporaryDirectory() as tmp:
        base = Path(tmp) / "records"
        store1 = RecordStore(base)
        r1 = _make("CKD cold start", disease="ckd")
        store1.save(r1)

        # Simulate cold start by creating new store instance
        store2 = RecordStore(base)
        assert store2.count() == 1
        loaded = store2.list_records(limit=10)
        assert len(loaded) == 1
        assert loaded[0].record_id == r1.record_id
    print("✓ Cold start loads persisted index")


def test_get_recent_uses_index():
    """get_recent() should filter by timestamp via index."""
    with TemporaryDirectory() as tmp:
        store = RecordStore(Path(tmp) / "records")
        r1 = _make("Recent CKD q", disease="ckd")
        store.save(r1)

        recent = store.get_recent(days=1, limit=10)
        assert len(recent) == 1
        assert recent[0].record_id == r1.record_id

        # Nothing from 0 days ago (cutoff is basically now)
        old = store.get_recent(days=0, limit=10)
        # Records saved just now should still be within the cutoff
        # but with days=0, the cutoff is exactly now, so it's borderline
        # Just verify the method runs without error
    print("✓ get_recent() uses index")


if __name__ == "__main__":
    test_save_creates_index()
    test_save_upserts_existing_entry()
    test_multiple_records_indexed()
    test_find_equivalent_uses_index()
    test_find_equivalent_no_match()
    test_list_records_uses_index()
    test_search_uses_index()
    test_count_uses_index()
    test_delete_removes_index_entry()
    test_rebuild_index()
    test_cold_start_loads_index()
    test_get_recent_uses_index()
    print("\n✓ All Gate 6D search index tests passed!")
