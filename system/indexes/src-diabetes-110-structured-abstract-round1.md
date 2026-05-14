---
id: src-diabetes-110-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-diabetes-110]
language: zh
last_compiled_at: 2026-05-14
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-diabetes-110 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref metadata and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-diabetes-110` |
| Title | Comparison of insulin infusion protocols for management of canine and feline diabetic ketoacidosis |
| DOI | `10.1111/vec.13354` |
| Container | Journal of Veterinary Emergency and Critical Care |
| Year | 2024 |
| Current card status | `abstract_weighted` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | original study |
| Population / sample signal | cats mentioned; count not mechanically extracted |
| Detected section labels | objective, animals, results, conclusions |
| Endpoint / theme signals | insulin, glucose, survival |

Short abstract lead for scope check only:

> Abstract Objective Describe the use of fixed‐rate intravenous insulin infusions (FRIs) in cats and dogs with diabetic k...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: insulin, glucose, survival
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
