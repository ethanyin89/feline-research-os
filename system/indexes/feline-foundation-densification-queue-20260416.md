---
id: system-feline-foundation-densification-queue-20260416
type: system
topic: operating-system
question_type: queue
language: zh
last_compiled_at: 2026-04-16
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Feline Foundation Densification Queue, 2026-04-16

这页只回答一个执行问题：

`既然基础研究层还没全部处理好，下一步最小、最值钱的补强顺序是什么？`

## 类型判断

这件事属于：

`检查后的执行队列`

不是新方案。

前面的完整性检查已经足够说明：

- 主干 compile 已经在
- 现在缺的是薄层补强

## 最短结论

先不要横向开新病种，也不要先做更复杂 UI。

先补 3 类东西：

1. `image / figure / OCR / table`
2. `still-thin disease branches`
3. `CKD 剩余薄层`

## Queue

### P0

`raw multimodal ingest gap`

目标：

- 把 figure / caption / panel / table 从“完全不在系统里”推进到“至少进入 raw 层”

原因：

- 当前 `raw/` 图片数为 `0`
- 这是最硬的素材层缺口
- 不补这层，系统就仍是 markdown-first vault，不是 image-aware research OS

最低完成标准：

- 建立图片素材落盘约定
- 建立 caption / figure source-card 约定
- 至少挑一个病种做小样本贯通

入口页：

- [image ingest protocol](image-ingest-protocol-20260416.md)
- [CKD image ingest pilot](ckd-image-ingest-pilot-20260416.md)
- [CKD image ingest manifest](ckd-image-ingest-manifest-20260416.md)
- [CKD image download checklist](ckd-image-download-checklist-20260417.md)
- [FIP image ingest pilot](fip-image-ingest-pilot-20260417.md)
- [FIP image ingest manifest](fip-image-ingest-manifest-20260417.md)
- [FIP image download checklist](fip-image-download-checklist-20260417.md)
- [IBD image ingest pilot](ibd-image-ingest-pilot-20260417.md)
- [IBD image ingest manifest](ibd-image-ingest-manifest-20260417.md)
- [IBD image download checklist](ibd-image-download-checklist-20260417.md)
- [HCM image ingest pilot](hcm-image-ingest-pilot-20260417.md)
- [HCM image ingest manifest](hcm-image-ingest-manifest-20260417.md)
- [HCM image download checklist](hcm-image-download-checklist-20260417.md)

### P1 ✓ DONE 2026-04-17

`FIP regulatory branch densification`

目标：

- 把 FIP regulatory 从 thin boundary page 推到 first jurisdiction split

原因：

- 当前 dashboard 已明确写 `no jurisdiction-specific analysis yet`
- FIP 主干强，但监管层仍是明显空洞

最低完成标准：

- ✓ 至少出现一张 jurisdiction-aware regulatory memo
- ✓ 不再只是 stop-sign page

完成产出：

- [FIP regulatory jurisdiction split memo, 2026-04-17](fip-regulatory-jurisdiction-split-memo-20260417.md)
- 覆盖 China / USA / EU / UK 四个司法区
- 全部 source_ids: src-reg-001 至 src-reg-009
- regulatory-brief.md 已从 stop-sign 更新为有结构的 linked memo

### P2 ✓ DONE 2026-04-17

`IBD regulatory + treatment hierarchy cleanup`

目标：

- 把 IBD 的 route thinking 和 treatment hierarchy 再压实一层

原因：

- 当前仍写着 `final treatment ranking` 不稳
- `recurring verification path` 仍缺

最低完成标准：

- ✓ treatment hierarchy 的 stronger feline-primary framing
- ✓ recurring verification path 变成稳定页

完成产出：

- [IBD treatment hierarchy feline-primary memo, 2026-04-17](ibd-treatment-hierarchy-feline-primary-memo-20260417.md)
  - 明确 step-1/step-2/step-3 阶梯，逐层标注置信度
  - 不再只是 "no final ranking"，而是给出 defensible floor
- [IBD recurring verification path, 2026-04-17](ibd-recurring-verification-path-20260417.md)
  - IBD 专属 verification 工作流
  - 覆盖 5 个常见 pitfall + 标准路径 + 常见问题模板

### P3 ✓ DONE 2026-04-17

`HCM second-wave densification`

目标：

- 把 HCM 从”真实 compiled module”推进到更稳的 second-wave state

原因：

- 当前仍明确是 `second-wave evidence densification`
- 不是 source 不够，而是 owner 还没压到底

最低完成标准：

- ✓ biomarker / AI / treatment branch 再压出一层更窄 owner

完成产出：

- [HCM second-wave owner map, 2026-04-17](hcm-second-wave-owner-map-20260417.md)
  - Biomarker owner question: NT-proBNP vs troponin conditional ranking by disease stage
  - AI owner question: workflow insertion point (screening vs monitoring vs borderline)
  - Treatment owner question: stage-specific skepticism weight (preclinical vs compensated vs CHF)
  - 每个 branch 的 “second-wave complete” 条件已明确定义
  - Dashboard 的 “Still Thin” 已从模糊 uncertainty 更新为具名 owner question

### P4 ✓ DONE 2026-04-17

`CKD residual thin-layer cleanup`

目标：

- 补 CKD 剩余的 model / early-detection / treatment-density 薄层

原因：

- CKD 最成熟，但并不等于 fully closed
- 当前还存在 `model thin but real` 和 newer early-detection density 不均

最低完成标准：

- ✓ model taxonomy 更明确
- ✓ early-detection literature 不再只是 support branch

完成产出：

- [CKD model taxonomy memo, 2026-04-17](ckd-model-taxonomy-memo-20260417.md)
  - 5 model types separated by what each can answer for different research purposes
  - Purpose-oriented matrix: mechanism / endpoint validation / drug efficacy / regulatory translation
  - Main gap explicitly named: Type 2 (controlled intervention) coverage for drug-efficacy questions
- [CKD early-detection frontier branch memo, 2026-04-17](ckd-early-detection-frontier-branch-memo-20260417.md)
  - Frontier branch carved out as a named parallel category (not "augmentation of serial surveillance")
  - Branch A (serial surveillance) vs Branch B (pre-clinical metabolomics/ML) distinction explicit
  - src-ckd-018 (AUC 0.929 ML panel) positioned correctly: distinct question, different time horizon
  - Evidence standards for the frontier branch defined separately from serial surveillance standards

## Do Not Do Yet

当前不要优先做：

- 新 disease shell
- 更复杂 chatbot 壳
- 通用平台化

这些都会稀释这轮检查暴露出来的真实缺口。

## Operator Rule

执行顺序只按这个原则：

`先补素材层真空，再补病种薄层，再补最成熟模块的尾差。`

不要反过来。

## One-Line Summary

这轮检查之后，最该做的不是重新想方向。

而是把：

`图片层缺席 + FIP/IBD/HCM 薄层 + CKD 尾差`

按这个顺序补平。
