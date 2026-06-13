---
id: src-cancer-049
type: source
title: "TiHo-0906: a new feline mammary cancer cell line with molecular, morphological, and immunocytological characteristics of epithelial to mesenchymal transition"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2018
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
pmid: "30185896"
pmcid: "PMC6125410"
doi: "10.1038/s41598-018-31682-1"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, tiho-0906, new, mammary, cell, line, molecular, morphological]
links:
  doi: "10.1038/s41598-018-31682-1"
  url: "https://www.nature.com/articles/s41598-018-31682-1"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "TiHo-0906 CNVs affect genomic regions with EMT/breast cancer genes: AKT1, GATA3, CCND2, CDK4, ZEB1, KRAS, HMGA2, ESRP1, MTDH, YWHAZ, MYC."
    - "Most CNVs located in amplified regions of FCAs B4 and F2."
    - "TiHo-0906 cells slightly positive for hormonal receptors (ER, PR) and HER-2."
    - "Doubling time 28.9h (low passage), 27.4h (high passage)."
    - "HMGA2 and CD44 expression significantly higher than reference tissue."
    - "Doxorubicin resistance: metabolic activity significantly decreases only at 100nM."
  source_supported_conclusion:
    - "TiHo-0906 is a stable FMC cell line co-expressing epithelial and mesenchymal markers."
    - "CNV profiles overlap with human metaplastic breast cancer genes."
    - "FCA F2 CNGs correspond to human HSA 8q (common breast cancer aberration)."
    - "Cell line shows EMT-like properties relevant to metastatic cancer research."
  llm_inference:
    - "TiHo-0906 may serve as model for studying doxorubicin resistance in FMC."
    - "EMT markers (HMGA2, CD44) could be therapeutic targets."
---

# TiHo-0906: a new feline mammary cancer cell line with molecular, morphological, and immunocytological characteristics of epithelial to mesenchymal transition

## Evidence-Depth Caveat

**Deep-extracted from PMC full text (PMC6125410).** 2018 Sci Rep: TiHo-0906 cell line from spindle-cell FMC; EMT markers (HMGA2↑, CD44↑); CNVs affect FCAs B4/F2 (orthologous to human 8q breast cancer aberrations); co-expresses epithelial (CK) and mesenchymal (vimentin) markers; doxorubicin resistance (IC50 ~100nM). Evidence level: original study with NGS, IHC, and functional assays.

## Source Check, 2026-06-10

Europe PMC full text extraction.

| Field | Value |
|-------|-------|
| PMID | 30185896 |
| PMCID | PMC6125410 |
| DOI | 10.1038/s41598-018-31682-1 |
| Journal | Sci Rep (Nature) |
| Year | 2018 |
| Authors | Buendia AJ, Soler MD, Garijo N, et al. |
| Open access | yes |

## Abstract Summary

This study established and characterized TiHo-0906, a feline mammary cancer cell line with epithelial-to-mesenchymal transition (EMT)-like properties.

**Model context:**

| Feature | Abstract-Extracted Detail |
|---------|---------------------------|
| Source tumor | Feline mammary carcinoma with anaplastic and malignant spindle cells |
| Human comparator | Human metaplastic breast carcinoma, spindle-cell subtype |
| Cell line | TiHoCMglAdcar0906 (TiHo-0906) |
| Characterization methods | CNV profiling, immunohistochemistry comparison, qPCR for HMGA2 and CD44, growth, migration, doxorubicin sensitivity |

**Key findings:**

- TiHo-0906 showed epithelial/mesenchymal phenotype and high HMGA2 and CD44 expression.
- Copy-number variations affected regions containing EMT-, breast-cancer-, and human metaplastic breast-cancer-associated genes, including AKT1, GATA3, CCND2, CDK4, ZEB1, KRAS, HMGA2, ESRP1, MTDH, YWHAZ, and MYC.
- Growth and migration remained comparable during subculturing.
- Low-passaged cells were two-fold more resistant to doxorubicin than high-passaged cells (IC50 99.97 nM vs 41.22 nM).

**Boundary:** This is cell-line and comparative-oncology tool evidence. It should not be converted into patient-level prognosis or treatment-response claims.

## One-Line Summary

TiHo-0906 is an EMT-like feline mammary cancer cell line derived from a poorly differentiated spindle-cell tumor, useful as a research model rather than clinical guidance.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: TiHo-0906: a new feline mammary cancer cell line with molecular, morphological, and immunocytological characteristics of epithelial to mesenchymal transition.
- The intake sheet locator is: https://www.nature.com/articles/s41598-018-31682-1.

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
