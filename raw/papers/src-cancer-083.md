---
id: src-cancer-083
type: source
title: "Early Detection, Aggressive Therapy: Optimizing the Management of Feline Mammary Masses"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: review
year: 2010
status: ingested
extraction_depth: abstract
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
pmid: 20193912
tags: [cancer, mammary, management, review, surgery, prognosis, fibroadenomatous-hyperplasia]
links:
  doi: "10.1016/j.jfms.2010.01.004"
  url: "https://doi.org/10.1016/j.jfms.2010.01.004"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Approximately 80% of feline mammary masses are malignant."
    - "Adenocarcinoma is the most common tumor type."
    - "Surgery is the most widely used treatment for malignant tumors."
    - "OVH or hormonal therapy are treatments of choice for fibroadenomatous hyperplasia."
  source_supported_conclusion:
    - "Early diagnosis is essential to improve prognosis and quality of life."
    - "Surgery routinely does not provide a cure for advanced/metastatic disease."
  llm_inference:
    - "Review article for mammary-carcinoma.md management section."
    - "80% malignancy rate is key clinical reference."
  # V2 enhanced fields
  study_design: "综述文章（2010 年 JFMS），猫乳腺肿块的临床管理综述——早期检测和积极治疗策略"
  core_argument: "约 80% 的猫乳腺肿块是恶性的——腺癌是最常见类型——手术是最广泛使用的治疗——但诊断时往往已晚期/转移——早期诊断对改善预后和生活质量至关重要"
  implicit_premise: "假设 80% 恶性率适用于所有临床情境（可能受转诊偏倚影响）；假设早期检测可改善结局（因果关系假设）"
  unexpected_finding: "手术通常无法治愈晚期/转移性疾病——这强调了早期检测的重要性——但也提示需要辅助治疗策略"
  title_gap: "标题说早期检测和积极治疗以优化猫乳腺肿块管理，但真正信息是临床现实：80% 恶性 + 诊断时往往晚期 = 预后有限——纤维腺瘤样增生（最常见良性肿块）可用 OVH/激素治疗"
  evidence_boundary: "综述文章证据；支持临床管理概述和 80% 恶性率声明，不支持具体治疗方案或生存估计——需要原始研究支持"
---

# Early Detection, Aggressive Therapy: Optimizing the Management of Feline Mammary Masses

## Source Check, 2026-06-03

| Field | Value |
|-------|-------|
| PMID | 20193912 |
| DOI | 10.1016/j.jfms.2010.01.004 |
| Journal | J Feline Med Surg |
| Year | 2010 |
| Authors | Giménez F, Hecht S, Craig LE, Legendre AM |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Malignancy rate | ~80% of feline mammary masses are malignant |
| Common type | Adenocarcinoma |
| Treatment | Surgery most widely used |
| Prognosis | Often advanced/metastatic at diagnosis; surgery rarely curative |
| Benign masses | Fibroadenomatous hyperplasia treated with OVH/hormonal therapy |

**Boundary:** Abstract-level extraction. Review article providing clinical management overview.

## One-Line Summary

JFMS review: 80% of feline mammary masses are malignant (adenocarcinoma most common); surgery is standard but rarely curative for advanced disease.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- Approximately 80% of feline mammary masses are malignant
- Adenocarcinoma is the most common tumor type
- Surgery is the most widely used treatment for malignant tumors
- Tumors are often advanced with metastasis at diagnosis
- OVH or hormonal therapy are treatments of choice for fibroadenomatous hyperplasia

### source_supported_conclusion

- Early diagnosis is essential to improve prognosis and quality of life
- Surgery routinely does not provide cure for advanced disease
- Fibroadenomatous hyperplasia (most common benign mass) responds to OVH/hormonal therapy

### llm_inference

- High-value review for mammary-carcinoma.md management section
- 80% malignancy rate is widely cited clinical reference
- Supports aggressive surgical approach recommendations

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
