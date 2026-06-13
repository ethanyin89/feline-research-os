---
id: feline-ckd-sheet-intake-sample-20260605
type: system
topic: ckd
last_compiled_at: 2026-06-05
owner: codex
status: pending-approval
verification_status: compiled
decision_grade: no
source_sheet: "Google Sheet feline-research-os, tab feline CKD, gid 396361602"
---

# Feline CKD Sheet Intake Sample, 2026-06-05

## Source

Google Sheet:

`https://docs.google.com/spreadsheets/d/1Y-MSR39kW5F5J4OedcctdeHk0jhe1mbyvsK43Fcc7lk/edit?gid=396361602#gid=396361602`

Resolved tab:

| Sheet | sheetId | Range Read | Shape |
|---|---:|---|---|
| `feline CKD` | `396361602` | `A1:B1000` | 51 non-empty source rows |

The tab is a two-column source list with no header row:

- column A: title
- column B: URL / locator

## Manual Sample Classification

| Sheet Row | Title | Initial Classification | Reason |
|---:|---|---|---|
| 1 | Feline CKD: Pathophysiology and risk factors — what do we know? | existing seed | Matches `src-ckd-001` in the mature 24-source CKD seed corpus. |
| 4 | ISFM Consensus Guidelines on the Diagnosis and Management of Feline Chronic Kidney Disease | existing seed | Matches `src-ckd-004`; guideline anchor already deep-extracted. |
| 18 | Early detection of feline chronic kidney disease via 3-hydroxykynurenine and machine learning | existing seed | Matches `src-ckd-018`; early-detection/ML biomarker source already deep-extracted. |
| 24 | Renal biomarkers in cats: A review of the current status in chronic kidney disease | existing seed | Matches `src-ckd-024`; biomarker review already deep-extracted. |
| 25 | Resistivity and pulsatility indexes in feline kidney disease: a systematic review | new CKD extension | Beyond the 24-source seed; likely imaging/ultrasound endpoint extension. |
| 27 | Serum fibroblast growth factor 23 (FGF-23): associations with hyperphosphatemia and clinical staging of feline chronic kidney disease | new CKD extension | High-value mineral-burden / endpoint extension; likely relevant to phosphorus-control artifacts. |
| 29 | Feline Morbillivirus, a New Paramyxovirus Possibly Associated with Feline Kidney Disease | new CKD extension / mechanism caution | Kidney association source, but title says `possibly`; likely mechanism/hypothesis branch, not routine CKD authority. |
| 36 | Chronic kidney disease in cats | new CKD extension / broad review candidate | PubMed locator; title is generic and may duplicate review coverage, but likely a compact review source. |
| 46 | Investigating the Efficacy of Kidney-Protective Lactobacillus Mixture-Containing Pet Treats in Feline Chronic Kidney Disease and Its Possible Mechanism | new CKD extension / intervention caution | Product-like intervention source; should be source-checked before any treatment claim. |
| 51 | The nutritional management of feline chronic kidney disease | incomplete locator | Title only, no URL in sheet. Must not become a source card until locator is recovered. |

## Intake Judgment

This sheet is not a new CKD bootstrap.

It is a CKD extension intake list:

- rows 1-24 map to the existing mature CKD seed corpus,
- rows 25-50 are likely extension candidates,
- row 51 is title-only and needs locator recovery.

## Completed Intake Step

The reusable intake manifest script was run against the local CSV snapshot:

`system/intake-queue/feline-ckd-google-sheet-20260605.csv`

- Manifest: `system/indexes/feline-ckd-intake-manifest-20260605.md`
- Sample source cards created for rows 25, 27, 28, 35, 37, and 46.
- Priority source cards created for rows 30, 36, 39, 41, and 50.
- Remaining locator-bearing extension source cards created for rows 26, 29, 31, 32, 33, 34, 38, 40, 42, 43, 44, 45, 47, 48, and 49.
- Metadata check reports:
  - `system/indexes/feline-ckd-extension-source-check-sample-20260605.md`
  - `system/indexes/feline-ckd-extension-source-check-priority-20260605.md`
  - `system/indexes/feline-ckd-extension-source-check-remaining-20260605.md`
- `src-ckd-025` and `src-ckd-026` were upgraded only to `abstract_weighted`.
- `src-ckd-027` through `src-ckd-030` remain `title_only`.
- `src-ckd-033`, `src-ckd-034`, and `src-ckd-035` were upgraded only to `abstract_weighted`.
- `src-ckd-031` and `src-ckd-032` remain `title_only`.
- `src-ckd-043`, `src-ckd-045`, and `src-ckd-046` were upgraded only to `abstract_weighted`.
- All other extension cards remain `title_only`.

The current regenerated manifest has `50` existing rows and `1` incomplete-locator row. Row 51 is title-only and must not become a source card until a locator is recovered.
