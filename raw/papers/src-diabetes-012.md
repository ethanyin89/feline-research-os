---
id: src-diabetes-012
type: source
title: "Frequency of feline diabetes mellitus and breed predisposition in domestic cats in Australia"
source_kind: paper
species: feline
diseases: [diabetes mellitus]
models: []
endpoints: [frequency, breed-risk]
jurisdictions: [Australia]
evidence_level: original-study
year: 2009
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [diabetes, epidemiology, breed-risk, Australia]
links:
  doi: "10.1016/j.tvjl.2007.09.019"
  url: "https://doi.org/10.1016/j.tvjl.2007.09.019"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "PubMed abstract reports 12,576 study cats and 93 diabetes cases over 5 years."
    - "Five-year period prevalence was 7.4 per 1000 cats."
    - "Burmese cats had a period prevalence of 22.4 per 1000 cats."
    - "PubMed abstract reports mean age at first diagnosis was higher in Burmese cats than in domestic short/longhaired cats."
  source_supported_conclusion:
    - "This is the Australian frequency and breed-predisposition anchor."
    - "This source strengthens the Burmese predisposition signal seen in the UK risk-factor source."
    - "Clinic-based period prevalence needs generalizability limits."
    - "The source supports breed-risk visibility, not the mechanism behind Burmese predisposition."
    - "UK and Australian denominator differences should stay visible in any cross-population synthesis."
  llm_inference:
    - "This is a full-text target if the module needs breed denominator, case definition, or age/sex stratification detail."
---

# Frequency of feline diabetes mellitus and breed predisposition in domestic cats in Australia

## One-Line Summary

Australian epidemiology source for diabetes frequency and breed predisposition in domestic cats.

## Why It Matters For Feline Diabetes

- adds population and breed-risk evidence outside the UK source
- helps separate breed predisposition from general obesity or age risk

## Key Findings

- abstract-level extraction confirms Australian feline-only clinic period-prevalence data
- 93 diabetes cases were identified among 12,576 cats over a 5-year period
- Burmese cats had a higher period prevalence than domestic short/longhaired cats
- mean age at first diagnosis was higher in Burmese cats than domestic short/longhaired cats in the abstract report
- this source is the strongest Australian breed-predisposition anchor in the seed corpus
- the signal strengthens the UK Burmese-risk finding while preserving a different denominator and clinic context

## Limits / Caveats

- extraction is abstract-weighted, not full-text
- clinic-based denominator limits broad prevalence generalization
- mechanism behind Burmese predisposition is not established by this card
- do not collapse clinic-based period prevalence into national prevalence
- do not turn breed predisposition into a deterministic individual prediction

## Australian Breed-Risk Logic

This source is the Australian counterpart to the UK risk-factor paper.

What can be promoted:

- two feline-only clinics contributed a 5-year diabetes frequency signal
- 12,576 study cats and 93 diabetes cases define the denominator and cases in the abstract
- Burmese cats had higher period prevalence than domestic short/longhaired cats
- age at first diagnosis differed by breed group in the abstract

What should be held:

- global prevalence
- genetic mechanism
- individual prediction
- causal interpretation
- direct equivalence to insured UK data

## Relationship To UK Risk-Factor Source

This card should be paired with [src-diabetes-009](src-diabetes-009.md).

The safe synthesis is:

- Burmese risk appears in both sources
- UK data add broader risk-factor signals including sex/neuter status, activity, weight, and medication exposure
- Australian data add feline-clinic period prevalence and breed-period-prevalence detail
- both need denominator caveats

## Write-Back Implications

- [risk and recognition](../../topics/diabetes/risk-and-recognition.md) should keep Burmese predisposition visible but bounded.
- [diabetes breed-risk synthesis memo](../../system/indexes/diabetes-breed-risk-synthesis-memo.md) should own the UK/Australia comparison.
- [synthesis index](../../topics/diabetes/synthesis-index.md) should avoid a single universal prevalence figure.

## Full-Text Target If Needed

If later outputs need population-risk tables, extract feline-only clinic denominator rules, case definitions, breed counts, age and sex stratification, and whether Burmese risk persists after adjustment. The key question is not only whether Burmese cats are enriched, but how far that signal travels outside the clinic population and into general risk communication.

## Current Safe Role

Use this source to strengthen breed-risk visibility and to pair with the UK insured-population source. It is strongest as a cross-population signal check, not as a universal prevalence estimate or genetic-mechanism claim for all cats.

## Open Follow-Up Questions

- which breeds were over- or under-represented?
- what denominator and case definition were used?
- are findings compatible with UK risk-factor data?

## Linked Entities

- diseases: diabetes mellitus
- models:
- endpoints: frequency, breed risk
- mechanisms:
- regulations:
