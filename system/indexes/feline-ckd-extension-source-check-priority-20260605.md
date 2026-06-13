---
id: feline-ckd-extension-source-check-priority-20260605
type: system
topic: content-pipeline
question_type: source-check-report
language: zh
last_compiled_at: 2026-06-05
verification_status: generated
decision_grade: no
owner: codex
status: active
---

# Feline Source Metadata Check, 2026-06-05

Source set: `CKD Google Sheet priority extension metadata check, 2026-06-05`

## Rule

This report is a repeatable second-pass source check. It does not make clinical claims.

- DOI metadata alone does not upgrade a card.
- Abstract availability can justify `abstract_weighted` only for navigation and extraction priority.
- Full-text or structured worksheet review is still required before `source_checked` or `deep_extracted`.

## Summary

- Cards checked: `5`
- Crossref metadata found: `3`
- Abstract available: `3`

## Check Table

| Source | Current | Recommended | DOI | Year | Container | Abstract | Error |
|---|---|---|---|---:|---|---|---|
| `src-ckd-031` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-ckd-032` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-ckd-033` | `title_only` | `abstract_weighted` | `10.1177/1098612x12469522` | 2013 | Journal of Feline Medicine and Surgery | `yes` |  |
| `src-ckd-034` | `title_only` | `abstract_weighted` | `10.1177/1098612x15625453` | 2017 | Journal of Feline Medicine and Surgery | `yes` |  |
| `src-ckd-035` | `title_only` | `abstract_weighted` | `10.1177/1098612x12461007` | 2013 | Journal of Feline Medicine and Surgery | `yes` |  |

## Abstract Availability Notes

### `src-ckd-031`

- Metadata check failed: no DOI in source card

### `src-ckd-032`

- Metadata check failed: no DOI in source card

### `src-ckd-033`

- Crossref title: Urinary tract infections in cats with chronic kidney disease
- Abstract lead for scope check only: Routine urine cultures were performed in cats with chronic kidney disease (CKD) to assess the overall prevalence and clinical signs associated with a positive urine culture (PUC)....
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-ckd-034`

- Crossref title: Risk and protective factors for cats with naturally occurring chronic kidney disease
- Abstract lead for scope check only: Objectives Chronic kidney disease (CKD) is a significant disease in cats. Identifying risk and protective factors may help to prevent this significant disease. Methods An age-matc...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-ckd-035`

- Crossref title: Urinary cytokine levels in apparently healthy cats and cats with chronic kidney disease
- Abstract lead for scope check only: Chronic kidney disease (CKD) is a common cause of illness and death in cats. The hallmark of CKD in cats is chronic tubulointerstitial nephritis, and inflammation contributes to t...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.
