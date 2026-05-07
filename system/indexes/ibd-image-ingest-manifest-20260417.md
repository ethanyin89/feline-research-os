---
id: system-ibd-image-ingest-manifest-20260417
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

# IBD Image Ingest Manifest, 2026-04-17

这页只回答一个执行问题：

`IBD 第一轮 pilot 图片如果现在开始人工落盘，目标文件名应该是什么？`

## 最短结论

直接按 source card 的 `links.local_assets` 落盘。

## Manifest

| Source | Target assets |
|---|---|
| `src-ibd-019` | verified: `raw/images/ibd/src-ibd-019-figure-1-pca-heatmap-ce-vs-control.png` |
| `src-ibd-003` | `raw/images/ibd/src-ibd-003-candidate-exclusion-first-workup-overview.png`, `raw/images/ibd/src-ibd-003-candidate-ibd-versus-mimic-summary-table.png` |
| `src-ibd-004` | `raw/images/ibd/src-ibd-004-candidate-fceai-component-table.png`, `raw/images/ibd/src-ibd-004-candidate-fceai-response-tracking-figure.png` |
| `src-ibd-015` | `raw/images/ibd/src-ibd-015-candidate-duodenum-versus-ileum-diagnostic-agreement-table.png`, `raw/images/ibd/src-ibd-015-candidate-site-specific-lymphoma-detection-summary.png` |
| `src-ibd-014` | `raw/images/ibd/src-ibd-014-candidate-hydrolysate-diet-response-summary.png`, `raw/images/ibd/src-ibd-014-candidate-diet-challenge-recurrence-table.png` |
| `src-ibd-022` | `raw/images/ibd/src-ibd-022-candidate-fibrosis-detection-method-comparison-table.png`, `raw/images/ibd/src-ibd-022-candidate-fibrosis-burden-versus-albumin-weight-figure.png` |

## Rule

这些文件名是：

`link-based candidate names`

不是对论文里真实 figure 编号的声明。

如果你后面真的从原文下载图片：

- 必须先核对原文实际 figure / table 标签
- 再决定是否把 `candidate-...` 改成真实 `fig2` / `table3`

在没有打开原文核对之前，不要自作主张写真实编号。

## Source Links

| Source | Link |
|---|---|
| `src-ibd-003` | `https://www.sciencedirect.com/science/article/pii/S1098612X99902048` |
| `src-ibd-004` | `https://academic.oup.com/jvim/article/24/5/1027/8447312` |
| `src-ibd-015` | `https://academic.oup.com/jvim/article/25/6/1253/8451361` |
| `src-ibd-014` | `https://pubmed.ncbi.nlm.nih.gov/20939411/` |
| `src-ibd-022` | `https://academic.oup.com/jvim/article/37/3/936/8447850` |

## Hard Rule

这页必须服从同一个约束：

`all material based on the real source link, no fake data allowed`

所以 manifest 只定义：

- `source id`
- `real link`
- `candidate target path`

不定义：

- 假的 figure 编号
- 假的 panel 顺序
- 假的 caption 文本

## One-Line Summary

这页的作用不是解释为什么这些图重要。

它只是把第一轮 IBD 图片 pilot 变成一份：

`基于真实 source link、但不伪造 figure 编号的 manifest。`

如果要按执行状态逐项核对，使用：

- [IBD image download checklist](ibd-image-download-checklist-20260417.md)
