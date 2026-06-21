---
id: src-diabetes-021
type: source
title: "Diabetes mellitus in cats"
source_kind: paper
species: feline
diseases: [diabetes mellitus]
models: []
endpoints: [glycemic-control, remission]
jurisdictions: []
evidence_level: review
year: 2005
status: deep_extracted
verification_status: deep_extracted
extraction_depth: full
decision_grade: no
language_qa_status: not_applicable
tags: [diabetes, clinical-overview, review]
links:
  doi: "10.1016/j.cvsm.2004.10.001"
  url: "https://doi.org/10.1016/j.cvsm.2004.10.001"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "PubMed abstract frames feline diabetes as multifactorial, involving genetic and environmental factors."
    - "PubMed abstract names diet, excess body weight, and physical inactivity as pathogenesis factors."
    - "PubMed abstract describes type 2 diabetes as most common in cats."
    - "PubMed abstract says most cats are insulin-dependent at diagnosis."
    - "PubMed abstract links early good glycemic control with clinical remission in a substantial proportion of diabetic cats."
  source_supported_conclusion:
    - "This is an older broad clinical overview anchor."
    - "The review frames feline diabetes as multifactorial and usually type-2-like, with many cats insulin-dependent at diagnosis."
    - "It links early glycemic control with remission potential, but newer remission reviews should govern evidence strength."
    - "This source should bridge mechanism, recognition, and translation historically, not control current treatment ranking."
    - "Early-control/remission language should defer to src-diabetes-007 for evidence-boundary interpretation."
  llm_inference:
    - "Useful historical clinical overview beneath the 2014 broad overview and newer treatment sources."
  # V2 enhanced fields
  study_design: "综述性回顾，汇集多项猫糖尿病临床和流行病学研究，重点分析遗传与环境因素以及临床表现"
  core_argument: "猫糖尿病是一种多因素疾病，表现大多类似于2型糖尿病，且多数猫在确诊时已需依赖胰岛素治疗"
  implicit_premise: "多因素发病机制包括遗传背景和环境影响，且现有诊断和治疗手段能够准确区分和管理猫糖尿病类型"
  title_gap: "标题仅表明讨论猫糖尿病，但论文深入阐释了糖尿病的多因素发病机制及其与胰岛素依赖状态和早期血糖控制的临床相关性——揭示管理策略的重要性"
  evidence_boundary: "未具体回答最新糖尿病 remission 概念和新兴治疗方法对临床治疗效果的影响"
  unexpected_finding: "绝大多数猫确诊时已表现为胰岛素依赖状态，而非单纯类似人类2型糖尿病的非胰岛素依赖状态"
---

# Diabetes mellitus in cats

## One-Line Summary

Broad Veterinary Clinics review for feline diabetes clinical framing as of 2005.

## Why It Matters For Feline Diabetes

- useful historical clinical overview
- should be compared with the 2014 broad JFMS overview and newer treatment sources

## Key Findings

- first-pass metadata confirms this as a 2005 Veterinary Clinics review
- accessible evidence frames feline diabetes as multifactorial, involving genetic and environmental factors, diet, excess body weight, and inactivity
- type-2-like disease is described as the common form, although most cats may require insulin at diagnosis
- early glycemic control is linked with remission potential
- the source keeps multifactorial pathogenesis, weight/inactivity, insulin dependence, and remission potential together
- it should be read as clinical overview context, not modern protocol authority

## Limits / Caveats

- full text not reviewed; this is an abstract/summary-weighted extraction
- older treatment recommendations may be superseded
- do not use this source to rank current insulin/SGLT2/diet approaches
- do not treat early glycemic control as a precise remission predictor without the systematic review boundary

## Historical Clinical Overview Logic

What can be promoted:

- feline diabetes is multifactorial
- type-2-like disease is common
- many cats may be insulin-dependent at diagnosis
- diet, excess body weight, and inactivity belong in pathogenesis/risk architecture
- early glycemic control is remission-relevant

What should be held:

- current treatment hierarchy
- exact remission estimates
- dosing or monitoring protocol
- product/regulatory interpretation

## Write-Back Implications

- [risk and recognition](../../topics/diabetes/risk-and-recognition.md) should use this as older support for body weight and inactivity.
- [translation brief](../../topics/diabetes/translation-brief.md) should preserve early-control relevance without ranking protocols from this card.
- [synthesis index](../../topics/diabetes/synthesis-index.md) should keep it below newer clinical and remission owners.

## Full-Text Target If Needed

Extract diagnostic and monitoring language, early-control/remission definitions, and any recommendations that have or have not survived newer sources.

## Current Safe Role

Use this source as older broad clinical context. It keeps multifactorial disease, body weight, inactivity, insulin dependence, and early glycemic control in the same frame. It should not control current treatment or monitoring advice, but it helps show why Diabetes needs mechanism, recognition, endpoint, and translation pages together.

It is especially useful as a bridge between mechanism and management. Later cards refine remission, diet, insulin, and SGLT2 branches, but this older overview explains why those branches have to remain connected in one clinical disease module.
Use it for module shape and historical clinical context, then defer to newer narrow owners for exact boundaries.
That keeps the overview useful without letting older recommendations overrule updated remission, diet, insulin, monitoring, or SGLT2 control layers in current synthesis and output write-back. Treat it as bridge context for module shape, not current advice now directly.

## Open Follow-Up Questions

- what diagnosis and monitoring framework does it use?
- how does it frame remission?
- which recommendations remain current?

## Linked Entities

- diseases: diabetes mellitus
- models:
- endpoints: glycemic control, remission
- mechanisms:
- regulations:
