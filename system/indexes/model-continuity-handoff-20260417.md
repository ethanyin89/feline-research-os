---
id: system-model-continuity-handoff-20260417
type: system
topic: operating-system
question_type: workflow
language: zh
last_compiled_at: 2026-04-18
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Model Continuity Handoff, 2026-04-17

这页只回答一个问题：

`如果当前任务因为 token 或模型切换要交给另一个模型，怎样保证不中断，而且不回头重做已经完成的东西？`

如果只想要最短 emergency 接手版，直接看：

- [Usage-limit emergency handoff, 2026-04-17](usage-limit-emergency-handoff-20260417.md)

## 类型判断

按 `$autoplan` 的四分法，这件事现在属于：

`检查`

不是新想法，不是新方案，也不是排查故障。

更准确地说，是：

`先检查 repo 真实状态，再按最窄执行断点接力。`

## 最短结论

不要再把下一棒写成：

`继续补 HCM image-ingest skeleton`

因为这一步已经完成了。

当前真正卡住的不是 skeleton，而是：

`真实图片还没有落盘，vision demo 仍然卡在 CKD figure extraction。`

## 当前已锁定的现实

### 1. Vision integration 代码已经在

[PLAN.md](../../PLAN.md) 已明确记录：

- `scripts/query.py` 已支持把 verified local assets 作为 image blocks 送进 Claude synthesis
- `scripts/app.py` 已支持把被回答引用的图片渲染出来
- `scripts/test_query.py` 已补 vision 相关测试
- 当前计划状态是：
  `Implementation complete (Steps 3-4). Human gate pending (Step 2 figure extraction).`

也就是说：

`代码主线不是当前瓶颈。`

### 2. 四个病种的 image-ingest skeleton 都已经在

现在 repo 里已经有：

- CKD pilot / manifest / checklist
- FIP pilot / manifest / checklist
- IBD pilot / manifest / checklist
- HCM pilot / manifest / checklist

对应 4 个 disease bucket 的 source cards 也已经写入了 `links.local_assets` 的
`candidate-*` 路径。

所以：

`不要再重做 pilot / manifest / checklist 这一层。`

### 3. 真正缺的现在是剩余 CKD raw image assets

当前 `raw/images/` 下面只有这些：

- `raw/images/README.md`
- `raw/images/ckd/README.md`
- `raw/images/ckd/src-ckd-001-mechanism-risk-factor-summary.jpg`
- `raw/images/ckd/src-ckd-001-mechanism-schematic.jpg`
- `raw/images/ckd/src-ckd-017-outcome-upc-by-subtype-table.png`
- `raw/images/ckd/src-ckd-017-imaging-pathology-classification-panel.jpg`
- `raw/images/ckd/src-ckd-022-pathology-histopath-findings-table.png`
- `raw/images/ckd/src-ckd-022-outcome-time-course-gfr-creatinine-table.png`
- `raw/images/ckd/src-ckd-024-outcome-biomarker-comparison-table.png`
- `raw/images/ckd/src-ckd-024-outcome-biomarker-landscape.jpeg`
- `raw/images/fip/README.md`
- `raw/images/hcm/README.md`
- `raw/images/ibd/README.md`
- `raw/images/shared/README.md`

`src-ckd-001`、`src-ckd-017` 和 `src-ckd-024` 已经不再是纯 candidate-only：

- `Downloaded = yes`
- `Verified against article label = yes`

但剩余 CKD pilot rows 仍然没有往前动。

所以当前系统现实是：

`image-aware 架构已经在，image-aware 证据层已经从 0 变成 5，但 CKD pilot 还没跑通。`

### 4. 当前最值钱的下一棒是 CKD，不是 HCM

为什么不是继续往 HCM 写文档：

- HCM skeleton 已经完成
- CKD 是当前 vision-integrated query plan 里明确写死的 MVP gate
- `PLAN.md` 里 pending 的 Step 2 指向的就是 CKD 5 篇 pilot source
- 没有 CKD 真实图片落盘，就没有 ask-the-vault 的第一轮 vision demo

所以当前最合适的 narrow goal 是：

`把 CKD pilot 的真实图片 extraction / verification 往前推进一棒。`

## 当前不要重做的东西

下一个模型不应该回头重做这些：

- `scripts/query.py / scripts/app.py / scripts/test_query.py`
- `CKD / FIP / IBD / HCM` 已存在的 image pilot / manifest / checklist
- 已经写好的 `local_assets: candidate-*` source-card 结构
- 全局 audit / maturity / queue / dashboard 大页
- “为什么要做 image-ingest” 这一层解释文档

这些已经够稳了。

## 当前最适合交接的下一步

### Narrow Goal

把 `CKD` 的真实图片落盘和核对推进到能支撑第一轮 vision demo。

### Why CKD Next

- 它是当前 query vision plan 的 MVP gate
- `PLAN.md` 已经把它标成唯一未完成的人机边界步骤
- 这一步完成后，`query.py` 和 `app.py` 才第一次能显示真实 figure
- 它比继续横向补文档更接近用户真正会感受到的价值

### Suggested CKD Pilot Set

继续围绕这 5 张 source card：

1. [src-ckd-001.md](../../raw/papers/src-ckd-001.md)
2. [src-ckd-013.md](../../raw/papers/src-ckd-013.md)
3. [src-ckd-017.md](../../raw/papers/src-ckd-017.md)
4. [src-ckd-022.md](../../raw/papers/src-ckd-022.md)
5. [src-ckd-024.md](../../raw/papers/src-ckd-024.md)

原因很简单：

- 它们已经在 CKD pilot / manifest / checklist 里写死
- 它们正是 `PLAN.md` 里 Step 2 指定的 5 篇
- 继续这 5 篇，不会引入新的 write surface

## Handoff Prompt

直接给下一个模型这段：

```text
You are working in this repo:
/Users/jiawei/Desktop/insclaude/feline-research-os

Read these files first (in this order):
1. system/indexes/multi-model-collaboration-boundary.md
2. system/indexes/model-continuity-handoff-20260417.md
3. PLAN.md
4. system/indexes/image-ingest-protocol-20260416.md
5. system/indexes/ckd-image-download-checklist-20260417.md

Current date: 2026-04-17

Your role:
WRITER FOR ONE NARROW SCOPE ONLY

Current round goal:
Advance the CKD pilot from candidate image placeholders to real, verified local assets
that can unlock the first vision-integrated ask-the-vault demo.

Current reality you must respect:
- vision integration code is already implemented
- CKD/FIP/IBD/HCM image-ingest skeleton docs already exist
- raw/images/ckd/ already contains 8 verified CKD assets from src-ckd-001, src-ckd-017, src-ckd-022, and src-ckd-024
- do not redo HCM or other disease skeleton work

Your write scope:
- raw/images/ckd/
- raw/papers/src-ckd-001.md
- raw/papers/src-ckd-013.md
- raw/papers/src-ckd-017.md
- raw/papers/src-ckd-022.md
- raw/papers/src-ckd-024.md
- system/indexes/ckd-image-download-checklist-20260417.md
- PLAN.md

Forbidden files:
- scripts/
- outputs/
- topics/fip/
- topics/ibd/
- topics/hcm/
- system/indexes/hcm-image-ingest-pilot-20260417.md
- system/indexes/hcm-image-ingest-manifest-20260417.md
- system/indexes/hcm-image-download-checklist-20260417.md
- system/indexes/fip-image-ingest-pilot-20260417.md
- system/indexes/fip-image-ingest-manifest-20260417.md
- system/indexes/fip-image-download-checklist-20260417.md
- system/indexes/ibd-image-ingest-pilot-20260417.md
- system/indexes/ibd-image-ingest-manifest-20260417.md
- system/indexes/ibd-image-download-checklist-20260417.md
- system/indexes/multi-disease-llm-wiki-status-audit-20260410.md
- system/indexes/disease-module-maturity-ladder.md
- system/indexes/cross-disease-densification-queue.md
- system/indexes/content-side-densification-queue.md

Hard rules:
- all material must be based on the real source links already present in the source cards
- no fake data allowed
- before article-label verification, do not claim real fig/table numbers
- do not treat candidate assets as verified evidence

Do:
- work only on the 5 CKD pilot sources already named in the checklist
- continue from the existing src-ckd-001/src-ckd-017/src-ckd-024 assets and only add remaining verified CKD assets under raw/images/ckd/
- update checklist rows from no -> yes only when the file is truly present or verified
- rename candidate assets only after article-label verification is complete
- keep PLAN.md aligned with the real execution state

Do not:
- rewrite the image-ingest architecture
- create new pilot/manifest/checklist docs for other diseases
- change query.py, app.py, tests, or acceptance docs
- widen scope to new sources

If the required PDFs or image files are not available in the environment:
- do not fake progress
- stop after confirming the blocker
- report exactly which source(s) are blocked and why

At the end, return:
1. which CKD source cards were touched
2. which files were added under raw/images/ckd/
3. which checklist rows changed
4. whether PLAN.md status changed
5. any remaining blockers for the vision demo
```

## Operator Rule

如果中途再次换模型，继续沿用同一条规则：

`不要交接“整个项目”，只交接当前最窄的执行断点。`

这次这个断点就是：

`CKD real image extraction + verification for the vision demo`

不是 HCM skeleton，也不是全局 status rewrite。

## One-Line Summary

当前最稳的 continuity 方案不是“让另一个模型继续补文档”。

而是：

`承认 skeleton 已经齐了，把下一棒收缩到 CKD 真实图片落盘与核对。`
