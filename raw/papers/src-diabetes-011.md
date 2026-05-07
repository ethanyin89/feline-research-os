---
id: src-diabetes-011
type: source
title: "SGLT2 inhibitor use in the management of feline diabetes mellitus"
source_kind: paper
species: feline
diseases: [diabetes mellitus]
models: []
endpoints: [glycemic-control, safety]
jurisdictions: []
evidence_level: review
year: 2024
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [diabetes, SGLT2, treatment, frontier]
links:
  doi: "10.1111/jvp.13466"
  url: "https://doi.org/10.1111/jvp.13466"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Bexagliflozin (Bexacat) and velagliflozin (Senvelgo) are FDA-approved SGLT2 inhibitors for feline diabetes."
    - "SGLT2 inhibitors are approved for uncomplicated feline diabetes mellitus."
    - "Suitable candidates require residual beta-cell function for SGLT2 inhibitor efficacy."
    - "Euglycemic diabetic ketoacidosis is a serious potential complication of SGLT2 inhibitor therapy."
    - "Patient selection criteria must be met before initiating SGLT2 inhibitor therapy."
    - "Ketone monitoring is required during SGLT2 inhibitor treatment."
    - "SGLT2 inhibitors work by increasing renal glucose excretion."
  source_supported_conclusion:
    - "This 2024 review establishes SGLT2 inhibitors as a legitimate treatment branch for selected diabetic cats."
    - "FDA approval for uncomplicated diabetes does not extend to complicated, insulin-dependent, or DKA-risk cases."
    - "Residual beta-cell function requirement means SGLT2 inhibitors are not universal first-line treatment."
    - "Euglycemic DKA risk mandates careful patient selection and ongoing ketone monitoring."
    - "The convenience of oral administration should not override safety and selection criteria."
  llm_inference:
    - "SGLT2 inhibitors represent a treatment option for selected patients, not a replacement for insulin in all cases."
    - "Patient selection should emphasize residual beta-cell function and absence of DKA risk factors."
    - "The regulatory and safety framework should guide treatment decisions, not marketing convenience."
---

# SGLT2 inhibitor use in the management of feline diabetes mellitus

## One-Line Summary

Recent treatment source for SGLT2 inhibitor use in feline diabetes management.

## Why It Matters For Feline Diabetes

- SGLT2 inhibitors can change the treatment architecture, but safety and selection boundaries matter
- should be handled as a frontier-treatment branch until deep-read

## Key Findings

- abstract-level extraction confirms SGLT2 inhibitors as a current feline treatment branch
- bexagliflozin and velagliflozin are named as recently FDA approved for uncomplicated feline diabetes
- candidate selection depends on residual beta-cell function
- euglycemic diabetic ketoacidosis is an explicit serious-complication concern
- later vault work has added primary U.S. regulatory and current-label cards for Bexacat and Senvelgo
- the paper should now be read as the clinical-review gateway into an SGLT2 branch whose strongest control layer lives in the FOI/current-label cards
- the source supports treatment-branch presence, not convenience-led treatment replacement

## Limits / Caveats

- extraction is abstract-weighted, not full-text
- do not generalize to complicated diabetes without label/source support
- do not rank Bexacat against Senvelgo from this review abstract
- do not infer EMA, UK, China, or global approval status from the U.S. source stack
- do not convert label dosing or monitoring statements into patient-specific clinical instructions

## SGLT2 Branch Logic

This source should be used to open the SGLT2 branch, not to finish it.

What can be promoted:

- SGLT2 inhibitors are now a real feline diabetes treatment branch.
- Bexagliflozin and velagliflozin are named as recently FDA-approved products for uncomplicated feline diabetes.
- Candidate selection requires residual beta-cell function.
- Euglycemic DKA belongs in the core safety boundary.

What should be held:

- SGLT2 as the preferred treatment for all cats
- use in complicated, insulin-dependent, insulin-treated, or DKA-risk cats without label-level support
- product superiority claims
- non-U.S. approval or availability claims
- direct comparison against insulin protocols without full-text clinical/comparator evidence

## Relationship To Regulatory Source Cards

The paper's abstract was the first reason the diabetes module needed a regulatory branch. The local vault now has the primary U.S. control stack:

- [src-reg-010 Bexacat FDA FOI](../../raw/regulations/src-reg-010-bexacat-fda-foi.md)
- [src-reg-011 Senvelgo FDA FOI](../../raw/regulations/src-reg-011-senvelgo-fda-foi.md)
- [src-reg-012 Bexacat current label](../../raw/regulations/src-reg-012-bexacat-current-label.md)
- [src-reg-013 Senvelgo current label](../../raw/regulations/src-reg-013-senvelgo-current-label.md)
- [diabetes SGLT2 current label control memo](../../system/indexes/diabetes-sglt2-current-label-control-memo.md)
- [diabetes SGLT2 label-section comparison memo](../../system/indexes/diabetes-sglt2-label-section-comparison-memo.md)

That stack changes the regulatory read from `review abstract says FDA approved` to `U.S. primary-source-backed and current-label-controlled branch`.

## Write-Back Implications

- [translation brief](../../topics/diabetes/translation-brief.md) should place SGLT2 as a selected-cat branch, not a treatment ladder leader.
- [regulatory brief](../../topics/diabetes/regulatory-brief.md) should cite the label/FOI cards for product-specific U.S. claims.
- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md) should preserve ketone/DKA and safety-monitoring endpoints.
- [synthesis index](../../topics/diabetes/synthesis-index.md) should treat SGLT2 as a label-controlled branch inside a wider diabetes architecture.

## Open Follow-Up Questions

- which cats are candidates or non-candidates?
- what safety monitoring is required?
- how does it compare with insulin-based management?

## Linked Entities

- diseases: diabetes mellitus
- models:
- endpoints: glycemic control, safety
- mechanisms: renal glucose excretion
- regulations:
