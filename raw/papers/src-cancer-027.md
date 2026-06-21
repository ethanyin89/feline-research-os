---
id: src-cancer-027
type: source
title: "Animal models for hormone-dependent human breast cancer. Relationship between steroid receptor profiles in canine and feline mammary tumors and survival rate"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 1984
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
pmid: 6690068
tags: [cancer, animal, models, hormone-dependent, human, breast, steroid, receptor, ER, PR, survival, prognosis]
links:
  doi: "10.1007/bf00255902"
  url: "https://doi.org/10.1007/bf00255902"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Canine and feline mammary tumors can be polyreceptive (ER, PR, androgen, glucocorticoid, mineralocorticoid)."
    - "Follow-up of 45 bitches with mammary carcinoma showed significantly higher survival in receptor-rich (ER and/or PR) tumors."
  source_supported_conclusion:
    - "Canine mammary tumors are suitable animal models for hormone-dependent human breast carcinoma."
    - "Receptor status correlates with survival in canine mammary carcinoma."
  llm_inference:
    - "Feline mammary tumors share polyreceptive characteristics with canine and human tumors."
    - "Historical foundation for receptor profiling in comparative mammary oncology."
  # V2 enhanced fields
  study_design: "原始研究（1984 年），犬猫乳腺肿瘤受体谱分析，45 只犬乳腺癌生存随访"
  core_argument: "犬猫乳腺肿瘤可为多受体型（ER、PR、雄激素、糖皮质激素、盐皮质激素）——受体丰富肿瘤生存率更高"
  implicit_premise: "假设犬类受体-生存关联可外推到猫；假设受体表达与激素依赖性治疗反应相关"
  unexpected_finding: "乳腺肿瘤不仅表达 ER/PR，还表达雄激素、糖皮质激素和盐皮质激素受体——多受体性超出传统激素受体关注范围"
  title_gap: "标题说激素依赖性乳腺癌的动物模型和受体谱与生存率，但真正发现是多受体性：犬猫乳腺肿瘤表达 5 种受体类型——这一复杂受体谱超出简单 ER/PR 分类"
  evidence_boundary: "1984 年研究，生存数据仅来自犬类队列（45 只）——猫特异性生存数据未在摘要中报告"
---

# Animal models for hormone-dependent human breast cancer

## Evidence-Depth Caveat

This card has deep extraction based on the abstract. 1984 comparative oncology: canine + feline mammary tumors are polyreceptive (ER, PR, androgen, glucocorticoid, mineralocorticoid). Receptor-rich tumors show better survival in 45-bitch canine cohort. Historical foundation for receptor-based prognosis. [Deep extraction worksheet](../../system/indexes/src-cancer-027-deep-extraction-round1.md).

## Source Check, 2026-06-02

| Field | Value |
|-------|-------|
| PMID | 6690068 |
| DOI | 10.1007/BF00255902 |
| Journal | Cancer Chemother Pharmacol |
| Year | 1984 |
| Authors | Martin PM, Cotard M, Mialot JP, André F, Raynaud JP |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Receptor types | ER, PR, androgen, glucocorticoid, mineralocorticoid in canine/feline mammary tumors |
| Study population | 45 bitches with mammary carcinoma (survival follow-up) |
| Prognostic finding | Receptor-rich (ER and/or PR) tumors had significantly higher survival |
| Model conclusion | Canine mammary tumors suitable for hormone-dependent breast cancer model |

**Boundary:** Abstract-level extraction. The 45-bitch cohort provides prognostic evidence for canine; feline receptor profiles mentioned but feline-specific survival data not reported in abstract.

## One-Line Summary

Historical 1984 study showing canine/feline mammary tumors are polyreceptive (ER, PR, androgen, glucocorticoid) with receptor-rich tumors showing better survival in canine cohort.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- Canine and feline mammary tumors can be polyreceptive
- Receptor types include: estrogen (ER), progestin (PR), androgen, glucocorticoid, mineralocorticoid
- 45 bitches with mammary carcinoma followed for survival analysis
- Survival rate significantly higher in animals with receptor-rich (ER and/or PR) tumors

### source_supported_conclusion

- Canine mammary tumors are suitable animal models for hormone-dependent human breast carcinoma
- Receptor status is prognostically significant in canine mammary cancer
- Both canine and feline mammary tumors share polyreceptive characteristics with human tumors

### llm_inference

- This 1984 study provides early foundation for receptor profiling in comparative mammary oncology
- The feline component is less detailed than canine but establishes shared receptor biology
- May inform mammary-carcinoma.md claims about receptor status and prognosis

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
