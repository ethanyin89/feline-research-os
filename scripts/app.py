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
from expert_review import build_expert_review_prompt, expert_review_stage_label
from search import vault_search


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
        ("fip", ["fip", "传腹", "传染性腹膜炎"]),
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
        "是什么",
        "怎么理解",
        "what is",
        "explain",
        "overview",
        "summary",
        "summarize",
    ]
    if any(marker in lowered or marker in question for marker in explanation_markers):
        return True
    # Very short disease-name prompts usually mean "give me the entry point."
    compact = re.sub(r"\s+", "", lowered)
    return compact in {"ckd", "fip", "hcm", "ibd", "fcv", "diabetes", "obesity", "cancer"}


def build_ckd_local_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return a deterministic CKD starter answer from compiled vault pages."""
    source_ids = [
        "src-ckd-001",
        "src-ckd-003",
        "src-ckd-004",
        "src-ckd-010",
        "src-ckd-011",
        "src-ckd-015",
        "src-ckd-016",
    ]
    if chinese:
        answer = (
            "这是本地 vault 解释结果，不是 API 综合回答；本次没有调用 API。 [llm_inference]\n\n"
            "## 直接解释\n"
            "在这个库里，猫 CKD 可以先理解为一种以老年猫为核心场景、以肾小管间质纤维化/肾纤维化为主要机制骨架的慢性肾脏疾病。"
            "最稳的读法不是把它归因到某一个单一原因，而是把它看成多条损伤路径最后汇合到肾功能下降和结构性病变上。"
            " [source_supported_conclusion: src-ckd-010, src-ckd-011, src-ckd-016]\n\n"
            "## 对普通读者意味着什么\n"
            "- CKD 不是只看一个数字。这个库把 creatinine、USG、UPCR/蛋白尿、收缩压、phosphorus、SDMA 放在第一波 endpoint 短名单里。"
            " [source_supported_conclusion: src-ckd-002, src-ckd-004, src-ckd-010]\n"
            "- 蛋白尿、血压、磷等指标不只是“分期表格”，它们也帮助连接病理结构、预后和管理重点。"
            " [source_supported_conclusion: src-ckd-010, src-ckd-015]\n"
            "- 治疗/管理层目前最清楚的基线支持是 renal diet；其他干预需要继续区分“临床常用”和“证据很强”。"
            " [source_supported_conclusion: src-ckd-003, src-ckd-006, src-ckd-007]\n\n"
            "## 现在不能说过头的地方\n"
            "- 不能说某一个单一机制就是猫 CKD 的主导起因。 [llm_inference]\n"
            "- 不能把 SDMA、磷、蛋白尿或血压简化成单一胜负排名。这个库更支持多轴解释。"
            " [source_supported_conclusion: src-ckd-004, src-ckd-010, src-ckd-015]\n"
            "- 不能把多个治疗方向直接写成已经证明的 disease-modifying therapy。 [source_supported_conclusion: src-ckd-007]\n\n"
            "## 下一步\n"
            "如果你只是入门，下一页读 `topics/ckd/synthesis-index-bilingual.md`；如果你关心机制，读 `topics/ckd/mechanism-overview.md`；"
            "如果你关心药效评价或试验终点，读 `topics/ckd/endpoint-handbook.md`。"
        )
    else:
        answer = (
            "This is a local vault explanation, not API synthesis. No API call was made. [llm_inference]\n\n"
            "## Direct Explanation\n"
            "In this vault, feline CKD is best introduced as a chronic kidney disease of mostly older cats, with tubulointerstitial or renal fibrosis as the safest mechanism backbone. "
            "The current evidence map does not support a single dominant initiating cause; it supports a multi-axis disease frame that links structural kidney damage to declining function. "
            "[source_supported_conclusion: src-ckd-010, src-ckd-011, src-ckd-016]\n\n"
            "## What This Means\n"
            "- CKD should not be read from one number alone. The first-wave endpoint shortlist is creatinine, USG, UPCR/proteinuria, systolic blood pressure, phosphorus, and SDMA. "
            "[source_supported_conclusion: src-ckd-002, src-ckd-004, src-ckd-010]\n"
            "- Proteinuria, blood pressure, and phosphorus help connect pathology, prognosis, and management priorities. "
            "[source_supported_conclusion: src-ckd-010, src-ckd-015]\n"
            "- Renal diet is the clearest baseline-supported management branch in the current treatment layer; other interventions need explicit evidence-strength labeling. "
            "[source_supported_conclusion: src-ckd-003, src-ckd-006, src-ckd-007]\n\n"
            "## Do Not Overstate\n"
            "- Do not claim one single mechanism as the proven dominant cause. [llm_inference]\n"
            "- Do not reduce SDMA, phosphorus, proteinuria, or blood pressure into one flat ranking. The vault supports multi-axis interpretation. "
            "[source_supported_conclusion: src-ckd-004, src-ckd-010, src-ckd-015]\n"
            "- Do not turn common clinical use into strong disease-modification claims. [source_supported_conclusion: src-ckd-007]\n\n"
            "## Next Step\n"
            "For a broad entry point, read `topics/ckd/synthesis-index-bilingual.md`. For mechanism, read `topics/ckd/mechanism-overview.md`. "
            "For efficacy evaluation or trial endpoints, read `topics/ckd/endpoint-handbook.md`."
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
    """Return a deterministic FIP recognition starter answer."""
    source_ids = ["src-fip-003", "src-fip-010", "src-fip-013", "src-fip-022", "src-fip-023"]
    if chinese:
        answer = (
            "这是本地 vault 的 FIP 识别解释，不是 API 综合回答；本次没有调用 API。 [llm_inference]\n\n"
            "## 直接解释\n"
            "FIP 不能靠一个症状或一个检测直接识别。这个库把 FIP 识别放在四个层面：风险/暴露背景、临床和实验室表现、effusive 与 non-effusive 形态、以及诊断检测的边界。"
            "现代抗病毒治疗改变了可行动性，但没有消除诊断不确定性。 [source_supported_conclusion: src-fip-003, src-fip-010, src-fip-022, src-fip-023]\n\n"
            "## 普通用户要抓住的点\n"
            "- 识别 FIP 是组合判断，不是单项检测裁决。 [source_supported_conclusion: src-fip-010, src-fip-022]\n"
            "- neurologic/ocular 分支需要单独看，不能和普通 FIP 工作流混成一个答案。 [source_supported_conclusion: src-fip-022, src-fip-023]\n"
            "- GS-441524/remdesivir 时代让治疗层更有行动性，但 baseline efficacy、package logic、neurologic rescue 和 durability 不能混写。 [source_supported_conclusion: src-fip-013]\n\n"
            "## 下一步\n"
            "读 `topics/fip/risk-and-recognition.md` 和 `topics/fip/diagnostic` 相关页面；如果要问治疗，单独问 GS-441524 baseline、remdesivir package 或 neurologic rescue。"
        )
    else:
        answer = (
            "This is a local FIP recognition explanation, not API synthesis. No API call was made. [llm_inference]\n\n"
            "## Direct Answer\n"
            "FIP recognition is a composite judgment, not a one-symptom or one-test answer. The vault separates risk and exposure context, clinical and clinicopathologic recognition, effusive versus non-effusive form, and diagnostic-test limits. "
            "Modern antiviral treatment changed actionability, but it did not remove diagnostic ambiguity. [source_supported_conclusion: src-fip-003, src-fip-010, src-fip-022, src-fip-023]\n\n"
            "## What To Watch\n"
            "- Treat FIP diagnosis as integrated evidence, not a single assay verdict. [source_supported_conclusion: src-fip-010, src-fip-022]\n"
            "- Neurologic or ocular extension is its own branch. [source_supported_conclusion: src-fip-022, src-fip-023]\n"
            "- GS-441524/remdesivir-era evidence should stay separated into baseline efficacy, package logic, neurologic rescue, and durability. [source_supported_conclusion: src-fip-013]\n\n"
            "## Next Step\n"
            "Read `topics/fip/risk-and-recognition.md`; for treatment, ask separately about baseline GS-441524, remdesivir package logic, or neurologic rescue."
        )
    return answer, source_ids


def build_hcm_local_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return a deterministic HCM starter answer."""
    source_ids = ["src-hcm-001", "src-hcm-008", "src-hcm-009", "src-hcm-010", "src-hcm-013", "src-hcm-024"]
    if chinese:
        answer = (
            "这是本地 vault 的 HCM 解释，不是 API 综合回答；本次没有调用 API。 [llm_inference]\n\n"
            "## 直接解释\n"
            "猫 HCM 在这个库里首先是结构性心肌表型问题，而不是单一 biomarker 问题。当前最稳的入口是 phenotype definition、echocardiography/gross morphometry、genotype pressure、remodeling depth 和治疗不确定性分层。"
            " [source_supported_conclusion: src-hcm-001, src-hcm-009, src-hcm-010, src-hcm-013, src-hcm-024]\n\n"
            "## 为什么危险\n"
            "- HCM 不能只理解成“左心室变厚”，remodeling、严重程度和 end-stage phenotype 都会影响解释。 [source_supported_conclusion: src-hcm-001, src-hcm-024]\n"
            "- biomarkers 和 AI 可以辅助筛查或分层，但不应替代结构表型权重。 [source_supported_conclusion: src-hcm-009, src-hcm-010, src-hcm-013]\n"
            "- 治疗证据真实存在，但很容易被说过头；当前库不支持把它写成最终 intervention hierarchy。 [source_supported_conclusion: src-hcm-008]\n\n"
            "## 下一步\n"
            "读 `topics/hcm/synthesis-index.md`；如果关心风险，继续看 HCM diagnostic-workup、endpoint separation 和 treatment evidence memos。"
        )
    else:
        answer = (
            "This is a local HCM explanation, not API synthesis. No API call was made. [llm_inference]\n\n"
            "## Direct Answer\n"
            "In this vault, feline HCM starts as a structural myocardial phenotype problem, not a biomarker-only problem. The stable entry points are phenotype definition, echocardiography/gross morphometry, genotype pressure, remodeling depth, and treatment uncertainty. "
            "[source_supported_conclusion: src-hcm-001, src-hcm-009, src-hcm-010, src-hcm-013, src-hcm-024]\n\n"
            "## Why It Is Risky\n"
            "- HCM should not be reduced to simple left-ventricular thickening; remodeling and end-stage phenotype change interpretation. [source_supported_conclusion: src-hcm-001, src-hcm-024]\n"
            "- Biomarkers and AI can augment screening or severity reading, but should not outrank structural phenotype authority. [source_supported_conclusion: src-hcm-009, src-hcm-010, src-hcm-013]\n"
            "- Treatment evidence is real but overclaim-sensitive and not a final intervention hierarchy. [source_supported_conclusion: src-hcm-008]\n\n"
            "## Next Step\n"
            "Read `topics/hcm/synthesis-index.md`; then use the diagnostic-workup, endpoint-separation, and treatment-evidence memos for narrower questions."
        )
    return answer, source_ids


def build_ibd_lymphoma_explanation(chinese: bool) -> tuple[str, list[str]]:
    """Return a deterministic IBD-versus-lymphoma starter answer."""
    source_ids = ["src-ibd-003", "src-ibd-010", "src-ibd-011", "src-ibd-015", "src-ibd-016", "src-ibd-019"]
    if chinese:
        answer = (
            "这是本地 vault 的 IBD/淋巴瘤鉴别解释，不是 API 综合回答；本次没有调用 API。 [llm_inference]\n\n"
            "## 直接解释\n"
            "猫 IBD 与小细胞/低级别 alimentary lymphoma 的区分，不应该被写成一个单项 marker 问题。这个库把它当作 diagnostic boundary 和 workup sequencing 问题：慢性肠病怀疑、影像压力、活检部位策略、整合病理，再到有限 marker 支持。"
            " [source_supported_conclusion: src-ibd-003, src-ibd-010, src-ibd-011, src-ibd-015, src-ibd-016, src-ibd-019]\n\n"
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
            "## Key Boundaries\n"
            "- Muscularis thickening is lymphoma-leaning, and ileal sampling can change diagnosis, so sampling strategy matters. [source_supported_conclusion: src-ibd-010, src-ibd-011]\n"
            "- Bcl-2 is stronger than shared COX-2 signal, but still not a standalone separator. [source_supported_conclusion: src-ibd-015, src-ibd-016]\n"
            "- Diet-first logic belongs inside chronic-enteropathy and food-response boundaries; it is not pure idiopathic-IBD proof. [source_supported_conclusion: src-ibd-014, src-ibd-021]\n\n"
            "## Next Step\n"
            "Read `topics/ibd/synthesis-index.md` plus the diagnostic-workup and boundary memos. Do not let one marker, image, biopsy note, or treatment response become the whole answer."
        )
    return answer, source_ids


