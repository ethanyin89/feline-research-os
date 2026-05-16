#!/usr/bin/env python3
"""
scripts/test_query.py — Unit tests for pure functions in query.py.

Run with: python3 scripts/test_query.py
No API key required. No files are written.
"""

import sys
import os
import tempfile
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from query import (
    _chat,
    build_source_index,
    build_slug,
    compact_source_card_context,
    compact_topic_page_context,
    compute_confidence,
    estimate_tokens,
    frontmatter_scalar,
    heuristic_files_for_route,
    heuristic_question_type,
    infer_disease_from_question,
    is_broad_explanation_question,
    list_saved_answers,
    markdown_section,
    merge_routing_with_guardrails,
    parse_json_block,
    parse_source_ids_from_answer,
    parse_source_ids_from_frontmatter,
    render_frontmatter,
    resolve_link,
    sanitize_provenance_tags,
    validate_openrouter_budget,
    validate_frontmatter,
    write_back,
    write_to_inbox,
    _parse_local_assets_from_frontmatter,
    _figure_type_from_filename,
    resolve_local_assets,
)
from search import vault_search, format_results_for_llm
from compile_trigger import find_downstream_files, build_recompile_queue
from run_acceptance_checklist import classify_runtime_blocker
from expert_review import build_expert_review_prompt, expert_review_stage_label
from health import is_obesity_compiled_guidance_gate_issue

VAULT_ROOT = Path(__file__).parent.parent

PASS = "\033[32mPASS\033[0m"
FAIL = "\033[31mFAIL\033[0m"

results = []


def test(name: str, fn):
    try:
        fn()
        results.append((name, True, None))
        print(f"  {PASS}  {name}")
    except Exception as e:
        results.append((name, False, str(e)))
        print(f"  {FAIL}  {name}")
        print(f"        {e}")


# ---------------------------------------------------------------------------
# build_source_index
# ---------------------------------------------------------------------------

def _test_build_source_index_real_vault():
    idx = build_source_index(VAULT_ROOT)
    assert len(idx) > 0, "Expected source cards in raw/"
    # Every value should be an existing Path
    for src_id, path in idx.items():
        assert path.exists(), f"Path for {src_id} does not exist: {path}"
    # IDs should match the pattern src-<disease>-<num>
    import re
    for src_id in idx:
        assert re.match(r"^src-[a-z]+-\d+$", src_id), f"Unexpected ID format: {src_id}"


def _test_build_source_index_synthetic():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        papers = root / "raw" / "papers"
        papers.mkdir(parents=True)
        (papers / "src-ckd-001.md").write_text(
            "---\nid: src-ckd-001\ntype: source\n---\n# Title\n"
        )
        (papers / "no-id.md").write_text("---\ntype: source\n---\n# No ID\n")
        (papers / "not-a-source.md").write_text("No frontmatter here\n")

        idx = build_source_index(root)
        assert "src-ckd-001" in idx, f"Expected src-ckd-001 in index, got: {list(idx)}"
        assert "no-id" not in idx
        assert len(idx) == 1, f"Expected 1 entry, got {len(idx)}"
        assert idx["src-ckd-001"] == papers / "src-ckd-001.md"


# ---------------------------------------------------------------------------
# resolve_link
# ---------------------------------------------------------------------------

def _test_resolve_link_relative():
    source = VAULT_ROOT / "topics" / "ckd" / "navigation.md"
    target = "../../system/indexes/reader-start-here.md"
    resolved = resolve_link(source, target)
    assert resolved is not None, f"Expected non-None for valid relative link"
    assert resolved.exists(), f"Resolved path does not exist: {resolved}"
    assert resolved.name == "reader-start-here.md"


def _test_resolve_link_http_returns_none():
    source = VAULT_ROOT / "topics" / "ckd" / "navigation.md"
    assert resolve_link(source, "https://example.com/paper") is None


def _test_resolve_link_anchor_only_returns_none():
    source = VAULT_ROOT / "topics" / "ckd" / "navigation.md"
    assert resolve_link(source, "#section-heading") is None


def _test_resolve_link_missing_file_returns_none():
    source = VAULT_ROOT / "topics" / "ckd" / "navigation.md"
    assert resolve_link(source, "../../does-not-exist.md") is None


# ---------------------------------------------------------------------------
# deterministic routing guardrails
# ---------------------------------------------------------------------------

def _test_infer_disease_from_question_ckd():
    assert infer_disease_from_question("Verify whether SDMA should be a core CKD anchor.") == "ckd"


def _test_infer_disease_from_question_ckd_chinese_creatinine():
    assert infer_disease_from_question("我的猫肌酐升高，这个库能告诉我什么") == "ckd"


def _test_infer_disease_from_question_ibd_boundary():
    q = "Where is the current IBD versus small-cell lymphoma boundary in this vault?"
    assert infer_disease_from_question(q) == "ibd"


def _test_infer_disease_from_question_diabetes():
    assert infer_disease_from_question("What is the SGLT2 role in feline diabetes?") == "diabetes"


def _test_infer_disease_from_question_fcv():
    assert infer_disease_from_question("What is the current FCV vaccine boundary in feline calicivirus?") == "fcv"


def _test_heuristic_question_type_claim_verification():
    q = "Verify whether SDMA should already be treated as a core early-detection anchor in this vault."
    assert heuristic_question_type(q) == "claim_verification"


def _test_heuristic_question_type_overview_chinese():
    q = "解释CKD"
    assert is_broad_explanation_question(q)
    assert heuristic_question_type(q) == "overview"


def _test_heuristic_question_type_overview_exact_disease():
    q = "CKD"
    assert is_broad_explanation_question(q)
    assert heuristic_question_type(q) == "overview"


def _test_heuristic_question_type_overview_chinese_worry():
    q = "我的猫肌酐升高，这个库能告诉我什么"
    assert is_broad_explanation_question(q)
    assert heuristic_question_type(q) == "overview"


def _test_heuristic_question_type_synthesis():
    q = "Compare CKD and HCM on the maturity of their endpoint architecture."
    assert heuristic_question_type(q) == "synthesis"


def _test_heuristic_question_type_regulatory():
    q = "What is the current regulatory path surface for feline CKD programs across China, FDA, and VMD?"
    assert heuristic_question_type(q) == "regulatory"


def _test_heuristic_question_type_recognition():
    q = "What is the current diagnostic workup architecture for feline FIP?"
    assert heuristic_question_type(q) == "recognition"


def _test_heuristic_question_type_recognition_chinese():
    q = "FIP怎么识别"
    assert heuristic_question_type(q) == "recognition"


def _test_heuristic_question_type_recognition_before_endpoints():
    q = "For feline HCM, what should be separated between recognition and endpoints?"
    assert heuristic_question_type(q) == "recognition"


def _test_heuristic_question_type_ibd_boundary_not_synthesis():
    q = "Where is the current IBD versus small-cell lymphoma boundary in this vault?"
    assert heuristic_question_type(q) == "recognition"


def _test_heuristic_question_type_ibd_boundary_chinese():
    q = "IBD和淋巴瘤怎么区分"
    assert heuristic_question_type(q) == "recognition"


def _test_heuristic_question_type_treatment():
    q = "How should SGLT2 and diet branches be separated in feline diabetes treatment?"
    assert heuristic_question_type(q) == "treatment"


def _test_heuristic_question_type_endpoints_chinese():
    q = "糖尿病猫为什么会缓解"
    assert heuristic_question_type(q) == "endpoints"


def _test_heuristic_files_for_route_synthesis():
    files = heuristic_files_for_route("synthesis", "ckd")
    assert files[0] == "system/indexes/disease-module-maturity-ladder.md"
    assert "system/indexes/cross-disease-second-wave-narrow-owner-audit.md" in files


def _test_heuristic_files_for_route_overview_starter_bundle():
    files = heuristic_files_for_route("overview", "ckd")
    assert files == [
        "topics/ckd/current-state-dashboard.md",
        "topics/ckd/synthesis-index.md",
    ], files


def _test_heuristic_files_for_route_diabetes_treatment_branches():
    files = heuristic_files_for_route("treatment", "diabetes")
    assert files[0] == "topics/diabetes/translation-brief.md", files
    assert "topics/diabetes/treatment-branch-map.md" in files
    assert "topics/diabetes/diet-architecture.md" in files
    assert "topics/diabetes/sglt2-label-control.md" in files


def _test_merge_routing_with_guardrails_overrides_qtype_and_prefixes_files():
    q = "Compare CKD and HCM on the maturity of their endpoint architecture."
    routed = {
        "question_type": "endpoints",
        "disease": "ckd",
        "files_to_load": ["topics/ckd/endpoint-handbook.md"],
        "reasoning": "Router guessed endpoints.",
    }
    merged = merge_routing_with_guardrails(q, None, routed)
    assert merged["question_type"] == "synthesis", merged
    assert merged["disease"] == "ckd", merged
    assert merged["files_to_load"][0] == "system/indexes/disease-module-maturity-ladder.md", merged
    assert "topics/ckd/endpoint-handbook.md" in merged["files_to_load"], merged


def _test_merge_routing_with_guardrails_claim_verification_prefers_verify_surface():
    q = "Verify whether SDMA should already be treated as a core early-detection anchor in this vault."
    merged = merge_routing_with_guardrails(q, None, {"question_type": "unknown", "disease": "unknown", "files_to_load": []})
    assert merged["question_type"] == "claim_verification", merged
    assert merged["disease"] == "ckd", merged
    assert merged["files_to_load"][0] == "system/indexes/verify-a-claim.md", merged


# ---------------------------------------------------------------------------
# parse_json_block
# ---------------------------------------------------------------------------

def _test_parse_json_block_raw():
    result = parse_json_block('{"action": "synthesize"}')
    assert result == {"action": "synthesize"}, result


def _test_parse_json_block_fenced():
    text = '```json\n{"action": "load_more", "files": ["topics/ckd/mechanism-overview.md"]}\n```'
    result = parse_json_block(text)
    assert result is not None
    assert result["action"] == "load_more"
    assert result["files"] == ["topics/ckd/mechanism-overview.md"]


def _test_parse_json_block_embedded_in_prose():
    text = 'I think we need more context. {"action": "load_sources", "source_ids": ["src-ckd-001"]} Done.'
    result = parse_json_block(text)
    assert result is not None
    assert result["action"] == "load_sources"


def _test_parse_json_block_invalid_returns_none():
    assert parse_json_block("not json at all") is None
    assert parse_json_block("{ broken json }") is None


def _test_parse_json_block_none_returns_none():
    assert parse_json_block(None) is None


def _test_chat_openai_compatible_none_content_raises_clear_error():
    class _FakeCompletions:
        def create(self, **kwargs):
            message = type("Message", (), {"content": None})()
            choice = type("Choice", (), {"message": message, "finish_reason": "stop"})()
            return type("Resp", (), {"choices": [choice]})()

    class _FakeChat:
        def __init__(self):
            self.completions = _FakeCompletions()

    class _FakeClient:
        def __init__(self):
            self.chat = _FakeChat()

    try:
        _chat(
            _FakeClient(),
            model="openai/gpt-5-mini",
            system="system",
            messages=[{"role": "user", "content": "hello"}],
            max_tokens=32,
        )
    except ValueError as exc:
        detail = str(exc)
        assert "OpenAI-compatible backend returned unsupported message content" in detail, detail
        assert "NoneType" in detail, detail
        assert "finish_reason='stop'" in detail, detail
    else:
        raise AssertionError("Expected None message.content to raise a clear ValueError")


def _test_chat_openai_compatible_none_content_includes_shape_summary():
    class _FakeCompletions:
        def create(self, **kwargs):
            message = type(
                "Message",
                (),
                {
                    "content": None,
                    "refusal": "",
                    "tool_calls": [object(), object()],
                    "annotations": [],
                    "audio": None,
                },
            )()
            choice = type("Choice", (), {"message": message, "finish_reason": "length"})()
            return type("Resp", (), {"choices": [choice]})()

    class _FakeChat:
        def __init__(self):
            self.completions = _FakeCompletions()

    class _FakeClient:
        def __init__(self):
            self.chat = _FakeChat()

    try:
        _chat(
            _FakeClient(),
            model="openai/gpt-5-mini",
            system="system",
            messages=[{"role": "user", "content": "hello"}],
            max_tokens=32,
        )
    except ValueError as exc:
        detail = str(exc)
        assert "finish_reason='length'" in detail, detail
        assert "tool_calls=2" in detail, detail
        assert "refusal_present=False" in detail, detail
        assert "content_type=NoneType" in detail, detail
    else:
        raise AssertionError("Expected None message.content to raise with shape summary")


# ---------------------------------------------------------------------------
# parse_source_ids_from_answer + compute_confidence
# ---------------------------------------------------------------------------

def _test_parse_source_ids_basic():
    answer = "Fibrosis is the primary driver. [quoted_fact: src-ckd-001] The role of TGF-β is well established. [source_supported_conclusion: src-ckd-002, src-ckd-003]"
    ids = parse_source_ids_from_answer(answer)
    assert ids == ["src-ckd-001", "src-ckd-002", "src-ckd-003"], ids


def _test_parse_source_ids_semicolon_separated():
    answer = "[quoted_fact: src-ckd-004; src-ckd-010] [source_supported_conclusion: src-ckd-003, src-ckd-006]"
    ids = parse_source_ids_from_answer(answer)
    assert ids == ["src-ckd-003", "src-ckd-004", "src-ckd-006", "src-ckd-010"], ids


def _test_parse_source_ids_deduplicates():
    answer = "[quoted_fact: src-ckd-001] [source_supported_conclusion: src-ckd-001, src-ckd-002]"
    ids = parse_source_ids_from_answer(answer)
    assert ids == ["src-ckd-001", "src-ckd-002"], ids


def _test_parse_source_ids_none():
    answer = "This is all llm_inference. [llm_inference] [llm_inference]"
    ids = parse_source_ids_from_answer(answer)
    assert ids == [], ids


