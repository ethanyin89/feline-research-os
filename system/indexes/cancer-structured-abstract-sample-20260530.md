---
id: cancer-structured-abstract-sample-20260530
type: system
topic: content-pipeline
question_type: structured-abstract-index
language: zh
last_compiled_at: 2026-05-30
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# Feline Structured Abstract Index, 2026-05-30

Source set: `feline cancer structured abstract 10-card sample, 2026-05-30`

## Rule

This is a structured abstract worksheet run after source-check. It creates abstract-only worksheets, not full-text deep extractions.

## Sample Table

| Source | Worksheet | Metadata |
|---|---|---|
| `src-cancer-003` | [src-cancer-003-structured-abstract-round1.md](src-cancer-003-structured-abstract-round1.md) | family=review; population=cats mentioned; count not mechanically extracted; sections=aim; signals=survival |
| `src-cancer-004` | [src-cancer-004-structured-abstract-round1.md](src-cancer-004-structured-abstract-round1.md) | family=review; population=cats mentioned; count not mechanically extracted; sections=animals |
| `src-cancer-005` | [src-cancer-005-structured-abstract-round1.md](src-cancer-005-structured-abstract-round1.md) | family=review; population=cats mentioned; count not mechanically extracted |
| `src-cancer-008` | [src-cancer-008-structured-abstract-round1.md](src-cancer-008-structured-abstract-round1.md) | family=review; population=cats mentioned; count not mechanically extracted |
| `src-cancer-009` | [src-cancer-009-structured-abstract-round1.md](src-cancer-009-structured-abstract-round1.md) | family=review; population=73 cats; sections=methods, results, conclusions; signals=survival, pathology |
| `src-cancer-019` | [src-cancer-019-structured-abstract-round1.md](src-cancer-019-structured-abstract-round1.md) | family=original study; population=not mechanically extracted; sections=background, methods, results |
| `src-cancer-021` | [src-cancer-021-structured-abstract-round1.md](src-cancer-021-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; sections=animals |
| `src-cancer-025` | [src-cancer-025-structured-abstract-round1.md](src-cancer-025-structured-abstract-round1.md) | family=guideline / consensus; population=not mechanically extracted; sections=results; signals=survival |
| `src-cancer-040` | [src-cancer-040-structured-abstract-round1.md](src-cancer-040-structured-abstract-round1.md) | family=review; population=cats mentioned; count not mechanically extracted; sections=practical relevance |
| `src-cancer-046` | [src-cancer-046-structured-abstract-round1.md](src-cancer-046-structured-abstract-round1.md) | family=review; population=cats mentioned; count not mechanically extracted; signals=quality of life, risk factor |

## Boundary

- Cards remain `abstract_weighted` unless a later full-text/deep-extraction pass changes them.
- This index can guide branch placement and extraction priority.
- No topic pages should be updated from this sample alone.
