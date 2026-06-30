---
id: src-obesity-095
type: source
title: "Comparative Aspects of Human, Canine, and Feline Obesity and Factors Predicting Progression to Diabetes"
source_kind: paper
species: [feline, canine, human]
diseases: [obesity, diabetes]
models: [comparative_model]
endpoints: [diabetes_progression, risk_factors, comparative_medicine]
jurisdictions: []
evidence_level: review
year: 2014
status: deep_extracted
extraction_depth: partial
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [obesity, diabetes, comparative-medicine, progression, risk-factors]
links:
  doi: "10.3390/VETSCI1020121"
  url: "https://www.mdpi.com/2306-7381/1/2/121"
  local_assets:
    - "../../raw/deep-extractions/ext-src-diabetes-028.md"
evidence_policy:
  quoted_fact:
    - "Compares human, canine, and feline obesity and diabetes progression."
    - "Published in Veterinary Sciences 2014."
  source_supported_conclusion:
    - "Identifies factors predicting progression from obesity to diabetes."
    - "Cross-species comparison of metabolic disease."
  llm_inference:
    - "Canonical deep extraction is maintained under src-diabetes-028; this obesity card is a shared-source alias."
    - "Use for obesity module routing, but avoid duplicating independent evidence text."
  study_design: "共享别名卡；证据所有权归 canonical `src-diabetes-028`；综述比较人、犬、猫肥胖向糖尿病进展的机制。"
  core_argument: "肥胖相关胰岛素抵抗并不等同于糖尿病进展；猫的关键断点是β细胞代偿、肝糖输出调节和物种特异性机制是否失控。"
  implicit_premise: "跨物种机制不能线性外推；同一 DOI 的 obesity alias 只用于 obesity 模块路由，不应复制独立证据。"
  unexpected_finding: "肥胖猫可通过降低空腹和餐后内源性葡萄糖生成来抵消外周葡萄糖摄取下降，因此严重肥胖也可能维持正常空腹血糖。"
  title_gap: "标题像跨物种综述，真正价值是阻止把“肥胖/胰岛素抵抗”直接写成“糖尿病必然进展”。"
  evidence_boundary: "这是机制综述和共享别名，不是经过长期随访验证的个体预测模型；不能把候选机制当作临床预测指标。"
---

# Comparative Obesity and Diabetes Progression

## Evidence-Depth Caveat

Shared-source alias. The canonical deep extraction is linked through `src-diabetes-028` and the same local asset is attached here for obesity routing.

## One-Line Summary

2014 review comparing human, canine, and feline obesity-to-diabetes progression, emphasizing that insulin resistance alone is not a validated progression predictor.

## Why It Matters For Feline Obesity

Progression risk:
1. Separates obesity, insulin resistance, beta-cell failure, and hepatic glucose output
2. Preserves species differences between human, canine, and feline mechanisms
3. Supports obesity module routing without duplicating independent evidence text

## Related Sources

- src-diabetes-121: Cat as human model
- src-obesity-093: One Health perspective

## Linked Entities

- diseases: obesity, diabetes
- models: comparative_model
- mechanisms: diabetes_progression, insulin_resistance
