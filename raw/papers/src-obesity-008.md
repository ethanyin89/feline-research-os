---
id: src-obesity-008
type: source
title: "Insulin Sensitivity Decreases with Obesity, and Lean Cats with Low Insulin Sensitivity are at Greatest Risk of Glucose Intolerance with Weight Gain"
source_kind: paper
species: feline
diseases: [obesity, glucose intolerance]
models: []
endpoints: [insulin-sensitivity, glucose-tolerance, weight-gain]
jurisdictions: []
evidence_level: original-study
year: 2001
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [obesity, insulin-sensitivity, glucose-intolerance, weight-gain, diabetes-bridge]
links:
  doi: "10.1053/JFMS.2001.0138"
  url: "https://pubmed.ncbi.nlm.nih.gov/11795959/"
  local_assets:
    - "../../raw/deep-extractions/ext-src-obesity-008.md"
evidence_policy:
  quoted_fact:
    - "The study followed 16 research cats, including 6 neutered males and 10 spayed females."
    - "Cats gained an average of 1.91 kg, approximately 44%, over a mean 10.5 months of ad libitum high-energy feeding."
    - "After weight gain, all cats had DEXA body fat >30%."
    - "Insulin sensitivity index Si decreased from 3.27 ± 1.58 to 1.56 ± 0.63 ×10^-4 per min/uU/ml, approximately halving with obesity."
    - "Glucose effectiveness Sg decreased by 26%."
    - "After obesity, 7/16 cats, approximately 44%, developed impaired glucose tolerance."
    - "Lean-state Si below the group median was associated with a 2.9-fold IGT risk after weight gain; low Si plus low Sg was associated with a 4-fold risk; fasting insulin above median was associated with a 4.7-fold risk."
  source_supported_conclusion:
    - "This source is a bounded obesity-diabetes mechanism anchor."
    - "It can support branch placement linking feline weight gain / obesity with insulin sensitivity, glucose effectiveness, and glucose tolerance."
    - "It supports individual-susceptibility framing rather than a universal claim that all obese cats become glucose intolerant."
    - "It must not be converted into screening thresholds, owner-facing weight-loss advice, or a full obesity guidance page by itself."
  llm_inference:
    - "This source may become the first obesity mechanism anchor."
    - "It may also sharpen the existing diabetes obesity/body-condition memo by adding a direct feline metabolic study behind the review-level bridge."
  # V2 enhanced fields
  study_design: "前后对照实验研究，16 只健康研究猫经约10.5个月自由采食高能量日粮增重，使用DEXA、IVGTT和Bergman MINMOD模型评估体组成、胰岛素敏感性、葡萄糖有效性和糖耐量"
  core_argument: "猫肥胖会使胰岛素敏感性约下降一半并降低葡萄糖有效性，但增重后是否发生糖耐量受损并不只由肥胖程度决定；瘦态时已有低胰岛素敏感性、低葡萄糖有效性或空腹高胰岛素的猫更容易在增重后失代偿。"
  implicit_premise: "胰岛素敏感性和葡萄糖耐量测定方法准确反映猫体内代谢状态，且体重变化是导致胰岛素敏感性变化的主要因素"
  title_gap: "标题强调肥胖降低胰岛素敏感性，但真正发现是瘦猫中胰岛素敏感性低者在增重后更易发生葡萄糖耐量异常——提示个体差异的重要性"
  evidence_boundary: "该研究证明的是诱导肥胖后的胰岛素抵抗和糖耐量受损风险分层，并未长期随访到自然发生糖尿病；不能转化为临床筛查阈值或减重处方。"
  unexpected_finding: "肥胖程度本身不能区分哪些猫会糖耐量受损；变胖前的Sᵢ、Sg和空腹胰岛素比体重更能提示个体易感性。"
---

# Insulin Sensitivity Decreases with Obesity, and Lean Cats with Low Insulin Sensitivity are at Greatest Risk of Glucose Intolerance with Weight Gain

## Evidence-Depth Caveat

This card now links to a desktop deep extraction and the earlier Sage-page worksheet. It is usable for bounded mechanism and branch-placement claims, but not for screening thresholds, weight-loss protocols, or owner-facing management advice.

## Source Check, 2026-05-14

Crossref metadata was checked as a repeatable second-pass intake step.

- DOI metadata resolved: yes
- Container: Journal of Feline Medicine and Surgery
- Year: 2001
- Abstract available in Crossref: yes

Deep extraction artifacts:

- [ext-src-obesity-008](../deep-extractions/ext-src-obesity-008.md)
- [src-obesity-008 deep extraction round 1](../../system/indexes/src-obesity-008-deep-extraction-round1.md)

## Deep Extraction, 2026-05-17

Official article-page review promoted this card from `abstract_weighted` to `deep_extracted`; the 2026-06-26 desktop deep extraction adds fuller passage-level support.

- safe use: obesity-to-insulin-sensitivity mechanism branch and diabetes bridge
- unsafe use: clinical screening rules, weight-loss prescriptions, or universal obesity-to-diabetes progression claims


## One-Line Summary

Original feline study showing that induced obesity approximately halves insulin sensitivity, reduces glucose effectiveness, and reveals impaired glucose tolerance especially in cats with low lean-state insulin sensitivity.

## Why It Matters For Feline Obesity

This source is unusually important because it can connect obesity to a measurable metabolic endpoint rather than only to body condition or owner perception. It also bridges the new obesity module with the existing diabetes obesity/body-condition logic.

The title itself is already a strong signal that the source belongs in Tier A. It names insulin sensitivity, obesity, low baseline insulin sensitivity, glucose intolerance, and weight gain. Those concepts are exactly where obesity becomes more than a weight-management topic and starts becoming a disease-risk architecture.

## Key Findings

### quoted_fact

- Crossref metadata identifies this as a 2001 Journal of Feline Medicine and Surgery article.
- The study used 16 cats and induced average weight gain of about 44%.
- Si decreased from 3.27 ± 1.58 to 1.56 ± 0.63 ×10^-4 per min/uU/ml.
- Sg decreased by 26%.
- 7/16 cats developed impaired glucose tolerance after weight gain.
- Low lean-state Si, low Sg, and high fasting insulin were risk signals for IGT after weight gain.

### source_supported_conclusion

- This is a high-value source for the obesity-diabetes bridge.
- It should be read before writing an obesity mechanism page.
- It can safely support the existence of a feline mechanism branch connecting weight gain / obesity with insulin sensitivity, glucose effectiveness, and glucose tolerance.
- It supports individual-susceptibility framing rather than a universal diabetes progression claim.

### llm_inference

- This source may become the first obesity mechanism anchor.
- It may also sharpen the existing diabetes obesity/body-condition memo by adding a direct feline metabolic study behind the review-level bridge.

## Claim-Fit Judgment

Strongest safe use:

- obesity-to-insulin-sensitivity mechanism branch
- diabetes overlap control
- endpoint planning for glucose tolerance and insulin sensitivity

Must not control yet:

- universal diabetes-risk prediction
- clinical screening rules
- treatment recommendations
- claims about all obese cats becoming glucose intolerant

## Image Asset TODO

- figures to capture: glucose/insulin response curves or study design diagrams if present
- why these matter: mechanism figures could become high-value retrieval assets after article label verification

## Open Follow-Up Questions

- Were effects reversible with weight loss?
- How should this study interact with diabetes remission and obesity/body-condition pages?

## Linked Entities

- diseases: obesity, glucose intolerance, diabetes mellitus
- models:
- endpoints: insulin sensitivity, glucose tolerance, weight gain
- mechanisms: insulin resistance
- regulations:
