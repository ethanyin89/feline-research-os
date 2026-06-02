---
id: src-cancer-059
type: source
title: "Feline STK gene expression in mammary carcinomas"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2002
status: ingested
extraction_depth: abstract
verification_status: abstract_weighted
pmid: 11896610
doi: "10.1038/sj.onc.1205221"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, stk, gene, expression, mammary, carcinomas]
links:
  doi: "10.1038/sj.onc.1205221"
  url: "https://www.nature.com/articles/1205221"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Feline STK gene expression in mammary carcinomas."
    - "The intake sheet locator is: https://www.nature.com/articles/1205221."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
---

# Feline STK gene expression in mammary carcinomas

## Evidence-Depth Caveat

This is a second-pass abstract-extracted source card. The abstract was fetched from PubMed (PMID 11896610) and key findings were extracted at abstract level only.

## Source Check, 2026-06-02

PubMed abstract fetched as a zero-cost extraction step.

- PMID: 11896610
- DOI: 10.1038/sj.onc.1205221
- Journal: Oncogene
- Year: 2002

## Abstract Summary

This study identified feline `stk` and examined its expression in feline mammary cancer as a comparative model for human breast cancer receptor biology.

**Study design:**

| Feature | Abstract-Extracted Detail |
|---------|---------------------------|
| Target | Feline `stk`, homologous to MET-family receptor genes |
| Expression assays | RT-PCR, Western blot, immunohistochemistry |
| Samples | 7/8 feline mammary carcinomas and a synchronous skin metastasis by RT-PCR; 10/34 archival mammary carcinoma samples stained by antibody |
| Interpretation | The abstract states the feline STK pattern could be superimposed on human RON receptor distribution in breast cancer |

**Boundary:** This is abstract-level molecular-comparative evidence. It does not establish feline clinical biomarker utility or treatment selection.

## One-Line Summary

PubMed abstract supports this source as feline mammary carcinoma STK/RON-comparative molecular evidence, not as a clinical biomarker recommendation.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Feline STK gene expression in mammary carcinomas.
- The intake sheet locator is: https://www.nature.com/articles/1205221.

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