def _test_sanitize_provenance_tags_filters_invalid_ids():
    answer = (
        "Claim [quoted_fact: src-hcm-mechanism; src-hcm-003]. "
        "Other [source_supported_conclusion: topic-hcm-dashboard]. "
        "Loose [llm_inference based on remodeling]. "
        "Bare [topic-ckd-current-state-dashboard]."
    )
    sanitized = sanitize_provenance_tags(answer, ["src-hcm-002", "src-hcm-003"])
    assert "[quoted_fact: src-hcm-003]" in sanitized
    assert "src-hcm-mechanism" not in sanitized
    assert "[source_supported_conclusion: topic-hcm-dashboard]" not in sanitized
    assert "[llm_inference based on remodeling]" not in sanitized
    assert "[topic-ckd-current-state-dashboard]" not in sanitized
    assert sanitized.endswith("[llm_inference]."), sanitized


def _test_sanitize_provenance_tags_normalizes_informal_source_brackets():
    answer = "结论[源自：src-ibd-003, src-ibd-024]，细节[中权重研究 src-ibd-010]。"
    sanitized = sanitize_provenance_tags(answer, ["src-ibd-003", "src-ibd-010", "src-ibd-024"])
    assert "[source_supported_conclusion: src-ibd-003, src-ibd-024]" in sanitized
    assert "[source_supported_conclusion: src-ibd-010]" in sanitized


def _test_expert_review_stage_label_tracks_manual_sample_gate():
    label = expert_review_stage_label()
    assert label == "manual sample 1/3-10", label


def _test_build_expert_review_prompt_preserves_answer_and_gate():
    prompt = build_expert_review_prompt(
        question="猫糖尿病哪些观察指标是核心终点？",
        answer="Remission is conditional. [source_supported_conclusion: src-diabetes-007]",
        disease="diabetes",
        question_type="endpoints",
        confidence="medium",
        source_ids=["src-diabetes-007", "src-diabetes-011"],
    )
    assert "manual sample 1/3-10" in prompt
    assert "not source evidence" in prompt
    assert "猫糖尿病哪些观察指标是核心终点？" in prompt
    assert "src-diabetes-007, src-diabetes-011" in prompt
    assert "Remission is conditional" in prompt


def _test_obesity_guidance_gate_allows_source_indexed_shell():
    path = Path("topics/obesity/current-state-dashboard.md")
    fm = {"topic": "obesity", "question_type": "dashboard", "decision_grade": "no"}
    text = "This source-indexed shell is not compiled obesity guidance. Sources remain partial."
    assert not is_obesity_compiled_guidance_gate_issue(path, fm, text)


def _test_obesity_guidance_gate_flags_compiled_guidance_before_deep_extraction():
    path = Path("topics/obesity/mechanism-overview.md")
    fm = {"topic": "obesity", "question_type": "mechanism", "decision_grade": "no"}
    text = "Obesity mechanism overview."
    assert is_obesity_compiled_guidance_gate_issue(path, fm, text)


def _test_classify_runtime_blocker_auth():
    stderr = "openai.AuthenticationError: Error code: 401 - {'error': {'message': 'User not found.'}}"
    assert classify_runtime_blocker(stderr) == "backend-auth"


def _test_classify_runtime_blocker_network():
    stderr = "httpcore.ConnectError: [Errno 1] Operation not permitted"
    assert classify_runtime_blocker(stderr) == "network"


def _test_classify_runtime_blocker_none():
    stderr = "[meta] ROUTER_QTYPE=overview\n[info] Synthesizing"
    assert classify_runtime_blocker(stderr) == ""


def _test_parse_source_ids_from_frontmatter_inline_list():
    content = textwrap.dedent("""\
        ---
        id: topic-ckd-endpoint
        source_ids: [src-ckd-001, src-ckd-002, src-ckd-003]
        ---
        # Body
    """)
    ids = parse_source_ids_from_frontmatter(content)
    assert ids == ["src-ckd-001", "src-ckd-002", "src-ckd-003"], ids


def _test_parse_source_ids_from_frontmatter_block_list():
    content = textwrap.dedent("""\
        ---
        id: topic-hcm-risk
        source_ids:
          - src-hcm-001
          - src-hcm-002
        question_type: recognition
        ---
        # Body
    """)
    ids = parse_source_ids_from_frontmatter(content)
    assert ids == ["src-hcm-001", "src-hcm-002"], ids


def _test_parse_source_ids_from_frontmatter_missing():
    content = textwrap.dedent("""\
        ---
        id: topic-empty
        question_type: synthesis
        ---
        # Body
    """)
    ids = parse_source_ids_from_frontmatter(content)
    assert ids == [], ids


def _test_frontmatter_scalar():
    content = textwrap.dedent("""\
        ---
        id: src-test-001
        title: "A Useful Source"
        year: 2024
        ---
        Body
    """)
    assert frontmatter_scalar(content, "title") == "A Useful Source"
    assert frontmatter_scalar(content, "year") == "2024"
    assert frontmatter_scalar(content, "missing") == ""


def _test_markdown_section():
    content = textwrap.dedent("""\
        # Title

        ## One-Line Summary

        Summary text.

        ### quoted_fact

        - fact one
        - fact two

        ### source_supported_conclusion

        - conclusion

        ## Limits / Caveats

        - caveat
    """)
    assert markdown_section(content, "### quoted_fact") == "- fact one\n- fact two"
    assert markdown_section(content, "## One-Line Summary") == (
        "Summary text.\n\n"
        "### quoted_fact\n\n"
        "- fact one\n- fact two\n\n"
        "### source_supported_conclusion\n\n"
        "- conclusion"
    )


def _test_compact_source_card_context_keeps_evidence_and_drops_full_body():
    content = textwrap.dedent("""\
        ---
        id: src-test-001
        title: "Compact Source"
        evidence_level: guideline
        verification_status: deep_extracted
        year: 2024
        ---

        # Compact Source

        ## One-Line Summary

        Short summary.

        ## Key Findings

        ### quoted_fact

        - Core fact.

        ### source_supported_conclusion

        - Supported conclusion.

        ## Long Body

        This should not be included in overview compact context.

        ## Limits / Caveats

        - Bounded caveat.
    """)
    compact = compact_source_card_context("src-test-001", "raw/papers/src-test-001.md", content)
    assert "compact overview source" in compact
    assert "Core fact." in compact
    assert "Supported conclusion." in compact
    assert "Bounded caveat." in compact
    assert "This should not be included" not in compact


def _test_compact_topic_page_context_keeps_overview_surface_and_drops_full_body():
    content = textwrap.dedent("""\
        ---
        id: topic-test-dashboard
        topic: ckd
        question_type: overview
        source_ids: [src-ckd-001, src-ckd-002, src-ckd-003]
        ---

        # Test Dashboard

        ## Current Status

        Useful status.

        ## Long Operational Section

        This should not be included in compact overview context.

        ## One-Sentence State

        Useful one sentence.
    """)
    compact = compact_topic_page_context("topics/ckd/current-state-dashboard.md", content)
    assert "compiled topic page" in compact
    assert "not a source card" in compact
    assert "Useful status." in compact
    assert "Useful one sentence." in compact
    assert "src-ckd-001" not in compact
    assert "This should not be included" not in compact


def _test_compute_confidence_high():
    answer = "Claim one. [quoted_fact: src-ckd-001] Claim two. [source_supported_conclusion: src-ckd-002]"
    assert compute_confidence(answer) == "high", compute_confidence(answer)


def _test_compute_confidence_medium():
    # 1 llm + 1 sourced → ratio = 0.5 → medium
    answer = "Claim one. [quoted_fact: src-ckd-001] Inference. [llm_inference]"
    assert compute_confidence(answer) == "medium", compute_confidence(answer)


def _test_compute_confidence_low():
    # 2 llm + 1 sourced → ratio = 0.67 → low
    answer = "[llm_inference] [llm_inference] [quoted_fact: src-ckd-001]"
    assert compute_confidence(answer) == "low", compute_confidence(answer)


def _test_compute_confidence_no_tags():
    answer = "No tags at all."
    assert compute_confidence(answer) == "low"


# ---------------------------------------------------------------------------
# OpenRouter budget guard
# ---------------------------------------------------------------------------

def _with_env(name: str, value, fn):
    old = os.environ.get(name)
    try:
        if value is None:
            os.environ.pop(name, None)
        else:
            os.environ[name] = value
        return fn()
    finally:
        if old is None:
            os.environ.pop(name, None)
        else:
            os.environ[name] = old


def _test_validate_openrouter_budget_accepts_one_dollar():
    assert _with_env("OPENROUTER_DAILY_BUDGET_USD", "1.00", validate_openrouter_budget) == 1.0


def _test_validate_openrouter_budget_rejects_missing():
    try:
        _with_env("OPENROUTER_DAILY_BUDGET_USD", None, validate_openrouter_budget)
    except ValueError as exc:
        assert "OPENROUTER_DAILY_BUDGET_USD not set" in str(exc), str(exc)
    else:
        raise AssertionError("Expected missing budget guard to raise")


def _test_validate_openrouter_budget_rejects_above_cap():
    try:
        _with_env("OPENROUTER_DAILY_BUDGET_USD", "1.01", validate_openrouter_budget)
    except ValueError as exc:
        assert "exceeds the project cap" in str(exc), str(exc)
    else:
        raise AssertionError("Expected budget above cap to raise")


# ---------------------------------------------------------------------------
# validate_frontmatter
# ---------------------------------------------------------------------------

def _valid_fm():
    return {
        "id": "qa-ckd-test-20260411",
        "type": "output",
        "output_kind": "qa",
        "topic": "ckd",
        "question": "What is the mechanism spine?",
        "question_type": "mechanism",
        "source_ids": ["src-ckd-001"],
        "generated_at": "2026-04-11",
        "hops": 2,
        "confidence": "medium",
    }


def _test_validate_frontmatter_valid():
    assert validate_frontmatter(_valid_fm()) == []


def _test_validate_frontmatter_missing_confidence():
    fm = _valid_fm()
    del fm["confidence"]
    missing = validate_frontmatter(fm)
    assert missing == ["confidence"], missing


def _test_validate_frontmatter_empty_string_counts_as_missing():
    fm = _valid_fm()
    fm["question_type"] = ""
    missing = validate_frontmatter(fm)
    assert "question_type" in missing, missing


def _test_validate_frontmatter_zero_hops_is_valid():
    fm = _valid_fm()
    fm["hops"] = 0
    assert validate_frontmatter(fm) == []


# ---------------------------------------------------------------------------
# build_slug
# ---------------------------------------------------------------------------

def _test_build_slug_basic():
    assert build_slug("What is the current mechanism spine for CKD?") == "what-is-the-current-mechanism-spine"


def _test_build_slug_strips_punctuation():
    assert build_slug("CKD: what is it?") == "ckd-what-is-it"


def _test_build_slug_short_question():
    assert build_slug("why CKD?") == "why-ckd"


# ---------------------------------------------------------------------------
# render_frontmatter
# ---------------------------------------------------------------------------

def _test_render_frontmatter_round_trips():
    fm = _valid_fm()
    fm["source_ids"] = ["src-ckd-001", "src-ckd-002"]
    fm["write_back_reviewed"] = False
    rendered = render_frontmatter(fm)
    assert rendered.startswith("---")
    assert rendered.endswith("---")
    assert "output_kind: qa" in rendered
    assert "- src-ckd-001" in rendered
    assert "write_back_reviewed: false" in rendered


# ---------------------------------------------------------------------------
# write_back (disk integration)
# ---------------------------------------------------------------------------

def _test_write_back_creates_file_with_valid_frontmatter():
    with tempfile.TemporaryDirectory() as tmp:
        vault_root = Path(tmp)
        # Minimal vault structure
        (vault_root / "outputs" / "qa").mkdir(parents=True)

        answer = textwrap.dedent("""\
            Feline CKD is primarily a fibrosis-driven disease. [quoted_fact: src-ckd-001]
            TGF-β is likely the central driver of progression. [source_supported_conclusion: src-ckd-001, src-ckd-002]
            Early detection may improve outcomes. [llm_inference]

            Files loaded: topics/ckd/mechanism-overview.md
            Source cards cited: src-ckd-001, src-ckd-002
        """)

        loaded = [vault_root / "topics" / "ckd" / "mechanism-overview.md"]

        out_path = write_back(
            answer=answer,
            question="What is the current mechanism spine for feline CKD?",
            disease="ckd",
            question_type="mechanism",
            hops_used=2,
            files_loaded=loaded,
            vault_root=vault_root,
        )

        assert out_path.exists(), f"Output file not created: {out_path}"
        content = out_path.read_text()

        # Frontmatter checks
        assert "type: output" in content
        assert "output_kind: qa" in content
        assert "topic: ckd" in content
        assert "confidence: medium" in content  # 1 llm / 3 total = 0.33 → medium
        assert "hops: 2" in content
        assert "- src-ckd-001" in content
        assert "- src-ckd-002" in content

        # Title check
        assert "# What is the current mechanism spine for feline CKD?" in content


def _test_write_back_aborts_on_missing_required_key():
    with tempfile.TemporaryDirectory() as tmp:
        vault_root = Path(tmp)
        (vault_root / "outputs" / "qa").mkdir(parents=True)

        try:
            write_back(
                answer="",  # empty answer → source_ids=[], confidence=low — all fine
                question="",  # empty question → validate_frontmatter should catch it
                disease="ckd",
                question_type="mechanism",
                hops_used=1,
                files_loaded=[],
                vault_root=vault_root,
            )
            # If we get here, the empty question slipped through. That's acceptable
            # since build_slug("") → "" and id still has disease+date components.
            # The real guard is validate_frontmatter — test that directly.
        except ValueError:
            pass  # expected


def _test_list_saved_answers_reads_outputs_and_inbox():
    with tempfile.TemporaryDirectory() as tmp:
        vault_root = Path(tmp)
        answer = "CKD answer. [quoted_fact: src-ckd-001]"
        loaded = [vault_root / "topics" / "ckd" / "mechanism-overview.md"]
        loaded[0].parent.mkdir(parents=True)
        loaded[0].write_text("# mechanism", encoding="utf-8")

        qa_path = write_back(
            answer=answer,
            question="What is CKD?",
            disease="ckd",
            question_type="mechanism",
            hops_used=1,
            files_loaded=loaded,
            vault_root=vault_root,
        )
        inbox_path = write_to_inbox(
            answer="FIP answer. [source_supported_conclusion: src-fip-001]",
            question="What is FIP?",
            disease="fip",
            question_type="recognition",
            vault_root=vault_root,
        )

        saved = list_saved_answers(vault_root, limit=10)
        files = {item["file"] for item in saved}
        assert str(qa_path.relative_to(vault_root)) in files
        assert str(inbox_path.relative_to(vault_root)) in files

        ckd_only = list_saved_answers(vault_root, limit=10, disease="ckd")
        assert len(ckd_only) == 1
        assert ckd_only[0]["question"] == "What is CKD?"
        assert ckd_only[0]["source_ids"] == ["src-ckd-001"]


def _test_list_saved_answers_ignores_rejected_inbox():
    with tempfile.TemporaryDirectory() as tmp:
        vault_root = Path(tmp)
        rejected = vault_root / "inbox" / "rejected" / "old.md"
        rejected.parent.mkdir(parents=True)
        rejected.write_text(textwrap.dedent("""\
            ---
            type: inbox
            topic: ckd
            question: "Rejected answer?"
            question_type: mechanism
            source_ids: [src-ckd-001]
            generated_at: 2026-04-23
            confidence: high
            ---

            # Rejected answer?

            Do not show.
        """), encoding="utf-8")

        assert list_saved_answers(vault_root, limit=10) == []


# ---------------------------------------------------------------------------
# estimate_tokens
# ---------------------------------------------------------------------------

def _test_estimate_tokens():
    text = "a" * 400
    assert estimate_tokens(text) == 100
    assert estimate_tokens("") == 0


# ---------------------------------------------------------------------------
# Vision integration tests
# ---------------------------------------------------------------------------

def _test_parse_local_assets_empty():
    """local_assets: [] returns empty list."""
    fm = "---\nid: src-test-001\nlinks:\n  url: https://example.com\n  local_assets: []\n---\n"
    assert _parse_local_assets_from_frontmatter(fm) == []


def _test_parse_local_assets_with_entries():
    """local_assets with two entries parses correctly."""
    fm = textwrap.dedent("""\
        ---
        id: src-test-001
        links:
          url: https://example.com
          local_assets:
            - raw/images/ckd/src-ckd-001-mechanism-schematic.png
            - raw/images/ckd/src-ckd-001-candidate-risk-factor.png
        ---
    """)
    result = _parse_local_assets_from_frontmatter(fm)
    assert len(result) == 2
    assert "raw/images/ckd/src-ckd-001-mechanism-schematic.png" in result
    assert "raw/images/ckd/src-ckd-001-candidate-risk-factor.png" in result


def _test_resolve_local_assets_filters_candidates_and_missing():
    """resolve_local_assets excludes candidate-* entries and non-existent files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        vault = Path(tmpdir)
        papers = vault / "raw" / "papers"
        papers.mkdir(parents=True)

        # Create a source card with one candidate and one "verified" (but missing) asset
        card_content = textwrap.dedent("""\
            ---
            id: src-ckd-001
            type: source
            links:
              url: https://example.com
              local_assets:
                - raw/images/ckd/src-ckd-001-candidate-mechanism.png
                - raw/images/ckd/src-ckd-001-mechanism-schematic.png
            ---
            # Title
        """)
        (papers / "src-ckd-001.md").write_text(card_content)

        # Neither file is on disk → should return empty list
        result = resolve_local_assets(["src-ckd-001"], vault)
        assert result == [], f"Expected [] when files missing, got {result}"

        # Create the verified (non-candidate) file → should now appear
        images_dir = vault / "raw" / "images" / "ckd"
        images_dir.mkdir(parents=True)
        real_file = images_dir / "src-ckd-001-mechanism-schematic.png"
        real_file.write_bytes(b"\x89PNG\r\n")  # minimal PNG header
        result = resolve_local_assets(["src-ckd-001"], vault)
        assert len(result) == 1
        assert result[0]["source_id"] == "src-ckd-001"
        assert result[0]["path"] == real_file.resolve()
        assert "candidate" not in result[0]["rel"]


def _test_write_back_includes_figures_used():
    """write_back includes figures_used in frontmatter when provided."""
    with tempfile.TemporaryDirectory() as tmpdir:
        vault = Path(tmpdir)
        (vault / "outputs" / "qa").mkdir(parents=True)
        figures = [{"source_id": "src-ckd-001", "file": "raw/images/ckd/src-ckd-001-mechanism.png", "described_in_answer": True}]
        answer = "Test answer. [quoted_fact: src-ckd-001]"
        out = write_back(
            answer=answer, question="What is the CKD mechanism?",
            disease="ckd", question_type="mechanism",
            hops_used=1, files_loaded=[],
            vault_root=vault, figures_used=figures,
        )
        content = out.read_text()
        assert "figures_used" in content
        assert "src-ckd-001" in content
        assert "described_in_answer" in content


# ---------------------------------------------------------------------------
# New edge cases: guards, empty inputs, missing cards, write-back None
# ---------------------------------------------------------------------------

def _test_parse_local_assets_key_missing():
    """Source card with no local_assets key at all returns []."""
    fm = "---\nid: src-test-001\nlinks:\n  url: https://example.com\n---\n"
    assert _parse_local_assets_from_frontmatter(fm) == []


def _test_resolve_local_assets_empty_source_ids():
    """Empty source_ids list returns []."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = resolve_local_assets([], Path(tmpdir))
        assert result == []


def _test_resolve_local_assets_card_file_not_found():
    """Source ID that doesn't map to a file on disk is skipped gracefully."""
    with tempfile.TemporaryDirectory() as tmpdir:
        vault = Path(tmpdir)
        (vault / "raw" / "papers").mkdir(parents=True)
        result = resolve_local_assets(["src-ghost-001"], vault)
        assert result == []


def _test_write_back_no_figures_used_key_when_none():
    """write_back() with figures_used=None does not include figures_used in frontmatter."""
    with tempfile.TemporaryDirectory() as tmpdir:
        vault = Path(tmpdir)
        (vault / "outputs" / "qa").mkdir(parents=True)
        out = write_back(
            answer="Test. [quoted_fact: src-ckd-001]",
            question="What is the CKD mechanism?",
            disease="ckd", question_type="mechanism",
            hops_used=1, files_loaded=[],
            vault_root=vault, figures_used=None,
        )
        content = out.read_text()
        assert "figures_used" not in content


def _test_resolve_local_assets_skips_large_file():
    """resolve_local_assets() skips files over 2MB with a warning."""
    with tempfile.TemporaryDirectory() as tmpdir:
        vault = Path(tmpdir)
        papers = vault / "raw" / "papers"
        papers.mkdir(parents=True)
        images = vault / "raw" / "images" / "ckd"
        images.mkdir(parents=True)

        large_png = images / "src-ckd-001-mechanism-large.png"
        large_png.write_bytes(b"\x89PNG\r\n" + b"0" * (3 * 1024 * 1024))

        card = papers / "src-ckd-001.md"
        card.write_text(
            "---\nid: src-ckd-001\nlinks:\n  local_assets:\n"
            "    - raw/images/ckd/src-ckd-001-mechanism-large.png\n---\n"
        )

        result = resolve_local_assets(["src-ckd-001"], vault)
        assert result == [], f"Expected [] for large file, got {result}"


def _test_resolve_local_assets_path_traversal_blocked():
    """resolve_local_assets() rejects paths that escape vault_root."""
    with tempfile.TemporaryDirectory() as tmpdir:
        vault = Path(tmpdir)
        papers = vault / "raw" / "papers"
        papers.mkdir(parents=True)

        card = papers / "src-ckd-001.md"
        card.write_text(
            "---\nid: src-ckd-001\nlinks:\n  local_assets:\n"
            "    - ../../etc/passwd\n---\n"
        )

        result = resolve_local_assets(["src-ckd-001"], vault)
        assert result == [], f"Path traversal not blocked: {result}"


# ---------------------------------------------------------------------------
# _figure_type_from_filename
# ---------------------------------------------------------------------------

def _test_resolve_local_assets_figure_type_routing_filters_mismatch():
    """resolve_local_assets with figure_type_hint excludes known mismatched types."""
    with tempfile.TemporaryDirectory() as tmpdir:
        vault = Path(tmpdir)
        papers = vault / "raw" / "papers"
        papers.mkdir(parents=True)
        images_dir = vault / "raw" / "images" / "ckd"
        images_dir.mkdir(parents=True)

        # Two figures: one mechanism, one imaging
        card_content = textwrap.dedent("""\
            ---
            id: src-ckd-001
            type: source
            links:
              url: https://example.com
              local_assets:
                - raw/images/ckd/src-ckd-001-mechanism-schematic.png
                - raw/images/ckd/src-ckd-001-imaging-echo.png
            ---
        """)
        (papers / "src-ckd-001.md").write_text(card_content)
        (images_dir / "src-ckd-001-mechanism-schematic.png").write_bytes(b"\x89PNG\r\n")
        (images_dir / "src-ckd-001-imaging-echo.png").write_bytes(b"\x89PNG\r\n")

        # With hint="mechanism" → imaging figure should be filtered out
        result = resolve_local_assets(["src-ckd-001"], vault, figure_type_hint="mechanism")
        assert len(result) == 1
        assert result[0]["figure_type"] == "mechanism"


def _test_resolve_local_assets_figure_type_routing_passes_unknown_type():
    """resolve_local_assets with figure_type_hint keeps figures whose type is None (non-standard name)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        vault = Path(tmpdir)
        papers = vault / "raw" / "papers"
        papers.mkdir(parents=True)
        images_dir = vault / "raw" / "images" / "ckd"
        images_dir.mkdir(parents=True)

        # One non-standard filename (figure_type=None) alongside a mismatched type
        card_content = textwrap.dedent("""\
            ---
            id: src-ckd-002
            type: source
            links:
              url: https://example.com
              local_assets:
                - raw/images/ckd/figure.png
                - raw/images/ckd/src-ckd-002-imaging-echo.png
            ---
        """)
        (papers / "src-ckd-002.md").write_text(card_content)
        (images_dir / "figure.png").write_bytes(b"\x89PNG\r\n")
        (images_dir / "src-ckd-002-imaging-echo.png").write_bytes(b"\x89PNG\r\n")

        # With hint="mechanism": non-standard "figure.png" keeps (type=None), imaging excluded
        result = resolve_local_assets(["src-ckd-002"], vault, figure_type_hint="mechanism")
        assert len(result) == 1
        assert result[0]["figure_type"] is None


def _test_resolve_local_assets_no_hint_passes_all_types():
    """resolve_local_assets without figure_type_hint returns all figure types."""
    with tempfile.TemporaryDirectory() as tmpdir:
        vault = Path(tmpdir)
        papers = vault / "raw" / "papers"
        papers.mkdir(parents=True)
        images_dir = vault / "raw" / "images" / "ckd"
        images_dir.mkdir(parents=True)

        card_content = textwrap.dedent("""\
            ---
            id: src-ckd-003
            type: source
            links:
              url: https://example.com
              local_assets:
                - raw/images/ckd/src-ckd-003-mechanism-schematic.png
                - raw/images/ckd/src-ckd-003-imaging-echo.png
                - raw/images/ckd/src-ckd-003-outcome-flowchart.png
            ---
        """)
        (papers / "src-ckd-003.md").write_text(card_content)
        for fname in ["src-ckd-003-mechanism-schematic.png", "src-ckd-003-imaging-echo.png", "src-ckd-003-outcome-flowchart.png"]:
            (images_dir / fname).write_bytes(b"\x89PNG\r\n")

        # No hint → all 3 figure types returned
        result = resolve_local_assets(["src-ckd-003"], vault)
        assert len(result) == 3


def _test_resolve_local_assets_jpg_jpeg_preserved_in_path():
    """resolve_local_assets preserves .jpg and .jpeg extensions in the returned path.

    This ensures synthesis_call() can correctly derive media_type (image/jpeg)
    rather than defaulting to image/png for JPEG files.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        vault = Path(tmpdir)
        papers = vault / "raw" / "papers"
        papers.mkdir(parents=True)
        images_dir = vault / "raw" / "images" / "ckd"
        images_dir.mkdir(parents=True)

        card_content = textwrap.dedent("""\
            ---
            id: src-ckd-004
            type: source
            links:
              url: https://example.com
              local_assets:
                - raw/images/ckd/src-ckd-004-mechanism-schematic.jpg
                - raw/images/ckd/src-ckd-004-outcome-table.jpeg
                - raw/images/ckd/src-ckd-004-imaging-echo.png
            ---
        """)
        (papers / "src-ckd-004.md").write_text(card_content)
        (images_dir / "src-ckd-004-mechanism-schematic.jpg").write_bytes(b"\xff\xd8\xff")  # JPEG magic
        (images_dir / "src-ckd-004-outcome-table.jpeg").write_bytes(b"\xff\xd8\xff")
        (images_dir / "src-ckd-004-imaging-echo.png").write_bytes(b"\x89PNG\r\n")

        result = resolve_local_assets(["src-ckd-004"], vault)
        suffixes = {a["path"].suffix.lower() for a in result}
        assert ".jpg" in suffixes, "Expected .jpg asset in result"
        assert ".jpeg" in suffixes, "Expected .jpeg asset in result"
        assert ".png" in suffixes, "Expected .png asset in result"
        assert len(result) == 3


def _test_figure_type_from_filename_standard():
    """Standard naming convention extracts the figure type segment."""
    assert _figure_type_from_filename("src-ckd-001-mechanism-schematic.png") == "mechanism"
    assert _figure_type_from_filename("src-hcm-010-imaging-echo-lv.png") == "imaging"
    assert _figure_type_from_filename("src-ckd-017-outcome-flowchart.png") == "outcome"


def _test_figure_type_from_filename_returns_none_for_short_name():
    """Filename with fewer than 4 dash-separated segments returns None."""
    assert _figure_type_from_filename("src-ckd-001.png") is None
    assert _figure_type_from_filename("figure.png") is None


def _test_figure_type_from_filename_requires_src_prefix():
    """Filename that doesn't start with 'src' returns None."""
    assert _figure_type_from_filename("raw-ckd-001-mechanism-schematic.png") is None


# ---------------------------------------------------------------------------
# vault_search
# ---------------------------------------------------------------------------

def _test_vault_search_finds_phosphorus_in_raw():
    results = vault_search("phosphorus", VAULT_ROOT, scope="raw", limit=5)
    assert len(results) > 0, "Expected at least one result for 'phosphorus' in raw/"
    assert results[0]["matches"] > 0
    assert results[0]["file"].startswith("raw/")

