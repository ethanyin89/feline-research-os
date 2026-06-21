---
id: src-cancer-060
type: source
title: "Comparison of virus-positive and virus-negative cases of feline leukemia and lymphoma"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: case-series
year: 1979
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
pmid: 225010
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, comparison, virus-positive, virus-negative, cases, leukemia, lymphoma]
links:
  doi: ""
  url: "https://pubmed.ncbi.nlm.nih.gov/225010/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Comparison of virus-positive and virus-negative cases of feline leukemia and lymphoma."
    - "The intake sheet locator is: https://pubmed.ncbi.nlm.nih.gov/225010/."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
  # V2 enhanced fields
  study_design: "回顾性病例系列（1979 年 Cancer Research），184 例猫白血病/淋巴瘤，波士顿 1972-1976，荧光抗体 FeLV 检测"
  core_argument: "FeLV 阴性猫白血病/淋巴瘤是真实存在的独立实体——33% 病例 FeLV 阴性——阴性猫诊断年龄更大（4.9 vs 3.5 岁）——68% >8 岁猫是 FeLV 阴性——病毒感染到癌症的平均诱导期 16.7 个月"
  implicit_premise: "假设荧光抗体检测代表真正的病毒状态（1970s 技术局限）；假设波士顿队列可外推到其他地区"
  unexpected_finding: "FeLV 阴性猫在老年猫中占主导——挑战了'猫白血病/淋巴瘤主要是病毒引起的'简单叙事——提示存在非病毒致癌途径或病毒清除后的迟发效应"
  title_gap: "标题说病毒阳性和病毒阴性猫白血病/淋巴瘤的比较，但真正发现是年龄分层：FeLV 阴性病例集中在老年猫——这种年龄-病毒状态关联在 1979 年是新发现"
  evidence_boundary: "历史性 FeLV 时代流行病学；支持历史比较背景，不支持当代患病率估计或治疗决策；检测技术已过时"
---

# Comparison of virus-positive and virus-negative cases of feline leukemia and lymphoma

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. 1979 Cancer Research: 184 leukemia/lymphoma cases Boston 1972-1976; 67% FeLV+, 33% FeLV-; FeLV- cats older (4.9 vs 3.5 years); 68% of cats >8 years were FeLV-; mean induction period 16.7 months. [Deep extraction worksheet](../../system/indexes/src-cancer-060-deep-extraction-round1.md).

## Source Check, 2026-06-01

PubMed abstract fetched as a zero-cost extraction step.

- PMID: 225010
- Journal: Cancer Research
- Year: 1979
- DOI: not listed in PubMed abstract output

## Abstract Summary

This historical case series compared virus-positive and virus-negative feline leukemia and lymphoma cases diagnosed in Boston from 1972 through 1976.

**Study design:**

| Feature | Abstract-Extracted Detail |
|---------|---------------------------|
| Cases | 184 feline leukemia and lymphoma cases |
| Location/time | Boston, 1972-1976 |
| Case mix | 58% lymphoma; 42% leukemia |
| Viral test | Fluorescent antibody test for circulating feline leukemia virus |

**Findings:**

- 67% of cats were virus-positive and 33% were virus-negative.
- Virus-positive and virus-negative cases were clinically and epidemiologically similar except for age at diagnosis.
- Virus-negative cats were older at diagnosis on average (4.9 years) than virus-positive cats (3.5 years).
- Among 22 cases diagnosed after 8 years of age, 15 were virus-negative.
- For 19 cats that were virus-positive and healthy at first test, the minimum mean induction period from first positive virus test to cancer diagnosis was 16.7 months, with a 2-41 month range.

**Boundary:** This is a historical Boston-era leukemia/lymphoma cohort. It supports FeLV-era comparison context, not contemporary prevalence or prognosis estimates.

## One-Line Summary

Historical Boston cohort comparing FeLV virus-positive and virus-negative feline leukemia/lymphoma cases, mainly useful for FeLV-era epidemiology context.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Comparison of virus-positive and virus-negative cases of feline leukemia and lymphoma.
- The intake sheet locator is: https://pubmed.ncbi.nlm.nih.gov/225010/.

### source_supported_conclusion

- This source supports historical FeLV-era comparison between virus-positive and virus-negative leukemia/lymphoma cases.
- Virus-negative cases skewed older in this cohort.
- The cohort should not be reused as a modern prevalence estimate.

### llm_inference

- This source may help lymphoma synthesis explain why FeLV-era literature needs date and testing-context labels.

## Claim-Fit Judgment

Strongest safe use:

- historical FeLV-era leukemia/lymphoma context
- virus-positive versus virus-negative comparison
- age-at-diagnosis caveat

Must not control yet:

- reader-facing medical advice
- contemporary prevalence estimates
- treatment decisions
- current FeLV risk quantification
- prognosis estimates

## Image Asset TODO

- figures to capture: unknown until source text is read
- why these matter: tables or figures should remain behind the candidate gate until labels are verified

## Open Follow-Up Questions

- Does the full text separate leukemia and lymphoma sufficiently for branch-specific use?
- What exact FeLV test method and case ascertainment limits should be carried forward?
- How should this historical cohort be contrasted with post-test-and-removal FeLV-era sources?

## Linked Entities

- diseases: cancer
- models: historical feline leukemia/lymphoma cohort
- endpoints: FeLV status; age at diagnosis; induction interval
- mechanisms: feline leukemia virus association
- regulations:
