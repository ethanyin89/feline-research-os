---
id: src-diabetes-111-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-diabetes-111]
language: zh
last_compiled_at: 2026-05-14
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-diabetes-111 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref metadata and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-diabetes-111` |
| Title | Treatment of Newly Diagnosed Diabetic Cats with Glargine Insulin Improves Glycaemic Control and Results in Higher Probability of Remission than Protamine Zinc and Lente Insulins |
| DOI | `10.1016/j.jfms.2009.05.016` |
| Container | Journal of Feline Medicine and Surgery |
| Year | 2009 |
| Current card status | `abstract_weighted` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | unclear from abstract metadata |
| Population / sample signal | cats mentioned; count not mechanically extracted |
| Detected section labels | none mechanically detected |
| Endpoint / theme signals | insulin, glucose, remission |

Short abstract lead for scope check only:

> Glycaemic control and remission probabilities were compared in 24 newly diagnosed diabetic cats treated twice daily wit...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: insulin, glucose, remission
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
