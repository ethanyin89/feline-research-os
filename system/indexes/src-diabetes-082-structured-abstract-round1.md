---
id: src-diabetes-082-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-diabetes-082]
language: zh
last_compiled_at: 2026-06-09
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-diabetes-082 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses PubMed and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-diabetes-082` |
| Title | Loose-control of diabetes mellitus with protamine zinc insulin in cats: 185 cases (2005-2015). |
| DOI | `not available` |
| Metadata provider | PubMed |
| Container | The Canadian veterinary journal = La revue veterinaire canadienne |
| Year | 2019 |
| Current card status | `title_only` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | original study |
| Population / sample signal | cats mentioned; count not mechanically extracted |
| Detected section labels | none mechanically detected |
| Endpoint / theme signals | insulin, glucose, remission, survival |

Short abstract lead for scope check only:

> This study evaluated the outcome of cats with diabetes mellitus treated with a loose-control approach using protamine z...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: insulin, glucose, remission, survival
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
