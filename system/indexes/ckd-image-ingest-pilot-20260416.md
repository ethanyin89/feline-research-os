---
id: system-ckd-image-ingest-pilot-20260416
type: system
topic: operating-system
question_type: pilot
language: zh
last_compiled_at: 2026-04-16
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# CKD Image Ingest Pilot, 2026-04-16

这页只回答一个小问题：

`如果先做一轮最小 image ingest pilot，CKD 应该先抓哪几张 source？`

## 类型判断

这件事属于：

`P0 pilot`

不是全量 rollout。

## 最短结论

先抓 5 张：

1. `src-ckd-001`
2. `src-ckd-013`
3. `src-ckd-017`
4. `src-ckd-022`
5. `src-ckd-024`

这 5 张覆盖了：

- 机制 backbone
- trial outcome architecture
- pathology-aware proteinuria branch
- experimental model layer
- biomarker / early-detection branch

## Why These Five

### src-ckd-001

[src-ckd-001.md](../../raw/papers/src-ckd-001.md)

为什么先抓：

- mechanism backbone 最核心
- review figure 很可能已经把 fibrosis-first 逻辑压成稳定图

### src-ckd-013

[src-ckd-013.md](../../raw/papers/src-ckd-013.md)

为什么先抓：

- core outcome set 非常像图表优先型 source
- 29 parameters / 9 themes 如果只留 prose，很容易损失结构

### src-ckd-017

[src-ckd-017.md](../../raw/papers/src-ckd-017.md)

为什么先抓：

- proteinuria 分支最需要 pathology panel
- 这类图像比摘要文字更能解释 compartment 差异

### src-ckd-022

[src-ckd-022.md](../../raw/papers/src-ckd-022.md)

为什么先抓：

- model layer 现在最薄
- 这张 paper 的价值很大一部分就在 histology 和 time-course figure

### src-ckd-024

[src-ckd-024.md](../../raw/papers/src-ckd-024.md)

为什么先抓：

- endpoint / biomarker branch 目前很依赖 review compression
- biomarker comparison 图表很可能比 prose 更适合后续 retrieval

## Pilot Rule

第一轮先不要追求每篇都抓完。

每篇只做：

- `1-3` 张最关键图片
- 回链到 `local_assets`
- 保证命名稳定

可直接照着落盘的目标文件名见：

- [CKD image ingest manifest](ckd-image-ingest-manifest-20260416.md)

## One-Line Summary

这轮 pilot 的目标不是让 CKD 图片层“全部完成”。

而是证明：

`图片可以从外部上下文，进入 source-card 可引用资产层。`
