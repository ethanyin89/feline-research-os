---
id: src-cancer-024
type: source
title: "Descriptive epidemiology of canine and feline cancer in California, United States from 2000 to 2019"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2026
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
pmid: 41763637
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, descriptive, epidemiology, california, united, states]
links:
  doi: "10.1016/j.tvjl.2026.106612"
  url: "https://pubmed.ncbi.nlm.nih.gov/41763637/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Descriptive epidemiology of canine and feline cancer in California, United States from 2000 to 2019."
    - "The intake sheet locator is: https://pubmed.ncbi.nlm.nih.gov/41763637/."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
  # V2 enhanced fields
  study_design: "回顾性流行病学研究，UC Davis VMTH 150,063 例患者（2000-2019），分析 9 种主要癌症类型"
  core_argument: "加州猫患者中 17.0% 被诊断为癌症——年龄是最强预测因子，但这是转诊医院群体而非一般流行率"
  implicit_premise: "假设学术转诊医院数据可代表癌症流行病学；假设犬类详细发现可外推到猫"
  unexpected_finding: "犬类中老年（≥12 岁）肉瘤、淋巴瘤和 MCT 的几率实际下降——可能反映竞争性死亡风险而非真正发病率下降"
  title_gap: "标题说加州犬猫癌症描述性流行病学，但真正发现是数据基础设施差距：摘要主要报告犬类发现——猫特异性风险比需要全文提取——需要加州范围癌症登记处"
  evidence_boundary: "转诊医院群体不代表一般群体癌症发病率；猫特异性风险比在摘要中未详细报告"
---

# Descriptive epidemiology of canine and feline cancer in California, United States from 2000 to 2019

## Deep Extraction, 2026-06-05

[Deep extraction worksheet](../../system/indexes/src-cancer-024-deep-extraction-round1.md)

Safe promoted role:

- US referral hospital cancer prevalence benchmark (17.0% of cats)
- age as primary cancer risk factor
- denominator discipline (referral population, not general incidence)
- comparison anchor with Swiss registry (src-cancer-002)

Do not use this source as:

- general population cancer incidence
- feline-specific odds ratios (abstract reports canine only)
- breed or sex-neuter risk claims for cats
- treatment or prognosis guidance

## Evidence-Depth Caveat

This is an abstract-weighted source card. Large US epidemiological study from UC Davis VMTH (2000-2019) covering 9 major cancer types.

## Full Abstract (PubMed)

Cancer is a leading cause of morbidity and mortality in middle- to old-aged dogs and cats, yet detailed epidemiological data remain limited. This study investigated the distribution of nine major cancer types in dogs and cats using hospital records from the Veterinary Medical Teaching Hospital at the University of California, Davis (2000-2019). Sarcoma, carcinoma, lymphoid neoplasia (LN), mast cell tumor (MCT), and melanoma were analyzed using multivariable logistic regression to assess associations with breed, age, and sex-neuter status. Among 150,063 patients (79.9% dogs; 20.1% cats), 26,883 were diagnosed with cancer (18.1% of dogs; 17.0% of cats). Older age was the strongest predictor of these cancers in both species, though odds of sarcoma, LN, and MCT declined in senior dogs (≥12 years). The following associations were specific to dogs. Spayed females had higher odds of LN (OR=1.43), MCT (OR=1.92), and melanoma (OR=1.63) compared to intact females, whereas neutering had no significant effect in males. Male dogs had higher odds of LN than females, both intact (OR=1.59) and spayed/neutered (OR=1.15), while spayed females had higher odds of MCT than neutered males (OR=1.28). Sarcoma and carcinoma odds varied by age and sex-neuter status, with significant interactions. These findings highlight complex, cancer-type-specific associations. A California-wide cancer registry would provide a more comprehensive picture of cancer epidemiology in companion animals.

## Key Extracted Findings

| Finding | Value | Boundary |
|---------|-------|----------|
| Total patients | 150,063 (79.9% dogs, 20.1% cats) | UC Davis VMTH 2000-2019 |
| Cancer diagnoses | 26,883 total | 18.1% dogs, 17.0% cats |
| Feline cancer rate | 17.0% of feline patients | hospital population, not general prevalence |
| Strongest predictor | older age (both species) | primary risk factor |
| Cancer types analyzed | sarcoma, carcinoma, LN, MCT, melanoma | 5 major categories |
| Study limitation | hospital referral population | may not represent general population |

**Feline-specific note:** The abstract reports combined dog/cat findings. Detailed feline-only odds ratios would require full-text extraction.

**Boundary:** This is a hospital referral population, not a population-based cancer registry. Cancer prevalence (17.0% of feline patients) reflects referral bias.

## One-Line Summary

US epidemiology study: 17.0% of cats in UC Davis VMTH (2000-2019) diagnosed with cancer; older age is strongest predictor.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Descriptive epidemiology of canine and feline cancer in California, United States from 2000 to 2019.
- The intake sheet locator is: https://pubmed.ncbi.nlm.nih.gov/41763637/.

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
