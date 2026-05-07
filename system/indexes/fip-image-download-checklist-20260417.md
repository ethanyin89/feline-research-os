---
id: system-fip-image-download-checklist-20260417
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

# FIP Image Download Checklist, 2026-04-17

这页只回答一个执行问题：

`如果现在开始按真实 link 下载 FIP pilot 图片，应该怎么逐项核对，而不是边下边猜？`

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
  - `yes` = 文件已经在 `raw/images/fip/`
- `Verified against article label`:
  - `no` = 还没核对原文编号
  - `yes` = 已确认 figure/table 标签
- `Final rename needed`:
  - `yes` = 需要把 `candidate-*` 改成真实标签
  - `no` = 当前文件名已经够稳，或者暂时保留 candidate 名

## Checklist

| Source | Real link | Candidate asset | Downloaded | Verified against article label | Final rename needed | Notes |
|---|---|---|---|---|---|---|
| `src-fip-003` | `https://veterinaryworld.org/Vol.17/November-2024/1.php` / PDF | `raw/images/fip/src-fip-003-figure-2-ascites-radiograph-kidney-ihc-panel.png` | `yes` | `yes` | `no` | verified against article PDF Figure-2; now listed in source-card `local_assets` |
| `src-fip-003` | `https://veterinaryworld.org/Vol.17/November-2024/1.php` | `raw/images/fip/src-fip-003-candidate-overview-mechanism-figure.png` | `no` | `no` | `yes` | broad modern review overview candidate |
| `src-fip-003` | `https://veterinaryworld.org/Vol.17/November-2024/1.php` | `raw/images/fip/src-fip-003-candidate-diagnostic-support-summary-table.png` | `no` | `no` | `yes` | review summary table candidate |
| `src-fip-015` | `https://journals.sagepub.com/doi/10.1016/j.jfms.2010.09.014` | `raw/images/fip/src-fip-015-candidate-staging-framework-table.png` | `no` | `no` | `yes` | staging structure candidate |
| `src-fip-015` | `https://journals.sagepub.com/doi/10.1016/j.jfms.2010.09.014` | `raw/images/fip/src-fip-015-candidate-clinicopathology-pattern-summary.png` | `no` | `no` | `yes` | clinicopathology summary candidate |
| `src-fip-019` | `https://academic.oup.com/jvim/article/37/5/1784/8447739` | `raw/images/fip/src-fip-019-candidate-treatment-protocol-summary-table.png` | `no` | `no` | `yes` | treatment package summary candidate |
| `src-fip-019` | `https://academic.oup.com/jvim/article/37/5/1784/8447739` | `raw/images/fip/src-fip-019-candidate-outcome-by-disease-form-figure.png` | `no` | `no` | `yes` | outcome split candidate |
| `src-fip-023` | `https://journals.sagepub.com/doi/10.1177/1098612X15574757` | `raw/images/fip/src-fip-023-candidate-csf-rt-pcr-performance-table.png` | `no` | `no` | `yes` | neurologic diagnostic performance candidate |
| `src-fip-023` | `https://journals.sagepub.com/doi/10.1177/1098612X15574757` | `raw/images/fip/src-fip-023-candidate-neurologic-versus-general-workup-branch.png` | `no` | `no` | `yes` | subgroup branch candidate |
| `src-fip-024` | `https://academic.oup.com/jvim/article/34/4/1587/8448359` | `raw/images/fip/src-fip-024-candidate-neurologic-treatment-course-summary.png` | `no` | `no` | `yes` | neurologic treatment course candidate |
| `src-fip-024` | `https://academic.oup.com/jvim/article/34/4/1587/8448359` | `raw/images/fip/src-fip-024-candidate-followup-imaging-or-csf-panel.png` | `no` | `no` | `yes` | follow-up panel candidate |

## Hard Rule

没有核对原文之前：

- 不要写真实 `fig2` / `table3`
- 不要声称某张候选图就是论文里的最终标签
- 不要在 compiled page 里把候选文件当成已验证证据

## Related Pages

- [FIP image ingest pilot](fip-image-ingest-pilot-20260417.md)
- [FIP image ingest manifest](fip-image-ingest-manifest-20260417.md)
- [image ingest protocol](image-ingest-protocol-20260416.md)

## One-Line Summary

这页的作用不是决定抓什么图。

它是把：

`真实 source link -> candidate asset -> verified rename`

压成一张能执行的 checklist。
