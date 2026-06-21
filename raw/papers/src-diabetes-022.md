---
id: src-diabetes-022
type: source
title: "Use of a high-protein diet in the management of feline diabetes mellitus"
source_kind: paper
species: feline
diseases: [diabetes mellitus]
models: []
endpoints: [glycemic-control]
jurisdictions: []
evidence_level: original-study
year: 2001
status: deep_extracted
verification_status: deep_extracted
extraction_depth: full
decision_grade: no
language_qa_status: not_applicable
tags: [diabetes, diet, high-protein, nutrition]
links:
  doi: ""
  url: "https://pubmed.ncbi.nlm.nih.gov/19746667/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "PubMed abstract describes adult diabetic cats transitioned from a high-fiber moderate-fat diet to a high-protein low-carbohydrate canned diet."
    - "PubMed abstract reports nine cats completed the study protocol."
    - "PubMed abstract reports insulin levels decreased in 8/9 cats after transition."
    - "PubMed abstract reports insulin injections were stopped in 3 cats."
    - "PubMed abstract reports regression analysis suggesting exogenous insulin could be reduced by more than 50% with no loss of fructosamine-based glucose control."
  source_supported_conclusion:
    - "This source belongs in the high-protein diet management branch."
    - "The abstract reports 9 cats completing transition from a high-fiber moderate-fat diet to a high-protein low-carbohydrate canned diet."
    - "Insulin dose decreased in 8/9 cats and injections stopped in 3 cats, but protein and carbohydrate effects are not isolated."
    - "The source supports diet effects on insulin requirement, not a universal remission protocol."
    - "It adds protein emphasis to the diet architecture but should stay bounded by small completed sample and combined high-protein/low-carbohydrate design."
  llm_inference:
    - "This is a high-priority full-text target if outputs need dropout, inclusion, or diet-composition detail."
  # V2 enhanced fields
  study_design: "前瞻性干预研究，9 只成年糖尿病猫从高纤维中脂肪饮食转为高蛋白低碳水化合物罐头饮食，监测胰岛素剂量及血糖控制指标变化"
  core_argument: "通过饮食调整为高蛋白低碳水化合物配方，绝大多数糖尿病猫的胰岛素需求显著降低，部分猫甚至可以停用胰岛素注射，而糖化果糖胺控制未受影响"
  implicit_premise: "高蛋白饮食对糖尿病猫的胰岛素敏感性提高及血糖控制有直接影响，而非其他未控变量所致"
  title_gap: "标题说使用高蛋白饮食管理糖尿病，但真正发现是高蛋白饮食显著减少了外源性胰岛素需求，提示饮食调整对治疗的潜在影响超出单纯辅助作用"
  evidence_boundary: "未区分蛋白质与碳水化合物各自独立对糖尿病控制的具体贡献，且样本量较小，未评估长期临床结局或不同疾病阶段适应性"
  unexpected_finding: "有三只猫在饮食调整后完全停用胰岛素注射，显示部分糖尿病猫能通过饮食控制实现胰岛素依赖性逆转"
---

# Use of a high-protein diet in the management of feline diabetes mellitus

## One-Line Summary

Veterinary Therapeutics source on high-protein diet use in feline diabetes management.

## Why It Matters For Feline Diabetes

- adds protein-focused diet evidence to the carbohydrate/fiber diet debate
- helps prevent diet architecture from becoming only low-carbohydrate versus high-fiber

## Key Findings

- NCBI metadata lists this as a 2001 Veterinary Therapeutics article
- DOI was not found in the first-pass metadata check
- 9 cats completed the protocol after transition to a high-protein low-carbohydrate canned diet
- insulin requirements decreased in 8/9 cats, and insulin injections were stopped in 3 cats
- abstract-level regression analysis suggested exogenous insulin could be reduced by more than 50% without loss of fructosamine-based glucose control
- this source expands diet architecture beyond low-carbohydrate versus high-fiber by adding a protein-emphasis branch
- it should be read as insulin-requirement reduction signal, not as proof of broad remission

## Limits / Caveats

- full text not reviewed; this is an abstract-weighted extraction
- only 9 cats completed the protocol
- protein emphasis and carbohydrate reduction are not isolated from each other
- the prior diet and new diet differ in multiple dimensions, so attribution must stay cautious
- do not generalize the insulin-reduction signal into a diet rule without full design details

## High-Protein Diet Logic

This source is useful because it makes diet architecture wider.

What can be promoted:

- a small completed sample transitioned to high-protein / low-carbohydrate canned diet
- insulin requirements decreased in most completing cats
- insulin injections stopped in some cats
- fructosamine-based control was not lost in the abstract-level signal

What should be held:

- broad generalizability
- isolated protein effect
- isolated carbohydrate effect
- remission protocol status
- diet hierarchy against `src-diabetes-015` without full-text comparison

## Relationship To Diet Architecture

This source should be paired with:

- [src-diabetes-006](src-diabetes-006.md), broad diet architecture
- [src-diabetes-015](src-diabetes-015.md), low-carbohydrate/low-fiber versus moderate-carbohydrate/high-fiber comparison
- [src-diabetes-016](src-diabetes-016.md), low-carbohydrate versus high-fiber review
- [src-diabetes-007](src-diabetes-007.md), remission boundary

The safe current read is:

`high-protein / low-carbohydrate diet may reduce insulin requirement in a small study, but protein and carbohydrate effects remain entangled`.

## Write-Back Implications

- [translation brief](../../topics/diabetes/translation-brief.md) should include a high-protein branch without turning it into a universal rule.
- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md) should separate insulin-dose reduction from remission.
- [synthesis index](../../topics/diabetes/synthesis-index.md) should keep protein, carbohydrate, fiber, and body-condition variables separate.

## Full-Text Target If Needed

Extract design type, dropout details, diet composition, insulin-adjustment rules, and fructosamine thresholds before using this source for protocol or hierarchy claims.

## Open Follow-Up Questions

- was the high-protein diet tested prospectively or retrospectively?
- what outcomes were measured?
- how does it relate to low-carbohydrate diet evidence?

## Linked Entities

- diseases: diabetes mellitus
- models:
- endpoints: glycemic control
- mechanisms: diet composition
- regulations:
