---
id: src-fip-002
type: source
title: "Changes in some acute phase protein and immunoglobulin concentrations in cats affected by feline infectious peritonitis or exposed to feline coronavirus infection"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2004
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, endpoint, acute-phase-protein, immunoglobulin]
links:
  doi: ""
  url: "https://www.sciencedirect.com/science/article/pii/S1090023303000558?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source explicitly studies acute phase protein and immunoglobulin concentration changes in cats with FIP or feline coronavirus exposure.
  source_supported_conclusion:
    - This source belongs in the supportive laboratory-marker branch rather than the definitive-diagnosis branch.
    - This source is best used as a bounded inflammatory/immunologic support anchor below clinicopathology.
  llm_inference:
    - This paper will likely help keep the FIP endpoint layer from collapsing into only mutation and clinicopathology logic.
    - The paper is most valuable when the case is already suspicious and needs richer laboratory context rather than a shortcut.
---

# One-line Summary

Laboratory-marker paper that anchors the acute phase protein / immunoglobulin support branch in FIP.

## Why It Matters For FIP

- provides non-mutation, non-clinicopathology laboratory support logic
- may help define what “supportive but non-definitive” biomarker evidence looks like in FIP
- now serves as the first deep-extracted acute-phase / immunoglobulin support anchor in the FIP module

## Key Findings

- title directly frames acute phase protein and immunoglobulin changes
- comparison includes cats with FIP and cats exposed to feline coronavirus infection
- best reused as supportive laboratory context rather than as a lead endpoint

## Supportive-Lab Role

This source gives the FIP endpoint layer a laboratory-support branch that is not simply clinicopathology and not simply mutation testing. The title is important because it compares cats affected by FIP with cats exposed to feline coronavirus infection. That makes the source more useful than a generic inflammatory-marker paper: the comparator is close to the real diagnostic problem, where coronavirus exposure is common but FIP disease is much narrower.

The practical wiki role is bounded strengthening. Acute phase protein and immunoglobulin changes can help contextualize a suspicious case, but this card should not lead the workup. It belongs after risk context and disease-form-aware clinicopathology, and beside other supportive channels such as effusion/CSF or mutation testing. The key teaching point is that FIP workup is layered: background exposure creates ambiguity, inflammatory and immune markers add context, and no single marker should be allowed to collapse the whole diagnostic problem.

This paper also improves endpoint architecture by preventing the module from becoming too sequence-centered. Mutation papers are compelling because they appear specific, but the real clinical workup also includes inflammatory burden, immune response, protein shifts, and conventional laboratory context. `src-fip-002` should therefore be used to create a named `acute phase / immunoglobulin support` row in the endpoint handbook.

The claim ceiling remains clear. Until full marker details are recovered, the card cannot say which acute phase proteins shift most, how well they discriminate FIP from exposure, or whether the changes are best for diagnosis, severity assessment, or monitoring. The safe promotion is architectural: this is a real support branch, it belongs below certainty language, and it helps distinguish disease burden from coronavirus exposure without becoming definitive.

The source should also be used to teach hierarchy inside laboratory evidence. Serology, acute phase proteins, immunoglobulins, mutation testing, and CSF viral detection should not be collapsed into one generic `lab tests` bucket. Each branch answers a different question and has a different overclaim risk. This card's question is inflammatory and immunologic context after exposure, not direct viral proof and not treatment response by itself.

In the compiled FIP endpoint page, this paper can sit between older serology (`src-fip-011`) and more targeted molecular or compartment testing (`src-fip-022`, `src-fip-023`). That position keeps the workup practical and layered.

## Limits / Caveats

- current card is deep-extracted at worksheet level, but still not full-text reviewed
- title alone does not determine how discriminative these markers actually are
- do not promote acute phase or immunoglobulin changes above clinicopathology-led suspicion
- do not infer marker-specific performance until the full article is reviewed

## Open Follow-up Questions

- which markers shift most strongly?
- are these changes useful for suspicion, monitoring, or both?
- how did the paper define coronavirus-exposed cats compared with FIP-affected cats?
- should this branch be grouped with effusion protein patterns or kept as systemic laboratory support?

## Deep Extraction

- [src-fip-002 deep extraction round 1](../../system/indexes/src-fip-002-deep-extraction-round1.md)

## Linked Entities

- acute phase proteins
- immunoglobulins
- diagnosis
