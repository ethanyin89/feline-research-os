---
id: src-obesity-066-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-obesity-066]
language: zh
last_compiled_at: 2026-05-14
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-obesity-066 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref metadata and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-obesity-066` |
| Title | The effect of obesity and subsequent weight reduction on cardiac morphology and function in cats |
| DOI | `10.1186/s12917-024-04011-0` |
| Container | BMC Veterinary Research |
| Year | 2024 |
| Current card status | `abstract_weighted` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | original study |
| Population / sample signal | 20 cats |
| Detected section labels | background, results |
| Endpoint / theme signals | weight, obesity, risk factor |

Short abstract lead for scope check only:

> Abstract Background In people, obesity is a risk factor for cardiovascular disease, associated with systemic hypertensi...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: weight, obesity, risk factor
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
