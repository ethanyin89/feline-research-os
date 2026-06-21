---
id: src-ckd-030
type: source
title: "Investigating the Efficacy of Kidney-Protective Lactobacillus Mixture-Containing Pet Treats in Feline Chronic Kidney Disease and Its Possible Mechanism"
source_kind: paper
species: feline
diseases: [CKD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2024
status: extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ckd, investigating, efficacy, kidney-protective, lactobacillus, mixture-containing, pet, treats]
links:
  doi: "10.3390/ani14040630"
  url: "https://www.mdpi.com/2076-2615/14/4/630"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The open full article reports a single-arm eight-week pilot: 12 cats enrolled, 6 completed, and 6 dropped out."
    - "The six completers included one stage 2 and five stage 3 CKD cats."
    - "Plasma TMAO, indoxyl sulfate, p-cresyl sulfate, and phenyl sulfate changes were not statistically significant; serum phosphate significantly increased."
  source_supported_conclusion:
    - "The study supports feasibility and trial-design learning for paired microbiome, toxin, renal, and owner-reported endpoints."
    - "It does not demonstrate probiotic efficacy, uremic-toxin reduction, or controlled CKD improvement."
  llm_inference:
    - "Microbiome changes and creatinine movement remain hypothesis-generating because there was no control group and only six completers."
  # V2 enhanced fields
  study_design: "单臂开放标签 8 周试验，12 只猫入组仅 6 只完成，益生菌零食（Lacticaseibacillus paracasei + Lactiplantibacillus plantarum）"
  core_argument: "益生菌零食在猫 CKD 中的可行性和试验设计经验——主要价值在于展示为什么需要更大规模对照试验"
  implicit_premise: "假设 50% 脱落率不会系统性偏倚完成者结果；假设微生物组变化可预测临床获益"
  unexpected_finding: "血清磷酸盐显著升高——任何未来益生菌 CKD 研究必须包括矿物质监测"
  title_gap: "标题说益生菌疗效，但真正发现是试验设计教训：50% 脱落、无对照组、尿毒症毒素无显著变化、磷反而升高——主要价值是展示为什么需要更大规模对照试验"
  evidence_boundary: "无对照组、无随机化、无盲法；尿毒症毒素（TMAO、IS、PCS、PS）变化均不显著；不能支持益生菌疗效主张"
---

# Investigating the Efficacy of Kidney-Protective Lactobacillus Mixture-Containing Pet Treats in Feline Chronic Kidney Disease and Its Possible Mechanism

## Evidence-Depth Caveat

This card is based on complete open publisher HTML. It is deep-extracted as a feasibility and research-design source, not as treatment evidence.

## Deep Extraction, 2026-06-06

- Access: complete MDPI publisher HTML.
- Worksheet: `system/indexes/src-ckd-030-deep-extraction-round1.md`.
- Cross-source memo: `system/indexes/ckd-uremic-toxin-microbiome-bridge-memo-20260606.md`.
- Promotion boundary: no probiotic, toxin-lowering, stage-improvement, or product recommendation.

## One-Line Summary

Single-arm six-completer probiotic-treat pilot that is useful for endpoint and failure-mode design, but insufficient for efficacy claims.

## Why It Matters For Feline CKD

This source tests the intervention side of the microbiome and uremic-toxin hypothesis. Its main value is showing why a larger controlled trial is still required.

## Key Findings

### quoted_fact

- Twelve cats enrolled and six completed the eight-week study.
- The study was single-arm, open-label, and had no concurrent control.
- Creatinine shifted lower with `p = 0.06`.
- TMAO, IS, PCS, and PS changes were not statistically significant.
- Serum phosphate significantly increased.

### source_supported_conclusion

- The study demonstrates feasibility of paired microbiome, toxin, kidney-function, and owner-reported measurements.
- Alpha diversity and selected taxa changed, but predicted microbial function does not prove a clinical mechanism.
- Attrition, palatability, mineral monitoring, and concurrent-care control are mandatory in future studies.

### llm_inference

- The creatinine and owner-reported changes may reflect treatment, concurrent care, regression to the mean, or ordinary variation.

## Claim-Fit Judgment

Strongest safe use:

- probiotic trial-design input
- adherence and attrition failure-mode mapping
- microbiome and toxin endpoint selection

Must not control:

- probiotic efficacy
- uremic-toxin reduction
- CKD stage improvement
- class-level or product-level recommendations

## Study Design Details

### Population and Attrition

| Metric | Value |
|--------|-------|
| Enrolled | 12 cats |
| Completed | 6 cats (50%) |
| Dropped out | 6 cats |
| Stage 2 completers | 1 cat |
| Stage 3 completers | 5 cats |

### Intervention

- Strains: Lacticaseibacillus paracasei MFM 18, Lactiplantibacillus plantarum MFM 30-3
- Dose: ~2.79-3.93 x 10^8 CFU/cat/day
- Duration: 8 weeks
- Format: Treats administered with usual CKD treatment and diet

### Key Design Limitations

- No concurrent control group
- No randomization
- No blinding
- 50% dropout rate (palatability-related in some cases)
- Results cannot be generalized to probiotics as a class

### Uremic Toxin Results

| Toxin | Statistical Significance |
|-------|-------------------------|
| TMAO | p > 0.05 (not significant) |
| Indoxyl sulfate | p > 0.05 (not significant) |
| p-Cresyl sulfate | p > 0.05 (not significant) |
| Phenyl sulfate | p > 0.05 (not significant) |

### Concerning Signal

Serum phosphate **significantly increased** after treatment - any future efficacy study must include mineral monitoring.

### Creatinine Movement

- Shifted lower with p = 0.06 (not statistically significant)
- One cat changed from stage 3 to stage 2
- Cannot separate treatment effect from regression to mean, hydration, concurrent care

## Image Assets

No figures captured. Microbiome sequencing figures are exploratory and do not warrant promotion without controlled trial validation.

## Linked Entities

- diseases: CKD (stages 2-3)
- models: single-arm pilot, 16S microbiome sequencing, PICRUSt pathway prediction
- endpoints: creatinine, TMAO, indoxyl sulfate, p-cresyl sulfate, phosphate, owner-reported QoL
- mechanisms: gut-derived uremic toxins, microbiome modulation
- regulations: none applicable
