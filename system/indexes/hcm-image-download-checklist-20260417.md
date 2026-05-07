---
id: system-hcm-image-download-checklist-20260417
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

# HCM Image Download Checklist, 2026-04-17

这页只回答一个执行问题：

`如果现在开始按真实 link 下载 HCM pilot 图片，应该怎么逐项核对，而不是边下边猜？`

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
  - `yes` = 文件已经在 `raw/images/hcm/`
- `Verified against article label`:
  - `no` = 还没核对原文编号
  - `yes` = 已确认 figure/table 标签
- `Final rename needed`:
  - `yes` = 需要把 `candidate-*` 改成真实标签
  - `no` = 当前文件名已经够稳，或者暂时保留 candidate 名

## Checklist

| Source | Real link | Candidate asset | Downloaded | Verified against article label | Final rename needed | Notes |
|---|---|---|---|---|---|---|
| `src-hcm-011` | `https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0168407` | `raw/images/hcm/src-hcm-011-fig-3-myk461-sam-lvot-gradient.png` | `yes` | `yes` | `no` | verified against PLOS article Fig 3; now listed in source-card `local_assets` |
| `src-hcm-001` | `https://journals.sagepub.com/doi/10.1177/1098612X211020162` | `raw/images/hcm/src-hcm-001-candidate-mechanism-overview.png` | `no` | `no` | `yes` | mechanism overview / HCM review schematic candidate |
| `src-hcm-001` | `https://journals.sagepub.com/doi/10.1177/1098612X211020162` | `raw/images/hcm/src-hcm-001-candidate-clinical-staging-diagram.png` | `no` | `no` | `yes` | clinical staging or pathophysiology summary candidate |
| `src-hcm-009` | `https://www.ahajournals.org/doi/10.1161/01.CIR.92.9.2645` | `raw/images/hcm/src-hcm-009-candidate-echo-phenotype-classification.png` | `no` | `no` | `yes` | echo hypertrophy pattern classification (diffuse vs segmental) candidate |
| `src-hcm-009` | `https://www.ahajournals.org/doi/10.1161/01.CIR.92.9.2645` | `raw/images/hcm/src-hcm-009-candidate-echo-measurements-table.png` | `no` | `no` | `yes` | echocardiographic measurements table candidate |
| `src-hcm-010` | `https://www.sciencedirect.com/science/article/abs/pii/S1760273409000095?via%3Dihub` | `raw/images/hcm/src-hcm-010-candidate-nt-probnp-threshold-scatter.png` | `no` | `no` | `yes` | NT-proBNP scatter / threshold figure (44 pmol/L boundary) candidate |
| `src-hcm-010` | `https://www.sciencedirect.com/science/article/abs/pii/S1760273409000095?via%3Dihub` | `raw/images/hcm/src-hcm-010-candidate-nt-probnp-roc-or-comparison-table.png` | `no` | `no` | `yes` | ROC curve or normal vs HCM comparison table candidate |
| `src-hcm-012` | `https://www.mdpi.com/2306-7381/11/5/214` | `raw/images/hcm/src-hcm-012-candidate-penetrance-curve-by-age.png` | `no` | `no` | `yes` | age-related penetrance curve (MYBPC3 p.A31P) candidate |
| `src-hcm-012` | `https://www.mdpi.com/2306-7381/11/5/214` | `raw/images/hcm/src-hcm-012-candidate-genotype-outcome-table.png` | `no` | `no` | `yes` | homo vs het outcome / cardiac death table candidate |
| `src-hcm-020` | `https://journals.sagepub.com/doi/10.1177/0300985819837717` | `raw/images/hcm/src-hcm-020-candidate-histopathology-panel.png` | `no` | `no` | `yes` | histopathology panel (HCM vs control myocardium) candidate |
| `src-hcm-020` | `https://journals.sagepub.com/doi/10.1177/0300985819837717` | `raw/images/hcm/src-hcm-020-candidate-macrophage-infiltration-figure.png` | `no` | `no` | `yes` | Iba1-positive macrophage-like cell density figure candidate |

## Hard Rule

所有图片必须来自 source card 里已有的真实链接。

不允许：

- AI 生成的图片
- 从其他来源自行搜索的替代图
- 使用 fig2 / table3 等真实标签，在核对原文之前

`candidate-*` 前缀是硬约束，不是风格选项。

## One-Line Summary

这页的作用是让 HCM 图片 pilot 可以按行执行，而不是靠记忆推进。

如果要看目标文件名的完整列表，使用：

- [HCM image ingest manifest](hcm-image-ingest-manifest-20260417.md)
