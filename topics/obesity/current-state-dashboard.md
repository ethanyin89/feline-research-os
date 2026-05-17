---
id: topic-obesity-current-state-dashboard
type: topic
topic: obesity
species: feline
disease: obesity
question_type: dashboard
source_ids: [src-obesity-001, src-obesity-002, src-obesity-003, src-obesity-004, src-obesity-005, src-obesity-006, src-obesity-007, src-obesity-008, src-diabetes-005]
last_compiled_at: 2026-05-17
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
language_qa_notes: "2026-05-17 checked after first obesity deep extraction; source-depth boundary is visible and no clinical guidance claims are made."
owner: codex
status: active
---

# Feline Obesity Current State Dashboard

## State

`source-indexed plus first mechanism anchor`

The 2026-05-13 sheet introduced a standalone feline obesity section. The corpus has been classified, de-duplicated, fully first-pass ingested as source cards, and fully source-checked against Crossref metadata / abstract availability. One card, `src-obesity-008`, is now deep-extracted as a bounded obesity-diabetes mechanism anchor. The rest of the obesity corpus remains partial: 43 cards are abstract-weighted and 43 are title-only.

## What Exists

| Layer | Status | Read |
|---|---|---|
| Google Sheet intake | done | 227 non-empty rows classified |
| Obesity candidate set | done | 87 obesity source cards now exist |
| Shared-source control | done | 10 shared existing rows marked for cross-linking after bootstrap |
| Obesity source cards | first-pass complete + full source-check + first deep extraction | `src-obesity-001` through `src-obesity-087`; 1 deep-extracted, 43 title-only, 43 abstract-weighted |
| Obesity source index | active | source index and depth map exist; `src-obesity-008` is the first deep-extracted mechanism anchor |
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

## First Deep-Extracted Anchor

`src-obesity-008` can now support bounded mechanism and branch-placement language: feline weight gain / obesity can be connected to insulin sensitivity, glucose effectiveness, and glucose tolerance as an obesity-diabetes bridge. It should not be used for screening thresholds, weight-loss prescriptions, risk ranking, or a public obesity guidance page by itself.

## Next Exit Condition

The module can move from `source-indexed` to `compiled starter` after:

1. `src-obesity-001`, `src-obesity-004`, and `src-obesity-005` are deep-extracted or have stronger source worksheets. `src-obesity-008` is already deep-extracted for the mechanism bridge.
2. Shared diabetes-obesity source handling is documented in the first compiled obesity page.
3. A first narrow obesity owner exists, preferably risk/assessment, prevention, or obesity-diabetes bridge.
4. Markdown and source-card checks pass.
