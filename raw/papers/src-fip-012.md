---
id: src-fip-012
type: source
title: "Prevalence of feline infectious peritonitis in specific cat breeds"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2006
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, prevalence, breed, risk]
links:
  doi: ""
  url: "https://journals.sagepub.com/doi/10.1016/j.jfms.2005.04.003"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source explicitly studies prevalence of FIP in specific cat breeds.
  source_supported_conclusion:
    - This source belongs in the breed-structure branch of FIP risk architecture.
  llm_inference:
    - This paper may help keep breed effects from being overgeneralized into universal risk claims.
  # V2 enhanced fields
  study_design: "原始研究，研究特定猫品种的 FIP 患病率"
  core_argument: "品种可以塑造 FIP 验前怀疑和群体水平风险建模——但品种患病率不诊断个体猫的 FIP"
  implicit_premise: "假设品种是群体结构证据而非简单单基因因果声明；假设品种富集可能受繁殖实践、多猫环境或转诊行为混淆"
  evidence_boundary: "流行病学信号，不证明遗传因果关系；不能作为个体猫的诊断证据"
---

# One-line Summary

Breed-prevalence paper that likely strengthens the population-structure side of FIP risk modeling.

## Why It Matters For FIP

- adds breed-context to the risk branch
- helps separate genetic or population-structure signal from household exposure signal

## Key Findings

- title directly frames breed-specific prevalence
- likely useful for risk-context rather than for disease mechanism alone

## Breed-Risk Role

This paper should anchor the breed-prevalence sublayer of FIP risk architecture. The important move is to treat breed as population-structure evidence, not as a simple one-gene causal claim and not as a diagnostic shortcut. The title supports a bounded statement: FIP prevalence can be studied across specific cat breeds, and breed context belongs in the risk branch.

For wiki reuse, this card should be paired with `src-fip-005` rather than read alone. `src-fip-005` gives a broader Australian risk-factor frame with age, sex, and patterned breed over- or under-representation. This source gives the branch a more focused breed-prevalence anchor. Together they should support careful language: breed can shape pretest suspicion and population-level risk modeling, but it does not diagnose FIP in an individual cat.

The source also helps prevent overgeneralized `pedigree cat` wording. Breed-associated prevalence can be patterned, context-dependent, and partly confounded by breeding practices, multi-cat environments, referral behavior, or population composition. Until the full article is reviewed, the safest compiled rule is to keep breed risk visible but subordinate to the larger recognition stack: exposure ecology, age and signalment, clinicopathologic presentation, and bounded diagnostic support.

In the future FIP risk page, this card should become one row in a structured risk table rather than a standalone paragraph. The table should separate what the source can support from what it cannot: breed prevalence is a useful epidemiologic signal; it is not proof of inherited causation, not proof of disease in a given cat, and not a substitute for clinical workup.

This card should also keep the module from treating all host-side risk as the same. Age, sex, breed, neuter status, and environment can point in the same direction but they are not interchangeable. Breed-prevalence work is especially vulnerable to overinterpretation because readers may jump from breed enrichment to genetic determinism. The safer framing is population structure: breed labels can reflect heredity, breeding practices, shared environments, referral patterns, and sampling denominators.

When combined with `src-fip-008` and `src-fip-020`, this source helps build a three-part risk model. `src-fip-008` describes endemic multi-cat ecology. `src-fip-020` describes referral and diagnostic-laboratory enrichment. `src-fip-012` describes breed prevalence. `src-fip-005` then gives a broader signalment-risk study with age, sex, and patterned breed findings. The wiki should show these as complementary sublayers rather than one pooled list.

The immediate write-back target is therefore not mechanism. It is risk-and-recognition: breed context can raise pretest suspicion when other evidence fits, but it should stay below clinical form, clinicopathology, and source-specific diagnostic support.

That placement preserves the source's usefulness without turning breed into a shortcut or certainty claim.

## Limits / Caveats

- current card is title-led ingest, not full-text reviewed
- breed prevalence does not automatically imply simple inherited causation
- do not use breed prevalence as individual-cat diagnostic evidence
- do not assume the same breed ranking applies across countries or time periods without verification

## Deep Extraction

- [src-fip-012 deep extraction round 1](../../system/indexes/src-fip-012-deep-extraction-round1.md)

## Open Follow-up Questions

- which breeds are enriched most strongly?
- how much of the breed signal survives after environment is considered?
- what denominator population was used for breed prevalence?
- how should this source be reconciled with the breed signals in `src-fip-005` and referral patterns in `src-fip-020`?

## Linked Entities

- breed prevalence
- risk factors
- epidemiology
