---
id: src-hcm-010
type: source
title: "Investigation into the use of plasma NT-proBNP concentration to screen for feline hypertrophic cardiomyopathy"
source_kind: paper
species: feline
diseases: [HCM]
models: []
endpoints: [nt-probnp]
jurisdictions: []
evidence_level: original-study
year: 2009
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [hcm, biomarker, screening]
links:
  doi: ""
  url: "https://www.sciencedirect.com/science/article/abs/pii/S1760273409000095?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The abstract states that the study evaluated NT-proBNP as a screening tool for cats with subclinical HCM."
    - "The abstract reports 40 adult Maine Coon or Maine Coon crossbred cats from a research colony, with echocardiography used to assess HCM severity."
    - "The abstract reports that NT-proBNP was significantly elevated in cats with severe HCM and that values above 44 pmol/L accurately predicted severe HCM."
    - "The abstract states that NT-proBNP was not increased in cats with moderate or equivocal HCM compared with normal cats."
    - "The abstract concludes that the test cannot be used to screen for mild to moderate HCM in that colony population."
  source_supported_conclusion:
    - NT-proBNP belongs to a screening-augmentation branch rather than pure phenotype-definition logic.
    - The study supports NT-proBNP as a severe-disease flag, not a sensitive screen for mild-to-moderate HCM.
    - The source is a key boundary paper for screening augmentation versus true diagnostic authority.
    - This paper is especially valuable because its most reusable contribution is a negative boundary: biomarker screening fails exactly where equivocal or milder phenotype recognition is hardest.
    - The study strengthens a use-case split in which NT-proBNP helps severe-burden flagging, while echocardiography retains authority for borderline and moderate structural disease.
  llm_inference:
    - This may become a key boundary paper for screening versus diagnosis.
    - HCM recognition pages should explicitly separate `severe-disease biomarker signal` from `general early screening competence`.
---

# One-line Summary

NT-proBNP screening paper that should anchor a separate screening-augmentation branch in HCM and explicitly prevent biomarker overclaim.

## Why It Matters For HCM

- gives the module a second major biomarker anchor after troponin
- helps separate screening logic from structural diagnosis
- now gives the HCM shell a safer first-pass rule that NT-proBNP is much stronger for severe HCM than for mild or equivocal disease

## Key Findings

- plasma NT-proBNP screening focus
- abstract shows strong signal for severe HCM but weak screening value for moderate or equivocal disease
- abstract concludes the test cannot be used to screen for mild to moderate HCM in the studied colony

## Why This Study Matters

This study matters because it turns the NT-proBNP branch from vague optimism into a real boundary.

The important point is not merely that NT-proBNP rises in some HCM cats. The paper asks a narrower screening question and then answers it in a use-case-specific way. Severe disease generates a usable signal, but moderate and equivocal disease do not. That is exactly the sort of distinction that keeps biomarker pages from becoming sloppy.

It is also useful because the paper's most important contribution is partly negative. It explicitly says the assay could not be used to screen for mild-to-moderate HCM in the studied colony population. That makes it much more valuable as a boundary-setting source than as a generic diagnostic success story.

## Screening Boundary Signal

The safest promotion from this source is:

- NT-proBNP is a severe-disease flag
- NT-proBNP is not reliable authority for mild or equivocal HCM screening
- biomarker screening and structural confirmation should remain separate branches
- colony-specific results should not be overgeneralized into universal practice language

That makes this card central for endpoint hierarchy even though it narrows rather than expands biomarker authority.

## Limits / Caveats

- current card is abstract-weighted, not full-text reviewed
- The cohort is colony-based and Maine Coon-heavy, so generalization should remain bounded.
- The source is strongest for screening-boundary logic, not for routine multimodal workup ranking across all clinical settings.

## Image Asset TODO

- figures to capture:
  - NT-proBNP threshold scatter
  - ROC curve or comparison table
- candidate target paths are tracked in [HCM image ingest manifest](../../system/indexes/hcm-image-ingest-manifest-20260417.md) until article labels are verified.

## Open Follow-up Questions

- how well does NT-proBNP perform as a screen?
- does the paper help define when biomarker screening adds value beyond imaging?
- how much of this colony-based result generalizes outside a Maine Coon research setting?
- how should NT-proBNP be separated from troponin in a stable HCM biomarker-use-case hierarchy?
- which equivocal or borderline phenotype states were hardest for NT-proBNP to detect?

## Linked Entities

- HCM
- NT-proBNP
