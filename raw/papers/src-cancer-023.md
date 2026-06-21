---
id: src-cancer-023
type: source
title: "Regional Variations in and Key Predictors of Feline Tumor Malignancy: A Decade-Long Retrospective Study in Korea"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2024
status: ingested
extraction_depth: abstract
verification_status: abstract_weighted
pmid: 39457919
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, regional, variations, key, predictors, malignancy, decade-long, retrospective]
links:
  doi: ""
  url: "https://www.mdpi.com/2076-2615/14/20/2989"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Regional Variations in and Key Predictors of Feline Tumor Malignancy: A Decade-Long Retrospective Study in Korea."
    - "The intake sheet locator is: https://www.mdpi.com/2076-2615/14/20/2989."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
  # V2 enhanced fields
  study_design: "回顾性研究（韩国 2012-2022），683 只猫的肿瘤数据，回归分析预测恶性因素"
  core_argument: "猫肿瘤谱系存在显著区域差异——韩国皮肤 SCC 罕见（vs 西方研究），可能反映环境暴露差异（室内生活方式）"
  implicit_premise: "假设 683 只猫样本可代表韩国猫群；假设皮肤 SCC 差异主要由 UV 暴露而非其他因素解释"
  unexpected_finding: "韩国皮肤 SCC 罕见，与西方研究形成鲜明对比——这一区域差异可能反映韩国猫的室内生活方式减少了 UV 暴露"
  title_gap: "标题说韩国猫肿瘤恶性的区域差异和关键预测因子，但真正发现是生活方式决定论：韩国皮肤 SCC 罕见——室内生活方式可能保护猫免受 UV 诱导的 SCC"
  evidence_boundary: "韩国单国数据，环境和生活方式因素可能解释区域差异；需要多中心数据集纳入环境、遗传和生活方式因素"
---

# Regional Variations in and Key Predictors of Feline Tumor Malignancy: A Decade-Long Retrospective Study in Korea

## Evidence-Depth Caveat

This is an abstract-weighted source card. 2024 Korean retrospective study (2012-2022) providing non-Western regional data on feline tumor patterns.

## Full Abstract (PubMed)

Feline cancer is increasingly recognized as a major cause of mortality, yet data on tumor prevalence and behavior in cats, particularly in non-Western regions, remain limited. This study analyzed a decade of feline tumor data in Korea from 2012 to 2022, focusing on age, breed, and anatomical location as predictors of malignancy. Data were collected from 683 cats, with regression analysis applied to determine significant associations. Older cats exhibited a markedly higher risk of malignancy, particularly in mast cell and mammary tumors. Tumors in the mammary gland and alimentary tract had malignancy rates exceeding 90%, underscoring the need for early detection in these regions. Interestingly, squamous cell carcinoma was rare in the skin, in stark contrast to Western studies, likely reflecting differences in environmental exposure. While breed was not a statistically significant predictor, certain breeds, including Persians and Russian Blues, showed a higher frequency of malignancy. These findings highlight the importance of regional tumor research in cats and the need for larger, multicenter datasets that incorporate environmental, genetic, and lifestyle factors.

## Key Extracted Findings

| Finding | Value | Boundary |
|---------|-------|----------|
| Study population | 683 cats, Korea 2012-2022 | decade-long retrospective |
| Age as predictor | older cats markedly higher malignancy risk | especially mast cell and mammary |
| Mammary malignancy rate | >90% | high malignancy location |
| Alimentary tract malignancy rate | >90% | high malignancy location |
| Skin SCC | rare (contrast to Western studies) | **regional variation** |
| Environmental hypothesis | differences in UV/environmental exposure | explains skin SCC rarity |
| Breed as predictor | NOT statistically significant | population-level |
| Higher malignancy breeds | Persians, Russian Blues | frequency, not significance |

**Regional insight:** Skin SCC rarity in Korea vs Western countries suggests environmental exposure (likely indoor lifestyle) affects cancer patterns. This is important for interpreting prevalence data across regions.

**Boundary:** This is a Korean single-country study. Environmental and lifestyle factors (indoor vs outdoor) may explain regional differences.

## One-Line Summary

Korean 2024 study: >90% malignancy in mammary/alimentary tumors; skin SCC rare (vs Western), suggesting environmental exposure differences.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Regional Variations in and Key Predictors of Feline Tumor Malignancy: A Decade-Long Retrospective Study in Korea.
- The intake sheet locator is: https://www.mdpi.com/2076-2615/14/20/2989.

### source_supported_conclusion

- This is a first-pass source-card placeholder for triage and queue control.
- It should not support prevalence, diagnostic, treatment, management, or risk-ranking claims yet.

### llm_inference

- The title suggests a possible `cancer` role, but the actual claim-fit requires abstract or full-text review.

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
