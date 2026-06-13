---
id: src-fip-027-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-fip-027]
language: zh
last_compiled_at: 2026-06-09
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-fip-027 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-fip-027` |
| Title | Open label clinical trial of orally administered molnupiravir as a first-line treatment for naturally occurring effusive feline infectious peritonitis |
| DOI | `10.1111/jvim.17187` |
| Metadata provider | Crossref |
| Container | Journal of Veterinary Internal Medicine |
| Year | 2024 |
| Current card status | `abstract_weighted` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | original study |
| Population / sample signal | 10 cats |
| Detected section labels | objective, background, animals, methods, results, conclusions |
| Endpoint / theme signals | remission, survival |

Short abstract lead for scope check only:

> Abstract Background Before the discovery of effective antiviral drugs, feline infectious peritonitis (FIP) was a unifor...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: remission, survival
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
