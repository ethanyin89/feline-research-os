---
id: src-cancer-003
type: source
title: "The role of COX expression in the prognostication of overall survival of canine and feline cancer: A systematic review"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: [overall-survival, COX, immunohistochemistry, prognosis]
jurisdictions: []
evidence_level: review
year: 2021
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, role, cox, expression, prognostication, overall, survival, systematic]
links:
  doi: "10.1002/vms3.460"
  url: "https://doi.org/10.1002/vms3.460"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Crossref metadata resolves this DOI and reports abstract availability for source scope checking."
    - "Crossref container: Veterinary Medicine and Science; year: 2021."
    - "Europe PMC full-text XML for PMC8294401 was accessible during the 2026-05-30 deep extraction pass."
  source_supported_conclusion:
    - "This source supports a COX/prognosis-marker layer for feline mammary carcinoma and feline oral SCC."
    - "It supports branch and marker caveats, but not treatment recommendations or owner-facing survival prediction."
  llm_inference:
    - "Mixed-species review conclusions require feline-only filtering before topic-page promotion."
---

# The role of COX expression in the prognostication of overall survival of canine and feline cancer: A systematic review

## Deep Extraction, 2026-05-30

Worksheet: [src-cancer-003 deep extraction](../../system/indexes/src-cancer-003-deep-extraction-round1.md)

This source was promoted from abstract-weighted triage to deep-extracted after full-text XML review through Europe PMC (`PMC8294401`). Wiley and direct PMC pages returned browser/challenge pages during this run, so Europe PMC was used as the accessible full-text route.

Safe promoted role:

- COX/prognosis-marker architecture for the cancer module
- feline mammary carcinoma COX-2 evidence caveat
- feline oral SCC COX-1 distribution-pattern caveat
- method-standardization warning for immunohistochemistry scoring and cutoffs

Do not use this source as:

- COX inhibitor treatment guidance
- owner-facing survival prediction
- a universal feline cancer biomarker rule
- a feline TCC prognostic rule
- support for COX-2 as an oral SCC prognostic marker

## Source Check, 2026-05-30

Crossref metadata was checked as a repeatable second-pass intake step before deep extraction.

- DOI metadata resolved: yes
- Container: Veterinary Medicine and Science
- Year: 2021
- Abstract available in Crossref: yes
- Full text manually verified: yes, Europe PMC XML
- Extraction status: deep-extracted

## One-Line Summary

Deep-extracted systematic review supporting a COX prognosis-marker layer, with feline reuse limited mainly to mammary carcinoma COX-2 and oral SCC COX-1 distribution-pattern caveats.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow. Full-text review confirms its role as a prognosis-marker source rather than a treatment-control source.

The safe current use is controlled marker evidence:

- define a COX/prognosis-marker layer
- filter mixed canine/feline conclusions before feline topic reuse
- preserve method caveats around immunohistochemistry scoring and cutoffs
- prevent COX inhibitor treatment claims from being inferred from prognostic-marker evidence

## Key Findings

### quoted_fact

- The intake sheet lists this title: The role of COX expression in the prognostication of overall survival of canine and feline cancer: A systematic review.
- The intake sheet locator is: 10.1002/vms3.460.
- The systematic review included 18 studies.
- The included evidence totaled 688 dogs and 145 cats.
- Four included studies involved cats.
- Feline-relevant tumour categories included mammary tumours, transitional cell carcinoma, and oral squamous cell carcinoma.

### source_supported_conclusion

- COX-2 can be carried as a feline mammary carcinoma prognosis-marker candidate with evidence-strength caveats.
- COX-1 distribution pattern, not COX-2, is the feline oral SCC marker signal in this review.
- COX quantification heterogeneity and immunohistochemistry subjectivity are core boundaries before any reader-facing claim.

### llm_inference

- Use this source as a cross-branch marker caution page, not as a treatment or prognosis calculator.
- Feline TCC content should remain low-confidence because the reviewed cat TCC study was too small for firm conclusions.

## Claim-Fit Judgment

Strongest safe use:

- prognosis-marker architecture
- mammary carcinoma COX-2 caveat
- oral SCC COX-1 caveat
- method-standardization warning

Must not control yet:

- reader-facing medical advice
- COX inhibitor recommendations
- survival prediction
- universal biomarker ranking
- guideline-like recommendations
- feline TCC prognostic claims

## Image Asset TODO

- figures to capture: PRISMA flow diagram and selected-study table may be useful for internal evidence review
- why these matter: they explain the evidence base and bias profile, but table reuse needs source/license review

## Open Follow-Up Questions

- Which mammary carcinoma branch sources should triangulate the COX-2 evidence?
- Should the oral SCC branch prioritize the Hayes et al. 2007 source for direct extraction?
- How should the module represent biomarker candidates without implying clinical decision rules?
- Is a separate prognosis-marker index warranted after more deep extractions?

## Linked Entities

- diseases: cancer
- models:
- endpoints: overall survival, prognosis, immunohistochemistry, COX scoring
- mechanisms: COX-1, COX-2, prostaglandin pathway, biomarker quantification
- regulations:
