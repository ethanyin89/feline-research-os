---
id: feline-ckd-priority-fulltext-availability-20260606
type: system
topic: content-pipeline
question_type: fulltext-availability-check
language: zh
last_compiled_at: 2026-06-06
verification_status: generated
decision_grade: no
owner: codex
status: active
---

# Feline Full-Text Availability Check, 2026-06-06

Source set: `CKD priority deep-extraction candidates 2026-06-06`

## Rule

This report checks full-text availability signals before deep extraction. It does not download articles, create clinical claims, or promote source-card status.

## Summary

- Cards checked: `4`
- Crossref metadata found: `0`
- With Crossref full-text/TDM links: `0`
- With license metadata: `0`
- With reachable HEAD probes: `0`
- With Crossref abstracts: `0`

Crossref requests repeatedly reset during this run. Direct primary-source verification was therefore performed afterward:

- `src-ckd-027`: complete PMC article available, PMCID `PMC11703532`.
- `src-ckd-029`: complete article PDF verified and reviewed.
- `src-ckd-047`: RVC repository advertises an open author manuscript, but direct access was blocked by a Cloudflare challenge in this environment.
- `src-ckd-049`: publisher and PubMed routes exposed an abstract only.

## Availability Table

| Source | Status | DOI | Abstract | Links | License | Reachable Probe | Recommendation |
|---|---|---|---|---:|---:|---:|---|
| `src-ckd-027` | `abstract_weighted` | `10.1080/01652176.2024.2447601` | `no` | 0 | 0 | 0 | metadata failed; manual lookup required |
| `src-ckd-029` | `abstract_weighted` | `10.1007/s11259-018-9719-z` | `no` | 0 | 0 | 0 | metadata failed; manual lookup required |
| `src-ckd-047` | `abstract_weighted` | `10.1016/j.cvsm.2016.06.002` | `no` | 0 | 0 | 0 | metadata failed; manual lookup required |
| `src-ckd-049` | `abstract_weighted` | `10.1016/j.cvsm.2016.06.014` | `no` | 0 | 0 | 0 | metadata failed; manual lookup required |

## Manual Resolution

| Source | Direct result | Extraction decision |
|---|---|---|
| `src-ckd-027` | Complete PMC article text | Deep extraction completed. |
| `src-ckd-029` | Complete 8-page article PDF | Deep extraction completed. |
| `src-ckd-047` | Open-manuscript lead, access challenge | Hold at `abstract_weighted`. |
| `src-ckd-049` | Abstract only | Hold at `abstract_weighted`. |

## Link Detail

### `src-ckd-027`

- Error: <urlopen error [Errno 54] Connection reset by peer>

- Title: Metabolomics reveals alterations in gut-derived uremic toxins and tryptophan metabolism in feline chronic kidney disease
- Container/year:  / 
- DOI landing: 
- Primary URL: 
- Full-text/TDM links: none in Crossref metadata
- License URLs: none in Crossref metadata
- HEAD probes: not run
- Next action: metadata failed; manual lookup required

### `src-ckd-029`

- Error: <urlopen error [Errno 54] Connection reset by peer>

- Title: A long term feed supplementation based on phosphate binders in Feline Chronic Kidney Disease
- Container/year:  / 
- DOI landing: 
- Primary URL: 
- Full-text/TDM links: none in Crossref metadata
- License URLs: none in Crossref metadata
- HEAD probes: not run
- Next action: metadata failed; manual lookup required

### `src-ckd-047`

- Error: <urlopen error [Errno 54] Connection reset by peer>

- Title: Current Understanding of the Pathogenesis of Progressive Chronic Kidney Disease in Cats
- Container/year:  / 
- DOI landing: 
- Primary URL: 
- Full-text/TDM links: none in Crossref metadata
- License URLs: none in Crossref metadata
- HEAD probes: not run
- Next action: metadata failed; manual lookup required

### `src-ckd-049`

- Error: <urlopen error [Errno 54] Connection reset by peer>

- Title: Utilization of Feeding Tubes in the Management of Feline Chronic Kidney Disease
- Container/year:  / 
- DOI landing: 
- Primary URL: 
- Full-text/TDM links: none in Crossref metadata
- License URLs: none in Crossref metadata
- HEAD probes: not run
- Next action: metadata failed; manual lookup required
