---
id: feline-ckd-extension-structured-abstract-20260605
type: system
topic: content-pipeline
question_type: structured-abstract-index
language: zh
last_compiled_at: 2026-06-05
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# Feline Structured Abstract Index, 2026-06-05

Source set: `CKD Google Sheet abstract-weighted extension structured abstract pass, 2026-06-05`

## Rule

This is a structured abstract worksheet run after source-check. It creates abstract-only worksheets, not full-text deep extractions.

## Sample Table

| Source | Worksheet | Metadata |
|---|---|---|
| `src-ckd-025` | [src-ckd-025-structured-abstract-round1.md](src-ckd-025-structured-abstract-round1.md) | family=review; population=cats mentioned; count not mechanically extracted; sections=animals, methods; signals=weight, ultrasonography |
| `src-ckd-026` | [src-ckd-026-structured-abstract-round1.md](src-ckd-026-structured-abstract-round1.md) | family=unclear from abstract metadata; population=304 cats; signals=biomarker, chronic kidney disease, fibroblast growth factor 23, fgf-23, hyperphosphatemia, phosphate, phosphorus, staging |
| `src-ckd-033` | [src-ckd-033-structured-abstract-round1.md](src-ckd-033-structured-abstract-round1.md) | family=unclear from abstract metadata; population=25 cats; signals=survival, risk factor, chronic kidney disease, urinary tract infection |
| `src-ckd-034` | [src-ckd-034-structured-abstract-round1.md](src-ckd-034-structured-abstract-round1.md) | family=original study; population=101 cats; sections=methods, results, conclusions; signals=risk factor, chronic kidney disease |
| `src-ckd-035` | [src-ckd-035-structured-abstract-round1.md](src-ckd-035-structured-abstract-round1.md) | family=unclear from abstract metadata; population=26 cats; signals=chronic kidney disease, cytokine |
| `src-ckd-043` | [src-ckd-043-structured-abstract-round1.md](src-ckd-043-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; sections=aim, methods, results, conclusions; signals=biomarker, carbonyl stress, chronic kidney disease, uraemic toxin |
| `src-ckd-045` | [src-ckd-045-structured-abstract-round1.md](src-ckd-045-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; sections=methods, results, conclusions; signals=albuminuria, chronic kidney disease, proteinuria |
| `src-ckd-046` | [src-ckd-046-structured-abstract-round1.md](src-ckd-046-structured-abstract-round1.md) | family=review; population=cats mentioned; count not mechanically extracted; sections=aim, practical relevance; signals=ultrasonography |

## Boundary

- Cards remain `abstract_weighted` unless a later full-text/deep-extraction pass changes them.
- This index can guide branch placement and extraction priority.
- No topic pages should be updated from this sample alone.
