---
id: src-hcm-001
type: source
title: "The Feline Cardiomyopathies: 2. Hypertrophic cardiomyopathy"
source_kind: paper
species: feline
diseases: [HCM]
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
tags: [hcm, review, mechanism]
links:
  doi: "10.1177/1098612X211020162"
  url: "https://journals.sagepub.com/doi/10.1177/1098612X211020162"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The abstract states that HCM is the most common feline cardiomyopathy seen clinically and may affect roughly up to 15% of domestic cats, mostly as subclinical disease."
    - "The abstract states that biomarkers should not be used on their own to diagnose HCM."
    - "The abstract states that severe feline HCM can usually be diagnosed by echocardiography, but mild to moderate wall thickening remains a diagnosis of exclusion."
    - "The abstract-level source card captures that diastolic dysfunction and left-atrial consequences drive heart failure and arterial thromboembolism risk."
    - "The abstract states that no current treatment reverses or slows the underlying cardiomyopathic process."
  source_supported_conclusion:
    - This is the best current broad HCM review anchor in the seed corpus.
    - The review supports modeling HCM recognition around echocardiography plus exclusion of other causes of left-ventricular hypertrophy, not around biomarker-only diagnosis.
    - The review supports keeping treatment language bounded, because it explicitly says no current therapy reverses or slows the cardiomyopathic process.
    - This source is especially valuable because it connects recognition hierarchy, exclusion-zone uncertainty, consequence architecture, and treatment pessimism inside one broad review frame.
    - The paper strengthens the rule that structural phenotype should lead the HCM module, while biomarkers remain supportive and translation remains consequence-management oriented.
  llm_inference:
    - This is a strong first deep-extraction candidate for the HCM module.
    - HCM pages should keep an explicit `exclusion zone` branch for mild-to-moderate hypertrophy rather than compressing all wall thickening into one diagnosis-positive story.
---

# One-line Summary

Broad feline HCM review that should anchor the first full compile of the disease module and set the main recognition and treatment boundaries.

## Why It Matters For HCM

- gives the module one broad HCM reference point before the map fragments into genetics, biomarkers, and treatment
- likely stabilizes baseline HCM terminology and branch architecture
- now gives the shell a safer first-pass rule that echocardiography leads while biomarkers stay supportive

## Key Findings

- dedicated HCM review anchor
- abstract frames HCM as the most common feline cardiomyopathy and mostly subclinical in prevalence
- abstract says biomarkers should not be relied on in isolation for diagnosis
- abstract says severe HCM is usually diagnosable by echocardiography, while mild to moderate hypertrophy remains a diagnosis of exclusion
- abstract says diastolic dysfunction and left-atrial consequences drive heart failure and arterial thromboembolism risk
- abstract says no current treatment reverses or slows the underlying cardiomyopathic process

## Why This Review Matters

This paper matters because it gives the HCM module one place where recognition, consequence, and treatment boundaries sit together instead of being inferred from separate narrow sources.

The first important contribution is disease framing. If HCM is both common and often subclinical, then the module cannot be built only around overt heart failure or late-stage visible disease. Recognition has to start before clinical decompensation becomes the only obvious entry point.

The second contribution is hierarchy control. The review does not let biomarkers outrank structure. Echocardiography still leads confirmation, and mild-to-moderate hypertrophy remains an exclusion problem rather than a flat positive test. That means uncertainty belongs near the center of the HCM module, not hidden in a footnote.

The third contribution is translational discipline. The paper explicitly refuses a disease-reversal story. Current treatment does not reverse or slow the underlying cardiomyopathic process. That makes this review a useful guardrail against overcompression when therapy papers start to look more exciting than the baseline evidence layer actually supports.

## Structural Signal

The safest promotion from this source is:

- HCM should be modeled as a structural-phenotype-led disease
- biomarkers are supportive, not standalone diagnostic authority
- mild-to-moderate hypertrophy needs a real exclusion-zone branch
- diastolic dysfunction and left-atrial burden connect phenotype to consequence
- treatment language should stay below disease-modification claims

That makes this card a true broad-anchor candidate rather than a generic summary source.

## Limits / Caveats

- current card is abstract-weighted, not full-text reviewed
- This source is strongest for architectural write-back and broad branch hierarchy, not for fine-grained therapeutic ranking or threshold-level echo rules.

## Image Asset TODO

- figures to capture:
  - mechanism overview
  - clinical staging or pathophysiology summary diagram
- candidate target paths are tracked in [HCM image ingest manifest](../../system/indexes/hcm-image-ingest-manifest-20260417.md) until article labels are verified.

## Open Follow-up Questions

- how does it frame structural phenotype versus genetics?
- how much treatment guidance does it actually support?
- how sharply does it separate severe echo-defined disease from mild-to-moderate exclusion-zone disease?
- what exact exclusion causes of left-ventricular hypertrophy does the review prioritize?
- how strongly does it connect left-atrial change to overt CHF versus arterial thromboembolism risk?

## Linked Entities

- HCM
- cardiomyopathy
- echocardiography
- biomarkers
