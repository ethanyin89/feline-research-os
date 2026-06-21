---
id: src-ckd-044
type: source
title: "Serum concentration of homocysteine in spontaneous feline chronic kidney disease"
source_kind: paper
species: feline
diseases: ['CKD']
models: ['clinical-study']
endpoints: ['remission']
evidence_level: original-study
year: 2019
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: yes
language_qa_status: bilingual_checked
tags: ['ckd', 'serum', 'concentration', 'homocysteine', 'spontaneous']
links:
  doi: "10.1016/j.tvjl.2019.105358"
  url: "https://doi.org/10.1016/j.tvjl.2019.105358"
  local_assets: []
abstract: "This study validated an enzymatic method for measuring serum homocysteine (Hcy) in cats and investigated its association with chronic kidney disease (CKD). A total of 36 cats (17 healthy but at risk of CKD and 19 with CKD) were monitored over 6 months with 63 serum samples. CKD cats had significantly higher Hcy levels (P=0.005), and Hcy correlated moderately with serum creatinine (r=0.51, P<0.0001) and weakly with proteinuria (r=0.26, P=0.045). Homocysteine was higher in moderate-severe CKD than mild CKD (P=0.002) and was not associated with hypertension. Furthermore, cats that developed CKD had higher Hcy at enrollment (P=0.046), suggesting HHcy may predict progression. The enzymatic assay showed good precision (intra-assay CV 3.1-6.7%, inter-assay CV 11.6-12.5%) and accuracy (recovery ~97%)."
methods_summary: "A prospective clinical study with 36 cats divided into healthy at-risk (n=17) and CKD groups (n=19) over 6 months. An enzymatic assay for serum Hcy was validated with coefficients of variation and recovery tests. Serum Hcy concentrations were compared between groups and correlated with serum creatinine, proteinuria (urinary protein to creatinine ratio), and blood pressure. Statistical analysis assessed significance of differences and correlations (P values, r coefficients). Disease progression was evaluated by comparing baseline Hcy in cats that developed CKD during follow-up versus those remaining stable."
evidence_policy:
  quoted_fact:
    - "Sample size: 36 cats total; 17 healthy at risk and 19 with CKD; total 63 samples over 6 months."
    - "Enzymatic assay intra-assay CV: 3.1-6.7%, inter-assay CV: 11.6-12.5%, recovery rate ~96.9±5.4%."
    - "CKD cats had significantly higher serum Hcy than at-risk cats (P=0.005)."
    - "Hcy concentration higher in moderate-severe CKD than mild CKD (P=0.002)."
    - "Moderate correlation between Hcy and serum creatinine (r=0.51, P<0.0001)."
    - "Weak correlation between Hcy and urinary protein to creatinine ratio (r=0.26, P=0.045)."
    - "No association found between homocysteine and hypertension."
    - "Cats that developed CKD had significantly higher baseline Hcy compared to stable cats (P=0.046)."
  source_supported_conclusion:
    - "Serum homocysteine concentrations increase with CKD severity in cats."
    - "Hyperhomocysteinemia (HHcy) is common in advanced feline CKD."
    - "Hcy levels moderately correlate with kidney function markers and weakly with proteinuria."
    - "Elevated homocysteine at baseline may predict progression to CKD."
    - "The enzymatic assay for feline serum Hcy is precise and accurate."
  llm_inference:
    - "Regular measurement of serum homocysteine might be valuable for early identification of cats at risk for CKD progression."
    - "Interventions targeting reduction of homocysteine could potentially modify CKD progression, pending further studies."
    - "Homocysteine is unlikely to be useful as a marker for CKD-associated hypertension in cats."
  # V2 enhanced fields
  study_design: "原始研究，36 只猫（17 只有风险健康猫和 19 只 CKD 猫）6 个月内的血清同型半胱氨酸研究"
  core_argument: "CKD 猫血清同型半胱氨酸显著升高（P=0.005）并与肌酐中度相关（r=0.51）——基线高 Hcy 可能预测 CKD 进展（P=0.046）"
  implicit_premise: "假设酶法检测（CV 3.1-6.7%）足够精确用于临床研究；假设相关性不证明因果关系"
  unexpected_finding: "同型半胱氨酸与高血压无关联——这限制了其作为 CKD 相关高血压标志物的用途"
  title_gap: "标题说 CKD 猫血清同型半胱氨酸，但真正发现是预测能力的分裂：Hcy 可预测 CKD 进展（P=0.046）但与高血压无关联——作为生物标志物有选择性价值而非通用价值"
  evidence_boundary: "36 只猫的前瞻性研究；可支持生物标志物探索但不能建立治疗建议；需要更大队列验证"
---

# Serum concentration of homocysteine in spontaneous feline chronic kidney disease

## Evidence-Depth Caveat

This card is based on complete publication text and represents a deep-extracted clinical study in spontaneous feline CKD.

## One-Line Summary

In a cohort of 36 cats, serum homocysteine was significantly elevated in CKD cats (P=0.005), correlated moderately with creatinine (r=0.51, P<0.0001), increased with CKD severity and proteinuria, and predicted disease progression (P=0.046) over 6 months.

## Why It Matters For Feline ['CKD']

Hyperhomocysteinemia may serve as a prognostic biomarker for CKD progression in cats, offering a new avenue for early intervention and monitoring in feline nephrology, supported by a validated enzymatic assay for serum measurement.

## Key Findings

### quoted_fact

* Enzymatic assay demonstrated good precision: intra-assay CV 3.1–6.7%, inter-assay CV 11.6–12.5%, recovery 96.9±5.4%.
* 36 cats studied: 17 healthy but at risk, 19 with CKD; 63 serum samples collected longitudinally over 6 months.
* Cats with CKD had significantly higher serum homocysteine than at-risk cats (P=0.005).
* Homocysteine concentration was significantly greater in moderate-severe CKD versus mild CKD (P=0.002).
* Moderate positive correlation between serum homocysteine and creatinine (r=0.51, P<0.0001).
* Weak positive correlation between homocysteine and urinary protein:creatinine ratio (r=0.26, P=0.045).
* No significant association between homocysteine levels and arterial hypertension.
* At baseline, cats that developed CKD had higher homocysteine than cats that remained stable (P=0.046).

### source_supported_conclusion

* Serum hyperhomocysteinemia is common in feline CKD, especially in advanced stages.
* Elevated serum homocysteine correlates with kidney dysfunction markers and proteinuria severity but not hypertension.
* Baseline homocysteine may serve as a biomarker for predicting CKD progression in cats.
* The enzymatic method used provides a reliable clinical tool for homocysteine measurement in feline serum.

### llm_inference

* Measurement of serum homocysteine could be incorporated into clinical monitoring protocols for cats at risk or diagnosed with CKD.
* Therapeutic strategies targeting reduction of homocysteine levels might be explored as potential modifiers of feline CKD progression.
* Given the lack of association with hypertension, Hcy modulation might not impact CKD-related hypertensive complications.
* Further longitudinal studies with larger cohorts are warranted to validate homocysteine’s predictive power and therapeutic relevance.

## Study Design Details

### Cohort Summary

| Group                     | n  | Description                          | Sampling Length | Key Findings                        |
|---------------------------|----|------------------------------------|-----------------|-----------------------------------|
| Healthy cats at risk of CKD | 17 | Cats without CKD but at potential risk | 6 months        | Lower baseline Hcy; some developed CKD during follow-up |
| Cats with CKD             | 19 | Diagnosed with varying stages of CKD | 6 months        | Elevated Hcy correlated with CKD severity |

- Total samples collected = 63 (multiple samples per cat over study duration)
- CKD severity stratified as mild vs moderate-severe based on clinical criteria
- Outcomes assessed: serum homocysteine concentration, serum creatinine, proteinuria (urinary protein:creatinine ratio), hypertension status, disease progression

## Linked Entities

- diseases: ['CKD']
- models: ['clinical-study']
- endpoints: ['remission']
- mechanisms: ['hyperhomocysteinemia', 'renal function impairment', 'proteinuria', 'disease progression']