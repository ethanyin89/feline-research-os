---
id: feline-structured-abstract-sample-20260514
type: system
topic: content-pipeline
question_type: structured-abstract-sample
language: zh
last_compiled_at: 2026-05-14
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# Feline Structured Abstract Sample, 2026-05-14

Source set: `diabetes obesity high-priority structured abstract sample 2026-05-14`

## Rule

This is a 3-10 source sample after full source-check. It creates abstract-only worksheets, not full-text deep extractions.

## Sample Table

| Source | Worksheet | Metadata |
|---|---|---|
| `src-diabetes-035` | [src-diabetes-035-structured-abstract-round1.md](src-diabetes-035-structured-abstract-round1.md) | family=original study; population=252 cats; sections=objective, animals, procedures, results, clinical relevance; signals=insulin, glucose, safety, effectiveness |
| `src-diabetes-050` | [src-diabetes-050-structured-abstract-round1.md](src-diabetes-050-structured-abstract-round1.md) | family=guideline / consensus; population=cats mentioned; count not mechanically extracted; sections=practical relevance; signals=insulin, glucose, remission, weight |
| `src-diabetes-087` | [src-diabetes-087-structured-abstract-round1.md](src-diabetes-087-structured-abstract-round1.md) | family=guideline / consensus; population=cats mentioned; count not mechanically extracted; signals=insulin, glucose |
| `src-diabetes-091` | [src-diabetes-091-structured-abstract-round1.md](src-diabetes-091-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; sections=background, animals, methods, results, conclusions; signals=remission, survival, quality of life |
| `src-obesity-004` | [src-obesity-004-structured-abstract-round1.md](src-obesity-004-structured-abstract-round1.md) | family=review; population=cats mentioned; count not mechanically extracted; sections=aim, animals; signals=insulin, weight, obesity, overweight, risk factor |
| `src-obesity-005` | [src-obesity-005-structured-abstract-round1.md](src-obesity-005-structured-abstract-round1.md) | family=review; population=cats mentioned; count not mechanically extracted; signals=obesity, prevention |
| `src-obesity-008` | [src-obesity-008-structured-abstract-round1.md](src-obesity-008-structured-abstract-round1.md) | family=original study; population=16 cats; sections=results; signals=insulin, glucose, effectiveness, weight, obesity |
| `src-obesity-080` | [src-obesity-080-structured-abstract-round1.md](src-obesity-080-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; sections=objective, animals, procedures, results, conclusions, clinical relevance; signals=weight, body condition, overweight, microbiota, activity |

## Boundary

- Cards remain `abstract_weighted` unless a later full-text/deep-extraction pass changes them.
- This sample justified the reusable structured-abstract workflow shape; broader use still must preserve the same boundaries.
- No topic pages should be updated from this sample alone.
