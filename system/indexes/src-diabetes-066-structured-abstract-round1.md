---
id: src-diabetes-066-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-diabetes-066]
language: zh
last_compiled_at: 2026-05-14
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-diabetes-066 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref metadata and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-diabetes-066` |
| Title | Prevalence of feline cataract: results of a cross‐sectional study of 2000 normal animals, 50 cats with diabetes and one hundred cats following dehydrational crises |
| DOI | `10.1111/j.1463-5224.2006.00497.x` |
| Container | Veterinary Ophthalmology |
| Year | 2006 |
| Current card status | `abstract_weighted` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | original study |
| Population / sample signal | 50 cats |
| Detected section labels | objective, animals, methods, results |
| Endpoint / theme signals | none mechanically detected |

Short abstract lead for scope check only:

> Abstract Objective In this study 2000 normal cats, 50 cats with diabetes and 100 cats with a history of dehydrational c...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: needs human source review
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
