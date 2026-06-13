---
id: src-ckd-025-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-ckd-025]
language: zh
last_compiled_at: 2026-06-05
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-ckd-025 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref metadata and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-ckd-025` |
| Title | Resistivity and pulsatility indexes in feline kidney disease: a systematic review |
| DOI | `10.1111/vru.13102` |
| Container | Veterinary Radiology &amp; Ultrasound |
| Year | 2022 |
| Current card status | `abstract_weighted` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | review |
| Population / sample signal | cats mentioned; count not mechanically extracted |
| Detected section labels | animals, methods |
| Endpoint / theme signals | weight, ultrasonography |

Short abstract lead for scope check only:

> Abstract Doppler ultrasonography is used in the evaluation of hemodynamics, and the resistivity (RI) and pulsatility (P...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: weight, ultrasonography
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
