"""
scripts/app.py — Streamlit chat UI for the feline research OS vault.

Usage:
    pip install streamlit anthropic openai
    ANTHROPIC_API_KEY=<key> streamlit run scripts/app.py

Opens localhost:8501 in your browser. Type a research question, get a
sourced answer with provenance tags. Optionally auto-save answers from the
sidebar.
"""

import os
import re
import sys
import json
import html
import urllib.request
from pathlib import Path
from typing import Optional

import streamlit as st

# ---------------------------------------------------------------------------
# Path setup — allow importing query.py from the same directory
# ---------------------------------------------------------------------------

SCRIPTS_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from query import (
    MODEL,
    OLLAMA_MODEL,
    OPENROUTER_MODEL,
    NoSourceCardsLoadedError,
    validate_openrouter_budget,
    make_client,
    build_source_index,
    build_source_titles,
    build_source_weights,
    compute_confidence,
    list_saved_answers,
    parse_source_ids_from_answer,
    run_query_core,
    write_back,
)
from search import vault_search


ENABLE_OLLAMA = os.environ.get("ENABLE_OLLAMA", "").lower() in {"1", "true", "yes", "on"}
BACKEND_LABELS = {
    "anthropic": "Anthropic (API)",
    "openrouter": "OpenRouter (API)",
    "ollama": "Ollama (local)",
}
AVAILABLE_BACKENDS = ["anthropic", "openrouter"] + (["ollama"] if ENABLE_OLLAMA else [])
OPENROUTER_STREAMLIT_COMMAND = (
    "OPENROUTER_DAILY_BUDGET_USD=1.00 "
    "OPENROUTER_MODEL=openai/gpt-4.1-mini "
    ".venv/bin/python -m streamlit run scripts/app.py"
)

# ---------------------------------------------------------------------------
# Provenance badge rendering
# ---------------------------------------------------------------------------

BADGE_PATTERNS = [
    (
        r"\[quoted_fact: ([^\]]+)\]",
        r'<span style="background:rgba(22,163,74,0.12);color:#16a34a;padding:2px 8px;'
        r'border:1px solid rgba(22,163,74,0.25);border-radius:4px;font-size:0.75em;white-space:nowrap;'
        r'font-family:\'Geist Mono\',monospace">'
        r"quote: \1</span>",
    ),
    (
        r"\[source_supported_conclusion: ([^\]]+)\]",
        r'<span style="background:rgba(202,138,4,0.12);color:#ca8a04;padding:2px 8px;'
        r'border:1px solid rgba(202,138,4,0.25);border-radius:4px;font-size:0.75em;white-space:nowrap;'
        r'font-family:\'Geist Mono\',monospace">'
        r"supported: \1</span>",
    ),
    (
        r"\[llm_inference\]",
        r'<span style="background:rgba(107,114,128,0.12);color:#6b7280;padding:2px 8px;'
        r'border:1px solid rgba(107,114,128,0.25);border-radius:4px;font-size:0.75em;white-space:nowrap;'
        r'font-family:\'Geist Mono\',monospace">'
        r"inference</span>",
    ),
]

EXAMPLE_QUESTIONS = [
    "解释CKD",
    "FIP怎么识别",
    "IBD和淋巴瘤怎么区分",
    "HCM是什么，为什么危险",
]

PROVENANCE_GUIDE_HTML = """
<div class="vault-panel" style="margin-top:24px">
  <div class="vault-panel-label">Evidence labels</div>
  <div class="vault-guide-row"><span class="prov-badge prov-quoted">quote</span><span>source wording or close paraphrase</span></div>
  <div class="vault-guide-row"><span class="prov-badge prov-supported">supported</span><span>synthesis supported by loaded sources</span></div>
  <div class="vault-guide-row"><span class="prov-badge prov-inference">inference</span><span>reasoning beyond direct source support</span></div>
</div>
"""

EMPTY_STATE_INTRO_HTML = """
<div class="vault-hero">
  <div class="vault-kicker">SOURCE-AWARE FELINE WIKI</div>
  <h1>Ask the vault</h1>
  <p>Ask a natural feline disease question. Get a compact answer that separates evidence, supported synthesis, uncertainty, and the next page worth reading.</p>
  <p>Unlike a generic wiki page, each answer starts from this vault's disease pages and source cards, then shows where the answer is strong and where it is only an inference.</p>
  <div class="vault-statline">0 sources · 0 topic pages · 0 diseases</div>
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
  <div class="vault-panel-label">Why this exists</div>
  <p class="vault-panel-copy">
    The vault turns dense veterinary literature into a first answer surface: practical explanation first,
    source support visible immediately, uncertainty kept in the answer instead of hidden in footnotes.
  </p>
</div>
"""

HOW_IT_WORKS_COPY = (
    "This tool searches six feline disease modules in the vault. It routes to compiled topic pages "
    "and source cards, writes a compact answer, and tags each claim with its evidence level. "
    "Green tags are close to source wording. Amber tags are supported synthesis. "
    "Gray tags mean the answer goes beyond the loaded sources."
)


def render_provenance(text: str) -> str:
    """Replace provenance tags with colored HTML badges."""
    for pattern, replacement in BADGE_PATTERNS:
        text = re.sub(pattern, replacement, text)
    return text


def queue_question(question: str) -> None:
    """Store a question to be executed on the current rerun."""
    st.session_state.pending_question = question


def render_example_question_chips(prefix: str, disabled: bool = False) -> None:
    """Render clickable example questions."""
    cols = st.columns(2)
    for i, question in enumerate(EXAMPLE_QUESTIONS):
        with cols[i % 2]:
            if st.button(question, key=f"{prefix}-example-{i}", use_container_width=True, disabled=disabled):
                queue_question(question)


def render_provenance_guide() -> None:
    """Explain provenance badge colors for new users."""
    st.markdown(PROVENANCE_GUIDE_HTML, unsafe_allow_html=True)


def render_how_it_works() -> None:
    """Show a lightweight onboarding explainer for first-time users."""
    with st.expander("How this works", expanded=not st.session_state.how_it_works_seen):
        st.markdown(HOW_IT_WORKS_HTML, unsafe_allow_html=True)
        st.caption(HOW_IT_WORKS_COPY)
    st.session_state.how_it_works_seen = True


def render_saved_answers_panel(prefix: str, disease_filter: Optional[str] = None) -> None:
    """Render recent saved QA/inbox answers as a reuse surface."""
    saved_answers = list_saved_answers(VAULT_ROOT, limit=5, disease=disease_filter)
    if not saved_answers:
        return

    with st.expander("Previously answered", expanded=False):
        for i, item in enumerate(saved_answers):
            question = html.escape(str(item["question"]))
            topic = html.escape(str(item["topic"]).upper())
            question_type = html.escape(str(item["question_type"]))
            confidence = html.escape(str(item["confidence"]))
            generated_at = html.escape(str(item["generated_at"] or "undated"))
            file_path = html.escape(str(item["file"]))
            source_ids = [html.escape(str(sid)) for sid in item.get("source_ids", [])]
            sources = " ".join(f"<code>{sid}</code>" for sid in source_ids[:4]) or "<span>no cited sources</span>"
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
                  <div class="vault-answer-file">{file_path}</div>
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
                st.rerun()


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

        if st.button("Clear this selection", key="clear-search-context"):
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


def render_answer_block(
    answer: str,
    confidence: str,
    figures_used: list[dict],
    key_prefix: str,
    source_ids: Optional[list[str]] = None,
    loaded_source_ids: Optional[list[str]] = None,
) -> None:
    """Render one assistant answer with provenance, copy button, confidence, figures, and sources."""
    source_ids = source_ids or []
    loaded_source_ids = loaded_source_ids or []
    cleaned_answer = strip_legacy_footer(answer)
    st.markdown(render_provenance(cleaned_answer), unsafe_allow_html=True)
    copy_button(answer, key=f"{key_prefix}-copy")
    render_trust_block(answer, confidence, source_ids, loaded_source_ids)

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


def render_empty_state() -> None:
    """Render first-run onboarding for ordinary users."""
    source_index = get_source_index()
    topic_count = len(list((VAULT_ROOT / "topics").rglob("*.md")))
    disease_count = len([p for p in (VAULT_ROOT / "topics").iterdir() if p.is_dir()])
    st.markdown(
        EMPTY_STATE_INTRO_HTML.replace("0 sources · 0 topic pages · 0 diseases",
                                       f"{len(source_index)} sources · {topic_count} topic pages · {disease_count} diseases"),
        unsafe_allow_html=True,
    )
    st.markdown("<div class='vault-panel'><div class='vault-panel-label'>Try asking</div></div>", unsafe_allow_html=True)
    render_example_question_chips("empty", disabled=backend_blocker is not None)
    render_saved_answers_panel("empty")
    render_provenance_guide()
    render_how_it_works()


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


def render_query_error(what_happened: str, technical_detail: str, extra_action_html: str = "") -> None:
    """Render a user-friendly query failure block."""
    safe_detail = sanitize_error_detail(technical_detail)
    extra_action = f"<div>{extra_action_html}</div>" if extra_action_html else ""
    render_notice(
        f"""
        <div class="vault-panel-label">Query failed</div>
        <div><strong>What happened:</strong> {html.escape(what_happened)}</div>
        <div style="margin-top:8px"><strong>What to try:</strong></div>
        <div style="margin-top:6px">Check your API key is set correctly</div>
        <div>Try switching between Anthropic (API) and OpenRouter (API) in the sidebar</div>
        {extra_action}
        <div>If local Ollama is intentionally enabled, make sure it's running: <code>ollama serve</code></div>
        """,
        tone="red",
    )
    with st.expander("Error details", expanded=True):
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
    if not detail:
        return "Query failed"
    if len(detail) > 150:
        detail = f"{detail[:147].rstrip()}..."
    return f"Query failed: {detail}"


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
    @import url('https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600&family=Geist+Mono:wght@400;500&display=swap');

    :root {
      --bg: #0f1117;
      --surface: #1a1d27;
      --surface-2: #222535;
      --border: #2d3147;
      --text: #e8eaf0;
      --muted: #8b90a0;
      --subtle: #4a4f64;
    }

    /* Base font */
    html, body, [class*="css"] {
      font-family: 'Geist', system-ui, sans-serif !important;
      font-size: 15px;
      line-height: 1.7;
    }

    [data-testid="stAppViewContainer"],
    [data-testid="stApp"],
    .stApp {
      background: var(--bg);
      color: var(--text);
    }

    [data-testid="stHeader"] {
      background: rgba(15,17,23,0.88);
      border-bottom: 1px solid rgba(45,49,71,0.5);
    }

    [data-testid="stSidebar"] {
      background: linear-gradient(180deg, rgba(26,29,39,0.96) 0%, rgba(15,17,23,0.98) 100%);
      border-right: 1px solid rgba(45,49,71,0.85);
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .stCaption {
      color: var(--muted) !important;
    }

    .block-container {
      max-width: 1120px;
      padding-top: 2rem;
      padding-bottom: 3rem;
    }

    /* Monospace: code, source IDs, file paths */
    code, pre, .stCode, [data-testid="stCode"] {
      font-family: 'Geist Mono', monospace !important;
      font-size: 12px !important;
    }

    /* Captions and metadata in muted mono */
    .stCaption, [data-testid="stCaptionContainer"] {
      font-family: 'Geist Mono', monospace !important;
      font-size: 11px !important;
      color: #8b90a0 !important;
    }

    /* Chat answer max-width */
    [data-testid="stChatMessageContent"] {
      max-width: 720px;
    }

    [data-testid="stChatMessage"] {
      background: transparent;
    }

    [data-testid="stChatMessageContent"] > div {
      background: rgba(26,29,39,0.58);
      border: 1px solid rgba(45,49,71,0.72);
      border-radius: 10px;
      padding: 16px 18px;
      box-shadow: inset 0 1px 0 rgba(255,255,255,0.015);
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
      border-radius: 6px !important;
      color: var(--text) !important;
      box-shadow: none !important;
    }

    [data-testid="stButton"] button,
    [data-testid="baseButton-secondary"] {
      background: var(--surface) !important;
      color: var(--text) !important;
      border: 1px solid var(--border) !important;
      border-radius: 6px !important;
      transition: background 120ms ease-out, border-color 120ms ease-out, transform 120ms ease-out;
    }

    [data-testid="stButton"] button:hover,
    [data-testid="baseButton-secondary"]:hover {
      background: var(--surface-2) !important;
      border-color: #3a3f58 !important;
      transform: translateY(-1px);
    }

    [data-testid="stExpander"] {
      border: 1px solid var(--border) !important;
      border-radius: 10px !important;
      background: rgba(26,29,39,0.44);
      overflow: hidden;
    }

    [data-testid="stExpander"] details summary {
      background: rgba(26,29,39,0.84);
    }

    [data-testid="stChatInput"] {
      background: linear-gradient(180deg, rgba(15,17,23,0) 0%, rgba(15,17,23,0.92) 22%, rgba(15,17,23,1) 100%);
      padding-top: 12px;
    }

    [data-testid="stChatInput"] textarea,
    [data-testid="stChatInput"] input {
      background: var(--surface) !important;
      border: 1px solid var(--border) !important;
      border-radius: 10px !important;
      color: var(--text) !important;
    }

    /* Figure captions under st.image() */
    [data-testid="stImage"] figcaption,
    [data-testid="stImageCaption"] {
      font-family: 'Geist Mono', monospace !important;
      font-size: 11px !important;
      color: #8b90a0 !important;
      margin-top: 4px;
    }

    .vault-hero {
      padding: 8px 0 24px 0;
    }

    .vault-kicker,
    .vault-panel-label {
      font-family: 'Geist Mono', monospace;
      font-size: 11px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 8px;
    }

    .vault-hero h1 {
      margin: 0;
      font-size: 40px;
      line-height: 1.05;
      font-weight: 600;
      color: var(--text);
    }

    .vault-hero p,
    .vault-panel-copy {
      margin: 10px 0 0 0;
      font-size: 15px;
      color: var(--muted);
      max-width: 680px;
    }

    .vault-statline {
      margin-top: 14px;
      font-family: 'Geist Mono', monospace;
      font-size: 11px;
      color: var(--muted);
    }

    .vault-panel {
      background: rgba(26,29,39,0.72);
      border: 1px solid rgba(45,49,71,0.9);
      border-radius: 10px;
      padding: 16px;
    }

    .vault-main-header {
      padding: 4px 0 18px 0;
    }

    .vault-main-header h1 {
      margin: 0;
      font-size: 32px;
      line-height: 1.08;
      font-weight: 600;
      color: var(--text);
    }

    .vault-search-card {
      padding: 12px 14px;
      margin-bottom: 8px;
    }

    .vault-search-title {
      font-family: 'Geist Mono', monospace;
      font-size: 12px;
      color: var(--text);
      margin-bottom: 4px;
    }

    .vault-search-subtitle {
      font-size: 11px;
      color: var(--muted);
      line-height: 1.5;
    }

    .vault-search-snippet {
      margin: 8px 0 10px 0;
      padding: 10px 12px;
      font-family: 'Geist Mono', monospace;
      font-size: 11px;
      line-height: 1.6;
      color: var(--muted);
      background: rgba(34,37,53,0.78);
      border: 1px solid rgba(45,49,71,0.82);
      border-radius: 8px;
      overflow-wrap: anywhere;
    }

    .vault-search-snippet mark {
      background: rgba(202,138,4,0.18);
      color: #f0d08b;
      padding: 0 2px;
      border-radius: 3px;
    }

    .vault-answer-row {
      padding: 12px 0 10px 0;
      border-top: 1px solid rgba(45,49,71,0.72);
    }

    .vault-answer-title {
      color: var(--text);
      font-size: 14px;
      font-weight: 500;
      line-height: 1.45;
    }

    .vault-answer-meta,
    .vault-answer-file,
    .vault-answer-sources {
      margin-top: 5px;
      font-family: 'Geist Mono', monospace;
      font-size: 11px;
      color: var(--muted);
      line-height: 1.5;
    }

    .vault-answer-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .vault-answer-sources {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      align-items: center;
    }

    .vault-answer-preview {
      margin: 2px 0 6px 0;
      color: var(--muted);
      font-size: 13px;
      line-height: 1.55;
    }

    .vault-inline-note {
      margin: 12px 0;
      padding: 10px 12px;
      background: rgba(26,29,39,0.6);
      border: 1px solid rgba(45,49,71,0.85);
      border-radius: 8px;
      color: var(--muted);
      font-size: 13px;
    }

    .vault-inline-note-amber {
      background: rgba(202,138,4,0.08);
      border-color: rgba(202,138,4,0.22);
      color: #d6b56b;
    }

    .vault-inline-note-red {
      background: rgba(239,68,68,0.08);
      border-color: rgba(239,68,68,0.22);
      color: #f2b0b0;
    }

    .vault-inline-note-green {
      background: rgba(22,163,74,0.08);
      border-color: rgba(22,163,74,0.22);
      color: #79d094;
    }

    .vault-inline-note code {
      color: var(--text);
      background: rgba(34,37,53,0.9);
      padding: 1px 6px;
      border-radius: 4px;
      border: 1px solid rgba(45,49,71,0.8);
    }

    .vault-guide-row {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-top: 8px;
      color: var(--text);
      font-size: 13px;
    }

    .prov-badge {
      display: inline-flex;
      align-items: center;
      padding: 2px 8px;
      border-radius: 4px;
      font-family: 'Geist Mono', monospace;
      font-size: 11px;
      white-space: nowrap;
      border: 1px solid transparent;
    }

    .prov-quoted {
      color: #16a34a;
      background: rgba(22,163,74,0.12);
      border-color: rgba(22,163,74,0.25);
    }

    .prov-supported {
      color: #ca8a04;
      background: rgba(202,138,4,0.12);
      border-color: rgba(202,138,4,0.25);
    }

    .prov-inference {
      color: #6b7280;
      background: rgba(107,114,128,0.12);
      border-color: rgba(107,114,128,0.25);
    }

    .vault-sidebar-meta {
      margin-top: 10px;
      padding: 12px 14px;
    }

    .vault-sidebar-meta-row {
      display: flex;
      justify-content: space-between;
      gap: 12px;
      margin-top: 8px;
      font-size: 11px;
      font-family: 'Geist Mono', monospace;
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
_preferred_backend = "anthropic"
_backend_default = st.query_params.get("backend", _preferred_backend)
if _backend_default not in AVAILABLE_BACKENDS:
    _backend_default = "anthropic"
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
if "last_answer_payload" not in st.session_state:
    st.session_state.last_answer_payload = None

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

backend_blocker: Optional[str] = None

with st.sidebar:
    st.markdown(
        """
        <div class="vault-panel" style="margin-bottom:12px">
          <div class="vault-kicker">Feline Research OS</div>
          <div style="font-size:20px;font-weight:600;color:#e8eaf0;line-height:1.15">Ask the vault</div>
          <div style="font-size:13px;color:#8b90a0;margin-top:8px">Ask a natural question. Get evidence, uncertainty, and a next step.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()

    st.markdown("<div class='vault-panel-label'>Answer engine</div>", unsafe_allow_html=True)
    backend_options = [BACKEND_LABELS[name] for name in AVAILABLE_BACKENDS]
    backend_choice = st.selectbox(
        "Answer engine",
        options=backend_options,
        index=AVAILABLE_BACKENDS.index(_backend_default),
        help="Anthropic requires ANTHROPIC_API_KEY. OpenRouter requires OPENROUTER_API_KEY. Set ENABLE_OLLAMA=true to show local Ollama.",
        label_visibility="collapsed",
    )
    if backend_choice.startswith("Anthropic"):
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

    if backend == "ollama":
        if is_ollama_reachable():
            render_notice("Ollama connected.", tone="green")
        else:
            backend_blocker = "Ollama is not reachable. Run `ollama serve` before asking."
            render_notice("Ollama not reachable. Run <code>ollama serve</code>.", tone="amber")
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
                render_notice(
                    f"OpenRouter key loaded. Project daily budget guard: ${openrouter_budget:.2f}.",
                    tone="green",
                )
        else:
            backend_blocker = "OPENROUTER_API_KEY is not set in this shell."
            render_notice("OPENROUTER_API_KEY not set. Switch backend or set the key before asking.", tone="amber")
    elif backend == "anthropic" and not os.environ.get("ANTHROPIC_API_KEY"):
        backend_blocker = "ANTHROPIC_API_KEY is not set in this shell."
        render_notice("ANTHROPIC_API_KEY not set. Switch backend or set the key before asking.", tone="amber")

    st.markdown("<div class='vault-panel-label'>Condition</div>", unsafe_allow_html=True)
    disease_choice = st.selectbox(
        "Condition",
        options=["Auto-detect", "CKD", "HCM", "FIP", "IBD", "Diabetes", "FCV"],
        index=0,
        help="Leave on Auto-detect to let the router determine the disease from your question.",
        label_visibility="collapsed",
    )
    disease_arg = None if disease_choice == "Auto-detect" else disease_choice.lower()

    with st.expander("Advanced settings", expanded=False):
        max_hops = st.slider(
            "Depth",
            min_value=1,
            max_value=5,
            value=3,
            help="Higher depth pulls in more readings before the answer is written.",
        )

        write_back_on = st.checkbox(
            "Auto-save answers",
            value=False,
            help="Saves each answer as a markdown file in the vault after synthesis.",
        )

    st.divider()
    st.markdown("<div class='vault-panel-label'>Find by keyword</div>", unsafe_allow_html=True)
    search_query = st.text_input(
        "Keyword",
        placeholder="Try phosphorus, SDMA, fibrosis...",
        label_visibility="collapsed",
    )
    search_scope = st.radio(
        "Scope",
        ["Everywhere", "Sources", "Topic pages"],
        horizontal=True,
        label_visibility="collapsed",
    )
    if search_query:
        scope_map = {"Everywhere": "all", "Sources": "raw", "Topic pages": "topics"}
        results = vault_search(search_query, VAULT_ROOT, scope=scope_map[search_scope], limit=5)
        if results:
            for i, result in enumerate(results):
                result_id = result["id"] or result["file"]
                st.markdown(
                    SEARCH_CARD_TEMPLATE.format(
                        title=result_id,
                        subtitle=(
                            f"{result['title']} · {result['matches']} matches"
                            if result["title"]
                            else f"{result['matches']} matches"
                        ),
                    ),
                    unsafe_allow_html=True,
                )
                if result["snippets"]:
                    render_search_snippet(result["snippets"][0], search_query)
                button_label = "Preview"
                if result["id"] and result["id"].startswith("src-"):
                    button_label = "Use for next answer"
                if st.button(button_label, key=f"search-result-{i}", use_container_width=True):
                    activate_search_result(result)
                    st.rerun()
                if i < len(results) - 1:
                    st.markdown("<div style='margin:6px 0;border-top:1px solid #2d3147'></div>", unsafe_allow_html=True)
        else:
            render_notice("No search results yet. Try a simpler keyword or switch scope.", tone="neutral")

    st.divider()

    # Last query metadata — populated after each query
    if "last_files_loaded" in st.session_state and st.session_state.last_files_loaded:
        with st.expander(
            f"Readings used ({len(st.session_state.last_files_loaded)})",
            expanded=False,
        ):
            for p in st.session_state.last_files_loaded:
                rel = Path(p).relative_to(VAULT_ROOT) if Path(p).is_absolute() else p
                st.code(str(rel), language=None)

    if "last_meta" in st.session_state and st.session_state.last_meta:
        meta = st.session_state.last_meta
        with st.expander("Answer summary", expanded=False):
            st.markdown(f"**Topic:** `{meta.get('disease', '—')}`")
            conf = meta.get("confidence", "—")
            color = {"high": "green", "medium": "orange", "low": "red"}.get(conf, "gray")
            st.markdown(
                f"**Confidence:** <span style='color:{color};font-weight:bold'>{conf}</span>",
                unsafe_allow_html=True,
            )
            if meta.get("source_ids"):
                st.write("**Sources cited:**")
                for sid in meta["source_ids"]:
                    st.code(sid, language=None)
            if meta.get("written_to"):
                render_notice(
                    f"Saved to <code>{html.escape(str(meta['written_to']))}</code>.",
                    tone="green",
                )
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
                        f"Saved to <code>{html.escape(written_to)}</code>.",
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
    st.markdown(
        f"""
        <div class="vault-panel vault-sidebar-meta">
          <div class="vault-panel-label">App status</div>
          <div class="vault-sidebar-meta-row"><span>engine</span><strong>{html.escape(str(active_model))}</strong></div>
          <div class="vault-sidebar-meta-row"><span>vault index</span><strong>{index_size} sources</strong></div>
          <div class="vault-sidebar-meta-row"><span>new saves</span><strong>appear after restart</strong></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

show_empty_state = len(st.session_state.messages) == 0 and not st.session_state.pending_question
if show_empty_state:
    render_empty_state()
else:
    render_main_header()

# ---------------------------------------------------------------------------
# Chat history display
# ---------------------------------------------------------------------------

render_search_context_panel()

for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant":
            render_answer_block(
                answer=msg["content"],
                confidence=msg.get("confidence", "medium"),
                figures_used=msg.get("figures_used", []),
                key_prefix=f"history-{i}",
                source_ids=msg.get("source_ids"),
                loaded_source_ids=msg.get("loaded_source_ids"),
            )
        else:
            st.markdown(msg["content"])

# ---------------------------------------------------------------------------
# Query execution
# ---------------------------------------------------------------------------

def run_query(question: str) -> bool:
    """Route, hop, synthesize, render, optionally write back."""
    if backend == "anthropic" and not os.environ.get("ANTHROPIC_API_KEY"):
        render_query_error(
            what_happened="Anthropic is selected, but ANTHROPIC_API_KEY is not set in this shell.",
            technical_detail="ANTHROPIC_API_KEY not set",
        )
        render_example_question_chips("anthropic-missing")
        return False

    if backend == "openrouter" and not os.environ.get("OPENROUTER_API_KEY"):
        render_query_error(
            what_happened="OpenRouter is selected, but OPENROUTER_API_KEY is not set in this shell.",
            technical_detail="OPENROUTER_API_KEY not set",
        )
        render_example_question_chips("openrouter-missing")
        return False

    if backend == "openrouter":
        try:
            validate_openrouter_budget()
        except ValueError as exc:
            render_query_error(
                what_happened=(
                    "OpenRouter is selected, but this Streamlit process was started without "
                    "the project-side daily budget guard."
                ),
                technical_detail=str(exc),
                extra_action_html=openrouter_budget_help_html(),
            )
            render_example_question_chips("openrouter-budget-missing")
            return False

    if backend == "ollama" and not is_ollama_reachable():
        render_query_error(
            what_happened="Ollama is selected, but the local Ollama server is not reachable.",
            technical_detail="Ollama not reachable at http://localhost:11434. Run `ollama serve`, then ask again.",
        )
        render_example_question_chips("ollama-missing")
        return False

    try:
        client = get_client(backend)
    except ImportError as e:
        render_query_error(
            what_happened="A required Python package is missing for the selected backend.",
            technical_detail=str(e),
        )
        return False
    source_index = get_source_index()
    source_weights = get_source_weights()

    with st.status("Routing question...", expanded=False) as status:
        try:
            result = run_query_core(
                client, question, VAULT_ROOT, source_index,
                source_weights=source_weights,
                disease_hint=disease_arg,
                preferred_source_ids=st.session_state.preferred_source_ids or None,
                max_hops=max_hops,
                model=active_model,
                on_status=lambda msg: status.update(label=msg, expanded=False),
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
        est_tokens = result["est_tokens"]

        status.update(label="Done", state="complete", expanded=False)

    # --- Parse metadata ---
    confidence = compute_confidence(answer)
    source_ids = parse_source_ids_from_answer(answer)

    # --- Render answer ---
    with st.chat_message("assistant"):
        render_answer_block(
            answer=answer,
            confidence=confidence,
            figures_used=figures_used,
            key_prefix=f"live-{len(st.session_state.messages)}",
            source_ids=source_ids,
            loaded_source_ids=loaded_source_ids,
        )

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
        "confidence": confidence,
        "figures_used": figures_used,
        "source_ids": source_ids,
        "loaded_source_ids": loaded_source_ids,
    })
    st.session_state.last_files_loaded = [str(p) for p in loaded_paths]

    st.session_state.last_meta = {
        "question_type": question_type,
        "disease": detected_disease,
        "hops_used": hops_used,
        "est_tokens": est_tokens,
        "confidence": confidence,
        "source_ids": source_ids,
        "loaded_source_ids": loaded_source_ids,
        "written_to": written_to,
        "figures_used": figures_used,
        "preferred_source_ids": list(st.session_state.preferred_source_ids),
    }
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
# Input
# ---------------------------------------------------------------------------

input_placeholder = (
    "Set the selected backend key/budget guard before asking."
    if backend_blocker
    else "Ask a natural feline health question..."
)
user_question = st.session_state.pending_question or st.chat_input(
    input_placeholder,
    disabled=backend_blocker is not None,
)
if user_question:
    st.session_state.pending_question = None
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)
    if run_query(user_question):
        st.rerun()
