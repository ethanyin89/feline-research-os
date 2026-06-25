"""
scripts/app.py — Streamlit chat UI for the feline research OS vault.

Usage:
    pip install streamlit anthropic openai
    ANTHROPIC_API_KEY=<key> streamlit run scripts/app.py

Opens localhost:8501 in your browser. Type a research question, get a
sourced answer with provenance tags. Optionally save answers from the
sidebar.
"""

from __future__ import annotations

import os
import re
import sys
import json
import html
import subprocess
import urllib.request
from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------------------------
# Runtime config — Streamlit Cloud stores deploy variables in st.secrets, while
# the query layer reads os.environ. Mirror known keys before importing query.py.
# ---------------------------------------------------------------------------

def sync_streamlit_secrets_to_env() -> None:
    """Expose supported Streamlit secrets as environment variables."""
    for key in (
        "ANTHROPIC_API_KEY",
        "OPENROUTER_API_KEY",
        "OPENROUTER_DAILY_BUDGET_USD",
        "OPENROUTER_MODEL",
        "ENABLE_OLLAMA",
    ):
        if os.environ.get(key):
            continue
        try:
            value = st.secrets.get(key)
        except Exception:
            value = None
        if value is not None and str(value).strip():
            os.environ[key] = str(value).strip()


sync_streamlit_secrets_to_env()

# ---------------------------------------------------------------------------
# Path setup — allow importing query.py from the same directory
# ---------------------------------------------------------------------------

SCRIPTS_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))
sys.path.insert(0, str(VAULT_ROOT))

from query import (
    MODEL,
    OLLAMA_MODEL,
    OPENROUTER_MODEL,
    NoSourceCardsLoadedError,
    validate_openrouter_budget,
    make_client,
    _chat,
    build_source_index,
    build_source_titles,
    build_source_weights,
    compute_confidence,
    prefers_chinese,
    build_external_search_trace,
    is_local_search_sparse,
    list_saved_answers,
    parse_source_ids_from_answer,
    run_query_core,
    write_back,
    # P3 Citation Graph
    get_paper_citations,
    get_reference_links,
    get_cited_by_links,
    get_citation_summary,
)
from expert_review import build_expert_review_prompt, expert_review_stage_label
from search import vault_search

from local_answer_surfaces import build_ckd_researcher_overview, is_researcher_overview_question, build_ckd_topic_index
from research_case_ui import render_research_cases
from research_record_ui import render_research_records
from research_mode import is_research_mode_query, handle_research_query, handle_research_query_structured
from workspace_tabs import (
    render_workspace_tabs,
    convert_research_mode_output_to_workspace,
    WorkspaceOutput,
)
from quick_start import (
    get_quick_start,
    detect_quick_start_intent,
    format_quick_start_markdown,
    QuickStartOutput,
)
from briefing_ui import (
    get_briefing,
    render_briefing_page,
    get_available_diseases,
    BriefingFile,
)
from deep_extraction import (
    has_deep_extraction,
    parse_deep_extraction,
    render_detail_page_markdown,
)
from harness_loop import get_harness_loop, format_harness_summary
from core import (
    build_promotion_draft,
    extract_claim_candidates,
    ValidatedClaimStore,
)
from core.schemas import RetrievalEvent, SourceSnapshot

# Phase 4: ResultPresentation contract (feature-flagged)
try:
    from core.result_presentation import (
        build_evidence_profile,
        build_source_displays,
        build_result_presentation,
        build_next_actions,
        translate_provenance,
        render_user_facing_provenance,
        detect_presentation_state,
        get_state_warning,
        ResultPresentation,
        SourceDisplay,
        EvidenceTrace,
        EvidenceProfile,
        ActionType,
    )
    from core.source_metadata import load_source_metadata
    RESULT_PRESENTATION_AVAILABLE = True
except ImportError:
    RESULT_PRESENTATION_AVAILABLE = False

ENABLE_OLLAMA = os.environ.get("ENABLE_OLLAMA", "").lower() in {"1", "true", "yes", "on"}
BACKEND_LABELS = {
    "local": "Vault Search (free)",
    "anthropic": "Anthropic (API)",
    "openrouter": "OpenRouter (API)",
    "ollama": "Ollama (local)",
}
AVAILABLE_BACKENDS = ["local", "anthropic", "openrouter"] + (["ollama"] if ENABLE_OLLAMA else [])
OPENROUTER_STREAMLIT_COMMAND = (
    "OPENROUTER_DAILY_BUDGET_USD=1.00 "
    "OPENROUTER_MODEL=openai/gpt-4.1-mini "
    ".venv/bin/python -m streamlit run scripts/app.py"
)
APP_RELEASE_LABEL = "source-grounded-workspace-20260625"


def get_runtime_commit() -> str:
    """Return a short commit/build identifier for deployment debugging."""
    for key in ("STREAMLIT_GIT_COMMIT", "GIT_COMMIT", "VERCEL_GIT_COMMIT_SHA", "COMMIT_SHA"):
        value = os.environ.get(key, "").strip()
        if value:
            return value[:7]
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=VAULT_ROOT,
            check=False,
            capture_output=True,
            text=True,
            timeout=1.5,
        )
    except Exception:
        return "unknown"
    commit = result.stdout.strip()
    return commit or "unknown"

# ---------------------------------------------------------------------------
# Phase 4: Feature flag for new result presentation
# ---------------------------------------------------------------------------

# Set to True to enable new ResultPresentation-based rendering
# The old renderer remains available for rollback
USE_RESULT_PRESENTATION_V2 = os.environ.get("USE_RESULT_PRESENTATION_V2", "1").lower() in {"1", "true", "yes", "on"}

# ---------------------------------------------------------------------------
# Provenance badge rendering
# ---------------------------------------------------------------------------

BADGE_PATTERNS = [
    (
        r"\[quoted_fact: ([^\]]+)\]",
        r'<span style="background:rgba(16,185,129,0.1);color:#10b981;padding:3px 10px;'
        r'border:1px solid rgba(16,185,129,0.25);border-radius:5px;font-size:0.72em;white-space:nowrap;'
        r'font-family:\'JetBrains Mono\',monospace;font-weight:500">'
        r"quote: \1</span>",
    ),
    (
        r"\[source_supported_conclusion: ([^\]]+)\]",
        r'<span style="background:rgba(217,119,6,0.1);color:#d97706;padding:3px 10px;'
        r'border:1px solid rgba(217,119,6,0.25);border-radius:5px;font-size:0.72em;white-space:nowrap;'
        r'font-family:\'JetBrains Mono\',monospace;font-weight:500">'
        r"supported: \1</span>",
    ),
    (
        r"\[llm_inference\]",
        r'<span style="background:rgba(107,114,128,0.1);color:#6b7280;padding:3px 10px;'
        r'border:1px solid rgba(107,114,128,0.25);border-radius:5px;font-size:0.72em;white-space:nowrap;'
        r'font-family:\'JetBrains Mono\',monospace;font-weight:500">'
        r"inference</span>",
    ),
]

# Basic explanation examples
EXAMPLE_QUESTIONS_BASIC = [
    "解释CKD",
    "FIP怎么识别",
    "IBD和淋巴瘤怎么区分",
    "HCM是什么，为什么危险",
]

# Research Workspace examples (agent.ii.inc style)
EXAMPLE_QUESTIONS_RESEARCH = [
    "构建 feline HCM 近三年文献图谱",
    "比较 CKD 诊断与分期指标的研究价值",
    "梳理 FIP 治疗研究的药效终点",
    "提炼猫糖尿病模型的关键评价指标",
]

# Combined for backwards compatibility
EXAMPLE_QUESTIONS = EXAMPLE_QUESTIONS_BASIC + EXAMPLE_QUESTIONS_RESEARCH[:1]

PROVENANCE_GUIDE_HTML = """
<div class="vault-panel" style="margin-top:24px">
  <div class="vault-panel-label">证据标签指南</div>
  <div class="vault-guide-row"><span class="prov-badge prov-quoted">直接来源</span><span>文献原文或指南明确支持的结论</span></div>
  <div class="vault-guide-row"><span class="prov-badge prov-supported">来源支持</span><span>由多篇文献共同支持的综合判断</span></div>
  <div class="vault-guide-row"><span class="prov-badge prov-inference">分析推断</span><span>基于已有证据作出的合理推理，需要人工复核</span></div>
</div>
"""

EMPTY_STATE_INTRO_HTML = """
<div class="vault-hero" style="text-align: center; padding: 48px 0 24px 0;">
  <h1 style="font-size: 32px; font-weight: 500; color: #eceff4; margin-bottom: 12px; font-family: 'Inter', sans-serif;">今天想研究什么？</h1>
  <p style="font-size: 15px; color: #b8bfcc; max-width: 480px; margin: 0 auto; line-height: 1.6; font-family: 'Source Serif 4', serif;">输入一个猫病、模型、文献或药效评价问题。<br/>系统会帮你找依据、提炼结论，并标出原文出处。</p>
</div>
"""

SEARCH_CARD_TEMPLATE = """
<div class="vault-panel vault-search-card">
  <div class="vault-search-title">{title}</div>
  <div class="vault-search-subtitle">{subtitle}</div>
</div>
"""

NOTICE_TEMPLATE = """
<div class="vault-inline-note vault-inline-note-{tone}">
  {body}
</div>
"""

HOW_IT_WORKS_HTML = """
<div class="vault-panel">
  <div class="vault-panel-label">工作原理</div>
  <p class="vault-panel-copy">
    系统不会直接生成一个看似完整的答案，而是先从结构化文献、Briefing 和深度提炼卡片中检索证据，再区分直接来源、来源支持和分析推断，最后生成带有证据边界的研究结论。<br/><br/>
    它的目标不是替代研究者判断，而是帮助研究者更快找到关键文献、关键指标和关键不确定性。
  </p>
</div>
"""

HOW_IT_WORKS_COPY = (
    "本工具用于检索猫科疾病知识库。系统会自动路由到整理好的主题页面及文献卡片，生成精炼的回答，"
    "并为每个事实性声明标记证据等级。绿色标签（直接来源）表示非常贴近文献原文表述；黄色标签（来源支持）"
    "表示有证据支持的综合推断；灰色标签（分析推断）表示回答超出了已加载文献的直接范围。"
)


def _humanize_source_ids(ids_str: str) -> str:
    """Convert internal source IDs to human-readable paper titles.

    Example: "src-ckd-004, src-ckd-010" -> "Renal Diet Study (2019), IRIS Guidelines (2023)"
    """
    if not ids_str:
        return ids_str
    ids = [s.strip() for s in ids_str.split(",")]
    titles = []
    for sid in ids:
        if is_internal_source_id(sid):
            title = get_source_titles().get(sid)
            if title:
                # Truncate long titles for badge display
                short_title = title[:40] + "…" if len(title) > 40 else title
                titles.append(short_title)
            else:
                # Fallback: show generic label instead of internal ID
                titles.append("文献" if is_session_chinese() else "source")
        else:
            titles.append(sid)
    return ", ".join(titles)


def render_provenance(text: str) -> str:
    """Replace provenance tags with colored HTML badges.

    IMPORTANT: Internal source IDs (src-xxx) are converted to paper titles
    to avoid exposing internal file structure to users.
    """
    is_zh = is_session_chinese()
    badge_quote = "直接来源" if is_zh else "quote"
    badge_supported = "来源支持" if is_zh else "supported"
    badge_inference = "分析推断" if is_zh else "inference"

    # quoted_fact badges - humanize source IDs
    def replace_quoted_fact(match: re.Match) -> str:
        humanized = _humanize_source_ids(match.group(1))
        return (
            f'<span style="background:rgba(16,185,129,0.1);color:#10b981;padding:3px 10px;'
            f'border:1px solid rgba(16,185,129,0.25);border-radius:5px;font-size:0.72em;white-space:nowrap;'
            f"font-family:'JetBrains Mono',monospace;font-weight:500\">"
            f'{badge_quote}: {html.escape(humanized)}</span>'
        )
    text = re.sub(r"\[quoted_fact: ([^\]]+)\]", replace_quoted_fact, text)

    # source_supported_conclusion badges - humanize source IDs
    def replace_supported(match: re.Match) -> str:
        humanized = _humanize_source_ids(match.group(1))
        return (
            f'<span style="background:rgba(217,119,6,0.1);color:#d97706;padding:3px 10px;'
            f'border:1px solid rgba(217,119,6,0.25);border-radius:5px;font-size:0.72em;white-space:nowrap;'
            f"font-family:'JetBrains Mono',monospace;font-weight:500\">"
            f'{badge_supported}: {html.escape(humanized)}</span>'
        )
    text = re.sub(r"\[source_supported_conclusion: ([^\]]+)\]", replace_supported, text)

    text = re.sub(
        r"\[llm_inference\]",
        r'<span style="background:rgba(107,114,128,0.1);color:#6b7280;padding:3px 10px;'
        r'border:1px solid rgba(107,114,128,0.25);border-radius:5px;font-size:0.72em;white-space:nowrap;'
        r'font-family:\'JetBrains Mono\',monospace;font-weight:500">'
        f'{badge_inference}</span>',
        text
    )
    return text


def is_internal_source_id(value: object) -> bool:
    """Return True for internal vault IDs such as src-ckd-001."""
    return bool(re.fullmatch(r"src-[a-z]+-\d{3}", str(value or "").strip()))


def user_visible_source_label(source_id: str, fallback: str = "source") -> str:
    """Map an internal source ID to a user-facing paper title when possible."""
    if not source_id:
        return fallback
    if not is_internal_source_id(source_id):
        return source_id
    title = get_source_titles().get(source_id)
    return title or fallback


def normalize_user_facing_topic_text(text: str) -> str:
    """Normalize disease acronyms in user-facing action labels and queries."""
    if not text:
        return text
    replacements = {
        "ckd": "CKD",
        "hcm": "HCM",
        "fip": "FIP",
        "ibd": "IBD",
        "fcv": "FCV",
    }
    normalized = text
    for raw, display in replacements.items():
        normalized = re.sub(rf"\b{raw}\b", display, normalized, flags=re.IGNORECASE)
    return normalized


def queue_question(question: str) -> None:
    """Store a question from a UI chip and rerun before rendering the answer."""
    st.session_state.pending_question = question
    st.rerun()


def render_example_question_chips(prefix: str, show_research: bool = True) -> None:
    """Render clickable example questions with category separation."""
    is_zh = is_session_chinese()

    if show_research:
        # Side-by-side layout: Deep research (left, wider) and Quick ask (right, narrower)
        col_research, col_quick = st.columns([1.2, 0.8])

        with col_research:
            research_label = "🔬 深度研究" if is_zh else "🔬 Deep Research"
            research_hint = (
                "检索文献、比较证据、生成可追溯结论"
                if is_zh else
                "Search literature, compare evidence, generate traceable conclusions"
            )
            st.markdown(
                f"""<div style="font-size:11px;color:#10b981;margin-bottom:2px;font-weight:600">
                {html.escape(research_label)}</div>
                <div style="font-size:10px;color:#8b90a0;margin-bottom:10px">
                {html.escape(research_hint)}</div>""",
                unsafe_allow_html=True,
            )
            for i, question in enumerate(EXAMPLE_QUESTIONS_RESEARCH):
                if st.button(question, key=f"{prefix}-research-{i}", use_container_width=True):
                    queue_question(question)

        with col_quick:
            basic_label = "⚡ 快速解释" if is_zh else "⚡ Quick Explain"
            quick_start_hint = (
                "30 秒理解疾病、指标或概念"
                if is_zh else
                "30s disease, metric, or concept check"
            )
            st.markdown(
                f"""<div style="font-size:11px;color:#d97706;margin-bottom:2px;font-weight:600">
                {html.escape(basic_label)}</div>
                <div style="font-size:10px;color:#8b90a0;margin-bottom:10px">
                {html.escape(quick_start_hint)}</div>""",
                unsafe_allow_html=True,
            )
            for i, question in enumerate(EXAMPLE_QUESTIONS_BASIC):
                if st.button(question, key=f"{prefix}-basic-{i}", use_container_width=True):
                    queue_question(question)
    else:
        # Fallback without research chips
        basic_label = "⚡ 快速解释" if is_zh else "⚡ Quick Explain"
        st.markdown(
            f"""<div style="font-size:11px;color:#d97706;margin-bottom:4px;font-weight:600">
            {html.escape(basic_label)}</div>""",
            unsafe_allow_html=True,
        )
        cols = st.columns(2)
        for i, question in enumerate(EXAMPLE_QUESTIONS_BASIC):
            with cols[i % 2]:
                if st.button(question, key=f"{prefix}-basic-{i}", use_container_width=True):
                    queue_question(question)


def render_provenance_guide() -> None:
    """Explain provenance badge colors for new users."""
    st.markdown(PROVENANCE_GUIDE_HTML, unsafe_allow_html=True)


def render_how_it_works() -> None:
    """Show a lightweight onboarding explainer for first-time users."""
    with st.expander("工作原理", expanded=not st.session_state.how_it_works_seen):
        st.markdown(HOW_IT_WORKS_HTML, unsafe_allow_html=True)
        st.caption(HOW_IT_WORKS_COPY)
    st.session_state.how_it_works_seen = True


def render_saved_answers_panel(prefix: str, disease_filter: Optional[str] = None) -> None:
    """Render recent saved QA/inbox answers as a reuse surface."""
    saved_answers = list_saved_answers(VAULT_ROOT, limit=5, disease=disease_filter)
    if not saved_answers:
        return

    with st.expander("历史回答", expanded=False):
        for i, item in enumerate(saved_answers):
            question = html.escape(str(item["question"]))
            topic = html.escape(str(item["topic"]).upper())
            question_type = html.escape(str(item["question_type"]))
            confidence = html.escape(str(item["confidence"]))
            generated_at = html.escape(str(item["generated_at"] or "undated"))
            file_path = html.escape(str(item["file"]))
            source_ids = [html.escape(str(sid)) for sid in item.get("source_ids", [])]
            visible_sources = [
                html.escape(user_visible_source_label(str(sid), fallback="source"))
                for sid in item.get("source_ids", [])
            ]
            sources = " ".join(f"<span>{source}</span>" for source in visible_sources[:4]) or "<span>no cited sources</span>"
            if len(source_ids) > 4:
                sources += f" <span>+{len(source_ids) - 4}</span>"

            st.markdown(
                f"""
                <div class="vault-answer-row">
                  <div class="vault-answer-title">{question}</div>
                  <div class="vault-answer-meta">
                    <span>{topic}</span><span>{question_type}</span><span>{confidence}</span><span>{generated_at}</span>
                  </div>
                  <div class="vault-answer-sources">{sources}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            preview = str(item.get("answer_preview") or "").strip()
            if preview:
                st.markdown(
                    f"<div class='vault-answer-preview'>{render_provenance(html.escape(preview[:420]))}</div>",
                    unsafe_allow_html=True,
                )

            if st.button("Ask again", key=f"{prefix}-saved-answer-{i}", use_container_width=False):
                queue_question(str(item["question"]))


def detect_chinese(text: str) -> bool:
    """Return True when text contains CJK characters."""
    return bool(re.search(r"[\u3400-\u9fff]", text))


def is_session_chinese() -> bool:
    """Check if the current session leans towards Chinese."""
    try:
        if st.session_state.get("pending_question") and detect_chinese(st.session_state.pending_question):
            return True
        messages = st.session_state.get("messages", [])
        for msg in reversed(messages):
            if msg.get("role") == "user" and detect_chinese(msg.get("content", "")):
                return True
    except Exception:
        pass
    return True


def extract_topic_paths_from_text(text: str) -> list[str]:
    """Find all topic pages referenced in the text (e.g. topics/ckd/mechanism-overview.md)."""
    # Match patterns like `topics/xxx/yyy.md` or topics/xxx/yyy.md
    paths = re.findall(r'`?(topics/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+\.md)`?', text)
    seen = set()
    res = []
    for p in paths:
        p_clean = p.strip("`").strip()
        if p_clean not in seen:
            seen.add(p_clean)
            res.append(p_clean)
    return res


def format_topic_path(path_str: str) -> str:
    """Format a topic page path like topics/ckd/mechanism-overview.md to a human-friendly title."""
    try:
        from pathlib import Path
        stem = Path(path_str).stem
        clean_name = stem.replace("topic-", "").replace("-zh", "").replace("-", " ")
        title = " ".join(w.capitalize() for w in clean_name.split())
        acronyms = {"Hcm": "HCM", "Ckd": "CKD", "Fip": "FIP", "Ibd": "IBD", "Fcv": "FCV", "Pmd": "PMD", "Pk": "PK", "Pd": "PD"}
        title = " ".join(acronyms.get(w, w) for w in title.split())
        return title
    except Exception:
        return path_str


def format_target_choice(choice_str: str) -> str:
    """Format a promotion target path to a clean, non-revealing human-friendly name."""
    try:
        from pathlib import Path
        stem = Path(choice_str).stem
        disease = "General"
        # Extract disease keyword if present
        parts = choice_str.split("/")
        for part in parts:
            p_lower = part.lower()
            if p_lower in {"hcm", "ckd", "fip", "ibd", "fcv", "diabetes"}:
                disease = p_lower.upper()
                break
        
        is_zh = is_session_chinese()
        if "validated-claims" in stem:
            return f"{disease} Validated Claims" if not is_zh else f"{disease} 已验证声称"
        elif "model-map" in stem:
            return f"{disease} Model Map (Bilingual)" if not is_zh else f"{disease} 双语模型图"
        elif "early-detection" in stem:
            return f"{disease} Early Detection" if not is_zh else f"{disease} 早期筛查与诊断"
        else:
            clean_name = stem.replace("-", " ").title()
            return f"{disease} {clean_name}"
    except Exception:
        return choice_str





DISEASE_GUIDE = {
    "zh": {
        "ckd": {
            "name": "猫慢性肾脏病 (CKD)",
            "queries": [
                ("解释CKD 或 什么是CKD", "获取本地CKD病理机制与分级概述"),
                ("CKD评价指标 或 CKD 疗效评估", "获取临床指标、实验室标志物与试验终点手册"),
                ("CKD 治疗边界 或 猫肾衰治疗限制", "获取磷结合剂等干预措施的标签边界评估")
            ]
        },
        "fip": {
            "name": "猫传染性腹膜炎 (FIP)",
            "queries": [
                ("解释FIP 或 什么是FIP", "获取FIP冠状病毒突变与病理生理学概述"),
                ("FIP怎么识别 或 FIP怎么诊断", "获取诊断标志物、临床分型与鉴别诊断"),
                ("FIP 药效评估 或 FIP 试验终点", "获取临床试验终点与疗效指标设计"),
                ("FIP 治疗证据 或 GS-441524 疗效", "获取抗病毒药物及支持性治疗临床证据")
            ]
        },
        "ibd": {
            "name": "猫炎症性肠病 (IBD)",
            "queries": [
                ("解释IBD 或 什么是IBD", "获取本地IBD慢性肠病及免疫病理学概述"),
                ("IBD和淋巴瘤怎么区分 或 IBD 淋巴瘤鉴别", "获取IBD与低级别消化道淋巴瘤诊断鉴别指南")
            ]
        },
        "hcm": {
            "name": "猫肥厚型心肌病 (HCM)",
            "queries": [
                ("解释HCM 或 什么是HCM", "获取HCM心脏重构、分级及超声筛查指标概述")
            ]
        },
        "diabetes": {
            "name": "猫糖尿病 (Diabetes)",
            "queries": [
                ("解释糖尿病 或 什么是糖尿病", "获取胰岛素敏感性、饮食控制与长期管理概述")
            ]
        },
        "fcv": {
            "name": "猫杯状病毒 (FCV)",
            "queries": [
                ("解释FCV 或 什么是FCV", "获取FCV口炎、急性发热与毒株异质性概述")
            ]
        },
        "obesity": {
            "name": "猫肥胖症 (Obesity)",
            "queries": [
                ("解释肥胖 或 什么是肥胖", "获取体况评分(BCS)、能量限制与减重策略概述")
            ]
        },
        "cancer": {
            "name": "猫肿瘤 (Cancer)",
            "queries": [
                ("解释肿瘤 或 什么是肿瘤", "获取猫恶性肿瘤（乳腺癌、淋巴瘤等）病理分期概述")
            ]
        }
    },
    "en": {
        "ckd": {
            "name": "Feline Chronic Kidney Disease (CKD)",
            "queries": [
                ("What is CKD? or Explain CKD", "Access local CKD overview, staging & pathophysiology"),
                ("CKD trial endpoints or CKD efficacy assessment", "Access clinical endpoints & lab markers handbook"),
                ("CKD treatment boundaries", "Access labeling and intervention boundaries for phosphate binders")
            ]
        },
        "fip": {
            "name": "Feline Infectious Peritonitis (FIP)",
            "queries": [
                ("What is FIP? or Explain FIP", "Access FIP coronavirus mutation & pathology overview"),
                ("How to recognize FIP? or FIP diagnosis", "Access diagnostic markers & differentiation checklist"),
                ("FIP trial endpoints or FIP efficacy evaluation", "Access clinical trial endpoints & design standards"),
                ("FIP treatment evidence or GS-441524 efficacy", "Access antiviral efficacy & supportive care evidence")
            ]
        },
        "ibd": {
            "name": "Feline Inflammatory Bowel Disease (IBD)",
            "queries": [
                ("What is IBD? or Explain IBD", "Access IBD chronic enteropathy & pathology overview"),
                ("How to differentiate IBD and lymphoma", "Access diagnostic differentiation guide for IBD vs. LGA lymphoma")
            ]
        },
        "hcm": {
            "name": "Feline Hypertrophic Cardiomyopathy (HCM)",
            "queries": [
                ("What is HCM? or Explain HCM", "Access HCM staging, remodeling & screening criteria overview")
            ]
        },
        "diabetes": {
            "name": "Feline Diabetes",
            "queries": [
                ("What is diabetes? or Explain diabetes", "Access insulin protocol, diet & glucose curve overview")
            ]
        },
        "fcv": {
            "name": "Feline Calicivirus (FCV)",
            "queries": [
                ("What is FCV? or Explain FCV", "Access FCV stomatitis, acute fever & viral strain diversity")
            ]
        },
        "obesity": {
            "name": "Feline Obesity",
            "queries": [
                ("What is obesity? or Explain obesity", "Access Body Condition Score (BCS) & weight loss strategies")
            ]
        },
        "cancer": {
            "name": "Feline Oncology (Cancer)",
            "queries": [
                ("What is cancer? or Explain cancer", "Access local tumor staging, lymphoma & oncology overview")
            ]
        }
    }
}


def infer_local_disease(question: str) -> str:
    """Small app-local disease detector for free search mode."""
    lowered = question.lower()
    if "ibd" in lowered and any(term in lowered or term in question for term in ["lymphoma", "淋巴瘤"]):
        return "ibd"
    patterns = [
        ("obesity", ["obesity", "obese", "body condition", "weight loss", "肥胖", "超重", "体况"]),
        ("diabetes", ["diabetes", "diabetic", "glucose", "insulin", "糖尿病"]),
        ("ckd", ["ckd", "kidney", "renal", "sdma", "肾", "慢性肾"]),
        ("hcm", ["hcm", "cardiomyopathy", "心肌"]),
        ("fip", ["fip", "传腹", "传染性腹膜炎", "gs-441524", "gs441524", "remdesivir"]),
        ("ibd", ["ibd", "inflammatory bowel", "肠病"]),
        ("fcv", ["fcv", "calicivirus", "杯状"]),
        ("cancer", ["cancer", "tumor", "tumour", "carcinoma", "lymphoma", "肿瘤", "癌", "淋巴瘤"]),
    ]
    for disease, needles in patterns:
        if any(needle in lowered or needle in question for needle in needles):
            return disease
    return "unknown"


def local_search_terms(question: str, disease: str) -> list[str]:
    """Build deterministic terms for no-API retrieval."""
    terms: list[str] = []

    def add(term: str) -> None:
        term = term.strip()
        if len(term) >= 2 and term not in terms:
            terms.append(term)

    # If the question contains Chinese, translate known keywords to English
    if detect_chinese(question):
        translation_map = {
            "肾": ["kidney", "renal"],
            "肾脏": ["kidney", "renal"],
            "肾衰": ["renal failure", "kidney failure"],
            "肌酐": ["creatinine"],
            "蛋白尿": ["proteinuria"],
            "磷": ["phosphorus", "phosphate"],
            "磷结合剂": ["phosphate binder"],
            "糖尿病": ["diabetes", "diabetic"],
            "胰岛素": ["insulin"],
            "血糖": ["glucose", "blood sugar"],
            "传腹": ["FIP", "infectious peritonitis"],
            "腹水": ["effusion", "ascites"],
            "冠状病毒": ["coronavirus"],
            "抗病毒": ["antiviral"],
            "剂量": ["dosage", "dose"],
            "疗效": ["efficacy", "outcome"],
            "药效": ["efficacy", "effect"],
            "临床试验": ["clinical trial"],
            "指标": ["endpoint", "marker"],
            "评估": ["assessment", "evaluation"],
            "评价": ["evaluation", "assessment"],
            "诊断": ["diagnosis", "diagnostic"],
            "识别": ["recognition", "detect"],
            "分级": ["staging", "stage"],
            "肠病": ["IBD", "enteropathy"],
            "淋巴瘤": ["lymphoma"],
            "活检": ["biopsy"],
            "腹泻": ["diarrhea"],
            "呕吐": ["vomiting"],
            "心肌": ["HCM", "cardiomyopathy"],
            "心脏": ["heart", "cardiac"],
            "超声": ["echocardiography", "ultrasound"],
            "杯状": ["FCV", "calicivirus"],
            "口炎": ["stomatitis"],
            "肥胖": ["obesity", "obese"],
            "减重": ["weight loss"],
            "减肥": ["weight loss"],
            "体况": ["body condition"],
            "肿瘤": ["tumor", "cancer"],
            "癌": ["cancer", "carcinoma"],
            "乳腺癌": ["mammary gland tumor", "breast cancer"],
            "终点": ["endpoint"],
        }
        for zh_word, en_words in translation_map.items():
            if zh_word in question:
                for en_w in en_words:
                    add(en_w)

    add(question)
    for token in re.findall(r"[A-Za-z][A-Za-z0-9+/_-]{2,}", question):
        add(token)
    disease_terms = {
        "obesity": ["obesity", "body condition", "weight", "肥胖"],
        "diabetes": ["diabetes", "insulin", "glucose", "糖尿病"],
        "cancer": ["cancer", "tumor", "carcinoma", "肿瘤"],
        "ckd": ["CKD", "endpoint", "creatinine", "proteinuria", "phosphorus", "SDMA"],
        "fip": ["FIP", "diagnosis", "recognition", "GS-441524"],
        "hcm": ["HCM", "echocardiography", "biomarker", "cardiomyopathy"],
        "ibd": ["IBD", "lymphoma", "biopsy", "chronic enteropathy"],
    }
    for term in disease_terms.get(disease, []):
        add(term)
    if "sirna" in question.lower():
        add("siRNA")
    return terms[:8]


def is_local_explanation_question(question: str) -> bool:
    """Detect broad user prompts that need a starter explanation, not only hits."""
    lowered = question.lower().strip()
    explanation_markers = [
        "解释",
        "说明",
        "介绍",
        "什么是",
        "是什么",
        "怎么理解",
        "what is",
        "explain",
        "explanation",
        "overview",
        "summary",
        "summarize",
        "current understanding",
        "researcher know",
        "researchers know",
    ]
    if any(marker in lowered or marker in question for marker in explanation_markers):
        return True
    # Very short disease-name prompts usually mean "give me the entry point."
    compact = re.sub(r"\s+", "", lowered)
    return compact in {"ckd", "fip", "hcm", "ibd", "fcv", "diabetes", "obesity", "cancer"}


def build_ckd_local_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return a plain-language CKD explanation for ordinary users."""
    source_ids = ["src-ckd-001", "src-ckd-003", "src-ckd-004", "src-ckd-010"]
    if chinese:
        answer = (
            "这是本地 vault 的猫慢性肾病解释，不是 API 综合回答；本次没有调用 API。 [inference]\n\n"
            "## 什么是猫慢性肾病（CKD）？\n\n"
            "**猫慢性肾病是指猫的肾脏长期受损，逐渐失去正常功能的疾病。**\n\n"
            "肾脏的工作是过滤血液、排出废物、调节水分和矿物质。当肾脏受损后，这些功能会慢慢下降，废物在体内堆积，引起各种健康问题。\n\n"
            "[source_supported_conclusion: src-ckd-004]\n\n"
            "## 有多常见？\n\n"
            "CKD是老年猫最常见的疾病之一：\n"
            "- **10岁以上**的猫中，约有**30-40%**患有某种程度的肾病\n"
            "- 随着猫的寿命延长，CKD发病率也在增加\n"
            "- 这是老年猫最常见的死亡原因之一\n\n"
            "[source_supported_conclusion: src-ckd-001]\n\n"
            "## 有什么症状？\n\n"
            "| 常见症状 |\n"
            "|----------|\n"
            "| 喝水增多 |\n"
            "| 排尿增多 |\n"
            "| 体重下降 |\n"
            "| 食欲减退 |\n"
            "| 呕吐 |\n"
            "| 精神变差 |\n"
            "| 毛发粗糙 |\n\n"
            "**注意：** 这些症状通常是渐进的，早期可能不明显。如果发现这些症状，请咨询兽医。\n\n"
            "[source_supported_conclusion: src-ckd-004]\n\n"
            "## 如何诊断？\n\n"
            "CKD诊断需要综合多项检查：\n"
            "| 检查项目 | 作用 |\n"
            "|----------|------|\n"
            "| 血液检查 | 评估肾功能（肌酐、尿素氮） |\n"
            "| 尿液检查 | 评估肾脏浓缩能力 |\n"
            "| 血压测量 | 高血压与CKD相关 |\n"
            "| 超声波 | 观察肾脏结构 |\n\n"
            "[source_supported_conclusion: src-ckd-004, src-ckd-010]\n\n"
            "## 可以治疗吗？\n\n"
            "**CKD目前无法治愈，但可以管理。**\n\n"
            "目标是减缓病情进展、控制症状、提高生活质量。\n\n"
            "| 管理措施 | 作用 |\n"
            "|----------|------|\n"
            "| 肾脏处方粮 | 最重要的基础管理 |\n"
            "| 磷结合剂 | 控制血磷 |\n"
            "| 抗高血压药 | 控制血压 |\n"
            "| 补液治疗 | 维持水分平衡 |\n\n"
            "**关键：** 肾脏处方粮是最有证据支持的管理措施。\n\n"
            "[source_supported_conclusion: src-ckd-003, src-ckd-004]\n\n"
            "## 早期发现很重要\n\n"
            "- **7岁以上**的猫应该定期体检\n"
            "- 包括血液和尿液检查\n"
            "- 早期发现可以更早开始管理\n\n"
            "[source_supported_conclusion: src-ckd-004]\n\n"
            "## 研究者视角\n"
            "- 猫 CKD 是一个老年、纤维化主导的复杂疾病。真正科学地“怎么发现”和“判断”它，不能靠单一指标，而要依靠多轴检测。\n"
            "- 核心的评估变量包括：肌酐 (creatinine)、尿比重 (USG)、蛋白尿 (UPCR)、血压 (blood pressure)、磷 (phosphorus) 和 SDMA。\n"
            "- 肾脏专用饮食 (renal diet) 是目前证据最扎实的基础管理方案。\n"
            "- 想要了解更多大众常识，也可以查阅维基百科 (Wikipedia)。\n\n"
            "## 不能说过头的地方\n"
            "- 我们不能把任何当前的治疗或管理方案说成能够“逆转”或“彻底治愈”慢性肾病。管理的目标只是延缓进展。\n"
            "- 这不是兽医诊疗建议，也不替代线下兽医判断。\n\n"
            "## 下一步\n"
            "- 深入阅读 `topics/ckd/mechanism-overview.md` 以了解完整的疾病模型与病理机制。\n"
            "- 在下一步研究中，将候选论文加入 Research Case 的证据区完成证据核实。\n"
        )
    else:
        answer = (
            "This is a local vault CKD explanation, not API synthesis. No API call was made. [inference]\n\n"
            "## What is Feline CKD?\n\n"
            "**Feline chronic kidney disease (CKD) is a condition where a cat's kidneys become damaged over time and gradually lose their normal function.**\n\n"
            "The kidneys filter blood, remove waste, and regulate water and minerals. When damaged, these functions slowly decline, waste builds up in the body, and various health problems arise.\n\n"
            "[source_supported_conclusion: src-ckd-004]\n\n"
            "## How Common Is It?\n\n"
            "CKD is one of the most common diseases in older cats:\n"
            "- About **30-40%** of cats over **10 years old** have some degree of kidney disease\n"
            "- As cats live longer, CKD incidence increases\n"
            "- It's one of the most common causes of death in older cats\n\n"
            "[source_supported_conclusion: src-ckd-001]\n\n"
            "## What Are the Signs?\n\n"
            "| Common Signs |\n"
            "|--------------|\n"
            "| Increased thirst |\n"
            "| Increased urination |\n"
            "| Weight loss |\n"
            "| Decreased appetite |\n"
            "| Vomiting |\n"
            "| Lethargy |\n"
            "| Poor coat condition |\n\n"
            "**Note:** These signs are usually gradual and may be subtle at first. Consult a veterinarian if you notice these signs.\n\n"
            "[source_supported_conclusion: src-ckd-004]\n\n"
            "## How Is It Diagnosed?\n\n"
            "CKD diagnosis requires multiple tests:\n"
            "| Test | Purpose |\n"
            "|------|--------|\n"
            "| Blood tests | Evaluate kidney function (creatinine, BUN) |\n"
            "| Urinalysis | Evaluate concentration ability |\n"
            "| Blood pressure | Hypertension linked to CKD |\n"
            "| Ultrasound | View kidney structure |\n\n"
            "[source_supported_conclusion: src-ckd-004, src-ckd-010]\n\n"
            "## Can It Be Treated?\n\n"
            "**CKD cannot be cured, but it can be managed.**\n\n"
            "Goals are to slow progression, control symptoms, and improve quality of life.\n\n"
            "| Management | Purpose |\n"
            "|------------|--------|\n"
            "| Renal diet | Most important base management |\n"
            "| Phosphate binders | Control blood phosphorus |\n"
            "| Blood pressure medication | Control hypertension |\n"
            "| Fluid therapy | Maintain hydration |\n\n"
            "**Key point:** Renal diet has the strongest evidence support.\n\n"
            "[source_supported_conclusion: src-ckd-003, src-ckd-004]\n\n"
            "## Early Detection Matters\n\n"
            "- Cats **over 7 years old** should have regular checkups\n"
            "- Including blood and urine tests\n"
            "- Early detection allows earlier management\n\n"
            "[source_supported_conclusion: src-ckd-004]\n\n"
            "## Researcher Lens\n"
            "- To analyze feline chronic kidney disease as a durable disease model, we must study How It Is Recognized through specific evidence layers.\n"
            "- Key diagnostic markers include creatinine, USG, UPCR (proteinuria), blood pressure, phosphorus, and SDMA. These act as essential prognostic markers and trial endpoints.\n"
            "- Renal diet remains the bedrock of supportive evidence. General entries can be found on Wikipedia.\n\n"
            "## Do Not Overstate\n"
            "- Do Not Overstate the efficacy of therapy without considering pathological subtypes. Feline CKD cannot be cured.\n\n"
            "## Next Step\n"
            "- Read `topics/ckd/mechanism-overview.md` for mechanisms, and `topics/ckd/endpoint-handbook.md` for trial endpoints.\n"
        )
    return answer, source_ids


def build_ckd_endpoint_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return a deterministic CKD endpoint starter answer."""
    source_ids = ["src-ckd-002", "src-ckd-004", "src-ckd-010", "src-ckd-013", "src-ckd-015"]
    if chinese:
        answer = (
            "这是本地 vault 的 CKD endpoint 解释，不是 API 综合回答；本次没有调用 API。 [llm_inference]\n\n"
            "## 直接回答\n"
            "猫 CKD 药效评价不能只靠一个指标。这个库当前把 creatinine、USG、UPCR/蛋白尿、收缩压、phosphorus、SDMA 放在第一波可用 endpoint 短名单里；"
            "它们分别覆盖肾功能、尿浓缩能力、蛋白尿/肾小球压力、血压负担、矿物代谢和早期检测压力。"
            " [source_supported_conclusion: src-ckd-002, src-ckd-004, src-ckd-010]\n\n"
            "## 为什么这样分\n"
            "- proteinuria、phosphorus 和 blood pressure 不只是记录项，也能连接病理结构、预后和管理重点。 [source_supported_conclusion: src-ckd-010, src-ckd-015]\n"
            "- 如果问题是治疗试验，endpoint 还应该包含疾病进程和 patient-level burden，不能只看实验室指标。 [source_supported_conclusion: src-ckd-013]\n"
            "- 当前仍不能把任何单一 endpoint 写成所有 CKD 药效评价的最终胜者。 [llm_inference]\n\n"
            "## 下一步\n"
            "读 `topics/ckd/endpoint-handbook.md`，再用 `topics/ckd/outcome-architecture` 相关 memo 检查 trial endpoint 是否过窄。"
        )
    else:
        answer = (
            "This is a local CKD endpoint explanation, not API synthesis. No API call was made. [llm_inference]\n\n"
            "## Direct Answer\n"
            "Feline CKD efficacy evaluation should not rely on one marker. The vault's first-wave endpoint shortlist is creatinine, USG, UPCR/proteinuria, systolic blood pressure, phosphorus, and SDMA. "
            "These cover renal function, urine concentrating ability, proteinuric or glomerular pressure, blood-pressure burden, mineral metabolism, and early-detection pressure. "
            "[source_supported_conclusion: src-ckd-002, src-ckd-004, src-ckd-010]\n\n"
            "## Why This Split Matters\n"
            "- Proteinuria, phosphorus, and blood pressure connect pathology, prognosis, and management priorities. [source_supported_conclusion: src-ckd-010, src-ckd-015]\n"
            "- Treatment-trial endpoint architecture should include disease-course and patient-level burden, not only laboratory markers. [source_supported_conclusion: src-ckd-013]\n"
            "- The current vault does not support naming one universal winning endpoint for all CKD efficacy questions. [llm_inference]\n\n"
            "## Next Step\n"
            "Read `topics/ckd/endpoint-handbook.md`, then check the CKD outcome architecture memo before designing a trial endpoint set."
        )
    return answer, source_ids


def build_fip_recognition_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return a plain-language FIP recognition answer for ordinary users."""
    source_ids = ["src-fip-003", "src-fip-006", "src-fip-015", "src-fip-005"]
    if chinese:
        answer = (
            "这是本地 vault 的 FIP 识别解释，不是 API 综合回答；本次没有调用 API。 [inference]\n\n"
            "## 如何识别FIP？\n\n"
            "### 🚨 需要立即就医的情况\n"
            "| 症状组合 | 说明 |\n"
            "|----------|------|\n"
            "| 肚子变大 + 精神差 | 可能是腹水，湿性FIP的典型表现 |\n"
            "| 反复发烧 + 消瘦 | 吃退烧药也不管用的发烧 |\n"
            "| 眼睛异常 + 发烧 | 眼睛浑浊、颜色改变 |\n"
            "| 走路不稳 + 发烧 | 可能是神经型FIP |\n\n"
            "[source_supported_conclusion: src-fip-006]\n\n"
            "### 高风险猫咪\n"
            "- **年龄**：1岁以下的幼猫风险最高\n"
            "- **来源**：猫舍、收容所、多猫家庭\n"
            "- **压力**：刚搬家、刚到新家、刚做手术\n\n"
            "[source_supported_conclusion: src-fip-003]\n\n"
            "### 早期症状\n"
            "- 食欲下降，以前爱吃现在不想吃\n"
            "- 精神变差，不爱玩，总是睡觉\n"
            "- 体重下降，明显变瘦\n"
            "- 发烧，摸起来比平时热\n\n"
            "[source_supported_conclusion: src-fip-015]\n\n"
            "### 重要提示\n"
            "- 我们不能靠一个症状或单一的诊断进行判断。FIP 诊断需要结合湿性 (effusive) 或干性 (non-effusive) 表现进行多轴评估。\n"
            "- 这些症状也可能是其他疾病，需要医生综合判断\n"
            "- FIP现在有药可治（GS-441524等），早发现早治疗效果更好\n"
            "- 如果怀疑FIP，请尽快就医\n\n"
            "## 下一步\n"
            "详细了解请阅读 `topics/fip/fip-warning-signs.md` 或 `topics/fip/what-is-fip.md`。"
        )
    else:
        answer = (
            "This is a local FIP recognition explanation, not API synthesis. No API call was made. [inference]\n\n"
            "## How to Recognize FIP?\n\n"
            "### 🚨 Seek Immediate Veterinary Care If:\n"
            "| Symptom Combination | What It Means |\n"
            "|---------------------|---------------|\n"
            "| Swollen belly + lethargy | Possible fluid buildup (wet FIP) |\n"
            "| Persistent fever + weight loss | Fever that doesn't respond to medication |\n"
            "| Eye changes + fever | Cloudy eyes, color changes |\n"
            "| Unsteady walking + fever | Possible neurological FIP |\n\n"
            "[source_supported_conclusion: src-fip-006]\n\n"
            "### High-Risk Cats\n"
            "- **Age**: Kittens under 1 year are at highest risk\n"
            "- **Environment**: Catteries, shelters, multi-cat households\n"
            "- **Stress**: Recent move, new home, recent surgery\n\n"
            "[source_supported_conclusion: src-fip-003]\n\n"
            "### Early Warning Signs\n"
            "- Loss of appetite\n"
            "- Decreased energy, sleeping more\n"
            "- Weight loss despite eating\n"
            "- Fever (feels warmer than usual)\n\n"
            "[source_supported_conclusion: src-fip-015]\n\n"
            "### Important Notes\n"
            "- FIP diagnosis cannot rely on a single one-symptom or one-test result. Broad evaluation must differentiate effusive and non-effusive forms.\n"
            "- These symptoms can also indicate other diseases; a vet must evaluate\n"
            "- FIP is now treatable (GS-441524 and similar drugs); early detection improves outcomes\n"
            "- If you suspect FIP, see a vet immediately\n\n"
            "## Next Step\n"
            "For more details, read `topics/fip/fip-warning-signs.md` or `topics/fip/what-is-fip.md`."
        )
    return answer, source_ids


def build_fip_local_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return a plain-language FIP overview for ordinary users."""
    source_ids = ["src-fip-003", "src-fip-005", "src-fip-006", "src-fip-015"]
    if chinese:
        answer = (
            "这是本地 vault 的 FIP 概览解释，不是 API 综合回答；本次没有调用 API。 [inference]\n\n"
            "## 什么是FIP？\n\n"
            "**FIP（猫传染性腹膜炎）是一种由冠状病毒变异引起的猫的严重疾病。**\n\n"
            "大多数猫感染冠状病毒后只会轻微腹泻或没有症状，但在少数猫体内，病毒会发生变异，引发全身性的严重炎症反应，这就是FIP。\n\n"
            "[source_supported_conclusion: src-fip-003]\n\n"
            "## 哪些猫容易得FIP？\n\n"
            "| 高风险因素 | 说明 |\n"
            "|-----------|------|\n"
            "| 年龄 | 1岁以下的幼猫风险最高 |\n"
            "| 环境 | 多猫家庭、猫舍、收容所 |\n"
            "| 压力 | 刚到新家、手术后、其他疾病 |\n\n"
            "[source_supported_conclusion: src-fip-005]\n\n"
            "## FIP有什么症状？\n\n"
            "### 湿性FIP（腹水型）\n"
            "- 肚子变大，像气球一样鼓起来\n"
            "- 呼吸困难\n"
            "- 精神差、食欲下降\n"
            "- 反复发烧\n\n"
            "### 干性FIP（非腹水型）\n"
            "- 眼睛问题：浑浊、颜色改变、怕光\n"
            "- 神经症状：走路不稳、抽搐、行为异常\n"
            "- 持续发烧、消瘦\n\n"
            "[source_supported_conclusion: src-fip-006]\n\n"
            "## FIP能治吗？\n\n"
            "**是的，现在有药物可以治疗FIP。**\n"
            "- GS-441524 和类似药物已经救活了很多FIP猫\n"
            "- 治疗需要持续84天（12周）\n"
            "- 早发现早治疗效果更好\n\n"
            "**重要提示：** 治疗需要在兽医指导下进行。\n\n"
            "## 下一步\n"
            "详细了解请阅读 `topics/fip/what-is-fip.md`、`topics/fip/fip-warning-signs.md` 以及 IBD / FIP 治疗证据比较备忘录。\n\n"
            "## 研究者视角\n"
            "- FIP 诊断极具挑战，具有诊断不确定性。不能仅凭单一的诊断指标进行裁决。\n"
            "- 从研究者视角来看，FIP 应区分为渗出型（湿性，effusive）与非渗出型（干性，non-effusive），包括神经型（neurologic）和眼部型（ocular）的分支。\n"
            "- GS-441524 和 remdesivir 等抗病毒药物的出现带来了抗病毒时代的药效行动力，重塑了治疗时机的选择。\n\n"
            "## 不能说过头的地方\n"
            "- 虽然抗病毒药物疗效显著，但我们不能说过头，也不宜把所有抗病毒证据合并成一个不分病型、不分随访耐久性的简单疗效结论。\n"
            "- 这不是兽医诊疗建议，也不替代线下兽医判断。"
        )
    else:
        answer = (
            "This is a local FIP overview, not API synthesis. No API call was made. [inference]\n\n"
            "## What is FIP?\n\n"
            "**FIP (Feline Infectious Peritonitis) is a serious disease caused by a mutated coronavirus.**\n\n"
            "Most cats infected with coronavirus only have mild diarrhea or no symptoms. But in some cats, the virus mutates and causes a severe inflammatory response throughout the body — this is FIP.\n\n"
            "[source_supported_conclusion: src-fip-003]\n\n"
            "## Which Cats Are at Risk?\n\n"
            "| Risk Factor | Details |\n"
            "|-------------|--------|\n"
            "| Age | Kittens under 1 year are at highest risk |\n"
            "| Environment | Multi-cat households, catteries, shelters |\n"
            "| Stress | New home, post-surgery, other illness |\n\n"
            "[source_supported_conclusion: src-fip-005]\n\n"
            "## What Are the Symptoms?\n\n"
            "### Wet FIP (Effusive)\n"
            "- Swollen belly (fluid buildup)\n"
            "- Difficulty breathing\n"
            "- Lethargy, loss of appetite\n"
            "- Persistent fever\n\n"
            "### Dry FIP (Non-Effusive)\n"
            "- Eye problems: cloudiness, color changes, light sensitivity\n"
            "- Neurological signs: unsteady walking, seizures, behavior changes\n"
            "- Persistent fever, weight loss\n\n"
            "[source_supported_conclusion: src-fip-006]\n\n"
            "## Can FIP Be Treated?\n\n"
            "**Yes, there are now drugs that can treat FIP.**\n\n"
            "- GS-441524 and similar antiviral agents like remdesivir have saved many cats with FIP.\n"
            "- Treatment typically lasts 84 days (12 weeks).\n"
            "- Early detection and treatment improve outcomes.\n\n"
            "**Important:** Treatment must be supervised by a veterinarian.\n\n"
            "## Researcher Lens\n"
            "- FIP presents a complex decision model and disease form shaped by risk, clinical presentation, and testing options.\n"
            "- We must address diagnostic uncertainty and understand diagnostic-test boundaries across effusive and non-effusive forms, including neurologic and ocular involvements.\n"
            "- Adequate treatment timing and antiviral-era actionability of GS-441524 or remdesivir are crucial.\n\n"
            "## Do Not Overstate\n"
            "- Do Not Overstate the efficacy of therapy without considering persistent carrier status, follow-up durability, or pathological subtypes.\n\n"
            "## Next Step\n"
            "- Read `topics/fip/what-is-fip.md` or `topics/fip/fip-warning-signs.md` for complete guidelines.\n"
        )
    return answer, source_ids


def build_fip_endpoint_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return FIP endpoint hierarchy for research queries - structured, verifiable content."""
    source_ids = [
        "src-fip-002", "src-fip-003", "src-fip-006", "src-fip-010",
        "src-fip-013", "src-fip-015", "src-fip-016", "src-fip-019",
        "src-fip-022", "src-fip-023", "src-fip-024"
    ]
    if chinese:
        answer = (
            "这是本地 vault 的 FIP 药效评价/诊断指标结构化回答。 [source_supported_conclusion]\n\n"
            "## Key-Claim Traceability\n\n"
            "| ID | Claim | Level | Sources | Boundary |\n"
            "|---|---|---|---|---|\n"
            "| FE1 | FIP endpoint logic 应该是分层支持，不是单一 marker 确诊 | B | src-fip-003, src-fip-006, src-fip-015 | 诊断支持框架，非最终诊断 |\n"
            "| FE2 | 临床病理模式和疾病形态是当前最强的操作性支持 endpoint | B | src-fip-006, src-fip-015 | 建立怀疑，非确诊 |\n"
            "| FE3 | 急性期、免疫球蛋白、渗出型免疫背景属于较低层级的背景支持 | B | src-fip-002, src-fip-007 | 背景支持，非现代主导 endpoint |\n"
            "| FE4 | 突变相关检测只有在同时理解其效用和局限时才有用 | B | src-fip-010, src-fip-022 | 有限度强化，非闭合 |\n"
            "| FE5 | CSF 病毒检测是神经/眼科分支的专门支持（强阳性价值，弱排除价值） | B | src-fip-023 | 分支特异性支持 |\n"
            "| FE6 | 治疗反应、缓解、复发、存活是随访结局，不是首诊 endpoint | C | src-fip-013, src-fip-016, src-fip-019, src-fip-024 | 治疗监测分支 |\n\n"
            "## Endpoint Hierarchy\n\n"
            "1. **临床病理模式与疾病形态** — 主导操作层\n"
            "   - 将非特异性担忧转为结构化 FIP workup\n"
            "   - 区分湿性、干性、神经型\n"
            "   - Sources: src-fip-003, src-fip-006, src-fip-015\n\n"
            "2. **急性期蛋白、免疫球蛋白、渗出型免疫背景** — 二级支持层\n"
            "   - 丰富 endpoint 图谱，但不应主导现代 workup\n"
            "   - Sources: src-fip-002, src-fip-007\n\n"
            "3. **血清学历史** — 背景层\n"
            "   - 暴露相关背景，非现代诊断权威\n"
            "   - Source: src-fip-011\n\n"
            "4. **突变相关检测** — 有限强化层\n"
            "   - 只有将效用和局限放在一起读才有意义\n"
            "   - 应强化已有怀疑，而非替代识别架构\n"
            "   - Sources: src-fip-010, src-fip-022\n\n"
            "5. **CSF 病毒检测（神经/眼科分支）** — 分支特异层\n"
            "   - 特异性 100%, PPV 100%, 总体敏感性 42.1%, NPV 57.7%\n"
            "   - 神经/眼科亚组敏感性 85.7%\n"
            "   - Source: src-fip-023\n\n"
            "6. **治疗结局 endpoints** — 随访层\n"
            "   - 反应、缓解、复发、存活\n"
            "   - 属于治疗监测，非首诊\n"
            "   - Sources: src-fip-013, src-fip-016, src-fip-019, src-fip-024\n\n"
            "## 核心要点\n\n"
            "最安全的 FIP endpoint 架构是**有序复合支持**：临床病理和疾病形态主导；\n"
            "较低的实验室和分子通道强化但不决定；CSF 支持属于神经/眼科分支；\n"
            "治疗结局属于随访而非诊断。\n\n"
            "## 如何验证\n\n"
            "- 本回答基于 FIP endpoint-handbook.md 的 Key-Claim 表格\n"
            "- 查看详细引用：打开 `raw/papers/src-fip-XXX.md`\n"
            "- 完整页面：`topics/fip/endpoint-handbook.md`"
        )
    else:
        answer = (
            "This is a local vault structured answer for FIP endpoint/evaluation queries. [source_supported_conclusion]\n\n"
            "## Key-Claim Traceability\n\n"
            "| ID | Claim | Level | Sources | Boundary |\n"
            "|---|---|---|---|---|\n"
            "| FE1 | FIP endpoint logic should be layered support, not one-marker certainty | B | src-fip-003, src-fip-006, src-fip-015 | diagnostic support frame, not final diagnosis |\n"
            "| FE2 | Clinicopathologic pattern and disease form are the strongest operational endpoints | B | src-fip-006, src-fip-015 | suspicion-building, not definitive proof |\n"
            "| FE3 | Acute-phase, immunoglobulin, effusive immune context belong in lower background support | B | src-fip-002, src-fip-007 | supportive context, not modern lead endpoints |\n"
            "| FE4 | Mutation-related assays useful only when utility and limitation held together | B | src-fip-010, src-fip-022 | bounded strengthening, not closure |\n"
            "| FE5 | CSF viral detection is specialized neurologic/ocular support (strong positive, weak rule-out) | B | src-fip-023 | branch-specific support |\n"
            "| FE6 | Treatment response, remission, relapse, survival are follow-up outcomes, not first-pass diagnostic endpoints | C | src-fip-013, src-fip-016, src-fip-019, src-fip-024 | treatment-monitoring branch |\n\n"
            "## Endpoint Hierarchy\n\n"
            "1. **Clinicopathologic Pattern & Disease Form** — Lead operational layer\n"
            "   - Turns non-specific concern into structured FIP workup\n"
            "   - Distinguishes wet, dry, neurologic forms\n"
            "   - Sources: src-fip-003, src-fip-006, src-fip-015\n\n"
            "2. **Acute-Phase, Immunoglobulin, Effusive Immune Context** — Second-tier support\n"
            "   - Enriches endpoint map but should not lead modern workup\n"
            "   - Sources: src-fip-002, src-fip-007\n\n"
            "3. **Historical Serology** — Background layer\n"
            "   - Exposure-linked background, not modern diagnostic authority\n"
            "   - Source: src-fip-011\n\n"
            "4. **Mutation-Related Assays** — Bounded strengthening\n"
            "   - Only meaningful when utility and limitation read together\n"
            "   - Should strengthen existing suspicion, not replace recognition architecture\n"
            "   - Sources: src-fip-010, src-fip-022\n\n"
            "5. **CSF Viral Detection (Neurologic/Ocular)** — Branch-specific layer\n"
            "   - Specificity 100%, PPV 100%, overall sensitivity 42.1%, NPV 57.7%\n"
            "   - Neurologic/ocular subgroup sensitivity 85.7%\n"
            "   - Source: src-fip-023\n\n"
            "6. **Treatment Outcome Endpoints** — Follow-up layer\n"
            "   - Response, remission, relapse, survival\n"
            "   - Belongs to treatment monitoring, not initial diagnosis\n"
            "   - Sources: src-fip-013, src-fip-016, src-fip-019, src-fip-024\n\n"
            "## Core Takeaway\n\n"
            "The safest FIP endpoint architecture is **ordered composite support**: clinicopathology and disease form lead;\n"
            "lower laboratory and molecular channels strengthen but do not settle; CSF support belongs to neurologic/ocular branch;\n"
            "treatment outcomes belong to follow-up rather than diagnosis.\n\n"
            "## How to Verify\n\n"
            "- This answer is based on FIP endpoint-handbook.md Key-Claim tables\n"
            "- View detailed citations: open `raw/papers/src-fip-XXX.md`\n"
            "- Full page: `topics/fip/endpoint-handbook.md`"
        )
    return answer, source_ids


def build_fip_treatment_evidence_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return FIP treatment evidence for research queries - structured, verifiable content."""
    source_ids = [
        "src-fip-003", "src-fip-013", "src-fip-016",
        "src-fip-017", "src-fip-019", "src-fip-024"
    ]
    if chinese:
        answer = (
            "这是本地 vault 的 FIP 治疗证据结构化回答。 [source_supported_conclusion]\n\n"
            "## Key-Claim Traceability\n\n"
            "| ID | Claim | Level | Sources | Boundary |\n"
            "|---|---|---|---|---|\n"
            "| FT1 | FIP 治疗在 GS/remdesivir 时代已实质性转变 | B | src-fip-003, src-fip-013, src-fip-016, src-fip-019 | 治疗转变，非通用治愈 |\n"
            "| FT2 | 神经型救治和方案逻辑证据不应合并到基线 GS 疗效中 | B | src-fip-017, src-fip-019, src-fip-024 | 分支分离 |\n"
            "| FT3 | 转化应保持在诊断和监管确定性边界之下 | C | src-fip-003 | 非决策级 |\n\n"
            "## Treatment Evidence Layers\n\n"
            "### Layer 1: 基线 GS-441524 疗效\n"
            "**核心来源**: src-fip-016\n"
            "- 31 只猫入组，26 只渗出型/干转湿型，5 只非渗出型\n"
            "- **未纳入**严重神经型和眼型\n"
            "- 24 只猫在发表时保持健康\n"
            "- 最佳剂量：4.0 mg/kg SC 每 24 小时，至少 12 周\n"
            "- **边界**：支持基线疗效，不能推广到严重神经/眼型\n\n"
            "### Layer 2: 长期缓解随访\n"
            "**核心来源**: src-fip-013\n"
            "- 口服 GS-441524 治疗后的长期缓解随访\n"
            "- 支持「治疗后持久性」层\n\n"
            "### Layer 3: 联合治疗方案\n"
            "**核心来源**: src-fip-019\n"
            "- Remdesivir + GS-441524 联合治疗\n"
            "- 覆盖渗出型和非渗出型\n"
            "- 支持「真实世界治疗方案」层\n\n"
            "### Layer 4: 神经型救治\n"
            "**核心来源**: src-fip-017, src-fip-024\n"
            "- 神经型 FIP 专门的抗病毒治疗\n"
            "- 支持「高复杂度治疗」分支\n"
            "- **边界**：是治疗类别转变，不是基线抗病毒的强化版\n\n"
            "## 核心要点\n\n"
            "1. GS-441524 已转变 FIP 治疗，但不是「无摩擦治愈」\n"
            "2. 早期死亡、复发、再治疗、剂量调整都是证据架构的一部分\n"
            "3. 神经型救治是独立分支，不能混入基线疗效\n"
            "4. 治疗转变不能擦除诊断仍然是支持性和复合性的事实\n\n"
            "## 如何验证\n\n"
            "- 基线治疗锚点：`raw/papers/src-fip-016.md`\n"
            "- 神经型治疗：`raw/papers/src-fip-017.md`, `src-fip-024.md`\n"
            "- 完整页面：`topics/fip/translation-brief.md`"
        )
    else:
        answer = (
            "This is a local vault structured answer for FIP treatment evidence. [source_supported_conclusion]\n\n"
            "## Key-Claim Traceability\n\n"
            "| ID | Claim | Level | Sources | Boundary |\n"
            "|---|---|---|---|---|\n"
            "| FT1 | FIP treatment materially transformed in GS/remdesivir era | B | src-fip-003, src-fip-013, src-fip-016, src-fip-019 | treatment transformation, not universal cure |\n"
            "| FT2 | Neurologic rescue and package-logic evidence should not collapse into baseline GS efficacy | B | src-fip-017, src-fip-019, src-fip-024 | branch separation |\n"
            "| FT3 | Translation should remain below diagnostic and regulatory certainty boundaries | C | src-fip-003 | not decision-grade |\n\n"
            "## Treatment Evidence Layers\n\n"
            "### Layer 1: Baseline GS-441524 Efficacy\n"
            "**Core source**: src-fip-016\n"
            "- 31 cats enrolled, 26 effusive/dry-to-effusive, 5 non-effusive\n"
            "- Severe neurologic and ocular cases **not recruited**\n"
            "- 24 cats remained healthy at publication\n"
            "- Optimal dosage: 4.0 mg/kg SC every 24 hours for at least 12 weeks\n"
            "- **Boundary**: supports baseline efficacy, cannot extend to severe neurologic/ocular\n\n"
            "### Layer 2: Long-term Remission Follow-up\n"
            "**Core source**: src-fip-013\n"
            "- Long-term remission follow-up after oral GS-441524\n"
            "- Supports \"post-treatment durability\" layer\n\n"
            "### Layer 3: Combination Treatment Package\n"
            "**Core source**: src-fip-019\n"
            "- Remdesivir + GS-441524 combination treatment\n"
            "- Covers effusive and non-effusive\n"
            "- Supports \"real-world treatment package\" layer\n\n"
            "### Layer 4: Neurologic Rescue\n"
            "**Core sources**: src-fip-017, src-fip-024\n"
            "- Dedicated antiviral treatment for neurologic FIP\n"
            "- Supports \"high-complexity treatment\" branch\n"
            "- **Boundary**: is a treatment-category shift, not intensified baseline antiviral\n\n"
            "## Core Takeaway\n\n"
            "1. GS-441524 transformed FIP treatment, but not \"frictionless cure\"\n"
            "2. Early deaths, relapse, retreatment, dose escalation are part of evidence architecture\n"
            "3. Neurologic rescue is distinct branch, should not merge into baseline efficacy\n"
            "4. Treatment transformation should not erase that diagnosis remains supportive and composite\n\n"
            "## How to Verify\n\n"
            "- Baseline treatment anchor: `raw/papers/src-fip-016.md`\n"
            "- Neurologic treatment: `raw/papers/src-fip-017.md`, `src-fip-024.md`\n"
            "- Full page: `topics/fip/translation-brief.md`"
        )
    return answer, source_ids


def build_hcm_local_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return a plain-language HCM explanation for ordinary users."""
    source_ids = ["src-hcm-001", "src-hcm-008", "src-hcm-009", "src-hcm-010"]
    if chinese:
        answer = (
            "这是本地 vault 的猫心肌病解释，不是 API 综合回答；本次没有调用 API。 [inference]\n\n"
            "## 什么是猫HCM？\n\n"
            "**HCM（肥厚型心肌病）是猫最常见的心脏病，心肌异常增厚，影响心脏正常工作。**\n\n"
            "心肌变厚后，心室空间变小，心脏充血和泵血能力下降，可能导致心力衰竭或血栓。\n\n"
            "[source_supported_conclusion: src-hcm-001]\n\n"
            "## 有多常见？\n\n"
            "- HCM是猫最常见的心脏病\n"
            "- 某些品种（缅因猫、布偶猫等）风险更高\n"
            "- 可能是遗传性的\n"
            "- 很多猫没有明显症状\n\n"
            "[source_supported_conclusion: src-hcm-001]\n\n"
            "## 有什么症状？\n\n"
            "**早期可能没有症状。** 晚期可能出现：\n\n"
            "| 症状 |\n"
            "|------|\n"
            "| 呼吸急促或困难 |\n"
            "| 张口呼吸 |\n"
            "| 精神变差 |\n"
            "| 食欲下降 |\n"
            "| 后腿突然瘫痪（血栓） |\n"
            "| 突然死亡 |\n\n"
            "**紧急情况：** 如果猫突然后腿无力、呼吸困难，立即就医！这可能是血栓。\n\n"
            "[source_supported_conclusion: src-hcm-001, src-hcm-008]\n\n"
            "## 如何诊断？\n\n"
            "| 检查 | 作用 |\n"
            "|------|------|\n"
            "| 心脏超声 | 诊断金标准，测量心肌厚度 |\n"
            "| 听诊 | 听心杂音（但很多HCM猫没有杂音） |\n"
            "| 心电图 | 检查心律 |\n"
            "| 胸片 | 检查肺部积液 |\n"
            "| 血液检查 | 心脏标志物（可辅助筛查） |\n\n"
            "**注意：** 心脏超声是确诊的最可靠方法。\n\n"
            "[source_supported_conclusion: src-hcm-009, src-hcm-010]\n\n"
            "## 可以治疗吗？\n\n"
            "**HCM目前无法治愈，但可以管理：**\n\n"
            "| 治疗目标 | 方式 |\n"
            "|----------|------|\n"
            "| 减轻心脏负担 | 药物控制心率 |\n"
            "| 预防血栓 | 抗凝药物 |\n"
            "| 控制心衰 | 利尿剂等 |\n"
            "| 定期监测 | 复查超声 |\n\n"
            "[source_supported_conclusion: src-hcm-008]\n\n"
            "## 高风险品种\n\n"
            "| 品种 |\n"
            "|------|\n"
            "| 缅因猫 |\n"
            "| 布偶猫 |\n"
            "| 英短 |\n"
            "| 波斯猫 |\n\n"
            "这些品种建议定期筛查。\n\n"
            "[source_supported_conclusion: src-hcm-001]\n\n"
            "## 研究者视角\n"
            "- 从研究者视角来看，肥厚型心肌病（HCM）的诊断关键在于其结构性表型定义（structural phenotype definition）。\n"
            "- 诊断不仅依赖心脏超声（echocardiography）来判断心肌重构（remodeling），还需要结合心脏标志物（biomarker/biomarkers）和基因型（genotype）进行多维分析。这就是为什么危险的病理生理学原因。\n"
            "- 在证据深度上，目前临床上没有单一的筛查工具可以完全替代多轴心脏评估，AI screening 是有益的前沿探索。\n\n"
            "## 不能说过头的地方\n"
            "- 我们不能或不应把任何局部的治疗证据直接写成最终的干预层级（intervention hierarchy）。\n"
            "- 这不是兽医诊疗建议，也不替代线下兽医判断。\n\n"
            "## 下一步\n"
            "- 详细了解请阅读 `topics/hcm/synthesis-index.md` 或 HCM treatment-evidence memo，以获取关于治疗证据的进一步指导。\n"
        )
    else:
        answer = (
            "This is a local vault HCM explanation, not API synthesis. No API call was made. [inference]\n\n"
            "## What is Feline HCM?\n\n"
            "**HCM (Hypertrophic Cardiomyopathy) is the most common heart disease in cats. The heart muscle becomes abnormally thick, affecting how the heart works.**\n\n"
            "When the muscle thickens, the heart chamber becomes smaller, reducing filling and pumping ability. This can lead to heart failure or blood clots.\n\n"
            "[source_supported_conclusion: src-hcm-001]\n\n"
            "## How Common Is It?\n\n"
            "- HCM is the most common heart disease in cats\n"
            "- Some breeds (Maine Coon, Ragdoll, etc.) are at higher risk\n"
            "- Can be hereditary\n"
            "- Many cats show no obvious symptoms\n\n"
            "[source_supported_conclusion: src-hcm-001]\n\n"
            "## What Are the Signs?\n\n"
            "**Early stages may have no symptoms.** Later signs include:\n\n"
            "| Signs |\n"
            "|-------|\n"
            "| Rapid or difficult breathing |\n"
            "| Open-mouth breathing |\n"
            "| Lethargy |\n"
            "| Decreased appetite |\n"
            "| Sudden hind leg paralysis (blood clot) |\n"
            "| Sudden death |\n\n"
            "**Emergency:** If your cat suddenly can't use back legs or has breathing difficulty, seek immediate vet care! This may be a blood clot.\n\n"
            "[source_supported_conclusion: src-hcm-001, src-hcm-008]\n\n"
            "## How Is It Diagnosed?\n\n"
            "| Test | Purpose |\n"
            "|------|--------|\n"
            "| Echocardiogram | Gold standard, measures heart muscle thickness |\n"
            "| Listening | Heart murmur (but many HCM cats have no murmur) |\n"
            "| ECG | Check heart rhythm |\n"
            "| X-ray | Check for fluid in lungs |\n"
            "| Blood tests | Heart biomarkers (can help screen) |\n\n"
            "**Note:** Echocardiogram is the most reliable method for diagnosis.\n\n"
            "[source_supported_conclusion: src-hcm-009, src-hcm-010]\n\n"
            "## Can It Be Treated?\n\n"
            "**HCM cannot be cured, but can be managed:**\n\n"
            "| Goal | Approach |\n"
            "|------|----------|\n"
            "| Reduce heart workload | Medications to control heart rate |\n"
            "| Prevent blood clots | Anti-clotting medication |\n"
            "| Control heart failure | Diuretics, etc. |\n"
            "| Regular monitoring | Follow-up echocardiograms |\n\n"
            "[source_supported_conclusion: src-hcm-008]\n\n"
            "## High-Risk Breeds\n\n"
            "| Breed |\n"
            "|-------|\n"
            "| Maine Coon |\n"
            "| Ragdoll |\n"
            "| British Shorthair |\n"
            "| Persian |\n\n"
            "Regular screening is recommended for these breeds.\n\n"
            "[source_supported_conclusion: src-hcm-001]\n\n"
            "## Researcher Lens\n"
            "- To understand feline HCM cardiomyopathy, we must evaluate the structural phenotype and phenotype definition via echocardiography.\n"
            "- Risk assessment shows why it is risky due to myocardial remodeling. We should utilize biomarkers, genotype testing, and AI screening.\n"
            "- In terms of evidence-depth, single parameters should not define the final diagnosis.\n\n"
            "## Do Not Overstate\n"
            "- Do not present local treatment evidence as the complete intervention hierarchy. We should not suggest a single marker replaces comprehensive workup.\n\n"
            "## Next Step\n"
            "- Read `topics/hcm/synthesis-index.md` or the HCM treatment-evidence memo for details.\n"
        )
    return answer, source_ids


def build_ibd_lymphoma_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return a deterministic IBD-versus-lymphoma starter answer."""
    source_ids = [
        "src-ibd-003",
        "src-ibd-010",
        "src-ibd-011",
        "src-ibd-014",
        "src-ibd-015",
        "src-ibd-016",
        "src-ibd-019",
        "src-ibd-021",
    ]
    if chinese:
        answer = (
            "这是本地 vault 的 IBD/淋巴瘤鉴别解释，不是 API 综合回答；本次没有调用 API。 [llm_inference]\n\n"
            "## 直接解释\n"
            "猫 IBD 与小细胞/低级别 alimentary lymphoma 的区分，不应该被写成一个单项 marker 问题。这个库把它当作 diagnostic boundary 和 workup sequencing 问题：慢性肠病怀疑、影像压力、活检部位策略、整合病理，再到有限 marker 支持。"
            " [source_supported_conclusion: src-ibd-003, src-ibd-010, src-ibd-011, src-ibd-015, src-ibd-016, src-ibd-019]\n\n"
            "## 研究者视角\n"
            "- 这个问题的研究核心是 boundary compression：IBD、chronic enteropathy、food-response 和 small-cell lymphoma 会在症状、影像、病理和治疗反应上互相挤压。"
            " [source_supported_conclusion: src-ibd-003, src-ibd-010, src-ibd-011, src-ibd-014]\n"
            "- 最容易误判的地方，是把 marker、影像、biopsy site、病理整合和 diet response 当作同一级别证据。"
            " [source_supported_conclusion: src-ibd-010, src-ibd-011, src-ibd-015, src-ibd-016, src-ibd-021]\n\n"
            "## 关键边界\n"
            "- muscularis thickening 更偏 lymphoma pressure，ileal sampling 可能改变诊断，所以采样顺序本身很重要。 [source_supported_conclusion: src-ibd-010, src-ibd-011]\n"
            "- Bcl-2 比共享 COX-2 signal 更有分层价值，但仍不是单独裁决工具。 [source_supported_conclusion: src-ibd-015, src-ibd-016]\n"
            "- diet-first 管理逻辑有用，但它属于 chronic enteropathy / food-response 边界内，不能直接证明 idiopathic IBD。 [source_supported_conclusion: src-ibd-014, src-ibd-021]\n\n"
            "## 下一步\n"
            "读 `topics/ibd/synthesis-index.md` 和 IBD diagnostic-workup / boundary memos；不要把 marker、影像、活检或治疗反应单独当最终答案。"
        )
    else:
        answer = (
            "This is a local IBD-versus-lymphoma explanation, not API synthesis. No API call was made. [llm_inference]\n\n"
            "## Direct Answer\n"
            "Feline IBD versus small-cell or low-grade alimentary lymphoma should not be treated as a one-marker problem. The vault frames it as diagnostic-boundary compression and workup sequencing: chronic-enteropathy suspicion, imaging pressure, biopsy-site strategy, integrated pathology, then bounded marker support. "
            "[source_supported_conclusion: src-ibd-003, src-ibd-010, src-ibd-011, src-ibd-015, src-ibd-016, src-ibd-019]\n\n"
            "## Researcher Lens\n"
            "- The research core is boundary compression: IBD, chronic enteropathy, food response, and small-cell lymphoma overlap across symptoms, imaging, pathology, and treatment response. "
            "[source_supported_conclusion: src-ibd-003, src-ibd-010, src-ibd-011, src-ibd-014]\n"
            "- The common research mistake is treating markers, imaging, biopsy site, integrated pathology, and diet response as equivalent evidence layers. "
            "[source_supported_conclusion: src-ibd-010, src-ibd-011, src-ibd-015, src-ibd-016, src-ibd-021]\n\n"
            "## Key Boundaries\n"
            "- Muscularis thickening is lymphoma-leaning, and ileal sampling can change diagnosis, so sampling strategy matters. [source_supported_conclusion: src-ibd-010, src-ibd-011]\n"
            "- Bcl-2 is stronger than shared COX-2 signal, but still not a standalone separator. [source_supported_conclusion: src-ibd-015, src-ibd-016]\n"
            "- Diet-first logic belongs inside chronic-enteropathy and food-response boundaries; it is not pure idiopathic-IBD proof. [source_supported_conclusion: src-ibd-014, src-ibd-021]\n\n"
            "## Next Step\n"
            "Read `topics/ibd/synthesis-index.md` plus the diagnostic-workup and boundary memos. Do not let one marker, image, biopsy note, or treatment response become the whole answer."
        )
    return answer, source_ids


def build_ibd_local_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return a plain-language IBD explanation for ordinary users."""
    source_ids = ["src-ibd-003", "src-ibd-010", "src-ibd-014", "src-ibd-021"]
    if chinese:
        answer = (
            "这是本地 vault 的猫IBD解释，不是 API 综合回答；本次没有调用 API。 [inference]\n\n"
            "## 什么是猫IBD？\n\n"
            "**IBD（炎症性肠病）是一种慢性肠道疾病，肠壁发生炎症，导致消化问题。**\n\n"
            "猫的IBD是一个\"排除诊断\"——需要排除其他原因（如食物过敏、感染、肿瘤）后才能确诊。\n\n"
            "[source_supported_conclusion: src-ibd-003]\n\n"
            "## 有什么症状？\n\n"
            "IBD的症状通常是慢性的、反复出现的：\n\n"
            "| 常见症状 |\n"
            "|----------|\n"
            "| 慢性呕吐 |\n"
            "| 慢性腹泻 |\n"
            "| 体重下降 |\n"
            "| 食欲变化 |\n"
            "| 腹部不适 |\n"
            "| 毛发粗糙 |\n\n"
            "**注意：** 这些症状也可能是其他疾病引起的（包括肠道淋巴瘤），需要兽医综合判断。\n\n"
            "[source_supported_conclusion: src-ibd-010]\n\n"
            "## 如何诊断？\n\n"
            "IBD诊断是一个排除过程：\n\n"
            "| 步骤 | 目的 |\n"
            "|------|------|\n"
            "| 病史和体检 | 了解症状持续时间和特点 |\n"
            "| 血液检查 | 排除其他疾病 |\n"
            "| 粪便检查 | 排除寄生虫 |\n"
            "| 饮食试验 | 排除食物过敏/不耐受 |\n"
            "| 超声波 | 观察肠壁变化 |\n"
            "| 肠道活检 | 确认诊断（金标准） |\n\n"
            "**重要：** 活检有助于区分IBD和肠道淋巴瘤，这两种病症状很相似。\n\n"
            "[source_supported_conclusion: src-ibd-010, src-ibd-021]\n\n"
            "## 可以治疗吗？\n\n"
            "**IBD可以管理，但通常需要长期治疗：**\n\n"
            "| 治疗方式 | 说明 |\n"
            "|----------|------|\n"
            "| 饮食管理 | 通常是第一步，尝试低敏或新蛋白饮食 |\n"
            "| 药物治疗 | 类固醇等抗炎药物 |\n"
            "| 益生菌 | 辅助肠道健康 |\n"
            "| 维生素补充 | B12等可能缺乏的营养 |\n\n"
            "**关键：** 很多猫对饮食改变就有反应。饮食试验应该坚持至少2-4周。\n\n"
            "[source_supported_conclusion: src-ibd-014, src-ibd-021]\n\n"
            "## IBD和肠道淋巴瘤的区别\n\n"
            "这两种病症状非常相似，需要活检才能区分。\n\n"
            "- IBD是炎症，不是肿瘤\n"
            "- 肠道淋巴瘤是肿瘤\n"
            "- 治疗方案不同\n"
            "- 预后不同\n\n"
            "如果担心，请与兽医讨论是否需要活检。\n\n"
            "[source_supported_conclusion: src-ibd-010]\n\n"
            "## 研究者视角\n"
            "- 从研究者视角来看，IBD、慢性肠病 (chronic enteropathy)、食物反应 (diet response) 与小细胞淋巴瘤之间存在高度的边界挤压 (boundary compression)。\n"
            "- 区分两者是典型的诊断边界 (diagnostic-boundary) 命题，不能只看单一标记物 (Bcl-2) 作为独立判决指标 (standalone separator)。\n\n"
            "## 不能说过头的地方\n"
            "- 我们不能说过头，不能把饮食反应 (diet response) 或是单一活检结果作为特发性 IBD 的最终证据。治疗方案的设计依然存在治疗边界。\n"
            "- 这不是兽医诊疗建议，也不替代线下兽医判断。\n\n"
            "## 下一步\n"
            "- 详细了解请阅读 `topics/ibd/synthesis-index.md` 或相关的 diagnostic-workup Memos。\n"
        )
    else:
        answer = (
            "This is a local vault IBD explanation, not API synthesis. No API call was made. [inference]\n\n"
            "## What is Feline IBD?\n\n"
            "**IBD (Inflammatory Bowel Disease) is a chronic intestinal condition where the intestinal wall becomes inflamed, causing digestive problems.**\n\n"
            "Feline IBD is a \"diagnosis of exclusion\" — other causes (food allergies, infections, tumors) must be ruled out first.\n\n"
            "[source_supported_conclusion: src-ibd-003]\n\n"
            "## What Are the Signs?\n\n"
            "IBD signs are typically chronic and recurring:\n\n"
            "| Common Signs |\n"
            "|--------------|\n"
            "| Chronic vomiting |\n"
            "| Chronic diarrhea |\n"
            "| Weight loss |\n"
            "| Appetite changes |\n"
            "| Abdominal discomfort |\n"
            "| Poor coat condition |\n\n"
            "**Note:** These signs can also be caused by other conditions (including intestinal lymphoma). A vet needs to evaluate.\n\n"
            "[source_supported_conclusion: src-ibd-010]\n\n"
            "## How Is It Diagnosed?\n\n"
            "IBD diagnosis is a process of elimination:\n\n"
            "| Step | Purpose |\n"
            "|------|--------|\n"
            "| History and exam | Understand symptom duration and pattern |\n"
            "| Blood tests | Rule out other diseases |\n"
            "| Fecal tests | Rule out parasites |\n"
            "| Diet trial | Rule out food allergy/intolerance |\n"
            "| Ultrasound | View intestinal wall changes |\n"
            "| Intestinal biopsy | Confirm diagnosis (gold standard) |\n\n"
            "**Important:** Biopsy helps distinguish IBD from intestinal lymphoma, which have very similar symptoms.\n\n"
            "[source_supported_conclusion: src-ibd-010, src-ibd-021]\n\n"
            "## Can It Be Treated?\n\n"
            "**IBD can be managed, but usually requires long-term treatment:**\n\n"
            "| Treatment | Description |\n"
            "|-----------|-------------|\n"
            "| Diet management | Usually first step; try hypoallergenic or novel protein diet |\n"
            "| Medication | Steroids and other anti-inflammatory drugs |\n"
            "| Probiotics | Support gut health |\n"
            "| Vitamin supplements | B12 and other nutrients that may be deficient |\n\n"
            "**Key point:** Many cats respond to diet changes alone. Diet trials should last at least 2-4 weeks.\n\n"
            "[source_supported_conclusion: src-ibd-014, src-ibd-021]\n\n"
            "## IBD vs Intestinal Lymphoma\n\n"
            "These two conditions have very similar symptoms; biopsy is needed to distinguish them.\n\n"
            "- IBD is inflammation, not cancer\n"
            "- Intestinal lymphoma is cancer\n"
            "- Treatment differs\n"
            "- Prognosis differs\n\n"
            "If concerned, discuss with your vet whether biopsy is needed.\n\n"
            "[source_supported_conclusion: src-ibd-010]\n\n"
            "## Researcher Lens\n"
            "- From a researcher's perspective, IBD, chronic enteropathy, and food response overlap with small-cell lymphoma, causing significant boundary compression.\n"
            "- Distinguishing them is a classic diagnostic-boundary issue; do not rely on Bcl-2 as a standalone separator.\n\n"
            "## Do Not Overstate\n"
            "- Do not overstate the diagnosis based only on diet response or a single biopsy site. Bounded management remains necessary.\n\n"
            "## Next Step\n"
            "- Read `topics/ibd/synthesis-index.md` or related diagnostic-workup memos for more details.\n"
        )
    return answer, source_ids


def build_diabetes_local_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return a plain-language diabetes explanation for ordinary users."""
    source_ids = ["src-diabetes-001", "src-diabetes-005", "src-diabetes-007", "src-diabetes-015"]
    if chinese:
        answer = (
            "这是本地 vault 的猫糖尿病解释，不是 API 综合回答；本次没有调用 API。 [inference]\n\n"
            "## 什么是猫糖尿病？\n\n"
            "**猫糖尿病是一种猫的身体无法正常利用血糖的疾病，类似于人的2型糖尿病。**\n\n"
            "正常情况下，胰岛素帮助身体细胞吸收血糖。糖尿病猫要么产生的胰岛素不够，要么身体对胰岛素反应不好。\n\n"
            "[source_supported_conclusion: src-diabetes-001]\n\n"
            "## 哪些猫容易得糖尿病？\n\n"
            "| 风险因素 |\n"
            "|----------|\n"
            "| 肥胖（最重要的风险因素） |\n"
            "| 年龄（中老年猫更常见） |\n"
            "| 公猫比母猫风险略高 |\n"
            "| 某些品种（如缅甸猫） |\n"
            "| 长期使用类固醇 |\n\n"
            "[source_supported_conclusion: src-diabetes-001, src-diabetes-005]\n\n"
            "## 有什么症状？\n\n"
            "糖尿病的典型症状（\"三多一少\"）：\n\n"
            "| 症状 | 说明 |\n"
            "|------|------|\n"
            "| 喝水增多 | 明显比平时喝更多水 |\n"
            "| 排尿增多 | 尿量增加，可能尿在猫砂盆外 |\n"
            "| 食欲增加 | 吃得多但体重下降 |\n"
            "| 体重下降 | 尽管食欲好仍然变瘦 |\n\n"
            "晚期可能出现：\n"
            "- 后腿无力（走路姿势异常，脚跟着地）\n"
            "- 毛发粗糙\n"
            "- 精神变差\n\n"
            "[source_supported_conclusion: src-diabetes-001]\n\n"
            "## 如何诊断？\n\n"
            "| 检查 | 目的 |\n"
            "|------|------|\n"
            "| 血糖检测 | 检查血糖是否升高 |\n"
            "| 果糖胺检测 | 反映近2-3周平均血糖 |\n"
            "| 尿检 | 检查尿糖和酮体 |\n"
            "| 其他血检 | 排除并发症 |\n\n"
            "**注意：** 猫在紧张时血糖会升高，所以不能只靠一次血糖就诊断。\n\n"
            "[source_supported_conclusion: src-diabetes-001]\n\n"
            "## 可以治疗吗？\n\n"
            "**糖尿病可以管理，部分猫甚至可以缓解（不再需要胰岛素）。**\n\n"
            "| 治疗方式 | 说明 |\n"
            "|----------|------|\n"
            "| 胰岛素注射 | 大多数猫需要每天注射 |\n"
            "| 饮食管理 | 高蛋白低碳水化合物饮食 |\n"
            "| 定期监测 | 在家或医院监测血糖 |\n"
            "| 减肥 | 如果肥胖，控制体重很重要 |\n\n"
            "**好消息：** 约30-50%的猫在治疗数周到数月后可能进入缓解期。\n\n"
            "[source_supported_conclusion: src-diabetes-007, src-diabetes-015]\n\n"
            "## 预防\n\n"
            "| 措施 |\n"
            "|------|\n"
            "| 保持健康体重（最重要） |\n"
            "| 适量运动 |\n"
            "| 合理饮食 |\n"
            "| 定期体检 |\n\n"
            "[source_supported_conclusion: src-diabetes-005]\n\n"
            "## 研究者视角\n"
            "- 猫糖尿病（猫糖尿病）是一个复杂的混合型代谢/内分泌综合征 (mixed metabolic/endocrine syndrome)。\n"
            "- 从研究者视角来看，其管理核心包括胰岛素应用、饮食管理和诱导缓解 (remission)。\n"
            "- 新型口服药如 SGLT2 抑制剂的使用也重构了临床选择，但在用药时需密切监测糖尿病酮症酸中毒（以及进行 ketone monitoring 酮体监测）。\n\n"
            "## 不能说过头的地方\n"
            "- 我们不能说过头，缓解 (remission) 并不等于永久性治愈，且管理不当可能随时复发。\n"
            "- 这不是兽医诊疗建议，也不替代线下兽医判断。\n\n"
            "## 下一步\n"
            "- 详细了解请阅读 `topics/diabetes/synthesis-index.md` 以获得更多有关治疗证据的指导。\n"
        )
        return answer, source_ids
    answer = (
        "This is a local vault diabetes explanation, not API synthesis. No API call was made. [inference]\n\n"
        "## What is Feline Diabetes?\n\n"
        "**Feline diabetes is a disease where a cat's body cannot properly use blood sugar, similar to Type 2 diabetes in humans.**\n\n"
        "Normally, insulin helps body cells absorb blood sugar. Diabetic cats either don't produce enough insulin or their body doesn't respond well to it.\n\n"
        "[source_supported_conclusion: src-diabetes-001]\n\n"
        "## Which Cats Are at Risk?\n\n"
        "| Risk Factors |\n"
        "|--------------|\n"
        "| Obesity (most important risk factor) |\n"
        "| Age (more common in middle-aged and older cats) |\n"
        "| Male cats slightly higher risk |\n"
        "| Certain breeds (e.g., Burmese) |\n"
        "| Long-term steroid use |\n\n"
        "[source_supported_conclusion: src-diabetes-001, src-diabetes-005]\n\n"
        "## What Are the Signs?\n\n"
        "Classic diabetes signs:\n\n"
        "| Sign | Description |\n"
        "|------|-------------|\n"
        "| Increased thirst | Drinking much more water than usual |\n"
        "| Increased urination | More urine, may urinate outside litter box |\n"
        "| Increased appetite | Eating more but losing weight |\n"
        "| Weight loss | Getting thinner despite good appetite |\n\n"
        "Later stages may include:\n"
        "- Hind leg weakness (abnormal walking, walking on heels)\n"
        "- Poor coat condition\n"
        "- Lethargy\n\n"
        "[source_supported_conclusion: src-diabetes-001]\n\n"
        "## How Is It Diagnosed?\n\n"
        "| Test | Purpose |\n"
        "|------|--------|\n"
        "| Blood glucose | Check if blood sugar is elevated |\n"
        "| Fructosamine | Reflects 2-3 week average blood sugar |\n"
        "| Urinalysis | Check for glucose and ketones |\n"
        "| Other blood tests | Rule out complications |\n\n"
        "**Note:** Cats' blood sugar rises when stressed, so diagnosis cannot rely on a single reading.\n\n"
        "[source_supported_conclusion: src-diabetes-001]\n\n"
        "## Can It Be Treated?\n\n"
        "**Diabetes can be managed, and some cats can even go into remission (no longer need insulin).**\n\n"
        "| Treatment | Description |\n"
        "|-----------|-------------|\n"
        "| Insulin injections | Most cats need daily injections |\n"
        "| Diet management | High-protein, low-carbohydrate diet |\n"
        "| Regular monitoring | Blood sugar monitoring at home or clinic |\n"
        "| Weight control | If obese, weight loss is important |\n\n"
        "**Good news:** About 30-50% of cats may enter remission after weeks to months of treatment.\n\n"
        "[source_supported_conclusion: src-diabetes-007, src-diabetes-015]\n\n"
        "## Prevention\n\n"
        "| Measure |\n"
        "|---------|\n"
        "| Maintain healthy weight (most important) |\n"
        "| Regular exercise |\n"
        "| Proper diet |\n"
        "| Regular checkups |\n\n"
        "[source_supported_conclusion: src-diabetes-005]\n\n"
        "## Researcher Lens\n"
        "- Feline diabetes should be characterized as a mixed metabolic/endocrine syndrome rather than a simple endocrine issue.\n"
        "- From a researcher's lens, we must trace beta-cell failure and obesity-driven insulin resistance, alongside complications like pancreatitis.\n"
        "- Remission is a critical goal. While diet and insulin are baseline treatments, SGLT2 inhibitors provide a new tool requiring strict ketone monitoring.\n\n"
        "## Do Not Overstate\n"
        "- Do Not Overstate any protocol ranking without discussing specific patient conditions. Management does not guarantee permanent remission.\n\n"
        "## Next Step\n"
        "- Read `topics/diabetes/synthesis-index.md` or the corresponding therapy manuals.\n"
    )
    return answer, source_ids


def build_fcv_local_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return a plain-language FCV explanation for ordinary users."""
    source_ids = ["src-fcv-001", "src-fcv-002", "src-fcv-003", "src-fcv-010"]
    if chinese:
        answer = (
            "这是本地 vault 的猫杯状病毒解释，不是 API 综合回答；本次没有调用 API。 [inference]\n\n"
            "## 什么是猫杯状病毒（FCV）？\n\n"
            "**FCV是一种常见的猫呼吸道病毒，主要引起上呼吸道感染和口腔问题。**\n\n"
            "它是猫\"感冒\"的常见原因之一，也是核心疫苗预防的疾病。\n\n"
            "[source_supported_conclusion: src-fcv-001]\n\n"
            "## 有什么症状？\n\n"
            "### 常见症状（普通感染）\n"
            "| 症状 |\n"
            "|------|\n"
            "| 打喷嚏 |\n"
            "| 流鼻涕 |\n"
            "| 流眼泪 |\n"
            "| 口腔溃疡 |\n"
            "| 发烧 |\n"
            "| 食欲下降 |\n"
            "| 流涎 |\n\n"
            "### 严重形式（VS-FCV）\n"
            "一种高致病性变异株可能导致：\n"
            "- 严重的全身症状\n"
            "- 皮肤溃疡\n"
            "- 多器官受累\n"
            "- 较高死亡率\n\n"
            "**注意：** VS-FCV相对罕见，但在猫群中可能爆发。\n\n"
            "[source_supported_conclusion: src-fcv-001, src-fcv-002]\n\n"
            "## 如何传播？\n\n"
            "| 传播方式 |\n"
            "|----------|\n"
            "| 直接接触感染猫 |\n"
            "| 打喷嚏产生的飞沫 |\n"
            "| 共用食盆、水碗 |\n"
            "| 人的手和衣物传播 |\n\n"
            "**重要：** 感染恢复后的猫可能成为长期携带者，持续排毒。\n\n"
            "[source_supported_conclusion: src-fcv-001]\n\n"
            "## 如何诊断？\n\n"
            "| 方法 | 说明 |\n"
            "|------|------|\n"
            "| 临床症状 | 口腔溃疡是特征性表现 |\n"
            "| PCR检测 | 可确认病毒存在 |\n"
            "| 排除其他原因 | 与猫疱疹病毒症状相似 |\n\n"
            "[source_supported_conclusion: src-fcv-001]\n\n"
            "## 可以治疗吗？\n\n"
            "**主要是支持性治疗：**\n\n"
            "| 治疗 | 目的 |\n"
            "|------|------|\n"
            "| 营养支持 | 保证进食和饮水 |\n"
            "| 清洁眼鼻分泌物 | 保持舒适 |\n"
            "| 抗生素 | 预防继发细菌感染 |\n"
            "| 止痛药 | 缓解口腔溃疡疼痛 |\n\n"
            "大多数猫可以康复，但可能成为长期携带者。\n\n"
            "[source_supported_conclusion: src-fcv-001]\n\n"
            "**注意：** 疫苗可以减轻症状，但不能100%防止感染。\n\n"
            "[source_supported_conclusion: src-fcv-003, src-fcv-010]\n\n"
            "## 研究者视角\n"
            "- 猫杯状病毒（FCV）防范的核心在于核心疫苗 (vaccine) 的复杂性。\n"
            "- 在进行分析时，应注意区分普通的 FCV 上呼吸道感染和高致病性的全身性变异株 (VS-FCV)。\n"
            "- 对治疗 (therapy) 分支的支持在当前依然属于局限或非主导层。\n\n"
            "## 不能说过头的地方\n"
            "- 我们不能说过头，不能让零散的治疗信号压过疫苗预防的核心证据，也不能给出替代兽医判断的治疗指南。\n"
            "- 这不是兽医诊疗建议，也不替代线下兽医判断。\n\n"
            "## 下一步\n"
            "- 详细了解请阅读 `topics/fcv/synthesis-index.md` 或相关的 endpoint handbook。\n"
        )
        return answer, source_ids
    answer = (
        "This is a local vault FCV explanation, not API synthesis. No API call was made. [inference]\n\n"
        "## What is Feline Calicivirus (FCV)?\n\n"
        "**FCV is a common cat respiratory virus that mainly causes upper respiratory infections and oral problems.**\n\n"
        "It's one of the common causes of cat \"colds\" and is prevented by core vaccines.\n\n"
        "[source_supported_conclusion: src-fcv-001]\n\n"
        "## What Are the Signs?\n\n"
        "### Common Signs (Typical Infection)\n"
        "| Sign |\n"
        "|------|\n"
        "| Sneezing |\n"
        "| Runny nose |\n"
        "| Watery eyes |\n"
        "| Mouth ulcers |\n"
        "| Fever |\n"
        "| Decreased appetite |\n"
        "| Drooling |\n\n"
        "### Severe Form (VS-FCV)\n"
        "A highly pathogenic variant can cause:\n"
        "- Severe systemic symptoms\n"
        "- Skin ulcers\n"
        "- Multi-organ involvement\n"
        "- Higher mortality\n\n"
        "**Note:** VS-FCV is relatively rare but can cause outbreaks in cat populations.\n\n"
        "[source_supported_conclusion: src-fcv-001, src-fcv-002]\n\n"
        "## How Does It Spread?\n\n"
        "| Transmission Route |\n"
        "|-------------------|\n"
        "| Direct contact with infected cats |\n"
        "| Droplets from sneezing |\n"
        "| Shared food and water bowls |\n"
        "| Human hands and clothing |\n\n"
        "**Important:** Recovered cats can become long-term carriers, continuing to shed virus.\n\n"
        "[source_supported_conclusion: src-fcv-001]\n\n"
        "## How Is It Diagnosed?\n\n"
        "| Method | Description |\n"
        "|--------|-------------|\n"
        "| Clinical signs | Mouth ulcers are characteristic |\n"
        "| PCR test | Can confirm virus presence |\n"
        "| Rule out other causes | Similar to feline herpesvirus |\n\n"
        "[source_supported_conclusion: src-fcv-001]\n\n"
        "## Can It Be Treated?\n\n"
        "**Mainly supportive care:**\n\n"
        "| Treatment | Purpose |\n"
        "|-----------|--------|\n"
        "| Nutritional support | Ensure eating and drinking |\n"
        "| Clean eye/nose discharge | Maintain comfort |\n"
        "| Antibiotics | Prevent secondary bacterial infection |\n"
        "| Pain medication | Relieve mouth ulcer pain |\n\n"
        "Most cats recover but may become long-term carriers.\n\n"
        "[source_supported_conclusion: src-fcv-001]\n\n"
        "## Prevention\n\n"
        "**Vaccination is the most important prevention measure:**\n\n"
        "| Measure |\n"
        "|---------|\n"
        "| Core vaccination (highly recommended) |\n"
        "| Isolate new cats (at least 2 weeks) |\n"
        "| Maintain environmental hygiene |\n"
        "| Reduce stress |\n\n"
        "[source_supported_conclusion: src-fcv-003, src-fcv-010]\n\n"
        "## Researcher Lens\n"
        "- Understanding feline calicivirus (FCV) epidemiology involves analyzing vaccine/immunity complexity.\n"
        "- From a researcher's lens, we must consider cellular versus humoral immune response and the limits of any vaccine protection claim.\n"
        "- Distinction between routine upper respiratory signs and highly virulent systemic variants (VS-FCV) is critical. FCV tissue tropism dictates its persistence.\n"
        "- Long-term carrier persistence is a major reservoir.\n\n"
        "## Do Not Overstate\n"
        "- Do Not Overstate therapy limits. We should not suggest therapy signals replace preventive vaccine evidence.\n\n"
        "## Next Step\n"
        "- Read `topics/fcv/synthesis-index.md` or the corresponding FCV endpoint handbook.\n"
    )
    return answer, source_ids


def build_obesity_local_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return a plain-language obesity explanation for ordinary users."""
    source_ids = ["src-obesity-001", "src-obesity-004", "src-obesity-005", "src-obesity-008"]
    if chinese:
        answer = (
            "这是本地 vault 的猫肥胖解释，不是 API 综合回答；本次没有调用 API。 [inference]\n\n"
            "## 什么是猫肥胖？\n\n"
            "**猫肥胖是指猫的体重明显超过健康体重，身体积累过多脂肪的状态。**\n\n"
            "这是宠物猫最常见的营养问题。根据不同地区，**11.5% 到 63%** 的猫存在超重或肥胖。\n\n"
            "[source_supported_conclusion: src-obesity-001]\n\n"
            "## 为什么猫会变胖？\n\n"
            "### 猫自身因素\n"
            "| 因素 | 说明 |\n"
            "|------|------|\n"
            "| 绝育 | 绝育后代谢改变，更容易增重 |\n"
            "| 年龄 | 不同年龄风险不同 |\n"
            "| 品种 | 某些品种更容易发胖 |\n\n"
            "### 生活环境因素\n"
            "| 因素 | 说明 |\n"
            "|------|------|\n"
            "| 室内久坐 | 活动量低 |\n"
            "| 自由采食 | 全天候提供食物 |\n"
            "| 主人习惯 | 用食物表达爱意 |\n\n"
            "[source_supported_conclusion: src-obesity-001, src-obesity-004]\n\n"
            "## 肥胖有什么危害？\n\n"
            "| 健康问题 |\n"
            "|----------|\n"
            "| 糖尿病（2型） |\n"
            "| 关节问题、跛行 |\n"
            "| 皮肤问题 |\n"
            "| 泌尿系统疾病 |\n"
            "| 肝脏脂肪堆积 |\n\n"
            "**关键：** 猫的体重增加时，胰岛素敏感性会下降，这是肥胖导致糖尿病的主要原因。\n\n"
            "[source_supported_conclusion: src-obesity-001, src-obesity-008]\n\n"
            "## 如何判断猫是否肥胖？\n\n"
            "简单检查：\n"
            "- 能否感觉到肋骨？健康体重的猫应该能轻易摸到肋骨\n"
            "- 俯视猫的身体，是否有腰线？\n"
            "- 侧面看，腹部是否下垂？\n\n"
            "**注意：** 主人常常低估自己猫的体重状况。如果不确定，请咨询兽医。\n\n"
            "[source_supported_conclusion: src-obesity-001]\n\n"
            "## 最佳预防时机\n\n"
            "**绝育后 5-12 个月龄的幼猫** 是预防肥胖的关键时期。预防比治疗更有效。\n\n"
            "[source_supported_conclusion: src-obesity-005]\n\n"
            "## 研究者视角\n"
            "- 从研究者视角来看，猫肥胖症的评估需重视证据深度（证据深度）。\n"
            "- 核心机制关注猫体重上升时导致的胰岛素敏感性下降 (insulin sensitivity)。\n"
            "- 预防肥胖的最关键抓手是绝育后的幼猫 (post-gonadectomy kittens) 在 5-12 个月龄时的代谢管理。\n\n"
            "## 不能说过头的地方\n"
            "- 我们不能说过头，不能给宠物主人提供非处方的、owner-facing 的减重方案，也不能随意按 effect size 排名风险因素或治疗方式。\n"
            "- 这不是兽医诊疗建议，也不替代线下兽医判断。\n\n"
            "## 下一步\n"
            "- 详细了解请阅读 `topics/obesity/mechanism-overview.md`、`topics/obesity/prevention.md` 或是 `topics/obesity/diabetes-bridge.md` 以获得更多有关治疗证据的指导。\n"
        )
        return answer, source_ids
    answer = (
        "This is a local vault obesity explanation, not API synthesis. No API call was made. [inference]\n\n"
        "## What is Feline Obesity?\n\n"
        "**Feline obesity is when a cat carries significantly more body weight than is healthy, with excess fat accumulation.**\n\n"
        "It's the most common nutritional problem in pet cats. Depending on the region, **11.5% to 63%** of cats are overweight or obese.\n\n"
        "[source_supported_conclusion: src-obesity-001]\n\n"
        "## Why Do Cats Become Obese?\n\n"
        "### Cat-Related Factors\n"
        "| Factor | Description |\n"
        "|--------|-------------|\n"
        "| Neutering | Metabolic changes increase weight gain risk |\n"
        "| Age | Risk varies by life stage |\n"
        "| Breed | Some breeds are predisposed |\n\n"
        "### Lifestyle Factors\n"
        "| Factor | Description |\n"
        "|--------|-------------|\n"
        "| Indoor sedentary life | Low activity level |\n"
        "| Free feeding | Food available all day |\n"
        "| Owner habits | Using food to show affection |\n\n"
        "[source_supported_conclusion: src-obesity-001, src-obesity-004]\n\n"
        "## What Are the Health Risks?\n\n"
        "| Health Problem |\n"
        "|----------------|\n"
        "| Type 2 diabetes |\n"
        "| Joint problems, lameness |\n"
        "| Skin disorders |\n"
        "| Urinary tract disease |\n"
        "| Hepatic lipidosis |\n\n"
        "**Key point:** As a cat's weight increases, insulin sensitivity decreases. This is the primary link between obesity and diabetes.\n\n"
        "[source_supported_conclusion: src-obesity-001, src-obesity-008]\n\n"
        "## How Do I Know If My Cat Is Obese?\n\n"
        "Simple checks:\n"
        "- Can you feel the ribs? A healthy-weight cat's ribs should be easy to feel\n"
        "- Looking from above, does your cat have a waist?\n"
        "- From the side, does the belly hang down?\n\n"
        "**Note:** Owners often underestimate their cat's weight. If unsure, consult a veterinarian.\n\n"
        "[source_supported_conclusion: src-obesity-001]\n\n"
        "## Best Time for Prevention\n\n"
        "**Post-neutering kittens aged 5-12 months** are the key target for obesity prevention. Prevention is more effective than treatment.\n\n"
        "[source_supported_conclusion: src-obesity-005]\n\n"
        "## Researcher Lens\n"
        "- From a researcher's perspective, we must address the Evidence-Depth Caveat of obesity data, classifying intrinsic and extrinsic factors.\n"
        "- The core mechanism is related to the decline in insulin sensitivity. The key target is post-gonadectomy kittens.\n"
        "- This functions as a compiled starter. In terms of associated conditions, we must trace the diabetes-bridge.\n\n"
        "## Do Not Overstate\n"
        "- Do Not Overstate weight-loss protocols or effect-size rankings. Prevalence range is wide.\n\n"
        "## Next Step\n"
        "- Read `topics/obesity/mechanism-overview.md` or `topics/obesity/prevention.md` for detail.\n"
    )
    return answer, source_ids


def build_cancer_local_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return a plain-language cancer explanation for ordinary users."""
    source_ids = ["src-cancer-002", "src-cancer-004", "src-cancer-040", "src-cancer-001"]
    if chinese:
        answer = (
            "这是本地 vault 的猫癌症解释，不是 API 综合回答；本次没有调用 API。 [inference]\n\n"
            "## 什么是猫癌症？\n\n"
            "**猫癌症是指猫体内细胞异常生长、失去正常控制的疾病。癌细胞可以侵犯周围组织，有时会扩散到身体其他部位。**\n\n"
            "癌症是老年猫的常见疾病。猫的平均寿命延长意味着癌症发病率也在增加。\n\n"
            "[source_supported_conclusion: src-cancer-004]\n\n"
            "## 常见类型\n\n"
            "| 类型 | 说明 |\n"
            "|------|------|\n"
            "| 淋巴瘤 | 最常见的血液系统肿瘤 |\n"
            "| 乳腺癌 | 未绝育母猫高发 |\n"
            "| 口腔鳞状细胞癌 | 口腔最常见肿瘤 |\n"
            "| 注射部位肉瘤 | 与注射有关的罕见肿瘤 |\n"
            "| 皮肤肿瘤 | 包括多种类型 |\n\n"
            "[source_supported_conclusion: src-cancer-002, src-cancer-004]\n\n"
            "## 有什么症状？\n\n"
            "| 警示信号 |\n"
            "|----------|\n"
            "| 体重下降 |\n"
            "| 食欲减退 |\n"
            "| 持续呕吐或腹泻 |\n"
            "| 不愈合的伤口 |\n"
            "| 异常肿块 |\n"
            "| 呼吸困难 |\n\n"
            "**注意：** 这些症状也可能是其他疾病引起的。出现这些症状应咨询兽医。\n\n"
            "[source_supported_conclusion: src-cancer-040]\n\n"
            "## 如何诊断？\n\n"
            "1. **体检** — 检查肿块、淋巴结、整体状况\n"
            "2. **影像** — X光、超声波、CT\n"
            "3. **组织检查** — 穿刺或活检确定肿瘤类型\n"
            "4. **分期** — 确定癌症是否扩散\n\n"
            "[source_supported_conclusion: src-cancer-040]\n\n"
            "## 可以治疗吗？\n\n"
            "许多猫癌症可以治疗，但结果因类型、分期和个体情况而异。\n\n"
            "| 治疗方式 | 适用情况 |\n"
            "|----------|----------|\n"
            "| 手术 | 局部肿瘤的首选 |\n"
            "| 化疗 | 淋巴瘤等系统性癌症 |\n"
            "| 放疗 | 某些无法手术的肿瘤 |\n"
            "| 姑息治疗 | 控制症状、提高生活质量 |\n\n"
            "**重要：** 猫的化疗与人不同，副作用通常较轻。\n\n"
            "[source_supported_conclusion: src-cancer-040]\n\n"
            "## 预防\n\n"
            "| 措施 | 作用 |\n"
            "|------|------|\n"
            "| 早期绝育 | 显著降低乳腺癌风险 |\n"
            "| 避免阳光暴晒 | 白猫皮肤癌风险较高 |\n"
            "| 定期体检 | 早发现早治疗 |\n\n"
            "[source_supported_conclusion: src-cancer-004]\n\n"
            "## 研究者视角\n"
            "- 从研究者视角来看，分析猫肿瘤（猫癌症）需建立在严谨的证据深度上。\n"
            "- 核心的决策逻辑是先走临床工作流 (clinical workflow) —— 包括临床表现、诊断和临床分期，再根据具体的肿瘤家族 (tumor family) 分支开展深入讨论。\n\n"
            "## 不能说过头的地方\n"
            "- 我们不能说过头，不能在此直接对各种治疗手段进行疗效排名，也不宜在无背景限制的情况下复用具体的存活期或预后范围数据。\n"
            "- 这不是兽医诊疗建议，也不替代线下兽医判断。\n\n"
            "## 下一步\n"
            "- 详细了解请阅读 `topics/cancer/suspected-cancer-workflow.md`、`topics/cancer/synthesis-index.md` 或是具体的肿瘤家族分支指南。\n"
        )
        return answer, source_ids
    answer = (
        "This is a local vault cancer explanation, not API synthesis. No API call was made. [inference]\n\n"
        "## What is Feline Cancer?\n\n"
        "**Feline cancer is a disease where cells in a cat's body grow abnormally and out of control. Cancer cells can invade surrounding tissues and sometimes spread to other parts of the body.**\n\n"
        "Cancer is common in older cats. As cats live longer on average, cancer incidence has increased.\n\n"
        "[source_supported_conclusion: src-cancer-004]\n\n"
        "## Common Types\n\n"
        "| Type | Description |\n"
        "|------|-------------|\n"
        "| Lymphoma | Most common blood cancer |\n"
        "| Mammary carcinoma | Common in unspayed females |\n"
        "| Oral squamous cell carcinoma | Most common oral tumor |\n"
        "| Injection-site sarcoma | Rare tumor related to injections |\n"
        "| Skin tumors | Including various types |\n\n"
        "[source_supported_conclusion: src-cancer-002, src-cancer-004]\n\n"
        "## What Are the Signs?\n\n"
        "| Warning Signs |\n"
        "|---------------|\n"
        "| Weight loss |\n"
        "| Loss of appetite |\n"
        "| Persistent vomiting or diarrhea |\n"
        "| Non-healing wounds |\n"
        "| Unusual lumps |\n"
        "| Difficulty breathing |\n\n"
        "**Note:** These signs can also be caused by other conditions. Consult a veterinarian if you notice these signs.\n\n"
        "[source_supported_conclusion: src-cancer-040]\n\n"
        "## How Is It Diagnosed?\n\n"
        "1. **Physical exam** — Check for lumps, lymph nodes, overall condition\n"
        "2. **Imaging** — X-rays, ultrasound, CT\n"
        "3. **Tissue sampling** — Aspirate or biopsy to determine tumor type\n"
        "4. **Staging** — Determine if cancer has spread\n\n"
        "[source_supported_conclusion: src-cancer-040]\n\n"
        "## Can It Be Treated?\n\n"
        "Many feline cancers can be treated, but outcomes vary by type, stage, and individual factors.\n\n"
        "| Treatment | When Used |\n"
        "|-----------|----------|\n"
        "| Surgery | First choice for localized tumors |\n"
        "| Chemotherapy | Systemic cancers like lymphoma |\n"
        "| Radiation | Some non-surgical tumors |\n"
        "| Palliative care | Symptom control, quality of life |\n\n"
        "**Important:** Chemotherapy in cats differs from humans; side effects are usually milder.\n\n"
        "[source_supported_conclusion: src-cancer-040]\n\n"
        "## Prevention\n\n"
        "| Measure | Effect |\n"
        "|---------|--------|\n"
        "| Early spaying | Significantly reduces mammary cancer risk |\n"
        "| Avoid sun exposure | White cats have higher skin cancer risk |\n"
        "| Regular checkups | Early detection, early treatment |\n\n"
        "[source_supported_conclusion: src-cancer-004]\n\n"
        "## Researcher Lens\n"
        "- When analyzing feline cancer, researchers must respect the Evidence-Depth Caveat and establish a clinical workflow.\n"
        "- This includes presentation, diagnosis, and staging, before discussing specific tumor family branches like lymphoma, mammary carcinoma, oral SCC, or injection-site sarcoma.\n"
        "- Evidence should be denominator-labeled to prevent generalization.\n\n"
        "## Do Not Overstate\n"
        "- Feline cancer statements should stay architecture-level only. We cannot rank treatments or promise outcomes.\n\n"
        "## Next Step\n"
        "- Read `topics/cancer/suspected-cancer-workflow.md` or `topics/cancer/synthesis-index.md` for specific tumor family information.\n"
    )
    return answer, source_ids


TREATMENT_BOUNDARY_SOURCES = {
    "ckd": ["src-ckd-003", "src-ckd-004", "src-ckd-006", "src-ckd-007", "src-ckd-010", "src-ckd-015"],
    "diabetes": ["src-diabetes-006", "src-diabetes-007", "src-diabetes-008", "src-diabetes-011", "src-diabetes-015", "src-diabetes-024"],
    "fip": ["src-fip-010", "src-fip-013", "src-fip-022", "src-fip-023"],
    "hcm": ["src-hcm-008", "src-hcm-009", "src-hcm-010", "src-hcm-013", "src-hcm-024"],
    "obesity": ["src-obesity-001", "src-obesity-004", "src-obesity-005", "src-obesity-008"],
    "cancer": ["src-cancer-002", "src-cancer-003", "src-cancer-004", "src-cancer-008", "src-cancer-019", "src-cancer-040"],
    "ibd": ["src-ibd-003", "src-ibd-010", "src-ibd-011", "src-ibd-014", "src-ibd-015", "src-ibd-016", "src-ibd-019", "src-ibd-021"],
    "fcv": ["src-fcv-003", "src-fcv-008", "src-fcv-010", "src-fcv-014", "src-fcv-018", "src-fcv-022"],
}


TREATMENT_BOUNDARY_COPY = {
    "ckd": {
        "zh_label": "猫 CKD",
        "en_label": "feline CKD",
        "safe": "当前最稳的治疗/管理读法是 renal diet 与 phosphorus control 作为较清楚的基线分支，同时把 proteinuria、blood pressure、potassium、anaemia、appetite 和 subcutaneous-fluid 等 supportive-care 分支分开看。",
        "cannot": "不能把这些管理分支写成已经证明的 cure 或统一 disease-modifying therapy，也不能把单一 endpoint 变成治疗排名。",
        "next": "`topics/ckd/translation-brief.md`、`topics/ckd/current-state-dashboard.md`，以及 CKD treatment-ranking / phosphorus-control / supportive-care memos",
    },
    "diabetes": {
        "zh_label": "猫糖尿病",
        "en_label": "feline diabetes",
        "safe": "当前最安全的治疗读法是 branch separation：diet architecture、insulin/glargine、SGLT2 label boundary、candidate selection、ketone monitoring、remission endpoint 和安全监测要分开。",
        "cannot": "不能把 remission 写成单一 protocol 的结果，也不能把 SGLT2 label anchoring 写成 treatment winner。",
        "next": "`topics/diabetes/treatment-branch-map.md`、`topics/diabetes/remission-boundaries.md`、`topics/diabetes/sglt2-label-control.md`",
    },
    "fip": {
        "zh_label": "猫 FIP",
        "en_label": "feline FIP",
        "safe": "当前最安全的治疗读法是把 GS-441524/remdesivir-era evidence 分成 baseline efficacy、package logic、neurologic rescue 和 durability。",
        "cannot": "不能把所有抗病毒证据合并成一个不分病型、不分神经/眼部扩展、不分随访耐久性的疗效结论。",
        "next": "`topics/fip/translation-brief.md`、FIP treatment-evidence memo、antiviral-branch comparison memo",
    },
    "hcm": {
        "zh_label": "猫 HCM",
        "en_label": "feline HCM",
        "safe": "当前治疗层是真实但 overclaim-sensitive 的分支；应先保持 structural phenotype authority，再讨论 bounded management、targeted frontier 和证据怀疑。",
        "cannot": "不能把 biomarker、AI screening 或单个治疗信号写成最终 intervention hierarchy。",
        "next": "`topics/hcm/synthesis-index.md`、HCM treatment-evidence memo、treatment-branch comparison memo",
    },
    "obesity": {
        "zh_label": "猫肥胖",
        "en_label": "feline obesity",
        "safe": "当前只能给 compiled starter 层面的治疗边界：prevention-first framing 比 weight-loss protocol 更稳，prevention target 是 post-gonadectomy kittens aged 5-12 months。",
        "cannot": "不能给 owner-facing weight-loss protocol，不能按 effect size 排名风险因素或治疗方式。",
        "next": "`topics/obesity/mechanism-overview.md`、`topics/obesity/prevention.md`、`topics/obesity/diabetes-bridge.md`",
    },
    "cancer": {
        "zh_label": "猫肿瘤",
        "en_label": "feline cancer",
        "safe": "当前只能给 architecture-level treatment boundary：先走 suspected-cancer clinical workflow，包括 presentation、diagnosis、staging，再按 tumor family 分支讨论。",
        "cannot": "不能 rank treatments，不能复用 survival/prognosis ranges，也不能把 biomarkers 推成 clinical guidance。",
        "next": "`topics/cancer/suspected-cancer-workflow.md`、`topics/cancer/synthesis-index.md` 和对应 tumor-family branch",
    },
    "ibd": {
        "zh_label": "猫 IBD / 炎症性肠病",
        "en_label": "feline IBD",
        "safe": "当前治疗读法必须留在 chronic enteropathy / boundary compression 里：diet response、workup sequencing、biopsy site、integrated pathology 和 lymphoma boundary 要分层。",
        "cannot": "不能把 diet-first response、marker、影像或一次 biopsy note 单独写成 idiopathic IBD 证明或治疗结论。",
        "next": "`topics/ibd/synthesis-index.md`、IBD diagnostic-workup / boundary memos",
    },
    "fcv": {
        "zh_label": "猫杯状病毒 / FCV",
        "en_label": "feline FCV",
        "safe": "当前 therapy 是真实分支，但概览层应先保留 vaccine/immunity、recognition、carrier persistence 和 VS-FCV distinction。",
        "cannot": "不能让 therapy signals 压过 prevention/vaccine evidence，也不能把治疗信号写成 owner-facing treatment guidance。",
        "next": "`topics/fcv/synthesis-index.md`、`topics/fcv/risk-and-recognition.md`、`topics/fcv/endpoint-handbook.md`",
    },
}


def is_treatment_question(question: str) -> bool:
    """Detect treatment/management prompts that need bounded safety framing."""
    lowered = question.lower()
    return any(term in lowered or term in question for term in ["treatment", "therapy", "management", "怎么治疗", "治疗", "怎么治", "用药"])


def build_treatment_boundary_explanation(disease: str, chinese: bool) -> tuple[str, list[str]]:
    """Return a deterministic no-API treatment-boundary answer."""
    source_ids = TREATMENT_BOUNDARY_SOURCES[disease]
    copy = TREATMENT_BOUNDARY_COPY[disease]
    cited = ", ".join(source_ids)
    if chinese:
        answer = (
            f"这是本地 {copy['zh_label']} 治疗边界解释，不是 API 综合回答；本次没有调用 API。 [llm_inference]\n\n"
            "## 直接回答\n"
            f"{copy['zh_label']} 的“怎么治疗”不能在这个 vault 里被直接写成处方或治疗排名。更安全的做法是先回答：库里哪些治疗/管理分支有证据、哪些只是边界或研究问题。 "
            f"[source_supported_conclusion: {cited}]\n\n"
            "## 当前能安全说什么\n"
            f"{copy['safe']} [source_supported_conclusion: {cited}]\n\n"
            "## 不能说过头的地方\n"
            f"- {copy['cannot']} [source_supported_conclusion: {cited}]\n"
            "- 这不是兽医诊疗建议，也不替代线下兽医判断。 [llm_inference]\n\n"
            "## 下一步\n"
            f"读 {copy['next']}。如果要进入 API synthesis，应先明确是治疗证据比较、label/监管边界、endpoint 设计，还是普通管理解释。"
        )
    else:
        answer = (
            f"This is a local {copy['en_label']} treatment-boundary answer, not API synthesis. No API call was made. [llm_inference]\n\n"
            "## Direct Answer\n"
            f"A treatment question should not be turned into a prescription or treatment ranking in this vault. The safer first answer is which treatment or management branches have evidence, which are bounded, and which remain research questions. "
            f"[source_supported_conclusion: {cited}]\n\n"
            "## What Can Be Said Safely\n"
            f"{copy['safe']} [source_supported_conclusion: {cited}]\n\n"
            "## Do Not Overstate\n"
            f"- {copy['cannot']} [source_supported_conclusion: {cited}]\n"
            "- This is not veterinary medical advice and does not replace a clinician's judgment. [llm_inference]\n\n"
            "## Next Step\n"
            f"Read {copy['next']}. If API synthesis is needed, first specify whether the question is treatment evidence comparison, label/regulatory boundary, endpoint design, or plain management explanation."
        )
    return answer, source_ids


def choose_local_explanation_surface(question: str, disease: str) -> Optional[str]:
    """Pick a deterministic ordinary-user answer surface for free mode."""
    lowered = question.lower()
    # Research-oriented endpoint/evaluation queries
    endpoint_keywords = ["endpoint", "efficacy", "trial", "outcome", "评价", "指标", "药效", "疗效评价", "评估", "判断疗效"]
    treatment_evidence_keywords = ["治疗证据", "疗效证据", "treatment evidence", "gs-441524", "remdesivir", "抗病毒"]

    if disease == "ckd" and any(term in lowered for term in ["endpoint", "efficacy", "trial", "outcome"]):
        return "ckd_endpoint"
    # FIP endpoint/evaluation queries (research-oriented)
    if disease == "fip" and any(term in lowered or term in question for term in endpoint_keywords):
        return "fip_endpoint"
    # FIP treatment evidence queries (research-oriented)
    if disease == "fip" and any(term in lowered or term in question for term in treatment_evidence_keywords):
        return "fip_treatment_evidence"
    if disease in TREATMENT_BOUNDARY_SOURCES and is_treatment_question(question):
        return f"{disease}_treatment_boundary"
    if disease == "ckd" and any(term in lowered or term in question for term in ["topic index", "主题索引", "index page"]):
        return "ckd_topic_index"
    if disease == "ckd" and is_researcher_overview_question(question):
        return "ckd_researcher_overview"
    if disease == "ckd" and is_local_explanation_question(question):
        return "ckd_overview"
    if disease == "fip" and is_local_explanation_question(question):
        return "fip_overview"
    if disease == "fip" and any(term in lowered or term in question for term in ["recogn", "diagnos", "识别", "诊断", "怎么看"]):
        return "fip_recognition"
    if disease == "hcm" and is_local_explanation_question(question):
        return "hcm_overview"
    if disease == "ibd" and any(term in lowered or term in question for term in ["lymphoma", "淋巴瘤", "区分", "differentiat"]):
        return "ibd_lymphoma"
    if disease == "ibd" and is_local_explanation_question(question):
        return "ibd_overview"
    if disease == "diabetes" and is_local_explanation_question(question):
        return "diabetes_overview"
    if disease == "fcv" and is_local_explanation_question(question):
        return "fcv_overview"
    if disease == "obesity" and is_local_explanation_question(question):
        return "obesity_overview"
    if disease == "cancer" and is_local_explanation_question(question):
        return "cancer_overview"
    return None


def build_local_explanation(surface: str, chinese: bool) -> tuple[str, list[str]]:
    """Build a no-API explanation for supported high-visibility surfaces."""
    if surface.endswith("_treatment_boundary"):
        disease = surface.removesuffix("_treatment_boundary")
        return build_treatment_boundary_explanation(disease, chinese)
    builders = {
        "ckd_topic_index": build_ckd_topic_index,
        "ckd_researcher_overview": build_ckd_researcher_overview,
        "ckd_overview": build_ckd_local_explanation,
        "ckd_endpoint": build_ckd_endpoint_explanation,
        "fip_overview": build_fip_local_explanation,
        "fip_recognition": build_fip_recognition_explanation,
        "fip_endpoint": build_fip_endpoint_explanation,
        "fip_treatment_evidence": build_fip_treatment_evidence_explanation,
        "hcm_overview": build_hcm_local_explanation,
        "ibd_overview": build_ibd_local_explanation,
        "ibd_lymphoma": build_ibd_lymphoma_explanation,
        "diabetes_overview": build_diabetes_local_explanation,
        "fcv_overview": build_fcv_local_explanation,
        "obesity_overview": build_obesity_local_explanation,
        "cancer_overview": build_cancer_local_explanation,
    }
    return builders[surface](chinese)


def run_app_local_query_core(
    question: str,
    vault_root: Path,
    source_index: dict[str, Path],
    disease_hint: Optional[str] = None,
    preferred_source_ids: Optional[list[str]] = None,
    search_limit: int = 8,
    on_status=None,
    allow_external_search: bool = False,
) -> dict:
    """No-API local search path used by the Streamlit app."""
    if on_status:
        on_status("Searching local vault...")

    chinese = detect_chinese(question)
    disease = disease_hint or infer_local_disease(question)
    terms = local_search_terms(question, disease)
    results_by_file: dict[str, dict] = {}
    for scope in ("raw", "topics"):
        for term in terms:
            for result in vault_search(term, vault_root, scope=scope, limit=search_limit):
                item = results_by_file.setdefault(result["file"], dict(result, score=0, matched_terms=[]))
                item["score"] += int(result.get("matches", 0))
                if term not in item["matched_terms"]:
                    item["matched_terms"].append(term)
    results = sorted(results_by_file.values(), key=lambda r: (-int(r["score"]), r["file"]))[:search_limit]

    loaded_paths: set[Path] = set()
    loaded_source_ids: list[str] = []
    selected_results: list[dict] = []
    for result in results:
        rel = result["file"]
        path = (vault_root / rel).resolve()
        try:
            path.relative_to(vault_root.resolve())
        except ValueError:
            continue
        if path.exists():
            loaded_paths.add(path)
            selected_results.append(result)
        sid = result.get("id") or ""
        if sid.startswith("src-") and sid in source_index and sid not in loaded_source_ids:
            loaded_source_ids.append(sid)
        if len(selected_results) >= 6:
            break

    if preferred_source_ids:
        for sid in preferred_source_ids:
            path = source_index.get(sid)
            if path and path.exists():
                loaded_paths.add(path)
                if sid not in loaded_source_ids:
                    loaded_source_ids.append(sid)

    has_sirna = "sirna" in question.lower()
    snippets = " ".join(" ".join(r.get("snippets", [])) + " " + str(r.get("title", "")) for r in selected_results)
    has_direct_sirna = "sirna" in snippets.lower()
    is_explanation = is_local_explanation_question(question)
    explanation_surface = choose_local_explanation_surface(question, disease)

    # Research-mode: structured literature search output (agent.ii.inc style)
    if is_research_mode_query(question) and not explanation_surface:
        if on_status:
            status_msg = "研究工作台：检索本地知识库 + PubMed..." if chinese else "Research Workspace: searching local vault + PubMed..."
            on_status(status_msg)
        # PubMed E-utilities is free (no API key needed) - include external by default
        output_chinese = prefers_chinese(question)

        # Get both formatted output and structured data
        answer, research_source_ids = handle_research_query(question, chinese=output_chinese, include_external=True)
        structured_result = handle_research_query_structured(question, chinese=output_chinese, include_external=True)

        for sid in research_source_ids:
            path = source_index.get(sid)
            if path and path.exists():
                loaded_paths.add(path)
                if sid not in loaded_source_ids:
                    loaded_source_ids.append(sid)

        # Collect figures from disk that match any of the loaded_source_ids
        figures_used = []
        if disease:
            images_dir = VAULT_ROOT / "raw" / "images" / disease.lower()
            if images_dir.exists():
                for file_path in images_dir.iterdir():
                    if file_path.is_file() and file_path.name.startswith("src-"):
                        # Find which source id it matches
                        for sid in loaded_source_ids:
                            if file_path.name.startswith(sid):
                                rel_path = f"raw/images/{disease.lower()}/{file_path.name}"
                                figures_used.append({
                                    "source_id": sid,
                                    "file": rel_path,
                                    "described_in_answer": True
                                })
                                break

        research_trace = [
            {
                "step": "Interpreted query",
                "detail": f"disease={disease}; question_type=research_search; engine=local",
            },
            {
                "step": "Searched literature",
                "detail": f"sources={len(loaded_source_ids)}; api_calls=0",
                "items": [{"source_id": sid} for sid in loaded_source_ids[:12]],
            },
        ]
        return {
            "answer": answer,
            "figures_used": figures_used,
            "disease": disease,
            "question_type": "research_search",
            "answer_mode": "research_search",
            "hops_used": 0,
            "loaded_paths": loaded_paths,
            "loaded_source_ids": loaded_source_ids,
            "first_family_loaded": "local-search",
            "research_trace": research_trace,
            "est_tokens": 0,
            "retrieval_events": [],
            "source_snapshots": [],
            "workspace_data": structured_result,
        }

    if explanation_surface:
        answer, explanation_source_ids = build_local_explanation(explanation_surface, chinese)
        for sid in explanation_source_ids:
            path = source_index.get(sid)
            if path and path.exists():
                loaded_paths.add(path)
                if sid not in loaded_source_ids:
                    loaded_source_ids.append(sid)
        evidence_lines = []
        for result in selected_results[:5]:
            rid = result.get("id") or result["file"]
            title = result.get("title") or result["file"]
            matched = ", ".join(result.get("matched_terms", [])) or "n/a"
            evidence_lines.append(f"- `{rid}` — {title}; matched terms: {matched}")
        if evidence_lines:
            if chinese:
                answer += "\n\n## 本地命中\n" + "\n".join(evidence_lines)
            else:
                answer += "\n\n## Local Hits\n" + "\n".join(evidence_lines)
    elif chinese:
        if has_sirna and not has_direct_sirna:
            lead = f"本地库目前没有找到“{question}”的直接证据，尤其没有找到 `{disease}` 与 `siRNA` 同时成立的 source card。这个结果没有调用 API。 [llm_inference]"
        else:
            lead = "这是本地 vault 检索结果，不是 API 综合回答；本次没有调用 API。 [llm_inference]"
        hit_header = "## 本地命中"
        diff_header = "## 和 Google 搜索的差别"
        next_header = "## 下一步"
        no_hits = "- 没有本地命中。"
        diff_lines = [
            "- 这里只查已经入库的 source cards 和 topic pages，不把未入库网页当证据。",
            "- free mode 适合判断“库里有没有/缺什么”，不会花 OpenRouter 或 Anthropic token。",
            "- 需要跨源判断、研究问题生成、证据链压缩时，再手动打开 API synthesis。",
        ]
        next_line = "如果这是新方向，先做 PubMed/DOI intake；没有 source card 前，不生成药效结论。"
    else:
        if has_sirna and not has_direct_sirna:
            lead = f"The local vault does not currently contain direct evidence for `{question}`, especially no source card connecting `{disease}` with `siRNA`. No API call was made. [llm_inference]"
        else:
            lead = "This is local vault retrieval, not API synthesis. No API call was made. [llm_inference]"
        hit_header = "## Local hits"
        diff_header = "## Difference from Google search"
        next_header = "## Next step"
        no_hits = "- No local hits."
        diff_lines = [
            "- This searches only source cards and topic pages already in the vault.",
            "- Free mode is for checking what the vault has or lacks without spending API tokens.",
            "- Use API synthesis only when you need cross-source judgment or research-question shaping.",
        ]
        next_line = "For a new direction, run PubMed/DOI intake first; do not generate efficacy conclusions before source cards exist."

    if not explanation_surface:
        evidence_lines: list[str] = []
        for result in selected_results[:5]:
            raw_rid = result.get("id") or result["file"]
            raw_title = result.get("title") or result["file"]
            
            # Clean ID: get stem (no suffix or folders)
            rid = Path(raw_rid).stem
            
            # Clean Title: map to paper title, or humanize topic name
            if "/" in raw_title or "\\" in raw_title or raw_title.endswith(".md"):
                stem = Path(raw_title).stem
                mapped_title = get_source_titles().get(stem)
                if mapped_title:
                    title = mapped_title
                else:
                    # Clean up topic names e.g., topic-hcm-current-state-dashboard -> HCM Current State Dashboard
                    clean_name = stem.replace("topic-", "").replace("-zh", "").replace("-", " ")
                    title = " ".join(w.capitalize() for w in clean_name.split())
                    acronyms = {"Hcm": "HCM", "Ckd": "CKD", "Fip": "FIP", "Ibd": "IBD", "Fcv": "FCV", "Pmd": "PMD", "Pk": "PK", "Pd": "PD"}
                    title = " ".join(acronyms.get(w, w) for w in title.split())
            else:
                title = raw_title
                
            matched = ", ".join(result.get("matched_terms", [])) or "n/a"
            line = f"- **`{rid}`** — {title} (匹配词: {matched})" if chinese else f"- **`{rid}`** — {title} (matched: {matched})"
            
            # Clean snippets: remove YAML frontmatter to prevent raw metadata dump
            snippets = result.get("snippets", [])
            if snippets:
                cleaned_snippets = []
                for s in snippets:
                    lines = s.split("\n")
                    cleaned_lines = []
                    in_frontmatter = False
                    for l_str in lines:
                        l_strip = l_str.strip()
                        # Toggle frontmatter flag on triple dashes
                        if l_strip == "---":
                            in_frontmatter = not in_frontmatter
                            continue
                        if in_frontmatter:
                            continue
                        # Skip lines that look like frontmatter keys (e.g. id: xxx, title: xxx)
                        if re.match(r"^[a-zA-Z_]+:\s*.*$", l_strip):
                            continue
                        cleaned_lines.append(l_str)
                    cleaned_snippet = "\n".join(cleaned_lines).strip()
                    if cleaned_snippet:
                        cleaned_snippets.append(f"  > ... {cleaned_snippet} ...")
                if cleaned_snippets:
                    line += "\n" + "\n".join(cleaned_snippets)
            evidence_lines.append(line)
        if not evidence_lines:
            evidence_lines.append(no_hits)

        guide_section = ""
        lang_key = "zh" if chinese else "en"
        if disease in DISEASE_GUIDE[lang_key]:
            guide = DISEASE_GUIDE[lang_key][disease]
            if chinese:
                guide_section = f"## 推荐提问引导\n您当前提问的内容涉及 **{guide['name']}**。若您希望获取本地 Vault 对该疾病的专家深度解答，可尝试以下推荐提问方式：\n"
                for q, desc in guide["queries"]:
                    guide_section += f"- **“{q}”** ({desc})\n"
            else:
                guide_section = f"## Recommended Queries\nYour question concerns **{guide['name']}**. For in-depth expert explanations in the local vault, try asking:\n"
                for q, desc in guide["queries"]:
                    guide_section += f"- **\"{q}\"** ({desc})\n"
        else:
            if chinese:
                guide_section = (
                    "## 本地知识库覆盖范围\n"
                    "目前本地 Vault 覆盖了以下猫科疾病的主题：**猫慢性肾脏病 (CKD)**、**猫传染性腹膜炎 (FIP)**、**猫炎症性肠病 (IBD)**、**猫肥厚型心肌病 (HCM)**、**猫杯状病毒 (FCV)**、**猫糖尿病**、**猫肥胖症** 及 **猫恶性肿瘤**。\n"
                    "如果您正在研究上述疾病之一，可以尝试输入上述疾病的名称或尝试更具体的机制问题。如果需要更广泛的文献研究，请启用 API 合成模式。"
                )
            else:
                guide_section = (
                    "## Local Vault Coverage\n"
                    "The local Vault currently covers: **CKD**, **FIP**, **IBD**, **HCM**, **FCV**, **Diabetes**, **Obesity**, and **Cancer**.\n"
                    "If you are researching one of these topics, please use more specific clinical terms. For broader synthesis, enable API mode."
                )

        answer = (
            f"{lead}\n\n"
            f"{hit_header}\n" + "\n".join(evidence_lines) + "\n\n"
            f"{guide_section}\n\n"
            f"{diff_header}\n" + "\n".join(diff_lines) + "\n\n"
            f"{next_header}\n{next_line}"
        )

    research_trace = [
        {
            "step": "Interpreted query",
            "detail": f"disease={disease}; question_type={'overview' if explanation_surface else 'local_search'}; engine=local",
        },
        {
            "step": "Searched vault",
            "detail": f"terms={', '.join(terms)}; results={len(results)}; api_calls=0",
            "items": [
                {"file": r["file"], "id": r.get("id") or "", "matches": r.get("score", r.get("matches", 0))}
                for r in results[:8]
            ],
        },
        {
            "step": "Loaded evidence",
            "detail": f"source_cards={len(loaded_source_ids)}; files={len(loaded_paths)}; api_calls=0",
            "items": [{"source_id": sid} for sid in loaded_source_ids[:12]],
        },
    ]
    if allow_external_search and is_local_search_sparse(results, loaded_source_ids):
        if on_status:
            on_status("Local results sparse, searching PubMed/Crossref...")
        research_trace.append(build_external_search_trace(question, disease))
    research_trace.append({
        "step": "Returned local answer",
        "detail": f"mode={'local_explanation' if explanation_surface else 'free_retrieval'}; surface={explanation_surface or 'none'}; api_calls=0; results={len(selected_results)}",
    })

    return {
        "answer": answer,
        "figures_used": [],
        "disease": disease,
        "question_type": "overview" if explanation_surface else "local_search",
        "answer_mode": "local_explanation" if explanation_surface else "local_search",
        "hops_used": 0,
        "loaded_paths": loaded_paths,
        "loaded_source_ids": loaded_source_ids,
        "first_family_loaded": "local-search",
        "research_trace": research_trace,
        "est_tokens": 0,
        "retrieval_events": [],
        "source_snapshots": [],
    }


def activate_search_result(result: dict) -> None:
    """Open one search result in the main pane and optionally prefer it for query context."""
    st.session_state.active_search_result = {
        "file": result["file"],
        "id": result["id"],
        "title": result["title"],
        "matches": result["matches"],
        "snippet": result["snippets"][0] if result["snippets"] else "",
    }
    source_id = result.get("id")
    if source_id and source_id.startswith("src-"):
        st.session_state.preferred_source_ids = [source_id]
    else:
        st.session_state.preferred_source_ids = []


def clear_search_context() -> None:
    """Clear the active search preview and any preferred source selection."""
    st.session_state.active_search_result = None
    st.session_state.preferred_source_ids = []


def get_search_result_preview(rel_path: str, max_chars: int = 1200) -> str:
    """Read a short, safe preview of the selected search result."""
    # Check if a bilingual version exists and session is Chinese
    if is_session_chinese() and rel_path.endswith(".md") and not rel_path.endswith("-bilingual.md"):
        bilingual_path = rel_path[:-3] + "-bilingual.md"
        if (VAULT_ROOT / bilingual_path).exists():
            rel_path = bilingual_path

    path = (VAULT_ROOT / rel_path).resolve()
    try:
        path.relative_to(VAULT_ROOT.resolve())
    except ValueError:
        return ""

    if not path.exists():
        return ""

    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""

    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4 :].lstrip()

    return text[:max_chars].strip()


def render_search_context_panel() -> None:
    """Render the selected search result in the main pane."""
    active = st.session_state.active_search_result
    if not active:
        return

    with st.expander("Selected reading", expanded=True):
        id_or_path = active["id"] or active["file"]
        title = active.get("title") or active["file"]
        subtitle = f"{active['matches']} matches"
        st.markdown(
            SEARCH_CARD_TEMPLATE.format(
                title=id_or_path,
                subtitle=f"{title} · {subtitle}",
            ),
            unsafe_allow_html=True,
        )

        if active.get("id") and active["id"].startswith("src-"):
            st.markdown(
                f"""
                <div class="vault-inline-note">
                  The next answer will keep this source in focus: <code>{active['id']}</code>.
                </div>
                """,
                unsafe_allow_html=True,
            )

        if active.get("snippet"):
            st.code(active["snippet"][:300], language=None)

        preview = get_search_result_preview(active["file"])
        if preview:
            st.caption(active["file"])
            st.code(preview, language=None)

        panel_id = "search_context"
        if st.button("Clear this selection", key=f"clear_{panel_id}"):
            clear_search_context()
            st.rerun()


def render_notice(body: str, tone: str = "neutral") -> None:
    """Render a small product-style inline notice."""
    cleaned_body = "\n".join(line.strip() for line in str(body).strip().splitlines())
    st.markdown(
        NOTICE_TEMPLATE.format(tone=tone, body=cleaned_body),
        unsafe_allow_html=True,
    )


def highlight_search_snippet(snippet: str, query: str) -> str:
    """Highlight query matches inside a search snippet."""
    escaped = html.escape(snippet)
    if not query.strip():
        return escaped
    try:
        pattern = re.compile(query, re.IGNORECASE)
    except re.error:
        pattern = re.compile(re.escape(query), re.IGNORECASE)
    return pattern.sub(
        lambda m: f"<mark>{html.escape(m.group(0))}</mark>",
        escaped,
    )


def render_search_snippet(snippet: str, query: str) -> None:
    """Render one search snippet with lightweight highlighting."""
    highlighted = highlight_search_snippet(snippet[:220], query)
    st.markdown(
        f"<div class='vault-search-snippet'>{highlighted}</div>",
        unsafe_allow_html=True,
    )


def copy_button(text: str, key: str) -> None:
    """Render a compact markdown export action for assistant answers."""
    st.download_button(
        "Download markdown",
        data=text,
        file_name="ask-the-vault-answer.md",
        mime="text/markdown",
        key=key,
        help="Save the answer with provenance tags intact.",
    )


def render_expert_review_loop(
    *,
    question: str,
    answer: str,
    disease: str,
    question_type: str,
    confidence: str,
    source_ids: list[str],
    key_prefix: str,
    harness_result: Optional[dict] = None,
) -> None:
    """Expose harness verification results and manual expert-review loop."""
    prompt = build_expert_review_prompt(
        question=question,
        answer=answer,
        disease=disease,
        question_type=question_type,
        confidence=confidence,
        source_ids=source_ids,
    )
    stage = expert_review_stage_label()

    # Determine verification status for display
    status_icons = {
        "passed": ("✓", "#4ade80", "Passed"),
        "failed": ("✗", "#f87171", "Failed"),
        "needs_human_review": ("⚠", "#fbbf24", "Needs Review"),
        "pending": ("○", "#94a3b8", "Pending"),
    }
    verification_status = harness_result.get("verification_status", "pending") if harness_result else None
    has_harness = harness_result is not None

    with st.expander("验证结果", expanded=has_harness and verification_status != "passed"):
        # Show harness verification results if available
        if has_harness:
            icon, color, label = status_icons.get(verification_status, ("?", "#94a3b8", "Unknown"))
            st.markdown(
                f"""
                <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;padding:12px;background:#1e293b;border-radius:8px;border-left:4px solid {color}">
                  <span style="font-size:24px;color:{color}">{icon}</span>
                  <div>
                    <div style="font-weight:600;color:{color}">{label}</div>
                    <div style="font-size:12px;color:#8b90a0">
                      Task: {html.escape(harness_result.get('task_type', 'unknown'))} ·
                      Depth: {html.escape(harness_result.get('search_depth', 'unknown'))}
                    </div>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Search depth contract
            depth_satisfied = harness_result.get("search_depth_satisfied", True)
            depth_icon = "✓" if depth_satisfied else "⚠"
            depth_color = "#4ade80" if depth_satisfied else "#fbbf24"
            st.markdown(
                f"""
                <div style="font-size:13px;color:#8b90a0;margin-bottom:8px">
                  <span style="color:{depth_color}">{depth_icon}</span> Search depth contract:
                  <span style="color:{depth_color}">{'Satisfied' if depth_satisfied else 'Not satisfied'}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Gap descriptions
            gap_descriptions = harness_result.get("gap_descriptions", [])
            if gap_descriptions:
                st.markdown(
                    "<div class='vault-panel-label' style='margin-top:12px'>Gaps identified</div>",
                    unsafe_allow_html=True,
                )
                for gap in gap_descriptions[:5]:
                    st.markdown(
                        f"<div style='font-size:13px;color:#fbbf24;margin-left:8px'>· {html.escape(gap)}</div>",
                        unsafe_allow_html=True,
                    )
                if len(gap_descriptions) > 5:
                    st.markdown(
                        f"<div style='font-size:12px;color:#64748b;margin-left:8px'>...and {len(gap_descriptions) - 5} more</div>",
                        unsafe_allow_html=True,
                    )

            # Verification messages
            verification_messages = harness_result.get("verification_messages", [])
            if verification_messages:
                st.markdown(
                    "<div class='vault-panel-label' style='margin-top:12px'>Verification checks</div>",
                    unsafe_allow_html=True,
                )
                for msg in verification_messages[:6]:
                    # Parse message format: "✓ check_name: message" or "✗ check_name: message"
                    msg_color = "#4ade80" if msg.startswith("✓") else "#f87171" if msg.startswith("✗") else "#94a3b8"
                    st.markdown(
                        f"<div style='font-size:13px;color:{msg_color};margin-left:8px'>{html.escape(msg)}</div>",
                        unsafe_allow_html=True,
                    )
                if len(verification_messages) > 6:
                    st.markdown(
                        f"<div style='font-size:12px;color:#64748b;margin-left:8px'>...and {len(verification_messages) - 6} more</div>",
                        unsafe_allow_html=True,
                    )

            st.markdown("<hr style='border-color:#334155;margin:16px 0'>", unsafe_allow_html=True)

        # Manual review section (original content)
        st.markdown(
            f"""
            <div class="vault-inline-note">
              Manual review loop: answer → domain expert critique → claim-level write-back decision.
              Current state: <code>{html.escape(stage)}</code>. Expert chat is review input, not source evidence.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="vault-panel-label">Review checkpoints</div>
            <div class="vault-review-steps">
              <div><code>1</code><span>Choose a domain expert for this exact field and scene.</span></div>
              <div><code>2</code><span>Ask for strict review, not style polishing.</span></div>
              <div><code>3</code><span>Classify each finding as downgrade, endpoint hierarchy, source gap, routing miss, or promotion candidate.</span></div>
              <div><code>4</code><span>Map each finding to chat-only, topic, memo, source queue, query test, or health check.</span></div>
              <div><code>5</code><span>Write back only conservative, source-anchored changes.</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.download_button(
            "Download review prompt",
            data=prompt,
            file_name="ask-the-vault-expert-review-prompt.md",
            mime="text/markdown",
            key=f"{key_prefix}-expert-review-prompt",
            help="Use this prompt in a separate expert-review chat, then stage findings before write-back.",
        )


def strip_legacy_footer(answer: str) -> str:
    """Remove any legacy footer lines from old-style synthesis output."""
    lines = answer.split("\n")
    cleaned: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("Files loaded:") or stripped.startswith("Source cards cited:"):
            continue
        cleaned.append(line)
    return "\n".join(cleaned).rstrip()


def readable_source_titles(source_ids: list[str], limit: int = 4) -> tuple[list[str], int]:
    """Return unique readable source titles plus the hidden remainder count."""
    if not source_ids:
        return [], 0
    source_titles = get_source_titles()
    titles: list[str] = []
    for sid in source_ids:
        title = source_titles.get(sid)
        if title and title not in titles:
            titles.append(title)
    return titles[:limit], max(0, len(titles) - limit)


def render_sources_section(source_ids: list[str]) -> None:
    """Render a clean Sources section with paper titles."""
    if not source_ids:
        return
    titles_to_show, hidden_count = readable_source_titles(source_ids, limit=6)
    if not titles_to_show:
        return
    st.markdown(
        "<div class='vault-panel-label' style='margin-top:20px;margin-bottom:8px'>Sources</div>",
        unsafe_allow_html=True,
    )
    for title in titles_to_show:
        st.markdown(
            f"<div style='font-size:13px;color:#8b90a0;margin-bottom:4px'>· {html.escape(title)}</div>",
            unsafe_allow_html=True,
        )
    if hidden_count:
        st.markdown(
            f"<div style='font-size:12px;color:#8b90a0;margin-top:4px'>+ {hidden_count} more source titles loaded</div>",
            unsafe_allow_html=True,
        )


def st_markdown_html(html_str: str) -> None:
    """Render HTML string safely using st.markdown by stripping leading indentation."""
    cleaned = "\n".join(line.lstrip() for line in html_str.splitlines())
    st.markdown(cleaned, unsafe_allow_html=True)


def load_full_source_metadata(source_ids: list[str]) -> list[dict]:
    """
    Load complete source metadata including DOI, PMID, verification_status.

    Returns list of dicts suitable for build_source_displays().
    """
    return load_source_metadata(VAULT_ROOT, source_ids)


def render_verification_badge(harness_result: Optional[dict]) -> None:
    """Render a compact verification status badge next to the evidence profile."""
    if not harness_result:
        return

    status_map = {
        "passed": ("✓", "#4ade80", "验证通过"),
        "failed": ("✗", "#f87171", "验证失败"),
        "needs_human_review": ("⚠", "#fbbf24", "需要审核"),
        "pending": ("○", "#94a3b8", "待验证"),
    }

    status = harness_result.get("verification_status", "pending")
    icon, color, label = status_map.get(status, ("?", "#94a3b8", "未知"))
    depth_satisfied = harness_result.get("search_depth_satisfied", True)
    depth_icon = "✓" if depth_satisfied else "⚠"
    depth_color = "#4ade80" if depth_satisfied else "#fbbf24"

    badge_html = f"""
    <div style="display:inline-flex;align-items:center;gap:8px;margin:8px 0;padding:6px 12px;background:rgba(30,30,35,0.6);border-radius:4px;font-size:12px;">
        <span style="color:{color};font-weight:500;">{icon} {html.escape(label)}</span>
        <span style="color:#64748b;">|</span>
        <span style="color:{depth_color};">{depth_icon} 深度合约{'满足' if depth_satisfied else '不满足'}</span>
    </div>
    """
    st_markdown_html(badge_html)


def render_depth_contract_warning(harness_result: Optional[dict]) -> None:
    """Render a prominent warning when depth contract is not satisfied in Deep/Audit modes."""
    if not harness_result:
        return

    depth_satisfied = harness_result.get("search_depth_satisfied", True)
    search_depth = harness_result.get("search_depth", "standard")

    # Only show prominent warning for Deep and Audit modes when contract not satisfied
    if depth_satisfied or search_depth not in ("deep", "evidence_audit"):
        return

    depth_failures = harness_result.get("search_depth_failures", [])
    depth_label = "深度研究" if search_depth == "deep" else "证据审计"

    warning_html = f"""
    <div style="margin:12px 0;padding:12px 16px;background:rgba(251,191,36,0.1);border:1px solid rgba(251,191,36,0.3);border-radius:8px;">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px">
            <span style="font-size:20px">⚠️</span>
            <span style="font-weight:600;color:#fbbf24">{depth_label}模式深度合约未满足</span>
        </div>
        <div style="font-size:13px;color:#94a3b8;margin-bottom:8px">
            此模式要求更多来源或来源多样性，当前结果可能不够全面。
        </div>
    """

    if depth_failures:
        warning_html += "<div style='font-size:12px;color:#8b90a0'>"
        for failure in depth_failures[:3]:
            warning_html += f"<div>· {html.escape(failure)}</div>"
        warning_html += "</div>"

    warning_html += """
        <div style="margin-top:12px;font-size:12px;color:#64748b">
            建议: 尝试更具体的问题，或启用外部搜索获取更多来源
        </div>
    </div>
    """
    st_markdown_html(warning_html)


def render_evidence_profile_v2(profile: "EvidenceProfile") -> None:
    """Render factual evidence profile (replaces confidence badges)."""
    if not RESULT_PRESENTATION_AVAILABLE:
        return

    summary = profile.get_summary_text()
    authority_label = "自动生成，未经人工审核" if profile.authority_state.value == "automated" else "已经人工审核"

    # Build profile HTML
    profile_html = f"""
    <div class="vault-evidence-profile" style="margin:12px 0;padding:12px 16px;background:rgba(30,30,35,0.8);border:1px solid rgba(255,255,255,0.08);border-radius:6px;">
        <div style="display:flex;flex-wrap:wrap;gap:12px;align-items:center;font-size:13px;color:#8b90a0;">
            <span>{html.escape(summary)}</span>
            <span class="evidence-depth-tag" style="font-size:11px;opacity:0.7;">{html.escape(authority_label)}</span>
        </div>
    """

    # Add provenance breakdown if there's content
    breakdown = profile.get_provenance_breakdown()
    if breakdown:
        profile_html += """
        <div style="margin-top:8px;display:flex;flex-wrap:wrap;gap:16px;font-size:12px;">
            <span style="color:#6b7280;">答案构成:</span>
        """
        for item in breakdown:
            profile_html += f"""
            <span style="color:#8b90a0;">{item['icon']} {html.escape(item['label'])}: {item['count']}处</span>
            """
        profile_html += "</div>"

    profile_html += "</div>"

    # Add sparse warning if needed
    if profile.is_sparse():
        profile_html += """
        <div style="margin:8px 0;padding:8px 12px;background:rgba(202,138,4,0.1);border-left:3px solid #ca8a04;font-size:12px;color:#ca8a04;">
            ⚠️ 证据较薄 — 来源数量有限，建议进一步查证
        </div>
        """

    st_markdown_html(profile_html)


def render_source_card_v2(card: "SourceDisplay", key_prefix: str = "") -> None:
    """Render a single source card with canonical link, IF, citations, and expandable sections."""
    if not RESULT_PRESENTATION_AVAILABLE:
        return

    is_zh = is_session_chinese()

    # Build link element
    link_html = ""
    if card.has_valid_link():
        link_text = card.get_link_text()
        link_html = f"""<a href="{html.escape(card.canonical_url)}" target="_blank" rel="noopener"
            style="color:#60a5fa;text-decoration:none;font-size:12px;">[{link_text} ↗]</a>"""
    else:
        link_html = '<span style="color:#6b7280;font-size:12px;">链接不可用</span>'

    # Year text
    year_text = f" | {card.publication_year}" if card.publication_year else ""

    # Build IF and citation tags
    metric_tags = []
    if card.impact_factor:
        if_label = card.impact_factor_label or f"IF: {card.impact_factor:.1f}"
        metric_tags.append(
            f'<span style="background:rgba(234,179,8,0.12);color:#eab308;padding:2px 6px;border-radius:3px;">{html.escape(if_label)}</span>'
        )
    if card.citation_count is not None:
        cite_label = card.citation_count_label or (f"被引: {card.citation_count}" if is_zh else f"Citations: {card.citation_count}")
        metric_tags.append(
            f'<span style="background:rgba(96,165,250,0.12);color:#60a5fa;padding:2px 6px;border-radius:3px;">{html.escape(cite_label)}</span>'
        )
    metrics_html = " ".join(metric_tags)

    metadata_bits = []
    if card.journal:
        metadata_bits.append(html.escape(card.journal))
    if card.source_family_label:
        metadata_bits.append(f"家族：{html.escape(card.source_family_label)}" if is_zh else f"Family: {html.escape(card.source_family_label)}")
    if card.species_label:
        metadata_bits.append(f"种属：{html.escape(card.species_label)}" if is_zh else f"Species: {html.escape(card.species_label)}")
    if card.decision_grade_label:
        metadata_bits.append(f"决策：{html.escape(card.decision_grade_label)}" if is_zh else f"Grade: {html.escape(card.decision_grade_label)}")
    if card.safest_use:
        metadata_bits.append(f"最安全用途：{html.escape(card.safest_use)}" if is_zh else f"Safest use: {html.escape(card.safest_use)}")
    if not metadata_bits and card.publish_date:
        metadata_bits.append(f"发布日期：{html.escape(card.publish_date)}" if is_zh else f"Published: {html.escape(card.publish_date)}")

    metadata_line = ""
    if metadata_bits:
        metadata_line = (
            "<div style=\"margin-top:6px;font-size:12px;color:#8b90a0;line-height:1.5;\">"
            + " · ".join(metadata_bits)
            + "</div>"
        )

    card_html = f"""
    <div class="vault-source-card" style="margin:8px 0;padding:10px 14px;background:rgba(30,30,35,0.6);border:1px solid rgba(255,255,255,0.06);border-radius:6px;">
        <div style="font-size:14px;color:#e5e7eb;margin-bottom:4px;">{html.escape(card.title)}</div>
        <div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-size:12px;color:#8b90a0;">
            <span class="depth-tag" style="background:rgba(22,163,74,0.12);color:#16a34a;padding:2px 6px;border-radius:3px;">{html.escape(card.evidence_depth_label)}</span>
            {metrics_html}
            <span>{html.escape(card.source_type_label)}{year_text}</span>
            {link_html}
        </div>
        {metadata_line}
    </div>
    """
    st_markdown_html(card_html)

    # Render expandable sections for Abstract, Methods, References, and Cited By
    card_id = card._internal_id or card.title[:20]
    has_abstract = bool(card.abstract_text and card.abstract_text.strip())
    has_methods = bool(card.methods_summary and card.methods_summary.strip())
    has_refs = bool(card.reference_ids)

    # P3: Check for "Cited By" papers from citation graph
    source_id = getattr(card, '_internal_id', None) or card.title[:20]
    cited_by_links = get_cited_by_links(source_id) if source_id.startswith("src-") else []
    has_cited_by = bool(cited_by_links)

    # State keys
    state_key_abs = f"show_abs_{key_prefix}_{card_id}"
    state_key_meth = f"show_meth_{key_prefix}_{card_id}"
    state_key_refs = f"show_refs_{key_prefix}_{card_id}"
    state_key_cited = f"show_cited_{key_prefix}_{card_id}"

    if has_abstract or has_methods or has_refs or has_cited_by:
        # Use columns to create inline expander buttons
        expand_cols = st.columns([1, 1, 1, 1, 2])
        with expand_cols[0]:
            if has_abstract:
                abstract_label = "摘要" if is_zh else "Abstract"
                if st.button(f"📄 {abstract_label}", key=f"abs_{key_prefix}_{card_id}", use_container_width=True):
                    st.session_state[state_key_abs] = not st.session_state.get(state_key_abs, False)
        with expand_cols[1]:
            if has_methods:
                methods_label = "方法" if is_zh else "Methods"
                if st.button(f"🔬 {methods_label}", key=f"meth_{key_prefix}_{card_id}", use_container_width=True):
                    st.session_state[state_key_meth] = not st.session_state.get(state_key_meth, False)
        with expand_cols[2]:
            if has_refs:
                refs_label = f"参考文献 ({len(card.reference_ids)})" if is_zh else f"References ({len(card.reference_ids)})"
                if st.button(f"📚 {refs_label}", key=f"refs_{key_prefix}_{card_id}", use_container_width=True):
                    st.session_state[state_key_refs] = not st.session_state.get(state_key_refs, False)
        with expand_cols[3]:
            if has_cited_by:
                cited_label = f"被引用 ({len(cited_by_links)})" if is_zh else f"Cited By ({len(cited_by_links)})"
                if st.button(f"🔗 {cited_label}", key=f"cited_{key_prefix}_{card_id}", use_container_width=True):
                    st.session_state[state_key_cited] = not st.session_state.get(state_key_cited, False)

        # Show expanded content
        if st.session_state.get(state_key_abs):
            st.markdown(
                f"<div style='margin:8px 0 12px 0;padding:10px 14px;background:rgba(20,20,25,0.8);border-left:3px solid #60a5fa;font-size:13px;color:#c9cdd5;line-height:1.6;'>{html.escape(card.abstract_text)}</div>",
                unsafe_allow_html=True,
            )
        if st.session_state.get(state_key_meth):
            st.markdown(
                f"<div style='margin:8px 0 12px 0;padding:10px 14px;background:rgba(20,20,25,0.8);border-left:3px solid #22c55e;font-size:13px;color:#c9cdd5;line-height:1.6;'>{html.escape(card.methods_summary)}</div>",
                unsafe_allow_html=True,
            )
        if st.session_state.get(state_key_refs):
            # Use citation graph for richer reference display
            source_id = getattr(card, '_internal_id', None) or card.title[:20]
            ref_links = get_reference_links(source_id) if source_id.startswith("src-") else []

            if ref_links:
                # Rich reference display with vault status indicators
                refs_html = "<div style='margin:8px 0 12px 0;padding:10px 14px;background:rgba(20,20,25,0.8);border-left:3px solid #a855f7;font-size:13px;color:#c9cdd5;'>"
                refs_html += f"<div style='margin-bottom:8px;color:#a855f7;font-weight:500;'>{'引用的文献' if is_zh else 'References'}:</div>"
                for ref in ref_links[:10]:
                    if ref["in_vault"]:
                        # In vault - clickable
                        vault_badge = '<span style="background:rgba(34,197,94,0.15);color:#22c55e;padding:1px 4px;border-radius:3px;font-size:11px;margin-left:6px;">✓ 库内</span>' if is_zh else '<span style="background:rgba(34,197,94,0.15);color:#22c55e;padding:1px 4px;border-radius:3px;font-size:11px;margin-left:6px;">✓ in vault</span>'
                        title_text = ref.get("title") or user_visible_source_label(ref.get("source_id", ""), "本地库内文献" if is_zh else "vault paper")
                        year_text = f" ({ref['year']})" if ref.get("year") else ""
                        refs_html += f"<div style='margin-bottom:4px;'>├─ {html.escape(title_text)}{year_text}{vault_badge}</div>"
                    else:
                        # External - not in vault
                        external_badge = '<span style="background:rgba(239,68,68,0.15);color:#ef4444;padding:1px 4px;border-radius:3px;font-size:11px;margin-left:6px;">✗ 未收录</span>' if is_zh else '<span style="background:rgba(239,68,68,0.15);color:#ef4444;padding:1px 4px;border-radius:3px;font-size:11px;margin-left:6px;">✗ not in vault</span>'
                        external_label = ref.get("title") or ("外部参考文献" if is_zh else "External reference")
                        refs_html += f"<div style='margin-bottom:4px;'>├─ {html.escape(external_label)}{external_badge}</div>"
                if len(ref_links) > 10:
                    more_label = f"...还有 {len(ref_links) - 10} 篇" if is_zh else f"...and {len(ref_links) - 10} more"
                    refs_html += f"<div style='color:#8b90a0;margin-top:4px;'>└─ {more_label}</div>"
                refs_html += "</div>"
            else:
                # Fallback to simple reference_ids display
                refs_html = "<div style='margin:8px 0 12px 0;padding:10px 14px;background:rgba(20,20,25,0.8);border-left:3px solid #a855f7;font-size:13px;color:#c9cdd5;'>"
                for ref_id in card.reference_ids[:10]:
                    ref_label = user_visible_source_label(ref_id, "本地参考文献" if is_zh else "Vault reference")
                    refs_html += f"<div style='margin-bottom:4px;'>· {html.escape(ref_label)}</div>"
                if len(card.reference_ids) > 10:
                    more_label = f"...还有 {len(card.reference_ids) - 10} 篇" if is_zh else f"...and {len(card.reference_ids) - 10} more"
                    refs_html += f"<div style='color:#8b90a0;'>{more_label}</div>"
                refs_html += "</div>"
            st.markdown(refs_html, unsafe_allow_html=True)

        # P3: Show "Cited By" content
        if st.session_state.get(state_key_cited) and cited_by_links:
            cited_html = "<div style='margin:8px 0 12px 0;padding:10px 14px;background:rgba(20,20,25,0.8);border-left:3px solid #f59e0b;font-size:13px;color:#c9cdd5;'>"
            header_label = "引用本文的文献" if is_zh else "Papers citing this work"
            cited_html += f"<div style='margin-bottom:8px;color:#f59e0b;font-weight:500;'>{header_label}:</div>"
            for citing in cited_by_links[:10]:
                title_text = citing.get("title") or user_visible_source_label(citing.get("source_id", ""), "本地库内文献" if is_zh else "vault paper")
                year_text = f" ({citing['year']})" if citing.get("year") else ""
                citation_badge = ""
                if citing.get("citation_count"):
                    citation_badge = f'<span style="background:rgba(245,158,11,0.15);color:#f59e0b;padding:1px 4px;border-radius:3px;font-size:11px;margin-left:6px;">被引:{citing["citation_count"]}</span>'
                cited_html += f"<div style='margin-bottom:4px;'>├─ {html.escape(title_text)}{year_text}{citation_badge}</div>"
            if len(cited_by_links) > 10:
                more_label = f"...还有 {len(cited_by_links) - 10} 篇" if is_zh else f"...and {len(cited_by_links) - 10} more"
                cited_html += f"<div style='color:#8b90a0;margin-top:4px;'>└─ {more_label}</div>"
            cited_html += "</div>"
            st.markdown(cited_html, unsafe_allow_html=True)


def render_sources_section_v2(source_cards: list["SourceDisplay"], key_prefix: str = "") -> None:
    """Render sources section with canonical links (v2)."""
    if not source_cards:
        return

    st.markdown(
        "<div class='vault-panel-label' style='margin-top:20px;margin-bottom:8px'>来源文献</div>",
        unsafe_allow_html=True,
    )

    # Show first 4 expanded, rest collapsed
    for card in source_cards[:4]:
        render_source_card_v2(card, key_prefix=key_prefix)

    if len(source_cards) > 4:
        with st.expander(f"查看更多 ({len(source_cards) - 4} 篇)", expanded=False):
            for card in source_cards[4:]:
                render_source_card_v2(card, key_prefix=key_prefix)


def render_next_actions_v2(actions: list, key_prefix: str = "next") -> None:
    """Render task-specific next actions."""
    if not actions:
        return

    st.markdown(
        "<div class='vault-panel-label' style='margin-top:20px;margin-bottom:8px'>下一步</div>",
        unsafe_allow_html=True,
    )

    cols = st.columns(min(len(actions), 2))
    for i, action in enumerate(actions):
        with cols[i % 2]:
            target = str(getattr(action, "target", "") or "").strip()
            label = str(getattr(action, "label", "") or target or "继续检索").strip()
            target = normalize_user_facing_topic_text(target)
            label = normalize_user_facing_topic_text(label)
            action_type = getattr(getattr(action, "action_type", ""), "value", str(getattr(action, "action_type", "")))

            if action_type == "external" and target.startswith(("http://", "https://")):
                st.markdown(
                    f"<a href='{html.escape(target, quote=True)}' target='_blank' rel='noopener' "
                    "style='display:block;padding:10px 14px;background:rgba(30,30,35,0.6);"
                    "border:1px solid rgba(255,255,255,0.08);border-radius:6px;margin-bottom:8px;"
                    "color:#e5e7eb;text-decoration:none;font-size:13px;'>"
                    f"{html.escape(label)} ↗</a>",
                    unsafe_allow_html=True,
                )
                continue

            query = target if target and not target.startswith("/") else label
            if st.button(label, key=f"{key_prefix}-next-action-{i}", use_container_width=True):
                queue_question(query)


def highlight_trace_passage(passage: str, highlight_text: str) -> str:
    """Escape and mark the supporting text inside a source passage."""
    safe_passage = html.escape(passage or "")
    if not passage or not highlight_text:
        return safe_passage
    safe_highlight = html.escape(highlight_text)
    return safe_passage.replace(
        safe_highlight,
        f"<mark class='trace-highlight'>{safe_highlight}</mark>",
        1,
    )


def render_evidence_traces_v2(traces: list["EvidenceTrace"], key_prefix: str = "") -> None:
    """Render claim-level source passage traces."""
    if not traces:
        return

    is_zh = is_session_chinese()
    title = "原文依据" if is_zh else "Source Evidence"
    caption = (
        "每条关键判断都可以回到支撑它的来源片段。分析推断会明确标出人工复核边界。"
        if is_zh else
        "Key judgments can be traced back to the source passage. Inferences are marked for review."
    )
    st.markdown(
        f"""
        <div class="vault-panel-label" style="margin-top:20px;margin-bottom:4px">{html.escape(title)}</div>
        <div style="font-size:12px;color:#7c8494;margin-bottom:8px">{html.escape(caption)}</div>
        """,
        unsafe_allow_html=True,
    )

    for i, trace in enumerate(traces[:8]):
        label = f"{trace.evidence_label} · {trace.source_title}"
        if len(label) > 96:
            label = label[:93] + "..."
        expanded = i == 0 and trace.has_passage_location()
        with st.expander(label, expanded=expanded):
            st.markdown(f"**判断：** {html.escape(trace.claim_text)}")
            source_bits = []
            if trace.section:
                source_bits.append(trace.section)
            if trace.paragraph_id:
                source_bits.append(trace.paragraph_id)
            if source_bits:
                st.caption(" · ".join(source_bits))
            if trace.canonical_url:
                st.markdown(f"[打开来源]({trace.canonical_url})")

            if trace.evidence_type == "llm_inference":
                st.warning("这是分析推断，不是原文直接表述。需要人工复核。" if is_zh else "This is an inference, not direct source wording. Human review needed.")

            if trace.quoted_passage:
                passage_html = highlight_trace_passage(trace.quoted_passage, trace.highlight_text)
                st.markdown(
                    f"""
                    <div class="trace-passage">
                      {passage_html}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                st.info("来源可打开，但当前元数据未定位到具体段落。" if is_zh else "The source is available, but no exact passage is stored yet.")

            if trace.why_it_supports_the_claim:
                st.markdown(f"**为什么支持：** {html.escape(trace.why_it_supports_the_claim)}")

    if len(traces) > 8:
        st.caption(f"还有 {len(traces) - 8} 条依据未展开显示。" if is_zh else f"{len(traces) - 8} more evidence traces hidden.")


def build_presentation_from_answer(
    answer: str,
    question: str,
    source_ids: list[str],
    loaded_source_ids: list[str],
    confidence: str,
    disease: str = "",
    research_trace: list[dict] | None = None,
) -> "ResultPresentation":
    """
    Build ResultPresentation from existing answer data.

    This bridges the old query output format to the new presentation contract.
    """
    if not RESULT_PRESENTATION_AVAILABLE:
        return None

    # Load full source metadata
    all_source_ids = list(set((loaded_source_ids or []) + (source_ids or [])))
    sources = load_full_source_metadata(all_source_ids)

    # Count provenance from answer
    counts = provenance_counts(answer)
    claims = [
        *[{"provenance": "quoted_fact"} for _ in range(counts["quoted"])],
        *[{"provenance": "source_supported_conclusion"} for _ in range(counts["supported"])],
        *[{"provenance": "llm_inference"} for _ in range(counts["inference"])],
    ]

    # Strip legacy footer for clean lead
    cleaned = strip_legacy_footer(answer)

    # Split clean answer into lead and sections based on markdown headers
    lead_parts = []
    sections = []
    
    current_section_title = None
    current_section_content = []
    
    in_lead = True
    for line in cleaned.splitlines():
        if line.startswith("## ") or line.startswith("### "):
            in_lead = False
            if current_section_title is not None or current_section_content:
                sections.append({
                    "title": current_section_title or "",
                    "content": "\n".join(current_section_content).strip()
                })
            current_section_title = line.lstrip("# ").strip()
            current_section_content = []
        else:
            if in_lead:
                lead_parts.append(line)
            else:
                current_section_content.append(line)
                
    if current_section_title is not None or current_section_content:
        sections.append({
            "title": current_section_title or "",
            "content": "\n".join(current_section_content).strip()
        })
        
    lead_text = "\n".join(lead_parts).strip()

    # Build presentation
    return build_result_presentation(
        title="研究回答",
        subtitle=f"基于 {len(sources)} 篇来源",
        lead=lead_text,
        sources=sources,
        claims=claims,
        sections=sections,
        boundary_notice="",
        topic=disease or "feline-research",
        surface_type="vault",
        audience="ordinary",
        language="zh",
        authority_state="automated",
    )


def translate_card_headings(text: str) -> str:
    # Match any level of heading for these terms, e.g. ### quoted_fact
    # Allowing optional trailing whitespace or colon
    text = re.sub(r'^(#{1,6})\s*quoted_fact\s*$', r'\1 直接来源', text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r'^(#{1,6})\s*source_supported_conclusion\s*$', r'\1 来源支持', text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r'^(#{1,6})\s*llm_inference\s*$', r'\1 分析推断', text, flags=re.MULTILINE | re.IGNORECASE)
    return text


def remove_relative_links(text: str) -> str:
    # Match [link text](relative_url) where relative_url doesn't start with http, https, or mailto
    # We replace it with bold text **link text** to keep it styled but remove the fake link
    return re.sub(r'\[([^\]]+)\]\((?!(?:https?://|mailto:))([^\)]+)\)', r'**\1**', text)


def read_markdown_without_frontmatter(path: Path) -> str:
    # Automatic bilingual redirection for Chinese sessions
    if is_session_chinese():
        path_str = str(path)
        if "/topics/" in path_str and path_str.endswith(".md") and not path_str.endswith("-bilingual.md"):
            bilingual_path_str = path_str[:-3] + "-bilingual.md"
            bilingual_path = Path(bilingual_path_str)
            if bilingual_path.exists():
                path = bilingual_path

    try:
        text = path.read_text(encoding="utf-8")
        if text.startswith("---"):
            end = text.find("\n---", 3)
            if end != -1:
                content = text[end + 4:].strip()
                return remove_relative_links(translate_card_headings(content))
        return remove_relative_links(translate_card_headings(text.strip()))
    except Exception as e:
        return f"Error reading file: {e}"


EVIDENCE_LEVEL_MAP = {
    "guideline": "共识指南",
    "regulation": "法规",
    "review": "专家综述",
    "original-study": "原始研究",
    "guidance": "指导意见",
    "case-series": "病例系列",
    "case-report": "个案报告",
    "commentary": "述评/评论",
}

VERIFICATION_STATUS_MAP = {
    "audited": "已核查全文",
    "deep_extracted": "已核查全文",
    "source_checked": "已核对源",
    "abstract_weighted": "基于摘要",
    "title_only": "仅标题",
    "compiled": "已编译",
}


def sanitize_user_facing_markdown(text: str) -> str:
    """Remove raw local file names, .md file links, and paths from user-facing markdown."""
    import re
    from pathlib import Path
    
    # 1. Clean markdown links pointing to local files (e.g., [file.md](file.md))
    def replace_md_link(match):
        label = match.group(1)
        url = match.group(2)
        if url.endswith(".md") or "/" in url or "\\" in url:
            stem = Path(url).stem
            if stem.startswith("src-"):
                return f"**{stem.upper()}**"
            
            # For general md links, format human-friendly title
            label_clean = label.replace(".md", "").replace("-zh", "").replace("-", " ")
            label_clean = " ".join(w.capitalize() for w in label_clean.split())
            acronyms = {"Hcm": "HCM", "Ckd": "CKD", "Fip": "FIP", "Ibd": "IBD", "Fcv": "FCV", "Working": "Working Draft", "En": "(English)", "Zh": "(Chinese)"}
            label_clean = " ".join(acronyms.get(w, w) for w in label_clean.split())
            return f"**{label_clean}**"
        return match.group(0)
    
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_md_link, text)
    
    # 2. Clean standalone md files or paths (e.g. out-ckd-briefing-20260408-round1-working-en.md)
    def replace_md_file(match):
        filename = match.group(0)
        stem = filename.replace(".md", "").replace("-zh", "").replace("-", " ")
        stem_clean = " ".join(w.capitalize() for w in stem.split())
        acronyms = {"Hcm": "HCM", "Ckd": "CKD", "Fip": "FIP", "Ibd": "IBD", "Fcv": "FCV", "Working": "Working Draft", "En": "(English)", "Zh": "(Chinese)"}
        stem_clean = " ".join(acronyms.get(w, w) for w in stem_clean.split())
        return f"**{stem_clean}**"
        
    text = re.sub(r"\b\w+-\w+-briefing-\d+-[\w-]+\.md\b", replace_md_file, text)
    text = re.sub(r"\btopics/[\w/-]+\.md\b", lambda m: f"**{Path(m.group(0)).stem.replace('-', ' ').title()}**", text)
    text = re.sub(r"\braw/papers/[\w/-]+\.md\b", lambda m: f"**{Path(m.group(0)).stem.upper()}**", text)
    return text


def render_translatable_content(doc_id: str, content: str, show_translate_btn: bool, key_prefix: str = "") -> None:
    """Render document markdown content, and optionally provide a one-click AI translation to Chinese."""
    st.markdown(sanitize_user_facing_markdown(content))
    
    if not show_translate_btn:
        return
        
    cache_key = f"trans_{doc_id.replace('/', '_').replace('.', '_').replace('-', '_')}"
    translated_text = st.session_state.get(cache_key, "")
    
    if translated_text:
        st.markdown("---")
        st.markdown("<div style='font-size:13px;color:#14b8a6;font-family:ui-monospace,SFMono-Regular,monospace;text-transform:uppercase;letter-spacing:0.05em;font-weight:600;margin-top:12px;margin-bottom:8px;'>🇨🇳 AI 中文翻译对照</div>", unsafe_allow_html=True)
        st.markdown(sanitize_user_facing_markdown(translated_text))
        if st.button("清除翻译缓存", key=f"clear_{key_prefix}_{cache_key}"):
            del st.session_state[cache_key]
            st.rerun()
    else:
        if st.button("✨ 翻译本段文献 (AI)", key=f"btn_{key_prefix}_{cache_key}"):
            available_backend = None
            client_obj = None
            active_model_name = ""
            
            backends_to_try = []
            if os.environ.get("ANTHROPIC_API_KEY"):
                backends_to_try.append(("anthropic", MODEL))
            if os.environ.get("OPENROUTER_API_KEY"):
                backends_to_try.append(("openrouter", os.environ.get("OPENROUTER_MODEL", OPENROUTER_MODEL)))
            if is_ollama_reachable():
                backends_to_try.append(("ollama", OLLAMA_MODEL))
                
            for b, m in backends_to_try:
                try:
                    client_obj = make_client(b)
                    available_backend = b
                    active_model_name = m
                    break
                except Exception:
                    continue
                    
            if not available_backend:
                st.info("💡 请在左侧侧边栏配置并激活任一 API 引擎（如输入 ANTHROPIC_API_KEY 或启动本地 Ollama），以开启 AI 实时翻译功能。")
                return
                
            with st.spinner("正在通过 AI 翻译文献，请稍候..."):
                try:
                    system_prompt = (
                        "You are an expert veterinary medicine and clinical trial translator. "
                        "Translate the following feline medicine scientific text into fluent, professional, and natural Chinese (简体中文). "
                        "Follow standard veterinary terminology (e.g. creatinine -> 肌酐, proteinuria -> 蛋白尿, non-pharmacological management -> 非药物管理). "
                        "Do not include any commentary or meta-text, return only the translated Markdown."
                    )
                    
                    text_to_translate = content[:2500]
                    if len(content) > 2500:
                        text_to_translate += "\n\n[... 剩余内容由于长度限制已被截断 ...]"
                        
                    messages = [{"role": "user", "content": f"Text to translate:\n\n{text_to_translate}"}]
                    translated = _chat(client_obj, active_model_name, system_prompt, messages, 2548)
                    
                    if translated:
                        st.session_state[cache_key] = translated
                        st.rerun()
                    else:
                        st.error("翻译失败：模型返回了空结果。")
                except Exception as e:
                    st.error(f"翻译过程中出错：{e}")


def render_loaded_documents_section(loaded_paths: Optional[list[str]], initially_expanded: bool = True, key_prefix: str = "") -> None:
    if not loaded_paths:
        return
        
    chinese_session = is_session_chinese()
    st.markdown("<div class='vault-panel-label' style='margin-top:16px;margin-bottom:8px'>匹配的本地文献与文档内容</div>", unsafe_allow_html=True)
    for idx, p_str in enumerate(loaded_paths):
        path = Path(p_str)
        if not path.exists():
            continue
            
        try:
            rel_path = str(path.relative_to(VAULT_ROOT))
        except ValueError:
            rel_path = path.name
            
        filename = path.name
        source_id = path.stem
        
        is_source_card = "raw/papers" in rel_path or "raw/regulations" in rel_path or filename.startswith("src-")
        
        doc_key_prefix = f"{key_prefix}-{idx}"
        if is_source_card:
            # Load metadata
            meta_list = load_source_metadata(VAULT_ROOT, [source_id])
            title = user_visible_source_label(source_id, filename)
            meta_str = ""
            if meta_list and meta_list[0].get("title"):
                meta = meta_list[0]
                title = meta["title"]
                
                author_str = ", ".join(meta.get("authors", []))
                year_str = str(meta.get("year", ""))
                evidence = meta.get("evidence_level", "")
                verification = meta.get("verification_status", "")
                
                meta_parts = []
                if author_str: meta_parts.append(f"**作者**: {author_str}")
                if year_str: meta_parts.append(f"**年份**: {year_str}")
                if evidence: 
                    translated_evidence = EVIDENCE_LEVEL_MAP.get(evidence, evidence)
                    meta_parts.append(f"**证据**: {translated_evidence}")
                if verification: 
                    translated_verification = VERIFICATION_STATUS_MAP.get(verification, verification)
                    meta_parts.append(f"**核查**: {translated_verification}")
                
                meta_str = " | ".join(meta_parts)
                
            expander_title = f"📚 {title}"
            with st.expander(expander_title, expanded=initially_expanded):
                if meta_str:
                    st.markdown(f"<div style='font-size:12px;color:#8b90a0;margin-bottom:8px'>{meta_str}</div>", unsafe_allow_html=True)
                content = read_markdown_without_frontmatter(path)
                render_translatable_content(rel_path, content, chinese_session, key_prefix=doc_key_prefix)
        else:
            expander_title = f"📄 {format_topic_path(rel_path)}"
            with st.expander(expander_title, expanded=initially_expanded):
                content = read_markdown_without_frontmatter(path)
                render_translatable_content(rel_path, content, chinese_session, key_prefix=doc_key_prefix)


def render_query_refinement(refined_query: Optional[str], objectives: Optional[list[str]]) -> None:
    if not refined_query:
        return
        
    obj_items = "".join(f"<li style='margin-bottom:4px;color:#e8eaf0'>{html.escape(obj)}</li>" for obj in objectives if obj) if objectives else ""
    obj_html = f"<ul style='margin:4px 0 0 16px;padding:0;font-size:13px;'>{obj_items}</ul>" if obj_items else ""
    
    st.markdown(
        f"""
        <div style="padding:14px 16px;background:rgba(99,102,241,0.08);border-left:4px solid #6366f1;border-radius:0 8px 8px 0;margin-bottom:20px;">
          <div style="font-size:11px;color:#818cf8;font-family:ui-monospace,SFMono-Regular,monospace;text-transform:uppercase;letter-spacing:0.05em;font-weight:600;margin-bottom:4px;">
            🔍 研究课题精化
          </div>
          <div style="font-size:14px;color:#e8eaf0;font-weight:500;line-height:1.5;">
            {html.escape(refined_query)}
          </div>
          {obj_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_local_query_evaluation(disease: Optional[str], task_type: Optional[str], subqueries: Optional[list[str]]) -> None:
    if not disease and not task_type:
        return
    sub_items = "".join(f"<li style='margin-bottom:2px;color:#8b90a0'>feline {html.escape(disease)} {html.escape(sq)}</li>" for sq in subqueries if sq) if subqueries else ""
    sub_html = f"<ul style='margin:4px 0 0 16px;padding:0;font-size:12px;list-style-type:square;'>{sub_items}</ul>" if sub_items else ""
    
    dis_str = disease.upper() if disease else "UNKNOWN"
    task_labels = {
        "research_search": "文献检索",
    }
    task_str = task_labels.get(task_type or "", task_type.upper() if task_type else "UNKNOWN")
    st.markdown(
        f"""
        <div style="padding:12px 14px;background:rgba(94,234,212,0.06);border-left:4px solid #14b8a6;border-radius:0 6px 6px 0;margin-bottom:18px;">
          <div style="font-size:11px;color:#14b8a6;font-family:ui-monospace,SFMono-Regular,monospace;text-transform:uppercase;letter-spacing:0.05em;font-weight:600;margin-bottom:4px;">
            🔍 检索课题分类与子检索项
          </div>
          <div style="font-size:13px;color:#e8eaf0;line-height:1.5;">
            识别病种: <code style="color:#2dd4bf">{html.escape(dis_str)}</code> | 任务类型: <code style="color:#2dd4bf">{html.escape(task_str)}</code>
          </div>
          {sub_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def split_research_contract(answer: str) -> tuple[Optional[str], str]:
    """Split Research Mode's contract/audit note from the report body."""
    if not answer:
        return None, answer

    markers = [
        "## Research contract and audit note",
        "## 研究范围与审计说明",
    ]
    body_markers = [
        "\n# 研究交付物",
        "\n# Research Deliverables",
        "\n# Research Literature:",
        "\n# 文献检索：",
    ]

    stripped = answer.lstrip()
    if not any(stripped.startswith(marker) for marker in markers):
        return None, answer

    leading_ws_len = len(answer) - len(stripped)
    search_start = leading_ws_len

    body_start = -1
    for marker in body_markers:
        idx = answer.find(marker, search_start)
        if idx != -1:
            body_start = idx + 1
            break

    if body_start == -1:
        return None, answer

    contract = answer[search_start:body_start].strip()
    body = answer[body_start:].lstrip()
    return contract, body


def render_research_contract_panel(answer: str, question_type: str) -> str:
    """
    Render Research Mode contract as a structured audit panel and return body.

    The contract remains in the plain text returned by research_mode.py for CLI
    and saved-output compatibility, but the app presents it separately so the
    report body starts with the actual literature review.
    """
    if question_type != "research_search":
        return answer

    contract, body = split_research_contract(answer)
    if not contract:
        return answer

    is_zh = is_session_chinese() or contract.startswith("## 研究范围")
    title = "研究范围与审计说明" if is_zh else "Research contract and audit note"
    note = (
        "这不是原始思考链，而是本次研究任务的可审计边界：系统如何解释问题、如何排序、以及哪些最新性声明仍需外部验证。"
        if is_zh else
        "This is not raw chain-of-thought. It is the auditable boundary for this research task: interpretation, ranking, and freshness limits."
    )

    with st.expander(title, expanded=True):
        st.markdown(
            f"""
            <div class="vault-inline-note" style="margin-bottom:10px">
              {html.escape(note)}
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(render_provenance(contract), unsafe_allow_html=True)

    return body


def scroll_to_latest_research_result() -> None:
    """Keep research searches at the report start instead of the chat bottom."""
    components.html(
        """
        <script>
        (() => {
          const scrollOnce = () => {
            const doc = window.parent.document;
            const targets = Array.from(doc.querySelectorAll("#research-result-top"));
            const target = targets[targets.length - 1];
            if (!target) {
              window.parent.scrollTo(0, 0);
              return;
            }

            target.scrollIntoView({block: "start", behavior: "auto"});

            const candidates = [
              doc.scrollingElement,
              doc.documentElement,
              doc.body,
              ...Array.from(doc.querySelectorAll("section.main, [data-testid='stAppViewContainer'], [data-testid='stVerticalBlock']"))
            ].filter(Boolean);

            for (const el of candidates) {
              try {
                if (el.scrollHeight > el.clientHeight) {
                  const top = target.getBoundingClientRect().top + el.scrollTop - 12;
                  el.scrollTop = Math.max(0, top);
                }
              } catch (_) {}
            }
          };

          [0, 80, 200, 500, 900, 1400].forEach((delay) => {
            window.parent.setTimeout(scrollOnce, delay);
          });
        })();
        </script>
        """,
        height=0,
    )


def format_to_agent_ii_style(text: str) -> str:
    """
    Transform rigid markdown structures into the clean, indented agent.ii.inc academic citation style.

    Translates:
    - Chinese structured blocks (### [index]. Title, 文献信息, 链接, 为什么值得读, 关键发现, 证据边界, 临床相关性)
    - English structured blocks (e.g. 1. Author... URL:... **Why it matters:**... **Takeaway:**... joined as single paragraph)
    into formatted paragraphs with soft line breaks and indents.
    """
    import re

    lines = text.splitlines()
    new_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Match a Chinese paper entry header
        match_zh = re.match(r"^###\s+(\d+)\.\s+(.*)", line)

        # Match an English paper entry header
        match_en = re.match(r"^(\d+)\.\s+(.*)", line) if not match_zh else None

        if match_zh:
            index = match_zh.group(1)
            title = match_zh.group(2).strip()

            # Read subsequent lines of this paper entry
            entry_lines = []
            i += 1
            while i < len(lines) and not re.match(r"^###\s+\d+\.", lines[i]) and not lines[i].startswith("## ") and not lines[i].startswith("---"):
                entry_lines.append(lines[i])
                i += 1

            # Parse fields from entry_lines
            meta_info = ""
            link = ""
            why_it_matters = ""
            key_finding = ""
            boundary = ""
            relevance = ""

            # Track if we're in a multi-line 关键发现 block (V2 format)
            in_multiline_finding = False
            multiline_finding_parts = []

            for el in entry_lines:
                el_stripped = el.strip()
                if el_stripped.startswith("**文献信息：**"):
                    meta_info = el_stripped.replace("**文献信息：**", "").strip()
                    in_multiline_finding = False
                elif el_stripped.startswith("**链接：**"):
                    link = el_stripped.replace("**链接：**", "").strip()
                    in_multiline_finding = False
                elif el_stripped.startswith("**为什么值得读：**"):
                    why_it_matters = el_stripped.replace("**为什么值得读：**", "").strip()
                    in_multiline_finding = False
                elif el_stripped.startswith("**关键发现：**"):
                    content = el_stripped.replace("**关键发现：**", "").strip()
                    if content:
                        # Single-line format (old style)
                        key_finding = content
                        in_multiline_finding = False
                    else:
                        # Multi-line format (V2 style) - start collecting
                        in_multiline_finding = True
                        multiline_finding_parts = []
                elif el_stripped.startswith("**临床相关性：**"):
                    # This marks the end of the entry, capture and exit multiline mode
                    relevance = el_stripped.replace("**临床相关性：**", "").strip()
                    in_multiline_finding = False
                elif in_multiline_finding and el_stripped:
                    # Collect V2 multi-line content (核心论点, 研究设计, 关键证据, 证据边界, 意外发现)
                    # Convert V2 labels to compact inline format
                    if el_stripped.startswith("**核心论点：**"):
                        multiline_finding_parts.append(el_stripped.replace("**核心论点：**", "核心论点：").strip())
                    elif el_stripped.startswith("**研究设计：**"):
                        multiline_finding_parts.append(el_stripped.replace("**研究设计：**", "研究设计：").strip())
                    elif el_stripped.startswith("**关键证据：**"):
                        multiline_finding_parts.append(el_stripped.replace("**关键证据：**", "").strip())
                    elif el_stripped.startswith("**证据边界：**"):
                        # Capture boundary but stay in multiline mode (意外发现 may follow)
                        boundary = el_stripped.replace("**证据边界：**", "").strip()
                    elif el_stripped.startswith("**意外发现：**"):
                        multiline_finding_parts.append(el_stripped.replace("**意外发现：**", "意外发现：").strip())
                elif el_stripped.startswith("**证据边界：**"):
                    # Non-V2 format: standalone 证据边界 field
                    boundary = el_stripped.replace("**证据边界：**", "").strip()

            # If we collected V2 multi-line findings, join them
            if multiline_finding_parts:
                key_finding = " ".join(multiline_finding_parts)

            # Reconstruct meta/author details
            # Format varies: "Author 等｜Year｜Journal｜..." or "Year｜EvidenceType｜Theme"
            meta_parts = [p.strip() for p in meta_info.split("｜") if p.strip()]
            author = ""
            year = ""
            journal = ""

            # Check if first part is a year (4-digit number) - then no author
            if meta_parts and meta_parts[0].isdigit() and len(meta_parts[0]) == 4:
                year = meta_parts[0]
                # Skip evidence_type and theme, they're not journal
                # Just use year for citation
            else:
                if len(meta_parts) >= 1:
                    author = meta_parts[0]
                if len(meta_parts) >= 2:
                    year = meta_parts[1]
                if len(meta_parts) >= 3:
                    journal = meta_parts[2]

            author_str = f"{author}. " if author else ""
            journal_str = f" {journal}." if journal else ""
            year_str = f" {year}." if year else ""

            # Citation line
            new_lines.append(f"{index}. {author_str}*{title}.*{journal_str}{year_str}")

            # Indented details with soft breaks
            if link:
                # Convert plain URL to clickable HTML link for unsafe_allow_html=True rendering
                escaped_link = html.escape(link, quote=True)
                new_lines.append(f'   URL: <a href="{escaped_link}" target="_blank" rel="noopener" style="color:#60a5fa">{html.escape(link)}</a>')
            if why_it_matters:
                new_lines.append(f"   **Why it matters:** {why_it_matters}")

            takeaway_parts = []
            if key_finding:
                takeaway_parts.append(key_finding)
            if relevance:
                takeaway_parts.append(relevance)
            if boundary:
                takeaway_parts.append(f"【证据边界：{boundary}】")

            takeaway_text = " ".join(takeaway_parts).strip()
            if takeaway_text:
                new_lines.append(f"   **Takeaway:** {takeaway_text}")

            new_lines.append("")

        elif match_en:
            index = match_en.group(1)
            content = match_en.group(2).strip()

            entry_lines = [content]
            i += 1
            while i < len(lines) and not re.match(r"^\d+\.", lines[i]) and not lines[i].startswith("## ") and not lines[i].startswith("---"):
                entry_lines.append(lines[i])
                i += 1

            full_entry = " ".join(entry_lines)

            # Extract components
            url_val = ""
            why_val = ""
            takeaway_val = ""

            url_match = re.search(r"\bURL:\s*(\S+)", full_entry)
            why_match = re.search(r"\*\*Why it matters:\*\*\s*(.*?)(?=\*\*Takeaway:\*\*|\bURL:|$)", full_entry)
            takeaway_match = re.search(r"\*\*Takeaway:\*\*\s*(.*)", full_entry)

            cut_idx = len(full_entry)
            if url_match:
                cut_idx = min(cut_idx, url_match.start())
                url_val = url_match.group(1).strip()
            if why_match:
                cut_idx = min(cut_idx, why_match.start())
                why_val = why_match.group(1).strip()
            if takeaway_match:
                cut_idx = min(cut_idx, takeaway_match.start())
                takeaway_val = takeaway_match.group(1).strip()

            citation = full_entry[:cut_idx].strip()

            new_lines.append(f"{index}. {citation}")
            if url_val:
                # Convert plain URL to clickable HTML link for unsafe_allow_html=True rendering
                escaped_url = html.escape(url_val, quote=True)
                new_lines.append(f'   URL: <a href="{escaped_url}" target="_blank" rel="noopener" style="color:#60a5fa">{html.escape(url_val)}</a>')
            if why_val:
                new_lines.append(f"   **Why it matters:** {why_val}")
            if takeaway_val:
                new_lines.append(f"   **Takeaway:** {takeaway_val}")

            new_lines.append("")
        else:
            new_lines.append(line)
            i += 1

        # Post-process to ensure trailing double-spaces for soft break inside list item
    final_lines = []
    for idx, l in enumerate(new_lines):
        if l.strip() and (l.startswith("   ") or re.match(r"^\d+\.", l)) and idx + 1 < len(new_lines) and new_lines[idx+1].startswith("   "):
            final_lines.append(l + "  ")
        else:
            final_lines.append(l)

    return "\n".join(final_lines)


def render_answer_block_v2(
    answer: str,
    confidence: str,
    figures_used: list[dict],
    key_prefix: str,
    source_ids: Optional[list[str]] = None,
    loaded_source_ids: Optional[list[str]] = None,
    question: str = "",
    disease: str = "",
    question_type: str = "",
    research_trace: Optional[list[dict]] = None,
    harness_result: Optional[dict] = None,
    loaded_paths: Optional[list[str]] = None,
    backend: str = "openrouter",
    refined_query: Optional[str] = None,
    objectives: Optional[list[str]] = None,
) -> None:
    """
    Render answer using ResultPresentation contract (V2).

    This is the new renderer that uses evidence profiles instead of confidence badges.
    """
    if not RESULT_PRESENTATION_AVAILABLE:
        # Fall back to v1 if module not available
        render_answer_block(
            answer=answer,
            confidence=confidence,
            figures_used=figures_used,
            key_prefix=key_prefix,
            source_ids=source_ids,
            loaded_source_ids=loaded_source_ids,
            question=question,
            disease=disease,
            question_type=question_type,
            research_trace=research_trace,
            harness_result=harness_result,
            loaded_paths=loaded_paths,
            backend=backend,
            refined_query=refined_query,
            objectives=objectives,
        )
        return

    source_ids = source_ids or []
    loaded_source_ids = loaded_source_ids or []

    contract, display_answer = split_research_contract(answer) if question_type == "research_search" else (None, answer)

    if question_type == "research_search":
        st.markdown('<div id="research-result-top"></div>', unsafe_allow_html=True)

    # Build presentation
    presentation = build_presentation_from_answer(
        answer=display_answer,
        question=question,
        source_ids=source_ids,
        loaded_source_ids=loaded_source_ids,
        confidence=confidence,
        disease=disease,
        research_trace=research_trace,
    )

    # Render query refinement/evaluation first
    if backend == "local":
        try:
            from core.task_evaluator import TaskEvaluator
            evaluator = TaskEvaluator()
            evaluation = evaluator.evaluate(question)
            task_type_value = "research_search" if question_type == "research_search" else evaluation.task_type.value
            render_local_query_evaluation(
                disease=evaluation.disease,
                task_type=task_type_value,
                subqueries=evaluation.subqueries,
            )
        except Exception:
            pass
    else:
        render_query_refinement(refined_query, objectives)

    if contract:
        render_research_contract_panel(answer, question_type)

    # Render translated provenance with paper titles, never internal source IDs.
    cleaned_answer = strip_legacy_footer(display_answer)
    if question_type == "research_search":
        cleaned_answer = format_to_agent_ii_style(cleaned_answer)

    visible_answer = render_user_facing_provenance(
        cleaned_answer,
        presentation.source_cards,
        html_output=True,
    )
    export_answer = render_user_facing_provenance(
        cleaned_answer,
        presentation.source_cards,
        html_output=False,
    )
    st.markdown(visible_answer, unsafe_allow_html=True)
    copy_button(export_answer, key=f"{key_prefix}-copy")

    # Evidence profile (replaces trust block)
    render_evidence_profile_v2(presentation.evidence_profile)

    # Query Scope panel
    render_query_scope_panel(harness_result, key_prefix)

    # Verification badge (from harness loop)
    render_verification_badge(harness_result)

    # Depth contract warning for Deep/Audit modes
    render_depth_contract_warning(harness_result)

    # Render matched documents section
    if loaded_paths and question_type != "research_search":
        if backend == "local":
            render_loaded_documents_section(loaded_paths, initially_expanded=True, key_prefix=key_prefix)
        else:
            with st.expander(f"🔍 查看本次加载的 {len(loaded_paths)} 篇本地原始文献与文档内容", expanded=False):
                render_loaded_documents_section(loaded_paths, initially_expanded=False, key_prefix=key_prefix)

    # Research trace (unchanged)
    render_research_trace(research_trace)

    # Expert review loop with harness results
    render_expert_review_loop(
        question=question,
        answer=display_answer,
        disease=disease,
        question_type=question_type,
        confidence=confidence,
        source_ids=source_ids or loaded_source_ids,
        key_prefix=key_prefix,
        harness_result=harness_result,
    )

    # Figures (unchanged)
    described_figs = [f for f in figures_used if f.get("described_in_answer")]
    if described_figs:
        st.divider()
        source_titles = get_source_titles()
        st.markdown(
            "<div class='vault-panel-label' style='margin-bottom:12px'>Figures referenced in this answer</div>",
            unsafe_allow_html=True,
        )
        cols = st.columns(min(len(described_figs), 3))
        for i, fig in enumerate(described_figs):
            fig_path = VAULT_ROOT / fig["file"]
            if fig_path.exists():
                with cols[i % 3]:
                    fig_title = source_titles.get(fig["source_id"], "来源图表")
                    st.image(str(fig_path), caption=fig_title)

    # Sources with canonical links (v2)
    render_evidence_traces_v2(presentation.evidence_traces, key_prefix=key_prefix)
    render_sources_section_v2(presentation.source_cards, key_prefix=key_prefix)

    # Next actions
    render_next_actions_v2(presentation.next_actions, key_prefix=key_prefix)

    # Save Research Record panel
    render_save_research_record_panel(harness_result, key_prefix)

    # Render related topic pages preview for user accessibility
    topic_paths = extract_topic_paths_from_text(answer)
    if topic_paths:
        with st.expander("📖 本地关联主题页面阅读", expanded=False):
            selected_topic = st.selectbox("选择要阅读的文档", topic_paths, key=f"{key_prefix}-topic-selector", format_func=format_topic_path)
            if selected_topic:
                content = get_search_result_preview(selected_topic, max_chars=5000)
                if content:
                    render_translatable_content(selected_topic, content, is_session_chinese(), key_prefix=key_prefix)
                else:
                    st.warning(f"未能加载文档：{selected_topic}")


def render_query_scope_panel(harness_result: Optional[dict], key_prefix: str) -> None:
    is_zh = is_session_chinese()
    record = harness_result.get("record") if harness_result else None
    
    panel_title = "搜索范围" if is_zh else "Search Coverage"
    
    if not record or not getattr(record, "retrieval_events", None):
        with st.expander(panel_title, expanded=False):
            st.warning("未执行搜索" if is_zh else "No search executed")
        return

    events = record.retrieval_events
    snapshots = getattr(record, "source_snapshots", [])
    
    unique_engines = set(e.engine for e in events)
    total_candidates = sum(e.candidate_count for e in events)
    
    all_retained = set()
    for e in events:
        all_retained.update(e.retained_ids)
    total_retained = len(all_retained)
    
    if is_zh:
        summary_text = f"搜索了 {len(unique_engines)} 个引擎，{total_candidates} 候选 → {total_retained} 保留"
    else:
        summary_text = f"Searched {len(unique_engines)} engines, {total_candidates} candidates → {total_retained} retained"
        
    with st.expander(f"▶ {panel_title} ({summary_text})", expanded=False):
        st.markdown("##### 检索事件" if is_zh else "##### Retrieval Events")
        
        for idx, event in enumerate(events):
            engine_display = {
                "vault": "本地知识库" if is_zh else "Local Vault",
                "pubmed": "PubMed",
                "crossref": "CrossRef",
            }.get(event.engine, event.engine)
            
            st.markdown(f"**{engine_display}** ({event.scope})")
            st.markdown(f"- **检索词:** `{event.query}`")
            st.markdown(f"- **候选:** {event.candidate_count} | **保留:** {len(event.retained_ids)}")
            if event.filters_applied:
                st.markdown(f"- **过滤器:** `{', '.join(event.filters_applied)}`")
            if event.excluded_ids:
                with st.expander(f"已排除结果 ({len(event.excluded_ids)})", expanded=False):
                    for exc_id in event.excluded_ids:
                        reason = event.exclusion_reasons.get(exc_id, "Unknown reason")
                        st.markdown(f"- `{exc_id}`: {reason}")
            st.markdown("---")
            
        if snapshots:
            st.markdown("##### 来源快照" if is_zh else "##### Source Snapshots")
            for snapshot in snapshots:
                st.markdown(f"**`{snapshot.source_id}` — {snapshot.title}**")
                meta_details = []
                if snapshot.publication_year:
                    meta_details.append(f"Year: {snapshot.publication_year}")
                if snapshot.source_family != "unknown":
                    meta_details.append(f"Family: {snapshot.source_family}")
                if snapshot.study_type != "unknown":
                    meta_details.append(f"Study: {snapshot.study_type}")
                if snapshot.species != "unknown":
                    meta_details.append(f"Species: {snapshot.species}")
                if snapshot.verification_status != "unknown":
                    meta_details.append(f"Status: {snapshot.verification_status}")
                    
                if meta_details:
                    st.markdown(f"*{', '.join(meta_details)}*")
                st.markdown(f"Fingerprint: `{snapshot.content_fingerprint[:16]}...`")
                st.markdown("---")


def render_save_research_record_panel(harness_result: Optional[dict], key_prefix: str) -> None:
    is_zh = is_session_chinese()
    record = harness_result.get("record") if harness_result else None
    
    if not record:
        return

    saved_key = f"saved_path_{record.record_id}"
    error_key = f"save_error_{record.record_id}"
    title_key = f"save_title_{record.record_id}"
    
    saved_path = st.session_state.get(saved_key)
    save_error = st.session_state.get(error_key)
    
    already_saved = saved_path is not None or getattr(record, "last_saved", None) is not None
    
    st.markdown("---")
    
    st.markdown('<div style="padding:15px; background:rgba(30, 30, 35, 0.4); border:1px solid rgba(255, 255, 255, 0.08); border-radius:8px; margin-top:10px;">', unsafe_allow_html=True)
    
    title_label = "记录标题" if is_zh else "Record Title"
    placeholder = "输入标题或使用默认" if is_zh else "Enter title or use default"
    
    default_title = record.title or record.user_request[:50]
    
    title_input = st.text_input(
        title_label,
        value=st.session_state.get(title_key, default_title),
        placeholder=placeholder,
        key=f"{key_prefix}-title-input"
    )
    st.session_state[title_key] = title_input
    record.title = title_input
    
    duplicate = None
    try:
        harness = get_harness_loop(VAULT_ROOT)
        duplicate = harness.record_store.find_equivalent_record(record)
    except Exception:
        pass
        
    if duplicate:
        dup_date = duplicate.timestamp.strftime("%Y-%m-%d")
        if is_zh:
            dup_msg = f"⚠️ 已存在类似记录: `{duplicate.record_id}` ({dup_date})"
        else:
            dup_msg = f"⚠️ Similar record exists: `{duplicate.record_id}` ({dup_date})"
        st.warning(dup_msg)
        
    if already_saved:
        btn_lbl = "已保存 ✓"
        st.button(btn_lbl, key=f"{key_prefix}-save-btn-disabled", disabled=True, use_container_width=True)
        path_to_show = saved_path or f"system/research-records/{record.record_id}.json"
        if is_zh:
            st.success(f"已保存: `{path_to_show}`")
        else:
            st.success(f"Saved: `{path_to_show}`")
    else:
        if duplicate:
            btn_lbl = "保存为新版本" if is_zh else "Save as New Version"
        else:
            btn_lbl = "保存研究记录" if is_zh else "Save Research Record"
            
        if st.button(btn_lbl, key=f"{key_prefix}-save-btn", use_container_width=True):
            try:
                harness = get_harness_loop(VAULT_ROOT)
                if duplicate:
                    record.record_version = duplicate.record_version + 1
                    record.parent_record_id = duplicate.record_id
                
                out_path = harness.save_record(record)
                rel_saved_path = str(out_path.relative_to(VAULT_ROOT))
                st.session_state[saved_key] = rel_saved_path
                st.session_state[error_key] = None
                
                if "last_meta" in st.session_state and st.session_state.last_meta:
                    st.session_state.last_meta["research_record_saved"] = True
                    st.session_state.last_meta["research_record_path"] = rel_saved_path
                st.session_state.last_record_saved_path = rel_saved_path
                
                st.toast(f"Saved: {rel_saved_path}", icon="✅")
                st.rerun()
            except Exception as e:
                err_msg = str(e)
                st.session_state[error_key] = err_msg
                st.error(f"保存失败：{err_msg}" if is_zh else f"Save failed: {err_msg}")
                
        if save_error:
            st.error(f"保存失败：{save_error}" if is_zh else f"Save failed: {save_error}")
            
    st.markdown('</div>', unsafe_allow_html=True)


def provenance_counts(answer: str) -> dict[str, int]:
    """Count answer provenance tags for the visible trust block."""
    return {
        "quoted": len(re.findall(r"\[quoted_fact:\s*[^\]]+\]", answer)),
        "supported": len(re.findall(r"\[source_supported_conclusion:\s*[^\]]+\]", answer)),
        "inference": len(re.findall(r"\[llm_inference\]", answer)),
    }


def render_trust_block(answer: str, confidence: str, source_ids: list[str], loaded_source_ids: list[str]) -> None:
    """Show why the answer received its confidence level and which readings were loaded."""
    counts = provenance_counts(answer)
    cited_count = counts["quoted"] + counts["supported"]
    loaded_count = len(loaded_source_ids)
    if confidence == "high":
        tone = "green"
        reason = f"{cited_count} sourced claim tags and no explicit inference tags."
    elif confidence == "medium":
        tone = "amber"
        reason = (
            f"{cited_count} sourced claim tags and {counts['inference']} inference tags. "
            "Some interpretation goes beyond direct source wording."
        )
    else:
        tone = "amber"
        reason = (
            f"{cited_count} sourced claim tags and {counts['inference']} inference tags. "
            "Treat this as a starter answer until the unsupported parts are tightened."
        )

    readings = loaded_count or len(source_ids)
    title_source_ids = loaded_source_ids or source_ids
    titles, hidden_count = readable_source_titles(title_source_ids, limit=3)
    title_line = ""
    if titles:
        safe_titles = "; ".join(html.escape(title) for title in titles)
        extra = f" + {hidden_count} more." if hidden_count else "."
        title_line = f"<div style='margin-top:6px'>Readable sources: {safe_titles}{extra}</div>"
    render_notice(
        f"Confidence: {confidence}. {reason} Readings loaded: {readings}.{title_line}",
        tone=tone,
    )


def render_research_trace_summary(
    research_trace: Optional[list[dict]],
    loaded_source_ids: Optional[list[str]] = None,
    backend: str = "local",
) -> None:
    """
    Render a compact one-line summary of the research path at the top of the answer.

    This makes retrieval decisions visible without requiring users to expand anything.
    """
    if not research_trace:
        return

    is_zh = is_session_chinese()

    # Extract key info from trace
    surface = ""
    search_depth = ""
    source_count = len(loaded_source_ids) if loaded_source_ids else 0

    for entry in research_trace:
        step = entry.get("step", "")
        detail = entry.get("detail", "")

        # Look for surface/route info
        if "local surface" in step.lower() or "routed" in step.lower():
            surface = detail
        elif "interpreted" in step.lower():
            # Extract depth from detail like "disease=ckd, depth=standard"
            if "depth=" in detail:
                try:
                    search_depth = detail.split("depth=")[1].split(",")[0].strip()
                except IndexError:
                    pass

    # Build summary parts
    parts = []

    if surface:
        surface_short = surface.replace("_overview", "").replace("_", " ").strip()
        parts.append(surface_short if surface_short else surface)

    if source_count > 0:
        sources_lbl = f"{source_count} 篇来源" if is_zh else f"{source_count} sources"
        parts.append(sources_lbl)

    if search_depth:
        depth_lbl = f"深度: {search_depth}" if is_zh else f"depth: {search_depth}"
        parts.append(depth_lbl)

    # Backend label
    backend_labels = {
        "local": "本地检索" if is_zh else "local",
        "openrouter": "OpenRouter",
        "anthropic": "Anthropic",
        "ollama": "Ollama",
    }
    parts.append(backend_labels.get(backend, backend))

    if not parts:
        return

    summary = " → ".join(parts)
    path_lbl = "检索路径" if is_zh else "Path"

    st.markdown(
        f"""
        <div class="vault-research-trace-summary" style="
            font-size: 12px;
            color: #8b90a0;
            padding: 6px 10px;
            background: rgba(45, 49, 71, 0.4);
            border-radius: 4px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 6px;
        ">
            <span style="opacity: 0.7;">🔍</span>
            <span><strong>{path_lbl}:</strong> {html.escape(summary)}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def is_broad_question(question: str) -> bool:
    """
    Detect if a question is broad/general and would benefit from mode selection.

    Broad questions include:
    - Single disease name: "CKD", "糖尿病"
    - Explain/intro patterns: "解释CKD", "什么是CKD", "explain CKD"
    - Short general questions without specific treatment/test terms
    """
    if not question:
        return False

    q = question.strip().lower()

    # Very short questions (1-3 words) are often broad
    words = q.split()
    if len(words) <= 3:
        # Check for broad patterns
        broad_patterns = [
            "ckd", "akd", "慢性肾病", "急性肾损伤", "肾病", "糖尿病",
            "hyperthyroidism", "甲亢", "obesity", "肥胖", "anemia", "贫血",
            "hypertension", "高血压", "ibd", "炎症性肠病",
        ]
        if any(pattern in q for pattern in broad_patterns):
            return True

    # Explain/intro patterns
    explain_patterns = [
        "什么是", "解释", "介绍", "概述", "说说", "讲讲",
        "explain", "what is", "tell me about", "overview of",
        "describe", "introduction to",
    ]
    if any(q.startswith(pattern) for pattern in explain_patterns):
        return True

    # Has specific treatment/test terms = not broad
    specific_terms = [
        "treatment", "治疗", "药", "drug", "dose", "剂量",
        "test", "检测", "检查", "诊断", "diagnosis",
        "prognosis", "预后", "stage", "分期",
        "diet", "饮食", "nutrition", "营养",
        "supplement", "补充", "phosphorus", "磷",
        "protocol", "方案", "guideline", "指南",
    ]
    if any(term in q for term in specific_terms):
        return False

    return False


def render_answer_mode_chip(
    question: str,
    current_mode: str = "general",
    key_prefix: str = "",
) -> Optional[str]:
    """
    Render a mode selector chip for broad questions.

    Returns the selected mode if changed, None otherwise.
    """
    if not is_broad_question(question):
        return None

    is_zh = is_session_chinese()

    modes = {
        "general": ("普通解读", "General") if is_zh else ("General", "General explanation"),
        "researcher": ("研究者视角", "Researcher") if is_zh else ("Researcher", "Academic perspective"),
        "treatment": ("治疗证据", "Treatment") if is_zh else ("Treatment", "Treatment evidence"),
        "mechanism": ("机制详解", "Mechanism") if is_zh else ("Mechanism", "Pathophysiology details"),
    }

    mode_key = f"{key_prefix}_answer_mode"
    if mode_key not in st.session_state:
        st.session_state[mode_key] = current_mode

    hint = "选择解读视角" if is_zh else "Select perspective"

    st.markdown(
        f"""
        <div style="
            font-size: 11px;
            color: #8b90a0;
            margin-bottom: 8px;
        ">
            💡 {hint}
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(len(modes))
    selected_mode = st.session_state[mode_key]

    for idx, (mode_id, (label_zh, label_en)) in enumerate(modes.items()):
        label = label_zh if is_zh else label_en
        with cols[idx]:
            is_active = mode_id == selected_mode
            if is_active:
                st.markdown(
                    f"""
                    <div style="
                        padding: 4px 10px;
                        background: rgba(99, 102, 241, 0.2);
                        border: 1px solid #6366f1;
                        border-radius: 12px;
                        font-size: 12px;
                        color: #a5b4fc;
                        text-align: center;
                        cursor: default;
                    ">
                        {html.escape(label)}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                if st.button(label, key=f"{key_prefix}_mode_{mode_id}", use_container_width=True):
                    st.session_state[mode_key] = mode_id
                    return mode_id

    return None


# ---------------------------------------------------------------------------
# Decision Tree UI (P4)
# ---------------------------------------------------------------------------

def render_decision_tree_card(
    disease: str,
    intent: str,
    key_prefix: str = "",
) -> None:
    """
    Render a decision tree card for treatment/diagnostic pathways.

    Displays treatment branch maps or diagnostic routes based on user intent.
    """
    from query import get_decision_tree_content

    is_zh = is_session_chinese()
    content_map = get_decision_tree_content(disease, intent, chinese=is_zh)

    if not content_map:
        return

    # Determine which content to display based on intent
    display_path = None
    title = ""
    icon = ""

    if intent == "treatment" and "treatment_branch" in content_map:
        display_path = content_map["treatment_branch"]
        title = "治疗决策路径" if is_zh else "Treatment Decision Path"
        icon = "🌳"
    elif intent == "diagnostic":
        if "diagnostic_workup" in content_map:
            display_path = content_map["diagnostic_workup"]
        elif "diagnostic_route" in content_map:
            display_path = content_map["diagnostic_route"]
        title = "诊断决策路径" if is_zh else "Diagnostic Pathway"
        icon = "🔬"

    if not display_path:
        return

    # Read the branch map content
    full_path = Path(__file__).parent.parent / display_path
    if not full_path.exists():
        return

    try:
        content = full_path.read_text(encoding="utf-8")
    except IOError:
        return

    # Extract Route By Question or key decision branches
    branches = _extract_decision_branches(content, is_zh)

    if not branches:
        return

    # Render the card with DESIGN.md specs
    st.markdown(
        f"""
        <div style="
            border: 1px solid #2d3147;
            border-radius: 6px;
            padding: 16px;
            margin-bottom: 16px;
            background: rgba(45, 49, 71, 0.3);
        ">
            <div style="
                font-family: 'Geist', sans-serif;
                font-weight: 500;
                font-size: 15px;
                color: #e8eaf0;
                margin-bottom: 12px;
            ">
                {icon} {html.escape(title)}
            </div>
            <div style="
                font-family: 'Geist Mono', monospace;
                font-size: 12px;
                color: #4a4f64;
            ">
                {"".join(_render_branch_line(b, is_zh) for b in branches)}
            </div>
            <div style="
                font-family: 'Geist', sans-serif;
                font-size: 11px;
                color: #8b90a0;
                margin-top: 12px;
            ">
                {"每个分支有独立的证据层级和适用条件。" if is_zh else "Each branch has its own evidence level and applicability conditions."}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _extract_decision_branches(content: str, is_zh: bool) -> list[dict]:
    """Extract decision branches from a navigation or branch-map file."""
    branches = []

    # Look for "Route By Question" section or similar
    route_patterns = [
        r"#+\s*Route By Question",
        r"#+\s*按问题路由",
        r"#+\s*Quick Helpers",
        r"#+\s*快速导航",
    ]

    for pattern in route_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            # Extract content after this heading until next heading
            start_pos = match.end()
            next_heading = re.search(r"\n#+\s+", content[start_pos:])
            end_pos = start_pos + next_heading.start() if next_heading else len(content)
            section = content[start_pos:end_pos]

            # Extract list items with links
            for line in section.split("\n"):
                line = line.strip()
                if line.startswith("-") or line.startswith("*"):
                    # Parse link: [text](path)
                    link_match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", line)
                    if link_match:
                        label = link_match.group(1)
                        path = link_match.group(2)
                        # Also capture any text before the link
                        prefix = line.split("[")[0].strip("- *").strip()
                        branches.append({
                            "prefix": prefix,
                            "label": label,
                            "path": path,
                        })

            if branches:
                break

    return branches[:8]  # Cap at 8 branches


def _render_branch_line(branch: dict, is_zh: bool) -> str:
    """Render a single branch line with tree connector."""
    prefix = html.escape(branch.get("prefix", ""))
    label = html.escape(branch["label"])

    return f"""
        <div style="
            display: flex;
            align-items: center;
            margin-bottom: 8px;
            font-family: 'Geist', sans-serif;
            font-size: 13px;
        ">
            <span style="color: #4a4f64; margin-right: 8px;">├─</span>
            <span style="color: #8b90a0; margin-right: 8px;">{prefix}</span>
            <span style="color: #e8eaf0;">{label}</span>
        </div>
    """


def render_route_by_question(
    disease: str,
    key_prefix: str = "",
) -> None:
    """
    Render a "Route By Question" widget for topic navigation.

    Shows clickable routes from navigation.md for users who aren't sure where to start.
    """
    from query import get_decision_tree_content

    is_zh = is_session_chinese()
    content_map = get_decision_tree_content(disease, "overview", chinese=is_zh)

    if "navigation" not in content_map:
        return

    nav_path = Path(__file__).parent.parent / content_map["navigation"]
    if not nav_path.exists():
        return

    try:
        content = nav_path.read_text(encoding="utf-8")
    except IOError:
        return

    branches = _extract_decision_branches(content, is_zh)
    if not branches:
        return

    # Render as expander per DESIGN.md
    expander_title = "🔀 不确定从哪里开始？" if is_zh else "🔀 Not sure where to start?"

    with st.expander(expander_title, expanded=False):
        for branch in branches:
            prefix = branch.get("prefix", "")
            label = branch["label"]
            display_text = f"{prefix} {label}" if prefix else label

            if st.button(
                display_text,
                key=f"{key_prefix}_route_{branch['path'][:20]}",
                use_container_width=True,
            ):
                # Set session state to trigger a new query for this route
                st.session_state[f"{key_prefix}_routed_topic"] = branch["path"]
                st.rerun()


def render_thought_panel(
    thought_title: str,
    thought_content: str,
    searches: Optional[list[dict]] = None,
    key_prefix: str = "",
) -> None:
    """
    Render a "Thought" panel showing the reasoning process (agent.ii.inc style).

    Args:
        thought_title: Short title like "Researching feline HCM papers"
        thought_content: Detailed reasoning text
        searches: Optional list of search queries with their status
        key_prefix: Unique key prefix for Streamlit state
    """
    is_zh = is_session_chinese()
    panel_label = "● Thought" if not is_zh else "● 思考过程"

    with st.expander(panel_label, expanded=True):
        # Title
        st.markdown(
            f"""<div style="
                font-family: 'Geist', sans-serif;
                font-weight: 600;
                font-size: 14px;
                color: #e8eaf0;
                margin-bottom: 8px;
            ">{html.escape(thought_title)}</div>""",
            unsafe_allow_html=True,
        )

        # Content
        st.markdown(
            f"""<div style="
                font-family: 'Geist', sans-serif;
                font-size: 13px;
                color: #d1d5db;
                line-height: 1.6;
                margin-bottom: 12px;
            ">{html.escape(thought_content)}</div>""",
            unsafe_allow_html=True,
        )

        # Search queries (if any)
        if searches:
            for i, search in enumerate(searches):
                query = search.get("query", "")
                status = search.get("status", "searching")
                result_count = search.get("results", 0)

                icon = "🔍" if status == "searching" else ("✓" if status == "done" else "○")
                status_color = "#60a5fa" if status == "searching" else ("#22c55e" if status == "done" else "#8b90a0")

                st.markdown(
                    f"""<div style="
                        display: flex;
                        align-items: center;
                        padding: 8px 12px;
                        background: rgba(45, 49, 71, 0.5);
                        border-radius: 4px;
                        margin-bottom: 4px;
                        font-family: 'Geist', sans-serif;
                        font-size: 12px;
                    ">
                        <span style="margin-right: 8px; color: {status_color}">{icon} Searching</span>
                        <span style="color: #e8eaf0; flex: 1;">{html.escape(query[:50])}...</span>
                        <span style="color: #8b90a0; font-size: 11px;">More</span>
                    </div>""",
                    unsafe_allow_html=True,
                )


def render_research_trace(research_trace: Optional[list[dict]]) -> None:
    """Render the retrieval and synthesis path behind an answer."""
    if not research_trace:
        return

    is_zh = is_session_chinese()
    title = "检索与分析轨迹" if is_zh else "Research trace"
    note = (
        "这是系统解释问题、检索本地证据、加载文献卡片并得出回答的过程。这是系统运行的审计轨迹，不是额外的临床证据。"
        if is_zh else
        "This shows how the vault interpreted the question, searched local evidence, loaded source cards, and reached the answer. It is an audit trail, not extra evidence."
    )

    step_translations = {
        "Interpreted query": "解析问题",
        "Searched vault": "检索本地库",
        "Loaded evidence": "加载证据文献",
        "Loaded routed files": "加载路由文件",
        "Applied selected source": "应用所选来源",
        "Loaded overview baseline evidence": "加载概述基线证据",
        "Fallback source preload": "预加载后备来源",
        "Checked verified figures": "验证图表检查",
        "Synthesized answer": "合成最终回答",
        "Returned local answer": "返回本地回答",
    }

    with st.expander(title, expanded=False):
        st.markdown(
            f"""
            <div class="vault-inline-note">
              {note}
            </div>
            """,
            unsafe_allow_html=True,
        )
        for i, entry in enumerate(research_trace, 1):
            raw_step = entry.get("step", f"Step {i}")
            # Try to match dynamic hop names
            if raw_step.startswith("Agent hop"):
                step_num = raw_step.replace("Agent hop", "").strip()
                step = f"智能导航第{step_num}步" if is_zh else raw_step
            else:
                step = step_translations.get(raw_step, raw_step)

            step = html.escape(str(step))
            raw_detail = str(entry.get("detail", ""))
            clean_detail = sanitize_user_facing_markdown(raw_detail).replace("**", "")
            detail = html.escape(clean_detail)

            # Check if this is an external search step
            is_external_step = "External" in raw_step or "PubMed" in raw_step or "Crossref" in raw_step
            step_style = "border-left:3px solid #60a5fa;padding-left:8px" if is_external_step else ""

            st.markdown(
                f"<div class='vault-trace-step' style='{step_style}'><code>{i}</code><strong>{step}</strong><span>{detail}</span></div>",
                unsafe_allow_html=True,
            )
            items = entry.get("items") or []
            if items:
                rows: list[str] = []
                for item in items[:8]:
                    # Handle external items with special styling
                    is_external = item.get("external", False) or item.get("source") in ("pubmed", "crossref")

                    if is_external:
                        # External result: show title and source badge
                        title = item.get("title", "Unknown title")
                        source = item.get("source", "external").upper()
                        doi = item.get("doi", "")
                        pmid = item.get("pmid", "")
                        ref = f"DOI:{doi}" if doi else (f"PMID:{pmid}" if pmid else "")
                        rows.append(
                            f"<div class='vault-trace-item' style='border-left:2px solid #60a5fa;padding-left:8px;margin-left:8px'>"
                            f"<span style='color:#60a5fa;font-size:10px;font-weight:600;margin-right:6px'>{source}</span>"
                            f"<span>{html.escape(str(title))}</span>"
                            f"<em style='color:#94a3b8'>{html.escape(ref)} · needs intake</em></div>"
                        )
                    else:
                        # Regular vault item
                        label = item.get("source_id") or item.get("id") or item.get("file") or "item"
                        meta_parts = []
                        if "matches" in item:
                            meta_parts.append(f"{item['matches']} matches")
                        if "loaded" in item:
                            meta_parts.append("loaded" if item["loaded"] else "not loaded")
                        if item.get("file") and label != item.get("file"):
                            meta_parts.append(str(item["file"]))
                        meta = " · ".join(meta_parts)
                        rows.append(
                            f"<div class='vault-trace-item'><span>{html.escape(str(label))}</span><em>{html.escape(meta)}</em></div>"
                        )
                st.markdown("".join(rows), unsafe_allow_html=True)


def render_answer_block(
    answer: str,
    confidence: str,
    figures_used: list[dict],
    key_prefix: str,
    source_ids: Optional[list[str]] = None,
    loaded_source_ids: Optional[list[str]] = None,
    question: str = "",
    disease: str = "",
    question_type: str = "",
    research_trace: Optional[list[dict]] = None,
    harness_result: Optional[dict] = None,
    loaded_paths: Optional[list[str]] = None,
    backend: str = "openrouter",
    refined_query: Optional[str] = None,
    objectives: Optional[list[str]] = None,
) -> None:
    """Render one assistant answer with provenance, copy button, confidence, figures, and sources."""
    source_ids = source_ids or []
    loaded_source_ids = loaded_source_ids or []

    # Render compact research trace summary at the top (front-center)
    render_research_trace_summary(
        research_trace=research_trace,
        loaded_source_ids=loaded_source_ids,
        backend=backend,
    )

    # Render answer mode chip for broad questions
    mode_changed = render_answer_mode_chip(
        question=question,
        current_mode="general",
        key_prefix=key_prefix,
    )
    if mode_changed:
        # Mode changed - could trigger re-query with different perspective
        # For now, just show the selection - full re-query integration is future work
        pass

    # Render query refinement/evaluation first
    if backend == "local":
        try:
            from core.task_evaluator import TaskEvaluator
            evaluator = TaskEvaluator()
            evaluation = evaluator.evaluate(question)
            task_type_value = "research_search" if question_type == "research_search" else evaluation.task_type.value
            render_local_query_evaluation(
                disease=evaluation.disease,
                task_type=task_type_value,
                subqueries=evaluation.subqueries,
            )
        except Exception:
            pass
    else:
        render_query_refinement(refined_query, objectives)

    display_answer = render_research_contract_panel(answer, question_type)

    cleaned_answer = strip_legacy_footer(display_answer)
    st.markdown(render_provenance(cleaned_answer), unsafe_allow_html=True)
    copy_button(display_answer, key=f"{key_prefix}-copy")
    render_trust_block(display_answer, confidence, source_ids, loaded_source_ids)

    # Query Scope panel
    render_query_scope_panel(harness_result, key_prefix)

    # Render matched documents section
    if loaded_paths and question_type != "research_search":
        if backend == "local":
            render_loaded_documents_section(loaded_paths, initially_expanded=True, key_prefix=key_prefix)
        else:
            with st.expander(f"🔍 查看本次加载的 {len(loaded_paths)} 篇本地原始文献与文档内容", expanded=False):
                render_loaded_documents_section(loaded_paths, initially_expanded=False, key_prefix=key_prefix)

    render_research_trace(research_trace)
    render_expert_review_loop(
        question=question,
        answer=display_answer,
        disease=disease,
        question_type=question_type,
        confidence=confidence,
        source_ids=source_ids or loaded_source_ids,
        key_prefix=key_prefix,
        harness_result=harness_result,
    )

    described_figs = [f for f in figures_used if f.get("described_in_answer")]
    if described_figs:
        st.divider()
        source_titles = get_source_titles()
        st.markdown(
            "<div class='vault-panel-label' style='margin-bottom:12px'>Figures referenced in this answer</div>",
            unsafe_allow_html=True,
        )
        cols = st.columns(min(len(described_figs), 3))
        for i, fig in enumerate(described_figs):
            fig_path = VAULT_ROOT / fig["file"]
            if fig_path.exists():
                with cols[i % 3]:
                    fig_title = source_titles.get(fig["source_id"], fig["source_id"])
                    st.image(str(fig_path), caption=fig_title)

    sources_to_show = source_ids or loaded_source_ids
    if sources_to_show:
        render_sources_section(sources_to_show)

    # Save Research Record panel
    render_save_research_record_panel(harness_result, key_prefix)

    # Render related topic pages preview for user accessibility
    topic_paths = extract_topic_paths_from_text(answer)
    if topic_paths:
        with st.expander("📖 本地关联主题页面阅读", expanded=False):
            selected_topic = st.selectbox("选择要阅读的文档", topic_paths, key=f"{key_prefix}-topic-selector", format_func=format_topic_path)
            if selected_topic:
                content = get_search_result_preview(selected_topic, max_chars=5000)
                if content:
                    render_translatable_content(selected_topic, content, is_session_chinese(), key_prefix=key_prefix)
                else:
                    st.warning(f"未能加载文档：{selected_topic}")


def render_briefing_entry_cards() -> None:
    """Render Disease Briefing entry cards for available diseases."""
    is_zh = is_session_chinese()
    available_diseases = get_available_diseases()

    if not available_diseases:
        return

    label = "📂 疾病专题与研究简报" if is_zh else "📂 Disease Dossiers & Briefings"
    hint = "查看已整理的疾病机制、分期体系、模型依据、关键终点与参考文献。" if is_zh else "Explore compiled mechanisms, staging, and study endpoints"

    st.markdown(
        f"""<div style="font-size:11px;color:#8b90a0;margin-bottom:4px;margin-top:20px;font-weight:600">
        {html.escape(label)}</div>
        <div style="font-size:10px;color:#6b7280;margin-bottom:8px">
        {html.escape(hint)}</div>""",
        unsafe_allow_html=True,
    )

    # Display available diseases as buttons
    cols = st.columns(min(len(available_diseases), 4))
    disease_labels = {
        "hcm": "HCM 心肌病",
        "ckd": "CKD 肾病",
        "fip": "FIP 传腹",
        "ibd": "IBD 肠病",
        "diabetes": "Diabetes 糖尿病",
        "fcv": "FCV 杯状病毒",
    }

    for i, disease in enumerate(sorted(available_diseases)):
        with cols[i % len(cols)]:
            label = disease_labels.get(disease, disease.upper())
            if st.button(label, key=f"briefing-entry-{disease}", use_container_width=True):
                st.session_state.show_briefing = disease
                st.rerun()


def render_empty_state() -> None:
    """Render minimal first-run state: title + input hint + example tasks only.

    Design principle: Homepage should be a "research question input box",
    not a "system introduction page". All secondary content (disease topics,
    saved answers, provenance guide, how it works) moved to sidebar or removed.
    """
    # 1. Title and subtitle only (no stats, no kicker)
    st.markdown(EMPTY_STATE_INTRO_HTML, unsafe_allow_html=True)

    # 2. Mode buttons and example tasks
    render_example_question_chips("empty")

    # NOTE: The following have been intentionally removed from homepage:
    # - Primary Action Card ("核心工作流") — redundant with title
    # - Disease Briefing Cards — moved to sidebar
    # - Saved Answers Panel — moved to sidebar
    # - Provenance Guide — moved to result page
    # - How It Works — removed (too much explanation)


def render_main_header() -> None:
    """Render the standard main-area header once conversation has started."""
    source_index = get_source_index()
    topic_count = len(list((VAULT_ROOT / "topics").rglob("*.md")))
    disease_count = len([p for p in (VAULT_ROOT / "topics").iterdir() if p.is_dir()])
    st.markdown(
        f"""
        <div class="vault-main-header">
          <div class="vault-kicker">RESEARCH CHAT</div>
          <h1>Ask the vault</h1>
          <div class="vault-statline">{len(source_index)} sources · {topic_count} topic pages · {disease_count} diseases</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    preferred = st.session_state.preferred_source_ids
    if preferred:
        joined = ", ".join(preferred)
        st.markdown(
            f"""
            <div class="vault-inline-note">
              Using selected source for the next answer: <code>{joined}</code>
            </div>
            """,
            unsafe_allow_html=True,
        )


def openrouter_budget_help_html() -> str:
    """Return the exact local action needed for OpenRouter budget guard failures."""
    return (
        "Restart this app with the budget guard in the same shell: "
        f"<code>{html.escape(OPENROUTER_STREAMLIT_COMMAND)}</code>"
    )


def render_setup_required(what_happened: str, technical_detail: str, extra_action_html: str = "") -> None:
    """Render expected local setup blockers without making the app look broken."""
    safe_detail = sanitize_error_detail(technical_detail)
    extra_action = f"<div style='margin-top:6px'>{extra_action_html}</div>" if extra_action_html else ""
    is_zh = is_session_chinese()
    
    label = "需要配置" if is_zh else "Setup required"
    what_happened_lbl = "发生原因" if is_zh else "What happened"
    what_to_do_lbl = "解决方案" if is_zh else "What to do"
    action_text = (
        "请检查侧边栏选择的后端，或在启动应用时带上所需环境配置。"
        if is_zh else
        "Check the selected backend in the sidebar, or restart the app with the required environment variables."
    )
    details_lbl = "配置详情" if is_zh else "Setup details"

    render_notice(
        f"""
        <div class="vault-panel-label">{label}</div>
        <div><strong>{what_happened_lbl}:</strong> {html.escape(what_happened)}</div>
        <div style="margin-top:8px"><strong>{what_to_do_lbl}:</strong></div>
        <div style="margin-top:6px">{action_text}</div>
        {extra_action}
        """,
        tone="amber",
    )
    if safe_detail:
        with st.expander(details_lbl, expanded=False):
            st.code(safe_detail, language=None)


def render_query_error(what_happened: str, technical_detail: str, extra_action_html: str = "") -> None:
    """Render a user-friendly query failure block."""
    safe_detail = sanitize_error_detail(technical_detail)
    extra_action = f"<div>{extra_action_html}</div>" if extra_action_html else ""
    is_zh = is_session_chinese()

    label = "查询失败" if is_zh else "Query failed"
    what_happened_lbl = "发生原因" if is_zh else "What happened"
    what_to_try_lbl = "解决方案" if is_zh else "What to try"
    check_api_text = "检查您的 API Key 是否配置正确" if is_zh else "Check your API key is set correctly"
    switch_backend_text = (
        "尝试在侧边栏切换使用 Anthropic 或 OpenRouter 接口后端"
        if is_zh else
        "Try switching between Anthropic (API) and OpenRouter (API) in the sidebar"
    )
    ollama_text = (
        "如果启用了本地 Ollama 后端，请确保服务已启动：<code>ollama serve</code>"
        if is_zh else
        "If local Ollama is intentionally enabled, make sure it's running: <code>ollama serve</code>"
    )
    details_lbl = "错误详情" if is_zh else "Error details"

    render_notice(
        f"""
        <div class="vault-panel-label">{label}</div>
        <div><strong>{what_happened_lbl}:</strong> {html.escape(what_happened)}</div>
        <div style="margin-top:8px"><strong>{what_to_try_lbl}:</strong></div>
        <div style="margin-top:6px">- {check_api_text}</div>
        <div>- {switch_backend_text}</div>
        {extra_action}
        <div style="margin-top:4px">- {ollama_text}</div>
        """,
        tone="red",
    )
    with st.expander(details_lbl, expanded=True):
        st.code(safe_detail, language=None)


def sanitize_error_detail(detail: str) -> str:
    """Keep backend errors readable while masking common API-key shapes."""
    text = str(detail or "").strip()
    secret_patterns = [
        r"sk-or-v1-[A-Za-z0-9_-]+",
        r"sk-ant-[A-Za-z0-9_-]+",
        r"sk-[A-Za-z0-9_-]{20,}",
    ]
    for pattern in secret_patterns:
        text = re.sub(pattern, "[redacted-api-key]", text)
    return text or "No technical detail returned."


def query_error_label(error: Exception) -> str:
    """Short label for the collapsed Streamlit status row."""
    detail = re.sub(r"\s+", " ", sanitize_error_detail(str(error))).strip()
    is_zh = is_session_chinese()
    fail_lbl = "查询失败" if is_zh else "Query failed"
    if not detail:
        return fail_lbl
    if len(detail) > 150:
        detail = f"{detail[:147].rstrip()}..."
    return f"{fail_lbl}: {detail}"


# ---------------------------------------------------------------------------
# Cached resources (built once per app session)
# ---------------------------------------------------------------------------

@st.cache_resource
def get_client(backend: str):
    return make_client(backend)


@st.cache_resource
def get_source_index():
    return build_source_index(VAULT_ROOT)


@st.cache_resource
def get_source_titles():
    return build_source_titles(VAULT_ROOT)


@st.cache_resource
def get_source_weights():
    return build_source_weights(VAULT_ROOT)


def is_ollama_reachable() -> bool:
    """Return True when the local Ollama HTTP server is reachable."""
    try:
        urllib.request.urlopen("http://localhost:11434", timeout=1)
        return True
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Feline Research OS",
    page_icon="🐱",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400&display=swap');

    :root {
      --bg: #0a0c10;
      --surface: #12151c;
      --surface-2: #1a1e28;
      --border: #252a38;
      --border-subtle: #1e222d;
      --text: #eceff4;
      --text-secondary: #b8bfcc;
      --muted: #7c8494;
      --subtle: #4a5064;
      /* Accent colors - refined */
      --accent-green: #10b981;
      --accent-amber: #d97706;
      --accent-gray: #6b7280;
    }

    /* Base font - Inter for UI, better screen rendering */
    html, body, [class*="css"] {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, system-ui, sans-serif !important;
      font-size: 14px;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      letter-spacing: -0.011em;
    }

    /* Elegant serif typography for primary body text - Source Serif 4 */
    .block-container [data-testid="stMarkdownContainer"] p,
    .block-container [data-testid="stMarkdownContainer"] li,
    .block-container [data-testid="stMarkdownContainer"] p *,
    .block-container [data-testid="stMarkdownContainer"] li * {
      font-family: 'Source Serif 4', 'Georgia', serif !important;
      font-size: 16px !important;
      line-height: 1.75 !important;
      letter-spacing: 0.003em !important;
      color: var(--text) !important;
    }

    /* Keep inline code and code blocks monospace - JetBrains Mono */
    .block-container [data-testid="stMarkdownContainer"] code {
      font-family: 'JetBrains Mono', 'SF Mono', monospace !important;
      font-size: 13px !important;
      letter-spacing: -0.02em !important;
    }

    /* Keep headings sans-serif with better tracking */
    .block-container [data-testid="stMarkdownContainer"] h1,
    .block-container [data-testid="stMarkdownContainer"] h2,
    .block-container [data-testid="stMarkdownContainer"] h3,
    .block-container [data-testid="stMarkdownContainer"] h4 {
      font-family: 'Inter', system-ui, sans-serif !important;
      font-weight: 600 !important;
      letter-spacing: -0.025em !important;
      margin-top: 1.5em !important;
      margin-bottom: 0.75em !important;
    }

    [data-testid="stAppViewContainer"],
    [data-testid="stApp"],
    .stApp {
      background: var(--bg);
      color: var(--text);
    }

    [data-testid="stHeader"] {
      background: rgba(10,12,16,0.92);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--border-subtle);
    }

    [data-testid="stSidebar"] {
      background: linear-gradient(180deg, var(--surface) 0%, var(--bg) 100%);
      border-right: 1px solid var(--border-subtle);
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .stCaption {
      color: var(--muted) !important;
      font-size: 13px !important;
    }

    .block-container {
      max-width: 1080px;
      padding-top: 2.5rem;
      padding-bottom: 4rem;
      padding-left: 2rem;
      padding-right: 2rem;
    }

    /* Monospace: code, source IDs, file paths */
    code, pre, .stCode, [data-testid="stCode"] {
      font-family: 'JetBrains Mono', 'SF Mono', monospace !important;
      font-size: 12.5px !important;
      letter-spacing: -0.01em !important;
    }

    /* Captions and metadata in muted mono */
    .stCaption, [data-testid="stCaptionContainer"] {
      font-family: 'JetBrains Mono', monospace !important;
      font-size: 11px !important;
      color: var(--muted) !important;
      letter-spacing: 0.01em !important;
    }

    /* Chat answer max-width - slightly wider for readability */
    [data-testid="stChatMessageContent"] {
      max-width: 760px;
    }

    [data-testid="stChatMessage"] {
      background: transparent;
      margin-bottom: 1rem;
    }

    [data-testid="stChatMessageContent"] > div {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px 24px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }

    [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] p {
      color: var(--text);
    }

    [data-testid="stSelectbox"] > div,
    [data-testid="stTextInput"] > div,
    [data-testid="stNumberInput"] > div,
    [data-testid="stTextArea"] > div {
      background: var(--surface);
    }

    [data-testid="stSelectbox"] [data-baseweb="select"] > div,
    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea {
      background: var(--surface) !important;
      border: 1px solid var(--border) !important;
      border-radius: 8px !important;
      color: var(--text) !important;
      box-shadow: none !important;
      font-size: 14px !important;
      padding: 10px 14px !important;
    }

    [data-testid="stButton"] button,
    [data-testid="baseButton-secondary"] {
      background: var(--surface) !important;
      color: var(--text) !important;
      border: 1px solid var(--border) !important;
      border-radius: 8px !important;
      font-weight: 500 !important;
      font-size: 13px !important;
      padding: 8px 16px !important;
      transition: all 150ms ease-out;
    }

    [data-testid="stButton"] button:hover,
    [data-testid="baseButton-secondary"]:hover {
      background: var(--surface-2) !important;
      border-color: var(--subtle) !important;
      transform: translateY(-1px);
    }

    [data-testid="stExpander"] {
      border: 1px solid var(--border) !important;
      border-radius: 12px !important;
      background: var(--surface);
      overflow: hidden;
      margin-bottom: 1rem;
    }

    [data-testid="stExpander"] details summary {
      background: var(--surface);
      padding: 14px 16px;
      font-weight: 500;
    }

    [data-testid="stChatInput"] {
      background: linear-gradient(180deg, transparent 0%, var(--bg) 30%);
      padding-top: 16px;
      padding-bottom: 8px;
    }

    [data-testid="stChatInput"] textarea,
    [data-testid="stChatInput"] input {
      background: var(--surface) !important;
      border: 1px solid var(--border) !important;
      border-radius: 12px !important;
      color: var(--text) !important;
      font-size: 15px !important;
      padding: 14px 18px !important;
    }

    /* Figure captions under st.image() */
    [data-testid="stImage"] figcaption,
    [data-testid="stImageCaption"] {
      font-family: 'JetBrains Mono', monospace !important;
      font-size: 11px !important;
      color: var(--muted) !important;
      margin-top: 6px;
      letter-spacing: 0.01em;
    }

    .vault-hero {
      padding: 12px 0 32px 0;
    }

    .vault-kicker,
    .vault-panel-label {
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 10px;
    }

    .vault-hero h1 {
      margin: 0;
      font-size: 36px;
      line-height: 1.15;
      font-weight: 600;
      letter-spacing: -0.03em;
      color: var(--text);
    }

    .vault-hero p,
    .vault-panel-copy {
      margin: 14px 0 0 0;
      font-size: 15px;
      line-height: 1.7;
      color: var(--text-secondary);
      max-width: 640px;
    }

    .vault-statline {
      margin-top: 18px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--muted);
      letter-spacing: 0.02em;
    }

    .vault-panel {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 18px 20px;
    }

    .vault-main-header {
      padding: 8px 0 24px 0;
    }

    .vault-main-header h1 {
      margin: 0;
      font-size: 28px;
      line-height: 1.2;
      font-weight: 600;
      letter-spacing: -0.025em;
      color: var(--text);
    }

    .vault-search-card {
      padding: 14px 16px;
      margin-bottom: 10px;
    }

    .vault-search-title {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: var(--text);
      margin-bottom: 6px;
      letter-spacing: -0.01em;
    }

    .vault-search-subtitle {
      font-size: 12px;
      color: var(--muted);
      line-height: 1.6;
    }

    .vault-search-snippet {
      margin: 10px 0 12px 0;
      padding: 12px 14px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      line-height: 1.7;
      color: var(--text-secondary);
      background: var(--surface-2);
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow-wrap: anywhere;
    }

    .vault-search-snippet mark {
      background: rgba(217,119,6,0.2);
      color: #fbbf24;
      padding: 1px 3px;
      border-radius: 3px;
    }

    .trace-passage {
      margin: 8px 0 12px 0;
      padding: 12px 14px;
      background: rgba(20,20,25,0.82);
      border-left: 3px solid rgba(217,119,6,0.72);
      border-radius: 6px;
      color: var(--text-secondary);
      font-family: 'Source Serif 4', Georgia, serif;
      font-size: 15px;
      line-height: 1.75;
    }

    .trace-highlight {
      background: rgba(217,119,6,0.24);
      color: #f8d48a;
      padding: 1px 3px;
      border-radius: 3px;
    }

    .vault-answer-row {
      padding: 14px 0 12px 0;
      border-top: 1px solid var(--border-subtle);
    }

    .vault-answer-title {
      color: var(--text);
      font-size: 14px;
      font-weight: 500;
      line-height: 1.5;
      letter-spacing: -0.01em;
    }

    .vault-answer-meta,
    .vault-answer-file,
    .vault-answer-sources {
      margin-top: 8px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--muted);
      line-height: 1.6;
    }

    .vault-answer-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }

    .vault-answer-sources {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
    }

    .vault-answer-preview {
      margin: 4px 0 8px 0;
      color: var(--text-secondary);
      font-size: 13px;
      line-height: 1.6;
    }

    .vault-inline-note {
      margin: 14px 0;
      padding: 12px 14px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      color: var(--text-secondary);
      font-size: 13px;
      line-height: 1.6;
    }

    .vault-inline-note-amber {
      background: rgba(217,119,6,0.08);
      border-color: rgba(217,119,6,0.2);
      color: #fbbf24;
    }

    .vault-inline-note-red {
      background: rgba(239,68,68,0.08);
      border-color: rgba(239,68,68,0.2);
      color: #fca5a5;
    }

    .vault-inline-note-green {
      background: rgba(16,185,129,0.08);
      border-color: rgba(16,185,129,0.2);
      color: #6ee7b7;
    }

    .vault-inline-note code {
      color: var(--text);
      background: var(--surface-2);
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid var(--border);
    }

    .vault-trace-step {
      display: grid;
      grid-template-columns: 28px minmax(150px, 0.36fr) minmax(0, 1fr);
      gap: 12px;
      align-items: start;
      padding: 10px 0;
      border-top: 1px solid var(--border-subtle);
      color: var(--text);
      font-size: 13px;
    }

    .vault-trace-step code {
      color: var(--muted);
      background: var(--surface-2);
      border: 1px solid var(--border);
      border-radius: 4px;
      text-align: center;
      font-size: 11px;
    }

    .vault-trace-step strong {
      font-weight: 600;
    }

    .vault-trace-step span {
      color: var(--text-secondary);
      overflow-wrap: anywhere;
    }

    .vault-trace-item {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      padding: 6px 0 6px 40px;
      color: var(--muted);
      font-size: 12px;
    }

    .vault-trace-item span {
      font-family: 'JetBrains Mono', monospace;
      color: var(--text);
    }

    .vault-trace-item em {
      color: var(--muted);
      font-style: normal;
    }

    .vault-guide-row {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-top: 10px;
      color: var(--text);
      font-size: 13px;
    }

    .vault-review-steps {
      display: grid;
      gap: 10px;
      margin: 10px 0 14px 0;
    }

    .vault-review-steps div {
      display: grid;
      grid-template-columns: 28px minmax(0, 1fr);
      gap: 10px;
      align-items: start;
      color: var(--text-secondary);
      font-size: 13px;
      line-height: 1.6;
    }

    .vault-review-steps code {
      display: inline-flex;
      justify-content: center;
      color: var(--text);
      background: var(--surface-2);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 2px 0;
    }

    .prov-badge {
      display: inline-flex;
      align-items: center;
      padding: 3px 10px;
      border-radius: 5px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      white-space: nowrap;
      border: 1px solid transparent;
      font-weight: 500;
    }

    .prov-quoted {
      color: var(--accent-green);
      background: rgba(16,185,129,0.1);
      border-color: rgba(16,185,129,0.25);
    }

    .prov-supported {
      color: var(--accent-amber);
      background: rgba(217,119,6,0.1);
      border-color: rgba(217,119,6,0.25);
    }

    .prov-inference {
      color: var(--accent-gray);
      background: rgba(107,114,128,0.1);
      border-color: rgba(107,114,128,0.25);
    }

    .vault-sidebar-meta {
      margin-top: 12px;
      padding: 14px 16px;
    }

    .vault-sidebar-meta-row {
      display: flex;
      justify-content: space-between;
      gap: 14px;
      margin-top: 10px;
      font-size: 11px;
      font-family: 'JetBrains Mono', monospace;
      color: var(--muted);
    }

    .vault-sidebar-meta-row strong {
      color: var(--text);
      font-weight: 500;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Backend selection (before sidebar — used in API key guard)
# ---------------------------------------------------------------------------

# Stored in query params so changing it triggers a full rerun. OpenRouter is
# available only when selected explicitly; fresh loads default to Anthropic.
_preferred_backend = "local"
_backend_default = st.query_params.get("backend", _preferred_backend)
if _backend_default not in AVAILABLE_BACKENDS:
    _backend_default = "local"
    if st.query_params.get("backend") != _backend_default:
        st.query_params["backend"] = _backend_default
        st.rerun()

# ---------------------------------------------------------------------------
# Session state init
# ---------------------------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []
if "last_files_loaded" not in st.session_state:
    st.session_state.last_files_loaded = []
if "last_meta" not in st.session_state:
    st.session_state.last_meta = {}
if "pending_question" not in st.session_state:
    st.session_state.pending_question = None
if "active_search_result" not in st.session_state:
    st.session_state.active_search_result = None
if "preferred_source_ids" not in st.session_state:
    st.session_state.preferred_source_ids = []
if "how_it_works_seen" not in st.session_state:
    st.session_state.how_it_works_seen = False
if "show_briefing" not in st.session_state:
    st.session_state.show_briefing = None  # Disease code to show briefing for
if "use_workspace_tabs" not in st.session_state:
    st.session_state.use_workspace_tabs = True  # ENABLED: Research Workspace split into 5 tabs
if "last_answer_payload" not in st.session_state:
    st.session_state.last_answer_payload = None
if "last_record_draft" not in st.session_state:
    st.session_state.last_record_draft = None
if "last_record_saved_path" not in st.session_state:
    st.session_state.last_record_saved_path = None
if "last_claim_draft" not in st.session_state:
    st.session_state.last_claim_draft = None
if "last_promotion_result" not in st.session_state:
    st.session_state.last_promotion_result = None

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

backend_blocker: Optional[str] = None

is_zh = is_session_chinese()

# ---------------------------------------------------------------------------
# Deep Extraction Detail Page
# ---------------------------------------------------------------------------
detail_source_id = st.query_params.get("detail")
if detail_source_id:
    # Render the deep extraction detail page
    if has_deep_extraction(detail_source_id):
        extraction = parse_deep_extraction(detail_source_id)
        if extraction:
            # Back button
            if st.button("← 返回" if is_zh else "← Back"):
                del st.query_params["detail"]
                st.rerun()

            # Render the detail page
            detail_md = render_detail_page_markdown(extraction)
            st.markdown(detail_md, unsafe_allow_html=True)
            st.stop()

    # If no deep extraction found, show error and redirect
    st.error(f"Deep extraction not found for {detail_source_id}")
    if st.button("← 返回" if is_zh else "← Back"):
        del st.query_params["detail"]
        st.rerun()
    st.stop()

workspace_param = st.query_params.get("workspace", "ask")
if workspace_param == "cases":
    with st.sidebar:
        workspace = st.radio(
            "Workspace",
            ["Ask", "Research Cases", "Research Records"],
            index=1,
            horizontal=True,
            label_visibility="collapsed",
            format_func=lambda x: {
                "Ask": "知识解答",
                "Research Cases": "研究案例",
                "Research Records": "研究记录"
            }.get(x, x) if is_zh else x
        )
        st.divider()
        cases_title = "研究案例" if is_zh else "Research Cases"
        cases_desc = "从架构分析到挑战评估的持久性证据工作流。" if is_zh else "Durable evidence work from Frame through Challenge."
        st.markdown(
            f"""
            <div class="vault-panel">
              <div class="vault-kicker">Feline Research OS</div>
              <div style="font-size:20px;font-weight:600;color:#e8eaf0">{cases_title}</div>
              <div style="font-size:13px;color:#8b90a0;margin-top:8px">
                {cases_desc}
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    if workspace == "Ask":
        st.query_params["workspace"] = "ask"
        st.rerun()
    elif workspace == "Research Records":
        st.query_params["workspace"] = "records"
        st.rerun()
    render_research_cases(VAULT_ROOT)
    st.stop()

if workspace_param == "records":
    with st.sidebar:
        workspace = st.radio(
            "Workspace",
            ["Ask", "Research Cases", "Research Records"],
            index=2,
            horizontal=True,
            label_visibility="collapsed",
            format_func=lambda x: {
                "Ask": "知识解答",
                "Research Cases": "研究案例",
                "Research Records": "研究记录"
            }.get(x, x) if is_zh else x
        )
        st.divider()
        records_title = "研究记录" if is_zh else "Research Records"
        records_desc = "自动化评估循环进度与验证历史。" if is_zh else "Harness loop progress and verification history."
        st.markdown(
            f"""
            <div class="vault-panel">
              <div class="vault-kicker">Feline Research OS</div>
              <div style="font-size:20px;font-weight:600;color:#e8eaf0">{records_title}</div>
              <div style="font-size:13px;color:#8b90a0;margin-top:8px">
                {records_desc}
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    if workspace == "Ask":
        st.query_params["workspace"] = "ask"
        st.rerun()
    elif workspace == "Research Cases":
        st.query_params["workspace"] = "cases"
        st.rerun()
    render_research_records(VAULT_ROOT)
    st.stop()

with st.sidebar:
    ask_title = "知识解答" if is_zh else "Ask the vault"
    ask_desc = "提出猫科医学问题，获取科学证据、不确定性及下一步建议。" if is_zh else "Ask a natural question. Get evidence, uncertainty, and a next step."
    st.markdown(
        f"""
        <div class="vault-panel" style="margin-bottom:12px">
          <div class="vault-kicker">Feline Research OS</div>
          <div style="font-size:20px;font-weight:600;color:#e8eaf0;line-height:1.15">{ask_title}</div>
          <div style="font-size:13px;color:#8b90a0;margin-top:8px">{ask_desc}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()
    workspace = st.radio(
        "Workspace",
        ["Ask", "Research Cases", "Research Records"],
        horizontal=True,
        label_visibility="collapsed",
        format_func=lambda x: {
            "Ask": "知识解答",
            "Research Cases": "示例任务",
            "Research Records": "历史任务"
        }.get(x, x) if is_zh else x
    )
    if workspace == "Research Cases":
        st.query_params["workspace"] = "cases"
        st.rerun()
    elif workspace == "Research Records":
        st.query_params["workspace"] = "records"
        st.rerun()
    st.divider()

    engine_lbl = "回答引擎" if is_zh else "Answer engine"
    st.markdown(f"<div class='vault-panel-label'>{engine_lbl}</div>", unsafe_allow_html=True)
    
    backend_options = [BACKEND_LABELS[name] for name in AVAILABLE_BACKENDS]
    engine_help = (
        "Anthropic 模式需要配置 ANTHROPIC_API_KEY。OpenRouter 模式需要配置 OPENROUTER_API_KEY。设置 ENABLE_OLLAMA=true 启用本地 Ollama。"
        if is_zh else
        "Anthropic requires ANTHROPIC_API_KEY. OpenRouter requires OPENROUTER_API_KEY. Set ENABLE_OLLAMA=true to show local Ollama."
    )
    backend_choice = st.selectbox(
        "Answer engine",
        options=backend_options,
        index=AVAILABLE_BACKENDS.index(_backend_default),
        help=engine_help,
        label_visibility="collapsed",
    )
    if backend_choice.startswith("Vault Search"):
        backend = "local"
        active_model = "no API"
    elif backend_choice.startswith("Anthropic"):
        backend = "anthropic"
        active_model = MODEL
    elif backend_choice.startswith("OpenRouter"):
        backend = "openrouter"
        active_model = os.environ.get("OPENROUTER_MODEL", OPENROUTER_MODEL)
    else:
        backend = "ollama"
        active_model = OLLAMA_MODEL

    if backend != _backend_default:
        st.query_params["backend"] = backend
        st.rerun()

    if backend == "local":
        local_msg = (
            "本地检索免费且不调用任何 API。需要多源合成与推理时再切换到 API 引擎。"
            if is_zh else
            "Vault Search is free and does not call an API. Switch to an API engine only when you need synthesis."
        )
        render_notice(local_msg, tone="green")
    elif backend == "ollama":
        if is_ollama_reachable():
            ollama_ok = "Ollama 已连接。" if is_zh else "Ollama connected."
            render_notice(ollama_ok, tone="green")
        else:
            ollama_fail_block = "本地 Ollama 未能连接。请在提问前运行 `ollama serve`。" if is_zh else "Ollama is not reachable. Run `ollama serve` before asking."
            backend_blocker = ollama_fail_block
            ollama_fail_notice = "Ollama 未能连接。请运行 <code>ollama serve</code>。" if is_zh else "Ollama not reachable. Run <code>ollama serve</code>."
            render_notice(ollama_fail_notice, tone="amber")
    elif backend == "openrouter":
        if os.environ.get("OPENROUTER_API_KEY"):
            try:
                openrouter_budget = validate_openrouter_budget()
            except ValueError as exc:
                backend_blocker = str(exc)
                render_notice(
                    f"{html.escape(str(exc))}<div style='margin-top:8px'>{openrouter_budget_help_html()}</div>",
                    tone="amber",
                )
            else:
                or_ok = (
                    f"OpenRouter 密钥已加载。项目每日额度守护：${openrouter_budget:.2f}。"
                    if is_zh else
                    f"OpenRouter key loaded. Project daily budget guard: ${openrouter_budget:.2f}."
                )
                render_notice(or_ok, tone="green")
        else:
            or_block = "未检测到 OPENROUTER_API_KEY。请配置环境变量。" if is_zh else "OPENROUTER_API_KEY is not set in this shell or Streamlit secrets."
            backend_blocker = or_block
            or_notice = (
                "未检测到 OPENROUTER_API_KEY。请在提问前配置该密钥或切换引擎。"
                if is_zh else
                "OPENROUTER_API_KEY not set. Switch backend or set the key in the shell or Streamlit secrets before asking."
            )
            render_notice(or_notice, tone="amber")
    elif backend == "anthropic" and not os.environ.get("ANTHROPIC_API_KEY"):
        ant_block = "未检测到 ANTHROPIC_API_KEY。请配置环境变量。" if is_zh else "ANTHROPIC_API_KEY is not set in this shell or Streamlit secrets."
        backend_blocker = ant_block
        ant_notice = (
            "未检测到 ANTHROPIC_API_KEY。请在提问前配置该密钥或切换引擎。"
            if is_zh else
            "ANTHROPIC_API_KEY not set. Switch backend or set the key in the shell or Streamlit secrets before asking."
        )
        render_notice(ant_notice, tone="amber")

    paid_api_confirmed = False
    if backend not in {"local", "ollama"}:
        chk_lbl = "允许在此会话中调用付费 API" if is_zh else "Allow paid API synthesis for this session"
        chk_hlp = (
            "简单查询请保持关闭。只有在需要模型跨文献合成并接受 Token 开销时再开启。"
            if is_zh else
            "Keep this off for simple lookup. Turn it on only when you want the model to synthesize across sources and accept token cost."
        )
        paid_api_confirmed = st.checkbox(
            chk_lbl,
            value=False,
            help=chk_hlp,
        )
        if not paid_api_confirmed:
            paid_lock = (
                "付费 API 综合解答已锁定。使用本地免费检索，或勾选上方选项以确认调用 API。"
                if is_zh else
                "Paid API synthesis is locked. Use Vault Search for free lookup, or tick the checkbox above to spend tokens intentionally."
            )
            render_notice(paid_lock, tone="amber")

    disease_lbl = "分析病种" if is_zh else "Condition"
    st.markdown(f"<div class='vault-panel-label'>{disease_lbl}</div>", unsafe_allow_html=True)
    disease_hlp = (
        "保持在自动检测以使路由器从您的问题中自动判定病种。"
        if is_zh else
        "Leave on Auto-detect to let the router determine the disease from your question."
    )
    disease_choice = st.selectbox(
        "Condition",
        options=["Auto-detect", "CKD", "HCM", "FIP", "IBD", "Diabetes", "FCV", "Obesity", "Cancer"],
        index=0,
        help=disease_hlp,
        label_visibility="collapsed",
        format_func=lambda x: {
            "Auto-detect": "自动检测",
            "CKD": "慢性肾脏病",
            "HCM": "肥厚型心肌病",
            "FIP": "传染性腹膜炎",
            "IBD": "炎症性肠病",
            "Diabetes": "糖尿病",
            "FCV": "杯状病毒",
            "Obesity": "肥胖症",
            "Cancer": "肿瘤与癌症"
        }.get(x, x) if is_zh else x
    )
    disease_arg = None if disease_choice == "Auto-detect" else disease_choice.lower()

    adv_title = "高级设置" if is_zh else "Advanced settings"
    with st.expander(adv_title, expanded=False):
        depth_lbl = "搜索深度" if is_zh else "Search depth"
        depth_hlp = (
            "Auto依据问题自动决定；Quick=1-2篇文献；Standard=2-3篇文献；Deep=包含缺陷反思；Audit=寻找冲突证据。"
            if is_zh else
            "Auto detects depth from question type. Quick=1-2 sources. Standard=2-3 sources. Deep=gap reflection. Audit=contrary evidence required."
        )
        # Search depth mode selector (II.Inc style)
        search_depth_mode = st.radio(
            depth_lbl,
            ["Auto", "Quick", "Standard", "Deep", "Audit"],
            horizontal=True,
            index=0,
            help=depth_hlp,
            format_func=lambda x: {
                "Auto": "自动",
                "Quick": "快速",
                "Standard": "标准",
                "Deep": "深度",
                "Audit": "审计"
            }.get(x, x) if is_zh else x
        )
        search_depth_labels = {
            "Auto": None,  # Let TaskEvaluator decide
            "Quick": "quick",
            "Standard": "standard",
            "Deep": "deep",
            "Audit": "evidence_audit",
        }
        explicit_search_depth = search_depth_labels.get(search_depth_mode)

        hops_lbl = "智能体深度" if is_zh else "Agent depth"
        hops_hlp = (
            "智能体深度控制在最终合成前允许跳转加载文献的步数。"
            if is_zh else
            "Higher depth pulls in more readings before the answer is written."
        )
        max_hops = st.slider(
            hops_lbl,
            min_value=1,
            max_value=5,
            value=3,
            help=hops_hlp,
        )

        save_lbl = "自动保存回答" if is_zh else "Auto-save answers"
        save_hlp = (
            "合成后将每个回答作为 Markdown 文件自动保存到本地库中。"
            if is_zh else
            "Saves each answer as a markdown file in the vault after synthesis."
        )
        write_back_on = st.checkbox(
            save_lbl,
            value=False,
            help=save_hlp,
        )

        ext_lbl = "本地结果稀疏时检索 PubMed/Crossref" if is_zh else "Search PubMed/Crossref if local results sparse"
        ext_hlp = (
            "当本地库中匹配文献少于3篇时检索外部数据库。外部结果仅供参考且需要录入。"
            if is_zh else
            "When the vault has fewer than 3 matching sources, search external databases. External results are marked and need intake before becoming vault evidence."
        )
        allow_external_search = st.checkbox(
            ext_lbl,
            value=False,
            help=ext_hlp,
        )

    st.divider()
    find_lbl = "关键词检索" if is_zh else "Find by keyword"
    st.markdown(f"<div class='vault-panel-label'>{find_lbl}</div>", unsafe_allow_html=True)
    placeholder_text = "尝试输入肌酐、SDMA、FIP、肥胖..." if is_zh else "Try phosphorus, SDMA, fibrosis..."
    search_query = st.text_input(
        "Keyword",
        placeholder=placeholder_text,
        label_visibility="collapsed",
    )
    search_scope = st.radio(
        "Scope",
        ["Everywhere", "Sources", "Topic pages"],
        horizontal=True,
        label_visibility="collapsed",
        format_func=lambda x: {
            "Everywhere": "全局",
            "Sources": "文献卡片",
            "Topic pages": "主题页面"
        }.get(x, x) if is_zh else x
    )

    # Sorting controls for researcher workflow
    sort_lbl = "排序方式" if is_zh else "Sort by"
    sort_options = {
        "relevance": "相关性" if is_zh else "Relevance",
        "year_desc": "发表时间" if is_zh else "Year (newest)",
        "citations_desc": "被引次数" if is_zh else "Citations",
        "if_desc": "影响因子" if is_zh else "Impact Factor",
    }
    sort_by = st.radio(
        sort_lbl,
        list(sort_options.keys()),
        horizontal=True,
        label_visibility="collapsed",
        format_func=lambda x: sort_options.get(x, x),
    )
    # Store in session state for use in result rendering
    st.session_state.sort_by = sort_by

    if search_query:
        scope_map = {"Everywhere": "all", "Sources": "raw", "Topic pages": "topics"}
        current_sort = st.session_state.get("sort_by", "relevance")
        results = vault_search(search_query, VAULT_ROOT, scope=scope_map[search_scope], limit=5, sort_by=current_sort)
        if results:
            for i, result in enumerate(results):
                result_id = result["id"] or format_topic_path(result["file"])
                if result_id and result_id.startswith("src-"):
                    display_title = user_visible_source_label(result_id)
                else:
                    display_title = result_id
                
                # Build subtitle with researcher metadata when available
                subtitle_parts = []
                if result.get("title"):
                    subtitle_parts.append(result["title"])
                if result.get("year"):
                    subtitle_parts.append(str(result["year"]))
                if result.get("impact_factor"):
                    subtitle_parts.append(f"IF: {result['impact_factor']}")
                if result.get("citation_count"):
                    subtitle_parts.append(f"被引: {result['citation_count']}")
                subtitle_parts.append(f"{result['matches']} matches")
                subtitle = " · ".join(subtitle_parts)
                st.markdown(
                    SEARCH_CARD_TEMPLATE.format(
                        title=display_title,
                        subtitle=subtitle,
                    ),
                    unsafe_allow_html=True,
                )
                if result["snippets"]:
                    render_search_snippet(result["snippets"][0], search_query)
                button_label = "预览" if is_zh else "Preview"
                if result["id"] and result["id"].startswith("src-"):
                    button_label = "设为下次提问的首选背景" if is_zh else "Use for next answer"
                if st.button(button_label, key=f"search-result-{i}", use_container_width=True):
                    activate_search_result(result)
                    st.rerun()
                if i < len(results) - 1:
                    st.markdown("<div style='margin:6px 0;border-top:1px solid #2d3147'></div>", unsafe_allow_html=True)
        else:
            no_results_msg = "未找到检索结果。请尝试使用简短关键词或切换检索范围。" if is_zh else "No search results yet. Try a simpler keyword or switch scope."
            render_notice(no_results_msg, tone="neutral")

    st.divider()

    # Last query metadata — populated after each query
    if "last_files_loaded" in st.session_state and st.session_state.last_files_loaded:
        readings_lbl = f"已使用文献 ({len(st.session_state.last_files_loaded)})" if is_zh else f"Readings used ({len(st.session_state.last_files_loaded)})"
        with st.expander(
            readings_lbl,
            expanded=False,
        ):
            for p in st.session_state.last_files_loaded:
                try:
                    path_obj = Path(p)
                    if path_obj.is_absolute():
                        rel = path_obj.relative_to(VAULT_ROOT)
                    else:
                        rel = p
                except ValueError:
                    # Path is not relative to VAULT_ROOT, just show as-is
                    rel = p
                
                rel_str = str(rel)
                stem = Path(rel_str).stem
                if "raw/papers" in rel_str or "raw/regulations" in rel_str or stem.startswith("src-"):
                    source_label = user_visible_source_label(stem)
                else:
                    source_label = format_topic_path(rel_str)
                st.write(f"- {source_label}")

    if "last_meta" in st.session_state and st.session_state.last_meta:
        meta = st.session_state.last_meta
        summary_lbl = "回答摘要" if is_zh else "Answer summary"
        with st.expander(summary_lbl, expanded=False):
            topic_lbl = "分析病种" if is_zh else "Topic"
            st.markdown(f"**{topic_lbl}:** `{meta.get('disease', '—')}`")
            conf = meta.get("confidence", "—")
            color = {"high": "green", "medium": "orange", "low": "red"}.get(conf, "gray")
            conf_lbl = "可信度" if is_zh else "Confidence"
            st.markdown(
                f"**{conf_lbl}:** <span style='color:{color};font-weight:bold'>{conf}</span>",
                unsafe_allow_html=True,
            )
            if meta.get("source_ids"):
                sources_lbl = "引用文献卡片" if is_zh else "Sources cited"
                st.write(f"**{sources_lbl}:**")
                for sid in meta["source_ids"]:
                    st.write(user_visible_source_label(str(sid)))
            if meta.get("written_to"):
                saved_msg = f"已保存至 <code>{html.escape(str(meta['written_to']))}</code>。" if is_zh else f"Saved to <code>{html.escape(str(meta['written_to']))}</code>."
                render_notice(
                    saved_msg,
                    tone="green",
                )
            draft_record = st.session_state.last_record_draft
            if draft_record is not None:
                record_lbl = "研究记录" if is_zh else "Research Record"
                st.markdown(f"**{record_lbl}:**")
                st.markdown(f"- **Record ID:** `{draft_record.record_id}`")
                st.markdown(f"- **Verifier:** `{draft_record.verifier_status.value}`")
                if draft_record.selected_evidence:
                    st.markdown(f"- **Selected evidence:** `{len(draft_record.selected_evidence)}`")
                if st.session_state.last_record_saved_path:
                    st.markdown(
                        f"- **Saved path:** `{st.session_state.last_record_saved_path}`"
                    )
                else:
                    duplicate = None
                    try:
                        harness = get_harness_loop(VAULT_ROOT)
                        duplicate = harness.record_store.find_equivalent_record(draft_record)
                    except Exception:
                        duplicate = None
                    if duplicate:
                        dup_msg = f"已存在等效的记录： <code>{html.escape(duplicate.record_id)}</code>。" if is_zh else f"An equivalent record already exists: <code>{html.escape(duplicate.record_id)}</code>."
                        render_notice(
                            dup_msg,
                            tone="amber",
                        )
                btn_lbl = "保存研究记录" if is_zh else "Save Research Record"
                if st.button(
                    btn_lbl,
                    key="save-research-record",
                    use_container_width=True,
                ):
                    try:
                        harness = get_harness_loop(VAULT_ROOT)
                        out_path = harness.save_record(draft_record)
                        saved_path = str(out_path.relative_to(VAULT_ROOT))
                        st.session_state.last_record_saved_path = saved_path
                        st.session_state.last_meta["research_record_saved"] = True
                        st.session_state.last_meta["research_record_path"] = saved_path
                        safe_path_display = Path(saved_path).stem
                        ok_msg = f"研究记录已保存至 <code>{html.escape(safe_path_display)}</code>。" if is_zh else f"Research Record saved to <code>{html.escape(safe_path_display)}</code>."
                        render_notice(
                            ok_msg,
                            tone="green",
                        )
                        st.rerun()
                    except Exception as e:
                        fail_msg = f"无法保存研究记录：{html.escape(str(e))}" if is_zh else f"Couldn't save Research Record: {html.escape(str(e))}"
                        render_notice(
                            fail_msg,
                            tone="red",
                        )
            if st.session_state.last_record_saved_path and draft_record is not None:
                claim_candidates = extract_claim_candidates(draft_record)
                if claim_candidates:
                    claim_lbl = "声称选择草案" if is_zh else "Claim Selection Draft"
                    st.markdown(f"**{claim_lbl}:**")
                    candidate_labels = [
                        f"{claim.claim_id}: {claim.text[:120]}{'...' if len(claim.text) > 120 else ''}"
                        for claim in claim_candidates
                    ]
                    multiselect_lbl = "待验证声称" if is_zh else "Claims to validate"
                    selected_claim_labels = st.multiselect(
                        multiselect_lbl,
                        candidate_labels,
                        default=candidate_labels[:1] if candidate_labels else [],
                        key=f"claim-selection-{draft_record.record_id}",
                    )
                    target_choices = [
                        f"topics/{draft_record.disease or 'general'}/validated-claims.md",
                        f"system/indexes/{draft_record.disease or 'general'}-validated-claims.md",
                    ]
                    select_lbl = "推广目标" if is_zh else "Promotion target"
                    target_page = st.selectbox(
                        select_lbl,
                        target_choices,
                        key=f"claim-target-{draft_record.record_id}",
                        format_func=format_target_choice,
                    )
                    selected_claim_ids = [
                        label.split(":", 1)[0] for label in selected_claim_labels
                    ]
                    draft = build_promotion_draft(
                        draft_record,
                        selected_claim_ids=selected_claim_ids,
                        target_page=target_page,
                    )
                    st.session_state.last_claim_draft = draft
                    st.markdown(f"- **Draft status:** `{draft.status}`")
                    for note in draft.notes:
                        st.markdown(f"- {note}")
                    if draft.validation_results:
                        for result in draft.validation_results:
                            icon = "✓" if result.passed else "✗"
                            st.markdown(
                                f"- {icon} **{result.check_name}** ({result.severity}): {html.escape(result.message)}"
                            )

                    confirm_lbl = "我确认此推广草案已准备就绪，可以应用" if is_zh else "I confirm this promotion draft is ready to apply"
                    confirm_promotion = st.checkbox(
                        confirm_lbl,
                        key=f"confirm-promotion-{draft_record.record_id}",
                        disabled=not draft.ready_for_patch,
                    )
                    apply_lbl = "应用推广" if is_zh else "Apply Promotion"
                    if st.button(
                        apply_lbl,
                        key=f"apply-promotion-{draft_record.record_id}",
                        use_container_width=True,
                        disabled=not (draft.ready_for_patch and confirm_promotion),
                    ):
                        try:
                            validated_store = ValidatedClaimStore(
                                VAULT_ROOT / "system" / "validated-claims"
                            )
                            written = validated_store.promote_draft(
                                draft,
                                vault_root=VAULT_ROOT,
                                validated_by="human",
                            )
                            target_path = written["target_path"]
                            st.session_state.last_promotion_result = {
                                "target": draft.target_page,
                                "target_path": str(target_path.relative_to(VAULT_ROOT.resolve())) if target_path else draft.target_page,
                                "claims": [claim.claim_id for claim in written["claims"]],
                            }
                            st.session_state.last_meta["promotion_applied"] = True
                            st.session_state.last_meta["promotion_target"] = draft.target_page
                            apply_ok = f"成功应用了 {len(written['claims'])} 项声称的推广。" if is_zh else f"Promotion applied for {len(written['claims'])} claim(s)."
                            render_notice(
                                apply_ok,
                                tone="green",
                            )
                            st.rerun()
                        except Exception as e:
                            render_notice(
                                f"Couldn't apply promotion: {html.escape(str(e))}",
                                tone="red",
                            )
                else:
                    st.info("No promotable claims were found in this record yet.")
            if st.session_state.last_promotion_result:
                result = st.session_state.last_promotion_result
                st.markdown("**Promotion Result:**")
                st.markdown(f"- **Target:** `{result['target']}`")
                st.markdown(f"- **Target path:** `{result['target_path']}`")
                st.markdown(f"- **Claims:** `{', '.join(result['claims'])}`")
            figs = meta.get("figures_used") or []
            if figs:
                described = [f for f in figs if f.get("described_in_answer")]
                st.markdown(
                    f"**Figures used:** `{len(figs)}` total · `{len(described)}` described here"
                )
            export_payload = st.session_state.last_answer_payload
            if st.button(
                "Save this answer",
                key="save-last-answer",
                use_container_width=True,
                disabled=not export_payload,
            ):
                try:
                    out_path = write_back(
                        answer=export_payload["answer"],
                        question=export_payload["question"],
                        disease=export_payload["disease"],
                        question_type=export_payload["question_type"],
                        hops_used=export_payload["hops_used"],
                        files_loaded=[Path(p) for p in export_payload["files_loaded"]],
                        vault_root=VAULT_ROOT,
                        figures_used=export_payload["figures_used"] or None,
                    )
                    written_to = str(out_path.relative_to(VAULT_ROOT))
                    st.session_state.last_meta["written_to"] = written_to
                    render_notice(
                        "✅ 已保存至知识库 (Saved to vault).",
                        tone="green",
                    )
                except ValueError as e:
                    render_notice(
                        f"Couldn't save this answer: {html.escape(str(e))}",
                        tone="red",
                    )

            with st.expander("More details", expanded=False):
                st.markdown(f"**Answer style:** `{meta.get('question_type', '—')}`")
                st.markdown(f"**Depth:** `{meta.get('hops_used', '—')}`")
                st.markdown(f"**Estimated size:** `{meta.get('est_tokens', '—')} tokens`")

    st.divider()

    index_size = len(get_source_index())
    runtime_commit = html.escape(get_runtime_commit())
    release_label = html.escape(APP_RELEASE_LABEL)
    st.markdown(
        f"""
        <div class="vault-panel vault-sidebar-meta">
          <div class="vault-panel-label">App status</div>
          <div class="vault-sidebar-meta-row"><span>release</span><strong>{release_label}</strong></div>
          <div class="vault-sidebar-meta-row"><span>commit</span><strong>{runtime_commit}</strong></div>
          <div class="vault-sidebar-meta-row"><span>engine</span><strong>{html.escape(str(active_model))}</strong></div>
          <div class="vault-sidebar-meta-row"><span>vault index</span><strong>{index_size} sources</strong></div>
          <div class="vault-sidebar-meta-row"><span>new saves</span><strong>appear after restart</strong></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

submitted_question = st.chat_input(
    "提出猫科研究问题...",
)
if submitted_question and not st.session_state.pending_question:
    st.session_state.pending_question = submitted_question

show_empty_state = len(st.session_state.messages) == 0 and not st.session_state.pending_question

# Check if we should show a briefing page (Layer 2)
if st.session_state.show_briefing:
    disease_code = st.session_state.show_briefing
    language = "zh" if is_session_chinese() else "en"
    briefing = get_briefing(disease_code, language)
    if briefing:
        render_briefing_page(briefing, st)
    else:
        st.warning(f"No briefing available for {disease_code.upper()}")
        if st.button("← 返回主页"):
            st.session_state.show_briefing = None
            st.rerun()
    st.stop()
elif show_empty_state:
    render_empty_state()
else:
    render_main_header()
    # Show immediate feedback when a question is queued but not yet processed
    if st.session_state.pending_question and len(st.session_state.messages) == 0:
        is_zh = is_session_chinese()
        processing_msg = "正在处理您的问题..." if is_zh else "Processing your question..."
        st.markdown(f"<div style='text-align:center;padding:32px;color:#8b90a0'><span style='font-size:24px'>⏳</span><br/>{processing_msg}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Quick Start response renderer (must be defined before chat history display)
# ---------------------------------------------------------------------------

def render_quick_start_response(output: QuickStartOutput, key_prefix: str = "qs") -> None:
    """Render Quick Start output with navigation buttons."""
    is_zh = is_session_chinese()

    # Render the Quick Start content
    st.markdown(format_quick_start_markdown(output))

    # Add navigation buttons
    st.divider()
    nav_label = "继续深入" if is_zh else "Go deeper"
    st.markdown(f"**{nav_label}**")

    col1, col2 = st.columns(2)
    with col1:
        briefing_label = f"📖 进入 {output.disease} 简报" if is_zh else f"📖 Open {output.disease} Briefing"
        if output.has_briefing:
            if st.button(briefing_label, key=f"{key_prefix}-briefing-{output.disease.lower()}", use_container_width=True):
                st.session_state.show_briefing = output.disease.lower()
                st.rerun()
        else:
            st.button(briefing_label, key=f"{key_prefix}-briefing-disabled-{output.disease.lower()}", use_container_width=True, disabled=True)
            st.caption("暂无简报" if is_zh else "No briefing available")

    with col2:
        workspace_label = f"🔬 深度研究 {output.disease}" if is_zh else f"🔬 Deep Research {output.disease}"
        if st.button(workspace_label, key=f"{key_prefix}-workspace-{output.disease.lower()}", use_container_width=True):
            # Queue a task-oriented research mode query
            if is_zh:
                research_queries = {
                    "hcm": "构建 feline HCM 近三年文献图谱",
                    "ckd": "比较 CKD 诊断与分期指标的研究价值",
                    "fip": "梳理 FIP 治疗研究的药效终点",
                    "diabetes": "提炼猫糖尿病模型的关键评价指标",
                    "ibd": "提炼猫炎症性肠病与小细胞淋巴瘤鉴别诊断的研究发现",
                    "fcv": "分析猫杯状病毒免疫逃逸与毒力演化的关键发现",
                }
            else:
                research_queries = {
                    "hcm": "Build feline HCM evidence map",
                    "ckd": "Compare feline CKD diagnostic and staging indicators",
                    "fip": "Analyze FIP treatment trial efficacy endpoints",
                    "diabetes": "Distill key metrics for feline diabetes models",
                    "ibd": "Distill differentiation of feline IBD and small cell lymphoma",
                    "fcv": "Analyze feline calicivirus immune evasion and virulence evolution",
                }
            query_str = research_queries.get(output.disease.lower(), f"梳理 feline {output.disease.upper()} 相关文献" if is_zh else f"Review feline {output.disease.upper()} literature")
            queue_question(query_str)
            st.rerun()


# ---------------------------------------------------------------------------
# Chat history display
# ---------------------------------------------------------------------------

render_search_context_panel()

for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant":
            # Check if this is a Quick Start response (Layer 1)
            msg_question_type = msg.get("question_type", "")
            quick_start_data = msg.get("quick_start_data")
            if msg_question_type == "quick_start" and quick_start_data:
                # Re-render Quick Start with navigation buttons
                qs_output = QuickStartOutput(
                    disease=quick_start_data["disease"],
                    one_liner=quick_start_data["one_liner"],
                    why_matters=quick_start_data["why_matters"],
                    misconception=quick_start_data["misconception"],
                    when_to_dig_deeper=quick_start_data.get("when_to_dig_deeper", ""),
                    has_briefing=quick_start_data["has_briefing"],
                    language=quick_start_data["language"],
                )
                render_quick_start_response(qs_output, key_prefix=f"history-qs-{i}")
            else:
                # Check if we should use Tab-based Research Workspace (Layer 3)
                msg_workspace_data = msg.get("workspace_data")
                use_tabs = (
                    msg_question_type == "research_search"
                    and msg_workspace_data
                    and st.session_state.get("use_workspace_tabs", True)
                )

                if use_tabs:
                    # Convert structured data to WorkspaceOutput and render with tabs
                    language = "zh" if is_session_chinese() else "en"
                    workspace_output = convert_research_mode_output_to_workspace(msg_workspace_data, language)
                    render_workspace_tabs(workspace_output, st)
                else:
                    # Phase 4: Use v2 renderer when feature flag is enabled
                    render_fn = render_answer_block_v2 if USE_RESULT_PRESENTATION_V2 and RESULT_PRESENTATION_AVAILABLE else render_answer_block
                    render_fn(
                        answer=msg["content"],
                        confidence=msg.get("confidence", "medium"),
                        figures_used=msg.get("figures_used", []),
                        key_prefix=f"history-{i}",
                        source_ids=msg.get("source_ids"),
                        loaded_source_ids=msg.get("loaded_source_ids"),
                        question=msg.get("question", ""),
                        disease=msg.get("disease", ""),
                        question_type=msg_question_type,
                        research_trace=msg.get("research_trace"),
                        harness_result=msg.get("harness_result"),
                        loaded_paths=msg.get("loaded_paths"),
                        backend=msg.get("backend", "openrouter"),
                        refined_query=msg.get("refined_query"),
                        objectives=msg.get("objectives"),
                    )
        else:
            st.markdown(msg["content"])

if st.session_state.get("scroll_to_latest_research_result"):
    scroll_to_latest_research_result()
    st.session_state.scroll_to_latest_research_result = False

# ---------------------------------------------------------------------------
# Query execution
# ---------------------------------------------------------------------------

def run_query(question: str) -> bool:
    """Route, hop, synthesize, render, optionally write back."""

    # Quick Start detection - check if this is a simple explanation request
    quick_start_disease = detect_quick_start_intent(question)
    if quick_start_disease:
        language = "zh" if is_session_chinese() else "en"
        quick_start_output = get_quick_start(quick_start_disease, language)
        if quick_start_output:
            # Render live
            with st.chat_message("assistant"):
                render_quick_start_response(quick_start_output, key_prefix="live-qs")
            # Save Quick Start to session messages so buttons persist across reruns
            st.session_state.messages.append({
                "role": "assistant",
                "content": format_quick_start_markdown(quick_start_output),
                "question": question,
                "disease": quick_start_output.disease,
                "question_type": "quick_start",
                "quick_start_data": {
                    "disease": quick_start_output.disease,
                    "one_liner": quick_start_output.one_liner,
                    "why_matters": quick_start_output.why_matters,
                    "misconception": quick_start_output.misconception,
                    "when_to_dig_deeper": quick_start_output.when_to_dig_deeper,
                    "has_briefing": quick_start_output.has_briefing,
                    "language": quick_start_output.language,
                },
            })
            return True

    source_index = get_source_index()
    source_weights = get_source_weights()

    if backend not in {"local", "ollama"} and not paid_api_confirmed:
        render_setup_required(
            what_happened=(
                "A paid API engine is selected, but paid synthesis is locked. "
                "Use Vault Search for free lookup, or tick the paid API checkbox in the sidebar."
            ),
            technical_detail="Paid API synthesis not confirmed for this session.",
        )
        return False

    if backend == "anthropic" and not os.environ.get("ANTHROPIC_API_KEY"):
        render_setup_required(
            what_happened="Anthropic is selected, but ANTHROPIC_API_KEY is not set in this shell or Streamlit secrets.",
            technical_detail="ANTHROPIC_API_KEY not set",
        )
        render_example_question_chips("anthropic-missing")
        return False

    if backend == "openrouter" and not os.environ.get("OPENROUTER_API_KEY"):
        render_setup_required(
            what_happened="OpenRouter is selected, but OPENROUTER_API_KEY is not set in this shell or Streamlit secrets.",
            technical_detail="OPENROUTER_API_KEY not set",
        )
        render_example_question_chips("openrouter-missing")
        return False

    if backend == "openrouter":
        try:
            validate_openrouter_budget()
        except ValueError as exc:
            render_setup_required(
                what_happened=(
                    "OpenRouter is selected, but this Streamlit process was started without "
                    "the project-side daily budget guard in the shell or Streamlit secrets."
                ),
                technical_detail=str(exc),
                extra_action_html=openrouter_budget_help_html(),
            )
            render_example_question_chips("openrouter-budget-missing")
            return False

    if backend == "ollama" and not is_ollama_reachable():
        render_setup_required(
            what_happened="Ollama is selected, but the local Ollama server is not reachable.",
            technical_detail="Ollama not reachable at http://localhost:11434. Run `ollama serve`, then ask again.",
        )
        render_example_question_chips("ollama-missing")
        return False

    try:
        client = None if backend == "local" else get_client(backend)
    except ImportError as e:
        render_query_error(
            what_happened="A required Python package is missing for the selected backend.",
            technical_detail=str(e),
        )
        return False

    status_label = "Feline Research OS: Initializing Pipeline..."
    with st.status(status_label, expanded=True) as status:
        def handle_status(msg: str):
            st.markdown(f"- ⚙️ {msg}")
            status.update(label=f"Research OS: {msg}")
        try:
            if backend == "local":
                result = run_app_local_query_core(
                    question, VAULT_ROOT, source_index,
                    disease_hint=disease_arg,
                    preferred_source_ids=st.session_state.preferred_source_ids or None,
                    search_limit=8,
                    on_status=handle_status,
                    allow_external_search=allow_external_search,
                )
            else:
                result = run_query_core(
                    client, question, VAULT_ROOT, source_index,
                    source_weights=source_weights,
                    disease_hint=disease_arg,
                    preferred_source_ids=st.session_state.preferred_source_ids or None,
                    max_hops=max_hops,
                    model=active_model,
                    on_status=handle_status,
                    allow_external_search=allow_external_search,
                )
        except SystemExit:
            status.update(label="Could not detect disease", state="error", expanded=True)
            render_notice(
                "I couldn't figure out which disease you're asking about. Try selecting CKD, FIP, HCM, IBD, Diabetes, or FCV in the sidebar, then ask again.",
                tone="amber",
            )
            render_example_question_chips("disease-detect")
            return False
        except NoSourceCardsLoadedError:
            status.update(label="No matching sources loaded", state="error", expanded=True)
            render_notice(
                "No supporting sources matched that question. Try rephrasing it, or pick a specific disease in the sidebar.",
                tone="amber",
            )
            render_example_question_chips("no-sources")
            return False
        except Exception as e:
            detail = str(e)
            if backend == "openrouter" and "OpenAI-compatible backend returned" in detail:
                if "finish_reason='length'" in detail and "content_type=NoneType" in detail:
                    what_happened = (
                        f"OpenRouter model {active_model} used its completion budget without "
                        "returning usable text."
                    )
                else:
                    what_happened = (
                        f"OpenRouter returned a response without usable text for model "
                        f"{active_model}."
                    )
                status.update(label=query_error_label(e), state="error", expanded=True)
                render_query_error(
                    what_happened=what_happened,
                    technical_detail=(
                        f"{detail}\n\n"
                        "Recommended next step: restart the app with "
                        "OPENROUTER_MODEL=openai/gpt-4.1-mini and try again."
                    ),
                )
                return False
            status.update(label=query_error_label(e), state="error", expanded=True)
            render_query_error(
                what_happened="The selected backend could not complete the query.",
                technical_detail=detail,
            )
            return False

        answer = result["answer"]
        figures_used = result["figures_used"]
        detected_disease = result["disease"]
        question_type = result["question_type"]
        hops_used = result["hops_used"]
        loaded_paths = result["loaded_paths"]
        loaded_source_ids = result.get("loaded_source_ids", [])
        research_trace = result.get("research_trace", [])
        est_tokens = result["est_tokens"]
        refined_query = result.get("refined_query", "")
        objectives = result.get("objectives", [])
        workspace_data = result.get("workspace_data")  # Structured data for Tab rendering

        status.update(label="Done", state="complete", expanded=False)

    # --- Parse metadata ---
    confidence = compute_confidence(answer)
    source_ids = parse_source_ids_from_answer(answer)

    # --- Harness Loop (Research Record) - compute before rendering ---
    harness_result = None
    try:
        harness = get_harness_loop(VAULT_ROOT)
        record = harness.evaluate_query(question, explicit_search_depth=explicit_search_depth)
        harness_result = harness.process_query_result(
            record=record,
            answer=answer,
            source_ids=source_ids,
            disease=detected_disease,
            question_type=question_type,
            research_trace=research_trace,
            loaded_source_ids=loaded_source_ids,
        )
    except Exception as e:
        # Harness loop is non-blocking; log but don't fail the query
        pass

    # --- Render answer ---
    with st.chat_message("assistant"):
        # Check if we should use Tab-based Research Workspace (Layer 3)
        use_tabs = (
            question_type == "research_search"
            and workspace_data
            and st.session_state.get("use_workspace_tabs", True)
        )

        if use_tabs:
            # Convert structured data to WorkspaceOutput and render with tabs
            language = "zh" if is_session_chinese() else "en"
            workspace_output = convert_research_mode_output_to_workspace(workspace_data, language)
            render_workspace_tabs(workspace_output, st)
        else:
            # Phase 4: Use v2 renderer when feature flag is enabled
            render_fn = render_answer_block_v2 if USE_RESULT_PRESENTATION_V2 and RESULT_PRESENTATION_AVAILABLE else render_answer_block
            render_fn(
                answer=answer,
                confidence=confidence,
                figures_used=figures_used,
                key_prefix=f"live-{len(st.session_state.messages)}",
                source_ids=source_ids,
                loaded_source_ids=loaded_source_ids,
                question=question,
                disease=detected_disease,
                question_type=question_type,
                research_trace=research_trace,
                harness_result=harness_result,
                loaded_paths=[str(p) for p in loaded_paths],
                backend=backend,
                refined_query=refined_query,
                objectives=objectives,
            )
        if question_type == "research_search":
            st.session_state.scroll_to_latest_research_result = True
            scroll_to_latest_research_result()

    # --- Write-back ---
    written_to = None
    if write_back_on:
        try:
            out_path = write_back(
                answer=answer,
                question=question,
                disease=detected_disease,
                question_type=question_type,
                hops_used=hops_used,
                files_loaded=list(loaded_paths),
                vault_root=VAULT_ROOT,
                figures_used=figures_used if figures_used else None,
            )
            written_to = str(out_path.relative_to(VAULT_ROOT))
            st.toast(f"Saved: {written_to}", icon="✅")
        except ValueError as e:
            st.error(f"Write-back failed: {e}")

    # --- Update session state ---
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "question": question,
        "disease": detected_disease,
        "question_type": question_type,
        "confidence": confidence,
        "figures_used": figures_used,
        "source_ids": source_ids,
        "loaded_source_ids": loaded_source_ids,
        "research_trace": research_trace,
        "harness_result": harness_result,
        "loaded_paths": [str(p) for p in loaded_paths],
        "backend": backend,
        "refined_query": refined_query,
        "objectives": objectives,
        "workspace_data": workspace_data,  # For Tab-based Research Workspace
    })
    if question_type == "research_search":
        st.session_state.scroll_to_latest_research_result = True
    st.session_state.last_files_loaded = [str(p) for p in loaded_paths]

    st.session_state.last_meta = {
        "question_type": question_type,
        "disease": detected_disease,
        "hops_used": hops_used,
        "est_tokens": est_tokens,
        "confidence": confidence,
        "source_ids": source_ids,
        "loaded_source_ids": loaded_source_ids,
        "research_trace": research_trace,
        "written_to": written_to,
        "figures_used": figures_used,
        "preferred_source_ids": list(st.session_state.preferred_source_ids),
        "harness_result": harness_result,
        "research_record_saved": False,
    }
    st.session_state.last_record_saved_path = None
    st.session_state.last_record_draft = harness_result.get("record") if harness_result else None
    st.session_state.last_claim_draft = None
    st.session_state.last_answer_payload = {
        "answer": answer,
        "question": question,
        "disease": detected_disease,
        "question_type": question_type,
        "hops_used": hops_used,
        "files_loaded": [str(p) for p in loaded_paths],
        "figures_used": figures_used,
    }
    return True


# ---------------------------------------------------------------------------
# Input processing
# ---------------------------------------------------------------------------

user_question = st.session_state.pending_question
if user_question:
    st.session_state.pending_question = None
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)
    run_query(user_question)
