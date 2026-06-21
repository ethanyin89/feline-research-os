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
  url: "https://doi.org/10.1053/JFMS.2001.0138"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Crossref metadata resolves this DOI and reports abstract availability for source scope checking."
    - "Crossref container: Journal of Feline Medicine and Surgery; year: 2001."
    - "The official article page reports 16 cats and an average weight increase of 44.2% over 10 months."
    - "The official article page reports that obesity was accompanied by decreased tissue sensitivity to insulin and reduced glucose effectiveness."
    - "The official article page reports that cats with lower lean-state insulin sensitivity and glucose effectiveness had higher risk of impaired glucose tolerance after weight gain."
  source_supported_conclusion:
    - "This source is a bounded obesity-diabetes mechanism anchor."
    - "It can support branch placement linking feline weight gain / obesity with insulin sensitivity, glucose effectiveness, and glucose tolerance."
    - "It supports individual-susceptibility framing rather than a universal claim that all obese cats become glucose intolerant."
    - "It must not be converted into screening thresholds, owner-facing weight-loss advice, or a full obesity guidance page by itself."
  llm_inference:
    - "This source may become the first obesity mechanism anchor."
    - "It may also sharpen the existing diabetes obesity/body-condition memo by adding a direct feline metabolic study behind the review-level bridge."
  # V2 enhanced fields
  study_design: "前瞻性实验研究，16 只健康猫在 10 个月内体重增加约 44.2%，通过测量胰岛素敏感性和葡萄糖耐量变化进行观察"
  core_argument: "肥胖降低猫体组织对胰岛素的敏感性，且瘦猫中胰岛素敏感性较低者在体重增加后更易发生葡萄糖耐量异常"
  implicit_premise: "胰岛素敏感性和葡萄糖耐量测定方法准确反映猫体内代谢状态，且体重变化是导致胰岛素敏感性变化的主要因素"
  title_gap: "标题强调肥胖降低胰岛素敏感性，但真正发现是瘦猫中胰岛素敏感性低者在增重后更易发生葡萄糖耐量异常——提示个体差异的重要性"
  evidence_boundary: "该研究未探讨肥胖相关胰岛素抵抗的分子机制，也未验证是否所有肥胖猫均会发展为糖尿病"
  unexpected_finding: "尽管总体肥胖降低胰岛素敏感性，但瘦猫中本来胰岛素敏感性较低的个体更容易因增重而出现葡萄糖耐量受损，显示个体代谢差异显著"
---

# Insulin Sensitivity Decreases with Obesity, and Lean Cats with Low Insulin Sensitivity are at Greatest Risk of Glucose Intolerance with Weight Gain

## Evidence-Depth Caveat

This card now has a first deep-extraction worksheet from the official Sage article page. It is usable for bounded mechanism and branch-placement claims, but not for screening thresholds, weight-loss protocols, or owner-facing management advice.

## Source Check, 2026-05-14

Crossref metadata was checked as a repeatable second-pass intake step.

- DOI metadata resolved: yes
- Container: Journal of Feline Medicine and Surgery
- Year: 2001
- Abstract available in Crossref: yes

Use boundary:

- This card may guide navigation and extraction priority.
- It must not support reader-facing clinical claims until a full abstract extraction or source worksheet is completed.

Abstract lead for scope check only: This study quantifies the effects of marked weight gain on glucose and insulin metabolism in 16 cats which increased their weight by an average of 44.2% over 10 months. Significan...

## Deep Extraction, 2026-05-17

Official article-page review promoted this card from `abstract_weighted` to `deep_extracted`.

- [src-obesity-008 deep extraction round 1](../../system/indexes/src-obesity-008-deep-extraction-round1.md)
- safe use: obesity-to-insulin-sensitivity mechanism branch and diabetes bridge
- unsafe use: clinical screening rules, weight-loss prescriptions, or universal obesity-to-diabetes progression claims


## One-Line Summary

Original feline study candidate linking obesity, weight gain, insulin sensitivity, and glucose intolerance.

## Why It Matters For Feline Obesity

This source is unusually important because it can connect obesity to a measurable metabolic endpoint rather than only to body condition or owner perception. It also bridges the new obesity module with the existing diabetes obesity/body-condition logic.

The title itself is already a strong signal that the source belongs in Tier A. It names insulin sensitivity, obesity, low baseline insulin sensitivity, glucose intolerance, and weight gain. Those concepts are exactly where obesity becomes more than a weight-management topic and starts becoming a disease-risk architecture.

## Key Findings

### quoted_fact

- Crossref metadata identifies this as a 2001 Journal of Feline Medicine and Surgery article.
- The Crossref abstract begins by describing a study quantifying effects of marked weight gain on glucose and insulin metabolism in 16 cats.
- The title states that insulin sensitivity decreases with obesity.
- The official article page reports average weight gain of 44.2% over 10 months in 16 cats.
- The official article page reports decreased tissue sensitivity to insulin and reduced glucose effectiveness with obesity.
- The article links lower lean-state insulin sensitivity / glucose effectiveness with higher risk of impaired glucose tolerance after weight gain.

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

- exact effect sizes
- universal diabetes-risk prediction
- clinical screening rules
- treatment recommendations
- claims about all obese cats becoming glucose intolerant

## Image Asset TODO

- figures to capture: glucose/insulin response curves or study design diagrams if present
- why these matter: mechanism figures could become high-value retrieval assets after article label verification

## Open Follow-Up Questions

- What were the methods for inducing or measuring weight gain?
- What insulin-sensitivity metrics were used?
- Were effects reversible with weight loss?
- How should this study interact with diabetes remission and obesity/body-condition pages?

## Linked Entities

- diseases: obesity, glucose intolerance, diabetes mellitus
- models:
- endpoints: insulin sensitivity, glucose tolerance, weight gain
- mechanisms: insulin resistance
- regulations:
