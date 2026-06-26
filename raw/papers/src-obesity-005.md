---
id: src-obesity-005
type: source
title: "Identifying the target population and preventive strategies to combat feline obesity"
source_kind: paper
species: feline
diseases: [obesity]
models: []
endpoints: [prevention, target-population, risk-factors]
jurisdictions: []
evidence_level: review
year: 2024
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [obesity, prevention, target-population, risk-factors, review]
links:
  doi: "10.1177/1098612X241228042"
  url: "https://doi.org/10.1177/1098612X241228042"
  local_assets:
    - "../../raw/deep-extractions/ext-src-obesity-005.md"
evidence_policy:
  quoted_fact:
    - "The deep extraction identifies post-gonadectomy kittens aged 5-12 months as the primary target population for feline obesity prevention."
    - "The deep extraction reports that post-gonadectomy energy needs may decrease by up to 30%, while energy intake may increase by up to 50%."
    - "The deep extraction emphasizes growth monitoring, DER-based feeding, gram-scale food measurement, and 2-week reassessment after rapid weight gain."
    - "The deep extraction states that kittens under 12 months should receive growth-stage or all-life-stage food and should not simply be switched to adult weight-management or weight-loss food."
  source_supported_conclusion:
    - "This source is a full-text prevention anchor for feline obesity."
    - "It supports target-population framing around post-gonadectomy 5-12 month kittens."
    - "It supports a prevention workflow based on early communication, growth monitoring, DER-based feeding, food weighing, environment enrichment, and reassessment."
    - "It supports distinguishing kitten obesity prevention from adult weight-loss treatment."
  llm_inference:
    - "Owner-facing outputs can use this as a prevention-architecture source, but exact DER calculations and diet selection should still be framed as veterinary-guided."
    - "Because the paper is a review with nutrition-industry conflicts declared, distinguish directly cited evidence from expert synthesis."
  # V2 enhanced fields
  study_design: "开放获取综述；聚焦猫肥胖高风险窗口、绝育后幼猫、预防沟通、生长监测、DER 喂养、食物称量和环境管理。"
  core_argument: "猫肥胖管理应从成年肥胖后的减重治疗前移到绝育后5-12月龄幼猫的预防窗口，通过沟通、监测和精确喂养减少过量增重。"
  implicit_premise: "绝育后食欲上升与能量需求下降叠加，且5-12月龄仍处于可塑生长期，因此早期预防比成年后减重更可行。"
  title_gap: "标题说识别目标人群和预防策略；真正高价值结论是 post-gonadectomy 5-12月龄幼猫这个具体窗口，以及不能把幼猫当成年肥胖猫处理。"
  evidence_boundary: "综述和专家综合，不是预防方案随机试验；不能把宏量营养素范围、DER方程或食物形态建议当作已验证的统一处方。"
  unexpected_finding: "幼猫BCS偏高时也不应简单换成成年减重粮；预防核心是控制增长轨迹，而不是传统意义上的减肥。"
---

# Identifying the target population and preventive strategies to combat feline obesity

## Evidence-Depth Caveat

This card now links to a user-supplied full deep extraction. It is usable as the obesity prevention anchor, especially for post-gonadectomy kittens aged 5-12 months, while preserving the boundary between kitten growth prevention and adult weight-loss treatment.

## Source Check, 2026-05-14

Crossref metadata was checked as a repeatable second-pass intake step.

- DOI metadata resolved: yes
- Container: Journal of Feline Medicine and Surgery
- Year: 2024
- Abstract available in Crossref: yes

Deep extraction artifact:

- `raw/deep-extractions/ext-src-obesity-005.md`

## Deep Extraction, 2026-05-17

Full abstract review promoted this card from `abstract_weighted` to `deep_extracted`. The 2026-06-26 desktop deep extraction adds full-text prevention details and passage-level support.

- [src-obesity-005 deep extraction round 1](../../system/indexes/src-obesity-005-deep-extraction-round1.md)
- safe use: prevention architecture, target population identification, growth-monitoring workflow, DER-based feeding boundary
- unsafe use: validated prevention success rates, universal DER prescriptions, replacing veterinary nutrition guidance


## One-Line Summary

Feline-specific prevention review identifying post-gonadectomy kittens aged 5-12 months as the highest-priority prevention population and emphasizing growth monitoring plus precise feeding rather than adult-style weight loss.

## Why It Matters For Feline Obesity

Prevention is a different question from treatment. If the obesity module treats every obesity question as adult weight-loss management, it will miss the earlier and more actionable window: post-gonadectomy kittens whose growth trajectory is still changing.

This source matters because it gives the prevention branch a concrete target population and workflow: early owner communication, repeated growth tracking, DER-based food allocation, gram-scale measurement, and reassessment when rapid weight gain appears.

## Key Findings

### quoted_fact

- The source identifies post-gonadectomy kittens aged 5-12 months as the primary target population.
- It states that post-gonadectomy energy needs can fall while appetite/intake can rise.
- It recommends growth monitoring and DER-based feeding rather than traditional energy restriction during growth.
- It warns against simply switching kittens under 12 months to adult weight-management or weight-loss food.

### source_supported_conclusion

- This source is a Tier A obesity prevention anchor because it defines who prevention should target.
- It supports separating prevention from treatment in the obesity module.
- It supports owner-communication and growth-monitoring architecture.
- It supports the nutrition boundary that kitten prevention must preserve growth-stage nutrient adequacy.

### llm_inference

- This is the first narrow owner for obesity prevention rather than broad obesity management.
- It pairs with obesity mechanism and metabolic-phenotyping studies but should not be used to make disease-progression claims.

## Claim-Fit Judgment

Strongest safe use:

- prevention branch planning
- post-gonadectomy kitten target population
- growth curve / home weighing workflows
- DER-based feeding and food-scale execution
- nutrition boundary for kittens

Must not control yet:

- validated prevention success rates
- one-size-fits-all DER prescriptions
- adult weight-loss diet use in kittens
- product-specific nutrition claims
- claims that prevention evidence is equivalent to randomized trial proof

## Image Asset TODO

- figures to capture: possible prevention framework or target-population table
- why these matter: prevention frameworks are high-value if the source includes a structured table

## Open Follow-Up Questions

- Which cats does the article identify as priority prevention targets?
- Does it rely on early-life risk data, adult risk data, or expert synthesis?
- Does it separate prevention, recognition, and treatment?
- What claims are feline-specific versus general companion-animal prevention logic?

## Linked Entities

- diseases: obesity
- models:
- endpoints: prevention, target population, risk factors, growth monitoring, DER feeding
- mechanisms: post-gonadectomy appetite increase, reduced energy requirement, growth-trajectory risk
- regulations:
