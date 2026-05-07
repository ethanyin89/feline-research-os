---
id: topic-ibd-synthesis-index-bilingual
type: topic
topic: ibd
species: feline
disease: IBD
question_type: synthesis
language: bilingual
source_ids: [src-ibd-001, src-ibd-002, src-ibd-003, src-ibd-004, src-ibd-005, src-ibd-006, src-ibd-007, src-ibd-008, src-ibd-009, src-ibd-010, src-ibd-011, src-ibd-012, src-ibd-013, src-ibd-014, src-ibd-015, src-ibd-016, src-ibd-017, src-ibd-018, src-ibd-019, src-ibd-020, src-ibd-021, src-ibd-022, src-ibd-023, src-ibd-024]
last_compiled_at: 2026-04-23
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: active
---

# Feline IBD Synthesis Index, Bilingual

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| ISB1 | IBD synthesis prioritizes workup sequence and IBD-versus-lymphoma boundary handling | B | src-ibd-003, src-ibd-010, src-ibd-011, src-ibd-015, src-ibd-016, src-ibd-019 | bilingual derived layer |
| ISB2 | Biomarker and omics branches are support/frontier layers, not routine leaders | B | src-ibd-004, src-ibd-013, src-ibd-017 | no one-marker claim |
| ISB3 | Diet-first treatment remains bounded by chronic-enteropathy and food-response overlap | B | src-ibd-014, src-ibd-021 | not final treatment ranking |
| ISB4 | `src-ibd-009` is deep-extracted workflow support for pathology-report normalization, not decision-grade diagnosis | C | src-ibd-009 | keep below biopsy, imaging, and pathologist interpretation |

## Quick Helpers / 快速辅助入口

- if you want to trace a claim back down:
  [verify a claim](../../system/indexes/verify-a-claim.md)
- if you want to see real `promote / hold / partial promotion` examples:
  [promotion examples index](../../system/indexes/promotion-examples-index.md)

## What This Page Is / 这页是什么

**EN**  
This is the bilingual derived version of the main IBD synthesis page. It is for high-reuse internal discussion and cross-language alignment, not for replacing the raw source layer.

**ZH**  
这是 IBD 主综合页的双语派生版本。它服务于高频内部讨论和跨语言对齐，不用于替代原始来源层。

## Strongest Current Conclusions / 当前最稳的结论

### Core Backbone / 核心骨架

**EN**
- Feline IBD is best modeled inside a wider chronic-enteropathy frame.
- The first major compression problem is not treatment ranking but `IBD versus small-cell alimentary lymphoma` boundary handling.
- The strongest current operational backbone is:
  - exclusion-first diagnostic architecture
  - site-aware biopsy logic
  - imaging-aware suspicion adjustment
  - marker hierarchy rather than one-marker simplification

**ZH**
- 猫 IBD 最适合被放在更宽的 chronic-enteropathy 框架内建模。
- 当前第一位的压缩问题不是治疗排序，而是 `IBD versus small-cell alimentary lymphoma` 的边界处理。
- 当前最稳的操作骨架是：
  - 以排除式诊断为核心的架构
  - 带位点意识的 biopsy 逻辑
  - 带影像分支的怀疑调整
  - marker hierarchy，而不是单标志物简化

### Workup / 诊断流程

**EN**
- `FCEAI` belongs to activity tracking, not disease-class discrimination.
- `Muscularis thickening` is lymphoma-leaning support, not stand-alone diagnosis.
- `Biopsy-site choice` is part of the diagnosis itself, not just a procedural detail.

**ZH**
- `FCEAI` 属于活动度追踪层，不属于疾病类别区分层。
- `Muscularis thickening` 是偏 lymphoma 的支持信号，不是单独诊断。
- `Biopsy-site choice` 属于诊断本身，而不只是操作细节。

### Marker Hierarchy / 标志物分层

**EN**
- Support markers and frontier markers should not be flattened into one biomarker bucket.
- `vitamin D` and `fecal S100A12` currently belong to the support-marker layer.
- `metabolomics` is the strongest current frontier-separation branch, but still not routine-ready.

**ZH**
- support markers 和 frontier markers 不应被压成一个 biomarker bucket。
- `vitamin D` 和 `fecal S100A12` 目前属于 support-marker 层。
- `metabolomics` 是当前最强的 frontier-separation 分支，但仍未到 routine-ready。

### Pathology And Chronicity / 病理与慢性化

**EN**
- `Idiopathic IBD` now has its own pathology-depth branch.
- `fibrosis` should be modeled as a structural chronicity branch, not as background histology.
- Microbiota and mucosal-inflammatory differences deepen explanation, but do not yet lead routine workup.

**ZH**
- `Idiopathic IBD` 现在已经有了自己的 pathology-depth 分支。
- `fibrosis` 应被建模为结构性慢性化分支，而不是背景病理。
- microbiota 和黏膜炎症差异会加深解释层，但还不足以主导 routine workup。

### Translation / 转化层

**EN**
- `hydrolysed diet response` is the cleanest current early treatment anchor.
- The safest practical frame remains `diet-first chronic-enteropathy management`.
- Early treatment signal still overlaps with food-responsive disease and should not be overstated as idiopathic-IBD-specific proof.

**ZH**
- `hydrolysed diet response` 是当前最清楚的早期治疗锚点。
- 目前最稳妥的实践框架仍然是 `diet-first chronic-enteropathy management`。
- 早期治疗信号仍与 food-responsive disease 重叠，不应被夸成 idiopathic-IBD-specific proof。

## What Still Feels Weak / 当前仍然偏弱的地方

**EN**
- treatment primary-study density
- jurisdiction-specific regulatory strategy
- extension branches such as eosinophilic fibroplasia and granulomatous colitis
- final treatment ranking

**ZH**
- 治疗原始研究密度
- jurisdiction-specific regulatory strategy
- eosinophilic fibroplasia 和 granulomatous colitis 等 extension branches
- 最终治疗排序

## What We Can Defend / 当前可以稳妥主张的内容

**EN**
- feline IBD should be held inside chronic enteropathy
- disease-boundary compression is at least as important as treatment compression
- workup architecture should lead before biomarkers
- fibrosis and idiopathic pathology belong above marker trivia, but below decision-grade certainty

**ZH**
- feline IBD 应被稳定地放在 chronic enteropathy 内理解
- 疾病边界压缩至少和治疗压缩同等重要
- 诊断流程架构应先于 biomarker 叙事
- fibrosis 和 idiopathic pathology 比零散 marker 更重要，但还不到 decision-grade certainty

## What We Should Not Overstate / 当前不应说过头的内容

**EN**
- one-marker diagnosis for IBD
- routine-ready metabolomic deployment
- strong idiopathic-IBD-specific efficacy claims
- a finished regulatory path

**ZH**
- 不应把 IBD 讲成 one-marker diagnosis
- 不应把 metabolomics 讲成 routine-ready
- 不应过度主张 idiopathic-IBD-specific efficacy
- 不应假装监管路径已经完成

## Best Reuse Targets / 当前最适合复用的页面

- [synthesis index](synthesis-index.md)
- [current state dashboard bilingual](current-state-dashboard-bilingual.md)
- [briefing working en](../../outputs/briefings/out-ibd-briefing-20260409-round1-working-en.md)
- [briefing zh](../../outputs/briefings/out-ibd-briefing-20260409-round1-zh.md)

## Note / 说明

This bilingual page is a compiled derivative.  
It keeps the raw source layer untouched and does not imply stronger evidence than the underlying source set.

这页双语页属于编译层派生物。  
它不会改动原始来源层，也不意味着它比底层来源集合更强。
