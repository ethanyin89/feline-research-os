---
id: src-cancer-090
type: source
title: "Activation of AKT in feline mammary carcinoma: A new prognostic factor for feline mammary tumours"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2012
status: ingested
extraction_depth: abstract
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
pmid: 21282070
tags: [cancer, mammary, AKT, PI3K, PTEN, HER2, prognosis, signaling]
links:
  doi: "10.1016/j.tvjl.2010.12.016"
  url: "https://www.sciencedirect.com/science/article/abs/pii/S109002331000448X?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "p-AKT expression correlates with tumour malignancy, histological dedifferentiation, clinical recurrence."
    - "p-AKT+ tumors = shorter disease-free period."
    - "AKT activation associated with HER2 expression and PTEN down-regulation."
    - "Feline AKT shows high homology with human AKT gene."
  source_supported_conclusion:
    - "AKT activation is a prognostic marker for FMC."
    - "PI3K/AKT/PTEN pathway dysregulation similar to human breast cancer."
  llm_inference:
    - "Supports mammary-carcinoma.md molecular pathway claims."
    - "Feline model valid for human breast cancer AKT pathway research."
  # V2 enhanced fields
  study_design: "回顾性队列研究（2012 年 Vet J），39 只猫的 27 例恶性 + 12 例良性乳腺肿瘤，24 个月随访，p-AKT/HER2/PTEN 表达分析"
  core_argument: "p-AKT 激活是 FMC 的新预后因素——与恶性程度、组织学去分化、临床复发相关——p-AKT+ 肿瘤的无病期更短——AKT 激活与 HER2 表达和 PTEN 下调相关——猫 AKT 与人 AKT 高度同源"
  implicit_premise: "假设 PI3K/AKT/PTEN 通路在 FMC 中的失调模式与人类乳腺癌相似；假设免疫组化检测的 p-AKT 可代表通路功能活性"
  unexpected_finding: "AKT 激活与 ERα 或 PR 表达无关——暗示 FMC 中 AKT 通路激活是激素非依赖性机制——与人类激素非依赖性乳腺癌亚型一致"
  title_gap: "标题说 AKT 激活是 FMC 的新预后因素，但真正发现是机制整合：p-AKT-HER2-PTEN 轴共同失调——与人类乳腺癌分子亚型一致——支持 FMC 作为人类乳腺癌研究模型的有效性"
  evidence_boundary: "回顾性队列证据（n=39 猫）；支持 AKT 预后标记物声明和比较肿瘤学框架，不直接支持 PI3K 抑制剂治疗推荐——治疗意义是推论"
---

# Activation of AKT in feline mammary carcinoma: A new prognostic factor for feline mammary tumours

## Source Check, 2026-06-03

| Field | Value |
|-------|-------|
| PMID | 21282070 |
| DOI | 10.1016/j.tvjl.2010.12.016 |
| Journal | Vet J |
| Year | 2012 |
| Authors | Maniscalco L, Iussich S, de Las Mulas JM, et al. |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Sample size | 27 malignant + 12 benign tumors from 39 cats |
| p-AKT correlation | Malignancy, dedifferentiation, clinical recurrence |
| Survival impact | p-AKT+ tumors = shorter disease-free period |
| Pathway | AKT activation with HER2 expression, PTEN down-regulation |
| ER/PR | No AKT activation relation to ERα or PR expression |
| Homology | Feline AKT high homology with human AKT |

**Boundary:** Abstract-level extraction. AKT pathway findings can inform FMC molecular subtyping and prognosis claims.

## One-Line Summary

p-AKT expression correlates with FMC malignancy, dedifferentiation, recurrence, and shorter DFS; associated with HER2+/PTEN-down pattern similar to human breast cancer.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- 27 malignant + 12 benign mammary tumors from 39 cats, 24-month follow-up
- p-AKT expression correlates with tumour malignancy, histological dedifferentiation, recurrence
- p-AKT+ tumors have shorter disease-free period than p-AKT-negative
- AKT activation associated with HER2 expression and PTEN down-regulation
- No AKT activation relation to ERα or PR expression
- Feline AKT gene shows high homology with human AKT

### source_supported_conclusion

- AKT activation is a prognostic marker for FMC
- PI3K/AKT/PTEN pathway dysregulation similar to hormone-independent human breast cancer
- HER2-AKT axis validated in feline model

### llm_inference

- Supports mammary-carcinoma.md molecular pathway and prognosis claims
- AKT as potential therapeutic target (PI3K inhibitors)
- Feline model valid for human breast cancer AKT pathway research

## Claim-Fit Judgment

Strongest safe use:

- intake ownership
- source queue placement
- deduplication and future extraction planning

Must not control yet:

- reader-facing medical advice
- numeric claims
- comparative ranking
- guideline-like recommendations
- mechanism closure

## Image Asset TODO

- figures to capture: unknown until source text is read
- why these matter: tables or figures should remain behind the candidate gate until labels are verified

## Open Follow-Up Questions

- What source family is confirmed by the abstract or article body?
- Which claims, if any, are reusable for the cancer module?
- Does this source deserve deep extraction, or should it remain queue context?
- Are there tables or figures that change the module structure?

## Linked Entities

- diseases: cancer
- models:
- endpoints:
- mechanisms:
- regulations:
