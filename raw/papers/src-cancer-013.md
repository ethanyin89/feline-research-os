---
id: src-cancer-013
type: source
title: "Spontaneous feline mammary carcinoma is a model of HER2 overexpressing poor prognosis human breast cancer"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2005
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
pmid: 15705889
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, spontaneous, mammary, carcinoma, model, her2, overexpressing, poor]
links:
  doi: "10.1158/0008-5472.907.65.3"
  url: "https://aacrjournals.org/cancerres/article/65/3/907/518741/Spontaneous-Feline-Mammary-Carcinoma-Is-a-Model-of"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Spontaneous feline mammary carcinoma is a model of HER2 overexpressing poor prognosis human breast cancer."
    - "The intake sheet locator is: https://aacrjournals.org/cancerres/article/65/3/907/518741/Spontaneous-Feline-Mammary-Carcinoma-Is-a-Model-of."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
---

# Spontaneous feline mammary carcinoma is a model of HER2 overexpressing poor prognosis human breast cancer

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. Key 2005 Cancer Research paper: feline HER2 kinase domain 92% similar to human; 36-55% FMC show HER2 overexpression. Validates FMC as model for HER2+ poor prognosis human breast cancer. [Deep extraction worksheet](../../system/indexes/src-cancer-013-deep-extraction-round1.md).

## Full Abstract (PubMed)

Companion animal spontaneous tumors are suitable models for human cancer, primarily because both animal population and the tumors are genetically heterogeneous. Feline mammary carcinoma (FMC) is a highly aggressive, mainly hormone receptor-negative cancer, which has been proposed as a model for poor prognosis human breast cancer. We have identified and studied the feline orthologue of the HER2 gene, which is both an important prognostic marker and therapeutic target in human cancer. Feline HER2 (f-HER2) gene kinase domain is 92% similar to the human HER2 kinase. F-HER2-specific mRNA was found 3- to 18-fold increased in 3 of 3 FMC cell lines, in 1 of 4 mammary adenomas and 6 of 11 FMC samples using quantitative reverse transcription-PCR. Western blot showed that an anti-human HER2 antibody recognized a protein comigrating with the human p185HER2 in FMC cell lines. The same antibodies strongly stained 13 of 36 FMC archival samples. These data show that feline HER2 overexpression qualifies FMC as homologous to the subset of HER2 overexpressing, poor prognosis human breast carcinomas and as a suitable model to test innovative approaches to therapy of aggressive tumors.

## Key Extracted Findings

| Finding | Value | Boundary |
|---------|-------|----------|
| Feline HER2 homology | 92% similar to human HER2 kinase domain | molecular basis for model |
| FMC cell line HER2 mRNA | 3-18 fold increased in 3/3 cell lines | in vitro |
| FMC tumor HER2 mRNA | 6/11 (55%) samples increased | qRT-PCR |
| FMC archival HER2 staining | 13/36 (36%) strongly positive | IHC |
| Human antibody cross-reactivity | anti-human HER2 antibody recognizes feline HER2 | translational tool |
| Model qualification | FMC homologous to HER2+ poor prognosis human breast cancer | comparative oncology |

**Key insight:** The 92% kinase domain homology and cross-reactivity with human antibodies means HER2-targeted therapies developed for humans could potentially be tested in cats with naturally occurring HER2+ FMC.

**Boundary:** This establishes FMC as a HER2 model, not a treatment recommendation. HER2 positivity rate (36%) is from archival samples and may vary by population.

## One-Line Summary

2005 Cancer Research: Feline HER2 92% similar to human; 36% FMC are HER2+ — validates FMC as model for aggressive human breast cancer.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Spontaneous feline mammary carcinoma is a model of HER2 overexpressing poor prognosis human breast cancer.
- The intake sheet locator is: https://aacrjournals.org/cancerres/article/65/3/907/518741/Spontaneous-Feline-Mammary-Carcinoma-Is-a-Model-of.

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
