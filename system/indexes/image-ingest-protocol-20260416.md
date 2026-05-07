---
id: system-image-ingest-protocol-20260416
type: system
topic: operating-system
question_type: workflow
language: zh
last_compiled_at: 2026-04-16
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Image Ingest Protocol, 2026-04-16

这页只回答一个窄问题：

`当论文或法规材料里有关键图片、图表、panel、figure 时，应该怎样进入这个 vault？`

## 类型判断

这件事属于：

`检查后的 ingest workflow`

不是新架构。

## 最短结论

不要再把图片当作“看过但没入库”的外部上下文。

最小路径应该是：

1. 图片文件进入 `raw/images/`
2. source card 的 `links.local_assets` 指向该文件
3. 如果暂时没下载图片，也要在 source card 里留下 `Image Asset TODO`

## Why This Exists

当前系统的硬缺口不是 source card 不存在。

而是：

`图片层几乎完全没有进入 ingest pipeline`

这会直接导致：

- vision 模型无东西可读
- figure 改写不了机制或 endpoint 理解
- later query 只能用文本，不会触达关键图表

## Directory Rule

图片统一放在：

- [raw/images](../../raw/images/README.md)

并优先按 disease bucket 落：

- `raw/images/ckd/`
- `raw/images/fip/`
- `raw/images/hcm/`
- `raw/images/ibd/`
- `raw/images/shared/`

## File Naming Rule

推荐格式：

- `src-ckd-001-mechanism-schematic.jpg`
- `src-fip-019-outcome-treatment-protocol-summary-table.png`
- `src-hcm-020-pathology-histopathology-panel.png`

这样做的原因很简单：

- 先能回到 source id
- 再能回到 figure 序号
- 最后才是人类描述

## Source Card Rule

如果图片已经落盘，就写进：

```yaml
links:
  local_assets:
    - guessed-or-unverified-figure-path
```

如果图片还没落盘，不要写入猜测路径，也不要假装这篇 source 没有图像价值。

改成：

```yaml
links:
  local_assets: []
```

并在正文里写：

```markdown
## Image Asset TODO

- figures to capture:
  - fig1 mechanism schematic
  - fig2 histology panel
- why these matter:
  - fig1 may sharpen mechanism branch placement
  - fig2 may strengthen lesion-level interpretation
```

## What To Capture First

优先级不要平均分。

先抓这几类：

1. 会改变机制理解的 figure
2. 会改变 recognition / workup 结构的图
3. 会改变 endpoint hierarchy 的 plots
4. histology / imaging panels
5. 只有图里才有的关键表格

## What Not To Capture

先不要抓：

- 装饰性示意图
- 和核心结论无关的作者流程图
- 已经能从正文稳定恢复的普通表格截图

## Minimal Pilot

第一轮不要追求全量。

先做一个 pilot：

1. 选一个病种
2. 选 3-5 个高价值 source
3. 每篇只抓最关键 1-3 张 figure
4. 确认 `local_assets` 能稳定指回去

这样先把 pipeline 走通，再扩。

## One-Line Summary

图片 ingest 的目标不是“把所有图都存下来”。

而是把：

`会改变系统理解的图`

从外部上下文，变成 vault 内部可引用资产。
