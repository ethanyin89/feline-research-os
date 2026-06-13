"""Research Case domain model, invariants, transitions, and typed errors."""

from __future__ import annotations

import copy
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import PurePosixPath
from typing import Any


SCHEMA_VERSION = 1
STAGES = ("frame", "criteria", "evidence", "challenge")
PROGRESS_STATES = ("not_started", "in_progress", "blocked", "complete")
FRESHNESS_STATES = ("current", "stale")
CASE_ID_RE = re.compile(r"^case-[a-z0-9](?:[a-z0-9-]{1,62}[a-z0-9])?$")
ENTITY_ID_RE = re.compile(r"^(criterion|claim|evidence|challenge|gap|blocker|assumption)-[a-z0-9-]{1,64}$")

FRAME_REQUIRED = (
    "question",
    "scope",
    "alternatives",
    "asset",
    "indication",
    "jurisdiction",
    "owner",
    "reviewer",
    "deadline",
)
FRAME_SEMANTIC = {
    "question",
    "scope",
    "alternatives",
    "asset",
    "indication",
    "jurisdiction",
}

ERROR_REGISTRY = {
    "WRITE_MODE_DISABLED": "Open the repository on persistent local storage.",
    "CASE_NOT_FOUND": "Return to the case list and select an existing case.",
    "SCHEMA_UNSUPPORTED": "Open read-only or run a supported migration.",
    "CORRUPT_CASE": "Preserve the file and restore from a prior snapshot or backup.",
    "VALIDATION_FAILED": "Correct the highlighted fields and retry.",
    "INVALID_TRANSITION": "Complete the unmet stage requirements first.",
    "GATE_BLOCKED": "Resolve the named blocker before advancing.",
    "CASE_VERSION_CONFLICT": "Retain the draft, reload, and reconcile changes.",
    "WRITE_FAILED": "Retain the draft and retry after checking storage.",
    "SOURCE_UNAVAILABLE": "Keep citation metadata and remove verified status.",
    "SOURCE_CHANGED": "Mark affected claims stale and review the new source version.",
    "PATH_OUTSIDE_ROOT": "Use repository-relative paths under approved roots.",
    "LEGACY_IMPORT_BLOCKED": "Review the artifact and admission requirements.",
    "MIGRATION_FAILED": "Restore the backup and inspect the migration error.",
    "UNEXPECTED_ERROR": "Retain input and show a redacted diagnostic.",
}


