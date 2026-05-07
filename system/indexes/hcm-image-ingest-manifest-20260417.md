---
id: system-hcm-image-ingest-manifest-20260417
type: system
topic: operating-system
question_type: manifest
language: zh
last_compiled_at: 2026-04-17
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# HCM Image Ingest Manifest, 2026-04-17

这页只回答一个执行问题：

`HCM 第一轮 pilot 图片如果现在开始人工落盘，目标文件名应该是什么？`

## 最短结论

直接按 source card 的 `links.local_assets` 落盘。

## Manifest

| Source | Target assets |
|---|---|
| `src-hcm-011` | verified: `raw/images/hcm/src-hcm-011-fig-3-myk461-sam-lvot-gradient.png` |
| `src-hcm-001` | `raw/images/hcm/src-hcm-001-candidate-mechanism-overview.png`, `raw/images/hcm/src-hcm-001-candidate-clinical-staging-diagram.png` |
| `src-hcm-009` | `raw/images/hcm/src-hcm-009-candidate-echo-phenotype-classification.png`, `raw/images/hcm/src-hcm-009-candidate-echo-measurements-table.png` |
| `src-hcm-010` | `raw/images/hcm/src-hcm-010-candidate-nt-probnp-threshold-scatter.png`, `raw/images/hcm/src-hcm-010-candidate-nt-probnp-roc-or-comparison-table.png` |
| `src-hcm-012` | `raw/images/hcm/src-hcm-012-candidate-penetrance-curve-by-age.png`, `raw/images/hcm/src-hcm-012-candidate-genotype-outcome-table.png` |
| `src-hcm-020` | `raw/images/hcm/src-hcm-020-candidate-histopathology-panel.png`, `raw/images/hcm/src-hcm-020-candidate-macrophage-infiltration-figure.png` |

## Rule

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
| `src-hcm-001` | `https://journals.sagepub.com/doi/10.1177/1098612X211020162` |
| `src-hcm-009` | `https://www.ahajournals.org/doi/10.1161/01.CIR.92.9.2645` |
| `src-hcm-010` | `https://www.sciencedirect.com/science/article/abs/pii/S1760273409000095?via%3Dihub` |
| `src-hcm-012` | `https://www.mdpi.com/2306-7381/11/5/214` |
| `src-hcm-020` | `https://journals.sagepub.com/doi/10.1177/0300985819837717` |

## One-Line Summary

这页的作用不是解释为什么这些图重要。

它只是把第一轮 HCM 图片 pilot 变成一份：

`基于真实 source link、但不伪造 figure 编号的 manifest。`

如果要按执行状态逐项核对，使用：

- [HCM image download checklist](hcm-image-download-checklist-20260417.md)
