#!/usr/bin/env python3
"""Domain and persistence tests for the Research Case kernel."""

from __future__ import annotations

import json
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from unittest.mock import patch

from research_case_store import ResearchCaseStore
from research_cases import ResearchCaseError, apply_operation, derive_stage_states, new_case
from validate_research_cases import validate_case_corpus


FRAME = {
    "question": "Does phosphorus control merit further CKD research?",
    "scope": "Feline CKD evidence in the local vault",
    "alternatives": ["advance evidence review", "do not advance"],
    "asset": "phosphorus-control program",
    "indication": "feline CKD",
    "jurisdiction": "research only",
    "owner": "Jiawei",
    "reviewer": "Reviewer A",
    "deadline": "2026-06-30",
}

CRITERIA = [
    {
        "criterion_id": "criterion-efficacy",
        "name": "Outcome relevance",
        "threshold": "At least one reviewed outcome signal",
        "applicability": "Feline CKD",
        "required": True,
        "owner": "Jiawei",
        "rationale": "Required for translational relevance",
    }
]

CLAIMS = [
    {
        "claim_id": "claim-phosphorus-outcome",
        "text": "Phosphorus control has an outcome-relevant evidence signal.",
        "criterion_ids": ["criterion-efficacy"],
        "reviewed_disposition": "uncertain",
        "explicit_gap": False,
        "evidence": [
            {
                "evidence_id": "evidence-ckd-001",
                "source_id": "src-ckd-001",
                "relative_path": "raw/papers/src-ckd-001.md",
                "sha256": "a" * 64,
                "observed_at": "2026-06-07T00:00:00+00:00",
                "polarity": "mixed",
            }
        ],
    }
]

CHALLENGES = [
    {
        "challenge_id": "challenge-phosphorus-outcome",
        "claim_id": "claim-phosphorus-outcome",
        "counterclaim": "The outcome signal may not establish disease modification.",
        "reviewer": "Reviewer A",
        "disposition": "unresolved",
        "rationale": "Endpoint and applicability boundaries remain open.",
    }
]


def expect_error(code: str, fn) -> ResearchCaseError:
    try:
        fn()
    except ResearchCaseError as exc:
        assert exc.code == code, f"Expected {code}, got {exc.code}: {exc}"
        return exc
    raise AssertionError(f"Expected ResearchCaseError {code}")


def make_store(tmp: str) -> ResearchCaseStore:
    return ResearchCaseStore(Path(tmp) / "cases")


def create_case(store: ResearchCaseStore) -> dict:
    return store.create(
        "case-ckd-phosphorus",
        FRAME,
        "Jiawei",
        now="2026-06-07T00:00:00+00:00",
    )


def test_validation_and_initial_revision() -> None:
    expect_error("VALIDATION_FAILED", lambda: new_case("../escape", FRAME, "Jiawei"))
    expect_error(
        "VALIDATION_FAILED",
        lambda: new_case("case-invalid-frame", {**FRAME, "alternatives": ["one"]}, "Jiawei"),
    )
    with tempfile.TemporaryDirectory() as tmp:
        case = create_case(make_store(tmp))
        assert case["revision"] == 1
        assert case["revisions"][0]["identity_assurance"] == "self_asserted"
        assert case["revisions"][0]["content_hash"]
        states = derive_stage_states(case["current"])
        assert states["frame"] == {"progress": "complete", "freshness": "current"}
        assert states["criteria"]["progress"] == "not_started"


def test_semantic_and_administrative_frame_invalidation() -> None:
    document = new_case("case-frame-test", FRAME, "Jiawei")
    admin, invalidated = apply_operation(
        document,
        {"type": "update_frame", "fields": {"deadline": "2026-07-15"}},
    )
    assert invalidated == []
    assert admin["stale_stages"] == []

    semantic, invalidated = apply_operation(
        document,
        {"type": "update_frame", "fields": {"scope": "Expanded CKD evidence scope"}},
    )
    assert invalidated == ["challenge", "criteria", "evidence"]
    assert semantic["stale_stages"] == ["criteria", "evidence", "challenge"]


def test_transition_order_and_derived_completion() -> None:
    document = new_case("case-transition-test", FRAME, "Jiawei")
    expect_error(
        "INVALID_TRANSITION",
        lambda: apply_operation(document, {"type": "set_claims", "claims": CLAIMS}),
    )

    criteria_current, invalidated = apply_operation(
        document,
        {"type": "freeze_criteria", "criteria": CRITERIA},
    )
    document["current"] = criteria_current
    assert invalidated == ["challenge", "evidence"]
    assert derive_stage_states(criteria_current)["criteria"]["progress"] == "complete"
    assert derive_stage_states(criteria_current)["criteria"]["freshness"] == "current"

    claims_current, invalidated = apply_operation(
        document,
        {"type": "set_claims", "claims": CLAIMS},
    )
    document["current"] = claims_current
    assert invalidated == ["challenge"]
    states = derive_stage_states(claims_current)
    assert states["evidence"]["progress"] == "complete"
    assert states["evidence"]["freshness"] == "current"
    assert states["challenge"]["freshness"] == "stale"

    challenge_current, invalidated = apply_operation(
        document,
        {"type": "set_challenges", "challenges": CHALLENGES},
    )
    assert invalidated == []
    states = derive_stage_states(challenge_current)
    assert states["challenge"] == {"progress": "complete", "freshness": "current"}


def test_blocked_and_stale_can_coexist() -> None:
    document = new_case("case-blocker-test", FRAME, "Jiawei")
    current, _ = apply_operation(
        document,
        {
            "type": "add_blocker",
            "blocker": {
                "blocker_id": "blocker-source-access",
                "stage": "evidence",
                "description": "Full text unavailable",
                "owner": "Jiawei",
                "created_at": "2026-06-07T00:00:00+00:00",
            },
        },
    )
    current["stale_stages"] = ["evidence"]
    assert derive_stage_states(current)["evidence"] == {
        "progress": "blocked",
        "freshness": "stale",
    }


def test_atomic_store_history_idempotency_and_conflict() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        store = make_store(tmp)
        created = create_case(store)
        updated = store.update(
            created["case_id"],
            expected_revision=1,
            actor_label="Jiawei",
            reason="Update deadline",
            operation_id="op-deadline",
            operation={"type": "update_frame", "fields": {"deadline": "2026-07-15"}},
            now="2026-06-07T00:01:00+00:00",
        )
        assert updated["revision"] == 2
        assert len(updated["revisions"]) == 2
        assert len(updated["events"]) == 2

        repeated = store.update(
            created["case_id"],
            expected_revision=1,
            actor_label="Jiawei",
            reason="Update deadline",
            operation_id="op-deadline",
            operation={"type": "update_frame", "fields": {"deadline": "2026-07-15"}},
        )
        assert repeated["revision"] == 2
        expect_error(
            "CASE_VERSION_CONFLICT",
            lambda: store.update(
                created["case_id"],
                expected_revision=1,
                actor_label="Jiawei",
                reason="Stale edit",
                operation_id="op-stale",
                operation={"type": "update_frame", "fields": {"owner": "Other"}},
            ),
        )


def test_concurrent_same_revision_has_one_winner() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        store = make_store(tmp)
        created = create_case(store)

        def update(owner: str, operation_id: str):
            try:
                result = store.update(
                    created["case_id"],
                    expected_revision=1,
                    actor_label=owner,
                    reason="Concurrent owner update",
                    operation_id=operation_id,
                    operation={"type": "update_frame", "fields": {"owner": owner}},
                )
                return ("ok", result["revision"])
            except ResearchCaseError as exc:
                return (exc.code, None)

        with ThreadPoolExecutor(max_workers=2) as executor:
            results = list(
                executor.map(
                    lambda args: update(*args),
                    [("Owner A", "op-a"), ("Owner B", "op-b")],
                )
            )
        assert sorted(status for status, _ in results) == ["CASE_VERSION_CONFLICT", "ok"]
        assert store.load(created["case_id"])["revision"] == 2


def test_corrupt_future_schema_and_read_only_fail_closed() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "cases"
        root.mkdir()
        store = ResearchCaseStore(root)

        (root / "case-corrupt.json").write_text("{broken", encoding="utf-8")
        expect_error("CORRUPT_CASE", lambda: store.load("case-corrupt"))

        future = new_case("case-future", FRAME, "Jiawei")
        future["schema_version"] = 99
        (root / "case-future.json").write_text(json.dumps(future), encoding="utf-8")
        expect_error("SCHEMA_UNSUPPORTED", lambda: store.load("case-future"))

        read_only = ResearchCaseStore(root, write_enabled=False)
        expect_error(
            "WRITE_MODE_DISABLED",
            lambda: read_only.create("case-read-only", FRAME, "Jiawei"),
        )


def test_invalid_evidence_path_is_rejected() -> None:
    document = new_case("case-path-test", FRAME, "Jiawei")
    criteria_current, _ = apply_operation(
        document,
        {"type": "freeze_criteria", "criteria": CRITERIA},
    )
    document["current"] = criteria_current
    unsafe_claims = json.loads(json.dumps(CLAIMS))
    unsafe_claims[0]["evidence"][0]["relative_path"] = "../../etc/passwd"
    expect_error(
        "PATH_OUTSIDE_ROOT",
        lambda: apply_operation(document, {"type": "set_claims", "claims": unsafe_claims}),
    )


def test_legacy_attachment_is_unreviewed_and_grants_no_gate_credit() -> None:
    document = new_case("case-legacy-test", FRAME, "Jiawei")
    current, invalidated = apply_operation(
        document,
        {
            "type": "attach_legacy",
            "attachment": {
                "attachment_id": "legacy-brief",
                "relative_path": "outputs/business/legacy.md",
                "sha256": "b" * 64,
                "imported_at": "2026-06-07T00:00:00+00:00",
            },
        },
    )
    assert invalidated == []
    assert current["legacy_attachments"][0]["status"] == "legacy_unreviewed"
    states = derive_stage_states(current)
    assert states["criteria"]["progress"] == "not_started"
    assert states["evidence"]["progress"] == "not_started"


def test_failed_atomic_replace_preserves_previous_revision() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        store = make_store(tmp)
        created = create_case(store)
        path = Path(tmp) / "cases" / f"{created['case_id']}.json"
        before = path.read_bytes()

        with patch("research_case_store.os.replace", side_effect=OSError("simulated replace failure")):
            expect_error(
                "WRITE_FAILED",
                lambda: store.update(
                    created["case_id"],
                    expected_revision=1,
                    actor_label="Jiawei",
                    reason="Simulate failed write",
                    operation_id="op-failed-write",
                    operation={"type": "update_frame", "fields": {"owner": "Changed"}},
                ),
            )

        assert path.read_bytes() == before
        assert store.load(created["case_id"])["revision"] == 1


def test_schema_zero_migrates_on_update_with_backup() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "cases"
        root.mkdir()
        document = new_case("case-migrate", FRAME, "Jiawei")
        document["schema_version"] = 0
        document.pop("status")
        document["current"].pop("stale_stages")
        path = root / "case-migrate.json"
        path.write_text(json.dumps(document), encoding="utf-8")

        store = ResearchCaseStore(root)
        updated = store.update(
            "case-migrate",
            expected_revision=0,
            actor_label="Jiawei",
            reason="Migrate and update",
            operation_id="op-migrate",
            operation={"type": "update_frame", "fields": {"deadline": "2026-07-01"}},
        )
        assert updated["schema_version"] == 1
        assert updated["revision"] == 1
        assert (root / "case-migrate.schema-0.bak").exists()


def test_persisted_case_corpus_integrity() -> None:
    root = Path(__file__).resolve().parents[1]
    report = validate_case_corpus(root)
    assert report["case_count"] >= 1
    assert report["valid"], report["cases"]
    ckd_case = next(
        item
        for item in report["cases"]
        if item["case_id"] == "case-ckd-phosphorus-control"
    )
    assert ckd_case["stage_states"]["frame"]["progress"] == "complete"
    assert ckd_case["stage_states"]["criteria"]["progress"] == "blocked"
    assert ckd_case["stage_states"]["evidence"]["progress"] == "not_started"
    assert ckd_case["stage_states"]["challenge"]["progress"] == "not_started"


if __name__ == "__main__":
    tests = [
        test_validation_and_initial_revision,
        test_semantic_and_administrative_frame_invalidation,
        test_transition_order_and_derived_completion,
        test_blocked_and_stale_can_coexist,
        test_atomic_store_history_idempotency_and_conflict,
        test_concurrent_same_revision_has_one_winner,
        test_corrupt_future_schema_and_read_only_fail_closed,
        test_invalid_evidence_path_is_rejected,
        test_legacy_attachment_is_unreviewed_and_grants_no_gate_credit,
        test_failed_atomic_replace_preserves_previous_revision,
        test_schema_zero_migrates_on_update_with_backup,
        test_persisted_case_corpus_integrity,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
