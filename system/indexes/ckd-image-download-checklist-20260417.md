---
id: system-ckd-image-download-checklist-20260417
type: system
topic: operating-system
question_type: checklist
language: zh
last_compiled_at: 2026-04-18
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# CKD Image Download Checklist, 2026-04-17

这页只回答一个执行问题：

`如果现在开始按真实 link 下载 CKD pilot 图片，应该怎么逐项核对，而不是边下边猜？`

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
  - `yes` = 文件已经在 `raw/images/ckd/`
- `Verified against article label`:
  - `no` = 还没核对原文编号
  - `yes` = 已确认 figure/table 标签
- `Final rename needed`:
  - `yes` = 需要把 `candidate-*` 改成真实标签
  - `no` = 当前文件名已经够稳，或者暂时保留 candidate 名

## Checklist

| Source | Real link | Candidate asset | Downloaded | Verified against article label | Final rename needed | Notes |
|---|---|---|---|---|---|---|
| `src-ckd-001` | `https://journals.sagepub.com/doi/10.1177/1098612X13495234` | `raw/images/ckd/src-ckd-001-candidate-mechanism-schematic.png` | `yes` | `yes` | `no` | finalized as `raw/images/ckd/src-ckd-001-mechanism-schematic.jpg`; verified from PMC mirror inline graphic `img2` in the Pathogenesis section |
| `src-ckd-001` | `https://journals.sagepub.com/doi/10.1177/1098612X13495234` | `raw/images/ckd/src-ckd-001-candidate-risk-factor-summary.png` | `yes` | `yes` | `no` | finalized as `raw/images/ckd/src-ckd-001-mechanism-risk-factor-summary.jpg`; verified from PMC mirror inline graphic `img1` labeled `Risk factors` |
| `src-ckd-013` | `https://www.sciencedirect.com/science/article/abs/pii/S0167587721000921?via%3Dihub` | `raw/images/ckd/src-ckd-013-candidate-core-outcome-set-flowchart.png` | `no` | `no` | `yes` | core outcome architecture candidate; direct ScienceDirect PDF path currently returns Cloudflare `403`; Nottingham repository mirror also resolves to a Cloudflare challenge page rather than a downloadable PDF, and its DSpace bitstream API currently returns `401 Unauthorized`; the newer `nottingham-repository.worktribe.com` output page also resolves to a Cloudflare challenge shell with no visible file links in the current environment, although search-cache snippets indicate the page lists two downloadable PDF files; Bristol/handle publication pages expose metadata and abstract only, with no downloadable full-text object visible in the current environment |
| `src-ckd-013` | `https://www.sciencedirect.com/science/article/abs/pii/S0167587721000921?via%3Dihub` | `raw/images/ckd/src-ckd-013-candidate-core-themes-and-parameters-table.png` | `no` | `no` | `yes` | parameter table candidate; direct ScienceDirect PDF path currently returns Cloudflare `403`; Nottingham repository mirror also resolves to a Cloudflare challenge page rather than a downloadable PDF, and its DSpace bitstream API currently returns `401 Unauthorized`; the newer `nottingham-repository.worktribe.com` output page also resolves to a Cloudflare challenge shell with no visible file links in the current environment, although search-cache snippets indicate the page lists two downloadable PDF files; Bristol/handle publication pages expose metadata and abstract only, with no downloadable full-text object visible in the current environment |
| `src-ckd-017` | `https://journals.sagepub.com/doi/10.1177/1098612X20921056` | `raw/images/ckd/src-ckd-017-candidate-pathology-panel.png` | `yes` | `yes` | `no` | finalized as `raw/images/ckd/src-ckd-017-imaging-pathology-classification-panel.jpg`; verified against PMC `Figure 1` histopathologic classification panel |
| `src-ckd-017` | `https://journals.sagepub.com/doi/10.1177/1098612X20921056` | `raw/images/ckd/src-ckd-017-candidate-upc-by-subtype-table.png` | `yes` | `yes` | `no` | finalized as `raw/images/ckd/src-ckd-017-outcome-upc-by-subtype-table.png`; verified against PMC `Table 2` and rendered locally from the PMC table page |
| `src-ckd-022` | `https://journals.sagepub.com/doi/10.1177/0300985819837721` | `raw/images/ckd/src-ckd-022-candidate-time-course-gfr-creatinine.png` | `yes` | `yes` | `no` | finalized as `raw/images/ckd/src-ckd-022-outcome-time-course-gfr-creatinine-table.png`; verified against article `Table 1` and rendered locally from the article text table extraction |
| `src-ckd-022` | `https://journals.sagepub.com/doi/10.1177/0300985819837721` | `raw/images/ckd/src-ckd-022-candidate-histology-panel.png` | `yes` | `yes` | `no` | finalized as `raw/images/ckd/src-ckd-022-pathology-histopath-findings-table.png`; verified against article `Table 2` and rendered locally from the publicly exposed article table text |
| `src-ckd-024` | `https://academic.oup.com/jvim/article/36/2/379/8449129` | `raw/images/ckd/src-ckd-024-candidate-biomarker-landscape.png` | `yes` | `yes` | `no` | finalized as `raw/images/ckd/src-ckd-024-outcome-biomarker-landscape.jpeg`; verified against OUP open-access `Figure 1` biomarker map |
| `src-ckd-024` | `https://academic.oup.com/jvim/article/36/2/379/8449129` | `raw/images/ckd/src-ckd-024-candidate-biomarker-comparison-table.png` | `yes` | `yes` | `no` | finalized as `raw/images/ckd/src-ckd-024-outcome-biomarker-comparison-table.png`; verified against OUP open-access `Table 2` and rendered locally from the article HTML table fragment |

## Hard Rule

`src-ckd-022` 之前的 `candidate-model-design` 已在 `2026-04-18` 退役。

原因不是“下载失败后放弃”，而是当前可访问的 article surface 只明确暴露了主文 figures 和 supplemental tables `S1-S8`，没有单独可核对的 model-design 原始对象。

没有核对原文之前：

- 不要写真实 `fig2` / `table3`
- 不要声称某张候选图就是论文里的最终标签
- 不要在 compiled page 里把候选文件当成已验证证据

## When To Update Source Cards

只有当下面 2 条都满足，才更新 source card 的 `local_assets` 为最终名：

1. 文件已真实落盘
2. 已核对 article 里的实际标签

如果只完成了第 1 条，还没完成第 2 条，就继续保留 `candidate-*`。

## Related Pages

- [CKD image ingest pilot](ckd-image-ingest-pilot-20260416.md)
- [CKD image ingest manifest](ckd-image-ingest-manifest-20260416.md)
- [image ingest protocol](image-ingest-protocol-20260416.md)

## One-Line Summary

这页的作用不是决定抓什么图。

它是把：

`真实 source link -> candidate asset -> verified rename`

压成一张能执行的 checklist。
