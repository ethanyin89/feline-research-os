---
id: feline-ckd-extension-source-check-remaining-20260605
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

Source set: `CKD Google Sheet remaining extension metadata check, 2026-06-05`

## Rule

This report is a repeatable second-pass source check. It does not make clinical claims.

- DOI metadata alone does not upgrade a card.
- Abstract availability can justify `abstract_weighted` only for navigation and extraction priority.
- Full-text or structured worksheet review is still required before `source_checked` or `deep_extracted`.

## Summary

- Cards checked: `15`
- Crossref metadata found: `4`
- Abstract available: `3`

## Check Table

| Source | Current | Recommended | DOI | Year | Container | Abstract | Error |
|---|---|---|---|---:|---|---|---|
| `src-ckd-036` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-ckd-037` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-ckd-038` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-ckd-039` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-ckd-040` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-ckd-041` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-ckd-042` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-ckd-043` | `title_only` | `abstract_weighted` | `10.1177/1098612x18783858` | 2019 | Journal of Feline Medicine and Surgery | `yes` |  |
| `src-ckd-044` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-ckd-045` | `title_only` | `abstract_weighted` | `10.1177/1098612x19827597` | 2020 | Journal of Feline Medicine and Surgery | `yes` |  |
| `src-ckd-046` | `title_only` | `abstract_weighted` | `10.1177/1098612x20917598` | 2020 | Journal of Feline Medicine and Surgery | `yes` |  |
| `src-ckd-047` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-ckd-048` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-ckd-049` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-ckd-050` | `title_only` | `title_only` | `10.1186/s12917-018-1387-2` | 2018 | BMC Veterinary Research | `no` |  |

## Abstract Availability Notes

### `src-ckd-036`

- Metadata check failed: no DOI in source card

### `src-ckd-037`

- Metadata check failed: no DOI in source card

### `src-ckd-038`

- Metadata check failed: no DOI in source card

### `src-ckd-039`

- Metadata check failed: no DOI in source card

### `src-ckd-040`

- Metadata check failed: no DOI in source card

### `src-ckd-041`

- Metadata check failed: no DOI in source card

### `src-ckd-042`

- Metadata check failed: no DOI in source card

### `src-ckd-043`

- Crossref title: Investigation of hallmarks of carbonyl stress and formation of end products in feline chronic kidney disease as markers of uraemic toxins
- Abstract lead for scope check only: Objectives Cats are commonly affected by chronic kidney disease (CKD). Many reactive carbonyl intermediates and end products originating from the oxidative stress pathways are rec...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-ckd-044`

- Metadata check failed: no DOI in source card

### `src-ckd-045`

- Crossref title: Electrophoretic patterns of proteinuria in feline spontaneous chronic kidney disease
- Abstract lead for scope check only: Objectives The purpose of this study was to describe the electrophoretic patterns of proteinuria in cats at risk of and cats with chronic kidney disease (CKD), and to investigate...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-ckd-046`

- Crossref title: Feline abdominal ultrasonography: what’s normal? what’s abnormal? The kidneys and perinephric space
- Abstract lead for scope check only: Practical relevance: Abdominal ultrasound plays a vital role in the diagnostic work-up of many cats presenting to general and specialist practitioners. Ultrasound examination of t...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-ckd-047`

- Metadata check failed: no DOI in source card

### `src-ckd-048`

- Metadata check failed: no DOI in source card

### `src-ckd-049`

- Metadata check failed: no DOI in source card

### `src-ckd-050`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.
