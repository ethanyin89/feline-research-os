---
id: cancer-reading-plan-round-1
type: system
topic: cancer
question_type: reading-plan
language: zh
last_compiled_at: 2026-05-30
verification_status: draft
decision_grade: no
owner: codex
status: starter
---

# Cancer Reading Plan Round 1

## Goal

Convert the 2026-05-30 cancer sheet from a raw candidate list into a controlled source queue.

## First 10 Source-Card Sample

The first sample favored broad map and branch-anchor papers before narrow cell-line or therapy experiments:

| Planned ID | Sheet Row | Role |
|---|---:|---|
| `src-cancer-001` | 1 | oncogenomics / broad review candidate |
| `src-cancer-002` | 3 | registry / epidemiology candidate |
| `src-cancer-003` | 4 | systematic review / prognostic marker candidate |
| `src-cancer-004` | 5 | molecular mechanism review candidate |
| `src-cancer-005` | 6 | comparative oncology review candidate |
| `src-cancer-006` | 7 | historical comparative cancer context |
| `src-cancer-007` | 8 | regional prevalence candidate |
| `src-cancer-008` | 9 | lymphoproliferative disease classification anchor |
| `src-cancer-009` | 10 | mammary cancer outcome/treatment candidate |
| `src-cancer-010` | 11 | oncolytic virotherapy candidate |

## Exclusion Review

Rows matching these title patterns are currently excluded before source-card creation:

- `FELINE trial`
- `Feline Wolf Net`
- `feline sarcoma.*protein`
- `Feline immunodeficiency virus vector`
- `Current status of canine cancer registration`
- `domestic cat genome assembly`

These are title-level exclusions, not final literature judgments. Reopen them only if a later abstract/full-text check proves direct cat-oncology relevance.

## Current Status

| Step | Status |
|---|---|
| First-pass card sample | complete, `src-cancer-001..010` |
| Full first-pass bootstrap | complete, `src-cancer-001..102` |
| Full metadata / abstract check | complete, 29 `abstract_weighted`, 67 `title_only`, 6 `deep_extracted` |
| Structured abstract sample | complete, 10 worksheets |
| Full-text availability sample | complete, 14 candidates checked across five samples |
| Deep extraction | sample complete, `src-cancer-002`, `src-cancer-003`, `src-cancer-004`, `src-cancer-008`, `src-cancer-019`, and `src-cancer-040` |
| Topic synthesis | architecture compiled; treatment/prognosis still gated |

## Next Gate

After the fifth deep-extraction / availability sample:

1. use the 6-source sample as the approved reusable cancer deep-extraction skill step
2. keep `src-cancer-007`, `src-cancer-021`, and `src-cancer-046` blocked until non-challenge full-text sources are available
3. deep-extract only sources that will change branch structure or claim boundaries
4. continue branch pages only after branch-control sources are deep-extracted

## Branch-Control Extraction Priority

See [cancer-branch-control-candidates.md](cancer-branch-control-candidates.md) for the full mapping.

The next branch-control extractions should be MDPI open-access sources:

| Priority | Source | Branch | Rationale |
|---|---|---|---|
| 1 | `src-cancer-095` | oral SCC | etiologic review, MDPI open access |
| 2 | `src-cancer-063` | lymphoma | alimentary molecular landscape, MDPI open access |
| 3 | `src-cancer-068` | lymphoma | modern Australian demographics, MDPI open access |

These three sources are prioritized because:
- They address open synthesis questions (oral SCC clinical, lymphoma classification)
- They are on MDPI which is open access
- They would unlock gated branch pages if extracted

Paywalled sources (`src-cancer-047` for FISS, `src-cancer-046` for oral SCC clinical review) remain blocked until institutional access or alternative sources are found.

## Open Synthesis Questions

1. **Lymphoma classification / FeLV-shift**: Current anchor is `src-cancer-008`; need `src-cancer-063` or `src-cancer-065` for modern FeLV context
2. **Oral SCC clinical**: Need `src-cancer-095` (MDPI) since `src-cancer-046` is blocked
3. **FISS boundaries**: Need `src-cancer-047` but it's paywalled; `src-cancer-002` and `src-cancer-004` provide registry context
4. **FISS causality**: Same as above
5. **Treatment outcomes**: Gated until branch architecture is complete
