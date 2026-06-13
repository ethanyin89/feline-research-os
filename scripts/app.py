"""
scripts/app.py — Streamlit chat UI for the feline research OS vault.

Usage:
    pip install streamlit anthropic openai
    ANTHROPIC_API_KEY=<key> streamlit run scripts/app.py

Opens localhost:8501 in your browser. Type a research question, get a
sourced answer with provenance tags. Optionally save answers from the
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
    build_source_index,
    build_source_titles,
    build_source_weights,
    compute_confidence,
    build_external_search_trace,
    is_local_search_sparse,
    list_saved_answers,
    parse_source_ids_from_answer,
    run_query_core,
    write_back,
)
from expert_review import build_expert_review_prompt, expert_review_stage_label
from search import vault_search

from local_answer_surfaces import build_ckd_researcher_overview, is_researcher_overview_question
from research_case_ui import render_research_cases
from research_record_ui import render_research_records
from harness_loop import get_harness_loop, format_harness_summary
from core import (
    build_promotion_draft,
    extract_claim_candidates,
    ValidatedClaimStore,
)

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
    "This tool searches the feline disease modules in the vault. It routes to compiled topic pages "
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


def render_example_question_chips(prefix: str) -> None:
    """Render clickable example questions."""
    cols = st.columns(2)
    for i, question in enumerate(EXAMPLE_QUESTIONS):
        with cols[i % 2]:
            if st.button(question, key=f"{prefix}-example-{i}", use_container_width=True):
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


def detect_chinese(text: str) -> bool:
    """Return True when text contains CJK characters."""
    return bool(re.search(r"[\u3400-\u9fff]", text))


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
    # if disease == "ckd" and is_researcher_overview_question(question):
    #     return "ckd_researcher_overview"
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
            rid = result.get("id") or result["file"]
            title = result.get("title") or result["file"]
            matched = ", ".join(result.get("matched_terms", [])) or "n/a"
            evidence_lines.append(f"- `{rid}` — {title}; matched terms: {matched}")
        if not evidence_lines:
            evidence_lines.append(no_hits)

        answer = (
            f"{lead}\n\n"
            f"{hit_header}\n" + "\n".join(evidence_lines) + "\n\n"
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

    with st.expander("验证结果 / Expert Review", expanded=has_harness and verification_status != "passed"):
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


def render_source_card_v2(card: "SourceDisplay") -> None:
    """Render a single source card with canonical link."""
    if not RESULT_PRESENTATION_AVAILABLE:
        return

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

    metadata_bits = []
    if card.source_family_label:
        metadata_bits.append(f"家族：{html.escape(card.source_family_label)}")
    if card.species_label:
        metadata_bits.append(f"种属：{html.escape(card.species_label)}")
    if card.decision_grade_label:
        metadata_bits.append(f"决策：{html.escape(card.decision_grade_label)}")
    if card.safest_use:
        metadata_bits.append(f"最安全用途：{html.escape(card.safest_use)}")
    if not metadata_bits and card.publish_date:
        metadata_bits.append(f"发布日期：{html.escape(card.publish_date)}")

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
            <span>{html.escape(card.source_type_label)}{year_text}</span>
            {link_html}
        </div>
        {metadata_line}
    </div>
    """
    st_markdown_html(card_html)


def render_sources_section_v2(source_cards: list["SourceDisplay"]) -> None:
    """Render sources section with canonical links (v2)."""
    if not source_cards:
        return

    st.markdown(
        "<div class='vault-panel-label' style='margin-top:20px;margin-bottom:8px'>来源文献</div>",
        unsafe_allow_html=True,
    )

    # Show first 4 expanded, rest collapsed
    for card in source_cards[:4]:
        render_source_card_v2(card)

    if len(source_cards) > 4:
        with st.expander(f"查看更多 ({len(source_cards) - 4} 篇)", expanded=False):
            for card in source_cards[4:]:
                render_source_card_v2(card)


