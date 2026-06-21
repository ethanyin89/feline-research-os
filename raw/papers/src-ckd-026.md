---
id: src-ckd-026
type: source
title: "Serum fibroblast growth factor 23 (FGF-23): associations with hyperphosphatemia and clinical staging of feline chronic kidney disease"
source_kind: paper
species: feline
diseases: [CKD]
models: []
endpoints: [FGF-23, phosphorus, iPTH, CKD staging]
jurisdictions: []
evidence_level: original-study
year: 2021
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ckd, serum, fibroblast, growth, factor, fgf-23, associations, hyperphosphatemia, biomarker, staging, phosphorus, iPTH]
links:
  doi: "10.1177/1040638720985563"
  url: "https://doi.org/10.1177/1040638720985563"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "FGF-23 was higher in cats in all CKD stages than in controls."
    - "Higher serum phosphorus was observed in stage 3 (p = 0.04) and stage 4 (p < 0.01) compared to controls."
    - "No statistical difference was found in FGF-23 among age groups (p = 0.15) or by sex in healthy subjects."
    - "Pearson analysis indicated a positive linear relationship between FGF-23 and iPTH (control: r = 0.70, p < 0.01; CKD: r = 0.46, p = 0.02)."
  source_supported_conclusion:
    - "FGF-23 elevates earlier than hyperphosphatemia across CKD stages; hyperphosphatemia only appeared in stage 3-4."
    - "FGF-23 may be a useful biomarker of feline CKD and may precede hyperphosphatemia in advanced feline CKD."
    - "Age does not independently affect FGF-23 in healthy cats, reducing age-related confounding concerns."
  llm_inference:
    - "FGF-23 may serve as an earlier-stage biomarker than serum phosphorus for CKD monitoring."
    - "Cross-sectional design cannot establish temporal precedence; association does not prove prediction."
  # V2 enhanced fields
  study_design: "横断面研究，304 只猫（196 只 CKD 按 IRIS 分期、108 只健康对照），ELISA 检测血清 FGF-23 和 iPTH"
  core_argument: "FGF-23 在所有 CKD 分期均升高且早于高磷血症出现——高磷血症仅在 3-4 期出现，而 FGF-23 在 1-2 期已升高"
  implicit_premise: "假设横断面关联反映纵向时间顺序；假设 ELISA 检测在猫中经过验证"
  unexpected_finding: "健康猫中 FGF-23 与年龄无关（p=0.15）——减少了年龄相关混杂的担忧"
  title_gap: "标题说 FGF-23 与高磷和分期的关联，但真正发现是时间顺序提示：FGF-23 在所有分期均升高而高磷仅在 3-4 期——FGF-23 可能是比血磷更早的标志物"
  evidence_boundary: "横断面设计不能建立时间先后顺序；不能提供 FGF-23 诊断阈值或治疗决策指导；单中心研究"
---

# Serum fibroblast growth factor 23 (FGF-23): associations with hyperphosphatemia and clinical staging of feline chronic kidney disease

## Evidence-Depth Status

Full abstract extraction completed 2026-06-05. This card now supports module-level CKD biomarker and staging claims.

## Study Design

- Cross-sectional study
- 304 cats: 196 CKD (staged by IRIS), 108 healthy controls
- CKD stages: 34 stage 1, 74 stage 2, 51 stage 3, 37 stage 4
- Controls stratified by age: 0-2y, 3-6y, 7-10y, 11-14y, ≥15y
- Measurements: serum FGF-23 and intact PTH (iPTH) by ELISA

## One-Line Summary

FGF-23 elevates in all CKD stages before hyperphosphatemia appears, suggesting potential as an earlier biomarker than serum phosphorus.

## Why It Matters For Feline Ckd

This source was included in a reviewed feline literature intake sheet and classified as `new-ckd` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- "FGF-23 was higher in cats in all CKD stages than in controls."
- "Higher serum phosphorus was observed in stage 3 (p = 0.04) and stage 4 (p < 0.01) compared to controls."
- "No statistical difference was found in FGF-23 among age groups (p = 0.15) or by sex in healthy subjects."
- "Pearson analysis indicated a positive linear relationship between FGF-23 and iPTH (control: r = 0.70, p < 0.01; CKD: r = 0.46, p = 0.02)."
- "FGF-23 may be a useful biomarker of feline CKD and may precede hyperphosphatemia in advanced feline CKD."

### source_supported_conclusion

- FGF-23 elevates earlier than hyperphosphatemia across CKD stages; hyperphosphatemia only appeared in stage 3-4.
- Age does not independently affect FGF-23 in healthy cats, reducing age-related confounding concerns.
- FGF-23 and iPTH are positively correlated in both healthy and CKD cats.

### llm_inference

- FGF-23 may serve as an earlier-stage biomarker than serum phosphorus for CKD monitoring.
- Cross-sectional design cannot establish temporal precedence; association does not prove prediction.

## Claim-Fit Judgment

Strongest safe use:

- FGF-23 as an early-stage CKD biomarker candidate
- FGF-23 and phosphorus staging interaction evidence
- FGF-23 and iPTH correlation evidence
- Age-independence of FGF-23 in healthy cats

Must not control yet:

- Universal FGF-23 cutoff recommendations
- FGF-23 as a treatment decision driver
- Progression prediction claims (cross-sectional design limitation)
- Single-center generalizability

## Image Asset TODO

- figures to capture: unknown until source text is read
- why these matter: tables or figures should remain behind the candidate gate until labels are verified

## Open Follow-Up Questions

- What source family is confirmed by the abstract or article body?
- Which claims, if any, are reusable for the ckd module?
- Does this source deserve deep extraction, or should it remain queue context?
- Are there tables or figures that change the module structure?

## Linked Entities

- diseases: CKD
- models:
- endpoints:
- mechanisms:
- regulations:
