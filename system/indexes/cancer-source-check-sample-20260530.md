---
id: cancer-source-check-sample-20260530
type: system
topic: content-pipeline
question_type: source-check-report
language: zh
last_compiled_at: 2026-05-30
verification_status: generated
decision_grade: no
owner: codex
status: active
---

# Feline Source Metadata Check, 2026-05-30

Source set: `feline cancer first-pass 10-card metadata sample, 2026-05-30`

## Rule

This report is a repeatable second-pass source check. It does not make clinical claims.

- DOI metadata alone does not upgrade a card.
- Abstract availability can justify `abstract_weighted` only for navigation and extraction priority.
- Full-text or structured worksheet review is still required before `source_checked` or `deep_extracted`.

## Summary

- Cards checked: `10`
- Crossref metadata found: `5`
- Abstract available: `5`

## Check Table

| Source | Current | Recommended | DOI | Year | Container | Abstract | Error |
|---|---|---|---|---:|---|---|---|
| `src-cancer-001` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-002` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-003` | `title_only` | `abstract_weighted` | `10.1002/vms3.460` | 2021 | Veterinary Medicine and Science | `yes` |  |
| `src-cancer-004` | `title_only` | `abstract_weighted` | `10.21926/obm.genet.2102131` | 2021 | OBM Genetics | `yes` |  |
| `src-cancer-005` | `title_only` | `abstract_weighted` | `10.3390/vetsci2030111` | 2015 | Veterinary Sciences | `yes` |  |
| `src-cancer-006` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-007` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-008` | `title_only` | `abstract_weighted` | `10.1177/104063870001200401` | 2000 | Journal of Veterinary Diagnostic Investigation | `yes` |  |
| `src-cancer-009` | `title_only` | `abstract_weighted` | `10.1177/1098612x20964416` | 2021 | Journal of Feline Medicine and Surgery | `yes` |  |
| `src-cancer-010` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |

## Abstract Availability Notes

### `src-cancer-001`

- Metadata check failed: no DOI in source card

### `src-cancer-002`

- Metadata check failed: no DOI in source card

### `src-cancer-003`

- Crossref title: The role of COX expression in the prognostication of overall survival of canine and feline cancer: A systematic review
- Abstract lead for scope check only: Abstract Cyclooxygenase (COX) isoforms‐1 and ‐2 have been extensively investigated in cancer. Although COX‐2 is the isoform most studied and has been described in several malignan...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-004`

- Crossref title: Molecular Mechanisms of Feline Cancers
- Abstract lead for scope check only: Feline cancers have not been studied as extensively as canine cancers, though they may offer similar advantages, with cats being immunocompetent animals subject to similar conditi...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-005`

- Crossref title: Cats, Cancer and Comparative Oncology
- Abstract lead for scope check only: Naturally occurring tumors in dogs are well-established models for several human cancers. Domestic cats share many of the benefits of dogs as a model (spontaneous cancers developi...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-006`

- Metadata check failed: no DOI in source card

### `src-cancer-007`

- Metadata check failed: no DOI in source card

### `src-cancer-008`

- Crossref title: The Histologic Classification of 602 Cases of Feline Lymphoproliferative Disease using the National Cancer Institute Working Formulation
- Abstract lead for scope check only: Case information and histologic slides for 688 admissions of feline tissues from 12 veterinary institutions were assembled and reviewed to determine tissues obtained by biopsy or...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-009`

- Crossref title: Metastatic feline mammary cancer: prognostic factors, outcome and comparison of different treatment modalities – a retrospective multicentre study
- Abstract lead for scope check only: Objectives Although feline mammary carcinomas (FMCs) are highly metastatic, the literature and treatment options pertaining to advanced tumours are scarce. This study aimed to inv...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-010`

- Metadata check failed: no DOI in source card
