---
id: src-ckd-010
type: source
title: "Histomorphometry of Feline Chronic Kidney Disease and Correlation With Markers of Renal Dysfunction"
source_kind: paper
species: feline
diseases: [CKD]
models: []
endpoints: [creatinine, phosphorus, proteinuria, systolic blood pressure, anaemia]
jurisdictions: []
evidence_level: original-study
year: 2012
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
citation_count: 155
impact_factor: 2.2
journal: "Veterinary Pathology"
metadata_enriched: 2026-06-16
language_qa_status: not_applicable
tags: [ckd, histomorphometry, renal-dysfunction, pathology]
links:
  doi: "10.1177/0300985812453176"
  url: "https://journals.sagepub.com/doi/10.1177/0300985812453176"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "A total of 80 cats with CKD were included in the study."
    - "Cats were recruited from 2 first-opinion practices in London between 1992 and 2010."
    - "CKD diagnosis required a plasma creatinine concentration >2.0 mg/dL plus history and clinical signs compatible with chronic kidney disease."
    - "Only cats with plasma biochemical data obtained within the last 2 months of life were included."
    - "Doppler systolic blood pressure was recorded as the mean of 5 readings taken at each visit."
    - "Hypertension was diagnosed when systolic blood pressure was >170 mm Hg on 2 consecutive visits or on 1 visit when hypertensive chorioretinopathy was present."
    - "All hypertensive cats were treated with amlodipine, initially at 0.625 mg/day, with dose escalation to 1.25 mg/day or occasionally 2.5 mg/day."
    - "Interstitial fibrosis was the lesion best correlated with the severity of azotemia, hyperphosphatemia, and anemia."
    - "Proteinuria was associated with interstitial fibrosis and glomerular hypertrophy."
    - "Higher time-averaged systolic blood pressure was associated with glomerulosclerosis and hyperplastic arteriolosclerosis."
  source_supported_conclusion:
    - This study is a primary bridge source linking naturally occurring feline CKD pathology to operational clinical markers rather than just describing lesions in isolation.
    - Interstitial fibrosis should remain the top mechanism anchor because it ties directly to azotemia, phosphorus burden, and anaemia severity.
    - Proteinuria and systolic blood pressure should be interpreted as structurally informative markers, not only as abstract staging variables.
    - Endpoint architecture should remain multi-axis because phosphorus, proteinuria, anaemia, and blood pressure map to different lesion patterns rather than one flat severity line.
    - The blood-pressure signal in this study is stronger than a casual one-visit correlation because the authors used repeated measurements and time-averaged SBP.
  llm_inference:
    - The vault should explicitly distinguish fibrosis-linked markers from glomerulo-vascular injury-linked markers when summarizing CKD consequence patterns.
    - Later treatment or outcome pages should avoid assuming that all pathology-linked endpoints are interchangeable simply because they all worsen in advanced disease.
  # V2 enhanced fields
  study_design: "回顾性尸检研究，80 只 CKD 猫（1992-2010 年伦敦两家诊所），死前 2 个月内有生化数据，肾脏组织定量形态学分析"
  core_argument: "不同临床标志物反映不同的肾脏病理损伤轴——间质纤维化与氮质血症/高磷/贫血相关，而蛋白尿和血压与肾小球硬化/血管病变相关"
  implicit_premise: "假设晚期疾病的尸检病理能够反映生前疾病进程的结构基础；假设时间平均血压比单次测量更准确反映血管损伤暴露"
  unexpected_finding: "蛋白尿同时与间质纤维化和肾小球肥大相关，而非仅与肾小球病变相关——这提示蛋白尿可能反映多轴损伤而非单一机制"
  title_gap: "标题说组织形态学与标志物相关性，但真正发现是多轴损伤映射：不同标志物反映不同病理轴——间质纤维化对应氮质血症/高磷/贫血，血压对应肾小球硬化/血管病变"
  evidence_boundary: "尸检设计无法建立因果方向或预测价值；所有高血压猫均接受氨氯地平治疗，无法观察未治疗的血压-病理关联；样本来自晚期疾病，不能直接推断早期筛查价值"
---

# Histomorphometry of Feline Chronic Kidney Disease and Correlation With Markers of Renal Dysfunction

## One-Line Summary

This primary study linked quantified renal lesions with clinical pathology and found interstitial fibrosis to be the lesion most strongly associated with azotemia, hyperphosphatemia, and anaemia in feline CKD, while proteinuria and time-averaged systolic blood pressure mapped to different structural lesion patterns.

## Why It Matters For CKD

This is one of the strongest candidate primary studies for bridging mechanism and endpoint layers.

## Key Findings

### quoted_fact

- The study included kidneys from 80 cats with plasma biochemical data from the last 2 months of life.
- Cats were recruited through 2 London first-opinion practices between 1992 and 2010.
- CKD cases were included only if they had plasma creatinine above 2.0 mg/dl plus history and clinical signs compatible with chronic kidney disease.
- Renal sections were scored semiquantitatively for glomerulosclerosis, interstitial inflammation, and fibrosis.
- The study also measured glomerular volume, the proportion of obsolescent glomeruli, hyperplastic arteriolosclerosis, and tubular mineralization.
- UPC values from cats with bacteriuria or gross hematuria were excluded.
- Systolic blood pressure was measured by Doppler as the mean of 5 readings per visit.
- Hypertension was diagnosed if blood pressure exceeded 170 mmHg on 2 consecutive visits or on 1 visit with hypertensive chorioretinopathy.
- All hypertensive cats were started on amlodipine therapy, beginning at 0.625 mg daily and increasing if needed.
- Time-averaged systolic blood pressure was used in analyses rather than the last blood pressure reading.
- Interstitial fibrosis was the lesion best correlated with severity of azotemia, hyperphosphatemia, and anaemia.
- Proteinuria was associated with interstitial fibrosis and glomerular hypertrophy.
- Higher time-averaged systolic blood pressure was associated with glomerulosclerosis and hyperplastic arteriolosclerosis.
- CKD cases were diagnosed using plasma creatinine above 2.0 mg/dl plus history and clinical signs consistent with chronic disease.

### source_supported_conclusion

- Interstitial fibrosis should be treated as a top-tier mechanism entity because it bridges structure and multiple clinically used markers.
- Proteinuria and systolic blood pressure are not just monitoring variables, they also map to structural pathology associations in this study.
- This paper supports a more differentiated reading of endpoints: phosphorus, proteinuria, anaemia, and blood pressure are not all reflecting the same lesion axis.
- The blood-pressure findings are stronger than a casual cross-sectional association because the study used repeated measurements and time-averaged SBP rather than a single visit value.
- This paper is a key anchor for connecting mechanism and endpoint layers without relying only on reviews.
- This source supports moving from “endpoint importance” to “endpoint consequence mapping,” because different markers align with different structural lesion patterns.

### llm_inference

- Hyperphosphatemia, anaemia, proteinuria, and blood pressure should probably be grouped as pathology-linked downstream indicators in the endpoint handbook.
- When the vault compares endpoints, it should explicitly distinguish fibrosis-linked markers from glomerulo-vascular injury-linked markers.
- Later outcome-architecture work should treat endpoint movement as multi-axis structural consequence, not one flat severity scale.

## Why The Methods Matter

This paper is more useful than a generic pathology description because the authors made the clinical measurement side harder to dismiss.

- Proteinuria values were filtered to exclude bacteriuria or gross haematuria confounding.
- Blood pressure was not reduced to a single late reading.
- The pathologist was masked to clinicopathological data.
- Lesions were quantified across multiple compartments rather than summarized impressionistically.

That means the endpoint-to-lesion links here are still bounded by a late-disease necropsy design, but they are materially stronger than a casual cross-sectional clinic note correlation.

## Structural Consequence Mapping

The main reusable contribution of this study is not just that common CKD markers "correlate with pathology."

It is that different markers appear to carry different structural meanings:

- interstitial fibrosis aligns most strongly with azotemia, hyperphosphatemia, and anaemia
- proteinuria carries a fibrosis plus glomerular-hypertrophy signal
- time-averaged systolic blood pressure carries a glomerulosclerosis and vascular-injury signal

This is why endpoint interpretation in feline CKD should not collapse into one undifferentiated severity score.

## Limits / Caveats

- This is a necropsy-linked late-disease cohort, so the paper should not be overread as an early-screening or intervention-prioritization study.
- The exact regression coefficients and comparative effect sizes are still not copied in full, so this source supports structural directionality more strongly than precise lesion-ranking magnitudes.
- Because hypertensive cats received amlodipine, the blood-pressure findings are clinically meaningful but still embedded in treated-disease context rather than untreated natural history.

## Open Follow-Up Questions

- Which lesion-marker correlations remained strongest in multivariable analysis beyond fibrosis?
- How should pathology-linked markers be ranked against practical screening markers?
- Which lesion-level findings from the full paper are most reusable for future entity cards such as glomerulosclerosis?

## Linked Entities

- diseases: CKD
- models:
- endpoints: creatinine, phosphorus, proteinuria, systolic blood pressure, anaemia
- mechanisms: renal fibrosis, glomerulosclerosis
- regulations:
