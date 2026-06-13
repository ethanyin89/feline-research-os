---
id: src-ckd-039-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-ckd-039]
language: zh
last_compiled_at: 2026-06-06
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-ckd-039 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref + PubMed abstract and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-ckd-039` |
| Title | Changes in Renal Peritubular Capillaries in Canine and Feline Chronic Kidney Disease |
| DOI | `10.1016/j.jcpa.2018.03.004` |
| Metadata provider | Crossref + PubMed abstract |
| Container | Journal of Comparative Pathology |
| Year | 2018 |
| Current card status | `abstract_weighted` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | original study |
| Population / sample signal | cats mentioned; count not mechanically extracted |
| Detected section labels | none mechanically detected |
| Endpoint / theme signals | chronic kidney disease |

Short abstract lead for scope check only:

> Renal capillary rarefaction is a crucial event that leads to tubulointerstitial damage during the progression of chroni...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: chronic kidney disease
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