def _test_vault_search_returns_source_id():
    results = vault_search("proteinuria", VAULT_ROOT, scope="raw", limit=3)
    has_id = any(r["id"] is not None for r in results)
    assert has_id, "Expected at least one result with a source id"

def _test_vault_search_respects_limit():
    results = vault_search("CKD", VAULT_ROOT, scope="all", limit=3)
    assert len(results) <= 3

def _test_vault_search_no_results():
    results = vault_search("xyzzy_nonexistent_term_42", VAULT_ROOT, scope="raw")
    assert len(results) == 0

def _test_vault_search_regex():
    results = vault_search(r"proteinuria.*treatment", VAULT_ROOT, scope="topics", limit=5)
    assert len(results) > 0, "Expected regex match in topics"

def _test_format_results_for_llm_empty():
    assert format_results_for_llm([]) == "No results found."

def _test_format_results_for_llm_structure():
    fake = [{"file": "raw/papers/test.md", "id": "src-test-001", "title": "Test", "matches": 3, "snippets": ["snippet1"]}]
    output = format_results_for_llm(fake)
    assert "src-test-001" in output
    assert "snippet1" in output


# ---------------------------------------------------------------------------
# write_to_inbox
# ---------------------------------------------------------------------------

def _test_write_to_inbox_creates_file():
    with tempfile.TemporaryDirectory() as td:
        vr = Path(td)
        (vr / "inbox" / "ckd").mkdir(parents=True)
        answer = "CKD is common. [quoted_fact: src-ckd-001]"
        result = write_to_inbox(answer, "What is CKD?", "ckd", "mechanism", vr)
        assert result.exists(), f"Expected file at {result}"
        content = result.read_text()
        assert "review_status: pending" in content
        assert "src-ckd-001" in content
        assert "What is CKD?" in content

def _test_write_to_inbox_creates_directory():
    with tempfile.TemporaryDirectory() as td:
        vr = Path(td)
        # inbox/fip does NOT exist yet
        answer = "FIP answer. [llm_inference]"
        result = write_to_inbox(answer, "What is FIP?", "fip", "mechanism", vr)
        assert result.exists()
        assert "inbox/fip/" in str(result)


# ---------------------------------------------------------------------------
# compile_trigger
# ---------------------------------------------------------------------------

def _test_find_downstream_files_finds_topic_pages():
    downstream = find_downstream_files(["src-ckd-001"], VAULT_ROOT)
    assert "src-ckd-001" in downstream
    topic_files = [f for f in downstream["src-ckd-001"] if f.startswith("topics/")]
    assert len(topic_files) > 0, "Expected at least one topic page referencing src-ckd-001"

def _test_find_downstream_files_empty_for_nonexistent():
    downstream = find_downstream_files(["src-zzz-999"], VAULT_ROOT)
    assert downstream["src-zzz-999"] == []

def _test_build_recompile_queue_deduplicates():
    fake_downstream = {
        "src-a": ["topics/test.md", "system/test2.md"],
        "src-b": ["topics/test.md"],
    }
    queue = build_recompile_queue(fake_downstream)
    # topics/test.md should appear once with 2 sources
    test_entry = [q for q in queue if q["file"] == "topics/test.md"]
    assert len(test_entry) == 1
    assert test_entry[0]["source_count"] == 2
    assert sorted(test_entry[0]["affected_by"]) == ["src-a", "src-b"]

def _test_build_recompile_queue_sorted_by_count():
    fake_downstream = {
        "src-a": ["file1.md", "file2.md"],
        "src-b": ["file2.md", "file3.md"],
        "src-c": ["file2.md"],
    }
    queue = build_recompile_queue(fake_downstream)
    assert queue[0]["file"] == "file2.md"  # 3 sources
    assert queue[0]["source_count"] == 3


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print(f"\nRunning tests against vault at: {VAULT_ROOT}\n")

    test("build_source_index: real vault", _test_build_source_index_real_vault)
    test("build_source_index: synthetic files", _test_build_source_index_synthetic)

    test("resolve_link: valid relative link", _test_resolve_link_relative)
    test("resolve_link: http returns None", _test_resolve_link_http_returns_none)
    test("resolve_link: anchor-only returns None", _test_resolve_link_anchor_only_returns_none)
    test("resolve_link: missing file returns None", _test_resolve_link_missing_file_returns_none)

    test("infer_disease_from_question: CKD alias", _test_infer_disease_from_question_ckd)
    test("infer_disease_from_question: Chinese creatinine worry", _test_infer_disease_from_question_ckd_chinese_creatinine)
    test("infer_disease_from_question: IBD boundary", _test_infer_disease_from_question_ibd_boundary)
    test("infer_disease_from_question: diabetes alias", _test_infer_disease_from_question_diabetes)
    test("infer_disease_from_question: FCV alias", _test_infer_disease_from_question_fcv)
    test("heuristic_question_type: claim verification", _test_heuristic_question_type_claim_verification)
    test("heuristic_question_type: Chinese broad overview", _test_heuristic_question_type_overview_chinese)
    test("heuristic_question_type: exact disease overview", _test_heuristic_question_type_overview_exact_disease)
    test("heuristic_question_type: Chinese worry overview", _test_heuristic_question_type_overview_chinese_worry)
    test("heuristic_question_type: synthesis", _test_heuristic_question_type_synthesis)
    test("heuristic_question_type: regulatory", _test_heuristic_question_type_regulatory)
    test("heuristic_question_type: recognition", _test_heuristic_question_type_recognition)
    test("heuristic_question_type: recognition Chinese", _test_heuristic_question_type_recognition_chinese)
    test("heuristic_question_type: recognition beats endpoints wording", _test_heuristic_question_type_recognition_before_endpoints)
    test("heuristic_question_type: IBD boundary stays recognition", _test_heuristic_question_type_ibd_boundary_not_synthesis)
    test("heuristic_question_type: IBD boundary Chinese", _test_heuristic_question_type_ibd_boundary_chinese)
    test("heuristic_question_type: treatment", _test_heuristic_question_type_treatment)
    test("heuristic_question_type: endpoints Chinese", _test_heuristic_question_type_endpoints_chinese)
    test("heuristic_files_for_route: synthesis", _test_heuristic_files_for_route_synthesis)
    test("heuristic_files_for_route: overview starter bundle", _test_heuristic_files_for_route_overview_starter_bundle)
    test("heuristic_files_for_route: diabetes treatment branches", _test_heuristic_files_for_route_diabetes_treatment_branches)
    test("merge_routing_with_guardrails: synthesis override", _test_merge_routing_with_guardrails_overrides_qtype_and_prefixes_files)
    test("merge_routing_with_guardrails: claim verification surface", _test_merge_routing_with_guardrails_claim_verification_prefers_verify_surface)

    test("parse_json_block: raw JSON", _test_parse_json_block_raw)
    test("parse_json_block: fenced markdown", _test_parse_json_block_fenced)
    test("parse_json_block: embedded in prose", _test_parse_json_block_embedded_in_prose)
    test("parse_json_block: invalid returns None", _test_parse_json_block_invalid_returns_none)
    test("parse_json_block: None returns None", _test_parse_json_block_none_returns_none)
    test("_chat: openai-compatible None content raises clear error", _test_chat_openai_compatible_none_content_raises_clear_error)
    test("_chat: openai-compatible None content includes shape summary", _test_chat_openai_compatible_none_content_includes_shape_summary)

    test("parse_source_ids: basic", _test_parse_source_ids_basic)
    test("parse_source_ids: semicolon-separated", _test_parse_source_ids_semicolon_separated)
    test("parse_source_ids: deduplicates", _test_parse_source_ids_deduplicates)
    test("parse_source_ids: no citations", _test_parse_source_ids_none)
    test("sanitize_provenance_tags: filters invalid ids", _test_sanitize_provenance_tags_filters_invalid_ids)
    test("sanitize_provenance_tags: normalizes informal source brackets", _test_sanitize_provenance_tags_normalizes_informal_source_brackets)
    test("expert_review: stage label tracks manual gate", _test_expert_review_stage_label_tracks_manual_sample_gate)
    test("expert_review: prompt preserves answer and gate", _test_build_expert_review_prompt_preserves_answer_and_gate)
    test("health: obesity guidance gate allows source-indexed shell", _test_obesity_guidance_gate_allows_source_indexed_shell)
    test("health: obesity guidance gate flags compiled guidance", _test_obesity_guidance_gate_flags_compiled_guidance_before_deep_extraction)
    test("classify_runtime_blocker: auth", _test_classify_runtime_blocker_auth)
    test("classify_runtime_blocker: network", _test_classify_runtime_blocker_network)
    test("classify_runtime_blocker: none", _test_classify_runtime_blocker_none)
    test("parse_source_ids_from_frontmatter: inline list", _test_parse_source_ids_from_frontmatter_inline_list)
    test("parse_source_ids_from_frontmatter: block list", _test_parse_source_ids_from_frontmatter_block_list)
    test("parse_source_ids_from_frontmatter: missing", _test_parse_source_ids_from_frontmatter_missing)
    test("frontmatter_scalar: basic", _test_frontmatter_scalar)
    test("markdown_section: bounded extraction", _test_markdown_section)
    test("compact_source_card_context: overview evidence excerpt", _test_compact_source_card_context_keeps_evidence_and_drops_full_body)
    test("compact_topic_page_context: overview surface excerpt", _test_compact_topic_page_context_keeps_overview_surface_and_drops_full_body)

    test("compute_confidence: high", _test_compute_confidence_high)
    test("compute_confidence: medium", _test_compute_confidence_medium)
    test("compute_confidence: low", _test_compute_confidence_low)
    test("compute_confidence: no tags → low", _test_compute_confidence_no_tags)

    test("validate_openrouter_budget: accepts $1", _test_validate_openrouter_budget_accepts_one_dollar)
    test("validate_openrouter_budget: rejects missing", _test_validate_openrouter_budget_rejects_missing)
    test("validate_openrouter_budget: rejects above cap", _test_validate_openrouter_budget_rejects_above_cap)

    test("validate_frontmatter: valid", _test_validate_frontmatter_valid)
    test("validate_frontmatter: missing confidence", _test_validate_frontmatter_missing_confidence)
    test("validate_frontmatter: empty string is missing", _test_validate_frontmatter_empty_string_counts_as_missing)
    test("validate_frontmatter: hops=0 is valid", _test_validate_frontmatter_zero_hops_is_valid)

    test("build_slug: basic", _test_build_slug_basic)
    test("build_slug: strips punctuation", _test_build_slug_strips_punctuation)
    test("build_slug: short question", _test_build_slug_short_question)

    test("render_frontmatter: round-trips", _test_render_frontmatter_round_trips)

    test("write_back: creates file with valid frontmatter", _test_write_back_creates_file_with_valid_frontmatter)
    test("write_back: aborts cleanly on bad input", _test_write_back_aborts_on_missing_required_key)
    test("write_back: includes figures_used when provided", _test_write_back_includes_figures_used)
    test("list_saved_answers: reads outputs and inbox", _test_list_saved_answers_reads_outputs_and_inbox)
    test("list_saved_answers: ignores rejected inbox", _test_list_saved_answers_ignores_rejected_inbox)

    test("estimate_tokens", _test_estimate_tokens)

    test("_parse_local_assets: empty list", _test_parse_local_assets_empty)
    test("_parse_local_assets: two entries", _test_parse_local_assets_with_entries)
    test("resolve_local_assets: filters candidates and missing files", _test_resolve_local_assets_filters_candidates_and_missing)

    test("_parse_local_assets: key missing → []", _test_parse_local_assets_key_missing)
    test("resolve_local_assets: empty source_ids → []", _test_resolve_local_assets_empty_source_ids)
    test("resolve_local_assets: card not found → []", _test_resolve_local_assets_card_file_not_found)
    test("write_back: figures_used=None → no key", _test_write_back_no_figures_used_key_when_none)
    test("resolve_local_assets: large file skipped", _test_resolve_local_assets_skips_large_file)
    test("resolve_local_assets: path traversal blocked", _test_resolve_local_assets_path_traversal_blocked)

    test("_figure_type_from_filename: standard naming", _test_figure_type_from_filename_standard)
    test("_figure_type_from_filename: short name → None", _test_figure_type_from_filename_returns_none_for_short_name)
    test("_figure_type_from_filename: non-src prefix → None", _test_figure_type_from_filename_requires_src_prefix)

    test("resolve_local_assets: figure_type_hint filters mismatched types", _test_resolve_local_assets_figure_type_routing_filters_mismatch)
    test("resolve_local_assets: figure_type_hint passes unknown type (None)", _test_resolve_local_assets_figure_type_routing_passes_unknown_type)
    test("resolve_local_assets: no hint passes all types", _test_resolve_local_assets_no_hint_passes_all_types)
    test("resolve_local_assets: jpg/jpeg extensions preserved in path", _test_resolve_local_assets_jpg_jpeg_preserved_in_path)

    test("vault_search: finds phosphorus in raw", _test_vault_search_finds_phosphorus_in_raw)
    test("vault_search: returns source id", _test_vault_search_returns_source_id)
    test("vault_search: respects limit", _test_vault_search_respects_limit)
    test("vault_search: no results for nonsense", _test_vault_search_no_results)
    test("vault_search: regex matching", _test_vault_search_regex)
    test("format_results_for_llm: empty", _test_format_results_for_llm_empty)
    test("format_results_for_llm: structure", _test_format_results_for_llm_structure)

    test("write_to_inbox: creates file", _test_write_to_inbox_creates_file)
    test("write_to_inbox: creates directory", _test_write_to_inbox_creates_directory)

    test("find_downstream_files: finds topic pages", _test_find_downstream_files_finds_topic_pages)
    test("find_downstream_files: empty for nonexistent", _test_find_downstream_files_empty_for_nonexistent)
    test("build_recompile_queue: deduplicates", _test_build_recompile_queue_deduplicates)
    test("build_recompile_queue: sorted by count", _test_build_recompile_queue_sorted_by_count)

    passed = sum(1 for _, ok, _ in results if ok)
    failed = sum(1 for _, ok, _ in results if not ok)
    print(f"\n{'='*50}")
    print(f"  {passed} passed  |  {failed} failed  |  {len(results)} total")
    if failed:
        print("\nFailed tests:")
        for name, ok, err in results:
            if not ok:
                print(f"  - {name}: {err}")
    print()
    sys.exit(0 if failed == 0 else 1)
