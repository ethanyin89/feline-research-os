---
id: src-cancer-036
type: source
title: "Gene expression association study in feline mammary carcinomas"
source_kind: paper
species: feline
diseases: [cancer]
models: [human-breast-cancer]
endpoints: [gene-expression, clinicopathology]
jurisdictions: [Portugal]
evidence_level: original-study
year: 2019
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
pmid: "31461477"
pmcid: "PMC6713336"
doi: "10.1371/journal.pone.0221776"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, mammary, FMC, gene-expression, CCND1, PKM2, PTBP1, TP53, c-MYC, oral-contraceptive, biomarker]
links:
  doi: "10.1371/journal.pone.0221776"
  url: "https://doi.org/10.1371/journal.pone.0221776"
  pmc: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6713336/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "CCND1 gene is overexpressed in 52% (14/27) of FMCs."
    - "PKM2 is overexpressed in 67% (18/27) of FMCs."
    - "PTBP1 is increased in 46% (11/24) of FMCs."
    - "All expression levels are correlated (r = 0.42-0.97, p < 0.044) with exception of c-MYC and PKM2."
    - "Oral contraceptive administration showed to be positively related with the TP53, YBX1, CCND1, FUS and PTBP1 RNA levels."
    - "Lymph node metastasis was associated with c-MYC RNA levels."
  source_supported_conclusion:
    - "CCND1, PKM2, and PTBP1 are frequently overexpressed in FMC vs normal tissue."
    - "Cancer-related genes form a correlated expression network (except c-MYC/PKM2)."
    - "Oral contraceptive history is associated with multiple gene expression levels."
    - "c-MYC expression correlates with lymph node metastasis."
  llm_inference:
    - "PKM2 and CCND1 may be candidate therapeutic targets given high overexpression rates."
    - "Oral contraceptive association suggests hormonal influence on FMC molecular profile."
    - "Gene expression panel could inform FMC molecular subtyping."
  # V2 enhanced fields
  study_design: "原始研究（2019 年 PLOS ONE），27 例 FMC vs 正常组织的 RT-qPCR 基因表达分析，评估 7 个癌相关基因"
  core_argument: "CCND1（52%）、PKM2（67%）、PTBP1（46%）在 FMC 中过表达——口服避孕药使用与多个基因表达水平相关——c-MYC 表达与淋巴结转移相关"
  implicit_premise: "假设 mRNA 表达水平反映蛋白功能活性；假设口服避孕药与基因表达的关联是因果关系而非混杂因素"
  unexpected_finding: "口服避孕药使用与 TP53、YBX1、CCND1、FUS 和 PTBP1 RNA 水平正相关——这种激素暴露与分子谱的关联超出传统 ER/PR 框架——提示更广泛的转录调控影响"
  title_gap: "标题说 FMC 基因表达关联研究，但真正发现是网络结构：癌相关基因形成相关表达网络（r = 0.42-0.97）——只有 c-MYC 和 PKM2 例外——这种协调表达提示共同调控机制"
  evidence_boundary: "n=27 小样本；基因表达模式是研究生物标记物而非临床诊断工具；口服避孕药关联需要更大队列验证"
---

# Gene expression association study in feline mammary carcinomas

## Evidence-Depth Caveat

**Deep-extracted from PMC full text (PMC6713336).** This 2019 PLOS ONE study evaluated 7 cancer-related genes in FMC vs disease-free tissue. CCND1 (52%), PKM2 (67%), PTBP1 (46%) overexpressed. Oral contraceptive use associated with multiple gene levels. Evidence level: original study with RT-qPCR.

## Source Check, 2026-06-09

Europe PMC full text extraction.

- PMID: 31461477
- PMCID: PMC6713336
- DOI: 10.1371/journal.pone.0221776
- Journal: PLOS ONE
- Year: 2019
- Open access: yes (CC-BY)

## Abstract Summary

This study evaluated expression of 7 cancer-related genes in feline mammary carcinomas (FMCs) compared to disease-free tissue.

**Genes evaluated:**
- TP53 (tumor suppressor)
- CCND1 (cyclin D1)
- FUS (RNA-binding protein)
- YBX1 (Y-box binding protein)
- PTBP1 (polypyrimidine tract binding protein)
- c-MYC (oncogene)
- PKM2 (pyruvate kinase)

**Expression findings:**

| Gene | Expression in FMC |
|------|-------------------|
| CCND1 | **Overexpressed** |
| PTBP1 | **Overexpressed** |
| PKM2 | **Overexpressed** |
| TP53 | Normal |
| c-MYC | Normal |
| YBX1 | Normal |
| FUS | Normal |

**Clinical associations:**
- Oral contraceptive use → associated with TP53, YBX1, CCND1, FUS, PTBP1 RNA levels
- Tumor size → associated with YBX1 RNA levels
- Lymph node metastasis → associated with c-MYC RNA levels

**Gene correlations:**
Strong correlations among most cancer-related genes (exception: c-MYC and PKM2 not correlated).

**Boundary:** Gene expression patterns suggest complex molecular network; these are research biomarkers, not clinical diagnostic tools.

## One-Line Summary

CCND1, PTBP1, and PKM2 are overexpressed in FMC; oral contraceptive use associated with multiple gene expression levels.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Gene expression association study in feline mammary carcinomas.
- The intake sheet locator is: 10.1371/journal.pone.0221776.

### source_supported_conclusion

- This is a first-pass source-card placeholder for triage and queue control.
- It should not support prevalence, diagnostic, treatment, management, or risk-ranking claims yet.

### llm_inference

- The title suggests a possible `cancer` role, but the actual claim-fit requires abstract or full-text review.

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
