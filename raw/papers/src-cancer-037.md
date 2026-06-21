---
id: src-cancer-037
type: source
title: "A new detection method for canine and feline cancer using the olfactory system of nematodes"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
pmid: 36111250
year: 2022
doi: "10.1016/j.bbrep.2022.101332"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, new, detection, method, using, olfactory, system, nematodes]
links:
  doi: ""
  url: "https://www.sciencedirect.com/science/article/pii/S2405580822001327?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: A new detection method for canine and feline cancer using the olfactory system of nematodes."
    - "The intake sheet locator is: https://www.sciencedirect.com/science/article/pii/S2405580822001327?via%3Dihub."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
  # V2 enhanced fields
  study_design: "原始研究（2022 年 BBRC Reports），使用秀丽隐杆线虫趋化性检测犬猫尿液中的癌症信号"
  core_argument: "N-NOSE 线虫尿液测试对猫癌症检测显示 AUC 0.77-0.90——非侵入性筛查技术有早期诊断潜力"
  implicit_premise: "假设线虫对人类尿液癌症信号的趋化性可转移到犬猫；假设 AUC 值在更大验证队列中可重现"
  unexpected_finding: "线虫嗅觉系统可区分癌症和健康动物的尿液——这种跨物种癌症检测能力在犬猫中也有效——同一技术已商业化用于人类 15 种癌症筛查"
  title_gap: "标题说使用线虫嗅觉系统检测犬猫癌症的新方法，但真正限制是利益冲突：作者是测试开发公司（Hirotsu Bio Science Inc.）员工——单一研究需要独立验证"
  evidence_boundary: "早期验证研究；利益冲突（公司员工作者）；未指定癌症类型；临床应用前需要独立验证"
---

# A new detection method for canine and feline cancer using the olfactory system of nematodes

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. 2022 BBRC Reports: N-NOSE nematode urine test shows AUC 0.77-0.90 for feline cancer detection. Non-invasive screening technology, but single study with COI (company employees). [Deep extraction worksheet](../../system/indexes/src-cancer-037-deep-extraction-round1.md).

## Source Check, 2026-06-01

PubMed abstract fetched as a zero-cost extraction step.

- PMID: 36111250
- DOI: 10.1016/j.bbrep.2022.101332
- Journal: Biochemical and Biophysical Research Communications Reports
- Year: 2022
- Open access: yes

## Abstract Summary

This study evaluated N-NOSE (Nematode-NOSE), a cancer screening test using C. elegans chemotaxis to urine, for dogs and cats.

**Technology:**
- C. elegans nematodes show distinct chemotactic response to cancer patient urine
- Non-invasive screening using urine samples
- Already commercially available for human cancer screening (15 cancer types)

**Results:**

| Species | Cancer vs Healthy | Statistical Significance |
|---------|-------------------|-------------------------|
| Dogs | Significant difference | p < 0.01 |
| Cats | Significant difference | p < 0.04 |

**ROC Analysis (AUC values):**

| Species | Dilution 1 | Dilution 2 |
|---------|-----------|-----------|
| Dogs | 0.8114 | 0.7851 |
| Cats | 0.7667 | 0.9000 |

**Conclusion:**
N-NOSE shows potential as a simple, accurate, and low-cost cancer screening test for dogs and cats.

**Conflict of interest:** Authors are employees of Hirotsu Bio Science Inc. (test developer)

**Boundary:** This is early-stage validation research. Not yet a clinical recommendation for cancer screening.

## One-Line Summary

N-NOSE nematode-based urine test shows AUC 0.77-0.90 for feline cancer detection — emerging non-invasive screening technology.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: A new detection method for canine and feline cancer using the olfactory system of nematodes.
- The intake sheet locator is: https://www.sciencedirect.com/science/article/pii/S2405580822001327?via%3Dihub.

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
