---
id: src-obesity-071-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-obesity-071]
language: zh
last_compiled_at: 2026-06-06
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-obesity-071 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref metadata and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-obesity-071` |
| Title | Kidney function and glucose metabolism in overweight and obese cats |
| DOI | `10.1080/01652176.2020.1759844` |
| Container | Veterinary Quarterly |
| Year | 2020 |
| Current card status | `title_only` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | original study |
| Population / sample signal | cats mentioned; count not mechanically extracted |
| Detected section labels | background, methods, results, clinical relevance |
| Endpoint / theme signals | glucose, weight, obesity, overweight, chronic kidney disease |

Short abstract lead for scope check only:

> Background: In people, obesity and prediabetes mellitus might predispose to chronic kidney disease (CKD).Aims: To asses...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: glucose, weight, obesity, overweight, chronic kidney disease
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
