---
id: src-obesity-018-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-obesity-018]
language: zh
last_compiled_at: 2026-06-09
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-obesity-018 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses PubMed and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-obesity-018` |
| Title | Effectiveness of feline body mass index (fBMI) as new diagnostic tool for obesity. |
| DOI | `not available` |
| Metadata provider | PubMed |
| Container | The Japanese journal of veterinary research |
| Year | 2016 |
| Current card status | `title_only` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | unclear from abstract metadata |
| Population / sample signal | 6 cats |
| Detected section labels | none mechanically detected |
| Endpoint / theme signals | effectiveness, obesity |

Short abstract lead for scope check only:

> Feline body mass index (fBMI), BW/PCL, length from top of patella to end of calcaneus, was developed as a new diagnosti...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: effectiveness, obesity
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
