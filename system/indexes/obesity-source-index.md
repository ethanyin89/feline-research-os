---
id: obesity-source-index
type: index
topic: obesity
question_type: source-index
language: zh
last_compiled_at: 2026-05-17
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# Feline Obesity Source Index

## Bootstrap Corpus

The obesity module started from the 2026-05-13 diabetes / obesity spreadsheet intake.

This index tracks the first-pass obesity source-card layer. The full obesity sheet has now been ingested as conservative partial cards.

## Coverage Summary

| Scope | Count | State |
|---|---:|---|
| First-pass obesity cards | 87 | `src-obesity-001` through `src-obesity-087` |
| Deep-extracted obesity cards | 1 | `src-obesity-008` is evidence-usable for bounded mechanism / diabetes-bridge placement only |
| Shared diabetes/obesity sources | 10 | cross-link to existing disease-owner cards |

## First-Pass Source Cards

The table below keeps the original Tier A shell visible. The remaining `src-obesity-009` through `src-obesity-087` cards are title-only / partial intake cards and should be read through the [obesity bootstrap source queue](obesity-bootstrap-source-queue-20260513.md) until they are source-checked or deep-extracted.

| ID | Title | Primary Layer | Evidence Level | Status |
|---|---|---|---|---|
| src-obesity-001 | Feline obesity - prevalence, risk factors, pathogenesis, associated conditions and assessment: a review | shell / assessment | review | first-pass partial, title-only |
| src-obesity-002 | Canine and feline obesity: a review of pathophysiology, epidemiology, and clinical management | shell / management context | review | first-pass partial, title-only |
| src-obesity-003 | Canine and Feline Obesity Management | management | review | first-pass partial, title-only |
| src-obesity-004 | Overweight and obesity in domestic cats: epidemiological risk factors and associated pathologies | risk / associated pathologies | review | first-pass partial, title-only |
| src-obesity-005 | Identifying the target population and preventive strategies to combat feline obesity | prevention | review | first-pass partial, abstract-weighted |
| src-obesity-006 | Management of obesity in cats | management | review | first-pass partial, title-only |
| src-obesity-007 | Obesity Treatment: Environment and Behavior Modification | environment / behavior | review | first-pass partial, title-only |
| src-obesity-008 | Insulin Sensitivity Decreases with Obesity, and Lean Cats with Low Insulin Sensitivity are at Greatest Risk of Glucose Intolerance with Weight Gain | insulin sensitivity / diabetes bridge | original-study | deep-extracted; bounded mechanism anchor |

## Shared Existing Sources

| Existing ID | Role |
|---|---|
| src-diabetes-005 | obese diabetic cat bridge |
| src-diabetes-006 | diet and diabetes prevention/management |
| src-diabetes-023 | cross-species diabetes / ketoacidosis context |
| src-diabetes-016 | low carbohydrate versus high fiber diabetes diet debate |
| src-diabetes-002 | older diabetes pathogenesis |

## First-Pass Read

The first-pass obesity card set is intentionally cautious.

It proves:

- a standalone obesity corpus exists and has been fully first-pass ingested
- the first shell should include prevalence/risk, assessment, management, prevention, environment/behavior, and insulin-sensitivity bridge logic
- obesity should not be collapsed into diabetes
- shared diabetes-obesity sources should be cross-linked rather than duplicated

It does not prove:

- prevalence values
- risk-factor ranking
- body-condition thresholds
- weight-loss protocols
- owner-facing feeding or environment advice

## Next Priority

Deep extraction should start with:

1. `src-obesity-001`
2. `src-obesity-004`
3. `src-obesity-005`
4. ~~`src-obesity-008`~~ done, 2026-05-17; keep as bounded mechanism anchor, not public guidance
5. `src-obesity-003` or `src-obesity-006`, depending on whether the next output pressure is broad management or feline-only management.
