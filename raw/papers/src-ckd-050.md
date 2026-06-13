---
id: src-ckd-050
type: source
title: "Characterisation of feline renal cortical fibroblast cultures and their transcriptional response to transforming growth factor β1"
source_kind: paper
species: feline
diseases: [CKD]
models: [primary feline renal cortical fibroblast culture]
endpoints: [fibrosis-associated gene expression]
jurisdictions: []
evidence_level: original-study
status: extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ckd, characterisation, cortical, fibroblast, cultures, their, transcriptional, response]
links:
  doi: "10.1186/s12917-018-1387-2"
  url: "https://doi.org/10.1186/s12917-018-1387-2"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Primary renal cortical fibroblast cultures were established from four normal cat kidneys."
    - "After 24-hour TGF-beta1 stimulation, 13 of 20 fibrosis-associated genes changed."
  source_supported_conclusion:
    - "Primary feline renal fibroblasts mount a TGF-beta-driven profibrotic transcriptional response in vitro."
  llm_inference:
    - "This supports TGF-beta pathway plausibility and model use, but not in-vivo CKD causation or treatment efficacy."
---

# Characterisation of feline renal cortical fibroblast cultures and their transcriptional response to transforming growth factor β1

## Evidence-Depth Caveat

Full text was checked. This is a four-donor, healthy-kidney, in-vitro experiment. It supports cell-level mechanism and model claims, not clinical efficacy, safety, dose, or spontaneous-CKD causation.

## One-Line Summary

Primary feline renal cortical fibroblasts responded to TGF-beta1 with a profibrotic transcriptional program, with selected responses attenuated by receptor inhibition.

## Why It Matters For Feline CKD

This source adds direct feline evidence beneath the review-led TGF-beta fibrosis branch and establishes a reusable primary renal fibroblast culture model.

### Context Within CKD Mechanism Map

TGF-beta is implicated in mammalian renal fibrosis, but feline-specific evidence was limited before this study. By demonstrating that cat kidney fibroblasts respond to TGF-beta1 with a profibrotic transcriptional program similar to other species, this source:

1. **Validates cross-species pathway conservation** - Feline renal cells mount the expected response
2. **Establishes a feline-specific experimental model** - Primary fibroblast cultures can be used for future mechanism and drug studies
3. **Provides target-engagement evidence** - SB431542 attenuation shows receptor-mediated signaling can be pharmacologically modulated

### Evidence Gap This Source Does NOT Fill

The vault still lacks CKD-derived feline tissue studies. This source used normal cat kidneys, not kidneys from cats with spontaneous CKD. The jump from in-vitro pathway activation to in-vivo disease progression or treatment benefit remains unvalidated.

## Key Findings

### quoted_fact

- Primary cultures were derived from the renal cortex of four normal cats.
- TGF-beta1 stimulation changed 13 of 20 fibrosis-associated genes.
- `ACTA2`, `COL1A1`, `COL4A1`, and `CTGF` increased, while `MMP1` and `MMP3` decreased.

### source_supported_conclusion

- The experiment directly supports feline renal fibroblast responsiveness to TGF-beta1.
- SB431542 attenuation of selected responses supports receptor-mediated pathway engagement in culture.

### llm_inference

- The model can support mediator and target-engagement experiments, but it cannot establish in-vivo treatment benefit.

## Claim-Fit Judgment

Strongest safe use:

- feline in-vitro renal fibrosis model
- TGF-beta pathway plausibility
- cell-level target-engagement evidence

Must not control yet:

- clinical dosing or treatment recommendations
- in-vivo efficacy or safety
- spontaneous CKD causation
- whole-kidney fibrosis outcomes

## Study Design Details

### Experimental System

| Parameter | Value |
|-----------|-------|
| Donor cats | 4 (normal kidneys) |
| Cell type | Primary renal cortical fibroblasts |
| Stimulation | TGF-beta1, 24 hours |
| Genes assessed | 20 fibrosis-associated genes |
| Inhibitor tested | SB431542 (TGF-beta receptor I inhibitor) |

### Gene Expression Changes After TGF-beta1 Stimulation

| Direction | Genes | Biological Meaning |
|-----------|-------|-------------------|
| Increased | ACTA2, COL1A1, COL4A1, CTGF | Myofibroblast program, ECM production |
| Decreased | MMP1, MMP3 | Reduced matrix degradation |
| Responsive to SB431542 | ACTA2, COL1A1, COL4A1, CTGF | Receptor-mediated response confirmed |

### Key Evidence Boundaries

- **Donor source:** Normal cat kidneys, not spontaneous CKD
- **Scale:** Four donors, in-vitro system only
- **Level:** Gene expression, not tissue fibrosis or clinical outcomes
- **SB431542 result:** Target-engagement evidence, not clinical efficacy
- **Strongest role:** Mechanism and model anchor, not therapeutic recommendation

### Repository Role

This source adds direct feline in-vitro support to the TGF-beta fibrosis branch and expands the CKD model map with a primary renal fibroblast culture model. The distinction between mechanistic plausibility and validated in-vivo intervention must be preserved.

## Deep Extraction

- [Round 1 worksheet](../../system/indexes/src-ckd-050-deep-extraction-round1.md)

## Linked Entities

- diseases: CKD
- models: primary feline renal cortical fibroblast culture
- endpoints: fibrosis-associated gene expression (ACTA2, COL1A1, COL4A1, CTGF, MMP1, MMP3)
- mechanisms: TGF-beta1 signaling, renal fibrosis, myofibroblast activation
- regulations: none applicable
