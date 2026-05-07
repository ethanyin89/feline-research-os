---
id: system-fip-image-ingest-manifest-20260417
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

# FIP Image Ingest Manifest, 2026-04-17

这页只回答一个执行问题：

`FIP 第一轮 pilot 图片如果现在开始人工落盘，目标文件名应该是什么？`

## 最短结论

直接按 source card 的 `links.local_assets` 落盘。

## Manifest

| Source | Target assets |
|---|---|
| `src-fip-003` | verified: `raw/images/fip/src-fip-003-figure-2-ascites-radiograph-kidney-ihc-panel.png`; remaining candidates: `raw/images/fip/src-fip-003-candidate-overview-mechanism-figure.png`, `raw/images/fip/src-fip-003-candidate-diagnostic-support-summary-table.png` |
| `src-fip-015` | `raw/images/fip/src-fip-015-candidate-staging-framework-table.png`, `raw/images/fip/src-fip-015-candidate-clinicopathology-pattern-summary.png` |
| `src-fip-019` | `raw/images/fip/src-fip-019-candidate-treatment-protocol-summary-table.png`, `raw/images/fip/src-fip-019-candidate-outcome-by-disease-form-figure.png` |
| `src-fip-023` | `raw/images/fip/src-fip-023-candidate-csf-rt-pcr-performance-table.png`, `raw/images/fip/src-fip-023-candidate-neurologic-versus-general-workup-branch.png` |
| `src-fip-024` | `raw/images/fip/src-fip-024-candidate-neurologic-treatment-course-summary.png`, `raw/images/fip/src-fip-024-candidate-followup-imaging-or-csf-panel.png` |

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
| `src-fip-003` | `https://veterinaryworld.org/Vol.17/November-2024/1.php` |
| `src-fip-015` | `https://journals.sagepub.com/doi/10.1016/j.jfms.2010.09.014` |
| `src-fip-019` | `https://academic.oup.com/jvim/article/37/5/1784/8447739` |
| `src-fip-023` | `https://journals.sagepub.com/doi/10.1177/1098612X15574757` |
| `src-fip-024` | `https://academic.oup.com/jvim/article/34/4/1587/8448359` |

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

它只是把第一轮 FIP 图片 pilot 变成一份：

`基于真实 source link、但不伪造 figure 编号的 manifest。`

如果要按执行状态逐项核对，使用：

- [FIP image download checklist](fip-image-download-checklist-20260417.md)
