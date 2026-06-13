#!/usr/bin/env python3
"""Regression tests for Cut 0 authority containment."""

from __future__ import annotations

import tempfile
from pathlib import Path

from business_value_eval import evaluate_claim_card, evaluate_opportunity_brief
from claim_evidence import evaluate_claim, format_claim_card_markdown
from opportunity_brief import format_brief_markdown, generate_opportunity_brief
from source_inventory import format_source_inventory, get_source_inventory


ROOT = Path(__file__).parent.parent


def test_primary_ui_has_no_automatic_decision_actions() -> None:
    app = (ROOT / "scripts" / "app.py").read_text(encoding="utf-8")
    forbidden = (
        'st.button("Opportunity Brief"',
        'st.button("Endpoint Memo"',
        'st.button("Verify Claim"',
        "Decision Dashboard",
        'branch="general"',
    )
    for text in forbidden:
        assert text not in app, f"Unsafe primary UI action remains: {text}"


def test_claim_matcher_is_candidate_only() -> None:
    positive = evaluate_claim("ckd", "SDMA supports early CKD detection")
    negative = evaluate_claim("ckd", "SDMA does not support early CKD detection")

    allowed = {"candidate_matches_found", "no_candidate_matches"}
    assert positive.verdict in allowed
    assert negative.verdict in allowed
    assert positive.verdict_confidence == "not_assessed"
    assert negative.verdict_confidence == "not_assessed"
    assert positive.next_action in {"human_review", "search_more"}
    assert negative.next_action in {"human_review", "search_more"}

    rendered = format_claim_card_markdown(positive)
    lowered = rendered.lower()
    assert "candidate retrieval only" in lowered
    assert "semantic confidence" in lowered
    assert "| promote |" not in lowered
    assert "| kill |" not in lowered

    evaluation = evaluate_claim_card(rendered, "candidate.md")
    assert evaluation.passed, evaluation.errors


def test_general_and_implicit_opportunity_briefs_are_disabled() -> None:
    try:
        generate_opportunity_brief("ckd", "general", ["Explicit claim"])
    except ValueError as exc:
        assert "general" in str(exc).lower()
    else:
        raise AssertionError("The legacy general branch must be rejected")

    try:
        generate_opportunity_brief("ckd", "phosphorus control")
    except ValueError as exc:
        assert "explicit claims" in str(exc).lower()
    else:
        raise AssertionError("Automatic claim generation must be rejected")


def test_explicit_legacy_brief_disables_automatic_decision() -> None:
    brief = generate_opportunity_brief(
        "ckd",
        "phosphorus control",
        ["Phosphorus control is relevant to feline CKD management"],
    )
    rendered = format_brief_markdown(brief)
    lowered = rendered.lower()

    assert "unreviewed legacy output" in lowered
    assert "automated decision disabled" in lowered
    assert "**conditional go**" not in lowered
    assert "**no go" not in lowered
    assert "**hold" not in lowered

    evaluation = evaluate_opportunity_brief(rendered, "legacy-brief.md")
    assert evaluation.passed, evaluation.errors


def test_source_inventory_is_computed_from_files() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        papers = root / "raw" / "papers"
        papers.mkdir(parents=True)
        (papers / "src-ckd-001.md").write_text(
            "---\nid: src-ckd-001\nverification_status: deep_extracted\n---\n",
            encoding="utf-8",
        )
        (papers / "src-ckd-002.md").write_text(
            "---\nid: src-ckd-002\nverification_status: title_only\n---\n",
            encoding="utf-8",
        )

        inventory = get_source_inventory(root, "ckd")
        assert inventory["total"] == 2
        assert inventory["verification_status"]["deep_extracted"] == 1
        assert inventory["verification_status"]["title_only"] == 1
        label = format_source_inventory(inventory)
        assert "2 cards" in label
        assert "not a maturity or decision rating" in label


if __name__ == "__main__":
    tests = [
        test_primary_ui_has_no_automatic_decision_actions,
        test_claim_matcher_is_candidate_only,
        test_general_and_implicit_opportunity_briefs_are_disabled,
        test_explicit_legacy_brief_disables_automatic_decision,
        test_source_inventory_is_computed_from_files,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
