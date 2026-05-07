---
id: topic-hcm-diagnostic-workup-bilingual
type: topic
topic: hcm
species: feline
disease: HCM
question_type: recognition
source_ids: [src-hcm-001, src-hcm-007, src-hcm-008, src-hcm-009, src-hcm-010, src-hcm-013, src-hcm-021, src-hcm-023]
language: bilingual
last_compiled_at: 2026-04-10
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: active
---

# Feline HCM Diagnostic Workup, Bilingual

## Quick Helpers / 快速辅助入口

- if you want to trace a claim back down:
  [verify a claim](../../system/indexes/verify-a-claim.md)
- if you want to see real `promote / hold / partial promotion` examples:
  [promotion examples index](../../system/indexes/promotion-examples-index.md)

## What This Page Is / 这页是什么

**EN**  
This is the bilingual derived version of the HCM diagnostic-workup layer. It is for high-reuse internal workup discussion and cross-language alignment, not for replacing the raw source layer.

**ZH**  
这是 HCM diagnostic-workup 层的双语派生版本。它服务于高频内部诊断流程讨论和跨语言对齐，不用于替代原始来源层。

## Current Workup Architecture / 当前 workup 架构

### Clinical Suspicion / 临床怀疑层

**EN**
- workup should start from cardiomyopathy-aware clinical suspicion
- phenotype suspicion, age, and genotype context all matter here
- this layer should not be collapsed into one test trigger

**ZH**
- workup 应从带 cardiomyopathy 意识的临床怀疑开始
- phenotype suspicion、年龄和 genotype context 在这里都重要
- 这一层不应被压成单一测试触发器

### Structural Confirmation / 结构确认层

**EN**
- echocardiographic phenotype definition remains the operationally decisive branch
- gross morphometric discrimination also belongs here
- mild-to-moderate thickening should stay in an exclusion-aware zone

**ZH**
- echocardiographic phenotype definition 仍然是操作上最关键的分支
- gross morphometric discrimination 也属于这一层
- mild-to-moderate thickening 应继续保留在带排除意识的区域里

### Screening Augmentation / 筛查增强层

**EN**
- NT-proBNP and computational detection logic belong here
- these tools can help routing or suspicion-building
- they should remain below structural confirmation

**ZH**
- NT-proBNP 和 computational detection logic 属于这一层
- 这些工具可以帮助 routing 或 suspicion-building
- 它们应继续放在结构确认之下

### Overclaim Boundary / 过度主张边界层

**EN**
- biomarker support is not structural confirmation
- severe-disease flags are not the same as mild-disease screening competence
- genotype pressure is not the same as current confirmed phenotype
- AI is not routine first-wave authority

**ZH**
- biomarker support 不等于结构确认
- severe-disease flag 不等于 mild-disease screening competence
- genotype pressure 不等于 current confirmed phenotype
- AI 不是 routine first-wave authority

## What We Can Defend / 当前可以稳妥主张的内容

**EN**
- HCM workup is structure-first by design
- screening augmentation belongs in the module, but below confirmation
- mild-to-moderate thickening needs exclusion-aware interpretation
- age and genotype pressure can modify workup interpretation without becoming diagnosis by themselves

**ZH**
- HCM workup 天然是 structure-first 的
- screening augmentation 属于这个模块，但应放在 confirmation 之下
- mild-to-moderate thickening 需要带排除意识的解释
- 年龄和 genotype pressure 可以修正 workup interpretation，但不能单独变成 diagnosis

## What We Should Not Overstate / 当前不应说过头的内容

**EN**
- no one-test shortcut should replace structural confirmation
- NT-proBNP is not a reliable mild-to-moderate HCM screen
- mutation status is not stand-alone diagnosis
- AI should not be written as if it outranks structural workup

**ZH**
- 不应让任何 one-test shortcut 取代结构确认
- NT-proBNP 不是可靠的 mild-to-moderate HCM 筛查工具
- mutation status 不是 stand-alone diagnosis
- 不应把 AI 写成比 structural workup 更高的权威

## Best Current Anchors / 当前最佳锚点

- [HCM diagnostic-workup memo](../../system/indexes/hcm-diagnostic-workup-memo.md)
- [risk and recognition bilingual](risk-and-recognition-bilingual.md)
- [endpoint handbook bilingual](endpoint-handbook-bilingual.md)

## Note / 说明

This bilingual page is a compiled derivative.  
It keeps the raw source layer untouched and does not imply stronger evidence than the underlying source set.

这页双语页属于编译层派生物。  
它不会改动原始来源层，也不意味着它比底层来源集合更强。
