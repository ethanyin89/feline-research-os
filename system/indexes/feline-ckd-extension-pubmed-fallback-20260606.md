---
id: feline-ckd-extension-pubmed-fallback-20260606
type: system
topic: content-pipeline
question_type: source-check-report
language: zh
last_compiled_at: 2026-06-06
verification_status: generated
decision_grade: no
owner: codex
status: active
---

# Feline Source Metadata Check, 2026-06-06

Source set: `CKD extension PubMed fallback completion 2026-06-06`

## Rule

This report is a repeatable second-pass source check. It does not make clinical claims.

- DOI metadata alone does not upgrade a card.
- Abstract availability can justify `abstract_weighted` only for navigation and extraction priority.
- Full-text or structured worksheet review is still required before `source_checked` or `deep_extracted`.

## Summary

- Cards checked: `7`
- Metadata found: `7`
- Abstract available: `6`

## Check Table

| Source | Current | Recommended | Provider | DOI | Year | Container | Abstract | Error |
|---|---|---|---|---|---:|---|---|---|
| `src-ckd-027` | `title_only` | `abstract_weighted` | Crossref + PubMed abstract | `10.1080/01652176.2024.2447601` | 2025 | Veterinary Quarterly | `yes` |  |
| `src-ckd-029` | `title_only` | `abstract_weighted` | Crossref + PubMed abstract | `10.1007/s11259-018-9719-z` | 2018 | Veterinary Research Communications | `yes` |  |
| `src-ckd-032` | `title_only` | `title_only` | PubMed |  | 2014 | Journal of the American Veterinary Medical Association | `no` |  |
| `src-ckd-039` | `title_only` | `abstract_weighted` | Crossref + PubMed abstract | `10.1016/j.jcpa.2018.03.004` | 2018 | Journal of Comparative Pathology | `yes` |  |
| `src-ckd-044` | `title_only` | `abstract_weighted` | Crossref + PubMed abstract | `10.1016/j.tvjl.2019.105358` | 2019 | The Veterinary Journal | `yes` |  |
| `src-ckd-047` | `title_only` | `abstract_weighted` | Crossref + PubMed abstract | `10.1016/j.cvsm.2016.06.002` | 2016 | Veterinary Clinics of North America: Small Animal Practice | `yes` |  |
| `src-ckd-049` | `title_only` | `abstract_weighted` | Crossref + PubMed abstract | `10.1016/j.cvsm.2016.06.014` | 2016 | Veterinary Clinics of North America: Small Animal Practice | `yes` |  |

## Abstract Availability Notes

### `src-ckd-027`

- Metadata provider: Crossref + PubMed abstract
- Resolved title: Metabolomics reveals alterations in gut-derived uremic toxins and tryptophan metabolism in feline chronic kidney disease
- Abstract lead for scope check only: Chronic Kidney Disease (CKD) is one of the most common conditions affecting felines, yet the metabolic alterations underlying its pathophysiology remain poorly understood, hinderi...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-ckd-029`

- Metadata provider: Crossref + PubMed abstract
- Resolved title: A long term feed supplementation based on phosphate binders in Feline Chronic Kidney Disease
- Abstract lead for scope check only: Chronic kidney disease (CKD) is a very common disorder in elderly cats. A proper renal diet represents the most efficient therapeutic intervention to improve survival and life qua...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-ckd-032`

- PubMed metadata resolved, but no abstract was available.
- Keep the card at its current status until abstract or full text is read.

### `src-ckd-039`

- Metadata provider: Crossref + PubMed abstract
- Resolved title: Changes in Renal Peritubular Capillaries in Canine and Feline Chronic Kidney Disease
- Abstract lead for scope check only: Renal capillary rarefaction is a crucial event that leads to tubulointerstitial damage during the progression of chronic kidney disease (CKD). In the present study, changes in CD3...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-ckd-044`

- Metadata provider: Crossref + PubMed abstract
- Resolved title: Serum concentration of homocysteine in spontaneous feline chronic kidney disease
- Abstract lead for scope check only: Serum homocysteine (Hcy) increases in people and dogs with chronic kidney disease (CKD). Hyperhomocysteinemia (HHcy) has also been associated with CKD-related hypertension and pro...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-ckd-047`

- Metadata provider: Crossref + PubMed abstract
- Resolved title: Current Understanding of the Pathogenesis of Progressive Chronic Kidney Disease in Cats
- Abstract lead for scope check only: In cats with chronic kidney disease (CKD), the most common histopathologic finding is tubulointerstitial inflammation and fibrosis. However, these changes reflect a nonspecific re...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-ckd-049`

- Metadata provider: Crossref + PubMed abstract
- Resolved title: Utilization of Feeding Tubes in the Management of Feline Chronic Kidney Disease
- Abstract lead for scope check only: Esophagostomy feeding tubes are useful, and in many cases essential, for the comprehensive management of cats with moderate to advanced chronic kidney disease (CKD). They should b...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.
