---
id: topic-hcm-endpoint-handbook-bilingual
type: topic
topic: hcm
species: feline
disease: HCM
question_type: endpoint
source_ids: [src-hcm-006, src-hcm-009, src-hcm-010, src-hcm-013, src-hcm-017, src-hcm-019, src-hcm-023, src-hcm-024]
language: bilingual
last_compiled_at: 2026-04-10
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: active
---

# Feline HCM Endpoint Handbook, Bilingual

## Quick Helpers / 快速辅助入口

- if you want to trace a claim back down:
  [verify a claim](../../system/indexes/verify-a-claim.md)
- if you want to see real `promote / hold / partial promotion` examples:
  [promotion examples index](../../system/indexes/promotion-examples-index.md)

## What This Page Is / 这页是什么

**EN**  
This is the bilingual derived version of the HCM endpoint handbook. It is for high-reuse internal endpoint discussion and cross-language alignment, not for replacing the raw source layer.

**ZH**  
这是 HCM 终点手册的双语派生版本。它服务于高频内部终点讨论和跨语言对齐，不用于替代原始来源层。

## Best Used For / 最适合拿来做什么

**EN**
- seeing the endpoint hierarchy quickly
- separating structural confirmation from screening augmentation
- separating injury/severity markers from confirmation logic
- separating troponin, NT-proBNP, and frontier markers by use case

**ZH**
- 快速看清 endpoint hierarchy
- 区分 structural confirmation 和 screening augmentation
- 把 injury/severity markers 和 confirmation logic 分开
- 按 use case 分开 troponin、NT-proBNP 和 frontier markers

## Not Best Used For / 不最适合拿来做什么

**EN**
- one-marker diagnosis
- replacing echocardiography with biomarker shortcuts
- treating pathology depth as routine first-pass authority

**ZH**
- one-marker diagnosis
- 用 biomarker shortcut 替代 echocardiography
- 把 pathology depth 当成 routine first-pass authority

## Verify Next / 下一步去哪里核实

- [endpoint handbook](endpoint-handbook.md)
- [HCM endpoint separation memo](../../system/indexes/hcm-endpoint-separation-memo.md)
- [HCM biomarker use-case memo](../../system/indexes/hcm-biomarker-use-case-memo.md)
- [verify a claim](../../system/indexes/verify-a-claim.md)

## Living Page Cue / 活页面提示

**EN**
This is a living compiled page. It should update when better endpoint-stratification, biomarker ranking, or pathology-linked evidence changes the current hierarchy.

**ZH**
这是一张 living compiled page。只要更好的 endpoint-stratification、biomarker ranking 或 pathology-linked 证据改变当前层级，它就应该更新。

## Biomarker Use Cases / Biomarker 用途分层

**EN**
- troponin belongs most naturally to injury or burden interpretation
- NT-proBNP belongs more naturally to severe-disease flagging and bounded screening augmentation
- novel biomarkers belong to frontier stratification rather than routine authority
- AI stays adjacent to this branch as augmentation, not as biomarker replacement

**ZH**
- troponin 最自然地属于 injury 或 burden interpretation
- NT-proBNP 更自然地属于 severe-disease flagging 和有边界的 screening augmentation
- novel biomarkers 属于 frontier stratification，而不是 routine authority
- AI 在这里应继续被放在 augmentation 旁边，而不是 biomarker replacement

## Current Endpoint Map / 当前终点地图

### Structural Confirmation Branch / 结构确认分支

**EN**
- echocardiography and gross morphometry belong to the lead operational branch
- structural phenotype definition should stay above biomarker and AI branches
- phenotype heterogeneity should remain visible inside this branch

**ZH**
- echocardiography 和 gross morphometry 属于主导的 operational branch
- 结构表型定义应继续放在 biomarker 和 AI 分支之上
- 表型异质性应继续保留在这个分支内部

### Screening-Augmentation Branch / 筛查增强分支

**EN**
- NT-proBNP and computational augmentation belong here
- novel biomarkers and AI belong here as frontier augmentation, not routine authority
- these tools can help suspicion-building or routing
- they should remain below structural confirmation

**ZH**
- NT-proBNP 和 computational augmentation 属于这一层
- novel biomarkers 和 AI 在这里更适合被看成 frontier augmentation，而不是 routine authority
- 这些工具可以帮助 suspicion-building 或 routing
- 它们应继续放在 structural confirmation 之下

### Injury / Severity Branch / 损伤与严重度分支

**EN**
- troponin currently belongs more naturally to injury or severity interpretation
- biomarker elevation can matter without becoming structural authority
- this layer should remain distinct from screening augmentation

**ZH**
- troponin 目前更自然地属于 injury 或 severity interpretation
- biomarker 升高可以有意义，但不能自动获得结构确认的权威性
- 这一层应继续和 screening augmentation 分开

### Pathology-Depth Branch / 病理深度分支

**EN**
- pathology staging belongs in endpoint architecture
- right-ventricular involvement widens phenotype-depth interpretation inside this branch
- end-stage HCM is a remodeled phenotype with fibrosis, dilation, and vascular change
- this branch belongs to depth and severity architecture, not first-pass routine leadership

**ZH**
- pathology staging 属于 endpoint architecture
- right-ventricular involvement 会在这一层内部拉宽 phenotype-depth interpretation
- end-stage HCM 是带有 fibrosis、dilation 和 vascular change 的重构表型
- 这一分支属于 depth 和 severity architecture，而不是 first-pass routine leadership

## What We Can Defend / 当前可以稳妥主张的内容

**EN**
- HCM endpoint logic should be modeled as a hierarchy, not a flat list
- structural confirmation currently outranks biomarkers and AI
- biomarkers and AI are meaningful, but split by use case and maturity level
- biomarker placement is currently clearer than any final biomarker ranking
- pathology depth matters without replacing frontline recognition

**ZH**
- HCM 的 endpoint logic 应被建模成 hierarchy，而不是平面列表
- structural confirmation 目前仍然高于 biomarkers 和 AI
- biomarkers 和 AI 都有意义，但应按 use case 和成熟度分开
- 当前 biomarker placement 比任何最终 biomarker ranking 都更清楚
- pathology depth 很重要，但不能替代 frontline recognition

## What We Should Not Overstate / 当前不应说过头的内容

**EN**
- NT-proBNP is not a reliable universal screen for mild disease
- troponin is not a structural phenotype definition tool
- the vault still does not support one flat biomarker ranking across all contexts
- AI is not routine-ready endpoint authority
- pathology staging is not first-wave clinical confirmation

**ZH**
- NT-proBNP 不是 mild disease 的可靠通用筛查工具
- troponin 不是结构表型定义工具
- 这个 vault 目前仍不支持一个跨所有情境的平面 biomarker ranking
- AI 不是 routine-ready 的 endpoint authority
- pathology staging 不是 first-wave clinical confirmation

## Best Current Anchors / 当前最佳锚点

- [endpoint handbook](endpoint-handbook.md)
- [HCM endpoint separation memo](../../system/indexes/hcm-endpoint-separation-memo.md)
- [HCM biomarker use-case memo](../../system/indexes/hcm-biomarker-use-case-memo.md)
- [HCM frontier augmentation memo](../../system/indexes/hcm-frontier-augmentation-memo.md)
- [HCM phenotype-remodeling bridge memo](../../system/indexes/hcm-phenotype-remodeling-bridge-memo.md)

## Note / 说明

This bilingual page is a compiled derivative.  
It keeps the raw source layer untouched and does not imply stronger evidence than the underlying source set.

这页双语页属于编译层派生物。  
它不会改动原始来源层，也不意味着它比底层来源集合更强。
