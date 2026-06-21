---
id: src-fip-020
type: source
title: "Epidemiology of feline infectious peritonitis among cats examined at veterinary medical teaching hospitals"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2001
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, epidemiology, risk]
links:
  doi: ""
  url: "https://avmajournals.avma.org/view/journals/javma/218/7/javma.2001.218.1111.xml"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source explicitly studies epidemiology of FIP among cats examined at veterinary medical teaching hospitals.
    - The abstract reports that approximately 1 of every 200 new feline accessions and 1 of every 300 total feline accessions at VMTH in North America represented cats with FIP.
    - The abstract reports that approximately 1 of every 100 accessions at diagnostic laboratories represented cats with FIP.
    - The abstract reports that cats with FIP were significantly more likely to be young, purebred, and sexually intact males, and less likely to be spayed females.
  source_supported_conclusion:
    - This source belongs in the referral-population epidemiology branch of FIP recognition.
    - This source supports a distinct institutional-enrichment layer inside the risk branch.
  llm_inference:
    - This paper may help distinguish broad population risk from referral-cluster or hospital-case enrichment.
    - This paper is best used to separate referral burden from general-population risk context.
  # V2 enhanced fields
  study_design: "原始研究，兽医教学医院就诊猫中 FIP 的流行病学"
  core_argument: "FIP 在转诊群体中具有独特的制度富集模式——约每 200 只新入院猫中有 1 只、每 300 只总入院猫中有 1 只、每 100 只诊断实验室送检中有 1 只为 FIP"
  implicit_premise: "假设医院群体可能扭曲一般群体患病率逻辑；假设机构入院不应被视为社区分母"
  unexpected_finding: "按年份、月份或地区的比例无显著变化——这支持研究期内稳定的机构负担声明，而非 FIP 在任何地方都恒定的普遍声明"
  title_gap: "标题说教学医院流行病学，但真正发现是制度富集程度的量化：每 200 只新入院/300 只总入院/100 只实验室送检中有 1 只 FIP——转诊负担与社区患病率是不同的知识对象"
  evidence_boundary: "转诊群体流行病学；制度富集不同于社区患病率；信号模式特征（年轻、纯种、完整雄性）部分与其他风险研究趋同"
---

# One-line Summary

Hospital epidemiology paper that strengthens the referral-population side of FIP recognition.

## Why It Matters For FIP

- adds institutional epidemiology context to the risk branch
- helps keep risk architecture from relying only on household or breed studies
- now serves as the first deep-extracted referral-epidemiology anchor in the FIP module

## Key Findings

- about 1 in 200 new feline VMTH accessions involved FIP
- about 1 in 300 total feline VMTH accessions involved FIP
- about 1 in 100 diagnostic-laboratory accessions involved FIP
- young, purebred, and sexually intact male cats were over-represented
- spayed females were under-represented
- proportions did not vary significantly by year, month, or region in this dataset

## Referral-Epidemiology Role

This paper gives the FIP module a distinct institutional epidemiology branch. It should not be merged with general-population prevalence or household risk. The study frame is veterinary medical teaching hospitals and diagnostic laboratories, which means the source is about where FIP appears in referral and diagnostic flows. That is a different kind of knowledge from breed prevalence, cattery exposure, or routine primary-care suspicion.

The hard numbers make the source unusually useful for a wiki page: about 1 in 200 new feline VMTH accessions, about 1 in 300 total feline VMTH accessions, and about 1 in 100 diagnostic-laboratory accessions represented cats with FIP. These numbers should be preserved with their population frame attached. They can teach why FIP remains operationally prominent in tertiary and necropsy-heavy settings, but they should not be exported as community prevalence.

This source also reinforces signalment patterns already seen elsewhere. Young, purebred, sexually intact male cats were over-represented, while spayed females were under-represented. In the compiled risk architecture, that means referral epidemiology does not replace signalment risk; it partly converges with it. The right structure is therefore layered: institutional enrichment tells us where FIP concentrates in veterinary systems, while age, sex, breed, and environment tell us how suspicion can be weighted in a given cat.

The reported lack of significant variation by year, month, or region inside the dataset should be used carefully. It supports a stable institutional-burden claim during the studied frame, not a universal claim that FIP is constant everywhere. In the future risk-and-recognition page, this card should be the main source for `referral setting changes pretest context`.

## Limits / Caveats

- current card is deep-extracted at worksheet level, but still not full-text reviewed
- hospital populations can distort general-population prevalence logic
- institutional accessions should not be treated as community denominators
- temporal and regional stability claims belong only to the studied dataset until directly verified

## Open Follow-up Questions

- how should referral-enrichment context be weighted relative to community or multi-cat risk?
- how much of the observed burden comes from institutional case selection rather than underlying biology?
- what exact inclusion criteria separated new accessions, total accessions, and diagnostic-laboratory accessions?
- how should the source be summarized for readers who confuse referral burden with population prevalence?

## Deep Extraction

- [src-fip-020 deep extraction round 1](../../system/indexes/src-fip-020-deep-extraction-round1.md)

## Linked Entities

- epidemiology
- risk factors
- referral population
