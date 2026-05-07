---
id: src-fip-013
type: source
title: "Long-term follow-up of cats in complete remission after treatment of feline infectious peritonitis with oral GS-441524"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: []
jurisdictions: []
evidence_level: case-series
year: 2023
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, treatment, remission, follow-up]
links:
  doi: ""
  url: "https://journals.sagepub.com/doi/10.1177/1098612X231183250"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source explicitly focuses on long-term follow-up of cats in complete remission after oral GS-441524 treatment.
    - The abstract reports follow-up of 18 successfully treated cats for up to 1 year after treatment initiation, with 9 months after treatment completion.
    - The abstract reports stable laboratory parameters and undetectable blood viral loads in all but one cat on one occasion.
    - The abstract reports no confirmed relapse during the 1-year follow-up period.
  source_supported_conclusion:
    - This source belongs in the remission-durability branch of the FIP treatment architecture.
    - This source supports a real post-treatment durability layer distinct from baseline efficacy and rescue-complexity papers.
  llm_inference:
    - This paper will likely matter most once the treatment branch starts differentiating initial response from post-treatment durability.
    - The paper is best used as a selected remission-cohort durability anchor, not a whole-branch success estimate.
---

# One-line Summary

Follow-up paper that anchors remission durability rather than initial treatment response in FIP.

## Why It Matters For FIP

- extends treatment logic beyond immediate response
- helps the module distinguish remission durability from baseline efficacy
- now serves as the first deep-extracted durability anchor in the FIP module

## Key Findings

- abstract reports follow-up of 18 successfully treated cats through week 48 after treatment initiation
- laboratory parameters remained stable after treatment ended
- blood viral loads stayed undetectable except for one isolated event
- no confirmed relapse was reported during one-year follow-up
- recurrent fecal shedding, transient antibody rises, and mild delayed neurologic signs still appeared in a subset

## Remission-Durability Role

This source gives the treatment branch a post-treatment durability layer. It should not be filed as another generic `GS-441524 works` paper. Its object is different: cats that had already reached complete remission after oral GS-441524 treatment were followed to understand what remission looked like after therapy stopped.

The key reuse rule is selected-cohort framing. The abstract reports 18 successfully treated cats followed for up to 1 year after treatment initiation, with 9 months after treatment completion. That makes the study strong for durability among responders, but structurally optimistic if someone tries to use it as a whole-population success estimate. The wiki should therefore separate baseline efficacy, neurologic rescue, real-world treatment-package performance, and remission durability into different rows.

The follow-up texture is one of the most valuable parts of this source. Stable laboratory parameters and mostly undetectable blood viral loads support objective remission stability. No confirmed relapse during the follow-up period is a strong result. But the card must preserve the residual complexity: recurrent fecal shedding, transient antibody rises, and mild delayed neurologic signs appeared in some cats. Durable remission is therefore not the same as `nothing to monitor`.

In the treatment evidence memo, this source should sit above the experimental foundation (`src-fip-017`) and beside natural-disease clinical anchors (`src-fip-016`, `src-fip-019`, `src-fip-024`) as a distinct follow-up endpoint. It helps answer the owner's and clinician's next question after clinical success: what remains to watch once the cat appears well?

The safe compiled statement is: in a selected cohort of cats already in complete remission after oral GS-441524, one-year follow-up showed stable objective markers and no confirmed relapse, while still justifying continued post-treatment monitoring.

## Limits / Caveats

- current card is deep-extracted at worksheet level, but still not full-text reviewed
- remission-focused cohorts can overrepresent successful trajectories
- no-confirmed-relapse language should not be turned into universal cure language
- do not use this cohort as a baseline treatment success rate
- do not erase fecal shedding, antibody, or delayed neurologic follow-up complexity

## Open Follow-up Questions

- how should recurrent fecal shedding and transient antibody rises be interpreted inside durable remission?
- what follow-up burden should remain standard after clinical remission?
- which monitoring findings would change management rather than only documentation?
- how should this remission cohort be compared with natural-disease baseline and neurologic-treatment cohorts?

## Deep Extraction

- [src-fip-013 deep extraction round 1](../../system/indexes/src-fip-013-deep-extraction-round1.md)

## Linked Entities

- GS-441524
- remission
- follow-up
