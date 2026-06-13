---
id: src-ckd-034-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-ckd-034]
language: zh
last_compiled_at: 2026-06-05
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-ckd-034 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref metadata and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-ckd-034` |
| Title | Risk and protective factors for cats with naturally occurring chronic kidney disease |
| DOI | `10.1177/1098612x15625453` |
| Container | Journal of Feline Medicine and Surgery |
| Year | 2017 |
| Current card status | `abstract_weighted` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | original study |
| Population / sample signal | 101 cats |
| Detected section labels | methods, results, conclusions |
| Endpoint / theme signals | risk factor, chronic kidney disease |

Short abstract lead for scope check only:

> Objectives Chronic kidney disease (CKD) is a significant disease in cats. Identifying risk and protective factors may h...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: risk factor, chronic kidney disease
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
