---
id: system-usage-limit-emergency-handoff-20260417
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

# Usage-Limit Emergency Handoff, 2026-04-17

这页只回答一个问题：

`如果模型快到 usage limit，下一位模型怎样在 60 秒内接手，而不重新探索整个 repo？`

## 类型判断

按 `$autoplan` 的四分法，这件事属于：

`检查`

不是新方案。

因为目标不是重新决定方向，而是把当前真实状态压成最短可执行接力面。

## 15-Second Truth

当前 repo 的关键现实只有 4 句：

1. `scripts/query.py` 和 `scripts/app.py` 的 vision integration 已经做完。
2. `CKD / FIP / IBD / HCM` 的 image-ingest skeleton 文档都已经做完。
3. `src-ckd-001`、`src-ckd-017`、`src-ckd-022` 和 `src-ckd-024` 已经有 8 个真实 CKD 资产落在 `raw/images/ckd/`，并且已核到原文标签。
4. 所以当前 blocker 不是代码，也不是文档结构，而是剩余 `CKD Step 2 image extraction` 只还缺 `013` 的 source-access 解锁。

## If You Only Read Three Files

按这个顺序读：

1. [PLAN.md](../../PLAN.md)
2. [model-continuity-handoff-20260417.md](model-continuity-handoff-20260417.md)
3. [ckd-image-download-checklist-20260417.md](ckd-image-download-checklist-20260417.md)

如果只读完这 3 个文件，你就已经知道当前 round 的 90%。

如果你正好是这一轮最后负责收口的人，再加读：

4. [final-integrator-closeout-checklist-20260418.md](final-integrator-closeout-checklist-20260418.md)

## Verify In 3 Commands

如果你不信 handoff，先自己确认。只跑这 3 条：

```bash
find raw/images -maxdepth 2 -type f | sort
sed -n '78,100p' PLAN.md
sed -n '1,220p' system/indexes/ckd-image-download-checklist-20260417.md
```

你会看到：

- `raw/images/ckd/` 不再只有 README，而且现在有 8 个真实 CKD 资产
- `PLAN.md` 里 Step 2 已经达到 MVP threshold met
- CKD checklist 里 `src-ckd-001` 两行、`src-ckd-017` 两行、`src-ckd-022` 两行和 `src-ckd-024` 两行已经变成 `Downloaded = yes`

## Last Verified Snapshot

上次人工核对时间：

`2026-04-18`

当时看到的真实输出是：

```text
find raw/images -maxdepth 2 -type f | sort
raw/images/README.md
raw/images/ckd/README.md
raw/images/ckd/src-ckd-001-mechanism-risk-factor-summary.jpg
raw/images/ckd/src-ckd-001-mechanism-schematic.jpg
raw/images/ckd/src-ckd-017-imaging-pathology-classification-panel.jpg
raw/images/ckd/src-ckd-017-outcome-upc-by-subtype-table.png
raw/images/ckd/src-ckd-022-pathology-histopath-findings-table.png
raw/images/ckd/src-ckd-022-outcome-time-course-gfr-creatinine-table.png
raw/images/ckd/src-ckd-024-outcome-biomarker-comparison-table.png
raw/images/ckd/src-ckd-024-outcome-biomarker-landscape.jpeg
raw/images/fip/README.md
raw/images/hcm/README.md
raw/images/ibd/README.md
raw/images/shared/README.md
```

`PLAN.md` 对应段落仍然写着：

- `Step 2: CKD Figure Extraction (MVP THRESHOLD MET — 8 verified figures on disk)`
- `src-ckd-001`, `src-ckd-017`, `src-ckd-022`, and `src-ckd-024` have 8 verified CKD assets on disk
- remaining CKD sources are still blocked on source access

`ckd-image-download-checklist-20260417.md` 对应段落仍然写着：

- the 2 `src-ckd-001` rows are `Downloaded = yes`
- the 2 `src-ckd-001` rows are `Verified against article label = yes`
- the `src-ckd-017` UPC-table row is `Downloaded = yes`
- the `src-ckd-017` pathology-panel row is `Downloaded = yes`
- the `src-ckd-022` histopath-findings row is `Downloaded = yes`
- the `src-ckd-022` time-course row is `Downloaded = yes`
- the `src-ckd-024` comparison-table row is `Downloaded = yes`
- the `src-ckd-024` biomarker-landscape row is `Downloaded = yes`

如果你现在重跑命令看到的结果不同，说明状态变了。
从差异继续，不要从旧 narrative 继续。

## What Is Actually Blocked

当前卡住的是：

`PLAN.md -> Step 2: CKD Figure Extraction`

而且这个 blocker 现在已经缩小了，不是原地不动：

- `src-ckd-001` 的 2 张图、`src-ckd-017` 的 1 张表格渲染、`src-ckd-024` 的 1 张图已经落盘并完成核对
- `src-ckd-017` 的 pathology panel 也已经落盘并完成核对
- `raw/images/ckd/` 不再只有 `README.md`
- 但 `src-ckd-013` 仍然卡在 source access。ScienceDirect 直链是 Cloudflare `403`，Nottingham mirror 页面落到 Cloudflare challenge，bitstream API 也回 `401 Unauthorized`；`nottingham-repository.worktribe.com` output 页面也是 challenge 壳页；Bristol / handle publication 页面只给 metadata 和 abstract，没有 full-text 下载。`src-ckd-022` 的两张真实表格资产已经落盘；之前的 model-design candidate 因无可验证原始对象而退役

## What Not To Re-Do

不要重做这些：

- `scripts/query.py / scripts/app.py / scripts/test_query.py`
- HCM image-ingest pilot / manifest / checklist
- FIP image-ingest pilot / manifest / checklist
- IBD image-ingest pilot / manifest / checklist
- CKD image-ingest pilot / manifest / checklist 的结构设计
- 全局 audit / maturity / queue / dashboard 页

这些已经不是当前 round 的瓶颈。

## What To Do If Assets Are Still Missing

如果你接手时，剩余 CKD 源还是没有对应 PDF 或导出的图片文件：

1. 不要伪造“已下载”或“已核对”
2. 不要继续横向补别的 disease 文档
3. 只确认 blocker 仍然存在
4. 把 blocker 维持在这 4 个文件里一致：
   - `PLAN.md`
   - `system/indexes/model-continuity-handoff-20260417.md`
   - `system/indexes/codex-next-session-prompt.md`
   - `system/indexes/usage-limit-emergency-handoff-20260417.md`

这就够了。不要扩写。

## What To Do If Assets Appear

如果你接手时，环境里已经出现剩余 CKD 源对应 PDF 或导出的 PNG：

只做这一条窄链路：

1. 只从 `src-ckd-013` 里继续补文件到 `raw/images/ckd/`
2. 核对 article label
3. 更新这 5 张 source card 的 `local_assets`
4. 更新 [ckd-image-download-checklist-20260417.md](ckd-image-download-checklist-20260417.md)
5. 更新 [PLAN.md](../../PLAN.md)
6. 然后再跑 vision demo

不要在这一步顺手去改：

- 新 disease
- 新 UI
- 新 routing
- 新 acceptance docs

## When The Blocker Is Actually Cleared

不要因为“看到了 PDF”就宣布 blocker 解除。

只有这 3 条同时成立，才算真的开始往前动：

1. `raw/images/ckd/` 里出现至少一个新的真实图片文件，超出当前 `src-ckd-001` 这 2 张
2. 它能对上 CKD checklist 里的某一行 candidate asset
3. 它能回到 source card 里的真实 article link

## Exact CKD Scope

只围绕这 5 张 source：

- [src-ckd-001.md](../../raw/papers/src-ckd-001.md)
- [src-ckd-013.md](../../raw/papers/src-ckd-013.md)
- [src-ckd-017.md](../../raw/papers/src-ckd-017.md)
- [src-ckd-022.md](../../raw/papers/src-ckd-022.md)
- [src-ckd-024.md](../../raw/papers/src-ckd-024.md)

## Copy-Paste Prompt

如果你要把这一棒交给另一个模型，直接贴这个：

```text
You are working in:
/Users/jiawei/Desktop/insclaude/feline-research-os

Read only these files first:
1. PLAN.md
2. system/indexes/usage-limit-emergency-handoff-20260417.md
3. system/indexes/ckd-image-download-checklist-20260417.md

Current date: 2026-04-17

Task type:
CHECK, not a new plan.

Current round goal:
Either confirm the CKD image-extraction blocker is still real, or, if local assets now exist,
advance only the CKD image gate to unlock the first vision demo.

Hard rules:
- do not redo HCM/FIP/IBD image-ingest docs
- do not change scripts/ unless the CKD image gate is actually unblocked and forces it
- do not fake downloaded or verified image status
- do not widen scope beyond the 5 CKD pilot sources

If no local CKD PDFs or exported figures exist:
- stop after confirming the blocker
- keep the handoff docs consistent
- report the blocker plainly

If local CKD PDFs or exported figures do exist:
- work only on raw/images/ckd/, the 5 CKD source cards, the CKD checklist, and PLAN.md
- verify article labels before final renames
- then report exactly what changed
```

## One-Line Summary

usage limit 真来了，最稳的接法不是“继续看 repo”。

而是：

`先看这页，确认 blocker 还在不在，然后只做 CKD image gate 这一棒。`
