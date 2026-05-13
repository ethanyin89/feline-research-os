---
id: feline-diabetes-obesity-processing-definition-20260513
type: system
topic: content-pipeline
question_type: done-definition
language: zh
last_compiled_at: 2026-05-13
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# Feline Diabetes / Obesity Reference Processing Definition, 2026-05-13

This page defines what "processed" means for the Google Sheet:

`feline diabetes & obesity / 工作表1 / A:B`

It prevents the batch from becoming a one-off spreadsheet read.

## Autoplan Classification

This task is:

`方案 + 执行`

It is not a new idea, not only a check, and not a bug investigation. The work is to turn a provided literature sheet into durable, auditable source-intake state.

## What Counts As Processed

For this batch, "processed" has three levels.

| Level | Meaning | Current Status |
|---|---|---|
| Level 1: intake-processed | Every non-empty sheet row has been read, classified, de-duplicated, assigned an owner path, or explicitly held. | done |
| Level 2: source-ingested | A first-pass `raw/papers/src-*.md` card exists with title / locator / claim-fit caveats. | partial |
| Level 3: evidence-usable | The source has enough abstract/full-text extraction to support topic-page claims. | selective only |

The current sheet is processed at Level 1.

It is not fully Level 2 or Level 3, and it should not be described that way.

## Current Sheet Read

Source:

- Spreadsheet title: `feline diabetes & obesity`
- Spreadsheet id: `1Y-MSR39kW5F5J4OedcctdeHk0jhe1mbyvsK43Fcc7lk`
- Tab: `工作表1`
- Range: `A:B`
- Refreshed: `2026-05-13`

Current manifest:

- [feline diabetes / obesity intake manifest](feline-diabetes-obesity-intake-manifest-20260513.md)

Current counts after the first obesity Tier A ingest:

| Class | Count | Handling |
|---|---:|---|
| `existing` | 43 | already represented by existing source cards |
| `new-diabetes` | 94 | queued in diabetes extension source queue |
| `new-obesity` | 79 | queued behind the 8 obesity Tier A cards already ingested |
| `shared-existing` | 5 | cross-link to existing diabetes cards, not duplicate evidence text |
| `duplicate-in-sheet` | 5 | do not create duplicate cards |
| `section-label` | 1 | not a source |

Total non-empty rows classified: `227`.

## What Has Already Been Done

Durable workflow exists:

- [feline literature sheet intake workflow](feline-literature-sheet-intake-workflow.md)
- [scripts/literature_sheet_intake.py](../../scripts/literature_sheet_intake.py)

Required sample exists:

- [feline diabetes / obesity sheet intake sample](feline-diabetes-obesity-sheet-intake-sample-20260513.md)

The sample covered 10 rows:

- existing diabetes seed row
- duplicate diabetes row
- new diabetes source
- high-priority diabetes source
- obesity section marker
- new obesity source
- shared diabetes/obesity source

Queues exist:

- [diabetes extension source queue](diabetes-extension-source-queue-20260513.md)
- [obesity bootstrap source queue](obesity-bootstrap-source-queue-20260513.md)

Obesity first-pass ingest exists:

- `raw/papers/src-obesity-001.md`
- `raw/papers/src-obesity-002.md`
- `raw/papers/src-obesity-003.md`
- `raw/papers/src-obesity-004.md`
- `raw/papers/src-obesity-005.md`
- `raw/papers/src-obesity-006.md`
- `raw/papers/src-obesity-007.md`
- `raw/papers/src-obesity-008.md`

Obesity navigation exists:

- [obesity source index](obesity-source-index.md)
- [obesity source depth map](obesity-source-depth-map.md)
- [obesity current-state dashboard](../../topics/obesity/current-state-dashboard.md)

## What Is Not Done

Do not say:

- all 94 new diabetes rows have source cards
- all 79 remaining obesity rows have source cards
- obesity prevalence / risk ranking / management recommendations are evidence-usable
- the new diabetes extension corpus has changed the canonical 24-source diabetes module

Those would be false.

## Next Non-One-Off Step

The next reusable step is not another manual spreadsheet pass.

The next step is to extend the existing intake script or add a companion script that can turn approved manifest rows into conservative first-pass source cards.

Before that script writes all queued rows, it should be tested on 3-10 rows:

| Sample | Rows |
|---|---|
| diabetes guideline / practice control | 62, 99 |
| diabetes treatment / endpoint update | 47, 58, 103 |
| obesity Tier B / C candidate | 139, 146, 173, 223 |
| shared / duplicate guard | 137, 145 |

Expected behavior:

- assign IDs after the current highest disease-specific source ID
- preserve existing diabetes IDs `src-diabetes-001` through `src-diabetes-024`
- preserve existing obesity IDs `src-obesity-001` through `src-obesity-008`
- create only title-only / abstract-weighted cards unless the source text was actually read
- never promote new claims to topic pages in the same pass
- keep shared diabetes-obesity rows as cross-links unless a later claim-fit review needs a second owner

## Cron Decision

No cron.

This sheet is event-driven, not a living scheduled queue. Cron would be noise unless the sheet becomes an explicitly maintained recurring intake source.

## Karpathy Gap Read

This batch improves the `Data ingest` and `Compile discipline` layers of the Karpathy-style LLM wiki.

It does not yet improve sentence-level auditability or claim lookup for the new rows, because most new rows remain queued rather than deep-extracted.

The product-quality next move is a manifest-to-source-card bootstrap script with health checks, not another one-off hand conversion.
