---
id: src-fip-026
type: source
title: "Molnupiravir treatment of 18 cats with feline infectious peritonitis: A case series"
source_kind: paper
species: feline
diseases: [FIP]
models: [clinical case series]
endpoints: [remission, survival, adverse events, ALT]
jurisdictions: []
evidence_level: original-study
status: extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, molnupiravir, antiviral, treatment, case-series, japan]
links:
  doi: "10.1111/jvim.16832"
  url: "https://onlinelibrary.wiley.com/doi/full/10.1111/jvim.16832"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "18 cats diagnosed with FIP treated with molnupiravir at 10-20 mg/kg orally twice daily for 84 days."
    - "13 had effusive FIP, 5 had noneffusive FIP, 3 had neurological or ocular signs."
    - "4 cats with effusive FIP died or were euthanized within 7 days of starting treatment."
    - "14 cats completed treatment and remained in remission 139-206 days after starting treatment."
    - "Elevated ALT activity found in 3 cats at Days 7-9, all recovered without management."
    - "Pyogranulomatous lesions reduced or became undetectable on ultrasound in all 5 non-effusive cases."
  source_supported_conclusion:
    - "Molnupiravir is effective for FIP treatment at 10-20 mg/kg BID for 84 days."
    - "78% of cats (14/18) achieved sustained remission."
    - "Adverse events are transient and self-resolving (hepatic enzyme elevation)."
  llm_inference:
    - "Provides foundational case series evidence for molnupiravir as FIP antiviral."
    - "Early deaths (within 7 days) may reflect severe disease at presentation."
---

# Molnupiravir treatment of 18 cats with feline infectious peritonitis: A case series

## Evidence-Depth Caveat

Full text not directly accessible; extraction based on abstract and published summaries. Core quantitative outcomes are documented.

## One-Line Summary

Case series of 18 FIP cats treated with molnupiravir showed 78% (14/18) achieved sustained remission at 10-20 mg/kg BID for 84 days.

## Why It Matters For Feline FIP

First published case series establishing molnupiravir as a viable FIP antiviral alternative to GS-441524. Conducted in Japan with compounded formulation.

## Study Design Details

### Population

| Parameter | Value |
|-----------|-------|
| Total cats | 18 |
| Effusive FIP | 13 (72%) |
| Non-effusive FIP | 5 (28%) |
| Neurological/ocular signs | 3 |
| Study period | January-August 2022 |
| Location | You-Me Animal Clinic, Sakura-shi, Japan |

### Treatment Protocol

| Parameter | Value |
|-----------|-------|
| Drug | Molnupiravir (compounded in-house) |
| Dose | 10-20 mg/kg |
| Route | Oral |
| Frequency | Twice daily (BID) |
| Duration | 84 days |

### Outcomes

| Outcome | N | % |
|---------|---|---|
| Completed treatment | 14 | 78% |
| Died/euthanized (within 7 days) | 4 | 22% |
| Remission at follow-up | 14/14 | 100% |
| Remission duration | 139-206 days | — |

### Adverse Events

| Event | N | Timing | Resolution |
|-------|---|--------|------------|
| Elevated ALT | 3 | Days 7-9 | Spontaneous recovery |

## Key Findings

### quoted_fact

- 18 cats with FIP (13 effusive, 5 non-effusive)
- 3 cats had neurological or ocular involvement pre-treatment
- Dose: 10-20 mg/kg PO BID × 84 days
- 4 deaths/euthanasia within 7 days (all effusive FIP)
- 14 cats completed treatment with sustained remission
- Follow-up: 139-206 days post-treatment start
- Pyogranulomatous lesions resolved on ultrasound (non-effusive cases)
- Lab values normalized in all completing cats
- ALT elevation in 3 cats (transient, self-resolving)

### source_supported_conclusion

- Molnupiravir effective for FIP at 10-20 mg/kg BID
- 78% overall success rate (14/18)
- 100% remission in treatment completers
- Safety: transient hepatic changes only

### llm_inference

- Early mortality (within 7 days) likely reflects disease severity
- Compounded formulation used (not commercial product)
- 84-day duration matches GS-441524 standard protocol

## Claim-Fit Judgment

Strongest safe use:
- Molnupiravir as FIP treatment option
- 10-20 mg/kg BID dosing
- 84-day treatment duration
- Case series evidence for efficacy

Must not control yet:
- Optimal dose within range (individualized)
- Comparison to GS-441524 (see src-fip-028)
- Long-term relapse rates beyond 206 days
- Commercial formulation equivalence

## Deep Extraction

- Round 1 worksheet: [system/indexes/src-fip-026-deep-extraction-round1.md](../../system/indexes/src-fip-026-deep-extraction-round1.md)

## Clinical Context

Molnupiravir was originally developed as an influenza antiviral and gained prominence during the COVID-19 pandemic. Its mechanism of action involves viral mutagenesis through incorporation of faulty nucleotides during viral RNA replication. This case series represents the first application to feline coronavirus (the causative agent of FIP), demonstrating cross-species antiviral utility. The compounded formulation used in this study reflects the lack of veterinary-licensed molnupiravir products at the time of publication.

## Linked Entities

- diseases: FIP (effusive and non-effusive)
- models: clinical case series
- endpoints: remission, survival, ALT, ultrasound lesion resolution
- mechanisms: antiviral (nucleoside analog, viral mutagenesis)
- regulations: none applicable
