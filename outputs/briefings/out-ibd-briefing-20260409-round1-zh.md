---
id: out-ibd-briefing-20260409-round1-zh
type: output
output_kind: briefing
language: zh
topic: ibd
question: "基于当前 seed corpus，猫 IBD 在诊断流程、疾病边界、marker 与早期治疗上的第一版可用内部视图是什么？"
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

# 内部简报：猫 IBD Round 1

Derived from:

- [out-ibd-briefing-20260409-round1-working-en.md](out-ibd-briefing-20260409-round1-working-en.md)

## 用户问题

基于当前 seed corpus，猫 IBD 在诊断流程、疾病边界、marker 与早期治疗上的第一版可用内部视图是什么？

## 执行摘要

当前证据支持把猫 IBD 放在更宽的 `chronic enteropathy` 框架内理解，而不是把它当成一个可以靠单一检测、单一 marker、或单一句诊断定义清楚的对象。

当前最强的组织性结论是：猫 IBD 应该被建模为 `排除式诊断`，并始终保留 `IBD 与 small-cell alimentary lymphoma 边界问题`。

这条边界并不是由单一层解决的。在当前 corpus 里，它同时受到以下层级影响：

- 通过 `FCEAI` 表达的临床活动度逻辑
- 以 `muscularis thickening` 为代表的影像支持
- 以 `duodenum versus ileum` 为代表的取样位点策略
- tissue-marker 与 molecular-marker 带来的边界压力
- frontier metabolomic separation

当前 corpus 还清楚支持另外三点。

第一，`FCEAI` 是有用的，但它属于 chronic-enteropathy 的活动度与反应追踪层，不属于疾病类别区分层。

第二，`fibrosis` 现在已经足够强，应该被视为 structural chronicity branch，而不是背景病理描述。

第三，治疗层仍然明显薄于诊断层，但 `hydrolysed diet response` 现在已经是最清楚的早期实践锚点。即便如此，这条证据仍然和 food-responsive disease 有重叠，不能直接写成 idiopathic-IBD-specific proof。

这是一份中文派生简报，不应被误读为更高证据强度或 decision-grade 结论。

## 证据支持要点

### quoted_fact

- broad review material 将 feline IBD 定义为 diagnosis of exclusion。
- 同一综述指出 dietary intolerance 或 allergy 以及 well-differentiated alimentary lymphosarcoma 在临床和组织学上都可能模拟 IBD。
- FCEAI 研究给出了可追踪治疗反应的 chronic-enteropathy activity index。
- duodenal 与 ileal biopsy 研究显示两处位点一致性较差，且部分 small-cell lymphoma 仅在 ileum 被识别。
- ultrasound 研究显示 muscularis propria thickening 与 lymphoma 的关联强于与 IBD 的关联。
- metabolomic 研究显示 IBD 与 small-cell lymphoma 之间存在 frontier 级别的区分信号，但仍属研究层。
- vitamin D 与 fecal S100A12 研究都提示疾病相关异常，但都不能干净地区分 IBD 与 lymphoma。
- fibrosis 研究提示 intestinal fibrosis 在 feline chronic inflammatory enteropathy 中常见，并与较低体重和较低白蛋白相关。
- hydrolysed diet 研究提示小样本 chronic-enteropathy 队列中，单用饮食即可带来快速临床改善。

### source_supported_conclusion

- 当前 IBD 模块的首要组织原则应是 `排除式诊断流程`，而不是 biomarker-first diagnosis。
- `small-cell alimentary lymphoma` 应当被视为 IBD 模块内部的核心边界分支，而不是远端 differential。
- `FCEAI` 应被用作活动度与治疗反应 endpoint，而不是炎症性与肿瘤性疾病的区分器。
- `muscularis thickening` 是偏 lymphoma 的影像信号，但不是单独诊断。
- `biopsy-site choice` 是诊断的一部分，而不只是操作细节。
- `vitamin D` 与 `fecal S100A12` 属于 support-marker 层；`metabolomics` 属于更强但仍非 routine-ready 的 frontier 层。
- `fibrosis` 应被建模为位于 support-marker 之上的 structural chronicity branch。
- `hydrolysed diet response` 是当前最清楚的早期治疗锚点，但必须保留 mixed chronic-enteropathy 与 food-response 的边界。

### llm_inference

- 下一步最有价值的 compiled milestone 可能是 IBD output matrix，把诊断流程主导层、边界压力层、support-marker、frontier-marker 与 early-treatment anchor 明确分层。
- 当前 IBD 模块已经足以支持中文内部输出，但还不足以支持强 treatment-hierarchy 结论。

## 不确定性 / 限制

- 这份中文简报是从 working-English 输出层派生而来，不代表比底层证据更强。
- 当前简报建立在 first-round extraction 之上，不是对每篇全文逐行核读后的最终结论。
- 当前简报只压缩了部分最相关 source，不应被误读为 IBD 模块仍停留在 seed-only 状态。
- 治疗证据仍然薄于诊断与病理证据。
