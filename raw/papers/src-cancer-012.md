---
id: src-cancer-012
type: source
title: "Prognostic factors for feline mammary tumors"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 1984
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
pmid: 6746390
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, prognostic, factors, mammary]
links:
  doi: "10.2460/javma.1984.185.02.201"
  url: "https://pubmed.ncbi.nlm.nih.gov/6746390/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Prognostic factors for feline mammary tumors."
    - "The intake sheet locator is: https://pubmed.ncbi.nlm.nih.gov/6746390/."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
---

# Prognostic factors for feline mammary tumors

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. Classic 1984 study of 100 cats establishing tumor size as the primary prognostic factor (P<0.0001). Small tumors (1-8 cm³) have best prognosis. Age and breed not prognostic. [Deep extraction worksheet](../../system/indexes/src-cancer-012-deep-extraction-round1.md).

## Full Abstract (PubMed)

The case records of 100 cats with malignant mammary tumors were reviewed. All cats were staged clinically according to the staging system of the World Health Organization. The following information was obtained from the medical records: age at time of diagnosis, breed, tumor size, date of surgery, type of surgical procedure performed, histologic type of tumor, disease-free interval, survival time, and cause of death. Factors of no prognostic value were age (less than or equal to 10 years vs greater than 10 years) and breed. Tumor size was the most significant prognostic factor (P less than 0.0001). Cats with small tumors (1 cm3 to 8 cm3) had the best prognosis. The type of surgery, conservative vs radical, was significantly (P less than 0.01) related to disease-free interval, but was of no significance in prolonging survival time.

## Key Extracted Findings

| Finding | Value | Boundary |
|---------|-------|----------|
| Study population | 100 cats with malignant mammary tumors | WHO staging |
| Most significant prognostic factor | tumor size (P<0.0001) | primary predictor |
| Best prognosis | small tumors (1-8 cm³) | size threshold |
| NOT prognostic | age (≤10 vs >10 years) | no significance |
| NOT prognostic | breed | no significance |
| Surgery type | affects disease-free interval (P<0.01) | but NOT survival time |
| Surgery type | conservative vs radical | no survival difference |

**Boundary:** This is a 1984 study. Treatment modalities and staging may have evolved. Core finding (tumor size as primary prognostic factor) remains foundational.

## One-Line Summary

Candidate cancer source from sheet row 13. Use it for triage until abstract or full-text extraction proves a stronger role.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Prognostic factors for feline mammary tumors.
- The intake sheet locator is: https://pubmed.ncbi.nlm.nih.gov/6746390/.

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
