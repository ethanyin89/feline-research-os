---
id: src-cancer-058
type: source
title: "Myxoma virus induces apoptosis in cultured feline carcinoma cells"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2012
status: ingested
extraction_depth: abstract
verification_status: abstract_weighted
pmid: 22100245
doi: "10.1016/j.rvsc.2011.10.016"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, myxoma, virus, induces, apoptosis, cultured, carcinoma, cells]
links:
  doi: "10.1016/j.rvsc.2011.10.016"
  url: "https://www.sciencedirect.com/science/article/abs/pii/S0034528811004413?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Myxoma virus induces apoptosis in cultured feline carcinoma cells."
    - "The intake sheet locator is: https://www.sciencedirect.com/science/article/abs/pii/S0034528811004413?via%3Dihub."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
  # V2 enhanced fields
  study_design: "原始研究（2012 年 Res Vet Sci），两种猫癌细胞培养，黏液瘤病毒接种后观察"
  core_argument: "黏液瘤病毒在猫癌细胞培养中诱导凋亡——病毒蛋白表达和感染性颗粒产生被检测——原代猫癌细胞在接种后 48 小时内显示细胞死亡"
  implicit_premise: "假设体外溶瘤病毒敏感性可转化为体内治疗效果；假设黏液瘤病毒对正常猫细胞的安全性"
  unexpected_finding: "黏液瘤病毒（一种兔病毒）对猫癌细胞有溶瘤活性——这种跨物种溶瘤潜力在概念上令人惊讶——但需要体内验证"
  title_gap: "标题说黏液瘤病毒在培养的猫癌细胞中诱导凋亡，但真正发现是概念验证：这是体外溶瘤病毒敏感性信号——支持临床前可行性而非治疗效果"
  evidence_boundary: "体外溶瘤病毒证据；支持临床前敏感性信号，不支持猫的治疗效果；需要体内研究验证安全性和疗效"
---

# Myxoma virus induces apoptosis in cultured feline carcinoma cells

## Evidence-Depth Caveat

This is a second-pass abstract-extracted source card. The abstract was fetched from PubMed (PMID 22100245) and key findings were extracted at abstract level only.

## Source Check, 2026-06-02

PubMed abstract fetched as a zero-cost extraction step.

- PMID: 22100245
- DOI: 10.1016/j.rvsc.2011.10.016
- Journal: Research in Veterinary Science
- Year: 2012

## Abstract Summary

This study evaluated myxoma virus-induced oncolysis in two feline cancer cell cultures.

**Study design:**

| Feature | Abstract-Extracted Detail |
|---------|---------------------------|
| Model | Two feline cancer cell cultures |
| Intervention | Myxoma virus inoculation |
| Findings | Viral protein expression and infectious particle production were detected |
| Cell-death signal | Primary feline cancer cells showed cell death within 48 hours after inoculation |

**Boundary:** This is in vitro oncolytic-virus evidence. It supports a preclinical susceptibility signal, not treatment efficacy in cats.

## One-Line Summary

PubMed abstract supports this source as an in vitro myxoma-virus susceptibility signal in feline carcinoma cells, not as clinical therapy evidence.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Myxoma virus induces apoptosis in cultured feline carcinoma cells.
- The intake sheet locator is: https://www.sciencedirect.com/science/article/abs/pii/S0034528811004413?via%3Dihub.

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
