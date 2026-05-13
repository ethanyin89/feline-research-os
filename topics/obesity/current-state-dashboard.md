---
id: topic-obesity-current-state-dashboard
type: topic
topic: obesity
species: feline
disease: obesity
question_type: dashboard
source_ids: [src-diabetes-005]
last_compiled_at: 2026-05-13
confidence: low
verification_status: bootstrap
decision_grade: no
language_qa_status: light_checked
language_qa_notes: "2026-05-13 checked as bootstrap dashboard; source_ids points only to existing diabetes-obesity bridge while new obesity corpus remains queued, not compiled."
owner: codex
status: active
---

# Feline Obesity Current State Dashboard

## State

`bootstrap`

The 2026-05-13 sheet introduced a standalone feline obesity section. The corpus has been classified and queued, but source cards have not yet been created.

## What Exists

| Layer | Status | Read |
|---|---|---|
| Google Sheet intake | done | 227 non-empty rows classified |
| Obesity candidate set | done | 87 new obesity candidates |
| Shared-source control | done | 5 shared existing diabetes rows marked for cross-linking |
| Obesity source cards | not started | no `src-obesity-*` cards yet |
| Obesity topic pages | shell only | index, navigation, dashboard |

## Tier A Bootstrap Read

Start with:

1. feline-specific obesity review
2. broad canine/feline obesity review
3. obesity management review
4. newer epidemiology / associated pathology review
5. prevention / target-population strategy
6. obesity-to-insulin-sensitivity bridge

See [obesity bootstrap source queue](../../system/indexes/obesity-bootstrap-source-queue-20260513.md).

## Do Not Say Yet

- do not give obesity prevalence numbers from this new corpus until source cards exist
- do not rank weight-loss interventions
- do not make owner-facing feeding recommendations
- do not merge obesity into diabetes, and do not treat diabetes-obesity bridge evidence as the whole obesity module

## Next Exit Condition

The module can move from `bootstrap` to `source-indexed` after:

1. Tier A `src-obesity-*` source cards exist.
2. Each Tier A card has source family and claim-fit judgment.
3. Shared diabetes-obesity source handling is documented.
4. Markdown and source-card checks pass.
