---
id: feline-literature-sheet-intake-workflow
type: system
topic: content-pipeline
question_type: workflow
language: zh
last_compiled_at: 2026-05-13
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# Feline Literature Sheet Intake Workflow

这页回答一个具体问题：

`用户给一张新的 feline 文献表时，怎样处理才不会变成一次性手工活？`

## Classification

默认分类：

`检查 + 内容处理流程`

不是新产品想法，不是架构方案评审，也不是 bug 排查。核心动作是把外部文献清单变成可审计、可重复、可回滚的 source intake manifest。

## Stop Rule

不要从 Google Sheet 直接批量创建 source cards。

固定顺序：

1. 读项目经验和现有 owner。
2. 读 sheet metadata 和精确 range。
3. 手动抽样 3-10 条。
4. 写 sample note。
5. 生成完整 intake manifest。
6. 审核 manifest 后才创建 first-pass source cards。
7. 只对高复用来源 selective deep extraction。

## Required Owners To Read

- `~/.gstack/projects/feline-research-os/learnings.jsonl`
- [source processing ledger](source-processing-ledger-120-20260421.md)
- [disease module bootstrap workflow](disease-module-bootstrap-workflow.md)
- [source hierarchy and claim-fit policy](source-hierarchy-and-claim-fit-policy.md)
- disease source index, source depth map, and narrow owner memos for the affected module

## Manual Sample

The sample must include at least:

| Sample Type | Why |
|---|---|
| existing seed row | Confirms old source IDs are stable. |
| duplicate row | Prevents redundant source cards. |
| new disease-specific source | Tests first-pass classification. |
| shared-source row | Tests cross-link vs duplicate-card policy. |
| section marker / blank row | Prevents headers from becoming fake sources. |

Write the sample under `system/indexes/` with:

- `verification_status: sampled`
- `status: pending-approval`

## Full Manifest

Use:

```bash
python3 scripts/literature_sheet_intake.py \
  --csv /tmp/feline-literature.csv \
  --repo-root . \
  --source-label "Google Sheet title, tab, date" \
  --out system/indexes/feline-literature-intake-manifest-YYYYMMDD.md
```

The manifest is a review artifact, not source truth.

It should classify rows as:

- `existing`
- `shared-existing`
- `duplicate-in-sheet`
- `new-diabetes`
- `new-obesity`
- `section-label`

If a future sheet introduces a different disease marker, update the script explicitly and rerun the 3-10 row sample.

## ID Policy

- Existing IDs do not move.
- Diabetes extension continues after the current corpus: `src-diabetes-025`, `src-diabetes-026`, ...
- Obesity starts as `src-obesity-001` if obesity becomes a first-class disease/topic module.
- Shared diabetes/obesity DOI rows should normally become cross-links and owner notes, not duplicate evidence text.

## Deep Extraction Policy

First-pass ingest is not the same thing as deep extraction.

Deep extraction is only for:

- practice guideline / consensus
- broad review that controls the disease shell
- backbone mechanism source
- treatment-control source
- boundary source likely to be reused across pages

Routine duplicates, case reports, and cross-species context sources should not be deep-extracted by default.

## Cron Policy

No cron by default.

Literature sheet intake is event-driven. Add cron only if the user turns a spreadsheet into a living queue that should be checked on a schedule.

## Current Implementation

- Repo script: [scripts/literature_sheet_intake.py](../../scripts/literature_sheet_intake.py)
- Source-card bootstrap script: [scripts/literature_source_card_bootstrap.py](../../scripts/literature_source_card_bootstrap.py)
- Installed Codex skill: `~/.codex/skills/feline-literature-intake/SKILL.md`
- First sample: [feline diabetes / obesity sheet sample](feline-diabetes-obesity-sheet-intake-sample-20260513.md)
- First full manifest: [feline diabetes / obesity intake manifest](feline-diabetes-obesity-intake-manifest-20260513.md)
- Current done definition: [feline diabetes / obesity processing definition](feline-diabetes-obesity-processing-definition-20260513.md)
- First full source-card bootstrap: `src-diabetes-025` through `src-diabetes-118` and `src-obesity-009` through `src-obesity-087`
