---
id: cancer-source-depth-map
type: system
topic: cancer
question_type: source-depth-map
language: zh
last_compiled_at: 2026-05-30
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# Cancer Source Depth Map

## Summary

| Depth | Count | Meaning |
|---|---:|---|
| `title_only` | 73 | first-pass title/locator card only |
| `abstract_weighted` | 23 | Crossref or publisher metadata plus abstract availability |
| structured abstract worksheet | 10 | abstract-only worksheet exists |
| full-text availability sample | 14 | Crossref TDM/link probe plus manual access verification for selected candidates |
| `deep_extracted` | 6 | `src-cancer-002` registry denominator anchor; `src-cancer-004` molecular branch-map anchor; `src-cancer-019` mammary/TNBC model anchor; `src-cancer-003` COX/prognosis marker anchor; `src-cancer-040` practitioner workflow anchor; `src-cancer-008` lymphoma pathology anchor |

## Structured Abstract Sample

| Source | Current depth | Worksheet |
|---|---|---|
| `src-cancer-003` | `deep_extracted` | [src-cancer-003 structured abstract](src-cancer-003-structured-abstract-round1.md) |
| `src-cancer-004` | `deep_extracted` | [src-cancer-004 structured abstract](src-cancer-004-structured-abstract-round1.md) |
| `src-cancer-005` | `abstract_weighted` | [src-cancer-005 structured abstract](src-cancer-005-structured-abstract-round1.md) |
| `src-cancer-008` | `deep_extracted` | [src-cancer-008 structured abstract](src-cancer-008-structured-abstract-round1.md) |
| `src-cancer-009` | `abstract_weighted` | [src-cancer-009 structured abstract](src-cancer-009-structured-abstract-round1.md) |
| `src-cancer-019` | `deep_extracted` | [src-cancer-019 structured abstract](src-cancer-019-structured-abstract-round1.md) |
| `src-cancer-021` | `abstract_weighted` | [src-cancer-021 structured abstract](src-cancer-021-structured-abstract-round1.md) |
| `src-cancer-025` | `abstract_weighted` | [src-cancer-025 structured abstract](src-cancer-025-structured-abstract-round1.md) |
| `src-cancer-040` | `deep_extracted` | [src-cancer-040 structured abstract](src-cancer-040-structured-abstract-round1.md) |
| `src-cancer-046` | `abstract_weighted` | [src-cancer-046 structured abstract](src-cancer-046-structured-abstract-round1.md) |

## Boundary

This map is a processing control page, not a synthesis page. It says which cards are eligible for deeper work. It does not make medical, diagnostic, prognostic, or treatment claims.

## Full-Text Availability Sample

Full-text availability sample completed for high-reuse branch-control sources:

- `src-cancer-004`, molecular mechanisms review
- `src-cancer-005`, comparative oncology review
- `src-cancer-008`, lymphoma / lymphoproliferative classification
- `src-cancer-009`, metastatic mammary cancer outcomes
- `src-cancer-025`, mammary carcinoma prognosis review
- `src-cancer-046`, oral SCC clinical review

Result: all 6 have Crossref full-text/TDM links and abstracts; only `src-cancer-004` had a reachable HEAD probe during this check. The other 5 should be treated as access leads, not confirmed extraction-ready files.

Second continuation sample completed for:

- `src-cancer-019`, mammary basal-like / TNBC model
- `src-cancer-021`, oral SCC natural model

Result: `src-cancer-019` had reachable BMC Cancer / Springer Nature HTML and was deep-extracted. `src-cancer-021` had Crossref links but the Hindawi page returned a Cloudflare challenge and should remain access-blocked until a non-challenge source is available.

Third continuation sample completed for:

- `src-cancer-003`, COX expression / prognosis systematic review
- `src-cancer-040`, practical cancer starting-point review

Result: `src-cancer-003` had reachable Europe PMC full-text XML and was deep-extracted. `src-cancer-040` local direct fetch returned browser/challenge pages, but the SAGE full article page was browser-readable and was deep-extracted.

Fourth continuation sample completed for:

- `src-cancer-008`, lymphoma / lymphoproliferative disease classification
- `src-cancer-046`, oral SCC clinical manifestations review

Result: `src-cancer-008` local direct fetch returned HTTP 403, but the SAGE PDF was browser-readable and was deep-extracted. `src-cancer-046` exposed abstract/references only during this run and remains abstract-weighted / full-text blocked.

Fifth continuation sample completed for:

- `src-cancer-002`, Swiss Feline Cancer Registry 1965-2008
- `src-cancer-007`, South Africa feline cancer prevalence

Result: `src-cancer-002` had an ETH Research Collection open-access record and browser-readable PDF text and was deep-extracted as the first registry denominator anchor. `src-cancer-007` had an accessible publisher page and abstract, but direct PDF access returned verification / 404 responses during local probing, so it remains abstract-weighted / full-text blocked.

## Deep Extraction Sample

| Source | Current depth | Worksheet | Boundary |
|---|---|---|---|
| `src-cancer-002` | `deep_extracted` | [src-cancer-002 deep extraction](src-cancer-002-deep-extraction-round1.md) | registry proportions and branch priority, not population incidence or causality |
| `src-cancer-003` | `deep_extracted` | [src-cancer-003 deep extraction](src-cancer-003-deep-extraction-round1.md) | COX/prognosis marker layer, not treatment guidance |
| `src-cancer-004` | `deep_extracted` | [src-cancer-004 deep extraction](src-cancer-004-deep-extraction-round1.md) | molecular branch map, not treatment guidance |
| `src-cancer-008` | `deep_extracted` | [src-cancer-008 deep extraction](src-cancer-008-deep-extraction-round1.md) | lymphoma pathology classification, not treatment or prognosis guidance |
| `src-cancer-019` | `deep_extracted` | [src-cancer-019 deep extraction](src-cancer-019-deep-extraction-round1.md) | mammary carcinoma / TNBC model branch, not treatment guidance |
| `src-cancer-040` | `deep_extracted` | [src-cancer-040 deep extraction](src-cancer-040-deep-extraction-round1.md) | practitioner workflow shell, not tumor-specific treatment guidance |
