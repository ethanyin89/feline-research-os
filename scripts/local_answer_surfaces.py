"""Deterministic local answer surfaces for no-API public testing.

These helpers expose compiled topic pages as answer-shaped responses without
importing the Streamlit app module.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Optional

from query import parse_source_ids_from_frontmatter
from source_inventory import format_source_inventory, get_source_inventory

VAULT_ROOT = Path(__file__).parent.parent


def _contains_chinese(text: str) -> bool:
    return bool(re.search(r"[\u3400-\u9fff]", text))


def is_researcher_overview_question(question: str) -> bool:
    """Detect prompts that ask for a research-map style overview."""
    lowered = question.lower()
    markers = [
        "current understanding",
        "researcher know",
        "researchers know",
        "researcher overview",
        "research map",
        "evidence map",
        "what should a researcher know",
        "what should researchers know",
        "研究者应该知道",
        "研究者该知道",
        "研究者视图",
        "研究地图",
        "证据地图",
        "当前理解",
        "当前认识",
    ]
    return any(marker in lowered or marker in question for marker in markers)


def _infer_disease(question: str, disease_hint: Optional[str]) -> str:
    if disease_hint:
        return disease_hint
    lowered = question.lower()
    if any(term in lowered or term in question for term in ["fip", "传腹", "传染性腹膜炎", "gs-441524", "gs441524", "remdesivir"]):
        return "fip"
    if any(term in lowered or term in question for term in ["ckd", "kidney", "renal", "肾", "慢性肾"]):
        return "ckd"
    if any(term in lowered or term in question for term in ["diabetes", "diabetic", "糖尿病", "血糖", "胰岛素"]):
        return "diabetes"
    if any(term in lowered or term in question for term in ["obesity", "obese", "肥胖", "超重", "胰岛素抵抗"]):
        return "obesity"
    if any(term in lowered or term in question for term in ["cancer", "tumor", "tumour", "肿瘤", "癌"]):
        return "cancer"
    return "unknown"


def is_endpoint_matrix_question(question: str) -> bool:
    """Detect prompts that ask for structured endpoint/indicator matrix."""
    lowered = question.lower()
    markers = [
        "评价指标",
        "关键指标",
        "指标矩阵",
        "药效指标",
        "药效终点",
        "endpoint matrix",
        "key indicators",
        "efficacy endpoints",
        "model endpoints",
        "提炼.*指标",
        "模型.*指标",
    ]
    return any(marker in lowered or marker in question for marker in markers)


def _section(markdown: str, heading: str) -> str:
    pattern = re.compile(
        rf"(^## {re.escape(heading)}\n.*?)(?=^## |\Z)",
        re.M | re.S,
    )
    match = pattern.search(markdown)
    return match.group(1).strip() if match else ""


def _read_topic(vault_root: Path, rel_path: str) -> tuple[str, list[str]]:
    text = (vault_root / rel_path).read_text(encoding="utf-8")
    return text, parse_source_ids_from_frontmatter(text)


def _fip_endpoint(vault_root: Path, chinese: bool) -> tuple[str, list[str]]:
    text, source_ids = _read_topic(vault_root, "topics/fip/endpoint-handbook.md")
    key_claims = _section(text, "Key-Claim Traceability")
    hierarchy = _section(text, "Endpoint Hierarchy")
    takeaway = _section(text, "Core Takeaway")
    cited = ", ".join(source_ids[:6])
    inventory = format_source_inventory(get_source_inventory(vault_root, "fip"), chinese)
    if chinese:
        answer = (
            f"**{inventory}**\n\n"
            "这是本地 vault 的 FIP 药效评价/endpoint 结构化回答；本次没有调用 API。 "
            f"[source_supported_conclusion: {cited}]\n\n"
            f"{key_claims}\n\n{takeaway}\n\n{hierarchy}\n\n"
            "## 如何验证\n"
            "- 完整页面：`topics/fip/endpoint-handbook.md`\n"
            "- Source cards：打开 `raw/papers/src-fip-XXX.md`\n"
            "- 关键边界：不要把 FIP endpoint 写成单一 assay 排名或单一 marker 确诊。 [llm_inference]"
        )
    else:
        answer = (
            f"**{inventory}**\n\n"
            "This is a local vault structured answer for FIP endpoint/evaluation queries. No API call was made. "
            f"[source_supported_conclusion: {cited}]\n\n"
            f"{key_claims}\n\n{takeaway}\n\n{hierarchy}\n\n"
            "## How to Verify\n"
            "- Full page: `topics/fip/endpoint-handbook.md`\n"
            "- Source cards: open `raw/papers/src-fip-XXX.md`\n"
            "- Boundary: do not turn FIP endpoints into a single assay ranking or one-marker diagnosis. [llm_inference]"
        )
    return answer, source_ids


def _fip_treatment(vault_root: Path, chinese: bool) -> tuple[str, list[str]]:
    text, source_ids = _read_topic(vault_root, "topics/fip/translation-brief.md")
    key_claims = _section(text, "Key-Claim Traceability")
    safe_reading = _section(text, "Current Safe Reading")
    evidence_map = _section(text, "Evidence Map")
    uncertainty = _section(text, "Conflicts / Uncertainty")
    cited = ", ".join(source_ids[:5])
    inventory = format_source_inventory(get_source_inventory(vault_root, "fip"), chinese)
    if chinese:
        answer = (
            f"**{inventory}**\n\n"
            "这是本地 vault 的 FIP 治疗证据结构化回答；本次没有调用 API。 "
            f"[source_supported_conclusion: {cited}]\n\n"
            f"{key_claims}\n\n{safe_reading}\n\n{evidence_map}\n\n{uncertainty}\n\n"
            "## 如何验证\n"
            "- 完整页面：`topics/fip/translation-brief.md`\n"
            "- 基线治疗锚点：`raw/papers/src-fip-016.md`\n"
            "- 神经型/复杂治疗分支：`raw/papers/src-fip-017.md`, `raw/papers/src-fip-024.md`"
        )
    else:
        answer = (
            f"**{inventory}**\n\n"
            "This is a local vault structured answer for FIP treatment evidence. No API call was made. "
            f"[source_supported_conclusion: {cited}]\n\n"
            f"{key_claims}\n\n{safe_reading}\n\n{evidence_map}\n\n{uncertainty}\n\n"
            "## How to Verify\n"
            "- Full page: `topics/fip/translation-brief.md`\n"
            "- Baseline treatment anchor: `raw/papers/src-fip-016.md`\n"
            "- Neurologic/complex treatment branch: `raw/papers/src-fip-017.md`, `raw/papers/src-fip-024.md`"
        )
    return answer, source_ids


def _fip_recognition(vault_root: Path, chinese: bool) -> tuple[str, list[str]]:
    text, source_ids = _read_topic(vault_root, "topics/fip/fip-warning-signs.md")
    body = re.sub(r"\A---.*?---\s*", "", text, flags=re.S).strip()
    cited = ", ".join(source_ids)
    inventory = format_source_inventory(get_source_inventory(vault_root, "fip"), chinese)
    prefix = (
        f"**{inventory}**\n\n"
        f"这是本地 vault 的 FIP 识别/警示信号解释；本次没有调用 API。 [source_supported_conclusion: {cited}]\n\n"
        if chinese
        else f"**{inventory}**\n\n"
        f"This is a local vault FIP recognition and warning-signs answer. No API call was made. [source_supported_conclusion: {cited}]\n\n"
    )
    return prefix + body, source_ids


def _ckd_researcher_overview(vault_root: Path, chinese: bool) -> tuple[str, list[str]]:
    """Return a CKD researcher-map overview for broad research prompts."""
    mech_text, mech_sources = _read_topic(vault_root, "topics/ckd/mechanism-overview.md")
    endpoint_text, endpoint_sources = _read_topic(vault_root, "topics/ckd/endpoint-handbook.md")
    translation_text, translation_sources = _read_topic(vault_root, "topics/ckd/translation-brief.md")
    dashboard_text, dashboard_sources = _read_topic(vault_root, "topics/ckd/current-state-dashboard.md")

    source_ids: list[str] = []
    for sid in mech_sources + endpoint_sources + translation_sources + dashboard_sources:
        if sid not in source_ids:
            source_ids.append(sid)

    _ = (mech_text, endpoint_text, translation_text, dashboard_text)
    backbone_ids = ["src-ckd-001", "src-ckd-004", "src-ckd-010", "src-ckd-011", "src-ckd-013", "src-ckd-015", "src-ckd-016", "src-ckd-024"]
    cited_backbone = ", ".join(backbone_ids[:6])

    if chinese:
        answer = (
            "这是本地 vault 的 CKD 研究者视图，不是 API 综合回答；本次没有调用 API。 [llm_inference]\n\n"
            "## 一句话定位\n"
            "猫 CKD 是一个老年、纤维化主导、以多轴 endpoint 解释为主的疾病；在这个 vault 里，真正有用的读法不是只问“是什么”，而是问“哪条证据能支持哪种决策”。 "
            f"[source_supported_conclusion: {cited_backbone}]\n\n"
            "## Researcher Map\n"
            "- 疾病模型：纤维化是最稳的病理骨架，年龄相关自然史和病理-结局桥接比单一病因更可靠。 [source_supported_conclusion: src-ckd-001, src-ckd-010, src-ckd-011, src-ckd-016]\n"
            "- 识别与工作up：creatinine、USG、UPCR、SBP、phosphorus、SDMA 各自承担不同角色，不是一个分数能概括。 [source_supported_conclusion: src-ckd-004, src-ckd-010, src-ckd-024]\n"
            "- Endpoint 架构：运营性 endpoint 和试验性 endpoint 不要混成一个层级。 [source_supported_conclusion: src-ckd-013, src-ckd-015]\n"
            "- 治疗/转化：真正强的依然是 renal diet 和 phosphorus-control 这一层，其他分支更多是 bounded management。 [source_supported_conclusion: src-ckd-003, src-ckd-006, src-ckd-007]\n"
            "- 弱层：早期检测、疾病修饰、真正的干预模型密度仍然有限。 [llm_inference]\n\n"
            "## Evidence Backbone\n"
            "| Anchor | Role | What it supports | Boundary |\n"
            "|---|---|---|---|\n"
            "| src-ckd-011 | 纤维化机制骨架 | fibrosis-centered disease model | 机制框架，不是唯一病因 |\n"
            "| src-ckd-010 | 病理-指标桥接 | proteinuria, blood pressure, phosphorus are structural signals | bridge variables, not a flat score |\n"
            "| src-ckd-004 | 诊断/分期指南 | operational workup and surveillance | clinical workflow, not cure claim |\n"
            "| src-ckd-013 | 核心结局集 | trial breadth and owner-visible outcomes | trial architecture, not everyday ranking |\n"
            "| src-ckd-024 | biomarker review | SDMA as adjunctive early-detection support | adjunct, not standalone screen |\n\n"
            "## Key-Claim Traceability\n"
            "| ID | Claim | Level | Sources | Boundary |\n"
            "|---|---|---|---|---|\n"
            "| CM1 | Tubulointerstitial fibrosis 是 feline CKD 最稳的机制骨架 | B | src-ckd-001, src-ckd-010, src-ckd-011, src-ckd-016 | lesion-backbone，不是单一 initiating cause |\n"
            "| CM3 | Proteinuria、phosphorus、blood pressure 是结构性桥接变量 | B | src-ckd-010, src-ckd-015 | mechanism-endpoint bridge，不是单一 severity score |\n"
            "| CM4 | CKD-MBD 比 phosphorus 更宽，包含 calcium/PTH/FGF23 | B | src-ckd-015 | mineral-disorder frame，不是闭合 marker list |\n"
            "| CM6 | senescence 和 telomere shortening 是真实的 kidney-specific finding | C | src-ckd-023 | mechanism-enrichment，不是 primary driver claim |\n\n"
            "## What Not To Overstate\n"
            "- 不要把单一 initiating cause 写成已经证明的主因。\n"
            "- 不要把 SDMA 写成单独筛查替代物。\n"
            "- 不要把常见管理措施直接写成 disease modification。\n"
            "- 不要把 endpoint 列表压成一个 flat severity score。\n\n"
            "## Verification Path\n"
            "- `topics/ckd/mechanism-overview.md`\n"
            "- `topics/ckd/endpoint-handbook.md`\n"
            "- `topics/ckd/translation-brief.md`\n"
            "- `topics/ckd/current-state-dashboard.md`\n\n"
            "## Next Research Move\n"
            "如果你要继续做机制，读 mechanism overview；如果要做试验设计，读 endpoint handbook；如果要继续核查主张，把相关材料加入 Research Case 的候选证据区，由人工完成判断。"
        )
    else:
        answer = (
            "This is a local vault CKD researcher overview, not API synthesis. No API call was made. [llm_inference]\n\n"
            "## One-Paragraph Orientation\n"
            "Feline CKD is a geriatric, fibrosis-centered disease with multi-axis endpoint logic. In this vault, the useful reading is not just what CKD is, but which evidence supports which decision. "
            f"[source_supported_conclusion: {cited_backbone}]\n\n"
            "## Researcher Map\n"
            "- Disease model: fibrosis is the stable lesion backbone; age-related natural history and pathology-to-outcome bridges are more reliable than a single cause story. [source_supported_conclusion: src-ckd-001, src-ckd-010, src-ckd-011, src-ckd-016]\n"
            "- Recognition / workup: creatinine, USG, UPCR, SBP, phosphorus, and SDMA each do different jobs. [source_supported_conclusion: src-ckd-004, src-ckd-010, src-ckd-024]\n"
            "- Endpoint architecture: operational endpoints and trial endpoints should not be collapsed into one layer. [source_supported_conclusion: src-ckd-013, src-ckd-015]\n"
            "- Treatment / translation: renal diet and phosphorus control remain the strongest base layer; other branches stay bounded management questions. [source_supported_conclusion: src-ckd-003, src-ckd-006, src-ckd-007]\n"
            "- Weak layers: early detection, disease modification, and true intervention-model density are still limited. [llm_inference]\n\n"
            "## Evidence Backbone\n"
            "| Anchor | Role | What it supports | Boundary |\n"
            "|---|---|---|---|\n"
            "| src-ckd-011 | fibrosis mechanism backbone | fibrosis-centered disease model | mechanism frame, not the only cause |\n"
            "| src-ckd-010 | pathology-marker bridge | proteinuria, blood pressure, phosphorus as structural signals | bridge variables, not a flat score |\n"
            "| src-ckd-004 | diagnosis/staging guideline | operational workup and surveillance | clinical workflow, not a cure claim |\n"
            "| src-ckd-013 | core outcome set | trial breadth and owner-visible outcomes | trial architecture, not routine ranking |\n"
            "| src-ckd-024 | biomarker review | SDMA as adjunctive early-detection support | adjunct, not a standalone screen |\n\n"
            "## Key-Claim Traceability\n"
            "| ID | Claim | Level | Sources | Boundary |\n"
            "|---|---|---|---|---|\n"
            "| CM1 | Tubulointerstitial fibrosis is the most stable mechanism backbone for feline CKD | B | src-ckd-001, src-ckd-010, src-ckd-011, src-ckd-016 | lesion-backbone, not a single initiating cause |\n"
            "| CM3 | Proteinuria, phosphorus, and blood pressure are structural bridge variables | B | src-ckd-010, src-ckd-015 | mechanism-endpoint bridge, not a flat severity score |\n"
            "| CM4 | CKD-MBD is broader than phosphorus alone and includes calcium, PTH, and FGF23 | B | src-ckd-015 | mineral-disorder frame, not a closed marker list |\n"
            "| CM6 | Senescence and telomere shortening are real kidney-specific findings | C | src-ckd-023 | mechanism-enrichment, not a primary driver claim |\n\n"
            "## What Not To Overstate\n"
            "- Do not present a single initiating cause as proven.\n"
            "- Do not turn SDMA into a standalone screening replacement.\n"
            "- Do not write common management as disease modification.\n"
            "- Do not compress all endpoints into one flat severity score.\n\n"
            "## Verification Path\n"
            "- `topics/ckd/mechanism-overview.md`\n"
            "- `topics/ckd/endpoint-handbook.md`\n"
            "- `topics/ckd/translation-brief.md`\n"
            "- `topics/ckd/current-state-dashboard.md`\n\n"
            "## Next Research Move\n"
            "If you want mechanism, read mechanism overview. If you want trial design, read endpoint handbook. To investigate a claim, add the relevant material to a Research Case as candidate evidence for human review."
        )
    return answer, source_ids


def build_ckd_researcher_overview(chinese: bool) -> tuple[str, list[str]]:
    """Public app builder using the repository's default vault root."""
    return _ckd_researcher_overview(VAULT_ROOT, chinese)


def _ckd_topic_index(vault_root: Path, chinese: bool) -> tuple[str, list[str]]:
    """Return the CKD topic index contents with a clean local prefix."""
    rel_path = "topics/ckd/index-bilingual.md" if chinese else "topics/ckd/index.md"
    if not (vault_root / rel_path).exists():
        rel_path = "topics/ckd/index.md"
    text, source_ids = _read_topic(vault_root, rel_path)
    body = re.sub(r"\A---.*?---\s*", "", text, flags=re.S).strip()
    cited = ", ".join(source_ids[:6])
    inventory = format_source_inventory(get_source_inventory(vault_root, "ckd"), chinese)
    if chinese:
        prefix = (
            f"**{inventory}**\n\n"
            f"这是本地 vault 的 CKD 主题索引；本次没有调用 API。 [source_supported_conclusion: {cited}]\n\n"
        )
    else:
        prefix = (
            f"**{inventory}**\n\n"
            f"This is a local vault CKD topic index. No API call was made. [source_supported_conclusion: {cited}]\n\n"
        )
    return prefix + body, source_ids


def build_ckd_topic_index(chinese: bool) -> tuple[str, list[str]]:
    """Public app builder for the CKD topic index surface."""
    return _ckd_topic_index(VAULT_ROOT, chinese)


# ---------------------------------------------------------------------------
# Gold Standard endpoint snippets — structured matrix-first answers
# ---------------------------------------------------------------------------

GOLD_STANDARD_TOPICS = {
    "diabetes_model_endpoints": {
        "disease": "diabetes",
        "keywords": ["糖尿病模型", "糖尿病.*指标", "diabetes model", "diabetes.*endpoint"],
        "snippet_path": "outputs/gold_standards/diabetes_model_endpoints/endpoint_snippet.md",
        "full_path": "outputs/gold_standards/diabetes_model_endpoints/research_workspace_gold.md",
        "source_ids": ["src-diabetes-001", "src-diabetes-002", "src-diabetes-003", "src-diabetes-004",
                       "src-diabetes-005", "src-diabetes-008", "src-diabetes-009", "src-diabetes-010"],
    },
    "diabetes_treatment_remission": {
        "disease": "diabetes",
        "keywords": ["糖尿病治疗", "糖尿病缓解", "diabetes treatment", "diabetes remission", "胰岛素", "SGLT2"],
        "snippet_path": "outputs/gold_standards/diabetes_treatment_remission/endpoint_snippet.md",
        "full_path": "outputs/gold_standards/diabetes_treatment_remission/research_workspace_gold.md",
        "source_ids": ["src-diabetes-006", "src-diabetes-007", "src-diabetes-011", "src-diabetes-015",
                       "src-diabetes-016", "src-diabetes-017", "src-diabetes-021", "src-diabetes-022", "src-diabetes-024"],
    },
    "obesity_insulin_resistance": {
        "disease": "obesity",
        "keywords": ["肥胖.*指标", "肥胖模型", "肥胖.*终点", "胰岛素抵抗.*指标", "obesity.*endpoint", "obesity model", "insulin resistance.*endpoint", "GLUT-4", "代谢综合征", "肥胖猫.*评价"],
        "snippet_path": "outputs/gold_standards/obesity_insulin_resistance/endpoint_snippet.md",
        "full_path": "outputs/gold_standards/obesity_insulin_resistance/research_workspace_gold.md",
        "source_ids": ["src-obesity-005", "src-obesity-015", "src-obesity-016", "src-obesity-020",
                       "src-obesity-022", "src-obesity-025", "src-obesity-030", "src-obesity-055", "src-obesity-080", "src-obesity-095"],
    },
}


def _match_gold_standard_topic(question: str) -> Optional[str]:
    """Match a question to a gold_standard topic by keywords."""
    lowered = question.lower()
    for topic_id, config in GOLD_STANDARD_TOPICS.items():
        for keyword in config["keywords"]:
            if re.search(keyword, lowered) or re.search(keyword, question):
                return topic_id
    return None


def _gold_standard_endpoint_snippet(vault_root: Path, topic_id: str, chinese: bool) -> tuple[str, list[str]]:
    """Return structured endpoint matrix + full research workspace content.

    Structure:
    1. Compressed snippet (endpoint matrix) - first and prominent
    2. Full research workspace content (inline, not file path)
    3. NO Phase 2/3 deep extracts (those are internal assets in raw/deep-extractions/)
    """
    config = GOLD_STANDARD_TOPICS[topic_id]
    snippet_path = vault_root / config["snippet_path"]
    full_path = vault_root / config["full_path"]
    source_ids = config["source_ids"]

    # Read compressed snippet
    if snippet_path.exists():
        snippet = snippet_path.read_text(encoding="utf-8")
    else:
        snippet = "指标矩阵文件尚未生成。" if chinese else "Endpoint matrix file not yet generated."

    # Read full research workspace content
    full_content = ""
    if full_path.exists():
        full_content = full_path.read_text(encoding="utf-8")

    cited = ", ".join(source_ids[:6])
    disease = config["disease"]
    inventory = get_source_inventory(vault_root, disease)
    inv_str = format_source_inventory(inventory, chinese)

    # Topic display names
    topic_names = {
        "diabetes_model_endpoints": ("糖尿病模型评价指标", "Diabetes Model Endpoints"),
        "diabetes_treatment_remission": ("糖尿病治疗/缓解指标", "Diabetes Treatment/Remission"),
        "obesity_insulin_resistance": ("肥胖/胰岛素抵抗指标", "Obesity/Insulin Resistance"),
    }
    topic_zh, topic_en = topic_names.get(topic_id, (topic_id, topic_id))

    if chinese:
        answer = (
            f"**{inv_str}**\n\n"
            f"## {topic_zh}\n\n"
            f"[source_supported_conclusion: {cited}]\n\n"
            f"{snippet}\n\n"
        )
        if full_content:
            answer += (
                "---\n\n"
                "## 完整研究报告\n\n"
                f"{full_content}"
            )
    else:
        answer = (
            f"**{inv_str}**\n\n"
            f"## {topic_en}\n\n"
            f"[source_supported_conclusion: {cited}]\n\n"
            f"{snippet}\n\n"
        )
        if full_content:
            answer += (
                "---\n\n"
                "## Full Research Report\n\n"
                f"{full_content}"
            )
    return answer, source_ids


def build_gold_standard_topic_answer(
    topic_id: str,
    chinese: bool,
    vault_root: Path = VAULT_ROOT,
) -> tuple[str, list[str]]:
    """Build a gold-standard answer for an already matched topic id."""
    if topic_id not in GOLD_STANDARD_TOPICS:
        raise KeyError(f"unknown gold_standard topic: {topic_id}")
    return _gold_standard_endpoint_snippet(vault_root, topic_id, chinese)


def build_gold_standard_endpoint_answer(
    question: str,
    chinese: bool,
    vault_root: Path = VAULT_ROOT,
) -> Optional[tuple[str, list[str], str]]:
    """Build an endpoint matrix answer from gold_standards if matched.

    Returns:
        Tuple of (answer, source_ids, topic_id) or None if no match.
    """
    topic_id = _match_gold_standard_topic(question)
    if not topic_id:
        return None
    answer, source_ids = build_gold_standard_topic_answer(topic_id, chinese, vault_root)
    return answer, source_ids, topic_id


def _what_is(vault_root: Path, disease: str, chinese: bool) -> Optional[tuple[str, list[str]]]:
    rel_paths = {
        "fip": "topics/fip/what-is-fip.md",
        "ckd": "topics/ckd/what-is-ckd.md",
        "obesity": "topics/obesity/what-is-obesity.md",
        "cancer": "topics/cancer/what-is-cancer.md",
    }
    rel_path = rel_paths.get(disease)
    if not rel_path or not (vault_root / rel_path).exists():
        return None
    text, source_ids = _read_topic(vault_root, rel_path)
    body = re.sub(r"\A---.*?---\s*", "", text, flags=re.S).strip()
    cited = ", ".join(source_ids[:4])
    inventory = format_source_inventory(get_source_inventory(vault_root, disease), chinese)
    prefix = (
        f"**{inventory}**\n\n"
        f"这是本地 vault 的基础解释；本次没有调用 API。 [source_supported_conclusion: {cited}]\n\n"
        if chinese
        else f"**{inventory}**\n\n"
        f"This is a local vault plain-language explanation. No API call was made. [source_supported_conclusion: {cited}]\n\n"
    )
    return prefix + body, source_ids


def build_local_surface_answer(
    question: str,
    vault_root: Path,
    disease_hint: Optional[str] = None,
) -> Optional[dict]:
    """Return a deterministic surface result when the question matches one."""
    chinese = _contains_chinese(question)
    disease = _infer_disease(question, disease_hint)
    lowered = question.lower()

    # Priority 1: Gold standard endpoint matrix answers (structured matrix-first)
    if is_endpoint_matrix_question(question):
        result = build_gold_standard_endpoint_answer(question, chinese, vault_root)
        if result:
            answer, source_ids, topic_id = result
            config = GOLD_STANDARD_TOPICS[topic_id]
            inventory = get_source_inventory(vault_root, config["disease"])
            return {
                "answer": answer,
                "figures_used": [],
                "disease": config["disease"],
                "question_type": "endpoint_matrix",
                "answer_mode": "gold_standard_snippet",
                "hops_used": 0,
                "loaded_paths": set(),
                "loaded_source_ids": source_ids,
                "first_family_loaded": f"gold_standard_{topic_id}",
                "disease_maturity": "gold_standard",
                "disease_sources": inventory["total"],
                "disease_extraction": inventory["verification_status"],
                "research_trace": [
                    {
                        "step": "Matched gold_standard endpoint snippet",
                        "detail": f"topic={topic_id}; api_calls=0; source_ids={len(source_ids)}",
                    }
                ],
                "est_tokens": 0,
            }

    # Priority 2: Also check for gold standard match without explicit endpoint keywords
    topic_id = _match_gold_standard_topic(question)
    if topic_id:
        answer, source_ids = build_gold_standard_topic_answer(topic_id, chinese, vault_root)
        config = GOLD_STANDARD_TOPICS[topic_id]
        inventory = get_source_inventory(vault_root, config["disease"])
        return {
            "answer": answer,
            "figures_used": [],
            "disease": config["disease"],
            "question_type": "endpoint_matrix",
            "answer_mode": "gold_standard_snippet",
            "hops_used": 0,
            "loaded_paths": set(),
            "loaded_source_ids": source_ids,
            "first_family_loaded": f"gold_standard_{topic_id}",
            "disease_maturity": "gold_standard",
            "disease_sources": inventory["total"],
            "disease_extraction": inventory["verification_status"],
            "research_trace": [
                {
                    "step": "Matched gold_standard topic",
                    "detail": f"topic={topic_id}; api_calls=0; source_ids={len(source_ids)}",
                }
            ],
            "est_tokens": 0,
        }

    if disease == "ckd" and is_researcher_overview_question(question):
        answer, source_ids = _ckd_researcher_overview(vault_root, chinese)
        question_type = "overview"
        surface = "ckd_researcher_overview"
    elif disease == "ckd" and any(term in lowered or term in question for term in ["topic index", "主题索引", "index page"]):
        answer, source_ids = _ckd_topic_index(vault_root, chinese)
        question_type = "overview"
        surface = "ckd_topic_index"
    elif disease == "fip" and any(term in lowered or term in question for term in ["治疗证据", "疗效证据", "treatment evidence", "gs-441524", "remdesivir", "抗病毒"]):
        answer, source_ids = _fip_treatment(vault_root, chinese)
        question_type = "treatment"
        surface = "fip_treatment_evidence"
    elif disease == "fip" and any(term in lowered or term in question for term in ["endpoint", "efficacy", "trial", "outcome", "评价", "指标", "药效", "疗效评价", "评估", "判断疗效"]):
        answer, source_ids = _fip_endpoint(vault_root, chinese)
        question_type = "endpoints"
        surface = "fip_endpoint"
    elif disease == "fip" and any(term in lowered or term in question for term in ["recogn", "diagnos", "识别", "诊断", "怎么看", "警示", "症状"]):
        answer, source_ids = _fip_recognition(vault_root, chinese)
        question_type = "recognition"
        surface = "fip_recognition"
    elif any(term in lowered or term in question for term in ["什么是", "是什么", "解释", "what is", "explain", "overview"]):
        built = _what_is(vault_root, disease, chinese)
        if not built:
            return None
        answer, source_ids = built
        question_type = "overview"
        surface = f"{disease}_what_is"
    else:
        return None

    inventory = get_source_inventory(vault_root, disease)
    return {
        "answer": answer,
        "figures_used": [],
        "disease": disease,
        "question_type": question_type,
        "answer_mode": "local_surface",
        "hops_used": 0,
        "loaded_paths": set(),
        "loaded_source_ids": source_ids,
        "first_family_loaded": surface,
        "disease_maturity": "inventory_only",
        "disease_sources": inventory["total"],
        "disease_extraction": inventory["verification_status"],
        "research_trace": [
            {
                "step": "Matched local surface",
                "detail": f"surface={surface}; api_calls=0; source_ids={len(source_ids)}; inventory_cards={inventory['total']}",
            }
        ],
        "est_tokens": 0,
    }
