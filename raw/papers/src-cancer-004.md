---
id: src-cancer-004
type: source
title: "Molecular Mechanisms of Feline Cancers"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: review
year: 2021
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, molecular, mechanisms, cancers]
links:
  doi: "10.21926/obm.genet.2102131"
  url: "https://doi.org/10.21926/obm.genet.2102131"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The accessible HTML article was published in OBM Genetics in 2021 and reviews lymphoma, squamous cell carcinoma, sarcoma, mammary tumors, and mast cell tumors."
    - "The article is open access under a Creative Commons Attribution license."
    - "The article reports FISS occurrence as 1 to 10 per 10,000 vaccinated cats."
    - "The article reports one cited splenic mast cell tumor comparison with median survival of 856 days with splenectomy versus 342 days without splenectomy."
  source_supported_conclusion:
    - "This source is now the first deep-extracted cancer molecular branch-map anchor."
    - "It should shape branch placement for lymphoma, oral SCC, sarcoma/FISS, mammary carcinoma, and mast cell tumors."
    - "It should not be used as a treatment guideline or owner-facing recommendation source."
  llm_inference:
    - "The cancer module should split early by tumor family rather than compile a single flat oncology page."
    - "Comparative oncology model language should remain separated from feline clinical guidance."
---

# Molecular Mechanisms of Feline Cancers

## Evidence-Depth Caveat

This card has a round-1 deep-extraction worksheet based on the accessible open HTML article page. The Crossref XML endpoint returned CloudFront 503 during this run, so the extraction was not XML/PDF based.

## Deep Extraction, 2026-05-30

[Deep extraction worksheet](../../system/indexes/src-cancer-004-deep-extraction-round1.md)

This source is the first deep-extracted cancer molecular branch-map anchor. It is useful for organizing the cancer module into tumor-family branches:

- lymphoma
- oral squamous cell carcinoma
- sarcoma / injection-site sarcoma
- mammary carcinoma
- mast cell tumors

Use boundary:

- safe for branch placement, mechanism landscape, and extraction priority
- unsafe for treatment ranking, prognosis claims, biomarker decision rules, or human-to-cat therapy translation


## One-Line Summary

Deep-extracted molecular review that maps lymphoma, oral SCC, sarcoma/FISS, mammary carcinoma, and mast cell tumor branches for the feline cancer module.

## Why It Matters For Feline Cancer

This source prevents the new cancer module from becoming a flat list of unrelated oncology papers. It supplies the first reusable molecular branch map, while keeping treatment and comparative-oncology claims bounded.

## Key Findings

### quoted_fact

- The accessible HTML article reviews lymphoma, squamous cell carcinoma, sarcoma, mammary tumors, and mast cell tumors.
- The article is open access under a Creative Commons Attribution license.
- The article reports FISS occurrence as 1 to 10 per 10,000 vaccinated cats.
- The article reports one cited splenic mast cell tumor comparison with median survival of 856 days with splenectomy versus 342 days without splenectomy.

### source_supported_conclusion

- This source can anchor the first cancer molecular mechanism branch map.
- Lymphoma should preserve older FeLV/FIV logic separately from newer gastrointestinal lymphoma framing.
- Sarcoma should split injection-site associated disease from spontaneous sarcoma.
- Mammary carcinoma comparative-oncology claims should stay bounded from feline treatment guidance.

### llm_inference

- The cancer module should split early into tumor-family branches rather than compress into one generic oncology page.
- Comparative oncology model logic should be separated from direct feline clinical recommendations.

## Claim-Fit Judgment

Strongest safe use:

- molecular branch map
- comparative oncology boundary setting
- extraction priority for lymphoma, oral SCC, sarcoma/FISS, mammary carcinoma, and mast cell tumor branches

Must not control yet:

- treatment ranking
- owner-facing prognosis statements
- biomarker decision rules
- human-to-cat therapy translation
- numeric risk claims outside this review's cited context

## Image Asset TODO

- figures to capture: gene-expression and mutation tables if full table assets are needed later
- why these matter: table-level gene lists may help branch-specific mechanism pages, but should not be copied into topic pages without table verification

## Open Follow-Up Questions

- What source family is confirmed by the abstract or article body?
- Which claims, if any, are reusable for the cancer module?
- Does this source deserve deep extraction, or should it remain queue context?
- Are there tables or figures that change the module structure?

## Extraction Provenance

This card is marked full because the paired deep-extraction worksheet already captured the article's branch-map role and bounded numeric examples. The source should keep acting as an architecture anchor, while disease-specific pages rely on narrower tumor-family sources before making treatment, prognosis, or biomarker claims.

## Linked Entities

- diseases: cancer
- models:
- endpoints:
- mechanisms:
- regulations:
