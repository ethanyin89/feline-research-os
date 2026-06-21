---
id: src-ckd-009
type: source
title: "Feline comorbidities: The intermingled relationship between chronic kidney disease and hypertension"
source_kind: paper
species: feline
diseases: [CKD]
models: []
endpoints: [blood-pressure]
jurisdictions: []
evidence_level: review
year: 2021
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ckd, hypertension, comorbidity]
links:
  doi: "10.1177/1098612X211037872"
  url: "https://journals.sagepub.com/doi/10.1177/1098612X211037872"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The prevalence of hypertension in cats with chronic kidney disease has been reported to range from approximately 20% to 65%, depending on the population studied and the definition used."
    - "Current guidelines recommend a target systolic blood pressure of <160 mmHg to minimise the risk of target organ damage."
    - "Hypertensive target organ damage affects the eye, brain, heart, and kidney."
    - "Hypertension increases proteinuria, and proteinuria is an independent risk factor for progression and mortality in cats with chronic kidney disease."
    - "Amlodipine besylate and telmisartan are effective antihypertensive agents for use in these patients."
    - "Blood pressure monitoring in cats with chronic kidney disease is still infrequently performed."
    - "Cats with chronic kidney disease that are normotensive at diagnosis are significantly more likely than cats with normal renal function to develop hypertension later."
  source_supported_conclusion:
    - Systolic blood pressure is a first-wave CKD endpoint and management lever, not a secondary contextual afterthought.
    - Proteinuria and blood pressure should stay linked in compiled pages because this review places them inside the same progression and hemodynamic injury branch.
    - Hypertension management should be framed as target-organ protection and progression control, not only as a numeric threshold exercise.
    - Blood-pressure under-measurement is a real translation problem because implementation gaps can distort how CKD severity is recognized in practice.
    - Amlodipine and telmisartan belong in the antihypertensive branch, but this source alone should not be used to claim hard-outcome superiority between them.
  llm_inference:
    - Future efficacy-study planning should likely stratify CKD cohorts by hypertension status instead of treating blood pressure as background noise.
    - The translational branch may need a more explicit fork for `CKD with hypertension/proteinuria junction` versus `CKD without overt hemodynamic comorbidity`.
  # V2 enhanced fields
  study_design: "综述，涵盖猫 CKD 与高血压的交织关系（2021 年）"
  core_argument: "CKD 和高血压在猫中是双向共病——高血压增加蛋白尿和靶器官损害，需要常规血压监测和积极治疗"
  implicit_premise: "假设血压既是后果也是驱动因素；假设靶器官损害使抗高血压治疗超越肾脏生物标志物"
  unexpected_finding: "CKD 猫的血压监测仍不频繁进行——这意味着高血压可能在该人群中被低诊断"
  title_gap: "标题说 CKD 与高血压的交织关系，但真正发现是实施差距：血压监测仍不频繁——高血压在 CKD 猫中可能被系统性低诊断"
  evidence_boundary: "支持抗高血压重要性，但不支持特定药物间的硬性结局优越性声明"
---

# Feline comorbidities: The intermingled relationship between chronic kidney disease and hypertension

## One-Line Summary

This review frames CKD and hypertension in cats as a bidirectional comorbidity, with hypertension increasing proteinuria and target organ damage, and therefore requiring routine blood pressure monitoring and active treatment.

## Why It Matters For CKD

This may affect endpoint interpretation, patient stratification, and translational claims.

## Key Findings

### quoted_fact

- CKD is frequently diagnosed in association with hypertension in cats, and the two conditions have an intermingled cause-and-effect relationship.
- Hypertensive target organ damage to the eye, brain, heart, and kidney significantly affects welfare in cats with this comorbidity.
- Hypertension drives proteinuria, which is an independent risk factor for progression and mortality in cats with CKD.
- Current guidelines recommend a target systolic blood pressure below 160 mmHg to minimise risk of target organ damage.
- Amlodipine besylate and telmisartan are effective antihypertensive agents for use in these patients.
- Blood pressure monitoring in cats with CKD is still infrequently performed, and hypertension likely remains underdiagnosed in this population.
- Reported prevalence of hypertension in cats with CKD ranges from approximately 20% to 65%, depending on population and definition used.
- Cats with CKD that are normotensive at diagnosis are significantly more likely than cats with normal renal function to develop hypertension later.

### source_supported_conclusion

- Systolic blood pressure is unquestionably a first-wave CKD endpoint and cannot be treated as a secondary context variable.
- Proteinuria becomes even more important when the hypertension literature is added, because it sits at the intersection of progression and hemodynamic injury.
- The endpoint handbook should include a dedicated blood pressure and comorbidity subsection rather than scattering hypertension across multiple pages.
- Target-organ damage broadens the significance of blood-pressure control beyond the kidney alone, which makes SBP a welfare and translation variable as well as a renal endpoint.
- This source strengthens the claim that under-monitoring of blood pressure is itself an implementation gap in feline CKD care.

### llm_inference

- A later translation page should probably include a small treatment fork for CKD with hypertension vs CKD without hypertension because the management logic diverges materially.

## Junction Logic

This paper is important because it makes the CKD-hypertension-proteinuria junction impossible to ignore.

The safe read is:

- blood pressure is both consequence and driver
- proteinuria is not just a renal lab value, it sits inside the hemodynamic branch
- target-organ damage makes antihypertensive treatment about more than renal biomarkers
- implementation gaps matter because under-measurement hides a clinically important subgroup

That gives this source unusual leverage in both endpoint and translation pages.

## Limits / Caveats

- Mechanistic details of the CKD-hypertension interaction remain incompletely resolved.
- The review supports antihypertensive importance more strongly than it supports hard-outcome superiority claims for specific agents.
- This card is strongest for comorbidity framing, target-organ-damage relevance, and monitoring logic rather than for product-ranking detail.

## Open Follow-Up Questions

- How should hypertension status affect endpoint selection in future efficacy studies?
- Which blood pressure treatment effects are supported by feline outcome data versus consensus practice?

## Linked Entities

- diseases: CKD
- models:
- endpoints: systolic blood pressure, proteinuria
- mechanisms:
- regulations:
