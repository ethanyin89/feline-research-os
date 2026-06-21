---
id: src-cancer-043
type: source
title: "Identification of an immune-suppressed subtype of feline triple-negative basal-like invasive mammary carcinomas, spontaneous models of breast cancer"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2020
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
pmid: 31959092
doi: "10.1177/1010428319901052"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, identification, immune-suppressed, subtype, triple-negative, basal-like, invasive, mammary]
links:
  doi: "10.1177/1010428319901052"
  url: "https://doi.org/10.1177/1010428319901052"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Crossref metadata resolves this DOI and reports abstract availability for source scope checking."
    - "Crossref container: Tumor Biology; year: 2020."
  source_supported_conclusion:
    - "This card is abstract-weighted only; it can guide navigation and extraction priority."
    - "It must not support reader-facing clinical claims until a full abstract extraction or source worksheet is completed."
  llm_inference:
    - "High-reuse guideline, review, treatment-control, or risk-architecture sources remain candidates for deep extraction."
  # V2 enhanced fields
  study_design: "回顾性队列研究（2020 年 Tumour Biology），180 只手术治疗的猫侵袭性乳腺癌，2 年随访，FoxP3/ER/PR/Ki-67/HER2/CK14 标记物分析"
  core_argument: "调节性 T 细胞（Tregs）识别 FMC 的免疫抑制亚型——瘤周 Tregs 比瘤内多 300 倍——高 Tregs 与更差的 DFI 和 OS 相关——三阴性基底样（CK14+）肿瘤中存在 Treg 富集亚组——这是免疫治疗的潜在靶点"
  implicit_premise: "假设 Tregs 富集是免疫抑制的标记物而非旁观者效应；假设猫 TNBC 可作为人类 TNBC 免疫治疗研究的自发模型"
  unexpected_finding: "瘤周 Tregs 比瘤内多 300 倍——这种空间分布暗示免疫抑制主要发生在肿瘤边界而非核心——可能影响免疫治疗策略设计"
  title_gap: "标题说识别猫三阴性基底样侵袭性乳腺癌的免疫抑制亚型，但真正发现是预后分层：Treg 富集状态可用于患者分层——高 Tregs = 差预后——为免疫检查点抑制剂研究提供依据"
  evidence_boundary: "回顾性队列证据（n=180）；支持 Tregs 作为预后标记物和比较肿瘤学框架，不支持免疫治疗推荐——治疗意义是推论"
---

# Identification of an immune-suppressed subtype of feline triple-negative basal-like invasive mammary carcinomas, spontaneous models of breast cancer

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. 2020 Tumour Biology: 180 FMC cats, 68% TNBC; peritumoral Tregs 300× more abundant; high Tregs = worse survival. Treg-enriched basal-like TNBC is immune-suppressed subtype. [Deep extraction worksheet](../../system/indexes/src-cancer-043-deep-extraction-round1.md).

## Source Check, 2026-06-01

PubMed abstract fetched as a zero-cost extraction step.

- PMID: 31959092
- DOI: 10.1177/1010428319901052
- Journal: Tumour Biology
- Year: 2020

## Abstract Summary

This study tested whether regulatory T cells identify an immune-suppressed subgroup of feline invasive mammary carcinoma, especially triple-negative basal-like tumors.

**Study design:**

| Feature | Abstract-Extracted Detail |
|---------|---------------------------|
| Population | 180 female cats with feline invasive mammary carcinomas |
| Treatment context | Surgery only |
| Follow-up | 2-year post-mastectomy follow-up |
| Markers assessed | FoxP3, ER, PR, Ki-67, HER2, CK14 |
| TNBC subset | 123/180 tumors were ER-, PR-, HER2- |
| Luminal subset | 57/180 tumors were ER+ and/or PR+ |

**Key findings:**

- Peritumoral regulatory T cells were more than 300 times more abundant than intratumoral regulatory T cells.
- Peritumoral and intratumoral regulatory T cells were associated with shorter disease-free interval and overall survival in both triple-negative and luminal feline invasive mammary carcinomas.
- In triple-negative basal-like (CK14+) tumors, a regulatory T-cell-enriched subgroup had significantly poorer disease-free interval, overall survival, and cancer-specific survival than regulatory T-cell-poor tumors.

**Comparative oncology role:**

The authors frame feline invasive mammary carcinomas as spontaneous models for studying immunotherapy strategies in an immune-suppressed tumor microenvironment.

**Boundary:** This is prognostic and model-biology evidence from an abstract-level extraction. It does not establish an immunotherapy treatment recommendation for cats with mammary carcinoma.

## One-Line Summary

In 180 surgically treated feline invasive mammary carcinomas, high regulatory T-cell numbers identified poorer-prognosis tumors, including an immune-suppressed triple-negative basal-like subgroup.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Identification of an immune-suppressed subtype of feline triple-negative basal-like invasive mammary carcinomas, spontaneous models of breast cancer.
- The intake sheet locator is: 10.1177/1010428319901052.

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
