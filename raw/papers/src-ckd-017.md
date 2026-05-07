---
id: src-ckd-017
type: source
title: "Clinicopathologic and pathologic characteristics of feline proteinuric kidney disease"
source_kind: paper
species: feline
diseases: [CKD]
models: []
endpoints: [upcr]
jurisdictions: []
evidence_level: original-study
year: 2020
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ckd, proteinuria, clinicopathology, pathology, original-study]
links:
  doi: "10.1177/1098612X20921056"
  url: "https://journals.sagepub.com/doi/10.1177/1098612X20921056"
  local_assets:
    - raw/images/ckd/src-ckd-017-outcome-upc-by-subtype-table.png
    - raw/images/ckd/src-ckd-017-imaging-pathology-classification-panel.jpg
evidence_policy:
  quoted_fact:
    - "The aim of the study was to describe the causes, clinicopathologic features and outcomes of feline protein-losing nephropathy, defined as proteinuria secondary to glomerular disease."
    - "Kidney biopsy or necropsy samples from proteinuric cats submitted to the International Veterinary Renal Pathology Service were retrospectively reviewed."
    - "Fifty-eight percent (31/53) of proteinuric cats had immune-complex glomerulonephritis (ICGN)."
    - "Seventy-four percent (31/42) of cats with protein-losing nephropathy had ICGN."
    - "Cats with glomerular diseases other than ICGN had a higher median UPC than ICGN cats (14.5 vs 6.5; P <0.001)."
    - "The median age at diagnosis was 3.5 years in ICGN cats versus 1.3 years in cats with other glomerular diseases (P = 0.026)."
    - "Renal proteinuria in cats can be caused by both tubular and glomerular disease."
    - "In feline CKD, proteinuria is typically secondary to tubular dysfunction and glomerulosclerosis, which increase in prevalence with disease severity."
  source_supported_conclusion:
    - This is one of the strongest primary-study anchors for making the proteinuria branch more compartment-aware and less generic.
    - UPC should remain a core bridge variable, but its interpretation must stay tied to disease compartment and pathology context rather than magnitude alone.
    - Some feline proteinuria reflects primary glomerular disease directly, so the vault should not flatten all proteinuric cats into one diffuse older-cat CKD story.
    - This source strengthens the case for keeping proteinuria close to pathology and junction pages, not only inside staging logic.
    - Proteinuria-oriented treatment or prognosis claims should preserve subset caution because this study is narrower than the whole CKD population.
  llm_inference:
    - The proteinuria branch should now distinguish `proteinuria as glomerular disease signal` from `proteinuria as secondary CKD progression signal`.
    - A future dedicated proteinuric-subset note would be justified if the vault starts answering more subtype-specific questions.
---

# Clinicopathologic and pathologic characteristics of feline proteinuric kidney disease

## One-Line Summary

This primary-study paper shows that feline proteinuric kidney disease is often glomerular and frequently immune-complex mediated, with high UPC values, young age at onset in many cases, and important clinicopathologic consequences, making it one of the strongest current anchors for the proteinuria branch.

## Why It Matters For CKD

Proteinuria is already a major bridge variable in the vault. This looks like a high-value source for making that branch more primary-study grounded.

## Key Findings

### quoted_fact

- The aim of the study was to describe the causes, clinicopathologic features and outcomes of feline protein-losing nephropathy, defined as proteinuria secondary to glomerular disease.
- Kidney biopsy or necropsy samples from proteinuric cats submitted to the International Veterinary Renal Pathology Service were retrospectively reviewed.
- Fifty-eight percent (31/53) of proteinuric cats had immune-complex glomerulonephritis (ICGN).
- Seventy-four percent (31/42) of cats with protein-losing nephropathy had ICGN.
- Cats with glomerular diseases other than ICGN had a higher median UPC than ICGN cats (14.5 vs 6.5; P <0.001).
- Onset of protein-losing nephropathy occurred at a young age, with a median age at diagnosis of 3.5 years in ICGN cats versus 1.3 years in cats with other glomerular diseases (P = 0.026).
- Renal proteinuria in cats can be caused by both tubular and glomerular disease.
- In feline CKD, proteinuria is typically secondary to tubular dysfunction and glomerulosclerosis, which increase in prevalence with disease severity.
- UPC magnitude alone does not collapse all proteinuric pathology into one disease bucket.

### source_supported_conclusion

- This is a high-value primary-study source for strengthening the UPCR/proteinuria axis.
- The paper sharpens an important distinction in the vault: proteinuria in cats is not one thing. It may reflect glomerular disease directly, but in broader CKD it may also arise secondarily alongside tubular dysfunction and glomerulosclerosis.
- UPC should remain a central bridge variable, but interpretation depends on disease compartment and clinical context.
- This source strengthens the case for keeping proteinuria close to pathology-correlations rather than treating it only as a staging number.
- This source also keeps the hypertension-proteinuria branch honest by showing that not every proteinuric cat belongs to the same hemodynamic story.

### llm_inference

- This is one of the best current sources for turning the proteinuria branch from “important marker” into “marker with clearer compartment-level meaning.”
- It also suggests that some proteinuric feline renal disease sits outside the older-cat spontaneous CKD stereotype, because onset here can be relatively young.

## Why This Study Matters

This paper matters because it stops the vault from treating proteinuria as one flat clinical signal.

The safe upgrade is:

- proteinuria is still a major endpoint
- some proteinuria is primary glomerular disease
- some proteinuria is secondary CKD context
- UPC is valuable, but still not self-interpreting

That makes this study high-value for both endpoint and pathology-aware compilation.

## Limits / Caveats

- Current extraction is abstract-led plus visible introduction/results content, not full section-by-section extraction.
- This paper focuses on proteinuric kidney disease and protein-losing nephropathy, so generalization to the whole feline CKD population must remain cautious.
- The source is strongest for compartment-aware interpretation of proteinuria, not for universal CKD prevalence or treatment ranking.

## Image Asset TODO

- figures to capture:
  - renal pathology classification figure or representative biopsy panels
  - UPC-by-subtype plot or comparison table
  - lesion distribution table across ICGN versus other glomerular disease
- why these matter:
  - this source is one of the best proteinuria compartment anchors, and pathology panels would materially sharpen that distinction
  - subtype plots may change how the UPCR branch is explained in endpoint and pathology pages
  - image-linked lesion evidence is more reusable than prose alone for glomerular versus secondary-proteinuria separation

## Open Follow-Up Questions

- Which lesions correlate most strongly with proteinuria in this study?
- Does it change how UPCR should be positioned in the endpoint handbook?
- Does it support a separate proteinuric CKD note later?
- How often did hypertension, hypoalbuminemia, or azotemia develop across subtypes?
- Which pathological categories other than ICGN were most important?

## Linked Entities

- diseases: CKD
- models:
- endpoints: UPCR
- mechanisms:
- regulations:
