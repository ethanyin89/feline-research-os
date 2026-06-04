"""Deterministic local answer surfaces for no-API public testing.

These helpers expose compiled topic pages as answer-shaped responses without
importing the Streamlit app module.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Optional

from query import parse_source_ids_from_frontmatter


# Disease maturity levels for evidence depth indication
DISEASE_MATURITY = {
    "ckd": {"sources": 24, "extraction": "full", "maturity": "Mature", "label_en": "Evidence: Mature (24 sources, fully extracted)", "label_zh": "证据成熟度：完整（24篇来源，全量提取）"},
    "fip": {"sources": 24, "extraction": "full", "maturity": "Mature", "label_en": "Evidence: Mature (24 sources, fully extracted)", "label_zh": "证据成熟度：完整（24篇来源，全量提取）"},
    "hcm": {"sources": 24, "extraction": "full", "maturity": "Mature", "label_en": "Evidence: Mature (24 sources, fully extracted)", "label_zh": "证据成熟度：完整（24篇来源，全量提取）"},
    "ibd": {"sources": 24, "extraction": "full", "maturity": "Mature", "label_en": "Evidence: Mature (24 sources, fully extracted)", "label_zh": "证据成熟度：完整（24篇来源，全量提取）"},
    "fcv": {"sources": 24, "extraction": "full", "maturity": "Mature", "label_en": "Evidence: Mature (24 sources, fully extracted)", "label_zh": "证据成熟度：完整（24篇来源，全量提取）"},
    "diabetes": {"sources": 118, "extraction": "partial", "maturity": "Developing", "label_en": "Evidence: Developing (118 sources, partial extraction)", "label_zh": "证据成熟度：发展中（118篇来源，部分提取）"},
    "obesity": {"sources": 87, "extraction": "partial", "maturity": "Developing", "label_en": "Evidence: Developing (87 sources, partial extraction)", "label_zh": "证据成熟度：发展中（87篇来源，部分提取）"},
    "cancer": {"sources": 102, "extraction": "partial", "maturity": "Developing", "label_en": "Evidence: Developing (102 sources, partial extraction)", "label_zh": "证据成熟度：发展中（102篇来源，部分提取）"},
}


def _get_maturity_label(disease: str, chinese: bool) -> str:
    """Get the maturity label for a disease."""
    info = DISEASE_MATURITY.get(disease.lower(), {})
    if chinese:
        return info.get("label_zh", "证据成熟度：未知")
    return info.get("label_en", "Evidence: Unknown")


def _contains_chinese(text: str) -> bool:
    return bool(re.search(r"[\u3400-\u9fff]", text))


def _infer_disease(question: str, disease_hint: Optional[str]) -> str:
    if disease_hint:
        return disease_hint
    lowered = question.lower()
    if any(term in lowered or term in question for term in ["fip", "传腹", "传染性腹膜炎", "gs-441524", "gs441524", "remdesivir"]):
        return "fip"
    if any(term in lowered or term in question for term in ["ckd", "kidney", "renal", "肾", "慢性肾"]):
        return "ckd"
    if any(term in lowered or term in question for term in ["obesity", "obese", "肥胖", "超重"]):
        return "obesity"
    if any(term in lowered or term in question for term in ["cancer", "tumor", "tumour", "肿瘤", "癌"]):
        return "cancer"
    return "unknown"


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
    maturity = _get_maturity_label("fip", chinese)
    if chinese:
        answer = (
            f"**{maturity}**\n\n"
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
            f"**{maturity}**\n\n"
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
    maturity = _get_maturity_label("fip", chinese)
    if chinese:
        answer = (
            f"**{maturity}**\n\n"
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
            f"**{maturity}**\n\n"
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
    maturity = _get_maturity_label("fip", chinese)
    prefix = (
        f"**{maturity}**\n\n"
        f"这是本地 vault 的 FIP 识别/警示信号解释；本次没有调用 API。 [source_supported_conclusion: {cited}]\n\n"
        if chinese
        else f"**{maturity}**\n\n"
        f"This is a local vault FIP recognition and warning-signs answer. No API call was made. [source_supported_conclusion: {cited}]\n\n"
    )
    return prefix + body, source_ids


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
    maturity = _get_maturity_label(disease, chinese)
    prefix = (
        f"**{maturity}**\n\n"
        f"这是本地 vault 的基础解释；本次没有调用 API。 [source_supported_conclusion: {cited}]\n\n"
        if chinese
        else f"**{maturity}**\n\n"
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

    if disease == "fip" and any(term in lowered or term in question for term in ["治疗证据", "疗效证据", "treatment evidence", "gs-441524", "remdesivir", "抗病毒"]):
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

    maturity_info = DISEASE_MATURITY.get(disease, {})
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
        "disease_maturity": maturity_info.get("maturity", "Unknown"),
        "disease_sources": maturity_info.get("sources", 0),
        "disease_extraction": maturity_info.get("extraction", "unknown"),
        "research_trace": [
            {
                "step": "Matched local surface",
                "detail": f"surface={surface}; api_calls=0; source_ids={len(source_ids)}; maturity={maturity_info.get('maturity', 'Unknown')}",
            }
        ],
        "est_tokens": 0,
    }
