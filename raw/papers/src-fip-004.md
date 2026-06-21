---
id: src-fip-004
type: source
title: "Feline infectious peritonitis: insights into feline coronavirus pathobiogenesis and epidemiology based on genetic analysis of the viral 3c gene"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2009
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, mechanism, 3c-gene, pathobiogenesis]
links:
  doi: ""
  url: "https://www.microbiologyresearch.org/content/journal/jgv/10.1099/vir.0.016485-0"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source explicitly connects FIP pathobiogenesis and epidemiology to genetic analysis of the viral 3c gene.
    - The abstract reports analysis of the 3c gene in 27 FECV- and 28 FIPV-infected cats.
    - The abstract reports that functional 3c is crucial for gut replication of FECV but dispensable for systemic FIPV replication.
    - The abstract reports that the 3c gene was mutated in 71.4% of FIPVs but not in all, implying that 3c mutation is not the single cause of FIP.
  source_supported_conclusion:
    - This source belongs in the mechanism branch as a post-mutation-origin refinement source.
    - This source helps define a functional split between enteric gut competence and systemic disease competence.
    - This source supports using outbreak rarity as a mechanism consequence rather than a separate epidemiologic footnote.
    - The source blocks single-mutation simplification: 3c mutation is important but not sufficient as a total FIP explanation.
    - Intestinal and systemic viral findings should be kept compartment-specific in the mechanism map.
  llm_inference:
    - This paper likely helps bridge classical mutation-origin logic and more specific genetic pathobiogenesis logic.
    - This paper is one of the strongest candidates for keeping the mechanism branch from collapsing into a flat mutation story.
  # V2 enhanced fields
  study_design: "原始研究，27 只 FECV 感染猫和 28 只 FIPV 感染猫的 3c 基因分析"
  core_argument: "功能性 3c 基因对肠道 FECV 复制至关重要，但对全身性 FIPV 复制是可有可无的——这解释了为什么 FIP 爆发少见"
  implicit_premise: "假设 3c 基因功能状态是区分肠道能力和全身疾病能力的关键因素；假设样本量足以支持这些结论"
  unexpected_finding: "71.4% 的 FIPV 携带 3c 突变，但不是全部——这明确阻止了「单一突变导致 FIP」的简化叙事"
  title_gap: "标题说 3c 基因和发病机制，但真正发现是功能分离：3c 对肠道复制至关重要但对全身性 FIPV 是可有可无的——这解释了为什么 FIP 暴发少见，同时阻止单一突变简化叙事"
  evidence_boundary: "机制相关性不能直接转化为诊断工作流；肠道与全身病毒检测应保持区室特异性"
---

# One-line Summary

3c-gene paper that refines the mutation/pathobiogenesis branch beyond the classical origin model.

## Why It Matters For FIP

- adds a more specific genetic layer to mechanism interpretation
- may help explain why FIP emergence and epidemiology cannot be reduced to one flat mutation story
- now serves as the first deep-extracted 3c/pathobiogenesis anchor in the FIP module

## Key Findings

- abstract reports intact 3c in all FECVs and mutated 3c in the majority of FIPVs
- functional 3c appears crucial for gut replication but dispensable for systemic FIPV replication
- most cats with FIP had no detectable intestinal FCoV
- when intestinal FCoV was detected, it had intact 3c and appeared to reflect FECV superinfection
- poor gut replication of 3c-inactivated viruses helps explain why FIP outbreaks are uncommon

## Mechanism-Refinement Role

This paper deepens the mutation-origin branch by adding functional biology. The key distinction is not just that mutations occur; it is that enteric replication competence and systemic FIPV replication can require different viral functions. The abstract reports analysis of 3c in 27 FECV-infected and 28 FIPV-infected cats, with functional 3c crucial for gut replication of FECV and dispensable for systemic FIPV replication.

That makes this source the bridge between the classical mutation-origin paper and later spread/diagnostic-limit papers. It explains why FIP should not be compressed into a flat mutation story. Intact 3c supports gut competence; 3c disruption is common in FIPV; but not all FIPVs carry 3c mutation. That last point is essential because it blocks single-cause and one-marker claims.

The epidemiology point is also reusable. Poor gut replication of 3c-inactivated viruses helps explain why FIP outbreaks are uncommon. In other words, a virus can be systemically dangerous while being poor at intestinal spread. That turns outbreak rarity into a mechanism consequence, not merely an epidemiology footnote.

The safe compiled rule is: 3c helps split enteric background from systemic disease, but it does not by itself explain all FIP, diagnose all FIP, or collapse intestinal and systemic viral compartments into one linear trajectory.

## Limits / Caveats

- current card is deep-extracted at worksheet level, but still not full-text reviewed
- 3c is important but explicitly not sufficient as a single-cause explanation
- mechanism relevance does not justify diagnostic shortcut language
- do not treat intestinal FCoV detection as a direct mirror of systemic FIPV without compartment context
- full-text review is needed before promoting exact sampling or sequencing workflow claims

## Open Follow-up Questions

- how should the 3c branch be positioned relative to later spike/spread papers?
- how much of the outbreak-rarity interpretation should be promoted into higher-level synthesis?
- where should 3c sit relative to `systemic spread` versus `FIP diagnosis` in endpoint pages?

## Deep Extraction

- [src-fip-004 deep extraction round 1](../../system/indexes/src-fip-004-deep-extraction-round1.md)

## Linked Entities

- 3c gene
- pathobiogenesis
- mutation
