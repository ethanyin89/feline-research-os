---
id: feline-diabetes-structured-abstract-20260609
type: system
topic: content-pipeline
question_type: structured-abstract-index
language: zh
last_compiled_at: 2026-06-09
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# Feline Structured Abstract Index, 2026-06-09

Source set: `diabetes structured abstract batch 2026-06-09`

## Rule

This is a structured abstract worksheet run after source-check. It creates abstract-only worksheets, not full-text deep extractions.

## Sample Table

| Source | Worksheet | Metadata |
|---|---|---|
| `src-diabetes-030` | [src-diabetes-030-structured-abstract-round1.md](src-diabetes-030-structured-abstract-round1.md) | family=original study; population=96 cats; sections=animals, results; signals=risk factor, activity |
| `src-diabetes-031` | [src-diabetes-031-structured-abstract-round1.md](src-diabetes-031-structured-abstract-round1.md) | family=original study; population=12 cats; signals=pathology |
| `src-diabetes-036` | [src-diabetes-036-structured-abstract-round1.md](src-diabetes-036-structured-abstract-round1.md) | family=unclear from abstract metadata; population=cats mentioned; count not mechanically extracted; signals=insulin, glucose |
| `src-diabetes-041` | [src-diabetes-041-structured-abstract-round1.md](src-diabetes-041-structured-abstract-round1.md) | family=unclear from abstract metadata; population=not mechanically extracted; sections=results |
| `src-diabetes-044` | [src-diabetes-044-structured-abstract-round1.md](src-diabetes-044-structured-abstract-round1.md) | family=unclear from abstract metadata; population=cats mentioned; count not mechanically extracted |
| `src-diabetes-046` | [src-diabetes-046-structured-abstract-round1.md](src-diabetes-046-structured-abstract-round1.md) | family=unclear from abstract metadata; population=cats mentioned; count not mechanically extracted; signals=glucose, remission, obesity, activity |
| `src-diabetes-047` | [src-diabetes-047-structured-abstract-round1.md](src-diabetes-047-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; signals=insulin, glucose |
| `src-diabetes-051` | [src-diabetes-051-structured-abstract-round1.md](src-diabetes-051-structured-abstract-round1.md) | family=unclear from abstract metadata; population=cats mentioned; count not mechanically extracted; signals=insulin |
| `src-diabetes-053` | [src-diabetes-053-structured-abstract-round1.md](src-diabetes-053-structured-abstract-round1.md) | family=original study; population=2 cats; sections=objective; signals=insulin, remission, safety, weight, overweight |
| `src-diabetes-056` | [src-diabetes-056-structured-abstract-round1.md](src-diabetes-056-structured-abstract-round1.md) | family=review; population=cats mentioned; count not mechanically extracted; signals=insulin, glucose, safety, weight, overweight, prevention |
| `src-diabetes-059` | [src-diabetes-059-structured-abstract-round1.md](src-diabetes-059-structured-abstract-round1.md) | family=review; population=cats mentioned; count not mechanically extracted; signals=obesity, risk factor |
| `src-diabetes-061` | [src-diabetes-061-structured-abstract-round1.md](src-diabetes-061-structured-abstract-round1.md) | family=original study; population=1221 cats; signals=insulin, pathology |
| `src-diabetes-062` | [src-diabetes-062-structured-abstract-round1.md](src-diabetes-062-structured-abstract-round1.md) | family=unclear from abstract metadata; population=cats mentioned; count not mechanically extracted |
| `src-diabetes-082` | [src-diabetes-082-structured-abstract-round1.md](src-diabetes-082-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; signals=insulin, glucose, remission, survival |
| `src-diabetes-083` | [src-diabetes-083-structured-abstract-round1.md](src-diabetes-083-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; sections=animals; signals=insulin, remission |
| `src-diabetes-093` | [src-diabetes-093-structured-abstract-round1.md](src-diabetes-093-structured-abstract-round1.md) | family=review; population=cats mentioned; count not mechanically extracted; signals=insulin, obesity |
| `src-diabetes-095` | [src-diabetes-095-structured-abstract-round1.md](src-diabetes-095-structured-abstract-round1.md) | family=unclear from abstract metadata; population=cats mentioned; count not mechanically extracted; signals=insulin |
| `src-diabetes-101` | [src-diabetes-101-structured-abstract-round1.md](src-diabetes-101-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; signals=insulin |
| `src-diabetes-107` | [src-diabetes-107-structured-abstract-round1.md](src-diabetes-107-structured-abstract-round1.md) | family=original study; population=22 cats; sections=results; signals=insulin, body condition, obesity, risk factor |
| `src-diabetes-112` | [src-diabetes-112-structured-abstract-round1.md](src-diabetes-112-structured-abstract-round1.md) | family=original study; population=cats mentioned; count not mechanically extracted; sections=animals; signals=insulin, glucose |
| `src-diabetes-115` | [src-diabetes-115-structured-abstract-round1.md](src-diabetes-115-structured-abstract-round1.md) | family=unclear from abstract metadata; population=cats mentioned; count not mechanically extracted |

## Boundary

- Cards remain `abstract_weighted` unless a later full-text/deep-extraction pass changes them.
- This index can guide branch placement and extraction priority.
- No topic pages should be updated from this sample alone.
