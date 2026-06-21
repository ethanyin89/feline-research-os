---
id: src-cancer-029
type: source
title: "Frequency of Canine and Feline Tumors in a Defined Population"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 1978
status: ingested
extraction_depth: abstract
verification_status: abstract_weighted
pmid: 220774
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, frequency, defined, population]
links:
  doi: "10.1177/030098587801500602"
  url: "https://doi.org/10.1177/030098587801500602"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Crossref metadata resolves this DOI and reports abstract availability for source scope checking."
    - "Crossref container: Veterinary Pathology; year: 1978."
  source_supported_conclusion:
    - "This card is abstract-weighted only; it can guide navigation and extraction priority."
    - "It must not support reader-facing clinical claims until a full abstract extraction or source worksheet is completed."
  llm_inference:
    - "High-reuse guideline, review, treatment-control, or risk-architecture sources remain candidates for deep extraction."
  # V2 enhanced fields
  study_design: "基于人群的前瞻性登记研究（1978 年），美国第二个动物肿瘤登记处，Tulsa 地区定义人群，组织学确认"
  core_argument: "猫的肿瘤发生率约 0.5%（11,909 只），淋巴肉瘤是猫最常见肿瘤——猫的良性肿瘤发生率仅为犬的十分之一，恶性肿瘤发生率相似"
  implicit_premise: "假设登记期间的群体特征可代表一般伴侣动物群体；假设组织学确认标准在登记期间保持一致"
  unexpected_finding: "犬的良性肿瘤发生率是猫的 10 倍以上——但恶性肿瘤发生率两种动物相似——这种良性/恶性比例的物种差异在当时是新发现"
  title_gap: "标题说定义人群中犬猫肿瘤频率，但真正价值是基线数据：这是美国第二个基于人群的动物肿瘤登记处——提供真正的发病率估计而非转诊偏倚的医院数据"
  evidence_boundary: "1978 年数据，FeLV 疫苗前时代——淋巴肉瘤高发可能反映当时 FeLV 流行率；现代发病率模式可能已改变"
---

# Frequency of Canine and Feline Tumors in a Defined Population

## Evidence-Depth Caveat

This is an abstract-weighted source card. Foundational 1978 US registry study providing population-based tumor frequency data.

## Full Abstract (PubMed)

The Tulsa Registry of Canine and Feline Neoplasms was the second animal tumor registry in the United States concerned with a defined population in a delimited geographic area. Only tumors histologically confirmed by registry pathologists were included in frequency statistics based on the annual dog and cat population presented to veterinarians. During the first registry year, about 1% of the 63,504 dogs and 0.5% of the 11,909 cats had one or more primary tumors. While the incidence rate for malignant tumors in dogs was similar to that in cats, the incidence of benign tumors of dogs was over 10 times that of cats. The most common tumors were sebaceous adenoma in dogs and lymphosarcoma in cats. Mammary cancer was the most common malignant tumor in dogs.

## Key Extracted Findings

| Finding | Value | Boundary |
|---------|-------|----------|
| Registry type | Tulsa Registry, defined population | second US animal tumor registry |
| Dog tumor rate | ~1% of 63,504 dogs annually | histologically confirmed |
| Cat tumor rate | ~0.5% of 11,909 cats annually | histologically confirmed |
| Malignant tumor incidence | similar in dogs and cats | comparable malignancy rates |
| Benign tumor incidence | dogs 10x more than cats | species difference |
| Most common in cats | lymphosarcoma | #1 feline tumor type |
| Most common malignant in dogs | mammary cancer | species comparison |

**Registry methodology note:** This is a population-based registry with defined denominator, making it valuable for true incidence estimates rather than referral-biased hospital populations.

**Key insight:** Lymphosarcoma (lymphoma) was the most common tumor in cats in this 1978 defined population — supports lymphoma as a major feline cancer category.

## One-Line Summary

Candidate cancer source from sheet row 32. Use it for triage until abstract or full-text extraction proves a stronger role.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Frequency of Canine and Feline Tumors in a Defined Population.
- The intake sheet locator is: 10.1177/030098587801500602.

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
