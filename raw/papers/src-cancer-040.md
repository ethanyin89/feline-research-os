---
id: src-cancer-040
type: source
title: "Cats with Cancer: Where to start"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2013
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, where, start]
links:
  doi: "10.1177/1098612x13483235"
  url: "https://doi.org/10.1177/1098612x13483235"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Crossref metadata resolves this DOI and reports abstract availability for source scope checking."
    - "Crossref container: Journal of Feline Medicine and Surgery; year: 2013."
    - "The SAGE full article page was readable through the browser layer during the 2026-05-30 deep extraction pass."
  source_supported_conclusion:
    - "This source supports a practical feline oncology workflow shell: presentation, diagnosis, staging, and conditional treatment planning."
    - "It should not control tumor-specific treatment protocols or survival estimates."
  llm_inference:
    - "Use as workflow architecture before branch-specific tumor sources are promoted."
---

# Cats with Cancer: Where to start

## Deep Extraction, 2026-05-30

Worksheet: [src-cancer-040 deep extraction](../../system/indexes/src-cancer-040-deep-extraction-round1.md)

This source was promoted from abstract-weighted triage to deep-extracted after manual full article review. Direct local fetch returned a browser/challenge page, but the SAGE article page was readable through the browser layer.

Safe promoted role:

- general approach-to-feline-cancer workflow
- presentation and differential diagnosis orientation
- diagnosis and sampling boundary source
- staging-before-treatment source
- conditional treatment-modality overview

Do not use this source as:

- tumor-specific treatment protocol
- owner-facing survival estimate
- remote diagnostic rule from signs
- broad chemotherapy/radiotherapy recommendation
- recurrence or prognosis authority without tumor-specific sources

## Source Check, 2026-05-30

Crossref metadata was checked as a repeatable second-pass intake step before deep extraction.

- DOI metadata resolved: yes
- Container: Journal of Feline Medicine and Surgery
- Year: 2013
- Abstract available in Crossref: yes
- Full text manually verified: yes, SAGE browser-readable full article
- Extraction status: deep-extracted

## One-Line Summary

Deep-extracted practitioner workflow source for approaching cats with suspected or confirmed cancer, with diagnosis/staging gates before treatment discussion.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow. Full article review confirms its strongest role is practical workflow architecture, not disease-specific evidence grading.

The safe current use is workflow architecture:

- explain why suspected cancer needs veterinary diagnosis
- separate presentation, diagnosis, staging, and treatment planning
- list common tumor families as orientation only
- keep treatment claims conditional on tumor type, stage, feasibility, and patient/owner constraints

## Key Findings

### quoted_fact

- The intake sheet lists this title: Cats with Cancer: Where to start.
- The intake sheet locator is: 10.1177/1098612x13483235.
- The article is aimed at veterinary practitioners.
- The article sections include clinical signs, diagnosis, clinical staging, and treatment options and considerations.
- The article explicitly frames the evidence base for many feline tumours as limited.

### source_supported_conclusion

- The cancer module should start with workflow: presentation -> diagnosis -> staging -> branch-specific treatment planning.
- Cytology and biopsy should be represented as different sampling tools with different limits.
- Treatment modality summaries must remain conditional rather than ranked globally.

### llm_inference

- Use this source as a general navigation and safety source, then require tumor-specific sources before claims about prognosis or treatment.

## Claim-Fit Judgment

Strongest safe use:

- suspected-cancer workflow
- diagnosis and sampling boundaries
- staging gate before treatment
- conditional treatment-modality overview

Must not control yet:

- reader-facing medical advice
- tumor-specific protocols
- survival estimates
- treatment ranking
- chemotherapy/radiotherapy recommendations outside branch-specific evidence
- recurrence/prognosis claims

## Image Asset TODO

- figures to capture: common tumor table and selected clinical images may be useful for internal branch mapping
- why these matter: diagnostic and tumor-family visuals require careful permissions and reader-safety framing

## Open Follow-Up Questions

- Should the first reader-facing cancer page be a suspected-cancer workflow rather than a tumor-family page?
- Which tumor-specific sources should control lymphoma, oral SCC, mammary carcinoma, and soft tissue sarcoma branches?
- How should diagnosis and staging gates be represented in navigation?
- Which clinical signs can be safely listed without causing remote diagnosis?

## Linked Entities

- diseases: cancer
- models:
- endpoints: diagnosis, staging, treatment-planning, clinical-workflow
- mechanisms:
- regulations:
