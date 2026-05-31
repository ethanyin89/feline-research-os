---
id: cancer-source-index
type: system
topic: cancer
question_type: source-index
language: zh
last_compiled_at: 2026-05-30
verification_status: draft
decision_grade: no
owner: codex
status: starter
---

# Cancer Source Index

## Intake Summary

Source: [feline cancer intake manifest](feline-cancer-intake-manifest-20260530.md)

| Classification | Count |
|---|---:|
| `existing` | 102 |
| `out-of-scope` | 8 |
| `shared-existing` | 1 |

## Processing Status

| Layer | Count | Evidence boundary |
|---|---:|---|
| First-pass source cards | 102 | title/locator ownership only |
| `title_only` cards | 73 | no abstract-weighted upgrade yet |
| `abstract_weighted` cards | 23 | Crossref or publisher abstract availability only |
| Structured abstract worksheets | 10 | abstract-only worksheets, not full text |
| Deep-extracted cards | 6 | molecular branch-map, lymphoma classification, mammary/TNBC model, COX/prognosis marker, practitioner workflow, and registry denominator anchors |

## First-Pass Sample Cards

| ID | Sheet Row | Title | Primary Layer | Evidence Level | Status |
|---|---:|---|---|---|---|
| `src-cancer-001` | 1 | Feline Oncogenomics: What Do We Know about the Genetics of Cancer in Domestic Cats? | review | review | first-pass card; title_only |
| `src-cancer-002` | 3 | Swiss Feline Cancer Registry 1965-2008: the Influence of Sex, Breed and Age on Tumour Types and Tumour Locations | registry | original-study | deep-extracted; registry denominator anchor |
| `src-cancer-003` | 4 | The role of COX expression in the prognostication of overall survival of canine and feline cancer: A systematic review | review | review | deep-extracted; COX/prognosis marker anchor |
| `src-cancer-004` | 5 | Molecular Mechanisms of Feline Cancers | mechanism | review | deep-extracted; molecular branch-map anchor |
| `src-cancer-005` | 6 | Cats, Cancer and Comparative Oncology | comparative-oncology | review | first-pass card; abstract_weighted |
| `src-cancer-006` | 7 | Current information on feline and canine cancers and relationship or lack of relationship to human cancer | context | review | first-pass card; title_only |
| `src-cancer-007` | 8 | Feline cancer prevalence in South Africa (1998-2005): contrasts with the rest of the world | epidemiology | original-study | abstract-weighted; full-text blocked comparator |
| `src-cancer-008` | 9 | The Histologic Classification of 602 Cases of Feline Lymphoproliferative Disease using the National Cancer Institute Working Formulation | lymphoma | original-study | deep-extracted; lymphoma pathology classification anchor |
| `src-cancer-009` | 10 | Metastatic feline mammary cancer: prognostic factors, outcome and comparison of different treatment modalities | mammary-carcinoma | original-study | first-pass card; abstract_weighted |
| `src-cancer-010` | 11 | Oncolytic virotherapy of canine and feline cancer | therapy | review | first-pass card; title_only |

## Structured Abstract Sample

| Source | Role | Worksheet |
|---|---|---|
| `src-cancer-003` | systematic review / COX prognosis | [worksheet](src-cancer-003-structured-abstract-round1.md) |
| `src-cancer-004` | molecular mechanisms review | [worksheet](src-cancer-004-structured-abstract-round1.md) |
| `src-cancer-005` | comparative oncology review | [worksheet](src-cancer-005-structured-abstract-round1.md) |
| `src-cancer-008` | lymphoproliferative classification anchor | [worksheet](src-cancer-008-structured-abstract-round1.md) |
| `src-cancer-009` | metastatic mammary cancer outcomes | [worksheet](src-cancer-009-structured-abstract-round1.md) |
| `src-cancer-019` | mammary basal-like / TNBC model | [worksheet](src-cancer-019-structured-abstract-round1.md) |
| `src-cancer-021` | oral SCC natural model | [worksheet](src-cancer-021-structured-abstract-round1.md) |
| `src-cancer-025` | mammary carcinoma prognosis review | [worksheet](src-cancer-025-structured-abstract-round1.md) |
| `src-cancer-040` | practical oncology orientation | [worksheet](src-cancer-040-structured-abstract-round1.md) |
| `src-cancer-046` | oral SCC clinical/literature review | [worksheet](src-cancer-046-structured-abstract-round1.md) |

## Deep Extraction Sample

| Source | Role | Worksheet | Promotion boundary |
|---|---|---|---|
| `src-cancer-002` | Swiss registry / epidemiology | [deep extraction](src-cancer-002-deep-extraction-round1.md) | registry proportions and branch priority only; not population incidence or causality |
| `src-cancer-003` | COX/prognosis marker systematic review | [deep extraction](src-cancer-003-deep-extraction-round1.md) | prognosis-marker caveats only; not treatment guidance or survival prediction |
| `src-cancer-004` | molecular branch-map review | [deep extraction](src-cancer-004-deep-extraction-round1.md) | branch placement and extraction priority only; not treatment guidance |
| `src-cancer-008` | lymphoma pathology classification case series | [deep extraction](src-cancer-008-deep-extraction-round1.md) | classification and topography only; not treatment or modern immunophenotype guidance |
| `src-cancer-019` | mammary carcinoma / TNBC-like model study | [deep extraction](src-cancer-019-deep-extraction-round1.md) | marker and comparative-model boundaries only; not treatment guidance |
| `src-cancer-040` | practitioner workflow review | [deep extraction](src-cancer-040-deep-extraction-round1.md) | presentation, diagnosis, and staging workflow only; not tumor-specific treatment guidance |

## Source Family / Claim-Fit Map

| Family | Strongest safe use | Must not control |
|---|---|---|
| broad review / oncogenomics | shell architecture, branch naming, mechanism landscape | treatment ranking, prognosis certainty |
| registry / epidemiology | frequency, signalment, tumor-type distribution within its population | universal prevalence, causality |
| original clinical study | endpoint ownership, branch-specific detail | standard-of-care authority |
| comparative oncology model paper | model logic, translational relevance | feline clinical recommendation |
| cell-line / in vitro paper | mechanism or target hypothesis | patient-level efficacy |

## Current Do-Not-Control Notes

- `shared-existing` rows should cross-link to their current owner unless cancer needs a distinct claim-fit card.
- `out-of-scope` rows should not receive source cards without abstract/full-text justification.
- The first-pass corpus is title/locator-led unless a card is explicitly `abstract_weighted`.
- Structured abstract worksheets can guide branch placement and extraction priority, but must not drive reader-facing pages by themselves.
