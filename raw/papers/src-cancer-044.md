---
id: src-cancer-044
type: source
title: "Feline Leukemia Virus Infection: Age-Related Variation in Response of Cats to Experimental Infection"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 1976
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
pmid: 187771
doi: "10.1093/jnci/57.2.365"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, leukemia, virus, infection, age-related, variation, response, experimental]
links:
  doi: ""
  url: "https://academic.oup.com/jnci/article-abstract/57/2/365/910132?redirectedFrom=fulltext&login=false"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Feline Leukemia Virus Infection: Age-Related Variation in Response of Cats to Experimental Infection."
    - "The intake sheet locator is: https://academic.oup.com/jnci/article-abstract/57/2/365/910132?redirectedFrom=fulltext&login=false."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
  # V2 enhanced fields
  study_design: "实验感染研究（1976 年 JNCI），67 只 SPF 猫，Rickard 和 Kawakami-Theilen FeLV 株腹腔接种，不同年龄组"
  core_argument: "FeLV 易感性具有强烈的年龄依赖性——新生儿 100% 易感——2 周-2 月龄 85%——4 月龄或 1 岁仅 15%——易感猫持续病毒血症且无抗体——抵抗猫产生 FOCMA 和中和抗体"
  implicit_premise: "假设实验感染条件（腹腔接种）可代表自然感染模式；假设 1976 年的 SPF 猫结果可外推到当代（疫苗接种时代前）"
  unexpected_finding: "两种 FeLV 株诱导不同疾病——FeLV-R 主要导致胸腺淋巴肉瘤——FeLV-KT 导致非再生性贫血而无肿瘤——暗示病毒株决定疾病表型"
  title_gap: "标题说 FeLV 感染对实验感染的年龄相关反应变异，但真正发现是免疫-病毒平衡：易感性不仅与年龄相关——还与免疫反应能力相关——抗体阳性猫抵抗持续感染——支持早期疫苗接种策略"
  evidence_boundary: "经典实验感染证据（Hoover 实验室）；支持年龄依赖性易感性声明，但在疫苗接种时代的适用性有限——现代 FeLV 管理应结合当代指南"
---

# Feline Leukemia Virus Infection: Age-Related Variation in Response of Cats to Experimental Infection

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. 1976 JNCI: 67 SPF cats experimentally infected. Newborns 100% susceptible, 4+ months only 15%. FeLV-R → thymic lymphosarcoma; FeLV-KT → anemia. Foundation for age-related FeLV vulnerability. [Deep extraction worksheet](../../system/indexes/src-cancer-044-deep-extraction-round1.md).

## Source Check, 2026-06-01

PubMed abstract fetched as a zero-cost extraction step.

- PMID: 187771
- DOI: 10.1093/jnci/57.2.365
- Journal: Journal of the National Cancer Institute
- Year: 1976

## Abstract Summary

This experimental infection study evaluated age-related susceptibility of specific-pathogen-free cats to two FeLV strains.

**Study design:**

| Feature | Abstract-Extracted Detail |
|---------|---------------------------|
| Population | 67 specific-pathogen-free cats |
| Ages | Newborn, 2 weeks, 1 month, 2 months, 4 months, 1 year |
| Exposure | Intraperitoneal inoculation with Rickard or Kawakami-Theilen FeLV strains |
| Susceptibility endpoints | FeLV group-specific antigen in leukocytes, FeLV-related disease, FOCMA antibody, virus-neutralizing antibody |

**Age-related susceptibility:**

| Age at inoculation | Persistent viremia / FeLV-related disease |
|--------------------|------------------------------------------|
| Newborn | 100% |
| 2 weeks to 2 months | 85% |
| 4 months or 1 year | 15% |

**Immune-response pattern:**

- Cats susceptible to FeLV leukemogenesis became persistently FeLV gsa-positive by 4 weeks after inoculation and produced little or no FOCMA or virus-neutralizing antibody.
- Cats resisting FeLV leukemogenesis developed persistent FOCMA and virus-neutralizing titers and did not become FeLV gsa-positive.

**Virus-strain difference:**

- FeLV-R induced predominantly thymic lymphosarcoma.
- FeLV-KT caused fatal nonregenerative anemia without concurrent neoplasia.

**Boundary:** This is historical experimental-infection evidence, not modern FeLV prevention or management guidance.

## One-Line Summary

Experimental FeLV infection showed strong age-related susceptibility, with newborn and young kittens much more likely to develop persistent viremia and FeLV-related disease than older cats.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Feline Leukemia Virus Infection: Age-Related Variation in Response of Cats to Experimental Infection.
- The intake sheet locator is: https://academic.oup.com/jnci/article-abstract/57/2/365/910132?redirectedFrom=fulltext&login=false.

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
