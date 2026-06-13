---
id: src-ckd-179-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-ckd-179]
language: zh
last_compiled_at: 2026-06-13
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-ckd-179 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-ckd-179` |
| Title | Systolic blood pressure, routine kidney variables and renal ultrasonographic findings in cats naturally infected with feline immunodeficiency virus |
| DOI | `10.1177/1098612x16653165` |
| Metadata provider | Crossref |
| Container | Journal of Feline Medicine and Surgery |
| Year | 2017 |
| Current card status | `title_only` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | review |
| Population / sample signal | cats mentioned; count not mechanically extracted |
| Detected section labels | methods, results, conclusions |
| Endpoint / theme signals | proteinuria, ultrasonography |

Short abstract lead for scope check only:

> Objectives Hypertension is a common cause of proteinuria in HIV-infected people. In cats, feline immunodeficiency virus...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: proteinuria, ultrasonography
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
