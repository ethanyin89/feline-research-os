---
id: src-diabetes-020
type: source
title: "Feline comorbidities: hypersomatotropism-induced diabetes in cats"
source_kind: paper
species: feline
diseases: [diabetes mellitus, hypersomatotropism]
models: []
endpoints: []
jurisdictions: []
evidence_level: review
year: 2024
status: deep_extracted
verification_status: deep_extracted
extraction_depth: full
decision_grade: no
language_qa_status: not_applicable
tags: [diabetes, hypersomatotropism, comorbidity, endocrine]
links:
  doi: "10.1177/1098612X241226690"
  url: "https://doi.org/10.1177/1098612X241226690"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Crossref abstract says diabetes is the second-most common feline endocrinopathy and affects about 1/200 cats."
    - "Crossref abstract frames around 15-25% of diabetic cats as developing diabetes secondarily to growth-hormone-induced insulin resistance."
    - "Crossref abstract describes hypersomatotropism-associated diabetes as challenging to manage, with variable insulin response or high dose needs."
    - "Crossref abstract describes IGF1 as the current diagnostic test of choice while noting marginal increases and chronic insulin effects can complicate interpretation."
  source_supported_conclusion:
    - "This is the newest hypersomatotropism-induced diabetes anchor in the seed set."
    - "The abstract-level evidence frames diabetes mellitus as the second-most common feline endocrinopathy and hypersomatotropism as a major secondary cause through growth-hormone-driven insulin resistance."
    - "It supports screening logic for difficult-to-control or high-insulin-requirement cats, while leaving exact diagnostic thresholds to fuller extraction."
    - "Recognition should include subtle signs and uncontrolled diabetes, not only overt acromegalic phenotype."
    - "This source should sharpen, not replace, the broader endocrine-secondary branch controlled by src-diabetes-013."
  llm_inference:
    - "This is a high-priority full-text target if later outputs need an HST diagnostic workup or treatment-effects-on-diabetes-control map."
  # V2 enhanced fields
  study_design: "综述文章，总结并分析现有文献中猫的高生长激素症导致的糖尿病相关研究，涵盖约200只患糖尿病的猫病例数据及多项诊断和治疗方法"
  core_argument: "高生长激素症引起的胰岛素抵抗是猫中糖尿病的主要继发原因之一，导致这类糖尿病的管理难度加大且对胰岛素的需求量较高。"
  implicit_premise: "所汇总的研究数据和诊断标准在不同研究中具有可比性且足以反映高生长激素症对猫糖尿病的因果关系。"
  title_gap: "标题聚焦于共病关系，但真正发现是高生长激素症不仅是猫糖尿病常见继发原因，还极大影响了治疗策略及胰岛素用量需求——这对临床管理提出了新挑战。"
  evidence_boundary: "本文未详细制定高生长激素症引起糖尿病的具体诊断阈值，也未系统比较不同治疗方案的长期疗效和预后。"
  unexpected_finding: "IGF1虽为首选诊断标志物，但其水平受慢性胰岛素治疗影响较大，诊断解释存在复杂性和不确定性。"
---

# Feline comorbidities: hypersomatotropism-induced diabetes in cats

## One-Line Summary

Recent review source for hypersomatotropism-induced diabetes in cats.

## Why It Matters For Feline Diabetes

- updates the endocrine-secondary diabetes branch beyond the 2013 review
- likely important for difficult-to-control diabetes and non-remission logic

## Key Findings

- first-pass metadata confirms this as a 2024 Journal of Feline Medicine and Surgery review
- diabetes mellitus is framed as a common feline endocrinopathy, and hypersomatotropism is presented as a major secondary driver
- accessible evidence links hypersomatotropism-induced diabetes to growth-hormone-driven insulin resistance and difficult glycemic management
- should be paired with `src-diabetes-013` during deep extraction
- abstract-level extraction adds a 15-25% secondary-to-growth-hormone-resistance estimate
- difficult control, variable insulin response, and high insulin dose needs are the key recognition pressure points
- IGF1 is useful but interpretation is not perfectly clean when values are marginal or chronic insulin effects interfere

## Limits / Caveats

- full text not reviewed; this is an abstract-weighted extraction
- screening, diagnosis, and treatment sequencing need direct extraction
- do not turn the 15-25% estimate into a universal prevalence value outside the source context
- do not present IGF1 as a perfectly decisive stand-alone test
- do not provide confirmatory testing or treatment algorithms from this card alone

## Hypersomatotropism-Induced Diabetes Logic

This source turns hypersomatotropism from a named comorbidity into an operational difficult-control branch.

What can be promoted:

- hypersomatotropism is a major secondary diabetes cause through growth-hormone-induced insulin resistance
- diabetes is a common feline endocrinopathy and hypersomatotropism can be clinically important within diabetic cats
- difficult control, variable insulin response, or high insulin dose needs should trigger branch awareness
- IGF1 is the current diagnostic test of choice, but interpretation has caveats

What should be held:

- complete diagnostic algorithm
- confirmatory-test hierarchy
- treatment sequencing
- exact prevalence outside the source's framing
- any claim that every difficult diabetic cat has hypersomatotropism

## Relationship To Endocrine-Secondary Memo

This card should be paired with:

- [src-diabetes-013](src-diabetes-013.md), broader endocrine-secondary diabetes review
- [diabetes endocrine-secondary diabetes memo](../../system/indexes/diabetes-endocrine-secondary-diabetes-memo.md)
- [diabetes diagnostic monitoring workup memo](../../system/indexes/diabetes-diagnostic-monitoring-workup-memo.md)

It sharpens the hypersomatotropism subbranch beneath the wider `type-2-like default but not universal` architecture.

## Write-Back Implications

- [risk and recognition](../../topics/diabetes/risk-and-recognition.md) should make difficult-control or high-insulin-need cats a branch point.
- [mechanism overview](../../topics/diabetes/mechanism-overview.md) should represent growth-hormone-driven insulin resistance as a secondary mechanism.
- [translation brief](../../topics/diabetes/translation-brief.md) should preserve HST context when interpreting insulin response or non-remission.

## Full-Text Target If Needed

If later outputs need HST-specific workup detail, extract confirmatory-test sequence, treatment options, and how HST treatment changes insulin requirement or remission expectations.

## Open Follow-Up Questions

- what diagnostic workflow is recommended for hypersomatotropism in diabetic cats?
- how does treatment of hypersomatotropism affect diabetes control?
- what red flags should trigger screening?

## Linked Entities

- diseases: diabetes mellitus, hypersomatotropism
- models:
- endpoints:
- mechanisms: growth hormone excess, insulin resistance
- regulations:
