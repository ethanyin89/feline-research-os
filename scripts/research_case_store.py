"""Contained, revisioned, atomic JSON persistence for Research Cases."""

from __future__ import annotations

import copy
import fcntl
import json
import os
import tempfile
from contextlib import contextmanager
from pathlib import Path

from research_cases import (
    SCHEMA_VERSION,
    ResearchCaseError,
    apply_operation,
    canonical_json,
    content_hash,
    new_case,
    utc_now,
    validate_case_id,
    validate_current,
)


class ResearchCaseStore:
    def __init__(self, root: Path, write_enabled: bool = True):
        self.root = root.resolve()
        self.write_enabled = write_enabled

    def _require_write(self) -> None:
        if not self.write_enabled:
            raise ResearchCaseError(
                "WRITE_MODE_DISABLED",
                "Research Case writes are disabled for this deployment.",
            )

    def _case_path(self, case_id: str) -> Path:
        validate_case_id(case_id)
        path = (self.root / f"{case_id}.json").resolve()
        try:
            path.relative_to(self.root)
        except ValueError as exc:
            raise ResearchCaseError("PATH_OUTSIDE_ROOT", "Case path escaped the store root.") from exc
        return path

    def _lock_path(self, case_id: str) -> Path:
        return self._case_path(case_id).with_suffix(".lock")

    @contextmanager
    def _locked(self, case_id: str):
        self.root.mkdir(parents=True, exist_ok=True)
        lock_path = self._lock_path(case_id)
        with lock_path.open("a+", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)

    def _read_raw(self, path: Path) -> dict:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError as exc:
            raise ResearchCaseError("CASE_NOT_FOUND", f"Research Case not found: {path.stem}") from exc
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ResearchCaseError("CORRUPT_CASE", f"Could not read Research Case: {path.name}") from exc
        if not isinstance(data, dict):
            raise ResearchCaseError("CORRUPT_CASE", "Research Case root must be an object.")
        return data

    def _migrate(self, document: dict) -> tuple[dict, bool]:
        version = document.get("schema_version")
        if version == SCHEMA_VERSION:
            return document, False
        if not isinstance(version, int):
            raise ResearchCaseError("SCHEMA_UNSUPPORTED", "Research Case schema version is missing.")
        if version > SCHEMA_VERSION:
            raise ResearchCaseError(
                "SCHEMA_UNSUPPORTED",
                f"Research Case schema {version} is newer than supported schema {SCHEMA_VERSION}.",
            )
        migrated = copy.deepcopy(document)
        while migrated["schema_version"] < SCHEMA_VERSION:
            if migrated["schema_version"] == 0:
                migrated.setdefault("status", "active")
                migrated.setdefault("revisions", [])
                migrated.setdefault("events", [])
                migrated["current"].setdefault("stale_stages", [])
                migrated["schema_version"] = 1
            else:
                raise ResearchCaseError("MIGRATION_FAILED", "No migration path is available.")
        return migrated, True

    def _atomic_write(self, path: Path, document: dict) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        payload = json.dumps(document, ensure_ascii=True, indent=2, sort_keys=True) + "\n"
        temp_path: Path | None = None
        try:
            with tempfile.NamedTemporaryFile(
                "w",
                encoding="utf-8",
                dir=self.root,
                prefix=f".{path.stem}-",
                suffix=".tmp",
                delete=False,
            ) as handle:
                temp_path = Path(handle.name)
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temp_path, path)
            directory_fd = os.open(self.root, os.O_RDONLY)
            try:
                os.fsync(directory_fd)
            finally:
                os.close(directory_fd)
        except OSError as exc:
            raise ResearchCaseError("WRITE_FAILED", f"Could not write Research Case: {path.name}") from exc
        finally:
            if temp_path and temp_path.exists():
                temp_path.unlink()

    def load(self, case_id: str) -> dict:
        path = self._case_path(case_id)
        document, _ = self._migrate(self._read_raw(path))
        validate_current(document.get("current") or {})
        return document

    def list_cases(self) -> list[dict]:
        """Return lightweight case summaries; corrupt records remain visible."""
        if not self.root.exists():
            return []
        summaries = []
        for path in sorted(self.root.glob("case-*.json")):
            try:
                document, _ = self._migrate(self._read_raw(path))
                frame = document.get("current", {}).get("frame", {})
                summaries.append(
                    {
                        "case_id": document.get("case_id", path.stem),
                        "question": frame.get("question", ""),
                        "owner": frame.get("owner", ""),
                        "reviewer": frame.get("reviewer", ""),
                        "deadline": frame.get("deadline", ""),
                        "revision": document.get("revision", 0),
                        "status": document.get("status", "active"),
                        "error": "",
                    }
                )
            except ResearchCaseError as exc:
                summaries.append(
                    {
                        "case_id": path.stem,
                        "question": "",
                        "owner": "",
                        "reviewer": "",
                        "deadline": "",
                        "revision": 0,
                        "status": "unreadable",
                        "error": exc.code,
                    }
                )
        return summaries

    def create(self, case_id: str, frame: dict, actor_label: str, now: str | None = None) -> dict:
        self._require_write()
        with self._locked(case_id):
            path = self._case_path(case_id)
            if path.exists():
                raise ResearchCaseError("VALIDATION_FAILED", f"Research Case already exists: {case_id}")
            document = new_case(case_id, frame, actor_label, now=now)
            return self._commit_snapshot(
                document,
                current=document["current"],
                actor_label=actor_label,
                reason="create case",
                operation_id=f"create-{case_id}",
                invalidated=[],
                timestamp=now or utc_now(),
                path=path,
            )

    def update(
        self,
        case_id: str,
        expected_revision: int,
        actor_label: str,
        reason: str,
        operation_id: str,
        operation: dict,
        now: str | None = None,
    ) -> dict:
        self._require_write()
        if not actor_label.strip() or not reason.strip() or not operation_id.strip():
            raise ResearchCaseError("VALIDATION_FAILED", "Actor, reason, and operation ID are required.")
        with self._locked(case_id):
            path = self._case_path(case_id)
            document, migrated = self._migrate(self._read_raw(path))
            if migrated:
                backup = path.with_suffix(f".schema-{document['schema_version'] - 1}.bak")
                if not backup.exists():
                    backup.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
            if any(event.get("operation_id") == operation_id for event in document.get("events", [])):
                return document
            if document.get("revision") != expected_revision:
                raise ResearchCaseError(
                    "CASE_VERSION_CONFLICT",
                    f"Expected revision {expected_revision}, found {document.get('revision')}.",
                    {"expected": expected_revision, "actual": document.get("revision")},
                )
            current, invalidated = apply_operation(document, operation)
            return self._commit_snapshot(
                document,
                current=current,
                actor_label=actor_label,
                reason=reason,
                operation_id=operation_id,
                invalidated=invalidated,
                timestamp=now or utc_now(),
                path=path,
            )

    def _commit_snapshot(
        self,
        document: dict,
        current: dict,
        actor_label: str,
        reason: str,
        operation_id: str,
        invalidated: list[str],
        timestamp: str,
        path: Path,
    ) -> dict:
        updated = copy.deepcopy(document)
        revision = int(updated.get("revision", 0)) + 1
        snapshot_hash = content_hash(current)
        updated["schema_version"] = SCHEMA_VERSION
        updated["revision"] = revision
        updated["updated_at"] = timestamp
        updated["current"] = copy.deepcopy(current)
        updated.setdefault("revisions", []).append(
            {
                "revision": revision,
                "created_at": timestamp,
                "actor_label": actor_label,
                "identity_assurance": "self_asserted",
                "reason": reason,
                "content_hash": snapshot_hash,
                "snapshot": copy.deepcopy(current),
            }
        )
        updated.setdefault("events", []).append(
            {
                "revision": revision,
                "created_at": timestamp,
                "actor_label": actor_label,
                "identity_assurance": "self_asserted",
                "operation_id": operation_id,
                "reason": reason,
                "invalidated_stages": invalidated,
            }
        )
        validate_current(updated["current"])
        canonical_json(updated)
        self._atomic_write(path, updated)
        return updated
