---
id: src-hcm-076
type: source
title: "Left Atrioventricular Coupling Index in Feline Hypertrophic Cardiomyopathy: Association with Disease Severity and Arterial Thromboembolism"
source_kind: paper
species: feline
diseases: ['HCM']
models: ['clinical-study']
endpoints: ['remission']
evidence_level: original-study
year: 2026
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: bilingual_checked
tags: ['hcm', 'left', 'atrioventricular', 'coupling', 'index', 'hypertrophic', 'cardiomyopathy', 'association']
links:
  doi: "10.3390/vetsci13050491"
  url: "https://doi.org/10.3390/vetsci13050491"
  local_assets: []
abstract: "This retrospective cross-sectional study examined 91 cats stratified by ACVIM guidelines into healthy controls and varying stages of feline HCM including cats with arterial thromboembolism (FATE). The left atrioventricular coupling index (LACI-ED), defined as the ratio of left atrial (LA) end-diastolic volume to left ventricular (LV) end-diastolic volume, progressively increased with disease severity (p < 0.001) and correlated positively with LA size/volume (p < 0.01) and inversely with LV global longitudinal strain (GLS) (p < 0.01). ROC analysis for FATE detection showed limited discrimination with LACI-ED > 150% (AUC = 0.575; 95% CI 0.402–0.736), though elevated LACI-ED was significantly associated with higher odds of prevalent FATE (OR = 4.65; 95% CI: 1.405–29.215; p = 0.020). Pairwise ROC comparisons found no significant difference versus conventional echocardiographic parameters. The results suggest LACI-ED is a marker of disease severity in feline HCM but has limited utility for thromboembolic risk prediction."
methods_summary: "A retrospective, cross-sectional observational design including 91 cats categorized by ACVIM HCM stages: healthy controls (n=33), asymptomatic HCM stages B1 (n=14) and B2 (n=16), symptomatic HCM stage C (n=15), and cats with feline arterial thromboembolism (FATE) (n=13). Conventional and 2D speckle-tracking echocardiography were performed. LACI-ED was computed as the ratio of LA to LV end-diastolic volume. Statistical analyses included correlation testing, ROC curve analysis for FATE discrimination, odds ratio calculation for elevated LACI-ED, and pairwise comparisons of ROC areas with established echocardiographic indices."
evidence_policy:
  quoted_fact:
    - "Sample size: 91 cats (33 healthy controls, 14 B1, 16 B2, 15 stage C, 13 FATE)"
    - "LACI-ED increased with disease severity (p < 0.001)"
    - "Positive correlation between LACI-ED and LA size/volume (p < 0.01)"
    - "Inverse correlation between LACI-ED and LV GLS (p < 0.01)"
    - "ROC AUC for FATE detection using LACI-ED > 150%: 0.575 (95% CI: 0.402-0.736), sensitivity 46.2%, specificity 84.4%"
    - "Odds ratio for prevalent FATE with LACI-ED >150%: 4.65 (95% CI: 1.405-29.215), p = 0.020"
    - "No statistically significant difference in ROC area between LACI-ED and conventional echocardiographic parameters (p > 0.05)"
  source_supported_conclusion:
    - "LACI-ED reflects progressive remodeling correlating with feline HCM disease stage."
    - "Elevated LACI-ED is associated with increased odds of arterial thromboembolism but is not a reliable standalone predictor."
  llm_inference:
    - "LACI-ED could be incorporated as an adjunct structural parameter to assess disease severity in feline HCM clinics."
    - "Due to limited discriminative power for FATE, LACI-ED should be used cautiously and alongside other clinical assessments for thromboembolic risk."
  # V2 enhanced fields
  study_design: "回顾性横断面研究，91 只猫按 ACVIM 分期（健康对照 33、B1 14、B2 16、C 期 15、FATE 13），采用常规及斑点追踪超声心动图"
  core_argument: "LACI-ED 反映猫 HCM 疾病严重程度和心脏重塑进程，但对血栓栓塞事件的预测判别力有限，不能作为独立预测指标"
  implicit_premise: "假设横断面研究中 LACI-ED 与 FATE 的关联可以反映其作为临床预测指标的价值；假设回顾性分期与前瞻性评估具有同等准确性"
  unexpected_finding: "尽管 LACI-ED >150% 与 FATE 显著相关（OR=4.65, p=0.020），但其 ROC AUC 仅为 0.575（95% CI: 0.402-0.736），几乎等同于随机猜测"
  title_gap: "标题说 LACI-ED 与疾病严重程度和血栓栓塞相关，但真正发现是预测悖论：OR 4.65（显著）但 AUC 0.575（≈随机猜测）——强关联不等于好预测"
  evidence_boundary: "横断面设计无法确定 LACI-ED 变化是否先于临床事件；不能用于纵向预测；传统超声指标表现与 LACI-ED 无显著差异，因此新指标的增量价值有限"
---

# Left Atrioventricular Coupling Index in Feline Hypertrophic Cardiomyopathy: Association with Disease Severity and Arterial Thromboembolism

## Evidence-Depth Caveat

This card is based on complete publication text. It is deep-extracted as a clinical study.

## One-Line Summary

In 91 cats ranging from healthy to symptomatic HCM and FATE, LACI-ED progressively increased with disease severity (p < 0.001), correlated positively with LA size and inversely with LV GLS (p < 0.01), and while elevated LACI-ED (>150%) was associated with higher odds of FATE (OR = 4.65; p = 0.020), its diagnostic performance for thromboembolism was limited (AUC=0.575).

## Why It Matters For Feline ['HCM']

Hypertrophic cardiomyopathy is the most common cardiac disease in cats, often complicated by arterial thromboembolism, which carries high morbidity. LACI-ED combines left atrial and ventricular volumes into a single index reflecting cardiac remodeling and disease progression. This novel index may improve structural disease severity assessment beyond traditional parameters, guiding clinical management and prognosis, although its value in predicting thromboembolic risk remains uncertain and requires cautious interpretation.

## Key Findings

### quoted_fact

* The study included 91 cats: 33 healthy controls, 14 HCM stage B1 (asymptomatic), 16 HCM stage B2, 15 symptomatic HCM stage C, and 13 with arterial thromboembolism (FATE).
* LACI-ED rose progressively with HCM severity (p < 0.001), reaching the highest levels in symptomatic and FATE groups.
* LACI-ED correlated positively with left atrial size and volume (p < 0.01) and inversely with left ventricular global longitudinal strain (GLS) (p < 0.01).
* ROC curve analysis to identify FATE cases with LACI-ED > 150% showed low discriminatory ability: AUC = 0.575 (95% CI: 0.402–0.736), sensitivity 46.2%, specificity 84.4%.
* Cats with LACI-ED > 150% had significantly higher odds of prevalent FATE (OR = 4.65; 95% CI: 1.405–29.215; p = 0.020).
* Pairwise comparisons showed no significant difference in ROC curve areas between LACI-ED and conventional echocardiographic parameters (LA/Ao ratio, LA diameter, LV GLS; all p > 0.05).

### source_supported_conclusion

* LACI-ED is a reliable volumetric index reflecting left atrioventricular structural remodeling and disease progression in feline HCM.
* While increased LACI-ED associates with thromboembolic events, it lacks sufficient predictive accuracy to be used alone for risk stratification.
* Conventional echocardiographic markers perform similarly to LACI-ED in identifying cats with FATE.

### llm_inference

* Incorporation of LACI-ED into echocardiographic evaluation protocols may enhance assessment of structural cardiac changes in feline HCM.
* Given limited sensitivity and modest specificity for thromboembolism, LACI-ED should be complemented with additional clinical and echocardiographic risk factors for comprehensive FATE risk assessment.
* Prospective longitudinal studies are needed to validate LACI-ED’s prognostic utility and potential role in guiding therapeutic decisions.

## Study Design Details

### Cohort Summary

| Group              | Number of Cats (n) | Description                            |
|--------------------|--------------------|------------------------------------|
| Healthy Controls   | 33                 | No HCM, baseline normal controls  |
| HCM Stage B1       | 14                 | Asymptomatic, mild disease          |
| HCM Stage B2       | 16                 | Asymptomatic, more advanced disease |
| HCM Stage C        | 15                 | Symptomatic HCM                    |
| FATE (Thromboembolism) | 13              | Cats with acute arterial thromboembolism |

- Echocardiographic assessments included conventional 2D and speckle-tracking measurements.
- LACI-ED computed as (LA end-diastolic volume) / (LV end-diastolic volume).
- Statistical analyses involved correlations, ROC curves, odds ratios, and pairwise comparisons of discriminative test performance.

## Linked Entities

- diseases: ['HCM']
- models: ['clinical-study']
- endpoints: ['remission']
- mechanisms: ['left atrioventricular structural remodeling', 'left atrial enlargement', 'left ventricular systolic dysfunction', 'thromboembolism risk related to chamber remodeling']