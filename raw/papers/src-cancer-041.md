---
id: src-cancer-041
type: source
title: "Prognostic Factors in Feline Mammary Carcinoma"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
pmid: 6572759
year: 1983
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, prognostic, factors, mammary, carcinoma, get, access, arrow]
links:
  doi: "10.1093/jnci/70.4.709"
  url: "https://academic.oup.com/jnci/article-abstract/70/4/709/938577?redirectedFrom=fulltext&login=false"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Prognostic Factors in Feline Mammary Carcinoma Get access Arrow."
    - "The intake sheet locator is: https://academic.oup.com/jnci/article-abstract/70/4/709/938577?redirectedFrom=fulltext&login=false."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
  # V2 enhanced fields
  study_design: "前瞻性随访研究（1983 年 JNCI），202 只 FMC 手术治疗猫，分析 35 个因素"
  core_argument: "FMC 有 6 个独立预后因素：年龄、肿瘤直径、显微镜下淋巴结阳性、有丝分裂指数、肿瘤坏死、手术完整性——这些因素在校正后仍独立预测生存"
  implicit_premise: "假设 1983 年的手术技术和分期系统与现代实践可比；假设单变量显著因素中的混杂因素已被多变量分析充分控制"
  unexpected_finding: "17 个因素在单变量分析中与生存相关，但只有 6 个在校正后保持独立——这种大幅缩减表明许多传统预后因素实际上是混杂因素"
  title_gap: "标题说 FMC 预后因素，但真正发现是因素层级：校正后只有 6 个独立因素——其他 11 个单变量显著因素可能与这 6 个相关而非独立预测"
  evidence_boundary: "1983 年研究——治疗方法和分期可能不反映当前实践；核心预后因素仍具基础价值但具体阈值可能需要更新"
---

# Prognostic Factors in Feline Mammary Carcinoma Get access Arrow

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. Landmark 1983 JNCI study: 202 FMC cats, 6 independent prognostic factors — tumor diameter, lymph nodes, mitotic index, necrosis, age, surgical completeness. Foundational for FMC prognosis. [Deep extraction worksheet](../../system/indexes/src-cancer-041-deep-extraction-round1.md).

## Source Check, 2026-06-01

PubMed abstract fetched as a zero-cost extraction step.

- PMID: 6572759
- Journal: Journal of the National Cancer Institute (JNCI)
- Year: 1983

## Abstract Summary

This landmark 1983 JNCI study evaluated prognostic factors in feline mammary carcinoma using prospective follow-up of 202 surgically treated cats.

**Study design:**
- Prospective follow-up study
- 202 cats treated by mastectomy and block dissection
- 35 factors analyzed (general, anamnestic, clinical, histologic, therapy data)
- Outcomes: survival, local recurrence

**Univariate significant factors:** 17 factors related to survival

**Independent prognostic factors (after correction):**

| Factor | Relationship |
|--------|--------------|
| Age | Independent predictor |
| Tumor diameter | Independent predictor |
| Tumor-positive lymph nodes (microscopic) | Independent predictor |
| Mitotic figures | Independent predictor |
| Tumor necrosis | Independent predictor |
| Completeness of surgical treatment | Independent predictor |

**Comparative oncology value:**
Authors evaluated FMC and canine mammary cancer as models for experimental therapy, comparing prognostic factors with human mammary cancer.

**Boundary:** 1983 study — treatment approaches and staging may not reflect current practice. Core prognostic factors remain foundational.

## One-Line Summary

Classic 1983 JNCI study: 6 independent prognostic factors in 202 FMC cases — tumor diameter, lymph nodes, mitotic figures, necrosis, age, surgical completeness.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Prognostic Factors in Feline Mammary Carcinoma Get access Arrow.
- The intake sheet locator is: https://academic.oup.com/jnci/article-abstract/70/4/709/938577?redirectedFrom=fulltext&login=false.

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
