---
id: src-ckd-020
type: source
title: "Ultrasonography of the feline kidney: Technique, anatomy and changes associated with disease"
source_kind: paper
species: feline
diseases: [CKD]
models: []
endpoints: []
jurisdictions: []
evidence_level: review
year: 2012
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ckd, ultrasonography, imaging, kidney, review]
links:
  doi: "10.1177/1098612X12464461"
  url: "https://journals.sagepub.com/doi/10.1177/1098612X12464461"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Ultrasonography is an important tool for the detection of kidney disorders."
    - "It is more accurate than radiography for this purpose and is considered to be the reference modality for imaging the feline kidney."
    - "On ultrasound examination, focal or multifocal disorders may be readily identified, but diffuse changes are more challenging."
    - "B-mode ultrasonography is of limited use for differentiating between benign and malignant focal lesions."
    - "Compared with more advanced imaging modalities, such as computed tomography or magnetic resonance imaging, ultrasonography is more accessible, less expensive, does not require general anaesthesia and allows real-time procedures to be performed."
  source_supported_conclusion:
    - This review is useful for defining imaging as a real workup layer in feline renal assessment, not just a guideline checkbox.
    - Ultrasonography should be framed as a practical reference imaging modality for feline kidney assessment, but not as a standalone CKD-defining test.
    - The paper is stronger for workup completeness, structural context, and differential diagnosis than for early CKD-specific discrimination.
    - Diffuse renal disease remains harder to characterize ultrasonographically than focal disease, which limits overpromotion of ultrasound in CKD staging logic.
  llm_inference:
    - The vault should now treat ultrasound as a bounded `workup realism` branch: important for structural context and renal differential assessment, but below core biochemical/hemodynamic endpoints in default CKD summaries.
  # V2 enhanced fields
  study_design: "综述，涵盖猫肾超声检查的技术、解剖和疾病相关变化"
  core_argument: "超声是猫肾脏评估的参考成像方式——但弥漫性变化比局灶性病变更难表征，限制了超声在 CKD 分期逻辑中的过度推广"
  implicit_premise: "假设实用性和结构信息使超声有价值，但不能取代核心生化和血流动力学终点"
  unexpected_finding: "B 模式超声在区分良性和恶性局灶性病变方面有限——成像优势有边界"
  title_gap: "标题说肾脏超声检查，但真正发现是技术边界：弥漫性变化比局灶性病变更难表征——超声提供结构背景但不能取代核心生化终点"
  evidence_boundary: "综述跨越肾脏疾病广泛，非仅 CKD；工作流完整性强于终点提升"
---

# Ultrasonography of the feline kidney: Technique, anatomy and changes associated with disease

## One-Line Summary

This review shows that renal ultrasonography is the practical reference imaging modality for feline kidney assessment, but is better for structural context and differential diagnosis than for solving diffuse CKD interpretation on its own.

## Why It Matters For CKD

The guideline already includes imaging in the routine workup. This review helps turn that from a checkbox into a better-defined, but still bounded, workup layer.

## Key Findings

### quoted_fact

- Ultrasonography is an important tool for detecting feline kidney disorders.
- It is considered the reference imaging modality for the feline kidney and is more accurate than radiography.
- It provides excellent visualization of renal size, shape, and internal architecture.
- Focal or multifocal renal disorders are more readily identified than diffuse changes.
- B-mode ultrasonography is limited in differentiating benign from malignant focal lesions.
- Compared with CT or MRI, ultrasonography is more accessible, less expensive, does not require general anaesthesia, and permits real-time procedures.

### source_supported_conclusion

- This source is more useful for workup completeness than for first-wave endpoint ranking.
- Ultrasound should be treated as an important structural-context modality in feline CKD workup.
- The review supports imaging realism, but not ultrasound-first CKD diagnosis logic.
- The review supports workup realism more strongly than endpoint promotion, which helps densify compile quality without distorting the endpoint hierarchy.

### llm_inference

- If imaging density grows, this could justify a dedicated imaging-context note under CKD later.

## Practical Workup Signal

The safest place for this source in the vault is:

- above "imaging checkbox" language
- below core endpoint logic
- inside structural-context and differential-workup framing

That means it helps the system answer:

- what imaging adds
- why imaging still matters
- why imaging should not overrule the practical biochemical and hemodynamic core

It also helps refine a common overclaim. Ultrasound is strong because it is practical and structurally informative, not because it cleanly solves diffuse CKD classification. In other words, it improves the realism of renal assessment and differential workup without displacing creatinine, USG, proteinuria, or blood-pressure monitoring from the first-wave operational core.

## Limits / Caveats

- This is likely broader than CKD alone and may need selective extraction.
- The review spans renal disease broadly, not CKD only.
- Diffuse renal changes are harder to characterize than focal lesions, limiting direct CKD specificity.
- Accessibility and real-time procedural value strengthen ultrasound's workup role, but that still does not convert it into a primary CKD severity or efficacy endpoint.

## Open Follow-Up Questions

- Which ultrasonographic changes are most consistently useful in spontaneous feline CKD specifically?
- How much does ultrasound add when biochemical and urinary evidence is already present?
- Does the vault need a dedicated imaging/workup note or only bounded mentions inside endpoint and early-detection pages?

## Linked Entities

- diseases: CKD
- models:
- endpoints: diagnostic imaging, ultrasonography
- mechanisms:
- regulations:
