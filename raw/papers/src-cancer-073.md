---
id: src-cancer-073
type: source
title: "Expression of mPGES1 and p16 in feline and human oral squamous cell carcinoma: A comparative oncology approach"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2024
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
pmid: 38378135
tags: [cancer, FOSCC, HOSCC, mPGES1, p16, COX-2, CD147, comparative-oncology, inflammation]
links:
  doi: "10.1111/vco.12967"
  url: "https://doi.org/10.1111/vco.12967"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "42 HOSCC and 45 FOSCC samples analyzed."
    - "High p16 expression more common in HOSCC tumour cells vs adjacent stroma/epithelium."
    - "High mPGES1 in FOSCC more common in adjacent epithelium than other compartments."
    - "High CD147 HOSCC tumours more common in high mPGES1 group."
  source_supported_conclusion:
    - "Different expression patterns in FOSCC and HOSCC may relate to different risk factors."
    - "p16 is marker of papillomavirus-driven HOSCC; causal relationship in FOSCC not definitively demonstrated."
  llm_inference:
    - "Supports comparative oncology value of FOSCC model while noting species differences."
    - "Inflammation markers (COX-2, mPGES1) relevant for FOSCC pathogenesis."
---

# Expression of mPGES1 and p16 in feline and human oral squamous cell carcinoma: A comparative oncology approach

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. 2024 Vet Comp Oncol: 45 FOSCC vs 42 HOSCC compared; p16 patterns differ (HPV marker in humans); mPGES1 higher in adjacent epithelium in FOSCC; species-specific risk factors; FOSCC may model HPV-negative HOSCC. [Deep extraction worksheet](../../system/indexes/src-cancer-073-deep-extraction-round1.md).

## Source Check, 2026-06-02

| Field | Value |
|-------|-------|
| PMID | 38378135 |
| DOI | 10.1111/vco.12967 |
| Journal | Vet Comp Oncol |
| Year | 2024 |
| Authors | Nasry WHS, Jones K, Rodriguez-Lecompte JC, et al. |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Sample size | 42 HOSCC, 45 FOSCC |
| p16 expression | Higher in HOSCC tumor cells vs stroma; similar but NS trend in FOSCC |
| mPGES1 in FOSCC | Higher in adjacent epithelium than tumor/stroma |
| mPGES1 in HOSCC | More similar between compartments |
| CD147 correlation | High CD147 more common in high mPGES1 HOSCC |
| Species difference | Different expression patterns may relate to different risk factors |

**Boundary:** Abstract-level extraction. Comparative study highlights both similarities and differences between FOSCC and HOSCC.

## One-Line Summary

Comparative study of 45 FOSCC vs 42 HOSCC showing different mPGES1/p16 expression patterns, suggesting species-specific risk factors and pathogenesis.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- 45 FOSCC and 42 HOSCC samples with known COX-2 and CD147 expression
- High p16 more common in HOSCC tumor cells than adjacent stroma/epithelium
- High mPGES1 in FOSCC more common in adjacent epithelium than tumor
- High CD147 HOSCC tumors more common in high mPGES1 group
- p16 is marker of papillomavirus-driven HOSCC; causal role in FOSCC not definitively demonstrated

### source_supported_conclusion

- FOSCC and HOSCC share some inflammatory pathway features
- Different expression patterns may reflect species-specific risk factors
- COX-2 and mPGES1 both contribute to tumor inflammation

### llm_inference

- Supports comparative oncology value while noting species differences
- Important nuance: p16/HPV relationship validated in human but not feline OSCC
- May inform oral-squamous-cell-carcinoma.md claims about inflammation and comparative model validity

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
