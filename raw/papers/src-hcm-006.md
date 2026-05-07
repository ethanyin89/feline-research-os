---
id: src-hcm-006
type: source
title: "Cardiac Troponin I in Feline Hypertrophic Cardiomyopathy"
source_kind: paper
species: feline
diseases: [HCM]
models: []
endpoints: [cardiac-troponin-i]
jurisdictions: []
evidence_level: original-study
year: 2002
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [hcm, biomarker, troponin]
links:
  doi: ""
  url: "https://academic.oup.com/jvim/article/16/5/558/8453286"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The abstract reports plasma cardiac troponin I measurement in 33 healthy control cats and 20 cats with moderate to severe HCM."
    - "The abstract reports significantly higher cTnI concentrations in cats with HCM than in normal cats."
    - "The abstract reports sensitivity of 85% and specificity of 97% for differentiating moderate-to-severe HCM from normal cats."
    - "The abstract reports only weak correlation with left-ventricular free-wall thickness and no meaningful correlation with some other structural indices."
    - "The abstract reports higher cTnI in cats with active congestive heart failure than in cats without current heart failure."
  source_supported_conclusion:
    - Troponin belongs in the HCM biomarker branch.
    - The paper supports cTnI as a myocardial-injury or severity-linked marker, not as a replacement for structural phenotype definition.
    - The paper supports a biomarker-use-case split between disease detection in more advanced HCM and structural characterization itself.
    - This study is valuable because it gives the HCM endpoint branch a real blood-marker signal without allowing that signal to outrank echocardiographic phenotype definition.
    - The source strengthens a use-case hierarchy in which cTnI is more informative for injury burden and active failure pressure than for early structural screening.
  llm_inference:
    - This may become a key endpoint-separation paper after deeper review.
    - HCM endpoint pages should separate `injury/severity biomarker` from `screening biomarker` rather than ranking all blood markers in one flat list.
---

# One-line Summary

Troponin-focused biomarker study for the HCM endpoint branch, strongest as a myocardial-injury and severity signal rather than a standalone phenotype definition tool.

## Why It Matters For HCM

- gives the module one specific blood biomarker anchor
- helps separate phenotype recognition from biomarker interpretation
- now gives the HCM shell a safer rule that troponin rises with more advanced disease burden and active failure pressure

## Key Findings

- dedicated troponin I source
- abstract shows significantly higher cTnI in moderate-to-severe HCM versus healthy controls
- abstract reports 85% sensitivity and 97% specificity for differentiating moderate-to-severe HCM from normal cats
- abstract supports ongoing myocardial damage and stronger signal in cats with active congestive heart failure

## Why This Study Matters

This study matters because it keeps the HCM biomarker branch from becoming vague.

The useful signal is not simply that troponin rises. The study shows that cTnI separates moderate-to-severe HCM from healthy controls quite well, but it also shows only weak correlation with some structural measures. That combination matters. It means cTnI has real endpoint value, but not as a structural surrogate.

The study also sharpens use case. Troponin is higher in cats with active congestive heart failure, which suggests that the marker becomes more informative as clinical burden rises. That pushes cTnI toward an injury/severity interpretation rather than a pure early-recognition or phenotype-definition role.

## Biomarker Signal

The safest promotion from this source is:

- cTnI belongs in the real HCM biomarker branch
- it is stronger for moderate-to-severe disease than for broad screening language
- it should stay below structural phenotype definition in authority
- active CHF increases its interpretive weight

That makes this card useful not just for endpoint pages, but for keeping biomarker rhetoric disciplined across the whole HCM module.

It also gives the endpoint layer a cleaner internal split. Some markers are trying to help with suspicion or screening, while others mainly become informative once myocardial injury burden is already substantial. This study places cTnI much closer to the second category, which is exactly why it helps control biomarker overcompression.

## Limits / Caveats

- current card is abstract-weighted, not full-text reviewed
- older biomarker work may not map cleanly onto later use cases
- The source is strongest for biomarker role-bounding and severity interpretation, not for current multimarker screening policy.

## Open Follow-up Questions

- is troponin used here for diagnosis, severity, or prognosis?
- how does it compare to NT-proBNP after later review?
- how much of its signal is detecting advanced myocardial injury rather than early screening value?
- which structural indices failed to correlate meaningfully with cTnI?
- how should cTnI and NT-proBNP be separated in a stable HCM biomarker-use-case table?

## Linked Entities

- HCM
- cardiac troponin I
