---
id: src-obesity-019-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-obesity-019]
language: zh
last_compiled_at: 2026-05-14
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-obesity-019 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref metadata and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-obesity-019` |
| Title | Feline obesity: risk factors and clinical and metabolic findings |
| DOI | `10.5433/1679-0359.2021v42n6p3305` |
| Container | Semina: Ciências Agrárias |
| Year | 2021 |
| Current card status | `abstract_weighted` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | original study |
| Population / sample signal | cats mentioned; count not mechanically extracted |
| Detected section labels | animals |
| Endpoint / theme signals | glucose, quality of life, weight, body condition, obesity, overweight, risk factor, activity |

Short abstract lead for scope check only:

> Excess body fat can cause a series of metabolic and mechanical effects on the body. Therefore, this study aimed to veri...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: glucose, quality of life, weight, body condition, obesity
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
