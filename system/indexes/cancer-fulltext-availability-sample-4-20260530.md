---
id: cancer-fulltext-availability-sample-4-20260530
type: system
topic: content-pipeline
question_type: fulltext-availability-check
language: zh
last_compiled_at: 2026-05-30
verification_status: generated
decision_grade: no
owner: codex
status: active
---

# Feline Full-Text Availability Check, 2026-05-30

Source set: `feline cancer branch-control availability sample 4, lymphoma and oral SCC, 2026-05-30`

## Rule

This report checks full-text availability signals before deep extraction. It does not download articles, create clinical claims, or promote source-card status.

## Summary

- Cards checked: `2`
- Crossref metadata found: `2`
- With Crossref full-text/TDM links: `2`
- With license metadata: `2`
- With reachable HEAD probes: `0`
- With Crossref abstracts: `2`
- Manual access result: `src-cancer-008` local direct fetch returned HTTP 403 but the SAGE PDF was browser-readable; `src-cancer-046` SAGE page exposed abstract/references but not readable full text during this run.
- Promotion result: `src-cancer-008` deep-extracted; `src-cancer-046` remains abstract-weighted / full-text blocked.

## Availability Table

| Source | Status | DOI | Abstract | Links | License | Reachable Probe | Recommendation |
|---|---|---|---|---:|---:|---:|---|
| `src-cancer-008` | `abstract_weighted` | `10.1177/104063870001200401` | `yes` | 2 | 1 | 0 | full-text/TDM link present; verify access before deep extraction |
| `src-cancer-046` | `abstract_weighted` | `10.1177/089875641503200104` | `yes` | 2 | 1 | 0 | full-text/TDM link present; verify access before deep extraction |

## Link Detail

### `src-cancer-008`

- Title: The Histologic Classification of 602 Cases of Feline Lymphoproliferative Disease using the National Cancer Institute Working Formulation
- Container/year: Journal of Veterinary Diagnostic Investigation / 2000
- DOI landing: https://doi.org/10.1177/104063870001200401
- Primary URL: https://journals.sagepub.com/doi/10.1177/104063870001200401
- Full-text/TDM links: https://journals.sagepub.com/doi/pdf/10.1177/104063870001200401 (application/pdf, text-mi...; https://journals.sagepub.com/doi/pdf/10.1177/104063870001200401 (unspecified, similarity-...
- License URLs: https://journals.sagepub.com/page/policies/text-and-data-mining-license
- HEAD probes: https://journals.sagepub.com/doi/pdf/10.1177/104063870001200401 -> HTTP 403; https://journals.sagepub.com/doi/pdf/10.1177/104063870001200401 -> HTTP 403
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-cancer-046`

- Title: Feline Oral Squamous Cell Carcinoma: Clinical Manifestations and Literature Review
- Container/year: Journal of Veterinary Dentistry / 2015
- DOI landing: https://doi.org/10.1177/089875641503200104
- Primary URL: https://journals.sagepub.com/doi/10.1177/089875641503200104
- Full-text/TDM links: https://journals.sagepub.com/doi/pdf/10.1177/089875641503200104 (application/pdf, text-mi...; https://journals.sagepub.com/doi/pdf/10.1177/089875641503200104 (unspecified, similarity-...
- License URLs: https://journals.sagepub.com/page/policies/text-and-data-mining-license
- HEAD probes: https://journals.sagepub.com/doi/pdf/10.1177/089875641503200104 -> HTTP 403; https://journals.sagepub.com/doi/pdf/10.1177/089875641503200104 -> HTTP 403
- Next action: full-text/TDM link present; verify access before deep extraction
