---
id: src-diabetes-090-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-diabetes-090]
language: zh
last_compiled_at: 2026-05-14
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-diabetes-090 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref metadata and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-diabetes-090` |
| Title | Pasireotide for the Medical Management of Feline Hypersomatotropism |
| DOI | `10.1111/jvim.12608` |
| Container | Journal of Veterinary Internal Medicine |
| Year | 2015 |
| Current card status | `abstract_weighted` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | original study |
| Population / sample signal | 12 cats |
| Detected section labels | background, animals, methods, results, conclusions |
| Endpoint / theme signals | insulin, glucose |

Short abstract lead for scope check only:

> Abstract Background Feline hypersomatotropism (HST) is a cause of diabetes mellitus in cats. Pasireotide is a novel mul...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: insulin, glucose
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
