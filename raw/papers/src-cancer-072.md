---
id: src-cancer-072
type: source
title: "Satellite Noncoding RNAs (ncRNA) as Cancer Biomarkers? New Insights from FA-SAT ncRNA Molecular and Clinical Profiles in Feline Mammary Tumors"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2022
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
pmid: 36342778
tags: [cancer, ncRNA, FA-SAT, biomarker, mammary, ER, Ki-67, ERBB2, c-MYC]
links:
  doi: "10.1089/omi.2022.0114"
  url: "https://doi.org/10.1089/omi.2022.0114"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "FA-SAT DNA levels positively correlated with lymphovascular invasion."
    - "FA-SAT long RNA negatively correlated with Ki-67 index; positively associated with ER status."
    - "FA-SAT small RNA positively correlated with tumor size and skin ulceration."
    - "FA-SAT long RNA correlated with ERBB2 and c-MYC RNA levels."
  source_supported_conclusion:
    - "FA-SAT ncRNA offers prospects as a potential cancer biomarker in feline mammary tumors."
    - "ncRNA profiles correlate with clinicopathological parameters."
  llm_inference:
    - "Novel molecular biomarker research; FA-SAT is present in both cat and human genomes."
    - "May inform mammary-carcinoma.md claims about emerging biomarkers."
  # V2 enhanced fields
  study_design: "原始研究（2022 年 OMICS），猫乳腺肿瘤中 FA-SAT 卫星 ncRNA 的 DNA 和 RNA 水平分析，与临床病理参数相关"
  core_argument: "FA-SAT ncRNA 与猫乳腺肿瘤临床病理参数相关——DNA 水平与淋巴血管侵犯正相关——长链 RNA 与 Ki-67 负相关、与 ER 状态正相关——小 RNA 与肿瘤大小和皮肤溃疡正相关——FA-SAT 在猫和人类基因组中都存在"
  implicit_premise: "假设相关性代表因果关系或预后价值；假设猫-人类 FA-SAT 保守性意味着转化研究价值"
  unexpected_finding: "FA-SAT 长链 RNA 与 ERBB2 和 c-MYC RNA 水平相关——这种卫星 ncRNA-癌基因关联提示新的调控机制——可能为猫乳腺癌分子亚型提供新的生物标记物"
  title_gap: "标题问卫星 ncRNA 能否作为癌症生物标记物，但真正发现是多重相关：FA-SAT 不同形式（DNA、长 RNA、小 RNA）与不同临床参数相关——提示复杂的生物学功能——但临床效用尚未验证"
  evidence_boundary: "研究阶段生物标记物证据；支持新型分子标记物研究背景，不支持临床诊断或预后声明；相关性不等于因果"
---

# Satellite Noncoding RNAs (ncRNA) as Cancer Biomarkers? New Insights from FA-SAT ncRNA Molecular and Clinical Profiles in Feline Mammary Tumors

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. 2022 OMICS: FA-SAT satellite ncRNA studied in FMC; DNA correlates with lymphovascular invasion; long RNA correlates with ER status, ERBB2, c-MYC; small RNA correlates with tumor size; conserved in human genome; research-stage biomarker. [Deep extraction worksheet](../../system/indexes/src-cancer-072-deep-extraction-round1.md).

## Source Check, 2026-06-02

| Field | Value |
|-------|-------|
| PMID | 36342778 |
| DOI | 10.1089/omi.2022.0114 |
| Journal | OMICS |
| Year | 2022 |
| Authors | Ferreira D, Soares M, Correia J, et al. |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Biomarker | FA-SAT satellite ncRNA (DNA and RNA levels) |
| FA-SAT DNA | Positively correlated with lymphovascular invasion |
| FA-SAT long RNA | Negatively correlated with Ki-67; positively with ER status |
| FA-SAT small RNA | Positively correlated with tumor size and skin ulceration |
| Oncogene correlation | FA-SAT long RNA correlated with ERBB2 and c-MYC |
| Translational value | FA-SAT present in both cat and human genomes |

**Boundary:** Abstract-level extraction. Novel biomarker research; correlations reported but clinical utility not yet established.

## One-Line Summary

FA-SAT ncRNA levels correlate with lymphovascular invasion, Ki-67, ER status, tumor size, and ERBB2/c-MYC in feline mammary tumors—potential novel biomarker.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- FA-SAT is the major satellite DNA of the cat genome, also present in humans
- FA-SAT DNA levels positively correlated with lymphovascular invasion
- FA-SAT long RNA negatively correlated with Ki-67 index
- FA-SAT long RNA positively associated with ER status
- FA-SAT small RNA positively correlated with tumor size and skin ulceration
- FA-SAT long RNA correlated with ERBB2 and c-MYC RNA levels

### source_supported_conclusion

- FA-SAT ncRNA offers prospects as a potential cancer biomarker in cats
- Multiple clinicopathological associations suggest prognostic relevance
- Translational relevance: FA-SAT is conserved between cats and humans

### llm_inference

- Novel molecular biomarker approach for feline mammary cancer
- May complement existing markers (ER, PR, HER2, Ki-67) for FMC subtyping
- Research-stage biomarker; clinical utility not yet validated

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
