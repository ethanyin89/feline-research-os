---
id: src-diabetes-018
type: source
title: "Endoneurial microvascular pathology in feline diabetic neuropathy"
source_kind: paper
species: feline
diseases: [diabetes mellitus]
models: []
endpoints: [neuropathy, microvascular-pathology]
jurisdictions: []
evidence_level: original-study
year: 2008
status: deep_extracted
verification_status: deep_extracted
extraction_depth: full
decision_grade: no
language_qa_status: not_applicable
tags: [diabetes, neuropathy, microvascular-pathology, complication]
links:
  doi: "10.1016/j.mvr.2007.12.002"
  url: "https://doi.org/10.1016/j.mvr.2007.12.002"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "PubMed/PMC abstract reports nerve biopsies from 12 diabetic cats and comparison nerves from 7 nondiabetic cats."
    - "PubMed/PMC abstract reports diabetic cats had elevated long-term glycemic markers, impaired motor nerve conduction, and decreased myelinated nerve fiber density."
    - "PubMed/PMC abstract reports capillary size and luminal area were significantly increased in diabetic cats."
    - "PubMed/PMC abstract reports a vasoconstriction index was significantly decreased."
  source_supported_conclusion:
    - "This is a complication-mechanism anchor for feline diabetic neuropathy."
    - "The abstract-level evidence compares 12 diabetic cats with 7 controls and links neuropathy to impaired motor conduction, reduced myelinated fiber density, and endoneurial vascular changes."
    - "This supports a microvascular/pathology branch, not treatment or reversibility claims."
    - "Complication pages should include tissue pathology, not only clinical signs."
    - "This source should be paired with src-diabetes-004 for the neuropathy branch."
  llm_inference:
    - "This is a full-text target if the module needs cause-versus-consequence separation or pathology-severity mapping."
  # V2 enhanced fields
  study_design: "横断面原始研究，采集12只糖尿病猫和7只非糖尿病猫的神经活检标本，采用神经传导速度测试与组织病理分析方法"
  core_argument: "猫糖尿病神经病变与运动神经传导受损、髓鞘神经纤维密度减少及内神经微血管病变密切相关"
  implicit_premise: "糖尿病猫体内的长期血糖控制水平可通过神经生理和组织病理特征反映神经病变情况"
  title_gap: "标题强调内神经微血管病变，但真正发现是这些病变与运动神经功能障碍及髓鞘纤维密度下降紧密联系，揭示了病理机制全貌"
  evidence_boundary: "本研究未评估糖尿病神经病变的治疗手段或病变的可逆性，也未探讨其他非微血管因素对病变的影响"
  unexpected_finding: "糖尿病猫内神经毛细血管直径和腔面积显著增大，然而血管收缩指数显著下降，提示复杂的血管反应机制"
---

# Endoneurial microvascular pathology in feline diabetic neuropathy

## One-Line Summary

Original microvascular pathology source for feline diabetic neuropathy.

## Why It Matters For Feline Diabetes

- provides a tissue-level complication branch beyond glycemic endpoints
- likely pairs with the neurological-complications source

## Key Findings

- first-pass metadata confirms this as a 2008 Microvascular Research article
- the study compared 12 diabetic cats with 7 controls
- accessible evidence reports impaired motor conduction and decreased myelinated fiber density in diabetic cats
- microvascular findings include increased capillary size/luminal area and decreased vasoconstriction index
- useful for neuropathy mechanism and complication framing
- the source deepens neuropathy from gait/nerve injury to endoneurial vascular pathology
- it strengthens the idea that diabetic complications deserve their own endpoint/mechanism branch

## Limits / Caveats

- full text not reviewed; this is an abstract-weighted extraction
- clinical translation and prevalence are not established by this card
- do not infer a treatment target or reversibility claim from pathology alone
- do not treat microvascular change as proven causal direction without full-text support

## Microvascular Complication Logic

This source gives the neuropathy branch tissue-level depth.

What can be promoted:

- diabetic cats had impaired motor nerve conduction
- diabetic cats had decreased myelinated nerve fiber density
- diabetic cats had endoneurial capillary/luminal changes
- vasoconstriction-index findings support a microvascular pathology branch

What should be held:

- treatment mechanism
- reversibility
- routine screening schedule
- causal direction
- prevalence in general diabetic-cat populations

## Relationship To Neurological Complication Source

This card should be paired with [src-diabetes-004](src-diabetes-004.md).

The safe split is:

- `src-diabetes-004` anchors clinical neuropathy and nerve injury
- `src-diabetes-018` anchors endoneurial microvascular pathology
- [diabetes neuropathy boundary memo](../../system/indexes/diabetes-neuropathy-boundary-memo.md) keeps both below treatment-claim level

## Write-Back Implications

- [mechanism overview](../../topics/diabetes/mechanism-overview.md) should include microvascular pathology as complication biology.
- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md) should keep neuropathy and pathology separate from glycemic-control endpoints.
- [synthesis index](../../topics/diabetes/synthesis-index.md) should preserve complications in the disease model.

## Full-Text Target If Needed

If later outputs need mechanism-depth claims, extract vascular measurement methods, lesion localization, controls, glycemic-marker associations, and any discussion of whether vascular change is cause, consequence, or amplifier. Until then, this card supports a pathology branch, not a treatment target or reversibility claim.

## Current Safe Role

Use this source when the module needs to show that diabetic neuropathy has tissue and vascular depth. It should deepen complication biology, but it should not be converted into a therapeutic target or screening recommendation without stronger source support. It also helps separate complication mechanisms from routine glycemic-control endpoints and keeps chronic diabetic injury visible beside remission-focused treatment narratives. This matters because a remission-centered module can otherwise underweight damage already present before control improves clinically.

## Open Follow-Up Questions

- what microvascular lesions were described?
- how do lesions relate to neurologic signs?
- is pathology reversible or progressive?

## Linked Entities

- diseases: diabetes mellitus
- models:
- endpoints: neuropathy, microvascular pathology
- mechanisms: endoneurial microvascular injury
- regulations:
