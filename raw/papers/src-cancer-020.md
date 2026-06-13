---
id: src-cancer-020
type: source
title: "Feline Mammary Tumors"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: review
year: 1985
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
pmid: 3874468
doi: "10.1016/s0195-5616(85)50054-6"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, mammary]
links:
  doi: "10.1016/s0195-5616(85)50054-6"
  url: "https://www.sciencedirect.com/science/article/abs/pii/S0195561685500546?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Feline Mammary Tumors."
    - "The intake sheet locator is: https://www.sciencedirect.com/science/article/abs/pii/S0195561685500546?via%3Dihub."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
---

# Feline Mammary Tumors

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. 1985 Vet Clin NA foundational clinical review: FMC has rapid growth + high recurrence + poor survival → management triad of early diagnosis, aggressive surgery, frequent follow-up. Historical context. [Deep extraction worksheet](../../system/indexes/src-cancer-020-deep-extraction-round1.md).

## Full Abstract (PubMed)

The characteristics of feline mammary cancer--that is, the rapid growth of primary mammary tumors, the high rate of tumor recurrence, and the poor survival statistics--demonstrate the need for (1) early diagnosis of the primary tumor; (2) immediate, aggressive surgical therapy; and (3) frequent follow-up examinations to detect early clinical signs of recurrent disease. A number of factors that influence prognosis have been described. As more information becomes available concerning the behavior of feline mammary tumors and the results of various forms of treatment, more effective protocols can be developed. Continued etiologic research may play a vital role in determining the direction of therapy.

## Key Extracted Findings

| Finding | Value | Boundary |
|---------|-------|----------|
| Tumor characteristics | rapid growth, high recurrence, poor survival | aggressive behavior |
| Management need #1 | early diagnosis of primary tumor | clinical recommendation |
| Management need #2 | immediate, aggressive surgical therapy | treatment approach |
| Management need #3 | frequent follow-up exams for recurrence | monitoring strategy |
| Prognostic factors | multiple factors influence prognosis | mentioned, not detailed |

**Key insight:** This 1985 paper established the aggressive nature of FMC (rapid growth, high recurrence, poor survival) and the foundational management triad: early diagnosis, aggressive surgery, frequent follow-up. This clinical framing remains relevant.

**Boundary:** This is a 1985 review. Treatment protocols and prognostic factor understanding have evolved significantly. Historical context.

## One-Line Summary

1985 VCNA: FMC has rapid growth + high recurrence + poor survival → needs early diagnosis, aggressive surgery, frequent follow-up.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Feline Mammary Tumors.
- The intake sheet locator is: https://www.sciencedirect.com/science/article/abs/pii/S0195561685500546?via%3Dihub.

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
