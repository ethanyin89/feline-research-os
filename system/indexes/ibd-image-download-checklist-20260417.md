---
id: system-ibd-image-download-checklist-20260417
type: system
topic: operating-system
question_type: checklist
language: zh
last_compiled_at: 2026-04-17
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# IBD Image Download Checklist, 2026-04-17

这页只回答一个执行问题：

`如果现在开始按真实 link 下载 IBD pilot 图片，应该怎么逐项核对，而不是边下边猜？`

## 类型判断

按 `$autoplan` 的四分法，这件事属于：

`检查后的执行 checklist`

不是新方案。

## 最短结论

先不要直接把下载结果当真。

每张候选图都要过 4 个检查：

1. 是不是来自 source card 里的真实链接
2. 候选文件名和 source id 是否一致
3. 原文真实 figure / table 标签是否已核对
4. 是否需要把 `candidate-*` 改成真实标签名

## How To Use

执行时只按这张表走：

- `Downloaded`:
  - `no` = 还没落盘
  - `yes` = 文件已经在 `raw/images/ibd/`
- `Verified against article label`:
  - `no` = 还没核对原文编号
  - `yes` = 已确认 figure/table 标签
- `Final rename needed`:
  - `yes` = 需要把 `candidate-*` 改成真实标签
  - `no` = 当前文件名已经够稳，或者暂时保留 candidate 名

## Checklist

| Source | Real link | Candidate asset | Downloaded | Verified against article label | Final rename needed | Notes |
|---|---|---|---|---|---|---|
| `src-ibd-019` | `https://www.nature.com/articles/s41598-021-88707-5` | `raw/images/ibd/src-ibd-019-figure-1-pca-heatmap-ce-vs-control.png` | `yes` | `yes` | `no` | verified against Scientific Reports article Figure 1; now listed in source-card `local_assets` |
| `src-ibd-003` | `https://www.sciencedirect.com/science/article/pii/S1098612X99902048` | `raw/images/ibd/src-ibd-003-candidate-exclusion-first-workup-overview.png` | `no` | `no` | `yes` | broad review workup candidate |
| `src-ibd-003` | `https://www.sciencedirect.com/science/article/pii/S1098612X99902048` | `raw/images/ibd/src-ibd-003-candidate-ibd-versus-mimic-summary-table.png` | `no` | `no` | `yes` | mimic-boundary candidate |
| `src-ibd-004` | `https://academic.oup.com/jvim/article/24/5/1027/8447312` | `raw/images/ibd/src-ibd-004-candidate-fceai-component-table.png` | `no` | `no` | `yes` | endpoint architecture candidate |
| `src-ibd-004` | `https://academic.oup.com/jvim/article/24/5/1027/8447312` | `raw/images/ibd/src-ibd-004-candidate-fceai-response-tracking-figure.png` | `no` | `no` | `yes` | response-tracking candidate |
| `src-ibd-015` | `https://academic.oup.com/jvim/article/25/6/1253/8451361` | `raw/images/ibd/src-ibd-015-candidate-duodenum-versus-ileum-diagnostic-agreement-table.png` | `no` | `no` | `yes` | biopsy-site agreement candidate |
| `src-ibd-015` | `https://academic.oup.com/jvim/article/25/6/1253/8451361` | `raw/images/ibd/src-ibd-015-candidate-site-specific-lymphoma-detection-summary.png` | `no` | `no` | `yes` | lymphoma-boundary candidate |
| `src-ibd-014` | `https://pubmed.ncbi.nlm.nih.gov/20939411/` | `raw/images/ibd/src-ibd-014-candidate-hydrolysate-diet-response-summary.png` | `no` | `no` | `yes` | diet-first response candidate |
| `src-ibd-014` | `https://pubmed.ncbi.nlm.nih.gov/20939411/` | `raw/images/ibd/src-ibd-014-candidate-diet-challenge-recurrence-table.png` | `no` | `no` | `yes` | diet challenge candidate |
| `src-ibd-022` | `https://academic.oup.com/jvim/article/37/3/936/8447850` | `raw/images/ibd/src-ibd-022-candidate-fibrosis-detection-method-comparison-table.png` | `no` | `no` | `yes` | fibrosis method comparison candidate |
| `src-ibd-022` | `https://academic.oup.com/jvim/article/37/3/936/8447850` | `raw/images/ibd/src-ibd-022-candidate-fibrosis-burden-versus-albumin-weight-figure.png` | `no` | `no` | `yes` | fibrosis burden candidate |

## Hard Rule

没有核对原文之前：

- 不要写真实 `fig2` / `table3`
- 不要声称某张候选图就是论文里的最终标签
- 不要在 compiled page 里把候选文件当成已验证证据

## Related Pages

- [IBD image ingest pilot](ibd-image-ingest-pilot-20260417.md)
- [IBD image ingest manifest](ibd-image-ingest-manifest-20260417.md)
- [image ingest protocol](image-ingest-protocol-20260416.md)

## One-Line Summary

这页的作用不是决定抓什么图。

它是把：

`真实 source link -> candidate asset -> verified rename`

压成一张能执行的 checklist。