def render_next_actions_v2(actions: list) -> None:
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
            st_markdown_html(
                f"""
                <div style="padding:10px 14px;background:rgba(30,30,35,0.6);border:1px solid rgba(255,255,255,0.06);border-radius:6px;margin-bottom:8px;">
                    <span style="font-size:13px;color:#e5e7eb;">{html.escape(action.label)}</span>
                </div>
                """
            )


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
    all_source_ids = loaded_source_ids or source_ids
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
        )
        return

    source_ids = source_ids or []
    loaded_source_ids = loaded_source_ids or []

    # Build presentation
    presentation = build_presentation_from_answer(
        answer=answer,
        question=question,
        source_ids=source_ids,
        loaded_source_ids=loaded_source_ids,
        confidence=confidence,
        disease=disease,
        research_trace=research_trace,
    )

    # Render translated provenance with paper titles, never internal source IDs.
    cleaned_answer = strip_legacy_footer(answer)
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

    # Verification badge (from harness loop)
    render_verification_badge(harness_result)

    # Depth contract warning for Deep/Audit modes
    render_depth_contract_warning(harness_result)

    # Research trace (unchanged)
    render_research_trace(research_trace)

    # Expert review loop with harness results
    render_expert_review_loop(
        question=question,
        answer=answer,
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
    render_sources_section_v2(presentation.source_cards)

    # Next actions
    render_next_actions_v2(presentation.next_actions)


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


def render_research_trace(research_trace: Optional[list[dict]]) -> None:
    """Render the retrieval and synthesis path behind an answer."""
    if not research_trace:
        return

    with st.expander("Research trace", expanded=False):
        st.markdown(
            """
            <div class="vault-inline-note">
              This shows how the vault interpreted the question, searched local evidence, loaded source cards, and reached the answer. It is an audit trail, not extra evidence.
            </div>
            """,
            unsafe_allow_html=True,
        )
        for i, entry in enumerate(research_trace, 1):
            step = html.escape(str(entry.get("step", f"Step {i}")))
            detail = html.escape(str(entry.get("detail", "")))

            # Check if this is an external search step
            is_external_step = "External" in step or "PubMed" in step or "Crossref" in step
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
) -> None:
    """Render one assistant answer with provenance, copy button, confidence, figures, and sources."""
    source_ids = source_ids or []
    loaded_source_ids = loaded_source_ids or []
    cleaned_answer = strip_legacy_footer(answer)
    st.markdown(render_provenance(cleaned_answer), unsafe_allow_html=True)
    copy_button(answer, key=f"{key_prefix}-copy")
    render_trust_block(answer, confidence, source_ids, loaded_source_ids)
    render_research_trace(research_trace)
    render_expert_review_loop(
        question=question,
        answer=answer,
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
    render_example_question_chips("empty")
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


def render_setup_required(what_happened: str, technical_detail: str, extra_action_html: str = "") -> None:
    """Render expected local setup blockers without making the app look broken."""
    safe_detail = sanitize_error_detail(technical_detail)
    extra_action = f"<div style='margin-top:6px'>{extra_action_html}</div>" if extra_action_html else ""
    render_notice(
        f"""
        <div class="vault-panel-label">Setup required</div>
        <div><strong>What happened:</strong> {html.escape(what_happened)}</div>
        <div style="margin-top:8px"><strong>What to do:</strong></div>
        <div style="margin-top:6px">Check the selected backend in the sidebar, or restart the app with the required environment variables.</div>
        {extra_action}
        """,
        tone="amber",
    )
    if safe_detail:
        with st.expander("Setup details", expanded=False):
            st.code(safe_detail, language=None)


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

    .vault-trace-step {
      display: grid;
      grid-template-columns: 28px minmax(150px, 0.36fr) minmax(0, 1fr);
      gap: 10px;
      align-items: start;
      padding: 8px 0;
      border-top: 1px solid rgba(45,49,71,0.55);
      color: var(--text);
      font-size: 13px;
    }

    .vault-trace-step code {
      color: var(--muted);
      background: rgba(34,37,53,0.72);
      border: 1px solid rgba(45,49,71,0.8);
      border-radius: 4px;
      text-align: center;
    }

    .vault-trace-step strong {
      font-weight: 600;
    }

    .vault-trace-step span {
      color: var(--muted);
      overflow-wrap: anywhere;
    }

    .vault-trace-item {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      padding: 4px 0 4px 38px;
      color: var(--muted);
      font-size: 12px;
    }

    .vault-trace-item span {
      font-family: 'Geist Mono', monospace;
      color: var(--text);
    }

    .vault-trace-item em {
      color: var(--muted);
      font-style: normal;
    }

    .vault-guide-row {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-top: 8px;
      color: var(--text);
      font-size: 13px;
    }

    .vault-review-steps {
      display: grid;
      gap: 8px;
      margin: 8px 0 12px 0;
    }

    .vault-review-steps div {
      display: grid;
      grid-template-columns: 28px minmax(0, 1fr);
      gap: 8px;
      align-items: start;
      color: var(--muted);
      font-size: 13px;
      line-height: 1.55;
    }

    .vault-review-steps code {
      display: inline-flex;
      justify-content: center;
      color: var(--text);
      background: rgba(34,37,53,0.9);
      border: 1px solid rgba(45,49,71,0.8);
      border-radius: 4px;
      padding: 1px 0;
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

workspace_param = st.query_params.get("workspace", "ask")
if workspace_param == "cases":
    with st.sidebar:
        workspace = st.radio(
            "Workspace",
            ["Ask", "Research Cases", "Research Records"],
            index=1,
            horizontal=True,
            label_visibility="collapsed",
        )
        st.divider()
        st.markdown(
            """
            <div class="vault-panel">
              <div class="vault-kicker">Feline Research OS</div>
              <div style="font-size:20px;font-weight:600;color:#e8eaf0">Research Cases</div>
              <div style="font-size:13px;color:#8b90a0;margin-top:8px">
                Durable evidence work from Frame through Challenge.
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
        )
        st.divider()
        st.markdown(
            """
            <div class="vault-panel">
              <div class="vault-kicker">Feline Research OS</div>
              <div style="font-size:20px;font-weight:600;color:#e8eaf0">Research Records</div>
              <div style="font-size:13px;color:#8b90a0;margin-top:8px">
                Harness loop progress and verification history.
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
    workspace = st.radio(
        "Workspace",
        ["Ask", "Research Cases", "Research Records"],
        horizontal=True,
        label_visibility="collapsed",
    )
    if workspace == "Research Cases":
        st.query_params["workspace"] = "cases"
        st.rerun()
    elif workspace == "Research Records":
        st.query_params["workspace"] = "records"
        st.rerun()
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
        render_notice(
            "Vault Search is free and does not call an API. Switch to an API engine only when you need synthesis.",
            tone="green",
        )
    elif backend == "ollama":
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
            backend_blocker = "OPENROUTER_API_KEY is not set in this shell or Streamlit secrets."
            render_notice(
                "OPENROUTER_API_KEY not set. Switch backend or set the key in the shell or Streamlit secrets before asking.",
                tone="amber",
            )
    elif backend == "anthropic" and not os.environ.get("ANTHROPIC_API_KEY"):
        backend_blocker = "ANTHROPIC_API_KEY is not set in this shell or Streamlit secrets."
        render_notice(
            "ANTHROPIC_API_KEY not set. Switch backend or set the key in the shell or Streamlit secrets before asking.",
            tone="amber",
        )

    paid_api_confirmed = False
    if backend not in {"local", "ollama"}:
        paid_api_confirmed = st.checkbox(
            "Allow paid API synthesis for this session",
            value=False,
            help="Keep this off for simple lookup. Turn it on only when you want the model to synthesize across sources and accept token cost.",
        )
        if not paid_api_confirmed:
            render_notice(
                "Paid API synthesis is locked. Use Vault Search for free lookup, or tick the checkbox above to spend tokens intentionally.",
                tone="amber",
            )

    st.markdown("<div class='vault-panel-label'>Condition</div>", unsafe_allow_html=True)
    disease_choice = st.selectbox(
        "Condition",
        options=["Auto-detect", "CKD", "HCM", "FIP", "IBD", "Diabetes", "FCV", "Obesity", "Cancer"],
        index=0,
        help="Leave on Auto-detect to let the router determine the disease from your question.",
        label_visibility="collapsed",
    )
    disease_arg = None if disease_choice == "Auto-detect" else disease_choice.lower()

    with st.expander("Advanced settings", expanded=False):
        # Search depth mode selector (II.Inc style)
        search_depth_mode = st.radio(
            "Search depth",
            ["Auto", "Quick", "Standard", "Deep", "Audit"],
            horizontal=True,
            index=0,
            help="Auto detects depth from question type. Quick=1-2 sources. Standard=2-3 sources. Deep=gap reflection. Audit=contrary evidence required.",
        )
        search_depth_labels = {
            "Auto": None,  # Let TaskEvaluator decide
            "Quick": "quick",
            "Standard": "standard",
            "Deep": "deep",
            "Audit": "evidence_audit",
        }
        explicit_search_depth = search_depth_labels.get(search_depth_mode)

        max_hops = st.slider(
            "Agent depth",
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

        allow_external_search = st.checkbox(
            "Search PubMed/Crossref if local results sparse",
            value=False,
            help="When the vault has fewer than 3 matching sources, search external databases. External results are marked and need intake before becoming vault evidence.",
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
            draft_record = st.session_state.last_record_draft
            if draft_record is not None:
                st.markdown("**Research Record:**")
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
                        render_notice(
                            f"An equivalent record already exists: <code>{html.escape(duplicate.record_id)}</code>.",
                            tone="amber",
                        )
                if st.button(
                    "Save Research Record",
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
                        render_notice(
                            f"Research Record saved to <code>{html.escape(saved_path)}</code>.",
                            tone="green",
                        )
                        st.rerun()
                    except Exception as e:
                        render_notice(
                            f"Couldn't save Research Record: {html.escape(str(e))}",
                            tone="red",
                        )
            if st.session_state.last_record_saved_path and draft_record is not None:
                claim_candidates = extract_claim_candidates(draft_record)
                if claim_candidates:
                    st.markdown("**Claim Selection Draft:**")
                    candidate_labels = [
                        f"{claim.claim_id}: {claim.text[:120]}{'...' if len(claim.text) > 120 else ''}"
                        for claim in claim_candidates
                    ]
                    selected_claim_labels = st.multiselect(
                        "Claims to validate",
                        candidate_labels,
                        default=candidate_labels[:1] if candidate_labels else [],
                        key=f"claim-selection-{draft_record.record_id}",
                    )
                    target_choices = [
                        f"topics/{draft_record.disease or 'general'}/validated-claims.md",
                        f"system/indexes/{draft_record.disease or 'general'}-validated-claims.md",
                    ]
                    target_page = st.selectbox(
                        "Promotion target",
                        target_choices,
                        key=f"claim-target-{draft_record.record_id}",
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

                    confirm_promotion = st.checkbox(
                        "I confirm this promotion draft is ready to apply",
                        key=f"confirm-promotion-{draft_record.record_id}",
                        disabled=not draft.ready_for_patch,
                    )
                    if st.button(
                        "Apply Promotion",
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
                            render_notice(
                                f"Promotion applied for {len(written['claims'])} claim(s).",
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
                question_type=msg.get("question_type", ""),
                research_trace=msg.get("research_trace"),
                harness_result=msg.get("harness_result"),
            )
        else:
            st.markdown(msg["content"])

# ---------------------------------------------------------------------------
# Query execution
# ---------------------------------------------------------------------------

def run_query(question: str) -> bool:
    """Route, hop, synthesize, render, optionally write back."""
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
        "question": question,
        "disease": detected_disease,
        "question_type": question_type,
        "confidence": confidence,
        "figures_used": figures_used,
        "source_ids": source_ids,
        "loaded_source_ids": loaded_source_ids,
        "research_trace": research_trace,
        "harness_result": harness_result,
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
# Input
# ---------------------------------------------------------------------------

user_question = st.session_state.pending_question or st.chat_input(
    "Ask a natural feline health question...",
    accept_audio=False,
)
if user_question:
    st.session_state.pending_question = None
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)
    if run_query(user_question):
        st.rerun()
