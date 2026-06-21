---
id: src-fcv-005
type: source
title: "Epidemiological Investigation of Feline Upper Respiratory Tract Infection Encourages a Geographically Specific FCV Vaccine"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [prevalence, risk factors, vaccine locality]
jurisdictions: [China]
evidence_level: original-study
year: 2023
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, epidemiology, china, vaccine, prevalence]
links:
  doi: "10.3390/vetsci10010046"
  url: "https://www.mdpi.com/2306-7381/10/1/46"
  local_assets: []
evidence_policy:
  quoted_fact:
    - FCV was detected in 465 of 1158 cats with upper respiratory tract infection, accounting for 40.2%.
    - The study was designed to inform development of a geographically specific FCV vaccine.
  source_supported_conclusion:
    - This is a major modern FCV epidemiology anchor.
    - The paper supports keeping vaccine-locality pressure visible rather than assuming one universal strain solution.
  llm_inference:
    - This source should sit near the vaccine-breadth branch, not only under epidemiology.
  # V2 enhanced fields
  study_design: "前瞻性队列研究，包含武汉地区1158只患有上呼吸道感染的猫，通过病原检测确定FCV感染率和分布"
  core_argument: "武汉地区上呼吸道感染猫中FCV的高感染率和不同病毒株的地理分布支持开发地域特异性的FCV疫苗策略"
  implicit_premise: "不同地理区域的猫群中FCV菌株存在显著变异，且这些差异足以影响疫苗的保护效果"
  title_gap: "标题强调了上呼吸道感染的流行病学调查，但真正的发现是基于流行病学数据提出了地理特异性疫苗开发的新思路——这突破了传统单一疫苗株的理念"
  evidence_boundary: "本研究未评估地域特异性疫苗的实际免疫保护效果，也未探讨其他呼吸道病毒如猫疱疹病毒的流行情况及疫苗策略"
  unexpected_finding: "猫群中FCV携带率高达40.2%，远高于此前部分研究报道的感染率，显示病毒在该地区流行强度极高"
---

# Epidemiological Investigation of Feline Upper Respiratory Tract Infection Encourages a Geographically Specific FCV Vaccine

## One-Line Summary

Large Wuhan respiratory-cohort study arguing that FCV prevalence and strain pressure can justify geographically specific vaccine thinking.

## Why It Matters For FCV

- gives the module a large modern field-epidemiology anchor
- connects prevalence and risk-factor mapping to vaccine-strain selection pressure

## Key Findings

### quoted_fact

- FCV was detected in 465 of 1158 cats with upper respiratory tract infection, accounting for 40.2%.
- The study was designed to inform development of a geographically specific FCV vaccine.

### source_supported_conclusion

- FCV was the most frequent detected pathogen in the sampled URTI cohort.
- The cohort was large, hospital-based, and recent.
- The paper explicitly frames geography-specific vaccine pressure as a downstream implication.
- The study supports keeping regional strain pressure visible when discussing FCV vaccine design.

### llm_inference

- This source should sit between epidemiology and vaccine-breadth branches.
- Its safest role is `large symptomatic-cohort regional signal`, not `general cat-population prevalence`.

## Deep Extraction Notes

### Unit 1: The prevalence number is cohort-bound

- core_claim: FCV accounted for a large share of detected pathogens in cats with upper respiratory tract infection.
- hard_details: 465 of 1158 URTI cats were FCV-positive, 40.2%.
- implication: FCV deserves prominent placement in the URTI recognition and differential shell.
- boundary: this is not a general-population prevalence estimate and should not be written as prevalence among all cats.

### Unit 2: Geography is part of vaccine interpretation

- core_claim: the study connects local epidemiology to geography-specific vaccine thinking.
- hard_details: the paper was designed to inform development of a geographically specific FCV vaccine.
- implication: vaccine pages should avoid assuming one universal strain-fit answer.
- boundary: the paper does not by itself prove a deployed local vaccine would outperform existing products.

### Unit 3: Epidemiology and vaccine branches should cross-link

- core_claim: this source is not only a prevalence paper.
- hard_details: the title and preserved conclusions explicitly connect epidemiology with vaccine locality.
- implication: the FCV module should cross-reference this card from both epidemiology and vaccine-breadth pages.
- boundary: risk-factor details should be promoted only where the source layer preserves the adjusted results.

## Claim-Evidence Structure

| Claim | Evidence in this card | Safe downstream use | Do not use for |
|---|---|---|---|
| FCV is prominent in a symptomatic URTI cohort | 465/1158, 40.2% | URTI recognition and FCV priority | whole-population prevalence |
| Regional strain pressure matters | geography-specific vaccine framing | vaccine-locality caveat | proof of regional product superiority |
| Modern China data belongs in the module | 2023 large hospital-based cohort | current field-epidemiology anchor | global FCV epidemiology |
| Vaccine-fit claims need locality awareness | explicit vaccine-locality aim | cross-linking epidemiology and vaccine pages | universal strain-selection rule |

## Write-Back Implications

- [current state dashboard](../../topics/fcv/current-state-dashboard.md) should treat this as the main modern regional epidemiology anchor.
- [endpoint handbook](../../topics/fcv/endpoint-handbook.md) should cite this for vaccine-locality pressure, not only prevalence.
- [translation brief](../../topics/fcv/translation-brief.md) can safely say FCV may dominate symptomatic URTI cohorts in some settings, while preserving the cohort boundary.
- [regulatory brief](../../topics/fcv/regulatory-brief.md) should not convert this into a label or product-choice claim.

## Limits / Caveats

- symptomatic cohort data should not be read as general-population prevalence
- vaccine-locality logic still needs to be reconciled with older cross-neutralisation studies

## Open Follow-Up Questions

- what risk factors were strongest after adjustment?
- how different are the Wuhan strains from older F9-centered vaccine logic?

## Linked Entities

- diseases: FCV
- models:
- endpoints: prevalence, risk factors, vaccine locality
- mechanisms: strain diversity
- regulations:
