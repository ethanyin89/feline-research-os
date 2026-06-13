---
id: feline-ckd-extension-source-check-sample-20260605
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

Source set: `CKD Google Sheet extension sample metadata check, 2026-06-05`

## Rule

This report is a repeatable second-pass source check. It does not make clinical claims.

- DOI metadata alone does not upgrade a card.
- Abstract availability can justify `abstract_weighted` only for navigation and extraction priority.
- Full-text or structured worksheet review is still required before `source_checked` or `deep_extracted`.

## Summary

- Cards checked: `6`
- Crossref metadata found: `4`
- Abstract available: `2`

## Check Table

| Source | Current | Recommended | DOI | Year | Container | Abstract | Error |
|---|---|---|---|---:|---|---|---|
| `src-ckd-025` | `title_only` | `abstract_weighted` | `10.1111/vru.13102` | 2022 | Veterinary Radiology &amp; Ultrasound | `yes` |  |
| `src-ckd-026` | `title_only` | `abstract_weighted` | `10.1177/1040638720985563` | 2021 | Journal of Veterinary Diagnostic Investigation | `yes` |  |
| `src-ckd-027` | `title_only` | `title_only` | `10.1080/01652176.2024.2447601` | 2025 | Veterinary Quarterly | `no` |  |
| `src-ckd-028` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-ckd-029` | `title_only` | `title_only` | `10.1007/s11259-018-9719-z` | 2018 | Veterinary Research Communications | `no` |  |
| `src-ckd-030` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |

## Abstract Availability Notes

### `src-ckd-025`

- Crossref title: Resistivity and pulsatility indexes in feline kidney disease: a systematic review
- Abstract lead for scope check only: Abstract Doppler ultrasonography is used in the evaluation of hemodynamics, and the resistivity (RI) and pulsatility (PI) indexes provide information about resistance to blood flo...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-ckd-026`

- Crossref title: Serum fibroblast growth factor 23 (FGF-23): associations with hyperphosphatemia and clinical staging of feline chronic kidney disease
- Abstract lead for scope check only: Fibroblast growth factor 23 (FGF-23) is an independent monitor of the progression of chronic kidney disease (CKD) in human medicine, and FGF-23 may have value as a biomarker in fe...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-ckd-027`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-ckd-028`

- Metadata check failed: no DOI in source card

### `src-ckd-029`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-ckd-030`

- Metadata check failed: no DOI in source card
