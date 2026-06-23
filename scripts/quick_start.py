#!/usr/bin/env python3
"""
scripts/quick_start.py — Quick Start layer for the three-layer UI architecture.

Quick Start provides 30-second understanding of a disease/concept:
- One-line explanation
- Why it matters
- Common misconceptions
- Navigation buttons to Briefing or Research Workspace

Constraint: Output must fit in one screen (≤600 characters).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class QuickStartOutput:
    """Structured output for Quick Start layer."""
    disease: str
    one_liner: str  # 一句话解释
    why_matters: str  # 为什么重要
    misconception: str  # 容易误解
    when_to_dig_deeper: str  # 什么时候需要深入研究
    has_briefing: bool  # 是否有 Briefing 可用
    language: str  # "zh" or "en"

    def total_length(self) -> int:
        """Return total character count for one-screen constraint."""
        return len(self.one_liner) + len(self.why_matters) + len(self.misconception)


# Pre-defined Quick Start content for each disease
# These are curated from the analysis materials and briefings
QUICK_START_CONTENT_ZH: dict[str, QuickStartOutput] = {
    "hcm": QuickStartOutput(
        disease="HCM",
        one_liner="猫 HCM 是以左心室心肌增厚为主要特征的心肌病，可能导致舒张功能下降、左心房扩大、心衰和动脉血栓栓塞风险。",
        why_matters="很多猫早期没有明显症状，但一旦出现左心房扩大、血流淤滞或血栓形成，风险会明显增加。早期识别对于风险分层和管理至关重要。",
        misconception="HCM 不能只看室壁厚度。需要结合左心房大小、舒张功能、LVOTO/SAM、NT-proBNP、cTnI 和临床表现综合判断。",
        when_to_dig_deeper="需要评估无症状期的抗血栓指征、分期标准或心衰急性期管理方案时。",
        has_briefing=True,
        language="zh",
    ),
    "ckd": QuickStartOutput(
        disease="CKD",
        one_liner="猫慢性肾病（CKD）是老年猫最常见的疾病之一，以肾功能进行性下降为特征，常见于 10 岁以上猫。",
        why_matters="CKD 是猫死亡的主要原因之一。早期发现和管理可以显著延缓疾病进展，改善生活质量。",
        misconception="CKD 不只是「肾指标高」。IRIS 分期需要结合 creatinine、SDMA、蛋白尿和血压进行综合评估。",
        when_to_dig_deeper="需要对比不同降磷药物的药效学终点，或评估早期干预策略时。",
        has_briefing=True,
        language="zh",
    ),
    "fip": QuickStartOutput(
        disease="FIP",
        one_liner="猫传染性腹膜炎（FIP）是由猫冠状病毒突变引起的致命性疾病，分为湿性（渗出型）和干性（非渗出型）两种形式。",
        why_matters="FIP 曾被认为是不治之症，但近年 GS-441524 等抗病毒药物带来了治愈的可能性。早期诊断和治疗至关重要。",
        misconception="不是所有感染猫冠状病毒的猫都会发展为 FIP。只有病毒发生特定突变并引起免疫反应时才会发病。",
        when_to_dig_deeper="需要了解抗病毒药物的耐药性、复发率评价体系或入组标准时。",
        has_briefing=True,
        language="zh",
    ),
    "ibd": QuickStartOutput(
        disease="IBD",
        one_liner="猫炎症性肠病（IBD）是一组以慢性胃肠道炎症为特征的疾病，表现为反复呕吐、腹泻、体重下降。",
        why_matters="IBD 需要与小细胞淋巴瘤鉴别，两者临床表现相似但预后和治疗差异显著。组织病理学是金标准。",
        misconception="IBD 不是单纯的「肠胃敏感」。它是免疫介导的慢性炎症，需要系统性诊断和长期管理。",
        when_to_dig_deeper="需要探索 IBD 发展为淋巴瘤的标志物、微生态治疗研究进展时。",
        has_briefing=True,
        language="zh",
    ),
    "diabetes": QuickStartOutput(
        disease="Diabetes",
        one_liner="猫糖尿病是以胰岛素抵抗和/或胰岛素分泌不足为特征的代谢性疾病，表现为多饮、多尿、体重下降。",
        why_matters="与人类 2 型糖尿病相似，猫糖尿病在早期通过饮食管理和血糖控制可能实现缓解。肥胖是主要风险因素。",
        misconception="猫糖尿病不一定需要终身注射胰岛素。通过低碳水饮食和体重管理，部分猫可以达到临床缓解。",
        when_to_dig_deeper="需要了解 SGLT2 抑制剂在猫的应用，或糖尿病动物模型的造模标准时。",
        has_briefing=True,
        language="zh",
    ),
    "fcv": QuickStartOutput(
        disease="FCV",
        one_liner="猫杯状病毒（FCV）是引起猫上呼吸道感染和口腔溃疡的常见病原，也可导致跛行综合征。",
        why_matters="FCV 具有高度变异性，某些毒株可引起 VS-FCV（毒力增强型）导致全身性血管炎和高死亡率。",
        misconception="FCV 感染不只是「猫感冒」。病毒可以在康复后持续存在并传播给其他猫。",
        when_to_dig_deeper="需要探究 FCV 突变株检测机制或广谱抗病毒药研发进展时。",
        has_briefing=False,  # No briefing file yet
        language="zh",
    ),
}

QUICK_START_CONTENT_EN: dict[str, QuickStartOutput] = {
    "hcm": QuickStartOutput(
        disease="HCM",
        one_liner="Feline HCM is a heart muscle disease characterized by left ventricular wall thickening, leading to diastolic dysfunction, left atrial enlargement, heart failure, and arterial thromboembolism risk.",
        why_matters="Many cats show no early symptoms, but once left atrial enlargement, blood stasis, or thrombus formation occurs, risk increases significantly. Early detection is critical for risk stratification.",
        misconception="HCM cannot be diagnosed by wall thickness alone. Assessment requires LA size, diastolic function, LVOTO/SAM, NT-proBNP, cTnI, and clinical signs.",
        when_to_dig_deeper="When evaluating antithrombotic indications, staging criteria, or acute heart failure management protocols.",
        has_briefing=True,
        language="en",
    ),
    "ckd": QuickStartOutput(
        disease="CKD",
        one_liner="Feline chronic kidney disease (CKD) is one of the most common diseases in senior cats, characterized by progressive decline in kidney function, typically seen in cats over 10 years old.",
        why_matters="CKD is a leading cause of death in cats. Early detection and management can significantly slow disease progression and improve quality of life.",
        misconception="CKD is not just 'high kidney values'. IRIS staging requires comprehensive assessment of creatinine, SDMA, proteinuria, and blood pressure.",
        when_to_dig_deeper="When comparing pharmacodynamic endpoints of different phosphate binders or early intervention strategies.",
        has_briefing=True,
        language="en",
    ),
    "fip": QuickStartOutput(
        disease="FIP",
        one_liner="Feline infectious peritonitis (FIP) is a fatal disease caused by mutated feline coronavirus, presenting in wet (effusive) and dry (non-effusive) forms.",
        why_matters="FIP was once considered incurable, but GS-441524 and similar antivirals now offer hope for cure. Early diagnosis and treatment are critical.",
        misconception="Not all cats infected with feline coronavirus develop FIP. Disease only occurs when the virus mutates and triggers specific immune responses.",
        when_to_dig_deeper="When understanding antiviral resistance, relapse rate evaluation systems, or trial inclusion criteria.",
        has_briefing=True,
        language="en",
    ),
    "ibd": QuickStartOutput(
        disease="IBD",
        one_liner="Feline inflammatory bowel disease (IBD) is a group of diseases characterized by chronic GI inflammation, presenting with recurrent vomiting, diarrhea, and weight loss.",
        why_matters="IBD must be differentiated from small cell lymphoma — they present similarly but have vastly different prognosis and treatment. Histopathology is the gold standard.",
        misconception="IBD is not simply 'sensitive stomach'. It's an immune-mediated chronic inflammation requiring systematic diagnosis and long-term management.",
        when_to_dig_deeper="When exploring markers for IBD-to-lymphoma progression or microbiome therapy research.",
        has_briefing=True,
        language="en",
    ),
    "diabetes": QuickStartOutput(
        disease="Diabetes",
        one_liner="Feline diabetes is a metabolic disease characterized by insulin resistance and/or insufficient insulin secretion, presenting with polydipsia, polyuria, and weight loss.",
        why_matters="Similar to human type 2 diabetes, feline diabetes may achieve remission with early dietary management and glycemic control. Obesity is the main risk factor.",
        misconception="Feline diabetes doesn't always require lifelong insulin injections. Some cats can achieve clinical remission with low-carb diet and weight management.",
        when_to_dig_deeper="When evaluating SGLT2 inhibitors in cats or criteria for diabetic animal models.",
        has_briefing=True,
        language="en",
    ),
    "fcv": QuickStartOutput(
        disease="FCV",
        one_liner="Feline calicivirus (FCV) is a common pathogen causing upper respiratory infections and oral ulcers in cats, also associated with limping syndrome.",
        why_matters="FCV is highly variable — some strains cause VS-FCV (virulent systemic) leading to systemic vasculitis and high mortality.",
        misconception="FCV infection is not just 'cat cold'. The virus can persist after recovery and spread to other cats.",
        when_to_dig_deeper="When researching FCV mutant detection mechanisms or broad-spectrum antiviral development.",
        has_briefing=False,
        language="en",
    ),
}


def get_quick_start(disease: str, language: str = "zh") -> Optional[QuickStartOutput]:
    """
    Get Quick Start content for a disease.

    Args:
        disease: Disease code (hcm, ckd, fip, ibd, diabetes, fcv)
        language: "zh" for Chinese, "en" for English

    Returns:
        QuickStartOutput or None if not found
    """
    disease_lower = disease.lower().strip()

    # Normalize common variants
    disease_map = {
        "肥厚型心肌病": "hcm",
        "心肌病": "hcm",
        "慢性肾病": "ckd",
        "肾病": "ckd",
        "传腹": "fip",
        "传染性腹膜炎": "fip",
        "炎症性肠病": "ibd",
        "肠病": "ibd",
        "糖尿病": "diabetes",
        "杯状病毒": "fcv",
    }

    if disease_lower in disease_map:
        disease_lower = disease_map[disease_lower]

    if language == "zh":
        return QUICK_START_CONTENT_ZH.get(disease_lower)
    else:
        return QUICK_START_CONTENT_EN.get(disease_lower)


def detect_quick_start_intent(query: str) -> Optional[str]:
    """
    Detect if a query is asking for Quick Start explanation.

    Returns disease code if detected, None otherwise.

    Examples:
    - "解释CKD" -> "ckd"
    - "HCM是什么" -> "hcm"
    - "FIP怎么识别" -> "fip"
    - "IBD和淋巴瘤怎么区分" -> "ibd"
    """
    import re

    query_lower = query.strip().lower()
    if not query_lower:
        return None

    disease_codes = ["hcm", "ckd", "fip", "ibd", "diabetes", "fcv"]

    # 1. First find which disease codes are present in the query
    present_diseases = [code for code in disease_codes if code in query_lower]
    if not present_diseases:
        return None

    # 2. Check for exact match (e.g. query is exactly "ckd" or "hcm")
    if query_lower in disease_codes:
        return query_lower

    # 3. Check for explicit Quick Start patterns (regex/phrases)
    quick_start_phrases = [
        r"解释\s*",
        r"是什么",
        r"什么是\s*",
        r"怎么识别",
        r"如何识别",
        r"怎么区分",
        r"如何区分",
        r"区分\s*",
        r"为什么危险",
        r"为何危险",
        r"explain\s+",
        r"what\s+is\s+",
        r"what's\s+",
        r"how\s+to\s+identify",
        r"why\s+dangerous",
        r"how\s+to\s+recognize",
        r"概念\s*速查",
        r"疾病\s*速览",
        r"快速\s*理解",
        r"快速\s*入门",
    ]

    has_qs_indicator = False
    for phrase in quick_start_phrases:
        if re.search(phrase, query_lower):
            has_qs_indicator = True
            break

    if has_qs_indicator:
        # Override if query has clear research indicators: "构建", "比较", "梳理", "提炼", "证据", "终点", "指标", "地图", "文献", "研究"
        research_keywords = [
            "构建", "比较", "梳理", "提炼", "证据", "终点", "指标", "地图", "文献", "研究",
            "search", "find", "latest", "papers", "study", "studies", "trial", "trials",
            "dossier", "briefing", "workspace", "dossiers", "briefings"
        ]
        if any(kw in query_lower for kw in research_keywords):
            return None
        return present_diseases[0]

    return None


def format_quick_start_markdown(output: QuickStartOutput) -> str:
    """
    Format QuickStartOutput as markdown for display.

    The format is designed to be readable in one screen.
    """
    if output.language == "zh":
        return f"""## {output.disease} 是什么？

**一句话解释：**
{output.one_liner}

**为什么重要：**
{output.why_matters}

**容易误解：**
{output.misconception}

**什么时候需要深入研究：**
{output.when_to_dig_deeper}
"""
    else:
        return f"""## What is {output.disease}?

**One-liner:**
{output.one_liner}

**Why it matters:**
{output.why_matters}

**Common misconception:**
{output.misconception}

**When to dig deeper:**
{output.when_to_dig_deeper}
"""


# For testing
if __name__ == "__main__":
    # Test Quick Start for HCM
    hcm_zh = get_quick_start("hcm", "zh")
    if hcm_zh:
        print(format_quick_start_markdown(hcm_zh))
        print(f"\nTotal length: {hcm_zh.total_length()} chars")
        print(f"Has briefing: {hcm_zh.has_briefing}")
