---
id: src-cancer-102
type: source
title: "Horizontal Transmission of Feline Leukemia Virus Under Experimental Conditions"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 1977
status: ingested
extraction_depth: abstract
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
pmid: 189052
tags: [cancer, FeLV, transmission, horizontal, epidemiology, viremia]
links:
  doi: "10.1093/jnci/58.2.443"
  url: "https://academic.oup.com/jnci/article-abstract/58/2/443/1012927?redirectedFrom=fulltext&login=false"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "PubMed-indexed: J Natl Cancer Inst. 1977 Feb;58(2):443-4."
    - "Authors: Hoover EA, Olsen RG, Hardy WD Jr, Schaller JP."
    - "37 SPF cats inoculated with Rickard strain FeLV."
    - "20/37 inoculated cats became gsa-positive after 4-5 weeks."
    - "17/20 contact cats with gsa-positive cats became FeLV infected."
    - "Contact cats with gsa-negative cats: none became infected."
  source_supported_conclusion:
    - "GSA-positive state correlates with capacity for horizontal transmission."
    - "Horizontal transmission requires viremic (gsa-positive) source cat."
  llm_inference:
    - "Key paper for lymphoma.md FeLV transmission epidemiology."
    - "Hardy WD Jr is seminal FeLV researcher."
  # V2 enhanced fields
  study_design: "实验感染研究（1977 年 JNCI），37 只 SPF 猫，Rickard 株 FeLV 接种，同笼接触传播 40 周观察"
  core_argument: "水平传播需要病毒血症（gsa 阳性）源猫——20/37 接种猫变为 gsa 阳性——与 gsa+ 猫接触的 17/20 接触猫感染——与 gsa- 猫接触的 0% 感染——gsa 状态可预测传播风险"
  implicit_premise: "假设实验条件（SPF 猫、同笼接触）可代表自然多猫家庭传播；假设 Rickard 株可代表野生型 FeLV"
  unexpected_finding: "17/37 接种猫保持 gsa 阴性但产生抗体——这些猫不传播病毒——暗示病毒清除者是安全的共处伙伴——这对多猫家庭管理有重要意义"
  title_gap: "标题说实验条件下 FeLV 水平传播，但真正发现是传播风险分层：gsa 状态（而非感染史）决定传播能力——gsa- 抗体阳性猫不传播——这为 FeLV 阳性猫的管理提供依据"
  evidence_boundary: "实验传播证据（Hoover/Hardy 实验室）；支持 gsa 状态与传播风险的关联，但不直接支持当代多猫家庭管理建议——需要结合当代诊断方法解读"
---

# Horizontal Transmission of Feline Leukemia Virus Under Experimental Conditions

## Source Check, 2026-06-03

| Field | Value |
|-------|-------|
| PMID | 189052 |
| DOI | 10.1093/jnci/58.2.443 |
| Journal | J Natl Cancer Inst |
| Year | 1977 |
| Authors | Hoover EA, Olsen RG, Hardy WD Jr, Schaller JP |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Study type | Experimental transmission study |
| Sample | 37 SPF cats (inoculated + contact) |
| Key finding | 20/37 became gsa-positive after 4-5 weeks |
| Transmission | 17/20 contact cats with viremic cats became infected |
| No transmission | Contact with gsa-negative cats: 0% infection |

**Boundary:** Abstract-level extraction. Transmission findings inform FeLV epidemiology and lymphoma risk.

## One-Line Summary

FeLV horizontal transmission requires viremic (gsa-positive) source cat; 17/20 contact cats became infected from gsa+ cats vs 0% from gsa- cats.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- 37 SPF cats (newborn to 1 year) inoculated with Rickard strain FeLV
- Each inoculated cat shared cage with control SPF cat for 40 weeks
- 20/37 inoculated cats became gsa-positive after 4-5 weeks
- 17 remained gsa-negative but developed antibody titers
- 17/20 contact cats with gsa-positive cats became FeLV infected (4-18 weeks after viremia)
- 0% of contact cats with gsa-negative cats became infected
- Infected cats became chronic carriers (viremic) during 9-11 week observation

### source_supported_conclusion

- GSA-positive state correlates with capacity for horizontal FeLV transmission
- Horizontal transmission requires viremic source cat
- Non-viremic (antibody-positive, gsa-negative) cats do not transmit horizontally

### llm_inference

- Key paper for lymphoma.md FeLV transmission epidemiology
- Informs FeLV testing and isolation recommendations
- Hardy WD Jr is seminal FeLV researcher

## Claim-Fit Judgment

Strongest safe use:

- intake ownership
- source queue placement
- deduplication and future extraction planning

Must not control yet:

- reader-facing medical advice
- numeric claims
- comparative ranking
- guideline-like recommendations
- mechanism closure

## Image Asset TODO

- figures to capture: unknown until source text is read
- why these matter: tables or figures should remain behind the candidate gate until labels are verified

## Open Follow-Up Questions

- What source family is confirmed by the abstract or article body?
- Which claims, if any, are reusable for the cancer module?
- Does this source deserve deep extraction, or should it remain queue context?
- Are there tables or figures that change the module structure?

## Linked Entities

- diseases: cancer
- models:
- endpoints:
- mechanisms:
- regulations:
