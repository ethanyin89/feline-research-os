---
id: src-ckd-131-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-ckd-131]
language: zh
last_compiled_at: 2026-06-13
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-ckd-131 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref + PubMed abstract and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-ckd-131` |
| Title | Absence of renal cortical anisotropic backscattering artifact in feline chronic kidney disease |
| DOI | `10.1080/01652176.2021.1941397` |
| Metadata provider | Crossref + PubMed abstract |
| Container | Veterinary Quarterly |
| Year | 2021 |
| Current card status | `title_only` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | original study |
| Population / sample signal | 40 cats |
| Detected section labels | none mechanically detected |
| Endpoint / theme signals | chronic kidney disease |

Short abstract lead for scope check only:

> Renal cortical anisotropy backscattering artifact (CABA) is a focal hyperechoic region where the tubules are parallel t...

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
