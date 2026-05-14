---
id: src-diabetes-113-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-diabetes-113]
language: zh
last_compiled_at: 2026-05-14
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-diabetes-113 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref metadata and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-diabetes-113` |
| Title | Evaluation of routine hematology profile results and fructosamine, thyroxine, insulin, and proinsulin concentrations in lean, overweight, obese, and diabetic cats |
| DOI | `10.2460/javma.243.9.1302` |
| Container | Journal of the American Veterinary Medical Association |
| Year | 2013 |
| Current card status | `abstract_weighted` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | original study |
| Population / sample signal | 117 cats |
| Detected section labels | objective, animals, procedures, results, conclusions, clinical relevance |
| Endpoint / theme signals | insulin, glucose, weight, body condition, overweight |

Short abstract lead for scope check only:

> Abstract Objective —To compare results of hematologic testing in nondiabetic and diabetic cats to identify possible ind...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: insulin, glucose, weight, body condition, overweight
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
