---
id: cancer-fulltext-availability-sample-3-20260530
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

Source set: `feline cancer full-text availability sample 3 after deep extraction`

## Rule

This report checks full-text availability signals before deep extraction. It does not download articles, create clinical claims, or promote source-card status.

## Summary

- Cards checked: `2`
- Crossref metadata found: `2`
- With Crossref full-text/TDM links: `2`
- With license metadata: `2`
- With reachable HEAD probes: `0`
- With Crossref abstracts: `2`
- Manual access result: `src-cancer-003` reachable through Europe PMC full-text XML (`PMC8294401`); `src-cancer-040` local direct fetch returned browser/challenge pages, but the SAGE full article page was readable through the browser layer.
- Promotion result: `src-cancer-003` and `src-cancer-040` deep-extracted.

## Availability Table

| Source | Status | DOI | Abstract | Links | License | Reachable Probe | Recommendation |
|---|---|---|---|---:|---:|---:|---|
| `src-cancer-003` | `abstract_weighted` | `10.1002/vms3.460` | `yes` | 3 | 1 | 0 | full-text/TDM link present; verify access before deep extraction |
| `src-cancer-040` | `abstract_weighted` | `10.1177/1098612x13483235` | `yes` | 3 | 1 | 0 | full-text/TDM link present; verify access before deep extraction |

## Link Detail

### `src-cancer-003`

- Title: The role of COX expression in the prognostication of overall survival of canine and feline cancer: A systematic review
- Container/year: Veterinary Medicine and Science / 2021
- DOI landing: https://doi.org/10.1002/vms3.460
- Primary URL: https://onlinelibrary.wiley.com/doi/10.1002/vms3.460
- Full-text/TDM links: https://onlinelibrary.wiley.com/doi/pdf/10.1002/vms3.460 (application/pdf, text-mining); https://onlinelibrary.wiley.com/doi/full-xml/10.1002/vms3.460 (application/xml, text-mini...; +1 more
- License URLs: http://creativecommons.org/licenses/by-nc-nd/4.0/
- HEAD probes: https://onlinelibrary.wiley.com/doi/pdf/10.1002/vms3.460 -> HTTP 403; https://onlinelibrary.wiley.com/doi/full-xml/10.1002/vms3.460 -> HTTP 403; https://onlinelibrary.wiley.com/doi/pdf/10.1002/vms3.460 -> HTTP 403
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-cancer-040`

- Title: Cats with Cancer
- Container/year: Journal of Feline Medicine and Surgery / 2013
- DOI landing: https://doi.org/10.1177/1098612x13483235
- Primary URL: https://journals.sagepub.com/doi/10.1177/1098612X13483235
- Full-text/TDM links: https://journals.sagepub.com/doi/pdf/10.1177/1098612X13483235 (application/pdf, text-mini...; https://journals.sagepub.com/doi/full-xml/10.1177/1098612X13483235 (application/xml, text...; +1 more
- License URLs: https://journals.sagepub.com/page/policies/text-and-data-mining-license
- HEAD probes: https://journals.sagepub.com/doi/pdf/10.1177/1098612X13483235 -> HTTP 403; https://journals.sagepub.com/doi/full-xml/10.1177/1098612X13483235 -> HTTP 403; https://journals.sagepub.com/doi/pdf/10.1177/1098612X13483235 -> HTTP 403
- Next action: full-text/TDM link present; verify access before deep extraction
