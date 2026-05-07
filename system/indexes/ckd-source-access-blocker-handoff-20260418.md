---
id: system-ckd-source-access-blocker-handoff-20260418
type: system
topic: operating-system
question_type: workflow
language: zh
last_compiled_at: 2026-04-18
owner: codex
status: active
---

# CKD Source Access Blocker Handoff, 2026-04-18

这页只回答一个问题：

`在当前环境里，CKD 剩余未完成对象到底卡在哪些源站访问层，哪些路径已经证伪，不要再重试什么？`

## 类型判断

按 `$autoplan` 四分法，这件事属于：

`检查`

不是新方案。

## 当前已完成资产

`raw/images/ckd/` 当前已有 8 个真实已验证资产：

- `src-ckd-001-mechanism-risk-factor-summary.jpg`
- `src-ckd-001-mechanism-schematic.jpg`
- `src-ckd-017-imaging-pathology-classification-panel.jpg`
- `src-ckd-017-outcome-upc-by-subtype-table.png`
- `src-ckd-022-pathology-histopath-findings-table.png`
- `src-ckd-022-outcome-time-course-gfr-creatinine-table.png`
- `src-ckd-024-outcome-biomarker-comparison-table.png`
- `src-ckd-024-outcome-biomarker-landscape.jpeg`

## 剩余未完成对象

只剩这 2 个：

- `src-ckd-013-candidate-core-outcome-set-flowchart.png`
- `src-ckd-013-candidate-core-themes-and-parameters-table.png`

## 已证伪路径

### `src-ckd-013`

- ScienceDirect 直链 PDF：当前返回 Cloudflare `403`
- Nottingham repository live 页面：当前落到 Cloudflare challenge，不是可下载 PDF
- Nottingham DSpace bitstream API：当前返回 `401 Unauthorized`
- `nottingham-repository.worktribe.com` output 页面：当前也是 Cloudflare challenge 壳页，页面里没有暴露可执行文件链接
- Bristol / handle publication 页面：当前只暴露 metadata 和 abstract，没有 full-text / electronic version 下载链接
- 搜索缓存：显示 Nottingham 页面确实列了两个 PDF 文件
  - `Supplement 1 PVM HD` (95 Kb)
  - `PVM_paper_resubmission_March2021_V2_tracking_removed` (387 Kb)

结论：

`013` 不是“没有副本线索”，而是“有副本线索，但当前环境无法穿过源站限制拿到对象”。不要再重复打 ScienceDirect 直链、Nottingham live/API 页面、Worktribe output 页面，或者 Bristol / handle publication 页面。

### `src-ckd-022`

- 正文 `Table 1` 已经从文章文本提取并做成本地 render，已落盘
- 正文公开可访问的 article surface 暴露了主文 figures 和 supplemental tables `S1-S8`
- 当前没有看到单独可核对的 model-design 原始对象
- Sage supplemental PDF：当前直连 `journals.sagepub.com:443` 超时
- Sage `fig1/fig2` 原始图链接：已定位，但两条探测都超时；而且它们不是 model-design 对象

结论：

`022` 已经不再是 live blocker。`Table 1` 和 `Table 2` 都已经拿下；之前的 `model-design` 候选在当前可访问 source surface 上没有对应的可验证原始对象，因此被退役，而不是继续保留成未完成 extraction 目标。不要再重复打 supplemental 直链和 `fig1/fig2` 直图链。

## 现在还值得尝试的方向

只剩一类：

1. 找 `013` 的 Nottingham 两个 PDF 是否被别的公开缓存或镜像直接索引

## 不值得再做的事

- 不要重试 ScienceDirect `013` PDF 直链
- 不要重试 Nottingham live 页面 HTML
- 不要重试 `022` 的 Sage supplemental PDF 直链
- 不要重试 `022` 的 `fig1/fig2` 直图链
- 不要再补 handoff 结构文档

## 最小执行面

如果继续，只改这些：

- `raw/images/ckd/`
- `raw/papers/src-ckd-013.md`
- `system/indexes/ckd-image-download-checklist-20260417.md`
- `PLAN.md`

## One Line

当前剩下的 live blocker 不是内容问题，是 `013` 的源站访问问题。
