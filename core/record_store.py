"""
Research Record persistence layer.

Stores durable research records as JSON files,
enabling retrieval and continuation of past work.
"""

from __future__ import annotations

import json
import fcntl
import os
import tempfile
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from .schemas import ResearchRecord, TaskType, VerifierStatus


class RecordStore:
    """
    Persistent storage for Research Records.

    Records are stored as JSON files in a designated directory,
    with markdown summaries generated for human review.
    """

    def __init__(self, base_path: Path):
        """
        Initialize the record store.

        Args:
            base_path: Directory to store research records
        """
        self.base_path = Path(base_path).resolve()
        self.json_path = self.base_path / "json"
        self.markdown_path = self.base_path / "markdown"

        # Ensure directories exist
        self.json_path.mkdir(parents=True, exist_ok=True)
        self.markdown_path.mkdir(parents=True, exist_ok=True)

    def _record_json_path(self, record_id: str) -> Path:
        path = (self.json_path / f"{record_id}.json").resolve()
        path.relative_to(self.json_path)
        return path

    def _record_markdown_path(self, record_id: str) -> Path:
        path = (self.markdown_path / f"{record_id}.md").resolve()
        path.relative_to(self.markdown_path)
        return path

    def _lock_path(self, record_id: str) -> Path:
        return self._record_json_path(record_id).with_suffix(".lock")

    @contextmanager
    def _locked(self, record_id: str):
        self.base_path.mkdir(parents=True, exist_ok=True)
        lock_path = self._lock_path(record_id)
        with lock_path.open("a+", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)

    def _atomic_write_text(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        temp_path: Optional[Path] = None
        try:
            with tempfile.NamedTemporaryFile(
                "w",
                encoding="utf-8",
                dir=path.parent,
                prefix=f".{path.stem}-",
                suffix=".tmp",
                delete=False,
            ) as handle:
                temp_path = Path(handle.name)
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temp_path, path)
            dir_fd = os.open(path.parent, os.O_RDONLY)
            try:
                os.fsync(dir_fd)
            finally:
                os.close(dir_fd)
        finally:
            if temp_path and temp_path.exists():
                temp_path.unlink()

    @staticmethod
    def _normalize_text(text: str) -> str:
        return " ".join(text.split()).strip().lower()

    def save(self, record: ResearchRecord) -> Path:
        """
        Save a research record.

        Saves both JSON (for programmatic access) and
        Markdown (for human review).

        Args:
            record: The research record to save

        Returns:
            Path to the saved JSON file
        """
        json_file = self._record_json_path(record.record_id)
        md_file = self._record_markdown_path(record.record_id)

        with self._locked(record.record_id):
            json_written = False
            try:
                self._atomic_write_text(
                    json_file,
                    json.dumps(record.to_dict(), indent=2, ensure_ascii=False) + "\n",
                )
                json_written = True
                self._atomic_write_text(md_file, record.to_markdown() + "\n")
            except Exception:
                if json_written and json_file.exists():
                    json_file.unlink()
                if md_file.exists():
                    md_file.unlink()
                raise

        return json_file

    def find_equivalent_record(self, record: ResearchRecord) -> Optional[ResearchRecord]:
        """
        Find a saved record with the same normalized request, disease, task, evidence,
        and answer text.

        Returns:
            Matching ResearchRecord if one exists, otherwise None.
        """
        target_request = self._normalize_text(record.user_request)
        target_answer = self._normalize_text(record.final_answer)
        target_sources = list(dict.fromkeys(record.selected_evidence))
        target_disease = self._normalize_text(record.disease)
        target_task_type = record.task_type.value

        for existing in self.list_records(limit=10_000):
            if existing.record_id == record.record_id:
                continue
            if self._normalize_text(existing.user_request) != target_request:
                continue
            if self._normalize_text(existing.disease) != target_disease:
                continue
            if existing.task_type.value != target_task_type:
                continue
            if self._normalize_text(existing.final_answer) != target_answer:
                continue
            if list(dict.fromkeys(existing.selected_evidence)) != target_sources:
                continue
            return existing

        return None

    def load(self, record_id: str) -> Optional[ResearchRecord]:
        """
        Load a research record by ID.

        Args:
            record_id: The record ID to load

        Returns:
            ResearchRecord if found, None otherwise
        """
        json_file = self._record_json_path(record_id)
        if not json_file.exists():
            return None

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        return ResearchRecord.from_dict(data)

    def list_records(
        self,
        disease: Optional[str] = None,
        task_type: Optional[TaskType] = None,
        status: Optional[VerifierStatus] = None,
        limit: int = 50,
    ) -> List[ResearchRecord]:
        """
        List research records with optional filtering.

        Args:
            disease: Filter by disease
            task_type: Filter by task type
            status: Filter by verification status
            limit: Maximum records to return

        Returns:
            List of matching ResearchRecords
        """
        records = []

        # Load all records
        for json_file in sorted(self.json_path.glob("*.json"), reverse=True):
            if len(records) >= limit:
                break

            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                record = ResearchRecord.from_dict(data)

                # Apply filters
                if disease and record.disease.lower() != disease.lower():
                    continue
                if task_type and record.task_type != task_type:
                    continue
                if status and record.verifier_status != status:
                    continue

                records.append(record)

            except (json.JSONDecodeError, KeyError) as e:
                # Skip malformed records
                continue

        return records

    def search(self, query: str, limit: int = 20) -> List[ResearchRecord]:
        """
        Search records by text content.

        Simple keyword search in user_request, scope, and final_answer.

        Args:
            query: Search query
            limit: Maximum results

        Returns:
            Matching ResearchRecords
        """
        query_lower = query.lower()
        matches = []

        for json_file in sorted(self.json_path.glob("*.json"), reverse=True):
            if len(matches) >= limit:
                break

            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)

                # Search in key text fields
                searchable = " ".join([
                    data.get("user_request", ""),
                    data.get("scope", ""),
                    data.get("final_answer", ""),
                    data.get("disease", ""),
                ]).lower()

                if query_lower in searchable:
                    matches.append(ResearchRecord.from_dict(data))

            except (json.JSONDecodeError, KeyError):
                continue

        return matches

    def get_recent(self, days: int = 7, limit: int = 20) -> List[ResearchRecord]:
        """
        Get records from the last N days.

        Args:
            days: Number of days to look back
            limit: Maximum results

        Returns:
            Recent ResearchRecords
        """
        cutoff = datetime.now().timestamp() - (days * 24 * 60 * 60)
        records = []

        for json_file in sorted(self.json_path.glob("*.json"), reverse=True):
            if len(records) >= limit:
                break

            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)

                timestamp = datetime.fromisoformat(data["timestamp"])
                if timestamp.timestamp() >= cutoff:
                    records.append(ResearchRecord.from_dict(data))

            except (json.JSONDecodeError, KeyError):
                continue

        return records

    def get_related(
        self,
        disease: str,
        task_type: Optional[TaskType] = None,
        exclude_id: Optional[str] = None,
        limit: int = 5,
    ) -> List[ResearchRecord]:
        """
        Get related records for building on past work.

        Useful for the retrieval memory layer - finding
        what was previously concluded about a topic.

        Args:
            disease: Disease to match
            task_type: Optional task type filter
            exclude_id: Record ID to exclude (usually current record)
            limit: Maximum results

        Returns:
            Related ResearchRecords
        """
        records = []

        for json_file in sorted(self.json_path.glob("*.json"), reverse=True):
            if len(records) >= limit:
                break

            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)

                # Skip excluded record
                if exclude_id and data["record_id"] == exclude_id:
                    continue

                # Match disease
                if data.get("disease", "").lower() != disease.lower():
                    continue

                # Optionally match task type
                if task_type and data.get("task_type") != task_type.value:
                    continue

                # Only include verified records
                if data.get("verifier_status") != "passed":
                    continue

                records.append(ResearchRecord.from_dict(data))

            except (json.JSONDecodeError, KeyError):
                continue

        return records

    def count(self, disease: Optional[str] = None) -> int:
        """
        Count total records, optionally filtered by disease.

        Args:
            disease: Optional disease filter

        Returns:
            Count of matching records
        """
        if not disease:
            return len(list(self.json_path.glob("*.json")))

        count = 0
        for json_file in self.json_path.glob("*.json"):
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if data.get("disease", "").lower() == disease.lower():
                    count += 1
            except (json.JSONDecodeError, KeyError):
                continue

        return count

    def delete(self, record_id: str) -> bool:
        """
        Delete a research record.

        Args:
            record_id: The record ID to delete

        Returns:
            True if deleted, False if not found
        """
        json_file = self.json_path / f"{record_id}.json"
        md_file = self.markdown_path / f"{record_id}.md"

        deleted = False
        if json_file.exists():
            json_file.unlink()
            deleted = True
        if md_file.exists():
            md_file.unlink()

        return deleted
