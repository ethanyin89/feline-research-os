---
id: src-diabetes-119
type: source
title: "Feline comorbidities: Pathophysiology and management of the obese diabetic cat"
source_kind: paper
species: feline
diseases: [diabetes, obesity]
models: []
endpoints: [comorbidity, management, pathophysiology]
jurisdictions: []
evidence_level: review
year: 2021
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
pmid: "34167340"
tags: [diabetes, obesity, comorbidity, management, obese-diabetic]
links:
  doi: "10.1177/1098612X211021540"
  url: "https://pubmed.ncbi.nlm.nih.gov/34167340/"
  local_assets:
    - "../../raw/deep-extractions/ext-src-diabetes-005.md"
evidence_policy:
  quoted_fact:
    - "Published in JFMS 2021, Volume 23, Issue 7, pp 639-648."
    - "Authors: Clark M, Hoenig M."
  source_supported_conclusion:
    - "Reviews pathophysiology of obesity-diabetes comorbidity in cats."
    - "Provides management strategies for obese diabetic cats."
  llm_inference:
    - "Canonical diabetes source remains src-diabetes-005; this card is a later intake duplicate alias linked to the same deep extraction."
    - "Do not duplicate independent evidence text across src-diabetes-005 and src-diabetes-119."
  study_design: "重复别名卡；证据所有权归 canonical `src-diabetes-005`；该综述整合肥胖糖尿病猫的病理生理和管理策略。"
  core_argument: "肥胖通过多机制推动胰岛素抵抗，但肥胖糖尿病猫的管理不能机械先减重；若就诊时已有主动体重下降或肌肉流失，应先稳糖和稳体重，再进入可控减重。"
  implicit_premise: "同一 DOI 的多张卡必须共享同一证据源；别名卡只负责路由和防重复，不应生成独立证据文本。"
  title_gap: "标题看似是肥胖糖尿病共病综述，真正可转化价值是管理顺序：控糖、保肌肉、稳定后再减重。"
  evidence_boundary: "别名卡不独立扩展证据；具体低碳水、高蛋白、减重速度和药物策略仍以 canonical source 与原始研究为准。"
  unexpected_finding: "肥胖糖尿病猫并不总是适合立即热量限制，因为不少猫就诊时已经出现疾病相关体重和肌肉下降。"
---

# Obese Diabetic Cat Management

## Evidence-Depth Caveat

Duplicate-alias card. The canonical diabetes source remains `src-diabetes-005`; this card is linked to the same deep extraction so later intake rows do not re-open a duplicate source.

## One-Line Summary

2021 JFMS review covering pathophysiology and management of the obese diabetic cat, including the management sequence of glycemic stabilization before caloric restriction when active disease-related weight loss is present.

## Why It Matters For Feline Diabetes/Obesity

Comorbidity intersection:
1. Obesity is major risk factor for feline diabetes
2. Management strategies differ for dual-condition cats
3. Weight loss must be sequenced around current glycemic control, body weight trend, and muscle condition

## Related Sources

- src-diabetes-005: canonical source card and evidence owner
- src-diabetes-001: diabetes pathogenesis
- src-obesity-001: obesity pathophysiology

## Linked Entities

- diseases: diabetes, obesity
- endpoints: comorbidity, management
- mechanisms: insulin_resistance, weight_management
