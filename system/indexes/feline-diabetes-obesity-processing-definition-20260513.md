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
| Level 2: source-ingested | A first-pass `raw/papers/src-*.md` card exists with title / locator / claim-fit caveats, or the row is explicitly shared/section-only. | done |
| Level 2.5: source-checked | DOI metadata / Crossref abstract availability has been checked for the diabetes extension and obesity corpus. | done |
| Level 2.75: structured-abstract extracted | Abstract-only worksheets exist for every abstract-available diabetes extension and obesity card. | done for 103 abstract-weighted cards |
| Level 2.9: full-text availability sampled | High-priority deep-extraction candidates have Crossref full-text/TDM link and HEAD-probe availability checked. | sample done |
| Level 3: evidence-usable | The source has enough structured abstract/full-text extraction to support topic-page claims. | selective only |

The current sheet is processed at Level 2.5.

It is not fully Level 3, and it should not be described that way.

## Current Sheet Read

Source:

- Spreadsheet title: `feline diabetes & obesity`
- Spreadsheet id: `1Y-MSR39kW5F5J4OedcctdeHk0jhe1mbyvsK43Fcc7lk`
- Tab: `工作表1`
- Range: `A:B`
- Refreshed: `2026-05-13`

Current manifest:

- [feline diabetes / obesity intake manifest](feline-diabetes-obesity-intake-manifest-20260513.md)

Current counts after the full first-pass source-card bootstrap:

| Class | Count | Handling |
|---|---:|---|
| `existing` | 216 | represented by source cards |
| `shared-existing` | 10 | cross-link to existing disease-owner cards, not duplicate evidence text |
| `section-label` | 1 | not a source |

Total non-empty rows classified: `227`.

## What Has Already Been Done

Durable workflow exists:

- [feline literature sheet intake workflow](feline-literature-sheet-intake-workflow.md)
- [scripts/literature_sheet_intake.py](../../scripts/literature_sheet_intake.py)
- [scripts/literature_source_card_bootstrap.py](../../scripts/literature_source_card_bootstrap.py)
- [scripts/source_metadata_check.py](../../scripts/source_metadata_check.py)

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

Full first-pass ingest exists:

- `raw/papers/src-diabetes-001.md` through `raw/papers/src-diabetes-118.md`
- `raw/papers/src-obesity-001.md` through `raw/papers/src-obesity-087.md`

Obesity navigation exists:

- [obesity source index](obesity-source-index.md)
- [obesity source depth map](obesity-source-depth-map.md)
- [obesity current-state dashboard](../../topics/obesity/current-state-dashboard.md)

## What Is Not Done

Do not say:

- all 94 new diabetes extension rows are evidence-usable
- all 87 obesity rows are evidence-usable
- obesity prevalence / risk ranking / management recommendations are evidence-usable
- the new diabetes extension corpus has changed the canonical 24-source diabetes module

Those would be false.

## Source-Card Bootstrap Completed

The reusable source-card bootstrap step has been run. Before full write, it was tested on 3-10 representative rows:

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

Sample dry-run completed on 2026-05-13:

```bash
python3 scripts/literature_source_card_bootstrap.py \
  --csv /tmp/feline-diabetes-obesity-20260513.csv \
  --repo-root . \
  --rows 62,99,47,58,103,139,146,173,223,137,145
```

Result:

- planned 7 new first-pass cards
- skipped existing / shared / duplicate sample rows
- next diabetes IDs start at `src-diabetes-025`
- next obesity IDs start at `src-obesity-009`

Full write completed on 2026-05-13:

```bash
python3 scripts/literature_source_card_bootstrap.py \
  --csv /tmp/feline-diabetes-obesity-20260513.csv \
  --repo-root . \
  --write
```

Result:

- wrote 173 first-pass source cards
- diabetes extension now spans `src-diabetes-025` through `src-diabetes-118`
- obesity now spans `src-obesity-001` through `src-obesity-087`
- all generated cards are `extraction_depth: partial`, `verification_status: title_only`, and `decision_grade: no`

## Source-Check Sample Completed

The reusable source metadata / abstract check has been run on 10 high-priority cards:

```bash
python3 scripts/source_metadata_check.py \
  --repo-root . \
  --source-ids src-diabetes-050,src-diabetes-087,src-diabetes-046,src-diabetes-035,src-diabetes-091,src-obesity-001,src-obesity-004,src-obesity-005,src-obesity-008,src-obesity-080 \
  --source-label "diabetes/obesity priority sample 2026-05-13" \
  --out system/indexes/feline-diabetes-obesity-source-check-sample-20260513.md \
  --update-cards
```

Result:

- report: [feline diabetes / obesity source-check sample](feline-diabetes-obesity-source-check-sample-20260513.md)
- 10 DOI metadata records resolved
- 8 cards have Crossref abstracts and are now `abstract_weighted`
- 2 cards remain `title_only`: `src-diabetes-046`, `src-obesity-001`
- no cards were promoted to `source_checked`, `deep_extracted`, or decision-grade evidence

## Full Source-Check Completed

After the 10-card sample, the same reusable script was run across all diabetes extension and obesity cards:

```bash
python3 scripts/source_metadata_check.py \
  --repo-root . \
  --source-glob 'raw/papers/src-diabetes-0*.md' \
  --source-glob 'raw/papers/src-diabetes-1*.md' \
  --source-glob 'raw/papers/src-obesity-*.md' \
  --status title_only \
  --status abstract_weighted \
  --source-label 'diabetes extension and obesity full source-check 2026-05-14' \
  --report-id feline-diabetes-obesity-source-check-full-20260514 \
  --out system/indexes/feline-diabetes-obesity-source-check-full-20260514.md \
  --update-cards
```

Result:

- report: [feline diabetes / obesity full source-check](feline-diabetes-obesity-source-check-full-20260514.md)
- 181 cards checked: 94 diabetes extension cards and 87 obesity cards
- 167 DOI metadata records resolved
- 103 cards had Crossref abstracts and were kept or upgraded to `abstract_weighted`
- diabetes final status: 59 `abstract_weighted`, 35 `title_only`, plus the canonical 24 `deep_extracted` seed cards
- obesity final status: 44 `abstract_weighted`, 43 `title_only`
- no card was promoted to `source_checked`, `deep_extracted`, or decision-grade evidence by this step

## Structured Abstract Sample Completed

After full source-check, a high-priority 8-source structured abstract sample was generated:

```bash
python3 scripts/structured_abstract_extraction.py \
  --repo-root . \
  --source-ids src-diabetes-035,src-diabetes-050,src-diabetes-087,src-diabetes-091,src-obesity-004,src-obesity-005,src-obesity-008,src-obesity-080 \
  --source-label 'diabetes obesity high-priority structured abstract sample 2026-05-14' \
  --index-out system/indexes/feline-diabetes-obesity-structured-abstract-sample-20260514.md \
  --write
```

Result:

- report: [feline diabetes / obesity structured abstract sample](feline-diabetes-obesity-structured-abstract-sample-20260514.md)
- 8 abstract-only worksheets created
- worksheets cover guideline / consensus, treatment-control, remission / quality-of-life, obesity risk, prevention, obesity-diabetes bridge, and weight-loss intervention samples
- cards remain `abstract_weighted`
- no topic pages were promoted from these worksheets
- no card was promoted to `source_checked`, `deep_extracted`, or decision-grade evidence

## Full Structured Abstract Run Completed

After the 8-source sample proved usable, the same reusable script was run across all abstract-weighted diabetes extension and obesity cards:

```bash
python3 scripts/structured_abstract_extraction.py \
  --repo-root . \
  --source-glob 'raw/papers/src-diabetes-0*.md' \
  --source-glob 'raw/papers/src-diabetes-1*.md' \
  --source-glob 'raw/papers/src-obesity-*.md' \
  --status abstract_weighted \
  --source-label 'diabetes extension and obesity structured abstract full run 2026-05-14' \
  --index-id feline-diabetes-obesity-structured-abstract-full-20260514 \
  --index-out system/indexes/feline-diabetes-obesity-structured-abstract-full-20260514.md \
  --write
```

Result:

- report: [feline diabetes / obesity structured abstract full index](feline-diabetes-obesity-structured-abstract-full-20260514.md)
- 103 structured abstract worksheets exist
- all 59 diabetes extension `abstract_weighted` cards have abstract-only worksheets
- all 44 obesity `abstract_weighted` cards have abstract-only worksheets
- 78 title-only cards remain without structured abstract worksheets because Crossref did not expose an abstract or DOI resolution failed
- no source card was promoted above `abstract_weighted`
- no topic pages were updated from these worksheets

## Full-Text Availability Sample Completed

Before any full-text deep extraction, a 10-source availability sample was run:

```bash
python3 scripts/source_fulltext_availability.py \
  --repo-root . \
  --source-ids src-diabetes-050,src-diabetes-087,src-diabetes-046,src-diabetes-035,src-diabetes-091,src-obesity-001,src-obesity-004,src-obesity-005,src-obesity-008,src-obesity-080 \
  --source-label 'diabetes obesity deep-extraction candidate availability sample 2026-05-14' \
  --report-id feline-diabetes-obesity-fulltext-availability-sample-20260514 \
  --out system/indexes/feline-diabetes-obesity-fulltext-availability-sample-20260514.md \
  --probe-links \
  --probe-limit 2
```

Result:

- report: [feline diabetes / obesity full-text availability sample](feline-diabetes-obesity-fulltext-availability-sample-20260514.md)
- 10 Crossref metadata records resolved
- 10/10 had Crossref full-text/TDM links
- 9/10 had license metadata
- 5/10 had at least one reachable HEAD probe
- no article body was downloaded or stored
- no source card was promoted above `abstract_weighted` / `title_only`

## Next Non-One-Off Step

The next reusable step is running full-text deep extraction for the highest-value branch owners whose article access has been verified. Do not manually thicken random cards. Use the existing deep-extraction workflow, and update source indexes / depth maps after each extraction batch.

## Cron Decision

No cron.

This sheet is event-driven, not a living scheduled queue. Cron would be noise unless the sheet becomes an explicitly maintained recurring intake source.

## Karpathy Gap Read

This batch improves the `Data ingest`, `Retrieval hygiene`, and `Compile discipline` layers of the Karpathy-style LLM wiki.

It improves source discoverability because many title-only cards are now abstract-weighted, and structured abstract worksheets improve branch placement for 103 abstract-available sources. It still does not create sentence-level auditability or decision-grade claim lookup for the new rows, because abstract-only worksheets are not full-text deep extraction.

The product-quality next move is selective deep extraction with health checks, not another one-off hand conversion.
