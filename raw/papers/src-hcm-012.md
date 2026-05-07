---
id: src-hcm-012
type: source
title: "Influence of Clinical Aspects and Genetic Factors on Feline HCM Severity and Development"
source_kind: paper
species: feline
diseases: [HCM]
models: []
endpoints: [severity]
jurisdictions: []
evidence_level: original-study
year: 2024
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [hcm, genetics, severity]
links:
  doi: ""
  url: "https://www.mdpi.com/2306-7381/11/5/214"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The abstract states that feline HCM is primarily related to mutations in the MYBPC3 and MYH7 genes."
    - "The abstract studies heterozygosity and homozygosity for the p.A31P mutation in MYBPC3 in relation to HCM severity and development."
    - "The abstract states that homozygous cats had moderate to severe HCM, with higher penetrance and significant risk of cardiac death compared with heterozygous cats."
    - "The abstract states that HCM showed age-related penetrance, with no disease in cats up to 1 year and the highest proportion in cats aged 7 years and older."
  source_supported_conclusion:
    - Genotype-phenotype and severity pressure are already real branches in the HCM seed set.
    - The study supports keeping genotype dosage visible because homozygous and heterozygous states do not appear clinically equivalent.
    - The study supports age-aware penetrance as part of HCM recognition and risk framing.
    - This paper is one of the strongest current bridges between the genetics branch and the recognition/risk branches because it makes dosage and timing clinically meaningful.
    - The source argues against binary mutation language by showing that genotype state affects severity, penetrance, and cardiac-death risk differently.
  llm_inference:
    - This may become a key bridge between genetics and recognition after deep extraction.
    - HCM pages should keep genetics stratified by dosage and age-related penetrance instead of flattening mutation-positive cats into one uniform risk class.
---

# One-line Summary

Clinical-genetic severity paper that strengthens the genotype-phenotype branch and makes mutation dosage and age-related penetrance explicit.

## Why It Matters For HCM

- links genetics to clinical severity rather than leaving genetics abstract
- may become central for prognosis and recognition depth
- now gives the HCM shell a safer rule that genotype pressure should stay stratified, not flattened into simple mutation present/absent language

## Key Findings

- severity and development framing
- abstract links MYBPC3 p.A31P genotype dosage to severity differences
- abstract supports earlier and more severe disease in homozygous cats than in heterozygous cats
- abstract supports age-related penetrance

## Why This Study Matters

This study matters because it keeps the HCM genetics branch clinically grounded.

Without a paper like this, genetics can drift in one of two bad directions. It can become too abstract, where variants are mentioned but never tied to real disease pressure, or too simplistic, where mutation-positive status gets treated as one flat risk bucket. This source pushes against both errors.

Its main contribution is to make genotype dosage clinically meaningful. Homozygous and heterozygous p.A31P MYBPC3 states do not behave the same way. Severity, penetrance, and cardiac-death risk all move in the same direction, which gives the HCM module a more realistic genotype-to-phenotype bridge.

It also adds time structure. Age-related penetrance means genetic risk cannot be read as immediate phenotype certainty. That is important because it keeps recognition architecture connected to age, not only to mutation status.

## Genotype-Severity Signal

The safest promotion from this source is:

- genotype dosage should remain visible
- homozygous and heterozygous states should not be treated as clinically equivalent
- age-aware penetrance is part of recognition and risk framing
- genetics can influence risk and severity without becoming a standalone phenotype substitute

That makes this card more than a genetics paper. It is a bridge source linking mechanism, recognition, and risk.

## Limits / Caveats

- current card is abstract-weighted, not full-text reviewed
- The source is strongest for dosage-sensitive genotype framing around the studied mutation, not for universal claims across every feline HCM variant or breed.

## Image Asset TODO

- figures to capture:
  - penetrance curve by age
  - genotype outcome table
- candidate target paths are tracked in [HCM image ingest manifest](../../system/indexes/hcm-image-ingest-manifest-20260417.md) until article labels are verified.

## Open Follow-up Questions

- which clinical factors and which genetic factors dominate severity?
- does the paper change recognition or prognosis more?
- how much of this genotype-severity signal is reusable outside the studied mutation and breeds?
- how should genotype dosage be represented in a stable HCM risk-stratification page without overgeneralizing beyond p.A31P?
- what additional breed-specific or variant-specific contexts does the full paper discuss beyond the abstract framing?

## Linked Entities

- HCM
- genetics
- severity
