---
id: cancer-fulltext-availability-sample-2-20260530
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

Source set: `feline cancer additional full-text availability sample after blocked candidates, 2026-05-30`

## Rule

This report checks full-text availability signals before deep extraction. It does not download articles, create clinical claims, or promote source-card status.

## Summary

- Cards checked: `2`
- Crossref metadata found: `2`
- With Crossref full-text/TDM links: `2`
- With license metadata: `2`
- With reachable HEAD probes: `1`
- With Crossref abstracts: `2`
- Manual access result: `src-cancer-019` reachable as open HTML; `src-cancer-021` blocked by Cloudflare challenge during this run.
- Promotion result: `src-cancer-019` deep-extracted; `src-cancer-021` remains abstract-weighted / access-blocked.

## Availability Table

| Source | Status | DOI | Abstract | Links | License | Reachable Probe | Recommendation |
|---|---|---|---|---:|---:|---:|---|
| `src-cancer-019` | `abstract_weighted` | `10.1186/1471-2407-13-403` | `yes` | 4 | 1 | 3 | full-text/TDM link present; verify access before deep extraction |
| `src-cancer-021` | `abstract_weighted` | `10.1155/2013/502197` | `yes` | 3 | 1 | 0 | full-text/TDM link present; verify access before deep extraction |

## Link Detail

### `src-cancer-019`

- Title: Feline mammary basal-like adenocarcinomas: a potential model for human triple-negative breast cancer (TNBC) with basal-like subtype
- Container/year: BMC Cancer / 2013
- DOI landing: https://doi.org/10.1186/1471-2407-13-403
- Primary URL: https://bmccancer.biomedcentral.com/articles/10.1186/1471-2407-13-403
- Full-text/TDM links: http://link.springer.com/content/pdf/10.1186/1471-2407-13-403.pdf (application/pdf, text-...; http://link.springer.com/article/10.1186/1471-2407-13-403/fulltext.html (text/html, text-...; +2 more
- License URLs: http://www.springer.com/tdm
- HEAD probes: http://link.springer.com/content/pdf/10.1186/1471-2407-13-403.pdf -> 200 (application/pdf...; http://link.springer.com/article/10.1186/1471-2407-13-403/fulltext.html -> 200 (text/html...; http://link.springer.com/content/pdf/10.1186/1471-2407-13-403 -> 200 (application/pdf, le...
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-cancer-021`

- Title: A Naturally Occurring Feline Model of Head and Neck Squamous Cell Carcinoma
- Container/year: Pathology Research International / 2013
- DOI landing: https://doi.org/10.1155/2013/502197
- Primary URL: https://www.hindawi.com/journals/pri/2013/502197/
- Full-text/TDM links: http://downloads.hindawi.com/archive/2013/502197.pdf (application/pdf, text-mining); http://downloads.hindawi.com/archive/2013/502197.xml (application/xml, text-mining); +1 more
- License URLs: http://creativecommons.org/licenses/by/3.0/
- HEAD probes: http://downloads.hindawi.com/archive/2013/502197.pdf -> HTTP 403; http://downloads.hindawi.com/archive/2013/502197.xml -> HTTP 403; http://downloads.hindawi.com/archive/2013/502197.pdf -> HTTP 403
- Next action: full-text/TDM link present; verify access before deep extraction
