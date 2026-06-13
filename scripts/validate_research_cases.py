#!/usr/bin/env python3
"""Validate persisted Research Cases and their referenced local artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from research_cases import (
    SCHEMA_VERSION,
    ResearchCaseError,
    content_hash,
    derive_stage_states,
    validate_case_id,
    validate_current,
)


def _issue(code: str, message: str, **details: Any) -> dict[str, Any]:
    return {"code": code, "message": message, **details}


def _validate_reference(
    vault_root: Path,
    reference: dict,
    reference_type: str,
) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []
    relative_path = reference.get("relative_path")
    if not isinstance(relative_path, str) or not relative_path:
        return [_issue("REFERENCE_PATH_MISSING", f"{reference_type} has no relative_path.")]

    root = vault_root.resolve()
    path = (root / relative_path).resolve()
    try:
        path.relative_to(root)
    except ValueError:
        return [
            _issue(
                "PATH_OUTSIDE_ROOT",
                f"{reference_type} path escapes the vault root.",
                relative_path=relative_path,
            )
        ]

    if not path.is_file():
        return [
            _issue(
                "REFERENCE_MISSING",
                f"{reference_type} file does not exist.",
                relative_path=relative_path,
            )
        ]

    expected_hash = reference.get("sha256")
    if not isinstance(expected_hash, str) or len(expected_hash) != 64:
        issues.append(
            _issue(
                "REFERENCE_HASH_INVALID",
                f"{reference_type} has an invalid SHA-256.",
                relative_path=relative_path,
            )
        )
        return issues

    actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual_hash != expected_hash:
        issues.append(
            _issue(
                "REFERENCE_CHANGED",
                f"{reference_type} content no longer matches its recorded SHA-256.",
                relative_path=relative_path,
                expected_sha256=expected_hash,
                actual_sha256=actual_hash,
            )
        )
    return issues


def validate_case_document(
    document: dict,
    path: Path,
    vault_root: Path,
) -> dict[str, Any]:
    """Return a validation report for one persisted case document."""
    issues: list[dict[str, Any]] = []
    case_id = document.get("case_id", path.stem)

    try:
        validate_case_id(case_id)
    except ResearchCaseError as exc:
        issues.append(_issue(exc.code, str(exc)))
    if case_id != path.stem:
        issues.append(
            _issue(
                "CASE_ID_PATH_MISMATCH",
                "case_id does not match the JSON filename.",
                case_id=case_id,
                filename=path.name,
            )
        )
    if document.get("schema_version") != SCHEMA_VERSION:
        issues.append(
            _issue(
                "SCHEMA_UNSUPPORTED",
                "Persisted case does not use the current schema version.",
                schema_version=document.get("schema_version"),
            )
        )

    current = document.get("current")
    if not isinstance(current, dict):
        issues.append(_issue("CURRENT_MISSING", "Case current projection is missing."))
        current = {}
    else:
        try:
            validate_current(current)
        except ResearchCaseError as exc:
            issues.append(_issue(exc.code, str(exc), details=exc.details))

    revision = document.get("revision")
    revisions = document.get("revisions")
    events = document.get("events")
    if not isinstance(revision, int) or revision < 1:
        issues.append(_issue("REVISION_INVALID", "Case revision must be a positive integer."))
        revision = 0
    if not isinstance(revisions, list):
        issues.append(_issue("REVISION_HISTORY_MISSING", "Revision history must be a list."))
        revisions = []
    if not isinstance(events, list):
        issues.append(_issue("EVENT_HISTORY_MISSING", "Event history must be a list."))
        events = []

    expected_numbers = list(range(1, revision + 1))
    revision_numbers = [item.get("revision") for item in revisions if isinstance(item, dict)]
    event_numbers = [item.get("revision") for item in events if isinstance(item, dict)]
    if revision_numbers != expected_numbers:
        issues.append(
            _issue(
                "REVISION_HISTORY_NON_MONOTONIC",
                "Revision history must contain each revision exactly once in order.",
                observed=revision_numbers,
                expected=expected_numbers,
            )
        )
    if event_numbers != expected_numbers:
        issues.append(
            _issue(
                "EVENT_HISTORY_NON_MONOTONIC",
                "Event history must contain each revision exactly once in order.",
                observed=event_numbers,
                expected=expected_numbers,
            )
        )

    operation_ids = [
        item.get("operation_id")
        for item in events
        if isinstance(item, dict) and item.get("operation_id")
    ]
    if len(operation_ids) != len(set(operation_ids)):
        issues.append(_issue("DUPLICATE_OPERATION_ID", "Event operation IDs must be unique."))

    for item in revisions:
        if not isinstance(item, dict):
            issues.append(_issue("REVISION_ENTRY_INVALID", "Revision entry must be an object."))
            continue
        snapshot = item.get("snapshot")
        recorded_hash = item.get("content_hash")
        if not isinstance(snapshot, dict) or content_hash(snapshot) != recorded_hash:
            issues.append(
                _issue(
                    "REVISION_HASH_MISMATCH",
                    "Revision snapshot does not match its recorded content hash.",
                    revision=item.get("revision"),
                )
            )

    if revisions and isinstance(revisions[-1], dict):
        if revisions[-1].get("snapshot") != current:
            issues.append(
                _issue(
                    "CURRENT_NOT_LATEST",
                    "Current projection does not match the latest revision snapshot.",
                )
            )

    for attachment in current.get("legacy_attachments", []):
        if isinstance(attachment, dict):
            issues.extend(_validate_reference(vault_root, attachment, "Legacy attachment"))
    for claim in current.get("claims", []):
        if not isinstance(claim, dict):
            continue
        for evidence in claim.get("evidence", []):
            if isinstance(evidence, dict):
                issues.extend(_validate_reference(vault_root, evidence, "Evidence attachment"))

    return {
        "case_id": case_id,
        "path": path.relative_to(vault_root).as_posix(),
        "valid": not issues,
        "issues": issues,
        "stage_states": derive_stage_states(current) if current else {},
    }


def validate_case_corpus(vault_root: Path) -> dict[str, Any]:
    case_root = vault_root / "system" / "research-cases"
    reports: list[dict[str, Any]] = []
    if case_root.exists():
        for path in sorted(case_root.glob("case-*.json")):
            try:
                document = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
                reports.append(
                    {
                        "case_id": path.stem,
                        "path": path.relative_to(vault_root).as_posix(),
                        "valid": False,
                        "issues": [_issue("CORRUPT_CASE", str(exc))],
                        "stage_states": {},
                    }
                )
                continue
            if not isinstance(document, dict):
                reports.append(
                    {
                        "case_id": path.stem,
                        "path": path.relative_to(vault_root).as_posix(),
                        "valid": False,
                        "issues": [_issue("CORRUPT_CASE", "Case root must be an object.")],
                        "stage_states": {},
                    }
                )
                continue
            reports.append(validate_case_document(document, path, vault_root))

    issue_count = sum(len(report["issues"]) for report in reports)
    return {
        "case_count": len(reports),
        "valid_case_count": sum(1 for report in reports if report["valid"]),
        "issue_count": issue_count,
        "valid": issue_count == 0 and bool(reports),
        "cases": reports,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Vault root containing system/research-cases.",
    )
    parser.add_argument("--json", action="store_true", help="Print the full report as JSON.")
    args = parser.parse_args()

    root = args.root.resolve()
    report = validate_case_corpus(root)
    if args.json:
        print(json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True))
    else:
        print(
            f"Research Cases: {report['valid_case_count']}/{report['case_count']} valid; "
            f"{report['issue_count']} issue(s)"
        )
        for case in report["cases"]:
            states = ", ".join(
                f"{stage}={state['progress']}/{state['freshness']}"
                for stage, state in case["stage_states"].items()
            )
            print(f"- {case['case_id']}: {'PASS' if case['valid'] else 'FAIL'}")
            if states:
                print(f"  {states}")
            for issue in case["issues"]:
                print(f"  {issue['code']}: {issue['message']}")
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
