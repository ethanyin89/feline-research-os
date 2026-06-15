"""
Research Record persistence layer.

Stores durable research records as JSON files,
enabling retrieval and continuation of past work.

Gate 6A additions:
- Commit manifest for atomic dual-write verification
- Reconciliation queue for interrupted writes
- Schema migration support
"""

from __future__ import annotations

import hashlib
import json
import fcntl
import os
import tempfile
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Any

from .schemas import ResearchRecord, TaskType, VerifierStatus, SCHEMA_VERSION


class RecordStore:
    """
    Persistent storage for Research Records.

    Records are stored as JSON files in a designated directory,
    with markdown summaries generated for human review.

    Gate 6A features:
    - Commit manifest ensures both JSON and Markdown are valid
    - Reconciliation queue tracks interrupted writes
    - Schema migration for v1 -> v2 records
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
        self.manifest_path = self.base_path / "manifests"
        self.reconciliation_path = self.base_path / "reconciliation"

        # Ensure directories exist
        self.json_path.mkdir(parents=True, exist_ok=True)
        self.markdown_path.mkdir(parents=True, exist_ok=True)
        self.manifest_path.mkdir(parents=True, exist_ok=True)
        self.reconciliation_path.mkdir(parents=True, exist_ok=True)

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

    @staticmethod
    def _compute_hash(content: str) -> str:
        """Compute SHA-256 hash of content."""
        return hashlib.sha256(content.encode("utf-8")).hexdigest()

    def _manifest_path_for(self, record_id: str) -> Path:
        """Get manifest path for a record."""
        return self.manifest_path / f"{record_id}.manifest.json"

    def _reconciliation_path_for(self, record_id: str) -> Path:
        """Get reconciliation queue path for a record."""
        return self.reconciliation_path / f"{record_id}.pending.json"

    def _write_manifest(self, record_id: str, json_hash: str, md_hash: str) -> None:
        """Write commit manifest after successful dual-write."""
        manifest = {
            "record_id": record_id,
            "timestamp": datetime.now().isoformat(),
            "schema_version": SCHEMA_VERSION,
            "json_hash": json_hash,
            "markdown_hash": md_hash,
        }
        manifest_file = self._manifest_path_for(record_id)
        self._atomic_write_text(
            manifest_file,
            json.dumps(manifest, indent=2) + "\n"
        )

    def _add_to_reconciliation(self, record_id: str, stage: str, error: str) -> None:
        """Add a failed write to the reconciliation queue."""
        entry = {
            "record_id": record_id,
            "timestamp": datetime.now().isoformat(),
            "stage": stage,  # "json", "markdown", "manifest"
            "error": error,
        }
        recon_file = self._reconciliation_path_for(record_id)
        self._atomic_write_text(
            recon_file,
            json.dumps(entry, indent=2) + "\n"
        )

    def _clear_reconciliation(self, record_id: str) -> None:
        """Clear reconciliation entry after successful save."""
        recon_file = self._reconciliation_path_for(record_id)
        if recon_file.exists():
            recon_file.unlink()

    def verify_record_integrity(self, record_id: str) -> Dict[str, Any]:
        """
        Verify record integrity using commit manifest.

        Returns:
            Dict with 'valid' bool and 'issues' list
        """
        json_file = self._record_json_path(record_id)
        md_file = self._record_markdown_path(record_id)
        manifest_file = self._manifest_path_for(record_id)

        issues = []

        if not json_file.exists():
            issues.append("JSON file missing")
        if not md_file.exists():
            issues.append("Markdown file missing")

        # Records without manifests are v1 (pre-Gate 6A)
        if not manifest_file.exists():
            return {"valid": len(issues) == 0, "issues": issues, "version": 1}

        try:
            with open(manifest_file, "r", encoding="utf-8") as f:
                manifest = json.load(f)

            if json_file.exists():
                with open(json_file, "r", encoding="utf-8") as f:
                    json_content = f.read()
                if self._compute_hash(json_content) != manifest.get("json_hash"):
                    issues.append("JSON hash mismatch")

            if md_file.exists():
                with open(md_file, "r", encoding="utf-8") as f:
                    md_content = f.read()
                if self._compute_hash(md_content) != manifest.get("markdown_hash"):
                    issues.append("Markdown hash mismatch")

        except (json.JSONDecodeError, IOError) as e:
            issues.append(f"Manifest read error: {e}")

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "version": manifest.get("schema_version", 1) if manifest_file.exists() else 1
        }

    def list_reconciliation_queue(self) -> List[Dict[str, Any]]:
        """List all records in the reconciliation queue."""
        entries = []
        for recon_file in self.reconciliation_path.glob("*.pending.json"):
            try:
                with open(recon_file, "r", encoding="utf-8") as f:
                    entries.append(json.load(f))
            except (json.JSONDecodeError, IOError):
                continue
        return sorted(entries, key=lambda x: x.get("timestamp", ""), reverse=True)

    def save(self, record: ResearchRecord) -> Path:
        """
        Save a research record with commit manifest.

        Saves both JSON (for programmatic access) and
        Markdown (for human review), then writes a commit
        manifest to verify integrity.

        Args:
            record: The research record to save

        Returns:
            Path to the saved JSON file
        """
        # Update persistence metadata
        record.last_saved = datetime.now()
        record.persistence_status = "healthy"

        json_file = self._record_json_path(record.record_id)
        md_file = self._record_markdown_path(record.record_id)

        json_content = json.dumps(record.to_dict(), indent=2, ensure_ascii=False) + "\n"
        md_content = record.to_markdown() + "\n"

        json_hash = self._compute_hash(json_content)
        md_hash = self._compute_hash(md_content)

        with self._locked(record.record_id):
            json_written = False
            md_written = False
            try:
                # Write JSON
                self._atomic_write_text(json_file, json_content)
                json_written = True

                # Write Markdown
                self._atomic_write_text(md_file, md_content)
                md_written = True

                # Write manifest
                self._write_manifest(record.record_id, json_hash, md_hash)

                # Clear any prior reconciliation entry
                self._clear_reconciliation(record.record_id)

            except Exception as e:
                # Track what failed for reconciliation
                if not json_written:
                    self._add_to_reconciliation(record.record_id, "json", str(e))
                elif not md_written:
                    self._add_to_reconciliation(record.record_id, "markdown", str(e))
                else:
                    self._add_to_reconciliation(record.record_id, "manifest", str(e))

                # Clean up partial writes
                if json_written and json_file.exists():
                    json_file.unlink()
                if md_written and md_file.exists():
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
