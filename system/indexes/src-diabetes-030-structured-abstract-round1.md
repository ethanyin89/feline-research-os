---
id: src-diabetes-030-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-diabetes-030]
language: zh
last_compiled_at: 2026-06-09
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-diabetes-030 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref + PubMed abstract and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-diabetes-030` |
| Title | Indoor confinement and physical inactivity rather than the proportion of dry food are risk factors in the development of feline type 2 diabetes mellitus |
| DOI | `10.1016/j.tvjl.2007.08.035` |
| Metadata provider | Crossref + PubMed abstract |
| Container | The Veterinary Journal |
| Year | 2009 |
| Current card status | `title_only` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | original study |
| Population / sample signal | 96 cats |
| Detected section labels | animals, results |
| Endpoint / theme signals | risk factor, activity |

Short abstract lead for scope check only:

> With domestication and urbanisation, cats have transformed from being hunting animals that eat protein-rich prey into m...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: risk factor, activity
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
