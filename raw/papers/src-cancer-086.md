---
id: src-cancer-086
type: source
title: "The frequency of occurrence of feline leukaemia virus subgroups in cats"
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
decision_grade: no
language_qa_status: not_applicable
pmid: 204584
tags: [cancer, FeLV, subgroups, lymphosarcoma, epidemiology, carrier-cats]
links:
  doi: "10.1002/ijc.2910210314"
  url: "https://doi.org/10.1002/ijc.2910210314"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "PubMed-indexed: Int J Cancer. 1978 Mar 15;21(3):334-7."
    - "Authors: Jarrett O, Hardy WD Jr, Golder MC, Hay D."
    - "All FeLV isolates contained subgroup A; high proportion also contained subgroup B."
    - "FeLV-C was rare, occurred only in cats with disease."
    - "In lymphosarcoma cats: 42% FeLV-A, 58% FeLV-AB."
    - "In healthy carriers: 65% FeLV-A, 33% FeLV-AB."
  source_supported_conclusion:
    - "FeLV subgroup composition differs between diseased and healthy carrier cats."
    - "FeLV-B more common in cats with lymphosarcoma than in healthy carriers."
    - "FeLV-C associated only with disease, not healthy carrier state."
  llm_inference:
    - "May inform lymphoma.md FeLV subgroup epidemiology section."
    - "Subgroup distribution relevant to disease risk assessment."
  # V2 enhanced fields
  study_design: "横断面流行病学研究（1978 年 Int J Cancer），Glasgow 和 New York 猫，淋巴肉瘤猫 vs 健康携带者 FeLV 亚群分布"
  core_argument: "FeLV 亚群组成在患病猫和健康携带者之间存在差异——FeLV-B 在淋巴肉瘤猫中更常见（58% vs 33%）——FeLV-C 仅在患病猫中出现——暗示 FeLV-B 和 FeLV-C 具有更高致病性"
  implicit_premise: "假设 Glasgow 和 New York 两地的 FeLV 亚群分布可代表更广泛人群；假设横断面关联可推断因果——FeLV-B 导致淋巴肉瘤而非淋巴肉瘤选择 FeLV-B"
  unexpected_finding: "多猫家庭中 FeLV-AB 混合感染的携带率（53%）高于 FeLV-A 单独感染（28%）——暗示 FeLV-B 可能增强传播效率或感染持续性"
  title_gap: "标题说猫中 FeLV 亚群出现频率，但真正发现是亚群-疾病关联：FeLV-B 富集于淋巴肉瘤——FeLV-C 排他性出现在患病猫——亚群组成可能是疾病风险指标"
  evidence_boundary: "早期流行病学证据（Jarrett/Hardy 实验室）；支持亚群-疾病关联声明，不直接支持因果机制——亚群致病性差异是推论"
---

# The frequency of occurrence of feline leukaemia virus subgroups in cats

## Source Check, 2026-06-03

| Field | Value |
|-------|-------|
| PMID | 204584 |
| DOI | 10.1002/ijc.2910210314 |
| Journal | Int J Cancer |
| Year | 1978 |
| Authors | Jarrett O, Hardy WD Jr, Golder MC, Hay D |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Sample source | Glasgow and New York cats |
| Population | Lymphosarcoma cats + healthy carrier cats |
| FeLV-A prevalence | 100% of isolates |
| FeLV-B in lymphosarcoma | 58% (vs 33% in healthy carriers) |
| FeLV-C | Rare, only in diseased cats |
| Carrier rate in MCH | 42% overall (28% in MCH-A, 53% in MCH-AB) |

**Boundary:** Abstract-level extraction. FeLV subgroup epidemiology findings can inform lymphoma etiology claims.

## One-Line Summary

FeLV subgroup distribution differs between lymphosarcoma cats (58% FeLV-AB) and healthy carriers (33% FeLV-AB); FeLV-C rare and only in diseased cats.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- All FeLV isolates contained subgroup A (FeLV-A)
- High proportion also contained subgroup B (FeLV-B)
- FeLV-C rare, occurred only in association with FeLV-A (and sometimes FeLV-B)
- In lymphosarcoma cats: 42% FeLV-A only, 58% FeLV-AB
- In healthy carrier cats: 65% FeLV-A only, 33% FeLV-AB
- FeLV-C isolated only from cats with disease, not healthy carriers
- Overall carrier rate in multi-cat households: 42%
- MCH-A (FeLV-A only): 28% viraemic; MCH-AB: 53% viraemic

### source_supported_conclusion

- FeLV subgroup B more frequently associated with lymphosarcoma than with healthy carrier state
- FeLV subgroup C exclusively associated with diseased cats
- Multi-cat households with FeLV-AB have higher carrier rates than FeLV-A only households

### llm_inference

- Key paper for lymphoma.md FeLV subgroup epidemiology section
- Subgroup distribution may inform disease risk assessment
- Historical foundation for understanding FeLV pathogenicity differences

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
