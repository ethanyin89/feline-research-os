---
id: out-ibd-dossier-20260409-v1-zh
type: output
output_kind: dossier
language: zh
topic: ibd
question: "猫 IBD 在疾病框架、诊断流程、marker hierarchy、病理深度与早期治疗上的第一版可用内部 dossier 是什么？"
source_ids: [src-ibd-001, src-ibd-003, src-ibd-004, src-ibd-007, src-ibd-009, src-ibd-010, src-ibd-011, src-ibd-012, src-ibd-013, src-ibd-014, src-ibd-015, src-ibd-016, src-ibd-017, src-ibd-019, src-ibd-022]
generated_at: 2026-04-09
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: draft
evidence_policy:
  quoted_fact: []
  source_supported_conclusion: []
  llm_inference: []
---

# 猫 IBD 内部 Dossier V1

Derived from:

- [out-ibd-dossier-20260409-v1-working-en.md](out-ibd-dossier-20260409-v1-working-en.md)

## 用户问题

猫 IBD 在疾病框架、诊断流程、marker hierarchy、病理深度与早期治疗上的第一版可用内部 dossier 是什么？

## 执行摘要

基于当前 seed corpus，猫 IBD 已经可以作为一个可用的内部研究对象被建模，但前提是采用正确的架构。

当前模块不应被写成一个孤立、纯净、边界明确的疾病，而应被放在 `feline chronic enteropathy` 框架中理解。当前最强的组织逻辑是：

- diagnosis of exclusion
- IBD versus small-cell alimentary lymphoma boundary handling
- activity 与 identity 的分离
- marker hierarchy，而不是 generic biomarker flattening
- diet-first 但边界明确的 treatment framing

当前最重要的实际含义不是“哪个 biomarker 能诊断 IBD”，而是“哪组诊断流程层级，能最可辩护地把 inflammatory chronic enteropathy 和邻近疾病状态分开”。

这是一份中文派生 dossier，不应被误读为 bilingual dossier 或 decision-grade recommendation。

## 疾病框架

### quoted_fact

- broad review material 将 feline IBD 定义为 diagnosis of exclusion。
- dietary intolerance 或 allergy 以及 well-differentiated alimentary lymphosarcoma 都可能在临床和组织学上模拟 IBD。
- 后续 chronic-enteropathy 研究也持续使用更宽的 CE 框架，而不是狭义单标志物 IBD 框架。

### source_supported_conclusion

- 当前疾病对象最合理的表达是 `IBD within chronic enteropathy`。
- 系统需要同时保留 `idiopathic IBD depth` 与 `boundary disease pressure`。

## 诊断流程层

### source_supported_conclusion

- `FCEAI` 属于活动度与反应追踪层，而不是疾病类别区分层。
- `Biopsy-site selection` 属于核心诊断流程分支。
- `Muscularis thickening` 是能改变怀疑方向的信号，但不应超越 tissue diagnosis。

## Boundary 层

### source_supported_conclusion

- 当前 boundary branch 已经明确是 `multimodal`。
- tissue 与 molecular markers 能增加边界压力，但都不足以支持 one-marker workup leadership。
- `Metabolomics` 是当前最强的 frontier-separation branch，但仍低于 routine-ready 状态。

## Pathology 与 Chronicity 层

### source_supported_conclusion

- `Idiopathic IBD` 现在已经有了自己的 pathology-depth branch。
- `Fibrosis` 应被视为 structural chronicity 与 burden，而不是背景 histology。
- pathology depth 在实际诊断中仍低于 exclusion-first workup。

## Early Treatment 层

### source_supported_conclusion

- `Hydrolysed diet response` 是当前最清楚的直接治疗锚点。
- 当前最稳妥的实践框架是 `diet-first chronic-enteropathy management`。
- 现有治疗证据还不足以支持强 idiopathic-IBD-specific efficacy 语言。

## 不确定性 / 限制

- 这份中文 dossier 是由 working-English dossier 派生而来，不代表更强证据层。
- 当前文件只显式引用了部分高相关 source，不应被误读为 IBD 模块只完成了这些基础材料。
- IBD 目前仍无 jurisdiction-specific regulatory layer。
- 当前文件仍是 `decision_grade: no`。
