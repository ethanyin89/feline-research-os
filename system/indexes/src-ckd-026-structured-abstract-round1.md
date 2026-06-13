---
id: src-ckd-026-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-ckd-026]
language: zh
last_compiled_at: 2026-06-05
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-ckd-026 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref metadata and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-ckd-026` |
| Title | Serum fibroblast growth factor 23 (FGF-23): associations with hyperphosphatemia and clinical staging of feline chronic kidney disease |
| DOI | `10.1177/1040638720985563` |
| Container | Journal of Veterinary Diagnostic Investigation |
| Year | 2021 |
| Current card status | `abstract_weighted` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | unclear from abstract metadata |
| Population / sample signal | 304 cats |
| Detected section labels | none mechanically detected |
| Endpoint / theme signals | biomarker, chronic kidney disease, fibroblast growth factor 23, fgf-23, hyperphosphatemia, phosphate, phosphorus, staging |

Short abstract lead for scope check only:

> Fibroblast growth factor 23 (FGF-23) is an independent monitor of the progression of chronic kidney disease (CKD) in hu...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: biomarker, chronic kidney disease, fibroblast growth factor 23, fgf-23, hyperphosphatemia
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
