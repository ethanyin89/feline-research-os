#!/usr/bin/env python3
"""Regression tests for the result presentation contract and static adapters."""

from __future__ import annotations

import tempfile
from pathlib import Path

from core.result_presentation import (
    build_evidence_profile,
    build_next_actions,
    build_result_presentation,
    build_source_display,
    render_user_facing_provenance,
)
from core.source_metadata import load_source_metadata
from core.static_result_adapter import (
    build_overview_presentation,
    build_ranked_presentation,
)
from core.static_result_renderer import (
    render_overview,
    render_ranked,
    validate_visible_html,
)


ROOT = Path(__file__).parent.parent


def test_source_counts_are_distinct_from_claim_counts() -> None:
    profile = build_evidence_profile(
        [
            {"source_id": "one", "verification_status": "deep_extracted"},
            {"source_id": "two", "verification_status": "abstract_weighted"},
            {"source_id": "two", "verification_status": "abstract_weighted"},
        ],
        [{"provenance": "source_supported_conclusion"} for _ in range(7)],
    )
    assert profile.source_count == 2
    assert profile.supported_synthesis_count == 7
    assert profile.get_summary_text().startswith("基于 2 篇来源")


def test_unknown_status_is_not_promoted() -> None:
    profile = build_evidence_profile(
        [{"source_id": "one", "verification_status": "mystery"}],
        [],
    )
    assert profile.unknown_source_count == 1
    assert profile.abstract_weighted_count == 0


def test_source_display_uses_safe_url_fallback() -> None:
    card = build_source_display({
        "source_id": "one",
        "title": "Source",
        "verification_status": "source_checked",
        "url": "https://example.com/paper",
    })
    assert card.canonical_url == "https://example.com/paper"

    unsafe = build_source_display({
        "source_id": "two",
        "title": "Unsafe",
        "verification_status": "source_checked",
        "url": "javascript:alert(1)",
    })
    assert unsafe.canonical_url is None


def test_source_display_includes_optional_metadata() -> None:
    card = build_source_display({
        "source_id": "src-ckd-001",
        "title": "Readable source title",
        "verification_status": "deep_extracted",
        "source_kind": "paper",
        "evidence_level": "review",
        "species": "feline",
        "decision_grade": "provisional",
        "authors": ["A One", "B Two"],
        "journal": "Journal of Feline Medicine and Surgery",
        "pmcid": "PMC1234567",
        "tags": ["ckd", "review"],
    })
    assert card.source_family_label == "论文"
    assert card.species_label == "猫科 (feline)"
    assert card.decision_grade_label == "暂定决策级 (provisional)"
    assert card.safest_use == "分支图谱/证据综合 (branch map / synthesis)"
    assert card.must_not_control == "单一研究决定性主张 (single-study winner claims)"
    assert card.journal == "Journal of Feline Medicine and Surgery"
    assert card.pmcid == "PMC1234567"
    assert card.authors == ["A One", "B Two"]
    assert card.tags == ["ckd", "review"]
    assert card.canonical_url == "https://pmc.ncbi.nlm.nih.gov/articles/PMC1234567/"


def test_source_display_keeps_evidence_snippets() -> None:
    card = build_source_display({
        "source_id": "src-diabetes-025",
        "title": "Feline Diabetes Is Associated with Deficits",
        "verification_status": "deep_extracted",
        "quoted_facts": ["54 client-owned cats: lean, overweight, diabetic."],
        "supported_conclusions": ["Feline diabetes involves tissue-level insulin signaling deficits."],
        "llm_inferences": ["GLUT-4 may be a therapeutic target."],
    })
    assert card.quoted_facts == ["54 client-owned cats: lean, overweight, diabetic."]
    assert card.supported_conclusions[0].startswith("Feline diabetes")


def test_missing_source_metadata_is_explicit() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        metadata = load_source_metadata(Path(tmp), ["src-missing-001"])
    assert metadata[0]["verification_status"] == "metadata_unavailable"


def test_user_facing_provenance_uses_titles_not_ids() -> None:
    card = build_source_display({
        "source_id": "src-ckd-001",
        "title": "Readable source title",
        "verification_status": "deep_extracted",
        "doi": "10.1000/example",
    })
    source = "[source_supported_conclusion: src-ckd-001] [llm_inference]"
    rendered = render_user_facing_provenance(source, [card], html_output=False)
    assert "Readable source title" in rendered
    assert "来源支持" in rendered
    assert "分析推断" in rendered
    assert "src-ckd-001" not in rendered
    assert "source_supported_conclusion" not in rendered


def test_result_presentation_builds_claim_level_traces() -> None:
    presentation = build_result_presentation(
        title="研究回答",
        subtitle="基于 1 篇来源",
        lead="猫糖尿病模型评价应纳入组织机制指标。[quoted_fact: src-diabetes-025]",
        sources=[{
            "source_id": "src-diabetes-025",
            "title": "Feline Diabetes Is Associated with Deficits",
            "verification_status": "deep_extracted",
            "doi": "10.3390/ijms252313195",
            "quoted_facts": ["54 client-owned cats: lean (n=15), overweight (n=15), diabetic (n=24)."],
        }],
        claims=[{"provenance": "quoted_fact"}],
    )
    assert presentation.evidence_traces
    trace = presentation.evidence_traces[0]
    assert trace.evidence_label == "直接来源"
    assert trace.source_title == "Feline Diabetes Is Associated with Deficits"
    assert trace.highlight_text in trace.quoted_passage
    assert "src-diabetes-025" not in trace.claim_text
    assert presentation.validate() == []


def test_source_metadata_loads_block_abstract_and_evidence_policy() -> None:
    metadata = load_source_metadata(ROOT, ["src-diabetes-035"])[0]
    assert "The SENSATION study was a prospective" in metadata["abstract_text"]
    assert metadata["quoted_facts"]
    assert "252 client-owned diabetic cats" in metadata["quoted_facts"][0]


def test_homepage_copy_is_minimal_input_focused() -> None:
    """Homepage should be a 'research question input box', not a 'system intro page'."""
    app_text = (ROOT / "scripts/app.py").read_text(encoding="utf-8")
    # New minimal title
    assert "今天想研究什么？" in app_text
    # Old verbose titles should not appear
    assert "<h1>从一个研究问题开始</h1>" not in app_text
    assert "<h1>证据研究工作台</h1>" not in app_text
    # Homepage should not render these panels (moved to sidebar or removed)
    assert "render_briefing_entry_cards()" not in app_text.split("def render_empty_state")[1].split("def ")[0]
    assert "render_provenance_guide()" not in app_text.split("def render_empty_state")[1].split("def ")[0]
    assert "render_how_it_works()" not in app_text.split("def render_empty_state")[1].split("def ")[0]


def test_next_actions_use_user_facing_topic_labels() -> None:
    actions = build_next_actions("ckd", surface_type="vault")
    labels = [action.label for action in actions]
    targets = [action.target for action in actions]
    assert "深入了解CKD的机制" in labels
    assert "深入了解ckd的机制" not in labels
    assert "猫 CKD 病理生理机制" in targets


def test_next_actions_normalize_composite_topic_labels() -> None:
    actions = build_next_actions("feline ckd", surface_type="vault")
    labels = [action.label for action in actions]
    targets = [action.target for action in actions]
    assert "深入了解CKD的机制" in labels
    assert "猫 CKD 病理生理机制" in targets


def test_overview_fixture_renders_without_internal_tokens() -> None:
    presentation = build_overview_presentation(
        ROOT / "topics/ckd/what-is-ckd.md",
        ROOT,
    )
    document = render_overview(presentation)
    assert validate_visible_html(document) == []
    assert "什么是猫慢性肾病？" in document
    assert "Feline CKD: Current therapies" in document


def test_ranked_fixture_has_complete_boundaries() -> None:
    presentation = build_ranked_presentation(
        ROOT / "system/indexes/ckd-treatment-ranking-memo.md",
        ROOT,
    )
    assert presentation.validate() == []
    assert [tier.rank for tier in presentation.tiers] == [1, 2, 3, 4]
    assert all(
        item.supported_use and item.overclaim_boundary
        for tier in presentation.tiers
        for item in tier.interventions
    )
    document = render_ranked(presentation)
    assert validate_visible_html(document) == []


if __name__ == "__main__":
    tests = [
        test_source_counts_are_distinct_from_claim_counts,
        test_unknown_status_is_not_promoted,
        test_source_display_uses_safe_url_fallback,
        test_source_display_includes_optional_metadata,
        test_source_display_keeps_evidence_snippets,
        test_missing_source_metadata_is_explicit,
        test_user_facing_provenance_uses_titles_not_ids,
        test_result_presentation_builds_claim_level_traces,
        test_source_metadata_loads_block_abstract_and_evidence_policy,
        test_homepage_copy_is_minimal_input_focused,
        test_next_actions_use_user_facing_topic_labels,
        test_next_actions_normalize_composite_topic_labels,
        test_overview_fixture_renders_without_internal_tokens,
        test_ranked_fixture_has_complete_boundaries,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
