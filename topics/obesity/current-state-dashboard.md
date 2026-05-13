---
id: topic-obesity-current-state-dashboard
type: topic
topic: obesity
species: feline
disease: obesity
question_type: dashboard
source_ids: [src-obesity-001, src-obesity-002, src-obesity-003, src-obesity-004, src-obesity-005, src-obesity-006, src-obesity-007, src-obesity-008, src-diabetes-005]
last_compiled_at: 2026-05-13
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
language_qa_notes: "2026-05-13 checked as source-indexed dashboard; partial/title-only source boundary is visible and no clinical guidance claims are made."
owner: codex
status: active
---

# Feline Obesity Current State Dashboard

## State

`source-indexed`

The 2026-05-13 sheet introduced a standalone feline obesity section. The corpus has been classified, de-duplicated, and fully first-pass ingested as source cards. These are partial cards, not deep-extracted evidence.

## What Exists

| Layer | Status | Read |
|---|---|---|
| Google Sheet intake | done | 227 non-empty rows classified |
| Obesity candidate set | done | 87 obesity source cards now exist |
| Shared-source control | done | 10 shared existing rows marked for cross-linking after bootstrap |
| Obesity source cards | first-pass complete | `src-obesity-001` through `src-obesity-087`; partial and mostly title-only |
| Obesity source index | active | source index and depth map exist, but deep extraction is still pending |
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

- do not give obesity prevalence numbers from this new corpus until source cards are source-checked or deep-extracted
- do not rank weight-loss interventions
- do not make owner-facing feeding recommendations
- do not merge obesity into diabetes, and do not treat diabetes-obesity bridge evidence as the whole obesity module

## Next Exit Condition

The module can move from `source-indexed` to `compiled starter` after:

1. `src-obesity-001`, `src-obesity-004`, `src-obesity-005`, and `src-obesity-008` are deep-extracted.
2. Shared diabetes-obesity source handling is documented in the first compiled obesity page.
3. A first narrow obesity owner exists, preferably risk/assessment, prevention, or obesity-diabetes bridge.
4. Markdown and source-card checks pass.
