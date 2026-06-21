---
id: src-diabetes-004
type: source
title: "Neurological Complications Associated with Spontaneously Occurring Feline Diabetes Mellitus"
source_kind: paper
species: feline
diseases: [diabetes mellitus]
models: []
endpoints: [neuropathy]
jurisdictions: []
evidence_level: original-study
year: 2002
status: deep_extracted
verification_status: deep_extracted
extraction_depth: full
decision_grade: no
language_qa_status: not_applicable
tags: [diabetes, neuropathy, complication, pathology]
links:
  doi: "10.1093/jnen/61.10.872"
  url: "https://academic.oup.com/jnen/article-abstract/61/10/872/2916290"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Study compared 19 diabetic cats with 28 nondiabetic control cats."
    - "Assessment included physical examination, neurologic examination, electrophysiology, biochemical testing, and nerve/muscle biopsy."
    - "Diabetic cats demonstrated functional, structural, and biochemical nerve defects."
    - "Plantigrade posture was the most notable severe clinical impairment."
    - "Schwann-cell injury and demyelination were prevalent pathological findings."
    - "Axonal degeneration occurred in severe cases of diabetic neuropathy."
    - "Sensorimotor neuropathy underlies the plantigrade stance in diabetic cats."
  source_supported_conclusion:
    - "This 2002 original study provides pathology-grade evidence for diabetic neuropathy as a real complication in cats."
    - "The 19 vs 28 cohort comparison establishes case-control methodology for feline diabetic neuropathy."
    - "Plantigrade posture has electrophysiologic and histopathologic correlates, not just clinical observation."
    - "Nerve injury progresses from Schwann-cell damage through demyelination to axonal degeneration."
    - "Neuropathy should be represented as a tissue-level complication endpoint, not merely an owner-visible sign."
  llm_inference:
    - "This is a key source for complication visibility in the diabetes module."
    - "Plantigrade posture can serve as a clinical marker for underlying neuropathic damage."
    - "The progression from demyelination to axonal degeneration suggests early intervention may limit severity."
  # V2 enhanced fields
  study_design: "病例对照研究，比较19只糖尿病猫与28只非糖尿病对照猫，采用体格检查、神经学检查、电生理检测、生化分析及神经肌肉活检"
  core_argument: "自发性猫糖尿病会导致真实存在的神经病理性并发症，包括神经功能、结构及生化缺陷"
  implicit_premise: "糖尿病导致的神经病变能够通过临床、功能和组织学多层面方法准确识别和区别于非糖尿病猫的神经状态"
  title_gap: "标题聚焦神经并发症，但真正发现是通过电生理和组织病理证据确认了糖尿病神经病变的具体机制和表征——揭示了临床症状背后的细胞损伤过程"
  evidence_boundary: "未回答糖尿病神经并发症的具体治疗方法及长期临床预后，也未涉及糖尿病早期神经病变的预防策略"
  unexpected_finding: "跖行姿势作为最显著的临床表现，其背后对应着鞘细胞损伤和脱髓鞘病理变化，而不仅仅是简单的运动障碍"
---

# Neurological Complications Associated with Spontaneously Occurring Feline Diabetes Mellitus

## One-Line Summary

Original pathology-focused source for neurological complications in spontaneous feline diabetes.

## Why It Matters For Feline Diabetes

- keeps the module from becoming only a remission and glycemic-control story
- gives complication biology an early evidence anchor

## Key Findings

- first-pass metadata confirms this as a 2002 Journal of Neuropathology and Experimental Neurology article
- the study compared 19 diabetic cats with 28 nondiabetic cats
- diabetic cats with plantigrade posture were described as having sensorimotor neuropathy
- accessible pathology-level findings include Schwann-cell injury, demyelination, and severe axonal degeneration
- the source anchors neuropathy as real disease biology, not only a clinical observation
- it pairs naturally with `src-diabetes-018`, which adds endoneurial microvascular pathology

## Limits / Caveats

- full text not reviewed; this is an abstract/summary-weighted extraction
- clinical frequency, screening recommendations, and reversibility claims need fuller source-level extraction
- do not infer treatment response or reversibility from this card alone
- do not define routine screening for all diabetic cats without guideline/full-text support

## Neuropathy Complication Logic

This source prevents the diabetes module from becoming only remission, diet, and glycemic-control language.

What can be promoted:

- diabetic cats can have clinically visible sensorimotor neuropathy
- plantigrade posture is a severe clinical sign in the abstract-level framing
- neuropathy has electrophysiologic, structural, and biochemical correlates
- Schwann-cell injury, demyelination, and axonal degeneration belong in the complication map

What should be held:

- screening schedule
- reversibility after glycemic control
- treatment effect
- prevalence in routine diabetic populations
- direct severity staging

## Relationship To Microvascular Source

This card should be paired with [src-diabetes-018](src-diabetes-018.md).

The safe split is:

- `src-diabetes-004` anchors clinical/electrophysiologic/pathology neuropathy
- `src-diabetes-018` anchors endoneurial microvascular pathology
- [diabetes neuropathy boundary memo](../../system/indexes/diabetes-neuropathy-boundary-memo.md) keeps neuropathy as a complication and endpoint branch, not a treatment claim

## Write-Back Implications

- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md) should include neuropathy as a complication endpoint.
- [mechanism overview](../../topics/diabetes/mechanism-overview.md) should preserve nerve injury and pathology context.
- [synthesis index](../../topics/diabetes/synthesis-index.md) should keep complication biology visible beside remission and treatment.

## Full-Text Target If Needed

If later outputs need a neuropathy page, extract neurologic scoring, electrophysiologic measures, biopsy lesion categories, glycemic-marker relationships, and any statements about improvement after diabetes control. The current card supports complication reality and pathology depth; it does not yet support prognosis, screening cadence, or treatment response.

## Current Safe Role

Use this source when a diabetes answer is becoming too focused on remission or glucose numbers. It keeps chronic neurologic complication burden visible. It should not lead routine diagnosis, but it should prevent endpoint pages from ignoring clinically meaningful nerve injury and pathology.

## Open Follow-Up Questions

- what neurologic lesions were documented?
- how were clinical signs linked to pathology?
- what does the paper say about reversibility after glycemic control?

## Linked Entities

- diseases: diabetes mellitus
- models:
- endpoints: neuropathy
- mechanisms: microvascular injury
- regulations:
