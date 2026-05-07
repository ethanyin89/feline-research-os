---
id: src-fcv-009
type: source
title: "Calicivirus Infection in Cats"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [diagnosis, vaccination, environmental tenacity, treatment]
jurisdictions: []
evidence_level: review
year: 2022
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, review, abcd, diagnosis, vaccination]
links:
  doi: "10.3390/v14050937"
  url: "https://www.mdpi.com/1999-4915/14/5/937"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "MDPI abstract reports FCV is highly contagious, resistant to many disinfectants, and demonstrates high genetic variability."
    - "MDPI abstract reports FCV infections are particularly problematic in multicat environments."
    - "MDPI abstract reports FCV can best be detected by reverse-transcriptase PCR, but a negative result does not rule out infection and healthy cats can test positive."
    - "MDPI abstract reports all cats should be vaccinated against FCV, but vaccination protects cats from disease and not from infection."
    - "MDPI abstract reports infection-induced immunity is not life-long and does not protect against all strains, so cats recovered from caliciviral disease should still be vaccinated."
  source_supported_conclusion:
    - This is a major modern FCV diagnosis-and-control anchor.
    - The paper supports separating disease reduction from infection prevention.
    - The paper supports writing PCR as the best current detection tool while still preserving strong anti-overinterpretation boundaries.
    - The paper supports multicat-environment framing as a central FCV control context rather than a side note.
  llm_inference:
    - This source now serves as the main FCV diagnosis/control bridge between older guidelines and the 2025 broad-control review.
    - The safest downstream wording is `PCR-best-but-bounded, vaccination-core-but-non-sterilizing`.
---

# Calicivirus Infection in Cats

## One-Line Summary

Modern ABCD-style FCV review emphasizing diagnosis limits, non-sterilizing vaccination, and the breadth of FCV clinical disease.

## Why It Matters For FCV

- provides a newer diagnosis-and-control synthesis than the 2009 guideline
- gives explicit language against overinterpreting PCR and vaccine protection
- now serves as the main FCV deep-extracted diagnosis/control bridge anchor

## Key Findings

### quoted_fact

- MDPI abstract reports FCV is highly contagious, resistant to many disinfectants, and demonstrates high genetic variability.
- MDPI abstract reports FCV infections are particularly problematic in multicat environments.
- MDPI abstract reports FCV can best be detected by reverse-transcriptase PCR, but a negative result does not rule out infection and healthy cats can test positive.
- MDPI abstract reports all cats should be vaccinated against FCV, but vaccination protects cats from disease and not from infection.
- MDPI abstract reports infection-induced immunity is not life-long and does not protect against all strains, so cats recovered from caliciviral disease should still be vaccinated.

### source_supported_conclusion

- This source is the current best FCV review for compressing diagnosis, vaccine limitation, and multicat control into one modern bridge layer.
- The paper supports recognition/control language that is simultaneously test-aware and anti-test-overclaim.
- The paper supports a vaccine frame centered on disease reduction rather than sterilizing immunity.
- The strongest safe read is `PCR-best-but-bounded, vaccination-core-but-non-sterilizing`.

### llm_inference

- If the module later builds a FCV workup page, this card should control the opening diagnostic-caution section rather than sit only in broad translation prose.

## Limits / Caveats

- review-level synthesis still needs primary-paper pressure-testing
- should not substitute for direct vaccine-comparison or treatment-efficacy papers
- the current extraction is abstract-led plus selectively reviewed open text, not a full line-by-line extraction of the entire review

## Diagnosis-Control Logic

What can be promoted:

- FCV PCR is the best current detection tool in the review layer
- PCR results still require context because negative tests do not exclude infection and healthy cats can test positive
- vaccination is core, but should be written as disease mitigation rather than infection prevention
- multicat environments deserve explicit control-layer emphasis

What should be held:

- any statement that PCR alone confirms or excludes FCV
- any statement that FCV vaccination prevents infection
- any flattening of recovered-cat immunity into durable all-strain protection

## Operational Read

This paper matters because it gives the FCV module a clean middle layer between old practical
guideline wording and the newer broad-control review. The preserved abstract facts do three jobs
at once: they keep PCR at the top of the diagnostic tool hierarchy, they stop PCR from being
treated as etiologic closure, and they keep vaccination framed as core but non-sterilizing.

That is exactly why this card belongs in both recognition and translation surfaces. `src-fcv-004`
still owns hands-on practical guidance, and `src-fcv-007` now owns the highest-level integrated
control frame, but `src-fcv-009` is the bridge that makes the modern wording safer: `PCR-best-but-
bounded, vaccination-core-but-non-sterilizing, especially in multicat environments`.

Its main value is architectural: it stabilizes the diagnosis/control midpoint of the FCV module.

## Open Follow-Up Questions

- how strongly does the review prioritise chronic gingivostomatitis versus respiratory disease?
- what exact control advice is strongest for multicat environments?
- how far does the review go on vaccine-strain switching before it becomes too implementation-specific for top-layer pages?

## Linked Entities

- diseases: FCV
- models:
- endpoints: diagnosis, vaccination, environmental tenacity, treatment
- mechanisms: variability, persistence
- regulations:
