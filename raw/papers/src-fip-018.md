---
id: src-fip-018
type: source
title: "Amino acid changes in the spike protein of feline coronavirus correlate with systemic spread of virus from the intestine and not with feline infectious peritonitis"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2014
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, mechanism, spike, systemic-spread]
links:
  doi: ""
  url: "https://link.springer.com/article/10.1186/1297-9716-45-49"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source explicitly states that spike-protein amino acid changes correlate with systemic spread from the intestine and not with FIP itself.
  source_supported_conclusion:
    - This source belongs at the center of the boundary between spread-correlate logic and direct FIP diagnostic overclaim.
    - This paper is best used to separate systemic-spread correlation from disease certainty.
    - The source gives the mutation branch an intermediate layer between origin and diagnostic utility.
    - Spike amino acid changes can be biologically meaningful while still falling short of direct disease definition.
  llm_inference:
    - This paper may become one of the most important supports for the mutation-diagnostics boundary branch.
  # V2 enhanced fields
  study_design: "原始研究，研究猫冠状病毒 spike 蛋白氨基酸变化与病毒从肠道系统传播的相关性"
  core_argument: "Spike 氨基酸变化与病毒从肠道的系统传播相关，而非与 FIP 疾病本身相关——系统传播和 FIP 疾病身份是相关但不相同的"
  implicit_premise: "假设分子信号可以追踪系统传播而非直接疾病定义；假设突变或氨基酸变化信号可以在生物学上有意义但仍不足以作为独立 FIP 标志物"
  unexpected_finding: "标题明确表述相关性不是与 FIP 本身——这为突变诊断边界提供了一个中间层"
  title_gap: "标题明确说「相关性不是与 FIP 本身」——这正是核心发现：Spike 氨基酸变化追踪的是系统传播而非疾病定义，分子信号可以生物学上有意义但仍不足以作为独立 FIP 诊断标志物"
  evidence_boundary: "传播相关性语言不应被转换为诊断认可或诊断否定本身；需要全文审查才能引用性能指标或采样规则"
---

# One-line Summary

Spike-change paper that likely sharpens the boundary between systemic spread and actual FIP disease.

## Why It Matters For FIP

- helps keep mechanism and diagnosis from collapsing into one mutation story
- likely one of the best current brakes on overinterpreting spike changes as direct disease certainty

## Key Findings

- title directly says spike changes correlate with systemic spread, not with FIP itself
- likely crucial for later diagnostic-boundary work

## Spread-Boundary Role

This paper draws one of the cleanest boundary lines in the FIP mutation cluster. The title states that spike-protein amino acid changes correlate with systemic spread from the intestine and not with FIP itself. That makes it more than a generic caution source. It tells the module what the molecular signal may actually be tracking.

The branch sequence should therefore be layered. `src-fip-009` supports mutation-origin from endemic enteric coronavirus background. `src-fip-004` refines enteric versus systemic competence through 3c. This source adds a spread-correlation layer. Only after that should `src-fip-022` and `src-fip-010` be used to discuss diagnostic utility and diagnostic limitation.

The safe compiled rule is: systemic spread and FIP disease identity are related but not identical. A mutation or amino-acid-change signal can matter biologically without becoming a standalone FIP marker. This source should be one of the main brakes on one-step mutation-test certainty.

For wiki reuse, this card should sit between pathogenesis and diagnostics rather than being forced into either box. The useful sequence is: enteric coronavirus background, emergence or mutation logic, systemic spread from the intestine, then clinical disease and diagnostic interpretation. By occupying the spread layer, this paper keeps the FIP mechanism page from implying that one mutation event automatically equals clinical FIP.

That placement also makes the diagnostic boundary clearer. A spike amino-acid-change signal may be biologically meaningful if it tracks systemic spread, but the source title explicitly says that the correlation is not with FIP itself. The future mutation-diagnostics memo should use this as the bridge between `src-fip-009` and `src-fip-004` on the mechanism side and `src-fip-022` plus `src-fip-010` on the diagnostic side. It is the paper that explains why a molecular signal can be real, relevant, and still insufficient.

The card should prompt specific extraction questions later: which compartments were sampled, how systemic spread was defined, whether enteric and systemic virus populations were compared, and whether diseased and non-diseased cats were both represented. Until those details are recovered, the source can safely support the boundary claim but not any numeric test-performance or sampling rule.

## Limits / Caveats

- current card is deep-extracted at worksheet level, but still not full-text reviewed
- title alone does not reveal how strong or context-dependent the correlation is
- do not quote performance metrics or sampling rules until full text is reviewed
- spread-correlation language should not be converted into either diagnostic endorsement or diagnostic dismissal by itself

## Open Follow-up Questions

- what exactly is the spread signal detecting?
- how should this paper be weighed against mutation-detection utility papers?
- what sample compartments were evaluated, and how should compartment context change the diagnostic workup memo?

## Deep Extraction

- [src-fip-018 deep extraction round 1](../../system/indexes/src-fip-018-deep-extraction-round1.md)

## Linked Entities

- spike protein
- systemic spread
- mutation testing
