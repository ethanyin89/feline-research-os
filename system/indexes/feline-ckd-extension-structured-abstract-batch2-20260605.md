---
id: feline-ckd-extension-structured-abstract-batch2-20260605
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

Source set: `CKD extension batch 2 2026-06-05`

## Rule

This is a structured abstract worksheet run after source-check. It creates abstract-only worksheets, not full-text deep extractions.

## Sample Table

| Source | Worksheet | Metadata |
|---|---|---|
| `src-ckd-030` | [src-ckd-030-structured-abstract-round1.md](src-ckd-030-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; sections=results; signals=microbiota, chronic kidney disease, uremic toxin |
| `src-ckd-036` | [src-ckd-036-structured-abstract-round1.md](src-ckd-036-structured-abstract-round1.md) | family=unclear from abstract metadata; population=cats mentioned; count not mechanically extracted; sections=results; signals=chronic kidney disease |
| `src-ckd-037` | [src-ckd-037-structured-abstract-round1.md](src-ckd-037-structured-abstract-round1.md) | family=review; population=cats mentioned; count not mechanically extracted; signals=survival, chronic kidney disease |
| `src-ckd-038` | [src-ckd-038-structured-abstract-round1.md](src-ckd-038-structured-abstract-round1.md) | family=review; population=cats mentioned; count not mechanically extracted; signals=pathology |
| `src-ckd-041` | [src-ckd-041-structured-abstract-round1.md](src-ckd-041-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; sections=results; signals=chronic kidney disease, ultrasonography |
| `src-ckd-048` | [src-ckd-048-structured-abstract-round1.md](src-ckd-048-structured-abstract-round1.md) | family=original study; population=68 cats; sections=aim, methods, results, conclusions; signals=quality of life, chronic kidney disease |

## Boundary

- Cards remain `abstract_weighted` unless a later full-text/deep-extraction pass changes them.
- This index can guide branch placement and extraction priority.
- No topic pages should be updated from this sample alone.
