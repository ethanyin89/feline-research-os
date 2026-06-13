---
id: src-cancer-045
type: source
title: "Treatment of mammary cancer with focused ultrasound: A pilot study in canine and feline patients"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2023
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
pmid: 36917874
doi: "10.1016/j.ultras.2023.106974"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, treatment, mammary, focused, ultrasound, pilot, study, patients]
links:
  doi: "10.1016/j.ultras.2023.106974"
  url: "https://www.sciencedirect.com/science/article/abs/pii/S0041624X23000501?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Treatment of mammary cancer with focused ultrasound: A pilot study in canine and feline patients."
    - "The intake sheet locator is: https://www.sciencedirect.com/science/article/abs/pii/S0041624X23000501?via%3Dihub."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
---

# Treatment of mammary cancer with focused ultrasound: A pilot study in canine and feline patients

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. 2023 Ultrasonics: 9 dogs and cats with superficial mammary cancer; 2-MHz focused ultrasound produced coagulative necrosis in all tumors; feasibility only, not a treatment recommendation. [Deep extraction worksheet](../../system/indexes/src-cancer-045-deep-extraction-round1.md).

## Source Check, 2026-06-01

PubMed abstract fetched as a zero-cost extraction step.

- PMID: 36917874
- DOI: 10.1016/j.ultras.2023.106974
- Journal: Ultrasonics
- Year: 2023

## Abstract Summary

This pilot study assessed thermal focused ultrasound (FUS) feasibility for canine and feline mammary cancer therapy.

**Study design:**

| Feature | Abstract-Extracted Detail |
|---------|---------------------------|
| Technology | 2-MHz single-element spherically focused ultrasonic transducer integrated with robotic positioning |
| Preclinical validation | Rabbit thigh model used to validate tissue ablation protocol |
| Veterinary patients | 9 dogs and cats with superficial mammary cancer |
| Clinical protocol | FUS ablation followed by immediate surgical resection |
| Safety selection | Animals recruited under specific safety criteria |

**Key findings:**

- Histopathology demonstrated well-defined coagulative necrosis in all treated tumors.
- No off-target damage was reported in the abstract.
- The authors state that larger studies are needed to confirm safety and feasibility, especially for complete ablation of deep-seated tumors.

**Boundary:** This is a small mixed canine/feline pilot with immediate resection after FUS. It supports feasibility research only, not clinical adoption or outcome benefit.

## One-Line Summary

Focused ultrasound produced targeted coagulative necrosis without abstract-reported off-target damage in a 9-patient canine/feline mammary cancer pilot, but remains feasibility-stage evidence.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Treatment of mammary cancer with focused ultrasound: A pilot study in canine and feline patients.
- The intake sheet locator is: https://www.sciencedirect.com/science/article/abs/pii/S0041624X23000501?via%3Dihub.

### source_supported_conclusion

- This is a first-pass source-card placeholder for triage and queue control.
- It should not support prevalence, diagnostic, treatment, management, or risk-ranking claims yet.

### llm_inference

- The title suggests a possible `cancer` role, but the actual claim-fit requires abstract or full-text review.

## Claim-Fit Judgment

Strongest safe use:

- intake ownership
- source queue placement
- deduplication and future extraction planning

Must not control yet:

- reader-facing medical advice
- numeric claims
- comparative ranking
- guideline-like recommendations
- mechanism closure

## Image Asset TODO

- figures to capture: unknown until source text is read
- why these matter: tables or figures should remain behind the candidate gate until labels are verified

## Open Follow-Up Questions

- What source family is confirmed by the abstract or article body?
- Which claims, if any, are reusable for the cancer module?
- Does this source deserve deep extraction, or should it remain queue context?
- Are there tables or figures that change the module structure?

## Linked Entities

- diseases: cancer
- models:
- endpoints:
- mechanisms:
- regulations:
