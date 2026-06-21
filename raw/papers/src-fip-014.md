---
id: src-fip-014
type: source
title: "Feline infectious peritonitis epizootic caused by a recombinant coronavirus"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2025
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, mechanism, recombinant, epizootic]
links:
  doi: ""
  url: "https://pubmed.ncbi.nlm.nih.gov/40633571/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source explicitly reports an FIP epizootic caused by a recombinant coronavirus.
    - The abstract reports a highly pathogenic FCoV-CCoV recombinant responsible for a rapidly spreading outbreak originating in Cyprus.
    - The abstract reports that the minor recombinant region spanning spike shows 96.5% sequence identity to pantropic canine coronavirus NA/09.
    - The abstract reports that a near-cat-specific deletion in spike domain 0 is present in more than 90% of cats with FIP, while its direct association with disease development remains unclear.
  source_supported_conclusion:
    - This source belongs in the branch that prevents mutation-origin logic from hardening into one overly simple emergence model.
    - This source supports a recombinant-emergence and direct-transmission branch inside the FIP mechanism architecture.
    - This source is best used to widen the mechanism model, not to replace it with a new single-cause story.
  llm_inference:
    - This paper may become one of the strongest later correctives against single-path mechanism stories.
    - This paper likely forces the module to separate ordinary endemic-background logic from outbreak-capable recombinant logic.
  # V2 enhanced fields
  study_design: "原始研究，报告由 FCoV-CCoV 重组冠状病毒引起的 FIP 流行病（源自塞浦路斯）"
  core_argument: "FIP 发病机制需要多于一条路径——重组冠状病毒可引起具有直接传播能力的暴发，经典的个体猫内突变模型不足以涵盖所有 FIP"
  implicit_premise: "假设一次流行病足以扩展机制分支；假设重组暴发逻辑与地方性多猫背景逻辑是互补而非替代关系"
  unexpected_finding: "各年龄猫均在暴发中感染——这挑战了 FIP 主要影响幼猫的预期"
  title_gap: "标题说重组冠状病毒引起的流行病，但真正发现是机制扩展：FIP 发病需要多条路径——经典个体猫内突变模型不足以涵盖所有 FIP，重组暴发可感染所有年龄猫"
  evidence_boundary: "一次流行病可能拓宽分支但不能确定其普遍性；不应将重组暴发逻辑作为所有 FIP 的默认模型"
---

# One-line Summary

Recent recombinant-coronavirus paper that widens the mechanism branch beyond a single classical emergence pathway.

## Why It Matters For FIP

- pressures overly simple mutation-origin narratives
- may materially broaden how the module handles pathobiogenesis and outbreak logic
- now serves as the first deep-extracted recombinant-epizootic anchor in the FIP module

## Key Findings

- abstract reports a highly pathogenic FCoV-CCoV recombinant behind a rapidly spreading outbreak
- sequence identities across districts are strongly supportive of direct transmission
- cats of all ages were infected during the outbreak
- a spike domain 0 deletion was present in more than 90% of cats with FIP
- receptor-binding and cell-tropism changes are implicated, but not yet settled as direct causal proof

## Recombinant-Epizootic Role

This source widens the mechanism branch beyond the classical individual-cat conversion story. It reports a highly pathogenic FCoV-CCoV recombinant responsible for a rapidly spreading outbreak originating in Cyprus. That makes the paper an outbreak-pressure source, not merely a recombinant footnote.

For the FIP wiki, the main architectural change is that mechanism needs more than one route. Earlier mutation-origin and 3c sources support an endemic-background model in which feline enteric coronavirus can become FIP-associated through mutation and altered tissue/systemic behavior. `src-fip-014` adds a different route: recombinant emergence with outbreak-capable direct transmission. The right conclusion is not that the classical model is wrong, but that it is incomplete if presented as exclusive.

The hard details should travel with their caveats. The minor recombinant region spanning spike shows 96.5% sequence identity to pantropic canine coronavirus NA/09. Samples from different districts support direct transmission, and cats of all ages were infected during the outbreak. A near-cat-specific deletion in spike domain 0 was present in more than 90% of cats with FIP. At the same time, the direct association of that deletion with disease development remains unclear, so the source should not be simplified into a new single-cause mutation story.

This card should sit in the mechanism overview as a distinct recombinant-outbreak lane. It should cross-link to mutation-origin, spread-boundary, and spike-diagnostic cards because it pressures all of them: spike changes can matter, recombination can matter, direct transmission can matter, and none of those facts automatically becomes a universal diagnostic shortcut.

The downstream teaching point is strong: FIP pathobiogenesis is a systems problem across viral evolution, host context, tissue tropism, and epidemiologic setting. This 2025 source forces that systems model to include rare but high-impact recombinant epizootic behavior.

## Limits / Caveats

- current card is deep-extracted at worksheet level, but still not full-text reviewed
- one epizootic paper may widen the branch without settling its prevalence or generality
- enriched spike-deletion signals should not be promoted into proven causality
- do not imply that recombinant-outbreak logic is the ordinary baseline for all FIP
- do not convert direct-transmission evidence into a claim that every FIP case is directly contagious in the same way

## Open Follow-up Questions

- how exceptional is the recombinant event?
- does this paper change the default mechanism narrative or only add an exception branch?
- how should outbreak-capable recombinant logic be separated from endemic multi-cat risk logic?
- which spike or receptor-binding findings are mechanistic hypotheses versus established disease drivers?

## Deep Extraction

- [src-fip-014 deep extraction round 1](../../system/indexes/src-fip-014-deep-extraction-round1.md)

## Linked Entities

- recombinant coronavirus
- epizootic
- pathobiogenesis
