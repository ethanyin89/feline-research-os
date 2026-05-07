---
id: system-fip-image-ingest-pilot-20260417
type: system
topic: operating-system
question_type: pilot
language: zh
last_compiled_at: 2026-04-17
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# FIP Image Ingest Pilot, 2026-04-17

这页只回答一个小问题：

`如果先做一轮最小 image ingest pilot，FIP 应该先抓哪几张 source？`

## 类型判断

这件事属于：

`检查后的执行 / P0 pilot`

不是全量 rollout。

## 最短结论

先抓 5 张：

1. `src-fip-003`
2. `src-fip-015`
3. `src-fip-019`
4. `src-fip-023`
5. `src-fip-024`

这 5 张覆盖了：

- broad modern review backbone
- clinicopathology and staging structure
- real-world antiviral package logic
- neurologic diagnostic extension
- neurologic treatment complexity

## Why These Five

### src-fip-003

[src-fip-003.md](../../raw/papers/src-fip-003.md)

为什么先抓：

- 这是当前最强的 modern broad-review anchor
- 如果 review 里有 overview figure，它最适合做 FIP disease shell 的第一张总图

### src-fip-015

[src-fip-015.md](../../raw/papers/src-fip-015.md)

为什么先抓：

- recognition branch 最需要结构化 staging / clinicopathology 图表
- 这类信息如果只留 prose，最容易被压扁

### src-fip-019

[src-fip-019.md](../../raw/papers/src-fip-019.md)

为什么先抓：

- 现代 antiviral package logic 需要 protocol 和 outcome 图表支撑
- 这是 effusive / non-effusive / ocular / neurologic 混合队列的重要现实世界 anchor

### src-fip-023

[src-fip-023.md](../../raw/papers/src-fip-023.md)

为什么先抓：

- neurologic diagnostic branch 最怕被 generic workup 语言吞掉
- CSF detection 这种性能表格型信息非常适合进入图片层

### src-fip-024

[src-fip-024.md](../../raw/papers/src-fip-024.md)

为什么先抓：

- neurologic treatment complexity 是 FIP 最值钱也最容易被过度简化的分支之一
- serial follow-up panel 或 dosing-response 图最值得保住

## Pilot Rule

第一轮先不要追求每篇都抓完。

每篇只做：

- `1-3` 张最关键图片
- 回链到 `local_assets`
- 保证命名稳定
- 所有命名都保持 `candidate-*`

真正可落盘的目标文件名见：

- [FIP image ingest manifest](fip-image-ingest-manifest-20260417.md)

## Hard Rule

这轮 pilot 必须遵守：

`all material based on the real source link, no fake data allowed`

所以：

- 不提前写真实 `fig2` / `table3`
- 不假装已经打开过原文核对编号
- 只允许使用 `candidate-*` 命名，直到真实下载并核对 article label

## One-Line Summary

这轮 pilot 的目标不是让 FIP 图片层“全部完成”。

而是证明：

`FIP 的高价值图表资产可以从真实 source link，进入 source-card 可引用层。`
