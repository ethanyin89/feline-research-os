---
id: topic-ibd-risk-and-recognition-bilingual
type: topic
topic: ibd
species: feline
disease: IBD
question_type: recognition
source_ids: [src-ibd-003, src-ibd-004, src-ibd-009, src-ibd-010, src-ibd-015, src-ibd-016, src-ibd-017, src-ibd-019, src-ibd-024]
language: bilingual
last_compiled_at: 2026-04-09
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: draft
---

# Feline IBD Risk And Recognition, Bilingual

## Quick Helpers / 快速辅助入口

- if you want to trace a claim back down:
  [verify a claim](../../system/indexes/verify-a-claim.md)
- if you want to see real `promote / hold / partial promotion` examples:
  [promotion examples index](../../system/indexes/promotion-examples-index.md)

## What This Page Is / 这页是什么

**EN**  
This is the bilingual derived version of the IBD recognition page. It is for high-reuse internal recognition and workup discussion, not for replacing the raw source layer.

**ZH**  
这是 IBD 识别页的双语派生版本。它服务于高频内部识别和诊断流程讨论，不用于替代原始来源层。

## Current Recognition Architecture / 当前识别架构

### Entry Frame / 进入框架

**EN**
- recognition begins with `chronic gastrointestinal enteropathy suspicion`, not with one definitive marker
- feline IBD recognition should start from `diagnosis of exclusion`, not from default labeling
- chronic-enteropathy recognition should not be mistaken for confirmed idiopathic IBD

**ZH**
- 识别起点应是 `chronic gastrointestinal enteropathy suspicion`，而不是某一个 definitive marker
- 猫 IBD 的识别应从 `diagnosis of exclusion` 开始，而不是默认贴标签
- chronic-enteropathy 的识别不应被误当成已经确认的 idiopathic IBD

### Operational Clinical Layer / 操作性临床层

**EN**
- `disease-activity indexing` helps operationalize the clinical branch
- `FCEAI` helps stage burden and response tracking
- activity tracking supports management, but does not settle disease class

**ZH**
- `disease-activity indexing` 有助于把临床分支操作化
- `FCEAI` 有助于给负担和应答追踪分层
- 活动度追踪服务于管理，但并不决定疾病类别

### Workup-Shaping Layer / 塑造诊断流程的分支

**EN**
- `ultrasound`, `endoscopic biopsy`, and `histopathology` shape the next workup layer
- `duodenal convenience` and `diagnostic completeness` are not interchangeable
- site-aware tissue strategy should stay inside recognition, not be postponed to the very end

**ZH**
- `ultrasound`、`endoscopic biopsy` 和 `histopathology` 会塑造下一层诊断流程
- `duodenal convenience` 和 `diagnostic completeness` 并不可互换
- 带位点意识的 tissue strategy 应保留在识别层内部，而不是拖到最后才考虑

### Lymphoma-Boundary Pressure / lymphoma 边界压力

**EN**
- the workup must stay boundary-aware because `small-cell lymphoma` is the most important nearby differential branch in this corpus
- `muscularis thickening` should raise stronger lymphoma concern, but it does not close the case by itself
- the lymphoma boundary should shape suspicion early, not only appear at the end of pathology review

**ZH**
- 诊断流程必须持续保持边界意识，因为 `small-cell lymphoma` 是当前 corpus 里最重要的相邻鉴别分支
- `muscularis thickening` 应提高对 lymphoma 的怀疑度，但它本身并不能结案
- lymphoma 边界应在早期就塑造怀疑，而不是等到 pathology review 结束才出现

### Extension-Aware Differential Layer / 带 extension 意识的鉴别层

**EN**
- practice-oriented chronic-enteropathy review material reinforces that this recognition problem belongs to routine CE workup
- extension branches such as `granulomatous colitis` should stay visible as differential-awareness nodes
- neighboring extension diseases should widen awareness without distorting the core recognition spine

**ZH**
- 面向实践的 chronic-enteropathy 综述会强化一点：这个识别问题属于 routine CE workup
- `granulomatous colitis` 等 extension branches 应保持可见，作为 differential-awareness nodes
- 相邻 extension 疾病应扩宽鉴别意识，但不应扭曲核心识别主干

## What We Can Defend / 当前可以稳妥主张的内容

**EN**
- recognition in IBD is more about structured workup than about classic epidemiologic risk-factor compression
- the safest entry frame is `chronic enteropathy suspicion`
- exclusion-first workup should lead before biomarker compression
- lymphoma-boundary pressure belongs inside recognition from the beginning

**ZH**
- IBD 的识别更像 structured workup，而不是经典流行病学 risk-factor compression
- 最安全的入口框架仍是 `chronic enteropathy suspicion`
- exclusion-first workup 应先于 biomarker compression
- lymphoma-boundary pressure 应从一开始就放进 recognition 内部

## What We Should Not Overstate / 当前不应说过头的内容

**EN**
- no current recognition layer should be rewritten as one-marker diagnosis
- chronic-enteropathy suspicion is not idiopathic-IBD confirmation
- imaging support is not disease identity proof
- extension diseases should not be absorbed into the core idiopathic recognition spine

**ZH**
- 当前没有任何识别层应被改写成 one-marker diagnosis
- chronic-enteropathy suspicion 不等于 idiopathic-IBD confirmation
- 影像支持不等于疾病身份的证明
- extension diseases 不应被吸收到 core idiopathic recognition spine 里

## Best Current Anchors / 当前最佳锚点

- [risk and recognition](risk-and-recognition.md)
- [IBD diagnostic workup memo](../../system/indexes/ibd-diagnostic-workup-memo.md)
- [IBD-lymphoma boundary memo](../../system/indexes/ibd-lymphoma-boundary-memo.md)

## Note / 说明

This bilingual page is a compiled derivative.  
It keeps the raw source layer untouched and does not imply stronger evidence than the underlying source set.

这页双语页属于编译层派生物。  
它不会改动原始来源层，也不意味着它比底层来源集合更强。
