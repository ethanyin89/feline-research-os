---
id: src-cancer-103
type: source
title: "Letrozole + ribociclib versus letrozole + placebo as neoadjuvant therapy for ER+ breast cancer (FELINE trial)"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
status: ingested
extraction_depth: partial
year: 2020
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, letrozole, ribociclib, versus, placebo, neoadjuvant, therapy, breast]
links:
  doi: "10.1200/jco.2020.38.15_suppl.505"
  url: "https://doi.org/10.1200/jco.2020.38.15_suppl.505"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Crossref resolves metadata and reports abstract availability for source scope checking."
    - "Resolved container: Journal of Clinical Oncology; year: 2020."
  source_supported_conclusion:
    - "This card is abstract-weighted only; it can guide navigation and extraction priority."
    - "It must not support reader-facing clinical claims until a full abstract extraction or source worksheet is completed."
  llm_inference:
    - "High-reuse guideline, review, treatment-control, or risk-architecture sources remain candidates for deep extraction."
  # V2 enhanced fields
  study_design: "人类乳腺癌临床试验（FELINE trial），非猫研究——FELINE是试验名称缩写，不是物种"
  core_argument: "此来源是人类临床试验误收录——FELINE是试验名称缩写（Femara and Ribociclib），与猫物种无关，应从猫癌症模块移除"
  implicit_premise: "N/A——误收录到猫癌症来源库"
  unexpected_finding: "N/A——误收录"
  title_gap: "标题中的FELINE是试验名称缩写（Femara and Ribociclib in the Neoadjuvant Endocrine Setting），但被误认为是猫研究——应标记为非猫来源并移除"
  evidence_boundary: "人类临床试验（2020年JCO），不适用于猫癌症模块；标记为误收录待清理"
---

# Letrozole + ribociclib versus letrozole + placebo as neoadjuvant therapy for ER+ breast cancer (FELINE trial)

## Evidence-Depth Caveat

This is a second-pass abstract-available source card. It verifies Crossref abstract availability for source triage, but it is not a full abstract extraction or full-text read.

## Source Check, 2026-06-13

Crossref was checked as a repeatable second-pass intake step.

- Metadata resolved: yes
- Metadata provider: Crossref
- Container: Journal of Clinical Oncology
- Year: 2020
- Abstract available: yes

Use boundary:

- This card may guide navigation and extraction priority.
- It must not support reader-facing clinical claims until a full abstract extraction or source worksheet is completed.

Abstract lead for scope check only: 505 Background: Ribociclib (R) + letrozole (L) is superior to L in metastatic breast cancer (BC). Preoperative endocrine prognostic index (PEPI) score 0 after neoadjuvant endocrin...

## One-Line Summary

Candidate cancer source from sheet row 20. Use it for triage until abstract or full-text extraction proves a stronger role.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Letrozole + ribociclib versus letrozole + placebo as neoadjuvant therapy for ER+ breast cancer (FELINE trial).
- The intake sheet locator is: 10.1200/jco.2020.38.15_suppl.505.

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