def choose_local_explanation_surface(question: str, disease: str) -> Optional[str]:
    """Pick a deterministic ordinary-user answer surface for free mode."""
    lowered = question.lower()
    if disease == "ckd" and any(term in lowered for term in ["endpoint", "efficacy", "trial", "outcome"]):
        return "ckd_endpoint"
    if disease == "ckd" and is_local_explanation_question(question):
        return "ckd_overview"
    if disease == "fip" and any(term in lowered or term in question for term in ["recogn", "diagnos", "识别", "诊断", "怎么看"]):
        return "fip_recognition"
    if disease == "hcm" and is_local_explanation_question(question):
        return "hcm_overview"
    if disease == "ibd" and any(term in lowered or term in question for term in ["lymphoma", "淋巴瘤", "区分", "differentiat"]):
        return "ibd_lymphoma"
    return None


def build_local_explanation(surface: str, chinese: bool) -> tuple[str, list[str]]:
    """Build a no-API explanation for supported high-visibility surfaces."""
    builders = {
        "ckd_overview": build_ckd_local_explanation,
        "ckd_endpoint": build_ckd_endpoint_explanation,
        "fip_recognition": build_fip_recognition_explanation,
        "hcm_overview": build_hcm_local_explanation,
        "ibd_lymphoma": build_ibd_lymphoma_explanation,
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
        {
            "step": "Returned local answer",
            "detail": f"mode={'local_explanation' if explanation_surface else 'free_retrieval'}; surface={explanation_surface or 'none'}; api_calls=0; results={len(selected_results)}",
        },
    ]

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
) -> None:
    """Expose the manual expert-review loop for one rendered answer."""
    prompt = build_expert_review_prompt(
        question=question,
        answer=answer,
        disease=disease,
        question_type=question_type,
        confidence=confidence,
        source_ids=source_ids,
    )
    stage = expert_review_stage_label()

    with st.expander("Expert review loop", expanded=False):
        st.markdown(
            f"""
            <div class="vault-inline-note">
              This is a reusable manual review loop: answer → domain expert critique → claim-level write-back decision.
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
            st.markdown(
                f"<div class='vault-trace-step'><code>{i}</code><strong>{step}</strong><span>{detail}</span></div>",
                unsafe_allow_html=True,
            )
            items = entry.get("items") or []
            if items:
                rows: list[str] = []
                for item in items[:8]:
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
                question=msg.get("question", ""),
                disease=msg.get("disease", ""),
                question_type=msg.get("question_type", ""),
                research_trace=msg.get("research_trace"),
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

    status_label = "Searching local vault..." if backend == "local" else "Routing question..."
    with st.status(status_label, expanded=False) as status:
        try:
            if backend == "local":
                result = run_app_local_query_core(
                    question, VAULT_ROOT, source_index,
                    disease_hint=disease_arg,
                    preferred_source_ids=st.session_state.preferred_source_ids or None,
                    search_limit=8,
                    on_status=lambda msg: status.update(label=msg, expanded=False),
                )
            else:
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
        research_trace = result.get("research_trace", [])
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
            question=question,
            disease=detected_disease,
            question_type=question_type,
            research_trace=research_trace,
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
