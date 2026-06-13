#!/usr/bin/env python3
"""Create the CKD phosphorus pilot shell and admit one legacy brief unreviewed."""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from pathlib import Path

from research_case_store import ResearchCaseStore
from research_cases import ResearchCaseError


ROOT = Path(__file__).parent.parent
CASE_ID = "case-ckd-phosphorus-control"
LEGACY_PATH = ROOT / "outputs" / "business" / "ckd-phosphorus-control-opportunity-brief-20260604.md"

FRAME = {
    "question": "What evidence supports, limits, or blocks further research on phosphorus control in feline CKD?",
    "scope": "Local feline CKD vault evidence and the existing phosphorus-control legacy brief",
    "alternatives": [
        "advance to structured evidence review",
        "do not advance until specified evidence gaps are resolved",
    ],
    "asset": "phosphorus-control research program",
    "indication": "feline chronic kidney disease",
    "jurisdiction": "research diligence; no automated commercial or clinical decision",
    "owner": "Jiawei",
    "reviewer": "unassigned",
    "deadline": "2026-06-30",
}


def main() -> None:
    if not LEGACY_PATH.exists():
        raise SystemExit(f"Legacy brief not found: {LEGACY_PATH}")

    store = ResearchCaseStore(ROOT / "system" / "research-cases")
    try:
        case = store.load(CASE_ID)
    except ResearchCaseError as exc:
        if exc.code != "CASE_NOT_FOUND":
            raise
        case = store.create(CASE_ID, FRAME, "migration-cli")

    relative = LEGACY_PATH.relative_to(ROOT).as_posix()
    attachment = {
        "attachment_id": "legacy-ckd-phosphorus-brief-20260604",
        "relative_path": relative,
        "sha256": hashlib.sha256(LEGACY_PATH.read_bytes()).hexdigest(),
        "imported_at": datetime.now(timezone.utc).isoformat(),
        "original_review_status": "not trusted for Research Case gate credit",
    }
    case = store.update(
        CASE_ID,
        expected_revision=case["revision"],
        actor_label="migration-cli",
        reason="Admit legacy brief as unreviewed attachment",
        operation_id="import-legacy-ckd-phosphorus-brief-20260604",
        operation={"type": "attach_legacy", "attachment": attachment},
    )
    case = store.update(
        CASE_ID,
        expected_revision=case["revision"],
        actor_label="migration-cli",
        reason="Record required human Criteria review",
        operation_id="block-ckd-phosphorus-human-criteria",
        operation={
            "type": "add_blocker",
            "blocker": {
                "blocker_id": "blocker-human-criteria-review",
                "stage": "criteria",
                "description": (
                    "A named human reviewer must define and freeze decision criteria; "
                    "legacy generator output cannot supply them."
                ),
                "owner": "Jiawei",
                "created_at": datetime.now(timezone.utc).isoformat(),
            },
        },
    )
    print(f"{CASE_ID} revision {case['revision']}")
    print(f"legacy attachment status: {case['current']['legacy_attachments'][0]['status']}")
    print("criteria blocker: blocker-human-criteria-review")


if __name__ == "__main__":
    main()
