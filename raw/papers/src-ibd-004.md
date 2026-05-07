---
id: src-ibd-004
type: source
title: "A Clinical Index for Disease Activity in Cats with Chronic Enteropathy"
source_kind: paper
species: feline
diseases: [IBD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2010
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ibd, chronic-enteropathy, disease-activity]
links:
  doi: "10.1111/j.1939-1676.2010.0549.x"
  url: "https://academic.oup.com/jvim/article/24/5/1027/8447312"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source explicitly develops a clinical index for disease activity in cats with chronic enteropathy.
    - The abstract reports 82 cats with chronic enteropathy, including retrospective IBD cases and prospective IBD or food-responsive enteropathy cases.
    - The abstract states that the combination of gastrointestinal signs, endoscopic abnormalities, serum total protein, serum alanine transaminase or alkaline phosphatase activity, and serum phosphorus concentration comprised the feline chronic enteropathy activity index.
    - The abstract states that positive treatment responses were accompanied by significant reductions in FCEAI scores after treatment.
  source_supported_conclusion:
    - This source anchors the operational disease-activity branch of the IBD module.
    - The study supports treating FCEAI as a response-tracking and severity-staging tool across chronic enteropathy, not as a disease-class discriminator.
  llm_inference:
    - This was the correct second-wave IBD deep extraction target because it gives the module a concrete operational endpoint architecture.
---

# One-line Summary

Clinical-index paper that likely provides the lead operational endpoint framework for feline chronic enteropathy and IBD workup.

## Why It Matters For IBD

- gives the module a concrete disease-activity branch rather than only pathology and mechanism
- likely helps separate `clinical activity` from biopsy confirmation
- now serves as the first real operational endpoint anchor in the IBD module

## Key Findings

- abstract includes both retrospective IBD cases and prospective IBD or food-responsive enteropathy cases
- abstract identifies a multivariable index combining gastrointestinal signs, endoscopic abnormalities, serum total protein, ALT or ALP activity, and serum phosphorus
- abstract states that FCEAI correlated best with histopathologic inflammation among candidate variable sets
- abstract states that treatment response was accompanied by significant reduction in FCEAI score
- abstract conclusion supports use of FCEAI for initial severity assessment and treatment-response measurement in both IBD and FRE

## Disease-Activity Role

This paper anchors the operational endpoint layer for feline chronic enteropathy. Its main value is not disease identity; it is activity measurement. FCEAI combines gastrointestinal signs, endoscopic abnormalities, serum total protein, ALT or ALP activity, and serum phosphorus into a feline chronic enteropathy activity index. That gives the wiki a concrete answer to a practical question: once chronic enteropathy is live, how can severity and response be tracked?

The index must stay in the correct layer. Because the abstract includes IBD and food-responsive enteropathy, the score should not be treated as an IBD discriminator. It can help assess initial severity and track treatment response, but it does not settle whether the cat has idiopathic IBD, food-responsive disease, or small-cell lymphoma. This distinction is central to the module: activity, diagnosis, and boundary discrimination are different jobs.

For wiki reuse, this source should sit in the endpoint handbook rather than in the mechanism core. It is the lead activity-index anchor, while biopsy-site sources control lymphoma exclusion and diet sources control food-responsive claims. The response-tracking signal is useful because positive treatment responses were accompanied by significant reductions in FCEAI scores. That makes it relevant to monitoring and treatment follow-up, not just baseline triage.

The card also creates a useful warning about endoscopy-dependent scoring. If endoscopic abnormalities are part of the index, FCEAI may be less lightweight than a purely clinical score. The future output page should therefore explain where the index is operationally helpful and where its components limit casual use.

The safe compiled rule is: FCEAI can structure severity and response measurement in feline chronic enteropathy, including IBD and food-responsive enteropathy, but it should not be promoted into a lymphoma-exclusion or etiologic-diagnosis tool.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- a chronic-enteropathy activity index does not by itself settle IBD-versus-lymphoma boundary questions
- endoscopy-dependent components may limit lightweight frontline use
- do not convert response tracking into proof of disease class

## Image Asset TODO

- figures to capture:
  - FCEAI component table
  - score-versus-treatment-response figure
  - any pathology-correlation plot
- why these matter:
  - this source is the operational endpoint anchor for the IBD module and should preserve its multivariable architecture clearly
  - a component table is higher value than paraphrase because it defines what the index actually is
  - response-tracking and pathology-correlation plots would keep FCEAI in the monitoring layer rather than being mistaken for a class discriminator

## Open Follow-up Questions

- what variables are included in the index?
- how well does the index track pathology or treatment response?
- how much does FCEAI remain useful once lymphoma enters the workup frame?
- which component weights and score thresholds are used in the full article?
- does the index perform differently in IBD versus food-responsive enteropathy?

## Deep Extraction

- [src-ibd-004 deep extraction round 1](../../system/indexes/src-ibd-004-deep-extraction-round1.md)

## Linked Entities

- chronic enteropathy activity
- clinical index
- disease activity
