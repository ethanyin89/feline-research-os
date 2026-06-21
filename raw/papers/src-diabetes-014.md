---
id: src-diabetes-014
type: source
title: "Feline Diabetes mellitus"
source_kind: paper
species: feline
diseases: [diabetes mellitus]
models: []
endpoints: [glycemic-control, remission]
jurisdictions: []
evidence_level: review
year: 2014
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [diabetes, clinical-overview, review]
links:
  doi: "10.1177/1098612X14523187"
  url: "https://doi.org/10.1177/1098612X14523187"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Crossref abstract reports an approximate frequency of 1 in 200 cats."
    - "Crossref abstract frames most feline diabetes as type 2 diabetes mellitus."
    - "Crossref abstract describes type-2-like feline diabetes as peripheral insulin resistance plus progressive reduction in insulin production."
    - "Crossref abstract lists diet, insulin type, insulin dose, monitoring method, monitoring intensity, and concomitant therapy as management decisions."
    - "Crossref abstract keeps diabetic ketoacidosis, complications, and concurrent diseases in scope."
  source_supported_conclusion:
    - "This is a broad clinical overview anchor for the diabetes module."
    - "The source supports modeling feline diabetes as a clinical decision system spanning diet, insulin, monitoring, complications, and concurrent disease."
    - "The source supports remission as a goal while keeping ketoacidosis, complications, and comorbidity in scope."
    - "This card should route general diabetes questions into workup architecture rather than directly into treatment ranking."
    - "The default type-2-like frame should remain bounded by secondary endocrine, pancreatitis, and complicated-patient branches."
  llm_inference:
    - "This should anchor the first clinical architecture write-back, but not detailed protocol ranking."
    - "This is a high-priority full-text target if later outputs need diagnostic or monitoring schedules."
  # V2 enhanced fields
  study_design: "综述性研究，综合分析多个文献，涵盖猫糖尿病的诊断、治疗、监测及预后管理"
  core_argument: "猫糖尿病主要表现为类似人类2型糖尿病的周围胰岛素抵抗及胰岛素分泌逐渐减少，综合饮食调整、胰岛素使用、监测及并发症处理是有效管理的关键。"
  implicit_premise: "猫糖尿病的临床表现和治疗原则可通过类似人类2型糖尿病的病理机制进行统一框架构建和管理。"
  title_gap: "标题只是指出猫糖尿病，但实际综述提供了一个涵盖诊断、治疗、监测、并发症及共病处理的临床决策系统框架——超出了单纯疾病介绍的范畴。"
  evidence_boundary: "本文未深入探讨糖尿病特异性分子机制、基因易感性及新型治疗方案的临床试验效果，亦未细化不同种族或年龄猫群的个体差异。"
  unexpected_finding: "糖尿病酮症酸中毒及共病虽通常视为严重并发症，但该综述强调在管理目标中持续保持对这些风险的监控同样重要，促进全面治疗策略的制定。"
---

# Feline Diabetes mellitus

## One-Line Summary

Broad clinical overview source for feline diabetes diagnosis, treatment, monitoring, and prognosis framing.

## Why It Matters For Feline Diabetes

- should help set the first clinical spine before narrow treatment or diet studies are promoted
- likely useful for routing owner-facing questions into mechanism, diagnosis, monitoring, and treatment branches

## Key Findings

- abstract-level extraction supports this as a broad clinical overview anchor
- abstract frames diabetes as common in practice and usually type-2-like
- abstract identifies management decisions around diet, insulin type and dose, monitoring method and intensity, and concomitant therapy
- abstract keeps diabetic ketoacidosis, complications, and concurrent disease in scope
- the source's reusable value is the decision-system frame: diagnosis may be straightforward, but management is multi-variable
- remission can remain visible, but complicated cases and concurrent disease prevent the module from becoming remission-only

## Limits / Caveats

- extraction is abstract-weighted, not full-text
- do not promote exact insulin protocols, monitoring schedules, or remission rates from this card
- do not use this overview to erase secondary-endocrine diabetes, pancreatitis/DKA complexity, or SGLT2 label-specific candidacy rules
- do not turn management decision categories into patient-specific clinical instructions

## Clinical Architecture Logic

This source is the broad clinical routing anchor. It should answer where a general feline diabetes question enters the wiki, not which protocol wins.

What can be promoted:

- feline diabetes is common enough in practice to deserve a full module
- most cats can be framed as type-2-like by default
- type-2-like disease combines insulin resistance and progressive insulin-production decline
- clinical management includes diet, insulin, monitoring, concomitant therapy, complications, and concurrent disease
- remission can be a goal for many newly diagnosed cats, but complicated branches remain in scope

What should be held:

- exact diagnostic criteria
- insulin dose or schedule
- monitoring frequency
- remission-rate claims
- treatment hierarchy or product preference
- any claim that default type-2-like framing is universal

## Workup Routing

The [diabetes diagnostic monitoring workup memo](../../system/indexes/diabetes-diagnostic-monitoring-workup-memo.md) is the smallest durable owner for this source's architecture.

This card supports a six-gate workup map:

- diagnosis confirmation and baseline clinical context
- body-condition and presentation state
- secondary-endocrine suspicion
- pancreatitis / DKA complexity
- treatment candidacy
- monitoring intensity and endpoint selection

## Write-Back Implications

- [risk and recognition](../../topics/diabetes/risk-and-recognition.md) should use this source for common-disease and default type-2-like framing.
- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md) should keep monitoring strategy as an endpoint-family issue.
- [translation brief](../../topics/diabetes/translation-brief.md) should structure treatment around decisions and constraints, not one ladder.
- [synthesis index](../../topics/diabetes/synthesis-index.md) should keep clinical complexity visible beside remission potential.

## Open Follow-Up Questions

- what diagnostic and monitoring hierarchy does it recommend?
- how does it discuss remission?
- what insulin and diet guidance does it give?

## Linked Entities

- diseases: diabetes mellitus
- models:
- endpoints: glycemic control, remission
- mechanisms:
- regulations:
