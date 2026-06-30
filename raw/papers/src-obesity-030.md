---
id: src-obesity-030
type: source
title: "Metabolic Profiles of Feline Obesity Revealed by Untargeted and Targeted Mass Spectrometry-Based Metabolomics Approaches"
source_kind: paper
species: feline
diseases: [obesity]
models: [metabolic_phenotyping, serum_metabolomics]
endpoints: [mho, muo, glycine, citrulline, triglycerides, lpc18_2, kynurenine, pls_da]
jurisdictions: []
evidence_level: original-study
year: 2025
status: deep_extracted
extraction_depth: partial
verification_status: deep_extracted
decision_grade: provisional
language_qa_status: not_applicable
tags: [obesity, metabolomics, metabolic_phenotyping, mho, muo, triglycerides, amino_acids]
links:
  doi: "10.3390/vetsci12080697"
  url: "https://www.mdpi.com/2306-7381/12/8/697"
  local_assets:
    - "../../raw/deep-extractions/ext-src-obesity-030.md"
evidence_policy:
  quoted_fact:
    - "The deep extraction describes 28 cats grouped as metabolically healthy normal-weight, metabolically healthy overweight/obese, and metabolically unhealthy overweight/obese."
    - "Targeted metabolomics identified 48 statistically significant metabolites; the MHO group already showed lower glycine, citrulline, PC(39:5), and PC(42:7) compared with MHN."
    - "Only kynurenine among the reported untargeted features reached MSI Level 1 identification in the deep extraction."
  source_supported_conclusion:
    - "This source can support a content-layer claim that body weight or BCS alone may miss early metabolic heterogeneity in feline obesity."
    - "It can support candidate-marker discussion around amino acids, lipid species, and triglyceride-heavy MUO separation."
    - "It should preserve the distinction between MHO and MUO, including the possibility that apparently metabolically healthy obesity may already carry subtle metabolic changes."
  llm_inference:
    - "Glycine, citrulline, kynurenine, LPC18:2, and triglyceride species are candidate signals for research interpretation, not validated clinical screening thresholds."
    - "PLS-DA separation should be framed cautiously because the permutation tests reported in the deep extraction do not establish a fully validated classifier."
  study_design: "原始研究；28 只猫；按 MHN、MHO、MUO 分组；使用非靶向 LC-MS、靶向 LC-MS 和 FIA-MS 分析血清代谢组。"
  core_argument: "猫肥胖存在代谢表型异质性；BCS/体重不足以覆盖氨基酸、脂质和色氨酸/犬尿氨酸相关信号的变化。"
  implicit_premise: "肥胖风险需要同时看体况、糖脂代谢、脂肪因子和代谢组，而不能把所有超重/肥胖猫视为同一风险层。"
  title_gap: "标题强调代谢组谱，真正可复用的内容层价值在于 MHO 与 MUO 的差异，以及 MHO 已出现候选代谢异常。"
  evidence_boundary: "小样本、横断面、候选标志物研究；不能把代谢物差异升级为诊断面板、预后模型或治疗建议。"
---

# Metabolic Profiles of Feline Obesity Revealed by Untargeted and Targeted Mass Spectrometry-Based Metabolomics Approaches

## Evidence-Depth Caveat

This card has been upgraded from abstract-weighted intake to a user-supplied full deep extraction. It can support research-content claims about feline obesity metabolic phenotyping, but only within the boundaries of a small metabolomics study.

The linked raw extraction is the current passage owner:

- `raw/deep-extractions/ext-src-obesity-030.md`

## One-Line Summary

Serum metabolomics separated metabolically healthy normal-weight, metabolically healthy overweight/obese, and metabolically unhealthy overweight/obese cats, showing that MHO cats may already have subtle amino-acid and lipid changes even before broad routine-chemistry abnormalities.

## Key Findings

### quoted_fact

- The study grouped 28 cats as MHN, MHO, or MUO.
- MHO cats had lower glycine, citrulline, PC(39:5), and PC(42:7) versus MHN cats in the targeted analysis.
- MUO cats showed broad triglyceride-heavy differences, while the untargeted feature list should not be treated as a list of confirmed metabolites because only kynurenine was described as MSI Level 1.

### source_supported_conclusion

- This source supports content about metabolic heterogeneity within feline obesity.
- It supports the claim that BCS and body weight are insufficient as the only research-level descriptors of obesity risk.
- It supports cautious discussion of candidate metabolic markers for future validation.

### llm_inference

- Glycine or citrulline changes can be used as risk-architecture signals, not diagnostic thresholds.
- PLS-DA outputs should be treated as exploratory because the deep extraction records non-significant permutation tests for the classification models.
- This source is best used alongside insulin-sensitivity and obesity-mechanism sources, not as a standalone clinical decision source.

## Claim-Fit Judgment

Strong use:

- metabolic phenotyping of obese cats
- MHO versus MUO distinction
- candidate biomarker architecture
- explaining why obesity modules should not rely only on BCS

Do not use for:

- clinical diagnosis of metabolic health
- validated prediction of diabetes progression
- owner-facing screening thresholds
- treatment recommendations

## Linked Entities

- diseases: obesity
- models: metabolic phenotyping; serum metabolomics
- endpoints: glycine; citrulline; triglyceride species; LPC18:2; kynurenine; adiponectin
- mechanisms: amino-acid metabolism; lipid remodeling; candidate tryptophan-kynurenine signal
