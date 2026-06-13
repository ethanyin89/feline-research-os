# Handoff: CKD Google Sheet Intake

Date: 2026-06-05
Branch: `idea-chatacademia-research-workbench`
Status: CKD sheet intake complete for all rows with locators; row 51 remains blocked

## Source

User-provided Google Sheet:

`https://docs.google.com/spreadsheets/d/1Y-MSR39kW5F5J4OedcctdeHk0jhe1mbyvsK43Fcc7lk/edit?gid=396361602#gid=396361602`

Resolved tab:

- Spreadsheet title: `feline-research-os`
- Tab: `feline CKD`
- GID / sheetId: `396361602`
- Range read: `A1:B1000`
- Non-empty source rows: `51`

## What Happened

This was handled as a CKD extension intake, not a new CKD bootstrap.

- Rows 1-24 match the existing mature CKD seed corpus (`src-ckd-001` through `src-ckd-024`).
- Rows 25-50 were CKD extension candidates before sample-card creation.
- Row 51 is title-only and has no locator; it is blocked until a URL, DOI, PubMed ID, or other durable locator is recovered.

After all rows with locators were created as guarded intake cards and the manifest was regenerated, the current manifest counts are:

- `existing`: 50
- `incomplete-locator`: 1

Local snapshot:

- `system/intake-queue/feline-ckd-google-sheet-20260605.csv`

Review artifacts:

- `system/indexes/feline-ckd-sheet-intake-sample-20260605.md`
- `system/indexes/feline-ckd-intake-manifest-20260605.md`
- `system/indexes/feline-ckd-extension-source-check-sample-20260605.md`
- `system/indexes/feline-ckd-extension-source-check-priority-20260605.md`
- `system/indexes/feline-ckd-extension-source-check-remaining-20260605.md`
- `system/indexes/feline-ckd-extension-structured-abstract-20260605.md`
- `system/indexes/feline-ckd-extension-claim-fit-queue-20260605.md`
- `outputs/business/ckd-fgf23-phosphorus-staging-claim-card-20260605.md`
- `outputs/business/ckd-risk-protective-factors-architecture-claim-card-20260605.md`

Navigation indexes updated:

- `system/indexes/ckd-source-index.md`
- `system/indexes/source-depth-map.md`

## Source Cards Created

Twenty-six cards were created from the extension set in guarded batches:

| Sheet Row | Source ID | Current Depth | Verification | Note |
|---:|---|---|---|---|
| 25 | `src-ckd-025` | partial | abstract_weighted | DOI and Crossref abstract resolved. |
| 27 | `src-ckd-026` | partial | abstract_weighted | DOI and Crossref abstract resolved. |
| 28 | `src-ckd-027` | partial | title_only | DOI metadata resolved, but no Crossref abstract. |
| 35 | `src-ckd-028` | partial | title_only | No DOI in card. |
| 37 | `src-ckd-029` | partial | title_only | DOI metadata resolved, but no Crossref abstract. |
| 46 | `src-ckd-030` | partial | title_only | No DOI in card. |
| 30 | `src-ckd-031` | partial | title_only | No DOI in card. |
| 36 | `src-ckd-032` | partial | title_only | No DOI in card. |
| 39 | `src-ckd-033` | partial | abstract_weighted | DOI and Crossref abstract resolved. |
| 41 | `src-ckd-034` | partial | abstract_weighted | DOI and Crossref abstract resolved. |
| 50 | `src-ckd-035` | partial | abstract_weighted | DOI and Crossref abstract resolved. |
| 26 | `src-ckd-036` | partial | title_only | No DOI in card. |
| 29 | `src-ckd-037` | partial | title_only | No DOI in card. |
| 31 | `src-ckd-038` | partial | title_only | No DOI in card. |
| 32 | `src-ckd-039` | partial | title_only | No DOI in card. |
| 33 | `src-ckd-040` | partial | title_only | No DOI in card. |
| 34 | `src-ckd-041` | partial | title_only | No DOI in card. |
| 38 | `src-ckd-042` | partial | title_only | No DOI in card. |
| 40 | `src-ckd-043` | partial | abstract_weighted | DOI and Crossref abstract resolved. |
| 42 | `src-ckd-044` | partial | title_only | No DOI in card. |
| 43 | `src-ckd-045` | partial | abstract_weighted | DOI and Crossref abstract resolved. |
| 44 | `src-ckd-046` | partial | abstract_weighted | DOI and Crossref abstract resolved. |
| 45 | `src-ckd-047` | partial | title_only | No DOI in card. |
| 47 | `src-ckd-048` | partial | title_only | No DOI in card. |
| 48 | `src-ckd-049` | partial | title_only | No DOI in card. |
| 49 | `src-ckd-050` | partial | title_only | DOI metadata resolved, but no Crossref abstract. |

These cards are for source ownership and triage only. They must not support reader-facing CKD claims until abstract extraction, source worksheet review, or full-text extraction is complete.

Abstract-weighted cards after metadata checks:

- `src-ckd-025`
- `src-ckd-026`
- `src-ckd-033`
- `src-ckd-034`
- `src-ckd-035`
- `src-ckd-043`
- `src-ckd-045`
- `src-ckd-046`

All other extension cards remain `title_only`.

Structured abstract worksheets were created for the eight `abstract_weighted` cards:

- `system/indexes/src-ckd-025-structured-abstract-round1.md`
- `system/indexes/src-ckd-026-structured-abstract-round1.md`
- `system/indexes/src-ckd-033-structured-abstract-round1.md`
- `system/indexes/src-ckd-034-structured-abstract-round1.md`
- `system/indexes/src-ckd-035-structured-abstract-round1.md`
- `system/indexes/src-ckd-043-structured-abstract-round1.md`
- `system/indexes/src-ckd-045-structured-abstract-round1.md`
- `system/indexes/src-ckd-046-structured-abstract-round1.md`

## Script Changes

`scripts/literature_source_card_bootstrap.py`

- Added support for `new-ckd`.
- Added CKD/kidney/renal/chronic/disease stopwords to generated source-card tags.

`scripts/literature_sheet_intake.py`

- Title-only rows with empty locators now classify as `incomplete-locator`, not `new-*`.

`scripts/structured_abstract_extraction.py`

- Added CKD-specific endpoint/theme terms so structured abstract worksheets detect phosphorus, FGF-23, proteinuria, UTI, cytokine, uremic toxin, and ultrasound signals.
- Tightened `weight` detection to avoid non-body-weight false positives.
- Tightened source-family inference so guideline/consensus is driven by title-level evidence.

`system/indexes/ckd-source-index.md`

- Added a 2026-06-05 extension intake queue for `src-ckd-025` through `src-ckd-050`.

`system/indexes/source-depth-map.md`

- Updated CKD from `24` cards to `50` cards.
- Updated total strict disease paper cards from `325` to `351`.
- Marked CKD extension corpus as `26 ingested`, with `8 abstract_weighted` and `18 title_only`.
- Added the 8 CKD extension structured-abstract worksheets to the CKD depth row.

`outputs/business/ckd-fgf23-phosphorus-staging-claim-card-20260605.md`

- Added a non-promotable claim card around `src-ckd-026`.
- Verdict is `ABSENT / SOURCE_REVIEW_REQUIRED`; this is an extraction-planning artifact, not a supported claim.
- Submitted to `system/indexes/artifact-review-queue.json` as `ART-ckd_fgf23_phosphorus-01` with status `review`.
- Added queue comment: do not promote until `src-ckd-026` receives real abstract or full-text extraction.

`outputs/business/ckd-risk-protective-factors-architecture-claim-card-20260605.md`

- Added a non-promotable claim card around `src-ckd-034`.
- Verdict is `ABSENT / SOURCE_REVIEW_REQUIRED`; this is an extraction-planning artifact, not a supported risk-ranking claim.
- Submitted to `system/indexes/artifact-review-queue.json` as `ART-ckd_risk_protective_-01` with status `review`.
- Added queue comment: do not promote until `src-ckd-034` receives real abstract or full-text extraction and is compared with seed CKD risk sources.

## Verification

Ran:

```bash
python3 -m py_compile scripts/literature_sheet_intake.py scripts/literature_source_card_bootstrap.py scripts/source_metadata_check.py scripts/structured_abstract_extraction.py
python3 scripts/business_value_eval.py --artifact outputs/business/ckd-fgf23-phosphorus-staging-claim-card-20260605.md --verbose
python3 scripts/business_value_eval.py --artifact outputs/business/ckd-risk-protective-factors-architecture-claim-card-20260605.md --verbose
```

Result: passed.

## Suggested Next Move

Do not create row 51 until a locator is recovered.

Best next content step:

1. Use `system/indexes/feline-ckd-extension-claim-fit-queue-20260605.md` to choose the next narrow extraction target.
2. `src-ckd-026` and `src-ckd-034` now have non-promotable review artifacts; the next queue item is likely `src-ckd-033` for CKD + UTI boundary.
3. Consider real abstract extraction for `src-ckd-026`, `src-ckd-033`, `src-ckd-034`, and `src-ckd-035` because they now have abstract availability and may affect phosphorus staging, UTI boundary, risk architecture, or inflammatory endpoint claims.
4. Consider real abstract extraction for `src-ckd-043`, `src-ckd-045`, and `src-ckd-046` if the next CKD artifact needs uremic toxin, proteinuria, or ultrasound-boundary evidence.
5. Recover stronger locators or DOI metadata for `src-ckd-031`, `src-ckd-032`, and the other title-only extension cards before trying to use them as broad authorities.
6. Keep product-like intervention rows, especially row 46 / `src-ckd-030`, behind a stricter source-check boundary before any treatment-facing artifact uses them.
