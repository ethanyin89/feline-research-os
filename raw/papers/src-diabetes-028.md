---
id: src-diabetes-028
type: source
title: "Comparative Aspects of Human, Canine, and Feline Obesity and Factors Predicting Progression to Diabetes"
source_kind: paper
species: [feline, canine, human]
diseases: [diabetes mellitus, obesity]
models: [comparative_model, obesity_progression_model]
endpoints: [insulin_resistance, beta_cell_compensation, endogenous_glucose_production, adipokines, inflammation_markers]
jurisdictions: []
evidence_level: review
year: 2014
status: deep_extracted
extraction_depth: partial
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [diabetes, obesity, comparative-medicine, insulin-resistance, beta-cell-function, hepatic-glucose-output]
links:
  doi: "10.3390/vetsci1020121"
  url: "https://www.mdpi.com/2306-7381/1/2/121"
  local_assets:
    - "../../raw/deep-extractions/ext-src-diabetes-028.md"
evidence_policy:
  quoted_fact:
    - "Obesity is a clear type 2 diabetes risk factor in humans and cats, while canine evidence is less complete."
    - "More than 80% of obese insulin-resistant people maintain normal glucose and do not progress to type 2 diabetes."
    - "In a feline longitudinal obesity study, 20 cats developed obesity with up to 100% fat-mass increase while fasting glucose remained normal."
    - "In obese cats, endogenous glucose production is reduced in fasting and postprandial states, offsetting reduced peripheral glucose uptake."
  source_supported_conclusion:
    - "Insulin resistance alone is not sufficient to predict diabetes progression; beta-cell compensation or failure is the decisive gate."
    - "Feline obesity can be metabolically abnormal without producing a simple fasting-glucose gradient."
    - "Hepatic glucose output, beta-cell reserve, adipokines, and species-specific inflammation patterns should be separated in progression models."
  llm_inference:
    - "For feline obesity-to-diabetes modeling, use this source as a mechanism architecture review, not as a validated individual prediction tool."
  study_design: "综述，比较人、犬、猫肥胖向糖尿病进展的机制线索，重点讨论胰岛素分泌、肝脏内源性葡萄糖生成和炎症/脂肪因子差异"
  core_argument: "肥胖造成胰岛素抵抗，但人、犬、猫都可能长期代偿；真正决定肥胖是否进展为糖尿病的关键不是肥胖本身，而是β细胞代偿失败、肝糖输出失控和物种特异性机制共同出现。"
  implicit_premise: "肥胖、胰岛素抵抗、β细胞功能、肝糖输出和炎症反应在不同物种中不能被视为同一条线性路径，必须分别验证。"
  unexpected_finding: "肥胖猫可以通过降低空腹和餐后内源性葡萄糖生成来抵消外周葡萄糖摄取下降，因此即使严重肥胖也可能维持正常空腹血糖。"
  title_gap: "标题看似是跨物种肥胖综述，但真正价值是纠正“胰岛素抵抗等于糖尿病进展”的直觉，并提出β细胞和肝糖输出才是预测进展的核心断点。"
  evidence_boundary: "本文是机制综述，不提供经过长期、多中心随访验证的犬猫个体糖尿病进展预测模型；不能把候选机制直接写成已验证预测指标。"
---

# Comparative Aspects of Human, Canine, and Feline Obesity and Factors Predicting Progression to Diabetes

## Evidence-Depth Caveat

This card is linked to a desktop deep extraction of the 2014 review. Use it for mechanism architecture and cross-species progression framing, not as a validated individual prediction model.

## Source Check, 2026-05-14

Crossref metadata was checked as a repeatable second-pass intake step.

- DOI metadata resolved: yes
- Container: Veterinary Sciences
- Year: 2014
- Abstract available in Crossref: yes

Deep extraction artifact:

- [ext-src-diabetes-028](../deep-extractions/ext-src-diabetes-028.md)

## One-Line Summary

Cross-species review showing that obesity-related insulin resistance does not by itself predict diabetes progression; beta-cell reserve and hepatic glucose output determine whether compensation fails.

## Why It Matters For Feline Diabetes

This source is a useful bridge between feline obesity and diabetes because it separates three layers that are often collapsed:

- obesity and insulin resistance
- beta-cell compensation or failure
- hepatic endogenous glucose production

## Key Findings

### quoted_fact

- Obesity is a clear diabetes risk factor in humans and cats; canine evidence is less complete.
- More than 80% of obese insulin-resistant people remain normoglycemic.
- A 20-cat feline obesity study found fasting glucose remained normal even as fat mass increased up to 100%.
- Obese cats can lower endogenous glucose production in fasting and postprandial states.

### source_supported_conclusion

- Insulin resistance alone should not be used as a progression predictor.
- Feline obesity-to-diabetes progression should be framed as insulin resistance plus beta-cell and hepatic compensation failure.
- Species differences matter; human obesity inflammation pathways should not be imported into cats without feline evidence.

### llm_inference

- This source can support mechanism architecture and endpoint selection, but not an individual clinical risk calculator.

## Claim-Fit Judgment

Strongest safe use:

- obesity-to-diabetes mechanism architecture
- cross-species comparison boundaries
- endpoint selection for insulin resistance, beta-cell reserve, hepatic glucose output, adipokines, and inflammation

Must not control yet:

- reader-facing medical advice
- guideline-like recommendations
- individual progression prediction
- claims that obesity alone predicts diabetes

## Image Asset TODO

- figures/tables to capture: EGP, insulin secretion, adipokine, and inflammation comparison figures if local full-text assets are added later
- why these matter: they would allow claim-specific original paragraph/figure trace beyond the current deep extract

## Open Follow-Up Questions

- Can the MDPI page be mapped to stable section anchors for one-click paragraph jumps?
- Should `src-obesity-095` remain as an alias or be retired in favor of `src-diabetes-028`?
- Which topic pages currently cite obesity progression without beta-cell/hepatic compensation boundaries?

## Linked Entities

- diseases: diabetes mellitus, obesity
- models: comparative model, obesity progression model
- endpoints: insulin resistance, beta-cell compensation, endogenous glucose production, adipokines, inflammation markers
- mechanisms: beta-cell compensation failure, hepatic glucose output, species-specific inflammation
