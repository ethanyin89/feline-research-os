---
id: system-ckd-image-ingest-manifest-20260416
type: system
topic: operating-system
question_type: manifest
language: zh
last_compiled_at: 2026-04-16
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# CKD Image Ingest Manifest, 2026-04-16

这页只回答一个执行问题：

`CKD 第一轮 pilot 图片如果现在开始人工落盘，目标文件名应该是什么？`

## 最短结论

直接按 source card 的 `links.local_assets` 落盘。

## Manifest

| Source | Target assets |
|---|---|
| `src-ckd-001` | `raw/images/ckd/src-ckd-001-mechanism-schematic.jpg`, `raw/images/ckd/src-ckd-001-mechanism-risk-factor-summary.jpg` |
| `src-ckd-013` | `raw/images/ckd/src-ckd-013-candidate-core-outcome-set-flowchart.png`, `raw/images/ckd/src-ckd-013-candidate-core-themes-and-parameters-table.png` |
| `src-ckd-017` | `raw/images/ckd/src-ckd-017-imaging-pathology-classification-panel.jpg`, `raw/images/ckd/src-ckd-017-outcome-upc-by-subtype-table.png` |
| `src-ckd-022` | `raw/images/ckd/src-ckd-022-outcome-time-course-gfr-creatinine-table.png` ✓, `raw/images/ckd/src-ckd-022-pathology-histopath-findings-table.png` ✓ |
| `src-ckd-024` | `raw/images/ckd/src-ckd-024-outcome-biomarker-landscape.jpeg`, `raw/images/ckd/src-ckd-024-outcome-biomarker-comparison-table.png` |

## Rule

`src-ckd-022` 之前的 `candidate-model-design` 已在 `2026-04-18` 退役，因为当前可访问的 article surface 只明确暴露了主文 figures 和 supplemental tables `S1-S8`，没有单独可核对的 model-design 原始对象。

这些文件名是：

`link-based candidate names`

不是对论文里真实 figure 编号的声明。

如果你后面真的从原文下载图片：

- 必须先核对原文实际 figure / table 标签
- 再决定是否把 `candidate-...` 改成真实 `fig2` / `table3`

在没有打开原文核对之前，不要自作主张写真实编号。

如果需要 later rename，可以改文件名尾部描述，但不要改：

- `src id`
- `disease bucket`
- `candidate` 之前的稳定前缀

## Source Links

| Source | Link |
|---|---|
| `src-ckd-001` | `https://journals.sagepub.com/doi/10.1177/1098612X13495234` |
| `src-ckd-013` | `https://www.sciencedirect.com/science/article/abs/pii/S0167587721000921?via%3Dihub` |
| `src-ckd-017` | `https://journals.sagepub.com/doi/10.1177/1098612X20921056` |
| `src-ckd-022` | `https://journals.sagepub.com/doi/10.1177/0300985819837721` |
| `src-ckd-024` | `https://academic.oup.com/jvim/article/36/2/379/8449129` |

## One-Line Summary

这页的作用不是解释为什么这些图重要。

它只是把第一轮 CKD 图片 pilot 变成一份：

`基于真实 source link、但不伪造 figure 编号的 manifest。`

如果要按执行状态逐项核对，使用：

- [CKD image download checklist](ckd-image-download-checklist-20260417.md)
