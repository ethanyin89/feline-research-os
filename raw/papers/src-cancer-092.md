---
id: src-cancer-092
type: source
title: "Feline thymidine kinase 1: molecular characterization and evaluation of its serum form as a diagnostic biomarker"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2021
status: ingested
extraction_depth: abstract
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
pmid: 34579716
tags: [cancer, TK1, biomarker, serum, diagnosis, prognosis, lymphoma, mammary]
links:
  doi: "10.1186/s12917-021-03030-5"
  url: "https://doi.org/10.1186/s12917-021-03030-5"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "PubMed-indexed: BMC Vet Res. 2021 Sep 27;17(1):316."
    - "Authors: Wang L, Sharif H, Saellström S, Rönnberg H, Eriksson S."
    - "TK1 upregulated in cancer cells, leaked into blood."
    - "Serum TK1 used as biomarker for cancer diagnosis/prognosis in human medicine."
    - "Feline TK1 shows high sequence similarity to TK1 from other species."
  source_supported_conclusion:
    - "Serum TK1 may serve as diagnostic biomarker for feline cancers."
    - "Feline TK1 characterized and evaluated for diagnostic use."
  llm_inference:
    - "Potential pan-cancer biomarker for feline oncology."
    - "May inform cancer diagnosis section across tumor types."
  # V2 enhanced fields
  study_design: "分子表征研究（2021 年 BMC Vet Res），猫 TK1 的分子克隆、表达纯化和酶学特性研究"
  core_argument: "血清 TK1 可作为猫癌症的诊断生物标志物——TK1 在癌细胞中上调并泄漏入血——猫 TK1 与其他物种高度相似——底物包括嘧啶脱氧核苷和抗癌/抗病毒核苷类似物"
  implicit_premise: "假设人类医学中 TK1 作为癌症生物标志物的成功经验可转化到猫；假设血清 TK1 水平与肿瘤负荷相关"
  unexpected_finding: "猫 TK1 可磷酸化抗癌和抗病毒核苷类似物——暗示这些药物在猫中可能有效——这扩展了 TK1 研究的临床相关性"
  title_gap: "标题说猫 TK1 的分子表征和血清形式的诊断生物标志物评估，但真正价值是泛癌应用：TK1 不特异于任何肿瘤类型——可作为淋巴瘤、乳腺癌等多种肿瘤的监测标志物——并可能预测核苷类药物敏感性"
  evidence_boundary: "分子表征证据；支持 TK1 作为生物标志物候选的基础，不直接支持诊断应用——临床验证研究需要"
---

# Feline thymidine kinase 1: molecular characterization and evaluation of its serum form as a diagnostic biomarker

## Source Check, 2026-06-03

| Field | Value |
|-------|-------|
| PMID | 34579716 |
| DOI | 10.1186/s12917-021-03030-5 |
| Journal | BMC Vet Res |
| Year | 2021 |
| Authors | Wang L, Sharif H, Saellström S, Rönnberg H, Eriksson S |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Study type | Biomarker characterization |
| Target | Feline thymidine kinase 1 (TK1) |
| Mechanism | TK1 upregulated in cancer cells, leaked into blood |
| Application | Serum TK1 as diagnostic biomarker |
| Similarity | High sequence similarity to human TK1 |

**Boundary:** Abstract-level extraction. TK1 biomarker findings may inform pan-cancer diagnostic approaches.

## One-Line Summary

Feline TK1 characterized as potential serum biomarker for cancer diagnosis; high similarity to human TK1 supports translational relevance.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- TK1 catalyzes initial phosphorylation of thymidine in salvage pathway synthesis
- TK1 is a cytosolic enzyme with highest level during S-phase of cell cycle
- In cancer cells TK1 is upregulated and excess TK1 is leaked into blood
- Serum TK1 used as biomarker for cancer diagnosis and prognosis in human medicine
- Feline TK1 shows high sequence similarity to TK1 from other species
- Feline TK1 cloned, expressed and affinity purified

### source_supported_conclusion

- Serum TK1 may serve as diagnostic biomarker for feline cancers
- Feline TK1 enzymatically characterized for diagnostic application
- Substrates include pyrimidine deoxyribonucleosides, ribonucleosides, and some anticancer/antiviral nucleoside analogs

### llm_inference

- Potential pan-cancer biomarker applicable across tumor types (lymphoma, mammary, etc.)
- May inform cancer diagnosis and monitoring section
- Translational relevance for human-feline comparative oncology

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
