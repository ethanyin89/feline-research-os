"""Streamlit UI for the four-stage Research Case workspace."""

from __future__ import annotations

import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path

import streamlit as st

from research_case_store import ResearchCaseStore
from research_cases import ERROR_REGISTRY, ResearchCaseError, derive_stage_states


def _slug(value: str, fallback: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:48] or fallback


def _show_error(exc: ResearchCaseError) -> None:
    recovery = ERROR_REGISTRY.get(exc.code, ERROR_REGISTRY["UNEXPECTED_ERROR"])
    st.error(f"{exc.code}: {exc}")
    st.caption(recovery)


def _commit(
    store: ResearchCaseStore,
    case: dict,
    stage: str,
    actor: str,
    reason: str,
    operation: dict,
) -> dict | None:
    operation_id = (
        f"{case['case_id']}-{stage}-{case['revision']}-"
        f"{hashlib.sha256(repr(operation).encode()).hexdigest()[:12]}"
    )
    try:
        updated = store.update(
            case["case_id"],
            expected_revision=case["revision"],
            actor_label=actor,
            reason=reason,
            operation_id=operation_id,
            operation=operation,
        )
    except ResearchCaseError as exc:
        _show_error(exc)
        return None
    st.query_params["case"] = updated["case_id"]
    st.rerun()
    return updated


def _render_stage_status(case: dict) -> None:
    states = derive_stage_states(case["current"])
    columns = st.columns(4)
    for column, stage in zip(columns, ("frame", "criteria", "evidence", "challenge")):
        state = states[stage]
        with column:
            st.markdown(f"**{stage.title()}**")
            st.caption(f"{state['progress']} · {state['freshness']}")


def _render_case_header(case: dict) -> None:
    frame = case["current"]["frame"]
    st.markdown(f"## {case['case_id']}")
    st.markdown(frame["question"])
    st.caption(
        f"revision {case['revision']} · owner {frame['owner']} · reviewer "
        f"{frame['reviewer']} · due {frame['deadline']}"
    )
    st.info(
        "Evidence-controlled workspace. The system does not issue a final "
        "recommendation. Typed attestations use self-asserted identity."
    )
    _render_stage_status(case)


def _render_frame(store: ResearchCaseStore, case: dict) -> None:
    frame = case["current"]["frame"]
    case_id = case["case_id"]
    with st.form(f"frame-{case_id}-{case['revision']}"):
        question = st.text_area("Atomic research question", value=frame["question"], key=f"frame-question-{case_id}")
        scope = st.text_area("Scope", value=frame["scope"], key=f"frame-scope-{case_id}")
        alternatives = st.text_area(
            "Alternatives, one per line",
            value="\n".join(frame["alternatives"]),
            key=f"frame-alternatives-{case_id}"
        )
        asset = st.text_input("Asset", value=frame["asset"], key=f"frame-asset-{case_id}")
        indication = st.text_input("Indication", value=frame["indication"], key=f"frame-indication-{case_id}")
        jurisdiction = st.text_input("Jurisdiction", value=frame["jurisdiction"], key=f"frame-jurisdiction-{case_id}")
        owner = st.text_input("Owner", value=frame["owner"], key=f"frame-owner-{case_id}")
        reviewer = st.text_input("Reviewer label", value=frame["reviewer"], key=f"frame-reviewer-{case_id}")
        deadline = st.text_input("Deadline", value=frame["deadline"], key=f"frame-deadline-{case_id}")
        actor = st.text_input("Attesting actor", value=frame["owner"], key=f"frame-actor-{case_id}")
        submitted = st.form_submit_button("Save Frame")
    if submitted:
        _commit(
            store,
            case,
            "frame",
            actor,
            "Update Frame",
            {
                "type": "update_frame",
                "fields": {
                    "question": question,
                    "scope": scope,
                    "alternatives": [item.strip() for item in alternatives.splitlines() if item.strip()],
                    "asset": asset,
                    "indication": indication,
                    "jurisdiction": jurisdiction,
                    "owner": owner,
                    "reviewer": reviewer,
                    "deadline": deadline,
                },
            },
        )


def _render_criteria(store: ResearchCaseStore, case: dict) -> None:
    criteria = case["current"]["criteria"]
    case_id = case["case_id"]
    if criteria:
        st.dataframe(criteria, use_container_width=True, hide_index=True)
    with st.form(f"criteria-{case_id}-{case['revision']}"):
        name = st.text_input("Criterion name", key=f"criteria-name-{case_id}")
        threshold = st.text_area("Threshold", key=f"criteria-threshold-{case_id}")
        applicability = st.text_input("Applicability", value=case["current"]["frame"]["indication"], key=f"criteria-applicability-{case_id}")
        required = st.checkbox("Required criterion", value=True, key=f"criteria-required-{case_id}")
        owner = st.text_input("Criterion owner", value=case["current"]["frame"]["owner"], key=f"criteria-owner-{case_id}")
        rationale = st.text_area("Rationale", key=f"criteria-rationale-{case_id}")
        actor = st.text_input("Attesting actor", value=owner, key=f"criteria-actor-{case_id}")
        submitted = st.form_submit_button("Add and freeze Criteria version")
    if submitted:
        criterion_id = f"criterion-{_slug(name, 'item')}"
        replacement = [
            item for item in criteria if item.get("criterion_id") != criterion_id
        ] + [
            {
                "criterion_id": criterion_id,
                "name": name,
                "threshold": threshold,
                "applicability": applicability,
                "required": required,
                "owner": owner,
                "rationale": rationale,
            }
        ]
        _commit(
            store,
            case,
            "criteria",
            actor,
            "Freeze Criteria version",
            {"type": "freeze_criteria", "criteria": replacement},
        )


def _source_attachment(vault_root: Path, source_id: str) -> dict:
    path = (vault_root / "raw" / "papers" / f"{source_id}.md").resolve()
    approved_root = (vault_root / "raw" / "papers").resolve()
    try:
        relative = path.relative_to(vault_root.resolve())
        path.relative_to(approved_root)
    except ValueError as exc:
        raise ResearchCaseError("PATH_OUTSIDE_ROOT", "Source path is outside raw/papers.") from exc
    if not path.exists():
        raise ResearchCaseError("SOURCE_UNAVAILABLE", f"Source card not found: {source_id}")
    content = path.read_bytes()
    return {
        "relative_path": relative.as_posix(),
        "sha256": hashlib.sha256(content).hexdigest(),
        "observed_at": datetime.now(timezone.utc).isoformat(),
    }


def _render_evidence(store: ResearchCaseStore, case: dict, vault_root: Path) -> None:
    claims = case["current"]["claims"]
    criteria = case["current"]["criteria"]
    if not case["current"]["criteria_frozen_version"]:
        st.warning("Freeze at least one criterion before adding evidence.")
        return
    if claims:
        for claim in claims:
            with st.expander(f"{claim['claim_id']}: {claim['text']}", expanded=False):
                st.write(f"Disposition: {claim.get('reviewed_disposition') or 'not reviewed'}")
                st.write(f"Criteria: {', '.join(claim.get('criterion_ids', []))}")
                st.write(f"Evidence links: {len(claim.get('evidence', []))}")

    criterion_options = [item["criterion_id"] for item in criteria]
    case_id = case["case_id"]
    with st.form(f"evidence-{case_id}-{case['revision']}"):
        text = st.text_area("Atomic claim", key=f"evidence-text-{case_id}")
        linked = st.multiselect("Linked criteria", criterion_options, key=f"evidence-linked-{case_id}")
        disposition = st.selectbox(
            "Human-reviewed disposition",
            ["uncertain", "supports", "contradicts", "mixed", "irrelevant"],
            key=f"evidence-disposition-{case_id}"
        )
        explicit_gap = st.checkbox("Record as explicit evidence gap", key=f"evidence-gap-{case_id}")
        source_id = st.text_input("Source ID", placeholder="src-ckd-001", key=f"evidence-source-{case_id}")
        polarity = st.selectbox("Evidence polarity", ["support", "counter", "mixed", "context"], key=f"evidence-polarity-{case_id}")
        actor = st.text_input(
            "Attesting actor",
            value=case["current"]["frame"]["reviewer"],
            key=f"evidence-actor-{case_id}",
        )
        submitted = st.form_submit_button("Add reviewed claim evidence")
    if submitted:
        evidence = []
        if source_id.strip():
            try:
                attachment = _source_attachment(vault_root, source_id.strip())
            except ResearchCaseError as exc:
                _show_error(exc)
                return
            evidence.append(
                {
                    "evidence_id": f"evidence-{_slug(source_id, 'source')}",
                    "source_id": source_id.strip(),
                    "polarity": polarity,
                    **attachment,
                }
            )
        claim_id = f"claim-{_slug(text, 'item')}"
        replacement = [item for item in claims if item.get("claim_id") != claim_id] + [
            {
                "claim_id": claim_id,
                "text": text,
                "criterion_ids": linked,
                "reviewed_disposition": disposition,
                "explicit_gap": explicit_gap,
                "evidence": evidence,
            }
        ]
        _commit(
            store,
            case,
            "evidence",
            actor,
            "Add human-reviewed claim evidence",
            {"type": "set_claims", "claims": replacement},
        )


def _render_challenge(store: ResearchCaseStore, case: dict) -> None:
    claims = case["current"]["claims"]
    challenges = case["current"]["challenges"]
    case_id = case["case_id"]
    if not claims:
        st.warning("Add reviewed claims before Challenge.")
        return
    if challenges:
        st.dataframe(challenges, use_container_width=True, hide_index=True)
    claim_ids = [item["claim_id"] for item in claims]
    with st.form(f"challenge-{case_id}-{case['revision']}"):
        claim_id = st.selectbox("Claim", claim_ids, key=f"challenge-claim-{case_id}")
        counterclaim = st.text_area("Counterclaim or dissent", key=f"challenge-counter-{case_id}")
        disposition = st.selectbox("Challenge disposition", ["unresolved", "upheld", "revised", "rejected"], key=f"challenge-disposition-{case_id}")
        rationale = st.text_area("Rationale", key=f"challenge-rationale-{case_id}")
        reviewer = st.text_input("Reviewer label", value=case["current"]["frame"]["reviewer"], key=f"challenge-reviewer-{case_id}")
        submitted = st.form_submit_button("Record Challenge")
    if submitted:
        challenge_id = f"challenge-{_slug(claim_id, 'claim')}"
        replacement = [
            item for item in challenges if item.get("challenge_id") != challenge_id
        ] + [
            {
                "challenge_id": challenge_id,
                "claim_id": claim_id,
                "counterclaim": counterclaim,
                "reviewer": reviewer,
                "disposition": disposition,
                "rationale": rationale,
            }
        ]
        _commit(
            store,
            case,
            "challenge",
            reviewer,
            "Record Challenge disposition",
            {"type": "set_challenges", "challenges": replacement},
        )


def _render_history(case: dict) -> None:
    attachments = case["current"].get("legacy_attachments", [])
    if attachments:
        with st.expander("Unreviewed legacy attachments", expanded=False):
            for attachment in attachments:
                st.markdown(
                    f"`{attachment['attachment_id']}` · `{attachment['relative_path']}` · "
                    f"status `{attachment['status']}`"
                )
    with st.expander("Revision history", expanded=False):
        for revision in reversed(case.get("revisions", [])):
            st.markdown(
                f"`r{revision['revision']}` {revision['created_at']} · "
                f"{revision['actor_label']} · {revision['reason']}"
            )


def _render_create(store: ResearchCaseStore) -> None:
    st.markdown("## Create Research Case")
    create_case_id = "create"
    with st.form("create-research-case"):
        case_id = st.text_input("Case ID", placeholder="case-ckd-phosphorus", key=f"create-{create_case_id}-case-id")
        question = st.text_area("Atomic research question", key=f"create-{create_case_id}-question")
        scope = st.text_area("Scope", key=f"create-{create_case_id}-scope")
        alternatives = st.text_area("Alternatives, one per line", key=f"create-{create_case_id}-alternatives")
        asset = st.text_input("Asset", key=f"create-{create_case_id}-asset")
        indication = st.text_input("Indication", key=f"create-{create_case_id}-indication")
        jurisdiction = st.text_input("Jurisdiction", key=f"create-{create_case_id}-jurisdiction")
        owner = st.text_input("Owner", key=f"create-{create_case_id}-owner")
        reviewer = st.text_input("Reviewer label", key=f"create-{create_case_id}-reviewer")
        deadline = st.text_input("Deadline", placeholder="2026-06-30", key=f"create-{create_case_id}-deadline")
        submitted = st.form_submit_button("Create case")
    if submitted:
        frame = {
            "question": question,
            "scope": scope,
            "alternatives": [item.strip() for item in alternatives.splitlines() if item.strip()],
            "asset": asset,
            "indication": indication,
            "jurisdiction": jurisdiction,
            "owner": owner,
            "reviewer": reviewer,
            "deadline": deadline,
        }
        try:
            case = store.create(case_id, frame, owner)
        except ResearchCaseError as exc:
            _show_error(exc)
            return
        st.query_params["case"] = case["case_id"]
        st.rerun()


def render_research_cases(vault_root: Path) -> None:
    store = ResearchCaseStore(vault_root / "system" / "research-cases")
    st.title("Research Cases")
    st.caption("Frame -> Criteria -> Evidence -> Challenge")

    summaries = store.list_cases()
    options = ["Create new case"] + [item["case_id"] for item in summaries]
    requested = st.query_params.get("case")
    default_index = options.index(requested) if requested in options else 0
    case_id_val = "selection"
    selection = st.selectbox("Research Case", options, index=default_index, key=f"research_case_selection_{case_id_val}")
    if selection == "Create new case":
        _render_create(store)
        return

    try:
        case = store.load(selection)
    except ResearchCaseError as exc:
        _show_error(exc)
        return

    st.query_params["case"] = selection
    _render_case_header(case)
    tabs = st.tabs(["Frame", "Criteria", "Evidence", "Challenge"])
    with tabs[0]:
        _render_frame(store, case)
    with tabs[1]:
        _render_criteria(store, case)
    with tabs[2]:
        _render_evidence(store, case, vault_root)
    with tabs[3]:
        _render_challenge(store, case)
    _render_history(case)
    st.caption("Recommend and Sign are intentionally outside this release.")