class ResearchCaseError(Exception):
    """Stable domain/storage error exposed to the UI."""

    def __init__(self, code: str, message: str, details: dict | None = None):
        super().__init__(message)
        self.code = code
        self.details = details or {}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def content_hash(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def validate_case_id(case_id: str) -> None:
    if not CASE_ID_RE.fullmatch(case_id or ""):
        raise ResearchCaseError(
            "VALIDATION_FAILED",
            "Case ID must use lowercase letters, numbers, and hyphens.",
            {"field": "case_id"},
        )


def _validate_entity_id(entity_id: str, prefix: str) -> None:
    if not ENTITY_ID_RE.fullmatch(entity_id or "") or not entity_id.startswith(f"{prefix}-"):
        raise ResearchCaseError(
            "VALIDATION_FAILED",
            f"Invalid {prefix} ID: {entity_id!r}",
            {"field": f"{prefix}_id"},
        )


def _validate_text(value: Any, field: str, max_length: int = 10_000) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ResearchCaseError(
            "VALIDATION_FAILED",
            f"{field} is required.",
            {"field": field},
        )
    if len(value) > max_length:
        raise ResearchCaseError(
            "VALIDATION_FAILED",
            f"{field} exceeds {max_length} characters.",
            {"field": field},
        )


def validate_frame(frame: dict) -> None:
    missing = [field for field in FRAME_REQUIRED if not frame.get(field)]
    if missing:
        raise ResearchCaseError(
            "VALIDATION_FAILED",
            f"Frame is missing required fields: {', '.join(missing)}",
            {"fields": missing},
        )
    _validate_text(frame["question"], "question", 2_000)
    _validate_text(frame["scope"], "scope", 5_000)
    if not isinstance(frame["alternatives"], list) or len(frame["alternatives"]) < 2:
        raise ResearchCaseError(
            "VALIDATION_FAILED",
            "Frame requires at least two alternatives.",
            {"field": "alternatives"},
        )
    for field in ("asset", "indication", "jurisdiction", "owner", "reviewer", "deadline"):
        _validate_text(frame[field], field, 500)


def validate_criteria(criteria: list[dict]) -> None:
    if not criteria:
        raise ResearchCaseError("VALIDATION_FAILED", "At least one criterion is required.")
    seen: set[str] = set()
    for item in criteria:
        criterion_id = item.get("criterion_id", "")
        _validate_entity_id(criterion_id, "criterion")
        if criterion_id in seen:
            raise ResearchCaseError("VALIDATION_FAILED", f"Duplicate criterion ID: {criterion_id}")
        seen.add(criterion_id)
        for field in ("name", "threshold", "applicability", "owner", "rationale"):
            _validate_text(item.get(field), f"{criterion_id}.{field}", 2_000)
        if not isinstance(item.get("required"), bool):
            raise ResearchCaseError(
                "VALIDATION_FAILED",
                f"{criterion_id}.required must be boolean.",
            )


def validate_claims(claims: list[dict], criterion_ids: set[str]) -> None:
    seen: set[str] = set()
    for claim in claims:
        claim_id = claim.get("claim_id", "")
        _validate_entity_id(claim_id, "claim")
        if claim_id in seen:
            raise ResearchCaseError("VALIDATION_FAILED", f"Duplicate claim ID: {claim_id}")
        seen.add(claim_id)
        _validate_text(claim.get("text"), f"{claim_id}.text", 5_000)
        linked = set(claim.get("criterion_ids") or [])
        if not linked or not linked.issubset(criterion_ids):
            raise ResearchCaseError(
                "VALIDATION_FAILED",
                f"{claim_id} must link only to existing criteria.",
            )
        disposition = claim.get("reviewed_disposition")
        if disposition not in {None, "supports", "contradicts", "mixed", "irrelevant", "uncertain"}:
            raise ResearchCaseError(
                "VALIDATION_FAILED",
                f"Invalid reviewed disposition for {claim_id}.",
            )
        for evidence in claim.get("evidence", []):
            _validate_entity_id(evidence.get("evidence_id", ""), "evidence")
            for field in ("source_id", "relative_path", "sha256", "observed_at", "polarity"):
                _validate_text(evidence.get(field), f"{claim_id}.evidence.{field}", 2_000)
            relative_path = PurePosixPath(evidence["relative_path"])
            if relative_path.is_absolute() or ".." in relative_path.parts:
                raise ResearchCaseError(
                    "PATH_OUTSIDE_ROOT",
                    "Evidence paths must be repository-relative and cannot contain '..'.",
                )
            if not re.fullmatch(r"src-[a-z0-9-]+-\d{3}", evidence["source_id"]):
                raise ResearchCaseError("VALIDATION_FAILED", "Evidence source ID is invalid.")
            if len(evidence["sha256"]) != 64:
                raise ResearchCaseError("VALIDATION_FAILED", "Evidence SHA-256 must be 64 characters.")


def validate_challenges(challenges: list[dict], claim_ids: set[str]) -> None:
    seen: set[str] = set()
    for challenge in challenges:
        challenge_id = challenge.get("challenge_id", "")
        _validate_entity_id(challenge_id, "challenge")
        if challenge_id in seen:
            raise ResearchCaseError("VALIDATION_FAILED", f"Duplicate challenge ID: {challenge_id}")
        seen.add(challenge_id)
        if challenge.get("claim_id") not in claim_ids:
            raise ResearchCaseError("VALIDATION_FAILED", f"{challenge_id} references an unknown claim.")
        for field in ("counterclaim", "reviewer", "rationale"):
            _validate_text(challenge.get(field), f"{challenge_id}.{field}", 5_000)
        if challenge.get("disposition") not in {
            "upheld",
            "revised",
            "rejected",
            "unresolved",
        }:
            raise ResearchCaseError("VALIDATION_FAILED", f"Invalid disposition for {challenge_id}.")


def validate_current(current: dict) -> None:
    validate_frame(current.get("frame") or {})
    criteria = current.get("criteria") or []
    if current.get("criteria_frozen_version", 0):
        validate_criteria(criteria)
    criterion_ids = {item["criterion_id"] for item in criteria if item.get("criterion_id")}
    claims = current.get("claims") or []
    validate_claims(claims, criterion_ids)
    claim_ids = {item["claim_id"] for item in claims if item.get("claim_id")}
    validate_challenges(current.get("challenges") or [], claim_ids)


def _active_blockers(current: dict, stage: str) -> list[dict]:
    return [
        blocker
        for blocker in current.get("blockers", [])
        if blocker.get("stage") == stage and not blocker.get("resolved_at")
    ]


def derive_stage_states(current: dict) -> dict:
    """Derive progress and freshness; neither is directly editable."""
    stale = set(current.get("stale_stages") or [])
    frame = current.get("frame") or {}
    criteria = current.get("criteria") or []
    claims = current.get("claims") or []
    challenges = current.get("challenges") or []

    frame_complete = not [field for field in FRAME_REQUIRED if not frame.get(field)]
    criteria_complete = bool(criteria and current.get("criteria_frozen_version"))

    required_ids = {c["criterion_id"] for c in criteria if c.get("required")}
    covered_ids: set[str] = set()
    for claim in claims:
        if claim.get("reviewed_disposition") or claim.get("explicit_gap"):
            covered_ids.update(claim.get("criterion_ids") or [])
    evidence_complete = criteria_complete and required_ids.issubset(covered_ids)

    challenged_ids = {
        challenge.get("claim_id")
        for challenge in challenges
        if challenge.get("disposition") in {"upheld", "revised", "rejected", "unresolved"}
    }
    challenge_complete = bool(claims) and all(
        claim["claim_id"] in challenged_ids or claim.get("challenge_blocked")
        for claim in claims
    )

    completion = {
        "frame": frame_complete,
        "criteria": criteria_complete,
        "evidence": evidence_complete,
        "challenge": challenge_complete,
    }
    has_content = {
        "frame": bool(frame),
        "criteria": bool(criteria),
        "evidence": bool(claims),
        "challenge": bool(challenges),
    }

    result = {}
    for stage in STAGES:
        if _active_blockers(current, stage):
            progress = "blocked"
        elif completion[stage]:
            progress = "complete"
        elif has_content[stage]:
            progress = "in_progress"
        else:
            progress = "not_started"
        result[stage] = {
            "progress": progress,
            "freshness": "stale" if stage in stale else "current",
        }
    return result


def new_case(case_id: str, frame: dict, actor_label: str, now: str | None = None) -> dict:
    validate_case_id(case_id)
    validate_frame(frame)
    _validate_text(actor_label, "actor_label", 200)
    timestamp = now or utc_now()
    current = {
        "frame": copy.deepcopy(frame),
        "criteria": [],
        "criteria_frozen_version": 0,
        "claims": [],
        "challenges": [],
        "blockers": [],
        "gaps": [],
        "assumptions": [],
        "legacy_attachments": [],
        "stale_stages": [],
    }
    return {
        "schema_version": SCHEMA_VERSION,
        "case_id": case_id,
        "revision": 0,
        "status": "active",
        "created_at": timestamp,
        "updated_at": timestamp,
        "current": current,
        "revisions": [],
        "events": [],
    }


def apply_operation(document: dict, operation: dict) -> tuple[dict, list[str]]:
    """Apply one validated domain operation and return invalidated stages."""
    current = copy.deepcopy(document["current"])
    op_type = operation.get("type")
    invalidated: set[str] = set()

    if op_type == "update_frame":
        fields = operation.get("fields") or {}
        unknown = set(fields) - set(FRAME_REQUIRED)
        if unknown:
            raise ResearchCaseError("VALIDATION_FAILED", f"Unknown Frame fields: {sorted(unknown)}")
        semantic_changed = any(
            field in FRAME_SEMANTIC and current["frame"].get(field) != value
            for field, value in fields.items()
        )
        current["frame"].update(copy.deepcopy(fields))
        validate_frame(current["frame"])
        if semantic_changed:
            invalidated.update(("criteria", "evidence", "challenge"))

    elif op_type == "freeze_criteria":
        criteria = copy.deepcopy(operation.get("criteria") or [])
        validate_criteria(criteria)
        current["criteria"] = criteria
        current["criteria_frozen_version"] = int(current.get("criteria_frozen_version", 0)) + 1
        current["stale_stages"] = [
            stage for stage in current.get("stale_stages", []) if stage != "criteria"
        ]
        invalidated.update(("evidence", "challenge"))

    elif op_type == "set_claims":
        if not current.get("criteria_frozen_version"):
            raise ResearchCaseError("INVALID_TRANSITION", "Freeze Criteria before adding Evidence.")
        claims = copy.deepcopy(operation.get("claims") or [])
        criterion_ids = {item["criterion_id"] for item in current["criteria"]}
        validate_claims(claims, criterion_ids)
        if claims != current.get("claims", []):
            invalidated.add("challenge")
        current["claims"] = claims
        current["stale_stages"] = [
            stage for stage in current.get("stale_stages", []) if stage != "evidence"
        ]

    elif op_type == "set_challenges":
        challenges = copy.deepcopy(operation.get("challenges") or [])
        claim_ids = {item["claim_id"] for item in current.get("claims", [])}
        validate_challenges(challenges, claim_ids)
        current["challenges"] = challenges
        current["stale_stages"] = [
            stage for stage in current.get("stale_stages", []) if stage != "challenge"
        ]

    elif op_type == "add_blocker":
        blocker = copy.deepcopy(operation.get("blocker") or {})
        _validate_entity_id(blocker.get("blocker_id", ""), "blocker")
        if blocker.get("stage") not in STAGES:
            raise ResearchCaseError("VALIDATION_FAILED", "Blocker stage is invalid.")
        for field in ("description", "owner", "created_at"):
            _validate_text(blocker.get(field), f"blocker.{field}", 2_000)
        if any(b.get("blocker_id") == blocker["blocker_id"] for b in current["blockers"]):
            raise ResearchCaseError("VALIDATION_FAILED", "Duplicate blocker ID.")
        current["blockers"].append(blocker)

    elif op_type == "resolve_blocker":
        blocker_id = operation.get("blocker_id", "")
        resolved_at = operation.get("resolved_at") or utc_now()
        for blocker in current["blockers"]:
            if blocker.get("blocker_id") == blocker_id:
                blocker["resolved_at"] = resolved_at
                break
        else:
            raise ResearchCaseError("VALIDATION_FAILED", f"Unknown blocker: {blocker_id}")

    elif op_type == "attach_legacy":
        attachment = copy.deepcopy(operation.get("attachment") or {})
        _validate_text(attachment.get("attachment_id"), "attachment_id", 200)
        _validate_text(attachment.get("relative_path"), "legacy.relative_path", 2_000)
        _validate_text(attachment.get("sha256"), "legacy.sha256", 100)
        _validate_text(attachment.get("imported_at"), "legacy.imported_at", 200)
        relative_path = PurePosixPath(attachment["relative_path"])
        if relative_path.is_absolute() or ".." in relative_path.parts:
            raise ResearchCaseError(
                "PATH_OUTSIDE_ROOT",
                "Legacy attachment paths must be repository-relative.",
            )
        if len(attachment["sha256"]) != 64:
            raise ResearchCaseError("VALIDATION_FAILED", "Legacy SHA-256 must be 64 characters.")
        attachment["status"] = "legacy_unreviewed"
        if any(
            item.get("attachment_id") == attachment["attachment_id"]
            for item in current["legacy_attachments"]
        ):
            return current, []
        current["legacy_attachments"].append(attachment)

    else:
        raise ResearchCaseError("INVALID_TRANSITION", f"Unsupported operation: {op_type!r}")

    stale = set(current.get("stale_stages") or [])
    stale.update(invalidated)
    current["stale_stages"] = [stage for stage in STAGES if stage in stale]
    validate_current(current)
    return current, sorted(invalidated)
