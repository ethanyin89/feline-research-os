---
id: src-ckd-034
type: source
title: "Risk and protective factors for cats with naturally occurring chronic kidney disease"
source_kind: paper
species: feline
diseases: [CKD]
models: []
endpoints: [CKD risk, diet, lifestyle, water source]
jurisdictions: []
evidence_level: original-study
year: 2017
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ckd, risk, protective, factors, diet, dry-food, lifestyle, water, case-control, epidemiology]
links:
  doi: "10.1177/1098612x15625453"
  url: "https://doi.org/10.1177/1098612x15625453"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Male sex, tap water, and outdoor lifestyle were associated with increased CKD risk."
    - "Commercial dry cat food, filtered water, and indoor lifestyle were associated with decreased risk."
    - "Logistic regression demonstrated cats fed commercial dry cat food had significantly decreased CKD risk compared with other diets."
    - "Multivariable analysis found only feeding commercial dry cat food to be significant."
  source_supported_conclusion:
    - "Commercial dry cat food may be a potential protective factor for CKD in cats (authors' conclusion)."
    - "Male sex, tap water, and outdoor lifestyle are univariable risk factors that did not survive multivariable adjustment."
    - "Diet is a modifiable factor that deserves further investigation in CKD prevention."
  llm_inference:
    - "Case-control design with retrospective questionnaire limits causal inference."
    - "Commercial dry cat food is a heterogeneous category; formulation details unknown."
  # V2 enhanced fields
  study_design: "年龄匹配病例对照研究，130 只猫（101 只 CKD、29 只健康对照 ≥5 岁），问卷访谈收集饮食和生活方式数据，泰国曼谷"
  core_argument: "商业干猫粮是多变量分析中唯一保持显著性的潜在 CKD 保护因素——男性、自来水和户外生活方式在单变量中显著但未通过多变量调整"
  implicit_premise: "假设回顾性问卷可准确捕捉长期饮食史；假设干猫粮作为类别是同质的"
  unexpected_finding: "干猫粮作为保护因素与传统高水分饮食建议相矛盾——可能反映配方质量而非水分含量"
  title_gap: "标题说风险和保护因素，但真正发现是反直觉的：商业干猫粮是多变量分析中唯一显著的保护因素——与传统高水分饮食建议相矛盾，提示配方质量可能比水分含量更重要"
  evidence_boundary: "病例对照设计不能建立因果关系；对照组小（n=29）；泰国单中心可能不适用于其他人群；干猫粮的具体配方（蛋白质、磷、水分）未知"
---

# Risk and protective factors for cats with naturally occurring chronic kidney disease

## Evidence-Depth Status

Full abstract extraction completed 2026-06-05. This card now supports module-level CKD risk factor architecture claims.

## Study Design

- Age-matched case-control study
- 130 cats: 101 CKD, 29 clinically normal controls (aged ≥5 years)
- Data collection: questionnaire interviews, June 2004 to November 2014
- Location: Bangkok Metropolitan area (Thailand)
- Analysis: univariable and multivariable logistic regression with backward elimination

## One-Line Summary

Commercial dry cat food was the only factor that remained significant in multivariable analysis as a potential protective factor for CKD.

## Why It Matters For Feline Ckd

This source was included in a reviewed feline literature intake sheet and classified as `new-ckd` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- "Male sex, tap water, and outdoor lifestyle were associated with increased CKD risk."
- "Commercial dry cat food, filtered water, and indoor lifestyle were associated with decreased risk."
- "Logistic regression demonstrated cats fed commercial dry cat food had significantly decreased CKD risk compared with other diets."
- "Multivariable analysis found only feeding commercial dry cat food to be significant."

### source_supported_conclusion

- Commercial dry cat food may be a potential protective factor for CKD in cats.
- Male sex, tap water, and outdoor lifestyle are univariable risk factors that did not survive multivariable adjustment.
- Diet is a modifiable factor that deserves further investigation in CKD prevention.

### llm_inference

- Case-control design with retrospective questionnaire limits causal inference.
- Commercial dry cat food is a heterogeneous category; specific formulation details (protein, phosphorus, moisture) are unknown.
- Small control group (n=29) limits statistical power and precision.

## Claim-Fit Judgment

Strongest safe use:

- Risk factor architecture framing: male sex, outdoor lifestyle, tap water as univariable signals
- Diet as a modifiable factor hypothesis
- Evidence that dietary factors deserve further investigation in CKD prevention
- Lifestyle and environmental factor exploration

Must not control yet:

- Universal dry food recommendation (confounding not fully resolved)
- Causal claims about specific dietary interventions
- Risk ranking without replication in other populations
- Prevention protocol recommendations

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
