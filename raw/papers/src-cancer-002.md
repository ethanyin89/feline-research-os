---
id: src-cancer-002
type: source
title: "Swiss Feline Cancer Registry 1965–2008: the Influence of Sex, Breed and Age on Tumour Types and Tumour Locations"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: [Switzerland]
evidence_level: original-study
year: 2016
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, swiss, registry, influence, sex, breed, age, types]
links:
  doi: "10.1016/j.jcpa.2016.01.008"
  url: "https://doi.org/10.1016/j.jcpa.2016.01.008"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The ETH Research Collection record identifies this as an open-access 2016 Journal of Comparative Pathology article, volume 154, pages 195-210."
    - "The article analyzes the Swiss Feline Cancer Registry, comprising 51,322 feline patient records from 1965 to 2008 and 18,375 reported tumours."
    - "The article reports that data were analyzed with proportional calculations because obligatory cat registration was absent in Switzerland."
  source_supported_conclusion:
    - "This source can anchor registry-based tumor-type, location, age, sex/neuter, breed, and time-trend boundaries for the cancer module."
    - "It should not be used as universal feline cancer prevalence or causal proof outside the Swiss pathology-submission registry context."
  llm_inference:
    - "Registry and prevalence pages need a dedicated denominator caveat before numeric tumor-frequency claims."
---

# Swiss Feline Cancer Registry 1965–2008: the Influence of Sex, Breed and Age on Tumour Types and Tumour Locations

## Evidence-Depth Caveat

This card has a round-1 deep-extraction worksheet based on the ETH Research Collection open-access record and browser-readable PDF text. The source is a registry / epidemiology anchor, not a universal prevalence, causality, treatment, or prognosis source.

## Deep Extraction, 2026-05-30

[Deep extraction worksheet](../../system/indexes/src-cancer-002-deep-extraction-round1.md)

Safe promoted role:

- registry denominator and proportional-frequency caveats
- tumor-type and anatomic-location branch prioritization
- signalment variables: age, sex/neuter status, breed, and time
- FISS / fibrosarcoma and lymphoma time-trend hypotheses with explicit registry limits

Do not use this source as:

- universal feline cancer prevalence
- proof of vaccine causality
- treatment guidance
- owner-facing risk prediction
- prognosis or survival guidance

## One-Line Summary

Deep-extracted Swiss registry study useful for tumor-type, location, signalment, and time-trend architecture within a pathology-submission denominator.

## Why It Matters For Feline Cancer

This source gives the cancer module its first registry-based denominator. It should discipline numeric claims by tying them to Swiss pathology records, ICD-O-3 coding, and proportional calculations rather than implying population incidence.

## Key Findings

### quoted_fact

- The intake sheet lists this title: Swiss Feline Cancer Registry 1965–2008: the Influence of Sex, Breed and Age on Tumour Types and Tumour Locations.
- The DOI is 10.1016/j.jcpa.2016.01.008.
- The study is based on 51,322 feline patient records compiled from 1965 to 2008.
- The study reports 18,375 tumours in the registry records.
- The study used proportional calculations because there was no obligatory registration of cats in Switzerland.

### source_supported_conclusion

- This source supports registry-bounded frequency and branch-priority claims.
- It supports a prevalence / registry caveat page before tumor-family pages reuse numeric frequency language.
- Time trends for fibrosarcoma and lymphoma are useful hypothesis context, not causal closure.

### llm_inference

- Feline cancer synthesis should distinguish pathology-registry proportions from population incidence.
- FISS and FeLV/lymphoma timing should be treated as branch-control questions requiring corroborating sources.

## Claim-Fit Judgment

Strongest safe use:

- registry / prevalence architecture
- tumor-type and location branch priority
- signalment and time-trend caveats

Must not control yet:

- reader-facing medical advice
- universal prevalence claims
- causality claims
- treatment ranking
- guideline-like recommendations
- mechanism closure

## Image Asset TODO

- figures to capture: tumor-type and location time-trend figures, if image assets are later needed
- why these matter: they can support internal branch prioritization but should not be copied into owner-facing pages without table-level verification

## Open Follow-Up Questions

- Should the earlier Swiss registry overview paper be extracted as a paired denominator source?
- Which FISS-specific source should verify injection-site sarcoma claims before a sarcoma branch page is compiled?
- Which FeLV/lymphoma source should verify the lymphoma time-trend interpretation?

## Extraction Provenance

This card is marked full because the paired deep-extraction worksheet has already separated denominator facts from branch-priority interpretation. The added value is not more prose; it is the explicit warning that registry proportions must stay tied to pathology-submission records, not converted into population incidence.

## Linked Entities

- diseases: cancer
- models:
- endpoints:
- jurisdictions: Switzerland
- mechanisms:
- regulations:
