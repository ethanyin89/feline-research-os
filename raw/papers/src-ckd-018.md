---
id: src-ckd-018
type: source
title: "Early detection of feline chronic kidney disease via 3-hydroxykynurenine and machine learning"
source_kind: paper
species: feline
diseases: [CKD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2025
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ckd, early-detection, biomarker, machine-learning, 3-hydroxykynurenine]
links:
  doi: "10.1038/s41598-025-90019-x"
  url: "https://pubmed.ncbi.nlm.nih.gov/40011503/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The baseline study population consisted of 61 healthy cats, and 63 cats with CKD IRIS stage 2 (CKD2)."
    - "The longitudinal population of initially healthy cats counted 26 cats remaining healthy and 22 cats developing CKD2."
    - "The serum-to-urine ratio of 3-hydroxykynurenine was identified as a single biomarker candidate, yielding a high AUC (0.844) and accuracy (0.804)."
    - "Linear support vector machine-based modelling employing metabolites and clinical parameters enhanced AUC (0.929) and accuracy (0.862) six months before traditional diagnosis."
    - "S/U 3-hydroxykynurenine was confirmed as the best potential individual biomarker for early CKD."
    - "SDMA was only identified as the 14th most predictive individual metabolite at T-6."
    - "The study also demonstrated poor sensitivity values for SDMA on T0, T-6 and T-12 (0.571, 0.350 and 0.400, respectively)."
    - "Only cats with CKD2 were included."
    - "It is not excluded that CKD2 cats from the longitudinal population might already have CKD1 at T-6, which could lead to overestimations of performance."
    - "The absence of GFR measurements and renal ultrasonography further restricted the ability to detect these potential CKD1 cats."
  source_supported_conclusion:
    - This is one of the strongest current sources in the vault for saying that metabolomics may improve earlier feline CKD recognition beyond routine single-marker logic.
    - The paper supports a bounded claim of earlier discrimination, roughly six months before traditional CKD2 diagnosis, not a claim of solved population screening.
    - S/U 3-hydroxykynurenine is the strongest individual candidate biomarker in this study, while multi-metabolite models outperform any single marker.
    - The study weakens any strong assumption that SDMA alone is the best early-detection solution, because SDMA performed modestly as an individual predictor in this dataset.
    - The machine-learning result is promising but still pre-routine because the work remains metabolomics-heavy, sample-limited, and focused on CKD2 rather than a fully characterized earliest-disease population.
  llm_inference:
    - This paper does not overturn the vault's serial-surveillance framing, but it does justify adding a new layer: emerging metabolomic classifiers may eventually augment serial surveillance rather than replace it.
    - The most defensible promotion path is from `serial surveillance only` to `serial surveillance plus emerging biomarker-panel augmentation`.
  # V2 enhanced fields
  study_design: "原始研究，使用代谢组学和机器学习在传统 CKD2 诊断前 6 个月识别早期 CKD"
  core_argument: "血清/尿液 3-羟基犬尿氨酸比值是最佳单一生物标志物候选（AUC 0.844）——多代谢物 ML 模型在 T-6 达到 AUC 0.929，比 SDMA 表现更好"
  implicit_premise: "假设 CKD2 是有意义的早期检测目标；假设代谢组学工作流可以转化为实际筛查"
  unexpected_finding: "SDMA 仅是 T-6 时第 14 位最具预测性的个体代谢物——这削弱了 SDMA 是最佳早期检测解决方案的假设"
  title_gap: "标题说 3-羟基犬尿氨酸和机器学习早期检测，但真正发现是 SDMA 的局限：SDMA 仅是第 14 位预测物——多代谢物模型在 T-6 达到 AUC 0.929"
  evidence_boundary: "研究环境中的早期区分，非常规筛查就绪；仅包括 CKD2 猫，缺乏 GFR 和肾脏超声"
---

# Early detection of feline chronic kidney disease via 3-hydroxykynurenine and machine learning

## One-Line Summary

This study identifies S/U 3-hydroxykynurenine as the strongest individual early-biomarker candidate in its dataset and shows that multi-metabolite machine-learning models can discriminate cats up to six months before traditional CKD2 diagnosis, but with important limits around stage definition, practicality, and routine clinical deployment.

## Why It Matters For CKD

This is one of the highest-value current sources for the early-detection and SDMA-adjacent question set because it directly tests whether newer biomarker-plus-model logic actually changes the current screening picture.

## Key Findings

### quoted_fact

- The baseline study population consisted of 61 healthy cats and 63 cats with CKD IRIS stage 2.
- The longitudinal population consisted of 26 cats remaining healthy and 22 cats developing CKD IRIS stage 2 within one year.
- The serum-to-urine ratio of 3-hydroxykynurenine yielded an AUC of 0.844 and accuracy of 0.804.
- Linear support vector machine-based modelling with metabolites and clinical parameters yielded an AUC of 0.929 and accuracy of 0.862 six months before traditional diagnosis.
- S/U 3-hydroxykynurenine was confirmed as the best individual biomarker candidate in this study.
- SDMA was only the 14th most predictive individual metabolite at T-6 in this dataset.
- The paper reported poor SDMA sensitivity values at T0, T-6, and T-12.
- Only CKD2 cats were included, not a fully characterized CKD1 discovery cohort.
- The absence of GFR measurements and renal ultrasonography limited the ability to identify possible earlier-stage CKD cats.

### source_supported_conclusion

- This paper is a major early-detection innovation source, but it supports `earlier discrimination in a research setting` more strongly than `routine screening readiness`.
- The strongest single-marker story here is not SDMA, but S/U 3-hydroxykynurenine.
- The strongest overall performance comes from multi-metabolite modelling, not from a one-marker shortcut.
- The paper adds real pressure against oversimplifying SDMA as the best early biomarker in every setting.
- The strongest promotion path from this study is `panel augmentation of serial surveillance`, not `routine replacement of the practical core`.

### llm_inference

- The vault should now say that serial surveillance remains the practical backbone, while metabolomic biomarker panels represent a plausible future augmentation layer.
- This source increases the importance of metabolomic and ML early-detection literature, but it does not yet justify a routine workflow rewrite.
- In outcome-architecture terms, this paper contributes a frontier signal more than a routine-ready endpoint package.

## Limits / Caveats

- The discovery/training population and the validation population were still relatively small.
- Only CKD2 cats were included, so the paper does not directly solve the true CKD1 identification problem.
- Some baseline CKD2 cats were allowed renal diet or CKD medication, which could influence metabolomic separation.
- The study lacked GFR and renal ultrasonography for detecting possible earlier-stage disease.
- The metabolomics workflow is still heavier than a routine first-line clinical workup.

## Open Follow-Up Questions

- Can 3-hydroxykynurenine or related panels be turned into simpler assays suitable for routine screening?
- Does the performance hold in larger, multi-center, comorbidity-heavy clinical populations?
- How well does this approach separate CKD from hyperthyroidism and other common senior-cat confounders?
- Does the model still perform well when the target becomes CKD1 rather than future CKD2 diagnosis?

## Linked Entities

- diseases: CKD
- models: support vector machine, metabolomic classifier
- endpoints: 3-hydroxykynurenine, SDMA, creatinine, USG, GFR
- mechanisms:
- regulations:
