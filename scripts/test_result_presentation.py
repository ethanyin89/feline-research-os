#!/usr/bin/env python3
"""Regression tests for the result presentation contract and static adapters."""

from __future__ import annotations

import tempfile
from pathlib import Path

from core.result_presentation import (
    build_evidence_profile,
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
    assert card.species_label == "feline"
    assert card.decision_grade_label == "provisional"
    assert card.safest_use == "branch map / synthesis"
    assert card.must_not_control == "single-study winner claims"
    assert card.journal == "Journal of Feline Medicine and Surgery"
    assert card.pmcid == "PMC1234567"
    assert card.authors == ["A One", "B Two"]
    assert card.tags == ["ckd", "review"]
    assert card.canonical_url == "https://pmc.ncbi.nlm.nih.gov/articles/PMC1234567/"


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
        test_missing_source_metadata_is_explicit,
        test_user_facing_provenance_uses_titles_not_ids,
        test_overview_fixture_renders_without_internal_tokens,
        test_ranked_fixture_has_complete_boundaries,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
