---
id: src-fcv-016
type: source
title: "Distribution of the Feline Calicivirus Receptor Junctional Adhesion Molecule A in Feline Tissues"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [receptor distribution, tissue tropism]
jurisdictions: []
evidence_level: original-study
year: 2011
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, receptor, jam-a, tropism, pathology]
links:
  doi: "10.1177/0300985810375245"
  url: "https://journals.sagepub.com/doi/10.1177/0300985810375245"
  local_assets: []
evidence_policy:
  quoted_fact:
    - Feline JAM-A is a functional receptor for FCV.
    - fJAM-A was widely distributed in feline tissues and highly expressed on feline platelets.
  source_supported_conclusion:
    - This is the key receptor/tissue-distribution paper in the FCV seed set.
    - The paper supports using junctional-integrity disruption as a mechanism bridge for FCV lesion diversity.
  llm_inference:
    - This source should likely pair with ocular, enteric, and VS-FCV extension papers during deep extraction.
  # V2 enhanced fields
  study_design: "原始实验研究，使用多种猫组织样本，采用免疫组化和分子生物学技术检测猫结合粘附分子A（fJAM-A）表达分布"
  core_argument: "猫结合粘附分子A（fJAM-A）是猫杯状病毒（FCV）的功能性受体，其广泛分布于多种猫组织并在血小板上高表达，解释了FCV感染的广泛病变谱和组织嗜性"
  implicit_premise: "fJAM-A的组织分布模式与病毒的组织侵袭性和病变表现直接相关"
  title_gap: "标题关注fJAM-A在猫组织中的分布，但真正的发现是fJAM-A表达的广泛性和丰富性说明了FCV多样化病变机制的基础——为理解FCV的组织嗜性提供了重要机制支撑"
  evidence_boundary: "本研究未涉及fJAM-A受体与FCV感染致病性关系的动态变化，也未探讨受体阻断对临床治疗效果的影响"
  unexpected_finding: "fJAM-A不仅在预期的上皮组织中表达，还在猫血小板上高度表达，提示血小板可能在FCV感染中扮演未充分认识的角色"
---

# Distribution of the Feline Calicivirus Receptor Junctional Adhesion Molecule A in Feline Tissues

## One-Line Summary

Receptor-distribution paper linking feline JAM-A tissue expression to the wide lesion spectrum and tissue tropism of FCV infection.

## Why It Matters For FCV

- gives the module a concrete receptor-level mechanism anchor
- helps explain why FCV disease is not limited to one tissue compartment

## Key Findings

### quoted_fact

- Feline JAM-A is a functional receptor for FCV.
- fJAM-A was widely distributed in feline tissues and highly expressed on feline platelets.

### source_supported_conclusion

- fJAM-A was broadly distributed across epithelial and endothelial junctions.
- Expression was high on platelets and lower on peripheral blood leukocytes.
- FCV infection of epithelial monolayers redistributed fJAM-A to the cytosol.
- The source supports using receptor distribution as one bridge between FCV tropism and lesion diversity.

### llm_inference

- This source should anchor the receptor/tissue-tropism branch below broader mechanism pages.
- Its safest role is `JAM-A distribution and tropism support`, not `complete virulence explanation`.

## Deep Extraction Notes

### Unit 1: JAM-A gives the module a concrete receptor anchor

- core_claim: feline JAM-A is a functional receptor for FCV.
- hard_details: this is preserved as a quoted fact in the card.
- implication: mechanism pages can describe FCV entry and tropism with a named receptor rather than generic viral-entry language.
- boundary: receptor presence alone does not prove disease severity or pathotype.

### Unit 2: Tissue distribution supports broad tropism language

- core_claim: fJAM-A distribution across tissues helps explain why FCV is not limited to one tissue compartment.
- hard_details: fJAM-A was widely distributed and highly expressed on feline platelets.
- implication: lesion-diversity and systemic-disease discussions can use this card as a mechanistic bridge.
- boundary: the card should not be used as the sole explanation for VS-FCV severity.

### Unit 3: Junctional redistribution links entry to tissue effects

- core_claim: FCV infection can alter fJAM-A localisation in epithelial monolayers.
- hard_details: infection redistributed fJAM-A to the cytosol in the preserved source layer.
- implication: mechanism pages can connect receptor biology with junctional-integrity disruption language.
- boundary: downstream clinical claims still require pathology and disease-outcome sources.

## Claim-Evidence Structure

| Claim | Evidence in this card | Safe downstream use | Do not use for |
|---|---|---|---|
| JAM-A is an FCV receptor | quoted functional receptor statement | entry-mechanism overview | full pathogenesis closure |
| Tissue distribution is broad | widely distributed in feline tissues | tropism and lesion-diversity framing | exact tissue-risk prediction |
| Platelet expression is notable | high platelet expression | systemic-mechanism hypothesis context | proof of clinical thrombocytopathy |
| Infection affects receptor localisation | epithelial monolayer redistribution | junctional-integrity bridge | standalone VS-FCV mechanism |

## Write-Back Implications

- [mechanism overview](../../topics/fcv/mechanism-overview.md) should cite this as the receptor/tissue-distribution anchor.
- [current state dashboard](../../topics/fcv/current-state-dashboard.md) should keep receptor evidence separate from clinical syndrome hierarchy.
- [synthesis index](../../topics/fcv/synthesis-index.md) should pair this with ocular, enteric, and VS-FCV papers when discussing tropism.

## Limits / Caveats

- receptor distribution alone does not fully explain virulence differences
- the paper should not be overpromoted into a complete VS-FCV mechanism answer

## Open Follow-Up Questions

- how does receptor distribution intersect with ocular and systemic disease papers?
- are additional receptors or cofactors needed to explain highly virulent disease?

## Linked Entities

- diseases: FCV
- models:
- endpoints: receptor distribution, tissue tropism
- mechanisms: JAM-A, junctional integrity, pathogenesis
- regulations:
