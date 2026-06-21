---
id: src-fip-005
type: source
title: "Risk factors for feline infectious peritonitis in Australian cats"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: []
jurisdictions: [Australia]
evidence_level: original-study
year: 2012
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, epidemiology, risk-factors]
links:
  doi: ""
  url: "https://journals.sagepub.com/doi/10.1177/1098612X12441875"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source is a dedicated risk-factor study on Australian cats.
    - The abstract reports comparison of 382 confirmed FIP cases with the Companion Animal Register of NSW and the general cat population of Sydney.
    - The abstract reports that younger cats were significantly over-represented among FIP cases.
    - The abstract reports over-representation of British Shorthair, Devon Rex, and Abyssinian cats, and under-representation of domestic crossbred, Persian, and Himalayan cats.
  source_supported_conclusion:
    - This source belongs in the epidemiology and recognition branch, not in the mechanism or treatment branch.
    - This source gives the module a structured signalment-risk anchor centered on age, patterned breed signal, and male over-representation.
    - Risk context should raise suspicion earlier, but it does not diagnose FIP.
    - The Australian comparator structure means geography and population structure must travel with the risk claims.
  llm_inference:
    - This is one of the most useful early sources for building a practical recognition map.
    - This paper is best used to sharpen pretest suspicion rather than to broaden diagnostic claims.
  # V2 enhanced fields
  study_design: "病例对照研究，382 例确诊 FIP 猫 vs NSW 伴侣动物登记处 + 悉尼普通猫群（澳大利亚）"
  core_argument: "FIP 风险因素呈结构化模式——年幼、雄性、特定品种（英短、德文卷毛、阿比西尼亚）过度代表，而非简单的「所有纯种猫」警告"
  implicit_premise: "假设澳大利亚猫群的品种分布和环境因素可泛化到其他地区；假设 FIP 确诊病例的入选标准足够严格以排除假阳性"
  unexpected_finding: "波斯猫和喜马拉雅猫反而在 FIP 病例中「低于预期」——这与「纯种猫高风险」的简单叙事形成对比"
  title_gap: "标题说风险因素，但真正发现是结构化模式：英短、德文卷毛、阿比西尼亚过度代表，而波斯猫和喜马拉雅猫反而低于预期——「所有纯种猫高风险」是过度简化"
  evidence_boundary: "风险因素研究不能用于个体诊断；品种效应可能受地区繁殖谱系影响而无法直接移植；不能回答「为什么」某些品种高风险"
---

# One-line Summary

Dedicated epidemiology study that anchors the modern risk-factor branch of the FIP module.

## Why It Matters For FIP

- helps separate susceptibility and exposure context from later clinicopathologic diagnosis
- provides a field-population view rather than only referral-hospital disease description
- now serves as the first deep-extracted signalment-risk anchor in the FIP module

## Key Findings

- 382 confirmed FIP cases were compared with registry and general-population comparators
- younger cats were significantly over-represented
- British Shorthair, Devon Rex, and Abyssinian cats were over-represented
- domestic crossbred, Persian, and Himalayan cats were under-represented
- male cats were significantly over-represented

## Risk-Branch Role

This paper anchors the pretest-risk layer of the FIP recognition map. It is not a clinicopathology paper and not a diagnostic-performance paper. Its job is to answer a different question: which cats should make FIP rise earlier on the suspicion list before any one laboratory or molecular signal is interpreted?

The useful structure is specific rather than generic. The study compared 382 confirmed FIP cases with the Companion Animal Register of NSW and the general cat population of Sydney. Younger cats were over-represented, male cats were over-represented, and breed signals were patterned rather than a simple `all pedigree cats` warning. British Shorthair, Devon Rex, and Abyssinian cats were over-represented, while domestic crossbred, Persian, and Himalayan cats were under-represented.

The safe compiled rule is: age, sex, and breed/population context can sharpen suspicion, but they cannot settle diagnosis. This source belongs at the top of risk-and-recognition pages as pretest context, then clinicopathology, effusion/CSF/mutation evidence, and treatment context should be layered separately.

For wiki reuse, this card should become the first layer of a `risk before diagnosis` stack. It pairs naturally with `src-fip-008`, `src-fip-012`, and `src-fip-020`, but it should not be merged into them too early. Its distinct value is signalment and population context: age, sex, breed distribution, and comparator choice. The other epidemiology sources can then add incidence, environment, outbreak, or survival context without diluting this card's simpler operational rule.

The claim ceiling is also important. A young male cat from an over-represented breed can make FIP more salient, especially when later clinicopathologic signs fit, but this source cannot decide whether an individual cat has FIP. The future wiki page should therefore present risk variables as a pretest-weighting checklist, not as a diagnostic score. Geography should stay visible because the comparison groups were Australian/NSW/Sydney populations, and breed composition can change the apparent strength of associations.

## Limits / Caveats

- current card is deep-extracted at worksheet level, but still not full-text reviewed
- risk structure may not generalize cleanly outside its study population
- association data should not be translated into individual-cat certainty
- breed and sex signals should remain lower than clinical form and clinicopathology once disease is suspected

## Open Follow-up Questions

- how much of this risk structure transfers outside Australian populations?
- how should age, breed, and ecology be weighted relative to one another in recognition architecture?
- should this source be paired with `src-fip-008`, `src-fip-012`, and `src-fip-020` in a single risk-epidemiology memo?

## Deep Extraction

- [src-fip-005 deep extraction round 1](../../system/indexes/src-fip-005-deep-extraction-round1.md)

## Linked Entities

- risk factors
- multi-cat environments
- epidemiology
