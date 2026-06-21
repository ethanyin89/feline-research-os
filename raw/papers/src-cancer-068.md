---
id: src-cancer-068
type: source
title: "Demographics of Feline Lymphoma in Australian Cat Populations: 1705 Cases"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: [Australia]
evidence_level: case-series
year: 2024
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
pmid: "39728981"
tags: [cancer, lymphoma, demographics, epidemiology, breed-risk, sex-risk, age, anatomic-location, Australian]
links:
  doi: "10.3390/vetsci11120641"
  url: "https://www.mdpi.com/2306-7381/11/12/641"
  pubmed: "https://pubmed.ncbi.nlm.nih.gov/39728981/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Lymphoma is the most common haematopoietic cancer in cats."
    - "A total of 1705 lymphoma cases were identified and compared to a reference population of 85,741 cats."
    - "Eight breeds were identified as displaying increased potential risk of lymphoma and three at decreased risk."
    - "Male cats were found to be at increased risk (OR 1.2, 95%CI: 1.1 to 1.3, p = 0.002)."
    - "The lymphoma cases were older, with a median age of 11.7 years compared to 9.0 years."
    - "Lymphoma cases weighed less, with a median weight of 3.7 kg compared to 4.0 kg."
    - "Several breeds were found to have significant variations in the proportions of anatomical presentations including the Siamese, Burmilla, Australian mist, ragdoll, British shorthair, and domestic cats."
  source_supported_conclusion:
    - "This source provides modern Australian lymphoma demographics with large case numbers."
    - "Breed-specific risk and anatomic presentation patterns are documented."
    - "Sex and age risk factors are quantified with odds ratios."
  llm_inference:
    - "This source can complement src-cancer-008 for modern lymphoma epidemiology."
    - "Breed risk claims need Australian-population caveats."
  # V2 enhanced fields
  study_design: "回顾性流行病学研究（2024 年 Vet Sci），1705 例澳大利亚猫淋巴瘤病例与 85,741 只参考群体比较"
  core_argument: "澳大利亚猫淋巴瘤有可量化的风险因素——雄性风险增加（OR 1.2）——病例年龄更大（中位 11.7 vs 9.0 岁）——病例体重更轻（中位 3.7 vs 4.0 kg）——8 个品种风险增加，3 个品种风险降低——解剖位置模式因品种而异"
  implicit_premise: "假设澳大利亚猫群体可代表更广泛模式；假设体重与淋巴瘤的关联不仅仅是疾病导致的消瘦"
  unexpected_finding: "品种特异性解剖位置模式——暹罗、Burmilla、澳大利亚雾猫、布偶、英国短毛和家猫在解剖表现上有显著差异——这种品种-位置关联提示遗传因素可能影响淋巴瘤亚型"
  title_gap: "标题说澳大利亚猫群体的淋巴瘤人口统计学，但真正发现是风险分层：可量化的品种、性别、年龄和体重风险因素——大样本量（1705 例）提供统计效力——但品种名称需要全文提取"
  evidence_boundary: "澳大利亚群体数据；支持流行病学背景和风险因素量化，不支持普适性品种风险声明或因果机制结论"
---

# Demographics of Feline Lymphoma in Australian Cat Populations: 1705 Cases

## Deep Extraction, 2026-06-05

[Deep extraction worksheet](../../system/indexes/src-cancer-068-deep-extraction-round1.md)

Safe promoted role:

- modern lymphoma demographics with quantified risk factors
- male sex risk (OR 1.2, 95%CI 1.1-1.3, p=0.002)
- age signalment (median 11.7 years for cases)
- weight association (median 3.7 kg for cases)
- breed-anatomic presentation pattern variations

Do not use this source as:

- specific breed risk claims (names not in abstract, need full text)
- causal mechanism conclusions
- universal claims beyond Australian population
- treatment or prognosis guidance

Follow-up needed: full-text for 8 high-risk and 3 low-risk breed names.

## Evidence-Depth Caveat

This card has abstract-level extraction from PubMed (PMID: 39728981). It is a 2024 Australian epidemiological study with 1705 lymphoma cases and 85,741 reference population. Full-text deep extraction is recommended for breed-specific risk tables and anatomic presentation data.

## One-Line Summary

Large Australian lymphoma demographics study documenting breed risk, sex risk (male OR 1.2), age (median 11.7 years), and breed-specific anatomic presentation patterns.

## Why It Matters For Feline Cancer

This source provides modern lymphoma epidemiology data to complement the historical src-cancer-008 pathology classification. Key value:

- Large case numbers (1705 vs 602 in src-cancer-008)
- Modern timeframe (2024 publication)
- Reference population comparison (85,741 cats)
- Quantified risk factors with confidence intervals
- Breed-specific anatomic presentation patterns

## Key Findings

### quoted_fact

- "Lymphoma is the most common haematopoietic cancer in cats."
- "A total of 1705 lymphoma cases were identified and compared to a reference population of 85,741 cats."
- "Eight breeds were identified as displaying increased potential risk of lymphoma and three at decreased risk."
- "Male cats were found to be at increased risk (OR 1.2, 95%CI: 1.1 to 1.3, p = 0.002)."
- "The lymphoma cases were older, with a median age of 11.7 years compared to 9.0 years (p < 0.0001)."
- "Lymphoma cases weighed less, with a median weight of 3.7 kg compared to 4.0 kg (p = 0.010)."
- "Siamese, Burmilla, Australian mist, ragdoll, British shorthair, and domestic cats showed significant variations in anatomical presentations."

### source_supported_conclusion

- This source strengthens lymphoma epidemiology with modern data and large numbers.
- Breed-specific risk factors can inform breed-aware discussions.
- Age and weight associations provide signalment context.
- Anatomic presentation variations by breed may inform topography branch.

### llm_inference

- Full-text needed to identify the 8 high-risk and 3 low-risk breeds.
- Australian genetic pool isolation may limit generalizability.
- Comparison with src-cancer-002 Swiss data could reveal regional patterns.

## Claim-Fit Judgment

Strongest safe use:

- lymphoma demographics and signalment
- breed-risk hypothesis (with Australian population caveat)
- anatomic presentation patterns by breed
- age/weight correlation documentation

Should use with caveats:

- breed risk claims need population boundary
- odds ratios should include confidence intervals

Must not control yet:

- universal breed risk claims
- treatment or prognosis guidance
- causal mechanism claims

## Open Follow-Up Questions

- Which 8 breeds showed increased risk and which 3 showed decreased risk?
- Does the study address FeLV/FIV status?
- How do anatomic presentation patterns compare to src-cancer-008 topography data?

## Linked Entities

- diseases: cancer, lymphoma
- models:
- endpoints: demographics, breed risk, anatomic location
- mechanisms:
- regulations:
