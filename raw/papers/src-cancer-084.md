---
id: src-cancer-084
type: source
title: "Natural feline leukemia virus infection and the immune response of cats of different ages"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 1980
status: ingested
extraction_depth: abstract
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
pmid: 6258787
tags: [cancer, FeLV, age-susceptibility, immune-response, viremia, antibody, epidemiology]
links:
  doi: ""
  url: "https://pubmed.ncbi.nlm.nih.gov/6258787/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "71% of tracer kittens became viremic after 7 months exposure; 55% remained persistently infected."
    - "11% of tracer adults became infected by 7 months; 43% by 2 years."
    - "Mean latent periods: 3.4±1.8 months (kittens) vs 13.0±5.9 months (adults)."
    - "95% of kittens infected within 1 year; 61% of adults within 2 years."
  source_supported_conclusion:
    - "Kittens are more rapidly susceptible to FeLV than adults."
    - "Adult cats remain susceptible to FeLV following long-term natural exposure."
    - "Virus-neutralizing antibody appears in transiently viremic cats after viremia clearance."
  llm_inference:
    - "Key reference for age-dependent FeLV susceptibility claims."
    - "Supports lymphoma.md FeLV epidemiology section."
  # V2 enhanced fields
  study_design: "前瞻性流行病学研究（1980 年 Cancer Res），42 只幼猫 + 28 只成年猫作为示踪者置于 FeLV 聚集环境"
  core_argument: "FeLV 易感性具有明显的年龄依赖性——幼猫 7 个月时 71% 病毒血症（55% 持续感染）——成年猫 7 个月时仅 11%（2 年时 43%）——潜伏期差异大：幼猫 3.4 月 vs 成年猫 13.0 月——病毒中和抗体在一过性病毒血症清除后出现"
  implicit_premise: "假设示踪者研究设计可代表自然暴露模式；假设 1980 年的感染率可外推到当代（疫苗接种时代前）"
  unexpected_finding: "成年猫的'抵抗力'不是由于即时保护性体液免疫——而是延迟的潜伏期和较低的感染率——但 2 年内仍有 61% 感染"
  title_gap: "标题说不同年龄猫的自然 FeLV 感染和免疫反应，但真正发现是年龄-易感性分层：幼猫快速高度易感——成年猫有延迟但非绝对抵抗——支持幼猫优先疫苗接种策略"
  evidence_boundary: "经典流行病学证据（Essex/Gardner/Hardy 实验室）；支持年龄依赖性 FeLV 易感性声明，但在疫苗接种时代的适用性有限"
---

# Natural feline leukemia virus infection and the immune response of cats of different ages

## Source Check, 2026-06-03

| Field | Value |
|-------|-------|
| PMID | 6258787 |
| Journal | Cancer Res |
| Year | 1980 |
| Authors | Grant CK, Essex M, Gardner MB, Hardy WD Jr |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Study design | 42 kittens + 28 adults as tracers in FeLV cluster environments |
| Kitten infection | 71% viremic by 7 months; 55% persistently infected |
| Adult infection | 11% by 7 months; 43% by 2 years |
| Latent period | Kittens 3.4±1.8 months vs adults 13.0±5.9 months |
| Total infection rate | Kittens 95% within 1 year; adults 61% within 2 years |
| Immune response | Virus-neutralizing antibody in transiently viremic cats |

**Boundary:** Abstract-level extraction. Age-dependent susceptibility data can inform FeLV/lymphoma epidemiology claims.

## One-Line Summary

FeLV natural infection study: kittens 71% viremic by 7 months (latent period 3.4mo) vs adults 11% (latent period 13mo); age-dependent susceptibility confirmed.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- 42 kittens + 28 adults placed as tracers in FeLV cluster environments
- 71% of kittens became viremic by 7 months; 55% remained persistently infected
- 11% of adults became infected by 7 months; 43% by 2 years
- Mean latent periods: kittens 3.4±1.8 months vs adults 13.0±5.9 months
- Virus-neutralizing antibody appeared in transiently viremic cats after clearance
- FeLV infection detectable in 95% kittens within 1 year; 61% adults within 2 years

### source_supported_conclusion

- Kittens are significantly more susceptible to FeLV than adults
- Adult cats remain susceptible despite apparent resistance
- Adult "resistance" is not due to immediate protective humoral immunity
- Virus-neutralizing antibody correlates with transient vs persistent viremia

### llm_inference

- Key reference for age-dependent FeLV susceptibility in lymphoma.md
- Supports young cat vaccination priority recommendations
- Classic epidemiological study by Essex/Gardner/Hardy groups

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
