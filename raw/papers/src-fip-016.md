---
id: src-fip-016
type: source
title: "Efficacy and safety of the nucleoside analog GS-441524 for treatment of cats with naturally occurring feline infectious peritonitis"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2019
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, treatment, gs-441524]
links:
  doi: ""
  url: "https://journals.sagepub.com/doi/10.1177/1098612X19825701"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source is an efficacy and safety study of GS-441524 in cats with naturally occurring FIP.
    - The abstract reports 31 cats enrolled, including 26 with effusive or dry-to-effusive disease and five with non-effusive disease; severe neurologic and ocular FIP cases were not recruited.
    - The abstract reports that 24 cats remained healthy at publication and that the optimum dosage identified was 4.0 mg/kg SC every 24 hours for at least 12 weeks.
  source_supported_conclusion:
    - This is one of the main treatment anchors in the modern FIP literature set.
    - The study supports clinical efficacy of GS-441524 in naturally occurring FIP, but its case mix does not justify overgeneralizing to severe neurologic and ocular disease.
    - The treatment story should be framed as transformation with response management, not frictionless cure.
    - Early deaths, relapse, retreatment, and dose escalation are part of the evidence architecture.
  llm_inference:
    - This should be one of the first FIP papers to receive deep extraction.
  # V2 enhanced fields
  study_design: "原始研究，31 只自然发生 FIP 猫的 GS-441524 疗效和安全性研究"
  core_argument: "GS-441524 在自然发生 FIP 中转变了治疗——但病例组合不包括严重神经和眼部 FIP，疗效框架应保留复发、再治疗和剂量递增"
  implicit_premise: "假设 24/31 存活是有意义的基线疗效信号；假设排除的病例子集（神经/眼部）需要单独证据"
  unexpected_finding: "治疗故事包括早期死亡、复发、再治疗和剂量递增——这挑战了「GS 治愈 FIP」的简化叙事"
  title_gap: "标题说 GS-441524 疗效和安全性，但真正发现是转化而非治愈：24/31 存活但排除了严重神经/眼部病例，且包括早期死亡、复发和剂量递增——治疗框架应是「反应管理」而非「无摩擦治愈」"
  evidence_boundary: "基线自然疾病治疗锚点，非严重神经/眼部 FIP；不应转换为普遍全形式治愈语言"
---

# One-line Summary

Core natural-disease treatment paper that likely anchors the modern GS-441524 branch of the FIP module.

## Why It Matters For FIP

- moves the module from fatal-disease framing toward actual intervention outcomes
- likely becomes central to any later treatment ranking, outcome, or implementation memo
- now serves as the first deep-extracted natural-disease treatment anchor in the FIP module

## Key Findings

- abstract aim was to determine safety and efficacy in naturally acquired FIP
- enrolled cats were treated initially at 2.0 mg/kg SC daily and increased when indicated to 4.0 mg/kg
- four cats died or were euthanized within 2-5 days and a fifth after 26 days
- 26 cats completed the intended treatment period; relapses occurred but multiple cats responded to retreatment at higher dose
- abstract conclusion states GS-441524 was safe and effective and identifies 4.0 mg/kg SC daily for at least 12 weeks as the optimum dosage within this study

## Treatment-Branch Role

This paper is the baseline natural-disease treatment anchor for the modern FIP module. It moves the disease away from old fatal-endpoint framing by reporting GS-441524 efficacy and safety in cats with naturally occurring FIP. That changes the translational center of gravity: FIP can no longer be written as a disease with only supportive or terminal care.

The study is strong because it is clinical rather than only in vitro or experimental infection evidence. It enrolled 31 cats, most with effusive or dry-to-effusive disease and a smaller non-effusive group. The outcome signal is also strong: 24 cats remained healthy at publication, despite early deaths and relapses in the full treatment story.

The branch boundary is case mix. Severe neurologic and ocular FIP cases were not recruited, so this paper should not be used to settle high-complexity neurologic or ocular treatment. It should instead serve as the baseline GS-441524 anchor beneath which relapse, retreatment, dose escalation, and minimum treatment duration are all preserved.

The safe compiled rule is: GS-441524 transformed FIP treatment in this natural-disease cohort, but the paper supports bounded baseline treatment logic rather than universal all-form cure language.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- severe neurologic and ocular FIP cases were not recruited, so the paper should not be overextended to those branches
- efficacy framing should not be flattened into universal outcome certainty without deeper extraction
- protocol conclusions are study-specific and should not be converted into regulatory or product-ranking language without official-source support
- later real-world and neurologic-treatment papers are needed to widen this branch safely

## Open Follow-up Questions

- what response endpoints were actually used?
- how were effusive, non-effusive, ocular, and neurologic cases handled?
- what were the exact relapse patterns and retreatment thresholds?
- how should baseline GS evidence be compared with combination remdesivir-plus-GS case series?

## Deep Extraction

- [src-fip-016 deep extraction round 1](../../system/indexes/src-fip-016-deep-extraction-round1.md)

## Linked Entities

- GS-441524
- antiviral treatment
- remission
