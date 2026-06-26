---
id: src-obesity-066
type: source
title: "The effect of obesity and subsequent weight reduction on cardiac morphology and function in cats"
source_kind: paper
species: feline
diseases: [obesity]
models: [prospective_observational_weight_reduction, echocardiography, dexa]
endpoints: [left_ventricular_wall_thickness, diastolic_function, sbp, nt_probnp, hs_ctni, hrv, fat_mass]
jurisdictions: []
evidence_level: original-study
year: 2024
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: yes
language_qa_status: not_applicable
tags: [obesity, cardiac_morphology, echocardiography, weight_reduction, hcm_boundary]
links:
  doi: "10.1186/s12917-024-04011-0"
  url: "https://bmcvetres.biomedcentral.com/articles/10.1186/s12917-024-04011-0"
  local_assets:
    - "../../raw/deep-extractions/ext-src-obesity-066.md"
evidence_policy:
  quoted_fact:
    - "The deep extraction describes 20 obese domestic shorthair cats, with 11 reaching the weight-reduction target and completing repeat cardiovascular assessment."
    - "At baseline, 11/20 cats had at least one maximal end-diastolic IVS or LV free-wall thickness >=6.0 mm, and 15/19 had abnormal diastolic function classification."
    - "After weight reduction, excluding one cat considered to have progressed to primary HCM, LVFWd changed by -0.85 mm (P=0.019) and IVSd by -0.5 mm (P=0.047)."
  source_supported_conclusion:
    - "This source supports a claim that obesity can confound feline cardiac morphology interpretation, especially HCM-like wall thickness."
    - "It supports cautious discussion of partial reversibility of obesity-associated wall-thickness changes after controlled weight reduction."
    - "It supports separating echocardiographic morphology signals from blood pressure, HRV, and biomarker signals."
  llm_inference:
    - "Obesity should be treated as a potential HCM phenocopy or phenotype modifier, not as proven HCM causation."
    - "Weight reduction findings should be framed as prospective observational evidence with small-sample and no-control limitations."
  study_design: "前瞻性观察研究；20 只临床肥胖家短猫；11 只完成目标减重和重复心血管评估；使用 DEXA、超声心动图、SBP、心脏标志物和 HRV。"
  core_argument: "肥胖猫常见左室壁厚增加和舒张功能异常；成功减重后壁厚下降，提示肥胖相关心脏重构可能部分可逆，但证据仍受小样本和 HCM 混杂限制。"
  implicit_premise: "如果减重后壁厚下降，肥胖或减重相关管理可能参与心肌形态改变；但需要把潜在 HCM、饮食改变和测量变异作为竞争解释保留。"
  unexpected_finding: "肥胖猫的主要阳性信号不是普遍高血压、NT-proBNP 升高或 hs-cTnI 升高，而是超声壁厚和舒张功能异常。"
  title_gap: "标题说肥胖和减重影响心脏形态功能；真正值得用的是它给 HCM 判读提供了肥胖混杂边界。"
  evidence_boundary: "样本量小、无稳定体重对照、未多重校正、1 只猫疑似原发 HCM；不能证明肥胖导致 HCM，也不能建立筛查或治疗指南。"
---

# The effect of obesity and subsequent weight reduction on cardiac morphology and function in cats

## Evidence-Depth Caveat

This card has been upgraded from abstract-weighted intake to a user-supplied full deep extraction. It supports bounded claims about obesity-associated cardiac morphology and HCM diagnostic confounding, not broad cardiology guidance.

The linked raw extraction is the passage owner:

- `raw/deep-extractions/ext-src-obesity-066.md`

## One-Line Summary

In 20 obese cats, LV wall thickening and diastolic dysfunction were common despite mostly normal blood pressure and biomarkers; among cats completing weight reduction, LV wall thickness decreased, but the evidence remains small and observational.

## Key Findings

### quoted_fact

- 20 obese domestic shorthair cats were enrolled; 11 reached the weight-reduction target.
- Baseline LV wall thickness >=6.0 mm appeared in 11/20 cats.
- Baseline diastolic function was abnormal in 15/19 classifiable cats.
- After weight reduction, LVFWd and IVSd decreased in the analyzed group after excluding one suspected primary HCM progression case.

### source_supported_conclusion

- This source supports a cardiac-morphology branch in feline obesity.
- It supports clinical caution that obesity may mimic or modify HCM-like echocardiographic findings.
- It supports partial reversibility framing for wall-thickness changes after successful weight reduction.

### llm_inference

- In content outputs, the safest framing is diagnostic confounder and phenotype modifier, not direct HCM causation.
- The cardiac signal should be paired with limitations: no control group, small completion sample, diet changes, and possible HCM.

## Claim-Fit Judgment

Strong use:

- obesity cardiac morphology
- HCM phenocopy / diagnostic confounding
- weight-reduction follow-up evidence
- tissue/morphology versus biomarker distinction

Do not use for:

- HCM causation
- screening thresholds
- cardiology treatment recommendations
- proof that weight loss reverses all cardiac dysfunction

## Linked Entities

- diseases: obesity
- models: prospective observational weight reduction; echocardiography; DEXA
- endpoints: LVWT; IVSd; LVFWd; diastolic function; SBP; NT-proBNP; hs-cTnI; HRV
- mechanisms: obesity-related remodeling; metabolic/fat-associated myocardial change; HCM diagnostic confounding
