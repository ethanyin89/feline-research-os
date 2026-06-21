---
id: src-ibd-017
type: source
title: "Fecal S100A12 concentrations in cats with chronic enteropathies"
source_kind: paper
species: feline
diseases: [IBD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2023
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ibd, fecal-marker, chronic-enteropathy]
links:
  doi: "10.1177/1098612X231164273"
  url: "https://journals.sagepub.com/doi/10.1177/1098612X231164273"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The abstract reports 49 cats with chronic enteropathy and 19 healthy control cats.
    - The abstract states that 19 CE cats were diagnosed with IBD or chronic inflammatory enteropathy and 30 were diagnosed with alimentary lymphoma.
    - The abstract reports fecal S100A12 concentrations differed between lymphoma and control cats and between IBD and control cats.
    - The abstract reports no significant difference in fecal S100A12 concentrations between IBD and lymphoma.
  source_supported_conclusion:
    - This source belongs in the support-marker branch of chronic enteropathy and IBD endpoint architecture.
    - The study supports fecal S100A12 as a disease-versus-health inflammatory marker, not as an IBD-versus-lymphoma separator.
  llm_inference:
    - This paper is best modeled below metabolomics and below core workup, but above purely speculative markers because it is noninvasive and disease-associated.
  # V2 enhanced fields
  study_design: "前瞻性病例对照研究，纳入49只慢性肠病猫（其中19只诊断为炎症性肠病或慢性炎症性肠病，30只诊断为消化性淋巴瘤）与19只健康对照猫，采用粪便S100A12浓度检测进行炎症标志物分析"
  core_argument: "粪便S100A12浓度可作为猫慢性肠病中疾病状态与健康状态的炎症标志物，但无法区分炎症性肠病与肠道淋巴瘤"
  implicit_premise: "粪便中S100A12浓度与肠道炎症活动水平相关，能够反映肠道炎症的存在但不足以区分不同病因"
  title_gap: "标题强调粪便S100A12在慢性肠病中的浓度变化，但研究揭示该标志物虽能区分病与健康，无法区分不同类型肠病如IBD与淋巴瘤，挑战了其作为病理亚型鉴别工具的潜力"
  evidence_boundary: "本研究未能回答粪便S100A12是否能预测疾病预后或疗效，亦未探讨其他潜在炎症或免疫标志物的联合诊断价值"
  unexpected_finding: "尽管S100A12在炎症性肠病和肠道淋巴瘤猫中均升高，但两者之间无显著差异，提示该指标无法区分这两种不同病理状态"
---

# One-line Summary

Fecal biomarker paper that likely adds a newer noninvasive support-marker branch to feline chronic enteropathy workup.

## Why It Matters For IBD

- gives the endpoint layer a stool-based inflammatory marker candidate
- may help keep noninvasive support separate from biopsy-confirmation logic
- now serves as the first fecal inflammatory support-marker anchor in the IBD module

## Key Findings

- abstract includes 49 chronic enteropathy cats and 19 healthy controls
- abstract reports elevated fecal S100A12 in both IBD and lymphoma relative to controls
- abstract reports no significant difference between IBD and lymphoma groups
- abstract supports a noninvasive inflammatory signal that is disease-associated but not class-separating

## Fecal Support-Marker Role

This source anchors a noninvasive stool-marker branch for feline chronic enteropathy. Its value is real but bounded. The abstract includes 49 cats with chronic enteropathy and 19 healthy controls. Within the chronic enteropathy group, 19 cats were diagnosed with IBD or chronic inflammatory enteropathy and 30 were diagnosed with alimentary lymphoma. Fecal S100A12 concentrations differed between both disease groups and healthy controls, but did not significantly differ between IBD and lymphoma.

That result gives the wiki a clean teaching rule: S100A12 can be a disease-versus-health inflammatory support marker, but it is not a lymphoma-boundary discriminator in this source. It should sit below biopsy-site strategy, histopathology, and imaging boundary signals. It may still matter because a noninvasive marker can help flag intestinal inflammation or disease burden, especially if later studies support monitoring or response tracking.

The source should be grouped with vitamin D as a support-marker branch, but the matrix should separate serum burden context from fecal inflammatory context. It should also be kept below metabolomics, which has a stronger frontier separation claim, though metabolomics itself remains non-routine.

The safe compiled statement is: fecal S100A12 adds noninvasive support for abnormal chronic enteropathy, but it should not be used to distinguish IBD from alimentary lymphoma or to replace tissue-centered workup.

This card is especially useful for preventing noninvasive-marker hype. The attractive feature is sample convenience, not diagnostic finality. Future densification should focus on thresholds, longitudinal stability, and treatment-response behavior rather than rebranding the marker as a definitive diagnostic tool.

The endpoint page should therefore place fecal S100A12 in a `supportive noninvasive marker` row. It can help explain why a cat is not normal, but it cannot tell the reader which chronic-enteropathy subtype is present. That distinction is the source's main reusable lesson here.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- chronic-enteropathy coverage may blur exact specificity for IBD
- no significant IBD-versus-lymphoma difference should remain attached to every practical summary
- do not promote stool-marker convenience into diagnostic leadership

## Open Follow-up Questions

- does S100A12 separate health, IBD, and lymphoma?
- is the main value diagnostic, burden-related, or monitoring-related?
- are there clinically useful thresholds, or is the marker best treated as continuous support?
- does S100A12 change with treatment response in a way that would justify monitoring use?

## Deep Extraction

- [src-ibd-017 deep extraction round 1](../../system/indexes/src-ibd-017-deep-extraction-round1.md)

## Linked Entities

- S100A12
- fecal biomarker
- chronic enteropathy
