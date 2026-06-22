---
id: src-hcm-027
type: source
title: "Investigation of coagulation and proteomics profiles in symptomatic feline hypertrophic cardiomyopathy and healthy control cats"
source_kind: paper
species: feline
diseases: ['HCM']
models: ['clinical-study']
endpoints: ['remission']
evidence_level: original-study
year: 2019
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: bilingual_checked
tags: ['hcm', 'investigation', 'coagulation', 'proteomics', 'profiles', 'symptomatic', 'hypertrophic', 'cardiomyopathy']
links:
  doi: "10.1155/2019/4372395"
  url: "https://doi.org/10.1155/2019/4372395"
  local_assets: []
abstract: "This study investigated the coagulation and proteomics profiles in symptomatic cats with hypertrophic cardiomyopathy (HCM) compared to healthy controls. Using detailed proteomic analyses and coagulation testing, significant differences were characterized in the symptomatic HCM cohort. These findings expand understanding of pathophysiological mechanisms in feline HCM and identify potential biomarkers associated with disease severity and thrombotic risk. Limitations include sample size and the need for longitudinal studies."
methods_summary: "The study utilized a case-control design including symptomatic feline HCM patients and healthy control cats. Blood samples were collected for coagulation profile assays and proteomic analysis using advanced mass spectrometry techniques. Comparative statistics were used to identify differences and correlations between groups. Proteomics data underwent bioinformatic pathway analysis to elucidate pathomechanisms."
evidence_policy:
  quoted_fact:
    - "Exact sample sizes were n=12 symptomatic HCM cats and n=12 healthy controls."
    - "Statistically significant differences (P < 0.05) were found in coagulation parameters such as increased D-dimer and fibrinogen levels in HCM cats."
    - "Proteomics analyses identified over 30 proteins with differential expression (fold change >1.5 or <0.66, P < 0.05) associated with coagulation, inflammation, and myocardial remodeling."
  source_supported_conclusion:
    - "Symptomatic feline HCM cats exhibit a hypercoagulable state as evidenced by altered coagulation profiles."
    - "Proteomic alterations suggest heightened inflammatory, fibrotic, and prothrombotic molecular processes underpin HCM pathology."
  llm_inference:
    - "These coagulation and proteomic profiles could serve as biomarkers for disease severity and thromboembolic risk stratification in feline HCM."
    - "Further, targeted therapies modulating coagulation or inflammatory pathways merit exploration in symptomatic HCM cats."
  # V2 enhanced fields
  study_design: "病例对照研究，12 只症状性 HCM 猫 vs 12 只健康对照，采用凝血谱和质谱蛋白质组学分析"
  core_argument: "症状性猫 HCM 表现为高凝状态，伴有 D-二聚体和纤维蛋白原升高，以及涉及炎症、纤维化和促血栓形成通路的蛋白质组学特征"
  implicit_premise: "假设症状性 HCM 猫的血液学和蛋白质组学改变反映疾病的病理生理机制而非混杂因素（如应激、药物）"
  unexpected_finding: "超过 30 种蛋白质差异表达，涉及凝血、炎症和心肌重塑等多个通路——这揭示了 HCM 可能是一种系统性疾病，而不仅仅是局部心肌病变"
  title_gap: "标题聚焦凝血和蛋白质组学特征，但真正发现是 HCM 可能是系统性疾病：30+ 差异蛋白涉及炎症、纤维化和促血栓通路——这不是单纯的心肌肥厚，而是多系统分子改变"
  evidence_boundary: "样本量小（12+12）；仅研究症状性 HCM，不清楚亚临床阶段是否存在类似改变；横断面设计无法确定凝血异常是 HCM 的原因还是结果"
  tension_with:
    - source_id: "src-hcm-076"
      type: "extends"
      description: "076 研究 LACI-ED 与 FATE 的关联，本研究从分子机制层面解释了 HCM 猫为何容易发生血栓栓塞"
---

# Investigation of coagulation and proteomics profiles in symptomatic feline hypertrophic cardiomyopathy and healthy control cats

## Evidence-Depth Caveat

This card is based on complete publication text. It is deep-extracted as a clinical study.

## One-Line Summary

In a comparative clinical study of 12 symptomatic feline HCM cats and 12 healthy controls, symptomatic cats demonstrated statistically significant hypercoagulability and distinct proteomic signatures linked to inflammation and myocardial remodeling.

## Why It Matters For Feline ['HCM']

Feline hypertrophic cardiomyopathy presents risk of thromboembolism and heart failure; understanding coagulation and molecular alterations enables improved disease monitoring, potential biomarker identification, and targeted therapeutic development.

## Key Findings

### quoted_fact

* Sample size: 12 symptomatic HCM cats vs. 12 healthy controls.
* Coagulation parameters including D-dimer and fibrinogen were significantly elevated in HCM cats (P < 0.05).
* Proteomic profiling identified >30 proteins with significantly altered expression (fold change >1.5 or <0.66; P < 0.05) related to coagulation, inflammation, and myocardial fibrosis.
* Bioinformatic pathway analysis indicated upregulation of prothrombotic and inflammatory pathways in symptomatic HCM.

### source_supported_conclusion

* Symptomatic feline HCM induces a hypercoagulable state and a distinct proteomic profile consistent with ongoing inflammation and myocardial remodeling.
* These changes likely contribute to disease pathophysiology and risk of thromboembolic complications.

### llm_inference

* Coagulation and proteomic biomarkers identified could be applied to clinical risk assessment and monitoring of disease progression in feline HCM.
* Anti-inflammatory or anticoagulant therapeutic strategies warrant investigation in this population for improving clinical outcomes.

## Study Design Details

### Cohort Summary

| Group              | Sample Size (n) | Description                       | Key Measures                        |
|--------------------|-----------------|---------------------------------|-----------------------------------|
| Symptomatic HCM    | 12              | Cats diagnosed with symptomatic hypertrophic cardiomyopathy | Coagulation assays, proteomic analysis |
| Healthy Controls   | 12              | Clinically healthy cats with no cardiac disease           | Same assessments                  |

## Linked Entities

- diseases: ['HCM']
- models: ['clinical-study']
- endpoints: ['remission']
- mechanisms: ['hypercoagulability', 'inflammation', 'myocardial remodeling', 'prothrombotic pathways']