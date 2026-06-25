---
id: src-diabetes-024
type: source
title: "Insulin glargine 300 U/ml for the treatment of feline diabetes mellitus"
source_kind: paper
species: feline
diseases: [diabetes mellitus]
models: []
endpoints: [glycemic-control, safety]
jurisdictions: []
evidence_level: original-study
year: 2021
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [diabetes, insulin, glargine, treatment]
links:
  doi: "10.1177/1098612X211013018"
  url: "https://journals.sagepub.com/doi/10.1177/1098612X211013018"
  local_assets: ["../../raw/deep-extractions/ext-src-diabetes-024.md"]
evidence_policy:
  quoted_fact:
    - "Crossref abstract reports 13 client-owned diabetic cats completed the prospective clinical trial."
    - "Four cats suspected of hypersomatotropism were excluded from insulin efficacy evaluation."
    - "Two cats achieved remission during the 8-week study and two more after study end."
    - "Crossref abstract reports cats were treated with IGla-U300 twice daily and fed a low-carbohydrate diet."
    - "Crossref abstract reports biochemical hypoglycemia in 13/104 blood-glucose curves without reported clinical hypoglycemia signs."
  source_supported_conclusion:
    - "This source should anchor the insulin glargine U300 treatment branch."
    - "IGla-U300 appears promising in a small short-term study, but not comparative-winner status."
    - "Hypersomatotropism materially affects interpretation of insulin efficacy."
    - "Safety interpretation requires separating biochemical hypoglycemia from clinical hypoglycemia signs."
    - "The combined insulin-plus-low-carbohydrate-diet design blocks clean isolation of the insulin contribution."
    - "This source should support a treatment branch, not a final insulin hierarchy."
  llm_inference:
    - "This is a high-priority full-text target if later outputs need insulin protocol details, dose-adjustment rules, or durability claims."
  # V2 enhanced fields
  study_design: "前瞻性临床试验，13 只由客户拥有的糖尿病猫，排除疑似生长激素过多症猫，使用每日两次胰岛素格拉欣300 U/ml治疗并配合低碳水化合物饮食"
  core_argument: "胰岛素格拉欣300 U/ml在短期内对猫糖尿病具有潜在疗效，但生长激素过多症会显著影响胰岛素治疗效果的评估"
  implicit_premise: "该研究假设排除疑似生长激素过多症的猫后，剩余糖尿病猫的胰岛素反应可以准确反映胰岛素格拉欣300 U/ml的疗效"
  title_gap: "标题表明针对猫糖尿病的胰岛素格拉欣300 U/ml治疗，但研究揭示了生长激素过多症的影响可能导致疗效评估偏差——强调需谨慎解读"
  evidence_boundary: "未比较胰岛素格拉欣300 U/ml与其他胰岛素制剂的疗效差异，也未评估长期治疗安全性和疗效"
  unexpected_finding: "尽管多次血糖曲线出现生化性低血糖，但未观察到相关临床低血糖症状"
---

# Insulin glargine 300 U/ml for the treatment of feline diabetes mellitus

## One-Line Summary

Recent original treatment source for insulin glargine 300 U/ml in feline diabetes.

## Why It Matters For Feline Diabetes

- gives the insulin-treatment branch a newer glargine U300 anchor
- should be compared with older diet/insulin and newer SGLT2 sources

## Key Findings

- abstract-level extraction confirms this as a small prospective clinical trial
- cats received IGla-U300 twice daily plus a low-carbohydrate diet
- fructosamine decreased by week 8 in the abstract-level report
- biochemical hypoglycemia occurred in some blood-glucose curves without reported clinical hypoglycemia signs
- remission was observed during and after the short study window, but durability remains a follow-up question
- suspected hypersomatotropism changed efficacy interpretation, which reinforces the endocrine-secondary branch
- the strongest safe conclusion is `promising insulin branch`, not `best insulin protocol`

## Limits / Caveats

- extraction is abstract-weighted, not full-text
- does not prove superiority over other insulin protocols
- long-term durability and comparative safety need fuller evidence
- does not isolate IGla-U300 from concurrent low-carbohydrate diet effects
- remission findings should defer to the remission systematic-review boundary before becoming protocol claims
- biochemical hypoglycemia and clinical hypoglycemia signs should remain separated

## Glargine U300 Branch Logic

This source is the current glargine U300 anchor in the diabetes seed set.

What can be promoted:

- IGla-U300 has a small prospective clinical-trial signal in client-owned diabetic cats
- the study used home blood-glucose curves and fructosamine-related monitoring logic
- remission occurred in some cats during or after the observation window
- suspected hypersomatotropism was important enough to exclude some cats from efficacy evaluation
- biochemical hypoglycemia can appear without reported clinical signs, so safety interpretation needs detail

What should be held:

- superiority over other insulin protocols
- long-term remission or durability claims
- isolated insulin effect independent of the low-carbohydrate diet context
- dosing or dose-adjustment instructions
- claims that difficult-control cats can be interpreted without endocrine-comorbidity thinking

## Relationship To Treatment Architecture

This card sits in the insulin branch of the [diabetes treatment branch comparison memo](../../system/indexes/diabetes-treatment-branch-comparison-memo.md).

It should be compared against:

- diet architecture cards, because the trial included a low-carbohydrate diet
- [src-diabetes-007](src-diabetes-007.md), because remission claims defer to systematic-review caution
- endocrine-secondary cards, because hypersomatotropism altered efficacy interpretation
- SGLT2 cards, because newer oral branches should not be ranked against insulin without comparator evidence

## Write-Back Implications

- [translation brief](../../topics/diabetes/translation-brief.md) should keep IGla-U300 as promising but below comparative-winner language.
- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md) should separate fructosamine/glycemic control, remission, biochemical hypoglycemia, and clinical safety signs.
- [synthesis index](../../topics/diabetes/synthesis-index.md) should keep insulin protocol interpretation tied to endocrine-secondary and diet context.

## Open Follow-Up Questions

- what was the study design and sample size?
- what glycemic endpoints were used?
- how did glargine U300 compare with standard approaches?

## Linked Entities

- diseases: diabetes mellitus
- models:
- endpoints: glycemic control, safety
- mechanisms: basal insulin therapy
- regulations:
