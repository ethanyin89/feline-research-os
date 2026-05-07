---
id: topic-ibd-endpoint-handbook-bilingual
type: topic
topic: ibd
species: feline
disease: IBD
question_type: endpoints
source_ids: [src-ibd-004, src-ibd-010, src-ibd-013, src-ibd-015, src-ibd-017, src-ibd-019, src-ibd-022]
language: bilingual
last_compiled_at: 2026-04-09
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: draft
---

# Feline IBD Endpoint Handbook, Bilingual

## Quick Helpers / 快速辅助入口

- if you want to trace a claim back down:
  [verify a claim](../../system/indexes/verify-a-claim.md)
- if you want to see real `promote / hold / partial promotion` examples:
  [promotion examples index](../../system/indexes/promotion-examples-index.md)

## What This Page Is / 这页是什么

**EN**  
This is the bilingual derived version of the IBD endpoint handbook. It is for high-reuse internal endpoint discussion and cross-language alignment, not for replacing the raw source layer.

**ZH**  
这是 IBD 终点手册的双语派生版本。它服务于高频内部终点讨论和跨语言对齐，不用于替代原始来源层。

## Best Used For / 最适合拿来做什么

**EN**
- seeing the endpoint hierarchy quickly
- separating operational activity tracking from diagnostic confirmation and frontier markers
- keeping support markers and frontier markers from collapsing into one list

**ZH**
- 快速看清 endpoint hierarchy
- 区分 operational activity tracking、diagnostic confirmation 和 frontier markers
- 防止 support markers 和 frontier markers 被压成一个平面列表

## Not Best Used For / 不最适合拿来做什么

**EN**
- single-marker diagnosis
- replacing biopsy or pathology verification
- treating frontier signals as routine workflow leaders

**ZH**
- single-marker diagnosis
- 替代 biopsy 或 pathology verification
- 把 frontier signals 当成 routine workflow leaders

## Verify Next / 下一步去哪里核实

- [endpoint handbook](endpoint-handbook.md)
- [IBD support and frontier marker memo](../../system/indexes/ibd-support-and-frontier-marker-memo.md)
- [verify a claim](../../system/indexes/verify-a-claim.md)

## Living Page Cue / 活页面提示

**EN**
This is a living compiled page. It should update when better endpoint-stratification, marker-boundary, or pathology-linked evidence changes the hierarchy.

**ZH**
这是一张 living compiled page。只要更好的 endpoint-stratification、marker-boundary 或 pathology-linked 证据改变当前层级，它就应该更新。

## Current Endpoint Map / 当前终点地图

### Lead Operational Branch / 核心操作分支

**EN**
- `clinical activity` belongs to the lead operational branch.
- `FCEAI` is currently the strongest operational activity-and-response tool in the seed corpus.
- activity tracking belongs to chronic-enteropathy management, not to disease-class discrimination.

**ZH**
- `clinical activity` 属于核心操作分支。
- `FCEAI` 目前仍是 seed corpus 里最强的活动度与应答追踪工具。
- 活动度追踪属于 chronic-enteropathy management，不属于疾病类别区分。

### Diagnostic Confirmation Branch / 诊断确认分支

**EN**
- `histopathology` and `biopsy yield` belong to diagnostic confirmation rather than routine disease-activity tracking.
- endpoint logic should stay separate from the `IBD versus small-cell lymphoma` boundary itself.
- pathology endpoints should not be flattened into the same bucket as support biomarkers.

**ZH**
- `histopathology` 和 `biopsy yield` 属于诊断确认层，而不是常规活动度追踪层。
- endpoint logic 应继续和 `IBD versus small-cell lymphoma` 的边界问题分开。
- 病理终点不应和 support biomarkers 被压进同一个桶里。

### Imaging-Support Branch / 影像支持分支

**EN**
- `muscularis thickening` is currently the clearest lymphoma-leaning imaging signal.
- it should be used as suspicion-shaping support, not as stand-alone diagnosis.
- it sits above generic ultrasound abnormality but below biopsy and histopathology authority.

**ZH**
- `muscularis thickening` 目前仍是最清楚的偏 lymphoma 影像信号。
- 它应作为塑造怀疑度的支持信号，而不是单独诊断。
- 它高于一般性的超声异常，但仍低于 biopsy 和 histopathology 的权威性。

### Support-Marker Branch / 支持性标志物分支

**EN**
- `vitamin D` and `fecal S100A12` currently belong to bounded support-marker branches.
- these markers can support burden reading and noninvasive inflammatory context.
- they should not be promoted into one-marker workup leadership.

**ZH**
- `vitamin D` 和 `fecal S100A12` 目前都属于有边界的 support-marker 分支。
- 这些标志物可以帮助读取负担和非侵入性炎症语境。
- 它们不应被提升成 one-marker workup leadership。

### Frontier-Marker Branch / 前沿标志物分支

**EN**
- `metabolomics` is currently the strongest frontier / stratification branch in the seed corpus.
- it looks more promising for future biologic separation than for routine-ready diagnosis.
- it should remain below exclusion-first workup, imaging, biopsy-site strategy, and pathology.

**ZH**
- `metabolomics` 目前仍是 seed corpus 中最强的 frontier / stratification 分支。
- 它更像未来的生物学分层工具，而不是 routine-ready diagnosis。
- 它应继续放在 exclusion-first workup、影像、biopsy-site strategy 和 pathology 之下。

### Lower Marker-Depth Layer / 更低一层的 marker-depth

**EN**
- molecular-expression signals remain a lower marker-depth layer beneath core workup architecture.
- they add boundary pressure and biologic explanation.
- they do not currently justify routine leadership.

**ZH**
- 分子表达信号目前仍属于 core workup architecture 之下的更低一层 marker-depth。
- 它们会增加边界压力并补充生物学解释。
- 但它们目前还不足以主导 routine workup。

## What We Can Defend / 当前可以稳妥主张的内容

**EN**
- feline IBD does not yet have one clean single-marker endpoint that can lead the entire module
- endpoint logic should be modeled as a hierarchy, not a flat list
- `FCEAI` leads the operational activity layer
- support markers and frontier markers should remain separate

**ZH**
- 猫 IBD 目前还没有一个干净的单一标志物终点可以主导整个模块
- endpoint logic 应被建模成 hierarchy，而不是平面清单
- `FCEAI` 主导的是操作性活动度层
- support markers 和 frontier markers 应继续分开

## What We Should Not Overstate / 当前不应说过头的内容

**EN**
- no current marker should be presented as a definitive IBD diagnosis
- activity tracking is not etiologic classification
- frontier markers are not routine-ready workflow replacements
- imaging support is not disease identity proof

**ZH**
- 当前没有任何 marker 应被写成 definitive IBD diagnosis
- 活动度追踪不等于病因学分类
- frontier markers 不是 routine-ready 的流程替代品
- 影像支持不等于疾病身份的证明

## Best Current Anchors / 当前最佳锚点

- [endpoint handbook](endpoint-handbook.md)
- [IBD support and frontier marker memo](../../system/indexes/ibd-support-and-frontier-marker-memo.md)
- [IBD tissue-marker boundary memo](../../system/indexes/ibd-tissue-marker-boundary-memo.md)

## Note / 说明

This bilingual page is a compiled derivative.  
It keeps the raw source layer untouched and does not imply stronger evidence than the underlying source set.

这页双语页属于编译层派生物。  
它不会改动原始来源层，也不意味着它比底层来源集合更强。
