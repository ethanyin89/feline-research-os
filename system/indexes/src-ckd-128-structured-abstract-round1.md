---
id: src-ckd-128-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-ckd-128]
language: zh
last_compiled_at: 2026-06-13
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-ckd-128 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref + PubMed abstract and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-ckd-128` |
| Title | Urinary Fibroblast Growth Factor-23 and Soluble Alpha-Klotho in Cats with Chronic Kidney Disease |
| DOI | `10.1016/j.tvjl.2026.106652` |
| Metadata provider | Crossref + PubMed abstract |
| Container | The Veterinary Journal |
| Year | 2026 |
| Current card status | `title_only` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | original study |
| Population / sample signal | cats mentioned; count not mechanically extracted |
| Detected section labels | results |
| Endpoint / theme signals | biomarker, chronic kidney disease, fibroblast growth factor 23, phosphorus |

Short abstract lead for scope check only:

> Fibroblast growth factor 23 (FGF23) and α-Klotho play crucial roles in the pathogenesis of chronic kidney disease-miner...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: biomarker, chronic kidney disease, fibroblast growth factor 23, phosphorus
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
