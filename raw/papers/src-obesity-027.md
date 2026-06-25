---
id: src-obesity-027
type: source
title: "GLUT4 but not GLUT1 expression decreases early in the development of feline obesity"
source_kind: paper
species: feline
diseases: [obesity]
models: []
endpoints: [ivgtt, glucose_auc, insulin_auc, k_value, glut4_expression, glut1_expression]
jurisdictions: []
evidence_level: original-study
year: 2003
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [obesity, glut4, glut1, insulin-resistance, ivgtt, molecular-endpoint]
links:
  doi: "10.1016/j.domaniend.2003.11.003"
  url: "https://pubmed.ncbi.nlm.nih.gov/15063922/"
  local_assets:
    - "../../raw/deep-extractions/ext-src-obesity-027.md"
evidence_policy:
  quoted_fact:
    - "The study followed 17 domestic cats from lean state to obesity after 6 months of ad libitum food intake."
    - "Body weight increased significantly (P < 0.0001)."
    - "After obesity, IVGTT glucose AUC increased (P = 0.013), insulin AUC increased (P = 0.018), and K-value decreased (P = 0.017), while basal glucose and glycosylated hemoglobin did not change."
    - "Muscle GLUT4 expression decreased (P = 0.002) and fat GLUT4 expression decreased (P = 0.001); GLUT1 did not significantly change in either tissue."
    - "Muscle GLUT4 negatively correlated with insulin AUC (r2 = 0.36, P = 0.004), and fat GLUT4 negatively correlated with insulin AUC (r2 = 0.18, P = 0.040)."
  source_supported_conclusion:
    - "GLUT4 decline is an early molecular event in feline obesity before routine static glucose markers become abnormal."
    - "The unchanged GLUT1 result makes the glucose-transporter change more specific to insulin-responsive transport."
    - "Dynamic glucose tolerance and tissue GLUT4 are more sensitive early endpoints than fasting glucose alone."
  llm_inference:
    - "Use this as mechanism evidence for early feline obesity-related insulin resistance, not as proof that obesity inevitably progresses to diabetes."
  study_design: "前后对照机制研究，17只家猫从瘦状态经6个月自由采食形成肥胖，比较IVGTT指标及肌肉/脂肪GLUT4和GLUT1表达"
  core_argument: "猫肥胖早期即使基础血糖和糖化血红蛋白仍正常，动态葡萄糖处理和胰岛素反应已经异常，且肌肉和脂肪GLUT4而非GLUT1表达下降，提示胰岛素依赖性葡萄糖转运受损是早期机制事件。"
  implicit_premise: "IVGTT、胰岛素AUC和组织葡萄糖转运蛋白比空腹血糖更能捕捉肥胖早期胰岛素抵抗。"
  unexpected_finding: "基础血糖和糖化血红蛋白未改变并不削弱结论，反而说明GLUT4下降发生在临床可见葡萄糖不耐受之前。"
  title_gap: "标题强调GLUT4下降，但真正价值是把体重增加、动态糖耐量异常和组织分子改变连成早期肥胖胰岛素抵抗证据链。"
  evidence_boundary: "当前deep extraction主要基于摘要和PubMed元数据，不能还原全文中的饲料组成、活检部位、Western blot归一化细节或具体蛋白下降幅度；相关性不能证明GLUT4下降是唯一因果机制。"
---

# GLUT4 but not GLUT1 expression decreases early in the development of feline obesity

## Evidence-Depth Caveat

This card is linked to an abstract-level deep extraction. It supports early-mechanism claims about feline obesity, IVGTT changes, and GLUT4/GLUT1 expression, but it does not replace a full Elsevier article audit.

## One-Line Summary

In 17 cats followed from lean state to obesity, dynamic glucose handling and insulin response changed before basal glucose or glycosylated hemoglobin, while GLUT4 decreased in muscle and fat and GLUT1 did not.

## Why It Matters For Feline Obesity

This source is a molecular endpoint anchor for the obesity-to-insulin-resistance branch:

- it shows early dynamic metabolic abnormality before static glucose markers change
- it separates insulin-responsive GLUT4 from basal GLUT1
- it links GLUT4 expression to insulin AUC

## Key Findings

### quoted_fact

- 17 domestic cats were compared before and after 6 months of ad libitum feeding.
- Body weight increased significantly (P < 0.0001).
- After obesity, glucose AUC increased (P = 0.013), insulin AUC increased (P = 0.018), and K-value decreased (P = 0.017).
- Basal glucose and glycosylated hemoglobin did not change.
- Muscle GLUT4 decreased (P = 0.002), fat GLUT4 decreased (P = 0.001), and GLUT1 did not significantly change.
- Muscle and fat GLUT4 negatively correlated with insulin AUC.

### source_supported_conclusion

- GLUT4 is a useful early molecular endpoint for feline obesity-related insulin resistance.
- Fasting glucose alone can miss early obesity-associated metabolic strain.
- The unchanged GLUT1 result narrows the finding to insulin-responsive glucose transport rather than global transporter loss.

### llm_inference

- This paper supports a mechanism bridge, not a clinical prediction rule or treatment recommendation.

## Claim-Fit Judgment

Strongest safe use:

- early feline obesity mechanism
- IVGTT endpoint selection
- GLUT4 molecular endpoint framing

Must not control yet:

- reader-facing medical advice
- numeric claims
- obesity prevalence claims
- progression inevitability from obesity to diabetes
- treatment recommendations

## Image Asset TODO

- figures/tables to capture: full-text GLUT4/GLUT1 expression and IVGTT result figures if accessible later
- why these matter: they would strengthen paragraph-level trace beyond the PubMed abstract

## Open Follow-Up Questions

- What were the exact biopsy sites and Western blot normalization methods?
- What was the diet composition during ad libitum feeding?
- Were sex/neuter status effects assessed?

## Linked Entities

- diseases: obesity
- models:
- endpoints: IVGTT, glucose AUC, insulin AUC, K-value, GLUT4, GLUT1
- mechanisms: insulin-responsive glucose transport, early insulin resistance
