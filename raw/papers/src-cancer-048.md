---
id: src-cancer-048
type: source
title: "Feline gastrointestinal lymphoma"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: review
year: 2003
status: ingested
extraction_depth: abstract
verification_status: abstract_weighted
pmid: 14552162
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, gastrointestinal, lymphoma]
links:
  doi: "10.1016/s0195-5616(03)00054-8"
  url: "https://www.sciencedirect.com/science/article/abs/pii/S0195561603000548?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Feline gastrointestinal lymphoma."
    - "The intake sheet locator is: https://www.sciencedirect.com/science/article/abs/pii/S0195561603000548?via%3Dihub."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
  # V2 enhanced fields
  study_design: "综述（2003 年 Vet Clin NA Small Animal Practice），猫胃肠道淋巴瘤的临床实践洞察"
  core_argument: "胃肠道淋巴瘤是老年猫厌食和体重下降的常见原因——低级别淋巴瘤对化疗反应优于高级别——化疗的初始反应是最重要的预后指标"
  implicit_premise: "假设 2003 年的低级别 vs 高级别分类标准仍有效；假设初始化疗反应可作为长期结局的可靠预测因子"
  unexpected_finding: "低级别胃肠道淋巴瘤可能比以前认为的更常见——这种认知转变改变了预后预期——且大多数猫是 FeLV 和 FIV 阴性"
  title_gap: "标题说猫胃肠道淋巴瘤，但真正发现是分级依赖性结局：低级别与高级别淋巴瘤的化疗反应差异巨大——同一诊断名称下预后可能截然不同"
  evidence_boundary: "2003 年综述；关于分子标记物的陈述可能已过时；治疗反应陈述是方向性的而非具体生存数据"
---

# Feline gastrointestinal lymphoma

## Evidence-Depth Caveat

This is an abstract-weighted source card. The abstract provides clinical practice insights but full-text is needed for detailed treatment protocols.

## Full Abstract (PubMed)

Gastrointestinal lymphoma is a common cause of anorexia and weight loss in older cats, with or without vomiting or diarrhea. Most cats are feline leukemia virus-negative and feline immunodeficiency virus-negative. Low-grade gastrointestinal lymphoma may be more common than previously thought, and these cats respond better to chemotherapy agents than cats with high-grade lymphoma. The most significant prognostic indicator is initial response to chemotherapy, with cats that survive the initial induction period generally achieving long-term remission. Thus far, investigations into molecular markers and immunophenotyping have failed to identify useful prognostic indicators.

## Key Extracted Findings

| Finding | Value | Boundary |
|---------|-------|----------|
| Common presentation | anorexia, weight loss ± vomiting/diarrhea in older cats | clinical presentation |
| Viral status | most cats FeLV-negative and FIV-negative | post-FeLV era context |
| Low-grade prevalence | may be more common than previously thought | 2003 perspective |
| Low-grade vs high-grade | low-grade responds better to chemo | treatment-relevant |
| Key prognostic factor | initial response to chemotherapy | strongest predictor |
| Long-term remission | cats surviving induction generally achieve | prognosis context |
| Molecular markers | have not identified useful prognostic indicators | 2003 limitation |

**Boundary:** This is a 2003 review. Statements about molecular markers may be outdated. Treatment response statements are directional, not numeric survival ranges.

## One-Line Summary

Candidate cancer source from sheet row 51. Use it for triage until abstract or full-text extraction proves a stronger role.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Feline gastrointestinal lymphoma.
- The intake sheet locator is: https://www.sciencedirect.com/science/article/abs/pii/S0195561603000548?via%3Dihub.

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
