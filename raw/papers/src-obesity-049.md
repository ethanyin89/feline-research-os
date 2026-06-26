---
id: src-obesity-049
type: source
title: "Association between Gut Microbiota and Metabolic Health and Obesity Status in Cats"
source_kind: paper
species: feline
diseases: [obesity]
models: [mho_muo_phenotyping, fecal_microbiota_analysis]
endpoints: [bifidobacteriaceae, coriobacteriaceae, veillonellaceae, ruminococcaceae, triglycerides, adiponectin, bmi]
jurisdictions: []
evidence_level: original-study
year: 2024
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: yes
language_qa_status: not_applicable
tags: [obesity, gut_microbiota, mho, muo, metabolic_health, candidate_association]
links:
  doi: "10.3390/ani14172524"
  url: "https://www.mdpi.com/2076-2615/14/17/2524"
  local_assets:
    - "../../raw/deep-extractions/ext-src-obesity-049.md"
evidence_policy:
  quoted_fact:
    - "The deep extraction describes NO n=10, MHO n=12, and MUO n=9 cats after obesity and metabolic-health grouping."
    - "MUO classification used triglyceride >165 mg/dL and adiponectin <1.53 μg/mL, while MHO met 0-1 of these criteria."
    - "Bifidobacteriaceae, Coriobacteriaceae, and Veillonellaceae were higher in obese cats and positively associated with BMI; Ruminococcaceae was higher in MUO and associated with lipid markers."
  source_supported_conclusion:
    - "This source can support a research-layer claim that feline obesity can be split into metabolic-health phenotypes for exploratory microbiota analysis."
    - "It supports limited candidate-family associations between obesity/metabolic indices and fecal microbiota."
    - "It supports a boundary claim that overall fecal microbiota structure was not strongly separated by NO/MHO/MUO status."
  llm_inference:
    - "Bacterial families should be presented as exploratory associations, not causal drivers or treatment targets."
    - "The MHO/MUO definition is study-specific and should not be treated as a validated feline clinical classification."
  study_design: "原始研究；客户拥有、室内、已绝育猫；NO/MHO/MUO 分组；结合 TG、脂联素、BCS/BMI 与粪便菌群分析。"
  core_argument: "猫肥胖和代谢不健康状态与少数粪便菌群家族存在关联，但整体菌群结构分离有限。"
  implicit_premise: "粪便菌群可作为肠道微生态的研究代理；MHO/MUO 的探索性定义足以用于研究分层，但尚不足以成为临床分型标准。"
  unexpected_finding: "Bifidobacteriaceae 在肥胖猫中升高，与常见人/鼠研究中将 Bifidobacterium 视为代谢保护信号的直觉不同。"
  title_gap: "标题说菌群、代谢健康和肥胖状态有关；真正重要的是关联很有限，最可用的是候选菌群家族和 MHO/MUO 分层边界。"
  evidence_boundary: "小样本、横断面、研究性分型；不能推出菌群因果、益生菌/饮食干预建议或临床诊断阈值。"
---

# Association between Gut Microbiota and Metabolic Health and Obesity Status in Cats

## Evidence-Depth Caveat

This card has been upgraded from abstract-weighted intake to a user-supplied full deep extraction. It is usable for exploratory microbiota and metabolic-phenotype architecture, not for clinical microbiome intervention claims.

The linked raw extraction is the passage owner:

- `raw/deep-extractions/ext-src-obesity-049.md`

## One-Line Summary

A small 2024 feline study split cats into NO, MHO, and MUO groups and found selected bacterial-family associations, while also concluding that obesity and MHO/MUO status had only limited impact on fecal microbiota overall.

## Key Findings

### quoted_fact

- The study grouped cats as NO n=10, MHO n=12, and MUO n=9.
- MUO was defined using TG >165 mg/dL and adiponectin <1.53 μg/mL.
- Bifidobacteriaceae, Coriobacteriaceae, and Veillonellaceae were associated with obese status and BMI.
- Ruminococcaceae was linked more closely to MUO and lipid markers.

### source_supported_conclusion

- This source supports obesity metabolic-phenotype content that goes beyond BCS alone.
- It supports cautious microbiota-family association claims.
- It supports the negative/boundary claim that group-level microbiota separation was not strong.

### llm_inference

- The source is useful beside `src-obesity-030` as part of an MHO/MUO research layer.
- It should not be used to recommend microbiome testing, probiotics, antibiotics, or diet changes.

## Claim-Fit Judgment

Strong use:

- exploratory MHO/MUO phenotyping
- gut microbiota association layer
- candidate bacterial-family signals
- explaining why evidence remains limited

Do not use for:

- microbiome-based obesity treatment
- validated diagnostic panels
- causal claims
- owner-facing feeding guidance

## Linked Entities

- diseases: obesity
- models: MHO/MUO phenotyping; fecal microbiota analysis
- endpoints: TG; adiponectin; BMI; Bifidobacteriaceae; Coriobacteriaceae; Veillonellaceae; Ruminococcaceae
- mechanisms: carbohydrate fermentation hypothesis; lipid-marker association; candidate ghrelin/acetate pathway
