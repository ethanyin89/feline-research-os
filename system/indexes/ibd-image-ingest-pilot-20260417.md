---
id: system-ibd-image-ingest-pilot-20260417
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

# IBD Image Ingest Pilot, 2026-04-17

这页只回答一个小问题：

`如果先做一轮最小 image ingest pilot，IBD 应该先抓哪几张 source？`

## 类型判断

这件事属于：

`检查后的执行 / P0 pilot`

不是全量 rollout。

## 最短结论

先抓 5 张：

1. `src-ibd-003`
2. `src-ibd-004`
3. `src-ibd-015`
4. `src-ibd-014`
5. `src-ibd-022`

这 5 张覆盖了：

- broad exclusion-first backbone
- operational activity index
- biopsy-site and lymphoma boundary
- diet-first treatment anchor
- fibrosis and chronicity branch

## Why These Five

### src-ibd-003

[src-ibd-003.md](../../raw/papers/src-ibd-003.md)

为什么先抓：

- 这是最稳的 broad feline IBD anchor
- 如果要给 IBD disease shell 留第一张总图，它最合适

### src-ibd-004

[src-ibd-004.md](../../raw/papers/src-ibd-004.md)

为什么先抓：

- FCEAI 是 endpoint layer 的核心结构化对象
- component table 和 response plot 非常适合进入图片层

### src-ibd-015

[src-ibd-015.md](../../raw/papers/src-ibd-015.md)

为什么先抓：

- 这是 IBD-versus-small-cell-lymphoma boundary 最值钱的实操 paper 之一
- biopsy-site utility 这类信息用图表保存比 prose 更稳

### src-ibd-014

[src-ibd-014.md](../../raw/papers/src-ibd-014.md)

为什么先抓：

- 当前 treatment branch 里，diet-first 是最干净的 practical anchor
- response / challenge / recurrence 结构适合直接保在图表层

### src-ibd-022

[src-ibd-022.md](../../raw/papers/src-ibd-022.md)

为什么先抓：

- fibrosis 是 IBD 慢性化和组织重塑层最强的新结构支点
- method-comparison table 和 histology panel 非常值得保住

## Pilot Rule

第一轮先不要追求每篇都抓完。

每篇只做：

- `1-3` 张最关键图片
- 回链到 `local_assets`
- 保证命名稳定
- 所有命名都保持 `candidate-*`

真正可落盘的目标文件名见：

- [IBD image ingest manifest](ibd-image-ingest-manifest-20260417.md)

## Hard Rule

这轮 pilot 必须遵守：

`all material based on the real source link, no fake data allowed`

所以：

- 不提前写真实 `fig2` / `table3`
- 不假装已经打开过原文核对编号
- 只允许使用 `candidate-*` 命名，直到真实下载并核对 article label

## One-Line Summary

这轮 pilot 的目标不是让 IBD 图片层“全部完成”。

而是证明：

`IBD 的 workup / endpoint / fibrosis / diet-first 资产可以从真实 source link，进入 source-card 可引用层。`
