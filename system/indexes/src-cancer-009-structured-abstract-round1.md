---
id: src-cancer-009-structured-abstract-round1
type: system
topic: content-pipeline
question_type: structured-abstract-extraction
source_ids: [src-cancer-009]
language: zh
last_compiled_at: 2026-05-30
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-cancer-009 Structured Abstract Extraction, Round 1

## Evidence Boundary

This worksheet uses Crossref metadata and available abstract text only. It is not a full-text read, not a deep extraction, and not a permission to promote reader-facing clinical claims.

## Source Metadata

| Field | Value |
|---|---|
| Source | `src-cancer-009` |
| Title | Metastatic feline mammary cancer: prognostic factors, outcome and comparison of different treatment modalities – a retrospective multicentre study |
| DOI | `10.1177/1098612x20964416` |
| Container | Journal of Feline Medicine and Surgery |
| Year | 2021 |
| Current card status | `abstract_weighted` |

## Mechanical Abstract Signals

| Signal | Read |
|---|---|
| Source family | review |
| Population / sample signal | 73 cats |
| Detected section labels | methods, results, conclusions |
| Endpoint / theme signals | survival, pathology |

Short abstract lead for scope check only:

> Objectives Although feline mammary carcinomas (FMCs) are highly metastatic, the literature and treatment options pertai...

## Safe Reuse From This Worksheet

- Use this source for extraction priority and branch placement.
- Use the mechanical signals above to decide which high-level queue the source belongs in.
- Do not use this worksheet for numeric effect sizes, protocol selection, prevalence values, risk ranking, or owner-facing advice.

## Provisional Claim-Fit

- Branch fit: survival, pathology
- Best next action: structured full abstract review or full-text deep extraction if this source controls a branch.
- Promotion status: hold; no topic-page write-back from this worksheet alone.

## Open Questions Before Promotion

- Does the full abstract or article body support the implied branch role?
- Are species, population, endpoint, and intervention boundaries narrower than the title suggests?
- Are there numeric results, tables, or safety criteria that require full-text verification?
- Does this source duplicate an existing deep-extracted source or add a genuinely new branch?
