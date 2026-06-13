---
id: feline-ckd-extension-structured-abstract-pubmed-20260606
type: system
topic: content-pipeline
question_type: structured-abstract-index
language: zh
last_compiled_at: 2026-06-06
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# Feline Structured Abstract Index, 2026-06-06

Source set: `CKD extension PubMed fallback structured abstracts 2026-06-06`

## Rule

This is a structured abstract worksheet run after source-check. It creates abstract-only worksheets, not full-text deep extractions.

## Sample Table

| Source | Worksheet | Metadata |
|---|---|---|
| `src-ckd-027` | [src-ckd-027-structured-abstract-round1.md](src-ckd-027-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; signals=biomarker, chronic kidney disease, uremic toxin |
| `src-ckd-029` | [src-ckd-029-structured-abstract-round1.md](src-ckd-029-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; sections=animals; signals=survival, chronic kidney disease, phosphate, phosphorus, renal diet |
| `src-ckd-039` | [src-ckd-039-structured-abstract-round1.md](src-ckd-039-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; signals=chronic kidney disease |
| `src-ckd-044` | [src-ckd-044-structured-abstract-round1.md](src-ckd-044-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; signals=chronic kidney disease, homocysteine, proteinuria |
| `src-ckd-047` | [src-ckd-047-structured-abstract-round1.md](src-ckd-047-structured-abstract-round1.md) | family=unclear from abstract metadata; population=cats mentioned; count not mechanically extracted; signals=risk factor, chronic kidney disease |
| `src-ckd-049` | [src-ckd-049-structured-abstract-round1.md](src-ckd-049-structured-abstract-round1.md) | family=unclear from abstract metadata; population=cats mentioned; count not mechanically extracted; signals=chronic kidney disease |

## Boundary

- Cards remain `abstract_weighted` unless a later full-text/deep-extraction pass changes them.
- This index can guide branch placement and extraction priority.
- No topic pages should be updated from this sample alone.
