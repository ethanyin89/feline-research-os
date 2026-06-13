---
id: src-ckd-165-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-ckd-165]
language: zh
last_compiled_at: 2026-06-13
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-ckd-165 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref + PubMed abstract and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-ckd-165` |
| Title | Kidney and cystic volume imaging for disease presentation and progression in the cat autosomal dominant polycystic kidney disease large animal model |
| DOI | `10.1186/s12882-019-1448-1` |
| Metadata provider | Crossref + PubMed abstract |
| Container | BMC Nephrology |
| Year | 2019 |
| Current card status | `title_only` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | unclear from abstract metadata |
| Population / sample signal | cats mentioned; count not mechanically extracted |
| Detected section labels | background, methods, results, conclusions |
| Endpoint / theme signals | biomarker, chronic kidney disease, glomerular filtration rate, ultrasonography |

Short abstract lead for scope check only:

> BACKGROUND: Approximately 30% of Persian cats have a c.10063C > A variant in polycystin 1 (PKD1) homolog causing autoso...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: biomarker, chronic kidney disease, glomerular filtration rate, ultrasonography
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
