---
id: src-ckd-007
type: source
title: "Therapies for Feline Chronic Kidney Disease: What is the Evidence?"
source_kind: paper
species: feline
diseases: [CKD]
models: []
endpoints: []
jurisdictions: []
evidence_level: review
year: 2009
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ckd, therapy, evidence]
links:
  doi: "10.1016/j.jfms.2009.01.004"
  url: "https://journals.sagepub.com/doi/10.1016/j.jfms.2009.01.004"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The evidence-grading framework used grades I to IV."
    - "Chronic kidney disease was defined as kidney damage present for at least 3 months with or without decreased GFR, or a reduction in GFR persisting for at least 3 months."
    - "IRIS staging is based on at least 2 sequential serum creatinine measurements in a well-hydrated, fasted patient."
    - "Cats with a UPC >0.4 are considered proteinuric, cats with a UPC of 0.2-0.4 are borderline proteinuric, and cats with a UPC <0.2 are non-proteinuric."
    - "Long-term subcutaneous fluid therapy in cats with CKD is supported only by grade IV evidence."
  source_supported_conclusion:
    - This review is the main evidence-discipline source for preventing the treatment branch from collapsing into a flat list of common habits.
    - Treatment pages in the vault should keep explicit evidence-strength labels because this paper repeatedly separates common use from higher-quality support.
    - Proteinuria and blood pressure remain central treatment-organizing variables even inside an evidence-grading review, which strengthens their role as bridge endpoints.
    - Long-term subcutaneous fluid therapy should remain clearly bounded as common but weakly supported in the current corpus.
    - Renal diet and phosphorus-control logic can remain at the top of the treatment hierarchy without assuming that the rest of supportive care belongs on the same tier.
  llm_inference:
    - The safest treatment matrix is one that separates `baseline-supported`, `context-dependent`, and `weak-evidence/common-practice` branches.
    - Translation summaries should use this source to challenge overconfident intervention ranking language, not to introduce novelty claims.
  # V2 enhanced fields
  study_design: "系统综述，使用 I-IV 级证据分级框架评估猫 CKD 治疗方法"
  core_argument: "许多猫 CKD 干预措施虽被广泛使用，但缺乏或仅有弱证据支持——长期皮下补液仅有 IV 级证据，不应等同于有效性证明"
  implicit_premise: "假设常规做法与证据支持是可区分的概念；假设证据分级框架适用于指导治疗决策"
  unexpected_finding: "长期皮下补液——一种常见的猫 CKD 治疗方法——仅有 IV 级（最弱）证据支持"
  title_gap: "标题问证据是什么，但真正发现是实践与证据的分离：长期皮下补液虽广泛使用但仅有 IV 级证据——常规做法≠循证支持"
  evidence_boundary: "较旧综述，部分干预措施讨论可能需要更新；强于证据分级架构，弱于当前产品级推荐"
---

# Therapies for Feline Chronic Kidney Disease: What is the Evidence?

## One-Line Summary

This systematic review evaluates CKD therapies using an evidence-grading framework and argues that many interventions are commonly used despite weak or inconsistent supporting evidence.

## Why It Matters For CKD

This is useful for separating routine therapeutic habits from actual supporting evidence.

## Key Findings

### quoted_fact

- The review uses an evidence-grading framework from grade I to IV.
- Kidney disease is defined as functional or structural abnormalities in one or both kidneys.
- CKD is defined as kidney damage present for at least 3 months with or without decreased GFR, or a reduction in GFR persisting at least 3 months.
- IRIS staging uses at least two sequential serum creatinine measurements in a well-hydrated, fasted patient.
- UPC greater than 0.4 is classified as proteinuric in cats, while 0.2-0.4 is borderline and less than 0.2 is non-proteinuric.
- Long-term subcutaneous fluid therapy for CKD has only weak grade IV evidence in cats.
- The paper is valuable partly because it grades interventions that were already common in practice rather than assuming practice pattern equals proof.

### source_supported_conclusion

- This review should be used as the translation-layer reality check because it explicitly separates widespread practice from stronger evidence.
- Treatment planning in V1 should carry evidence strength labels rather than flattening all interventions into one therapeutic list.
- Proteinuria and blood pressure belong in the treatment map not only because they are measured, but because intervention decisions and prognosis discussions are built around them.
- This source strengthens the boundary that common supportive-care use should not be translated into disease-modification proof.
- The treatment branch should continue to rank renal diet and phosphorus-focused interventions above weakly supported supportive habits such as long-term subcutaneous fluids.

### llm_inference

- A future CKD treatment matrix should likely rank interventions as baseline-supported, context-dependent, or weak-evidence.

## Why This Review Matters More Than It Looks

This source does not win by being the newest treatment paper.
It wins because it imposes discipline.

Without it, the vault can drift toward:

- listing many CKD interventions
- treating common use as soft proof
- forgetting which branches actually have stronger support

With it, the safer reading is:

- some interventions deserve higher confidence labels
- some remain clinically reasonable but weakly evidenced
- evidence-strength labeling is part of the treatment architecture itself

## Practical Write-Back Signal

The main operational upgrades from this source are:

- keep evidence labels visible in treatment pages
- keep long-term subcutaneous fluids explicitly bounded as weak-evidence
- keep UPC and blood pressure connected to treatment reasoning
- keep renal diet and phosphorus control above lower-evidence adjunct branches

That makes this source a control document for treatment wording quality, not just another therapy summary.

## Limits / Caveats

- This is an older review and some intervention-specific discussions will need updating against newer studies and guidelines.
- The paper is stronger for evidence-grading architecture than for current product-by-product recommendation detail.
- Not every intervention category has been extracted at the same density, so this card currently supports treatment-boundary logic more strongly than exhaustive ranking.

## Open Follow-Up Questions

- Which intervention classes in this review reach the highest evidence grades in cats?
- Which weak-evidence therapies are still standard practice because of lack of better options?

## Linked Entities

- diseases: CKD
- models:
- endpoints: creatinine, GFR, UPCR, systolic blood pressure, phosphorus, potassium
- mechanisms:
- regulations:
