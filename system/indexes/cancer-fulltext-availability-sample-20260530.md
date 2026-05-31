---
id: cancer-fulltext-availability-sample-20260530
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

Source set: `feline cancer full-text availability sample, 2026-05-30`

## Rule

This report checks full-text availability signals before deep extraction. It does not download articles, create clinical claims, or promote source-card status.

## Summary

- Cards checked: `6`
- Crossref metadata found: `6`
- With Crossref full-text/TDM links: `6`
- With license metadata: `6`
- With reachable HEAD probes: `1`
- With Crossref abstracts: `6`

## Availability Table

| Source | Status | DOI | Abstract | Links | License | Reachable Probe | Recommendation |
|---|---|---|---|---:|---:|---:|---|
| `src-cancer-004` | `abstract_weighted` | `10.21926/obm.genet.2102131` | `yes` | 2 | 1 | 1 | full-text/TDM link present; verify access before deep extraction |
| `src-cancer-005` | `abstract_weighted` | `10.3390/vetsci2030111` | `yes` | 1 | 1 | 0 | full-text/TDM link present; verify access before deep extraction |
| `src-cancer-008` | `abstract_weighted` | `10.1177/104063870001200401` | `yes` | 2 | 1 | 0 | full-text/TDM link present; verify access before deep extraction |
| `src-cancer-009` | `abstract_weighted` | `10.1177/1098612x20964416` | `yes` | 3 | 1 | 0 | full-text/TDM link present; verify access before deep extraction |
| `src-cancer-025` | `abstract_weighted` | `10.1177/0300985814528221` | `yes` | 3 | 1 | 0 | full-text/TDM link present; verify access before deep extraction |
| `src-cancer-046` | `abstract_weighted` | `10.1177/089875641503200104` | `yes` | 2 | 1 | 0 | full-text/TDM link present; verify access before deep extraction |

## Link Detail

### `src-cancer-004`

- Title: Molecular Mechanisms of Feline Cancers
- Container/year: OBM Genetics / 2021
- DOI landing: https://doi.org/10.21926/obm.genet.2102131
- Primary URL: https://www.lidsen.com/journals/genetics/genetics-05-02-131
- Full-text/TDM links: https://www.lidsen.com/journals/genetics/genetics-05-02-131/obm.genet.2102131.xml (text/x...; https://www.lidsen.com/journals/genetics/genetics-05-02-131 (unspecified, similarity-chec...
- License URLs: https://creativecommons.org/licenses/by/4.0/
- HEAD probes: https://www.lidsen.com/journals/genetics/genetics-05-02-131/obm.genet.2102131.xml -> HTTP...; https://www.lidsen.com/journals/genetics/genetics-05-02-131 -> 200 (text/html; charset=ut...
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-cancer-005`

- Title: Cats, Cancer and Comparative Oncology
- Container/year: Veterinary Sciences / 2015
- DOI landing: https://doi.org/10.3390/vetsci2030111
- Primary URL: https://www.mdpi.com/2306-7381/2/3/111
- Full-text/TDM links: https://www.mdpi.com/2306-7381/2/3/111/pdf (unspecified, similarity-checking)
- License URLs: https://creativecommons.org/licenses/by/4.0/
- HEAD probes: https://www.mdpi.com/2306-7381/2/3/111/pdf -> HTTP 403
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-cancer-008`

- Title: The Histologic Classification of 602 Cases of Feline Lymphoproliferative Disease using the National Cancer Institute Working Formulation
- Container/year: Journal of Veterinary Diagnostic Investigation / 2000
- DOI landing: https://doi.org/10.1177/104063870001200401
- Primary URL: https://journals.sagepub.com/doi/10.1177/104063870001200401
- Full-text/TDM links: https://journals.sagepub.com/doi/pdf/10.1177/104063870001200401 (application/pdf, text-mi...; https://journals.sagepub.com/doi/pdf/10.1177/104063870001200401 (unspecified, similarity-...
- License URLs: https://journals.sagepub.com/page/policies/text-and-data-mining-license
- HEAD probes: https://journals.sagepub.com/doi/pdf/10.1177/104063870001200401 -> HTTP 403; https://journals.sagepub.com/doi/pdf/10.1177/104063870001200401 -> HTTP 403
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-cancer-009`

- Title: Metastatic feline mammary cancer: prognostic factors, outcome and comparison of different treatment modalities – a retrospective multicentre study
- Container/year: Journal of Feline Medicine and Surgery / 2021
- DOI landing: https://doi.org/10.1177/1098612x20964416
- Primary URL: https://journals.sagepub.com/doi/10.1177/1098612X20964416
- Full-text/TDM links: https://journals.sagepub.com/doi/pdf/10.1177/1098612X20964416 (application/pdf, text-mini...; https://journals.sagepub.com/doi/full-xml/10.1177/1098612X20964416 (application/xml, text...; +1 more
- License URLs: https://journals.sagepub.com/page/policies/text-and-data-mining-license
- HEAD probes: https://journals.sagepub.com/doi/pdf/10.1177/1098612X20964416 -> HTTP 403; https://journals.sagepub.com/doi/full-xml/10.1177/1098612X20964416 -> HTTP 403
- Next action: full-text/TDM link present; verify access before deep extraction

### `src-cancer-025`

- Title: Prognostic Evaluation of Feline Mammary Carcinomas
- Container/year: Veterinary Pathology / 2015
- DOI landing: https://doi.org/10.1177/0300985814528221
- Primary URL: https://journals.sagepub.com/doi/10.1177/0300985814528221
- Full-text/TDM links: https://journals.sagepub.com/doi/pdf/10.1177/0300985814528221 (application/pdf, text-mini...; https://journals.sagepub.com/doi/full-xml/10.1177/0300985814528221 (application/xml, text...; +1 more
- License URLs: https://journals.sagepub.com/page/policies/text-and-data-mining-license
- HEAD probes: https://journals.sagepub.com/doi/pdf/10.1177/0300985814528221 -> HTTP 403; https://journals.sagepub.com/doi/full-xml/10.1177/0300985814528221 -> HTTP 403
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
