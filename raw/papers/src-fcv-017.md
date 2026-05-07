---
id: src-fcv-017
type: source
title: "Mechanisms for persistence of acute and chronic feline calicivirus infections in the face of vaccination"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [persistence, chronic carriage, vaccine limits]
jurisdictions: []
evidence_level: original-study
year: 1995
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, persistence, vaccination, carrier-state, chronic]
links:
  doi: "10.1016/0378-1135(95)00101-F"
  url: "https://www.sciencedirect.com/science/article/abs/pii/037811359500101F?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "PubMed abstract reports the original FCV-F9 strain still generated cross-reactive antibodies against almost all field strains in California."
    - "PubMed abstract reports whole inactivated FCV-2280 vaccine produced high neutralizing antibody titers with equally broad cross-reactivity."
    - "PubMed abstract reports vaccine strains caused acute disease signs and protracted oral shedding when administered orally."
    - "PubMed abstract reports cats previously infected with field or vaccine strains developed much less severe acute illness after heterologous challenge but were not protected against the chronic carrier state."
    - "PubMed abstract reports persistence in the field could not be explained solely by vaccine-resistant strain emergence."
  source_supported_conclusion:
    - This is the current core persistence-and-vaccination-limit anchor in the FCV seed set.
    - The paper supports broad vaccine cross-reactivity as real but insufficient to solve chronic-carrier persistence.
    - The paper supports separating acute-disease reduction, heterologous challenge protection, and chronic-carrier prevention.
    - The paper keeps vaccine-virus shedding and post-inoculation viral change visible inside the FCV control model.
  llm_inference:
    - This source now serves as the first deep-extracted persistence-control anchor in the FCV module.
    - The safest downstream wording is `disease mitigation without carrier-state closure`, not `vaccine failure` and not `complete protection`.
---

# Mechanisms for persistence of acute and chronic feline calicivirus infections in the face of vaccination

## One-Line Summary

Classic persistence paper showing that FCV vaccine breadth and reduced acute disease do not automatically prevent chronic carriage or sustained field persistence.

## Why It Matters For FCV

- gives the module a structural answer to why FCV remains epidemiologically durable
- helps prevent “vaccine breadth” from being misread as “carrier-state control”
- now anchors the first FCV deep-extracted boundary between disease mitigation and persistence control

## Key Findings

### quoted_fact

- PubMed abstract reports the original FCV-F9 strain still generated cross-reactive antibodies against almost all examined California field strains.
- PubMed abstract reports whole inactivated FCV-2280 also produced broadly cross-reactive neutralizing antibodies.
- PubMed abstract reports orally administered vaccine strains caused acute disease signs and protracted oral shedding.
- PubMed abstract reports post-inoculation oral isolates collected five to ten weeks later could differ from parental virus and appear more vaccine resistant.
- PubMed abstract reports previously infected cats developed much less severe acute illness after heterologous challenge but were not protected against the chronic carrier state.

### source_supported_conclusion

- This source is the current best FCV boundary paper for separating broad immune coverage from chronic-carrier control.
- The paper supports persistence as a systems problem involving field strains, vaccine-virus behavior, shedding, and within-host change.
- The strongest safe read is `reduced acute disease without carrier-state closure`.

### llm_inference

- If the module later builds a vaccine hierarchy page, this paper should sit above product rhetoric as the main anti-overclaim anchor.

## Limits / Caveats

- older California-centered work still needs reconciliation with newer epidemiology and vaccine studies
- current card is deep-extracted at worksheet level, but still not full-text reviewed section by section
- should not be used alone to rank current vaccine products

## Persistence-Control Branch Logic

This card should sit at the top of the FCV anti-overclaim stack.

What can be promoted:

- broad cross-reactivity is real and should remain visible
- reduced acute illness after prior exposure is a meaningful vaccine/control outcome
- persistence and chronic carriage remain live even when those benefits exist
- vaccine-virus behavior and within-host change belong inside the control model

What should be held:

- any claim that broad neutralization equals durable field control
- any claim that vaccines fail simply because chronic carriage still exists
- any current-market product ranking derived from this older mechanistic paper

## Write-Back Implications

- [endpoint handbook](../../topics/fcv/endpoint-handbook.md) should keep acute disease, challenge protection, and carriage in separate endpoint buckets.
- [translation brief](../../topics/fcv/translation-brief.md) should keep vaccine language at disease reduction and control architecture, not infection elimination.
- [FCV vaccine-persistence boundary memo](../../system/indexes/fcv-vaccine-persistence-boundary-memo.md) should treat this card as the first deep-extracted persistence anchor for downstream branch control.

## Open Follow-Up Questions

- which persistence claims remain strongest in modern reviews?
- how should this paper interact with newer cellular-immunity and vaccine-platform studies?
- how much of the persistence story still maps cleanly onto today's geographically distinct FCV populations?

## Linked Entities

- diseases: FCV
- models:
- endpoints: persistence, chronic carriage, vaccine limits
- mechanisms: immune escape, carrier state
- regulations:
