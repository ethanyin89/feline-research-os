---
id: topic-cancer-current-state-dashboard
type: topic
topic: cancer
language: zh
last_compiled_at: 2026-05-30
verification_status: compiled
decision_grade: no
owner: codex
status: architecture-compiled
---

# Feline Cancer Current State Dashboard

## Status

| Area | State | Note |
|---|---|---|
| Intake | active | 111 sheet rows classified in the 2026-05-30 manifest |
| Existing overlap | partial | one row matches existing `src-obesity-085` cachexia/body-condition source |
| False positives | known risk | acronym, algorithm, gene/protein, and vector rows need exclusion review |
| Source cards | first-pass complete | `src-cancer-001..102` exist |
| Metadata / abstract check | complete | 29/102 cards are `abstract_weighted`; 67 remain `title_only`; 6 are `deep_extracted` |
| Structured abstract worksheets | sample complete | 10 abstract-only worksheets exist |
| Full-text availability | sample complete | 14 branch-control candidates checked across five samples; `src-cancer-007`, `src-cancer-021`, and `src-cancer-046` remain access/full-text blocked |
| Deep extraction | sample complete | `src-cancer-002` is the registry denominator anchor; `src-cancer-004` is the molecular branch-map anchor; `src-cancer-008` is the lymphoma pathology anchor; `src-cancer-019` is the mammary/TNBC model anchor; `src-cancer-003` is the COX/prognosis marker anchor; `src-cancer-040` is the practitioner workflow anchor |
| Reader-facing synthesis | architecture compiled | 8 branch pages compiled (workflow, mammary, lymphoma, oral SCC, FISS, COX, registry, index); treatment and prognosis guidance remain gated |
| Branch-control candidates | mapped | 5 open synthesis questions mapped to candidate sources; MDPI open-access extraction priority identified |

## Compiled Architecture Pages

- [Synthesis index](synthesis-index.md)
- [Suspected cancer workflow](suspected-cancer-workflow.md)
- [Lymphoma](lymphoma.md) — updated with FeLV-shift, demographics, molecular context
- [Mammary carcinoma](mammary-carcinoma.md)
- [Oral squamous cell carcinoma](oral-squamous-cell-carcinoma.md) — new, etiology branch
- [Injection site sarcoma (FISS)](injection-site-sarcoma.md) — new, adjuvant hypothesis branch
- [COX and prognosis marker caveats](cox-prognosis-markers.md)
- [Registry and prevalence](registry-and-prevalence.md)

## Strongest Early Candidate Branches

- broad feline oncology / oncogenomics reviews
- suspected-cancer clinical workflow
- cancer registry and prevalence papers
- mammary carcinoma comparative oncology
- mammary carcinoma / TNBC-like basal phenotype model
- COX / prognosis-marker caveats
- lymphoma and lymphoproliferative disease
- oral squamous cell carcinoma
- FeLV-associated neoplasia

## Do Not Do Yet

- do not rank treatments
- do not state prognosis ranges as reusable claims
- do not promote comparative oncology model papers into clinical guidance
- do not ingest rows where `feline` is only an acronym or non-cat label
