---
id: src-cancer-081
type: source
title: "The Landscape of Tumor-Infiltrating Immune Cells in Feline Mammary Carcinoma: Pathological and Clinical Implications"
source_kind: paper
species: feline
diseases: [cancer]
models: [human-breast-cancer]
endpoints: [disease-free-survival, overall-survival, lymph-node-status]
jurisdictions: [Portugal]
evidence_level: original-study
year: 2022
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
pmid: "36010653"
pmcid: "PMC9406662"
doi: "10.3390/cells11162578"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, mammary, FMC, TILs, TAMs, CD8, CD4, CD3, CD163, CD68, FoxP3, prognosis, tumor-microenvironment, immunotherapy]
links:
  doi: "10.3390/cells11162578"
  url: "https://www.mdpi.com/2073-4409/11/16/2578"
  pmc: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9406662/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "CD3+ T lymphocytes were the most common subset of immune cells (17.6%), followed by B lymphocytes (CD20+, 14.4%)."
    - "Approximately 32% of the tumor-associated macrophages (CD68+) showed an M2-polarized subtype (CD163+)."
    - "Cats with mammary carcinoma showing higher percentage of sCD8+ TILs had longer DFS and OS (21 ± 6.8 months vs. 8 ± 1.8 months, p = 0.05; 31.0 ± 7.9 months vs. 15.5 ± 4.0 months, p = 0.021)."
    - "The univariate Cox regression analysis demonstrated that the presence of sCD8+ TILs is a significant predictive prognostic factor for OS (HR: 0.421, CI: 0.197–0.900, p = 0.026)."
    - "Higher percentages of iCD4+ T cells were correlated with positive lymph node status (p = 0.003)."
    - "Total CD3+ TILs and sCD8+ T cells were negatively correlated with metastasis (p = 0.021 and p = 0.017, respectively)."
  source_supported_conclusion:
    - "Stromal CD8+ TILs are a favorable prognostic marker in FMC (HR 0.421 for OS)."
    - "Intratumoral CD4+ TILs correlate with lymph node metastasis (unfavorable)."
    - "CD163+ M2 macrophages associate with undifferentiated/aggressive phenotypes."
    - "Triple-negative normal-like FMC subtype enriched for immune cells (sCD3+, sCD8+, sCD68+)."
    - "FMC immune microenvironment resembles human breast cancer patterns."
  llm_inference:
    - "sCD8+ TILs may serve as patient stratification marker for FMC prognosis."
    - "M2 macrophage repolarization could be a therapeutic strategy."
    - "Immunotherapy approaches from human breast cancer may translate to FMC."
  # V2 enhanced fields
  study_design: "回顾性队列研究（2022 年 Cells），73 例 FMC，免疫荧光分析 TILs 和 TAMs，中位随访 14.5 个月"
  core_argument: "FMC 肿瘤微环境与人类乳腺癌相似——基质 CD8+ TILs 是有利预后标记物（HR 0.421，p=0.026）——肿瘤内 CD4+ TILs 与淋巴结转移正相关——CD163+ M2 巨噬细胞与未分化/侵袭性表型相关——三阴性正常样 FMC 亚型富集免疫细胞"
  implicit_premise: "假设人类乳腺癌免疫微环境模式可直接映射到 FMC；假设免疫细胞浸润模式的预后意义可转化为治疗策略"
  unexpected_finding: "基质 vs 肿瘤内定位有相反的预后意义——基质 CD8+ 有利但肿瘤内 CD4+ 与转移相关——这种空间特异性可能解释以往研究的矛盾结果"
  title_gap: "标题说 FMC 中肿瘤浸润免疫细胞的景观及其病理学和临床意义，但真正发现是预后分层：sCD8+ TILs 是独立预后因素——可用于患者分层——为 FMC 免疫治疗靶向提供依据"
  evidence_boundary: "回顾性队列证据（n=73）；支持预后标记物声明和比较肿瘤学框架，不直接支持免疫治疗推荐——免疫治疗意义是推论而非证明"
---

# The Landscape of Tumor-Infiltrating Immune Cells in Feline Mammary Carcinoma: Pathological and Clinical Implications

## Evidence-Depth Caveat

**Deep-extracted from PMC full text (PMC9406662).** This 2022 study of 73 FMCs characterizes tumor-infiltrating immune cells. sCD8+ TILs are prognostic (HR 0.421, p=0.026). DFS 9.6 months, OS 14.5 months overall. Evidence level: retrospective cohort with immunofluorescence.

## Source Check, 2026-06-09

Europe PMC full text extraction.

| Field | Value |
|-------|-------|
| PMID | 36010653 |
| PMCID | PMC9406662 |
| DOI | 10.3390/cells11162578 |
| Journal | Cells (MDPI) |
| Year | 2022 |
| Authors | Nascimento C, Gameiro A, Correia J, et al. |
| Open access | yes |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Sample size | 73 feline mammary carcinomas |
| Age at diagnosis | 11.7 ± 0.3 years (range 7-18) |
| Overall DFS | 9.6 ± 1.1 months (95% CI: 7.4-11.7) |
| Overall OS | 14.5 ± 1.3 months (95% CI: 11.8-17.2) |
| Markers analyzed | CD3, CD4, CD8, CD20, CD56, FoxP3, CD68, CD163 |
| Most common TIL | CD3+ T cells (17.6%) |
| M2 TAM proportion | 32% of CD68+ macrophages are CD163+ |
| sCD8+ high DFS | 21 ± 6.8 months vs 8 ± 1.8 months (p=0.05) |
| sCD8+ high OS | 31.0 ± 7.9 months vs 15.5 ± 4.0 months (p=0.021) |
| sCD8+ Cox HR | 0.421 (95% CI: 0.197-0.900, p=0.026) |

**Boundary:** Prognostic associations well-supported. Immunotherapy implications are inference, not demonstrated.

## One-Line Summary

73 FMC immune profiling: stromal CD8+ TILs predict better survival (HR 0.421); CD163+ M2 TAMs associate with undifferentiated tumors; immune patterns parallel human breast cancer.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- 73 FMC analyzed for TILs (CD3, CD4, CD8, CD20, CD56, FoxP3) and TAMs (CD68, CD163)
- Higher stromal CD8+ TILs associated with longer DFS (p=0.05) and OS (p=0.021)
- Higher intratumoral CD4+ TILs correlated with positive lymph node status (p=0.003)
- CD163+ TAMs associated with undifferentiated tumors (p=0.013)
- sCD3+, sCD8+, sCD68+ enriched in triple-negative normal-like carcinomas

### source_supported_conclusion

- FMC immune microenvironment resembles human breast cancer patterns
- CD8+ T cell infiltration is a favorable prognostic marker
- CD163+ M2 macrophages associate with aggressive phenotypes
- Immune profiling may inform FMC treatment selection

### llm_inference

- Strong support for mammary-carcinoma.md tumor microenvironment claims
- Aligns with human breast cancer immunology
- Potential immunotherapy targets identified (CD8, CD163)

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
