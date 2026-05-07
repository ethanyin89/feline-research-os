---
id: src-fcv-015
type: source
title: "Molecular Virology of Feline Calicivirus"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [pathogenesis, tissue tropism, replication]
jurisdictions: []
evidence_level: review
year: 2008
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, molecular-virology, review, pathogenesis, diversity]
links:
  doi: "10.1016/j.cvsm.2008.03.002"
  url: "https://www.sciencedirect.com/science/article/abs/pii/S0195561608000752?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Accessible abstract reports that FCVs demonstrate remarkable genetic, antigenic, and clinical diversity."
    - "Accessible abstract reports that outbreak vaccine-resistant strains occur frequently."
    - "Accessible article summary reports sections on host range, tissue tropism, receptors, and virus entry."
    - "Accessible article summary reports sections on genomic structure, genetic variability, translation, replication, capsid structure, and antigenic variation."
  source_supported_conclusion:
    - This is the core molecular-virology bridge in the FCV seed set.
    - The paper supports keeping diversity, tissue tropism, receptors, genomic structure, replication, and antigenic variation in one mechanism branch.
    - The paper supports linking molecular architecture to vaccine/control pressure rather than treating diversity as a side detail.
    - The paper supports a broader-than-respiratory FCV model that includes multiple clinical biotypes.
  llm_inference:
    - This source now serves as the first deep-extracted mechanism spine anchor in the FCV module.
    - The safest downstream wording is `diversity-first, tropism-aware mechanism-control spine`, not `simple respiratory virus`.
---

# Molecular Virology of Feline Calicivirus

## One-Line Summary

Mechanism-heavy FCV review connecting viral diversity, tissue tropism, genome architecture, replication, and capsid variation to clinical heterogeneity and vaccine/control pressure.

## Why It Matters For FCV

- gives the module a molecular bridge between clinical reviews and field epidemiology
- should stabilize the mechanism branch before extension papers fragment it
- now serves as the first FCV deep-extracted mechanism spine anchor

## Key Findings

### quoted_fact

- Accessible abstract reports FCV as a small, nonenveloped, positive-stranded RNA virus group model with high genetic, antigenic, and clinical diversity.
- Accessible abstract reports outbreak vaccine-resistant strains occur frequently.
- Accessible article summary reports sections on epidemiology, clinical disease, limping disease, lower respiratory tract disease, virulent systemic disease, and other biotypes.
- Accessible article summary reports sections on host range, tissue tropism, receptors, and virus entry.
- Accessible article summary reports sections on genomic structure, genetic variability, translation, replication, capsid structure, antigenic determinants, and antigenic variation.

### source_supported_conclusion

- This source is the current best FCV mechanism bridge for keeping diversity, tropism, replication, and antigenic variation in one frame.
- The paper supports a broader-than-URTD FCV model that can accommodate multiple clinical forms and tissue targets.
- The strongest safe read is that control difficulty is partly built into viral architecture rather than being only a field-management problem.

### llm_inference

- If the module later builds a dedicated mechanism or pathogenesis handbook, this card should anchor the opening hierarchy and anti-overcompression language.

## Limits / Caveats

- older review, so newer sequence and vaccine-platform work still matters
- current card is deep-extracted at worksheet level, but still not full-text reviewed section by section
- should not be used alone to represent current field prevalence or treatment efficacy

## Mechanism-Spine Logic

What can be promoted:

- FCV should be modeled as a diversity-first viral system
- receptor/tropism logic belongs inside the main mechanism branch
- genome/capsid/replication logic is relevant because it explains control pressure
- multiple clinical biotypes fit under the same molecular frame

What should be held:

- any current strain-by-strain virulence ranking
- any present-day field prevalence claim from this older review
- any claim that this review alone solves modern vaccine-platform questions

This card is therefore best reused as a mechanism-architecture source rather than as a current-state epidemiology source.

## Write-Back Implications

- [mechanism overview](../../topics/fcv/mechanism-overview.md) should treat this card as the opening molecular bridge rather than as one review among many.
- [FCV mechanism-control memo](../../system/indexes/fcv-mechanism-control-memo.md) can now lean more directly on diversity, tropism, replication, and capsid-variation language from this source.
- [current state dashboard](../../topics/fcv/current-state-dashboard.md) should treat the mechanism branch as having one deep-extracted spine anchor rather than only source-checked review support.

## Open Follow-Up Questions

- which mechanistic claims remain unchanged in the 2024 and 2025 updates?
- how strongly does the review separate classical FCV from VS-FCV pathogenesis?
- how should later receptor-distribution and cellular-immunity papers be layered under this broader mechanism frame?

## Linked Entities

- diseases: FCV
- models:
- endpoints: pathogenesis, tissue tropism, replication
- mechanisms: genome structure, receptors, diversity
- regulations:
