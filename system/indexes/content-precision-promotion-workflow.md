---
id: system-content-precision-promotion-workflow
type: system
topic: content-pipeline
question_type: workflow
language: bilingual
last_compiled_at: 2026-05-06
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Content Precision Promotion Workflow

这页回答的是一个 operator 问题：

`当 source cards 已经 full，但内容侧还要继续变厚时，下一轮到底怎么做，才不是一次性工作？`

## Classification

按 `/autoplan`，这件事属于：

`方案 + 内容处理`

不是想法，不是检查，也不是排查。

因为当前要固定的是一条可重复执行的内容提升流程，而不是验证单个事实或修单个 bug。

## One-Line Rule

当 disease module 已经有 `24/24` source cards、`24/24` worksheets、explicit full source-card depth 时，下一轮默认不要再做 generic thickening。

默认走：

`narrow owner -> source-anchor check -> promote / partial-promote / hold -> inbox write-back -> dashboard/topic/output sync`

## Why This Workflow Exists

当前 vault 的 `120` source-card 层已经完成。

后续重复出现的内容工作，不再是：

- 建 source card
- 补 round-1 worksheet
- 让 broad page 看起来更完整

而是：

- 一个窄 owner 是否已经稳定到能上升
- 一个 branch boundary 是否只能保留为控制层
- 一个 route-fit / assay / workup 判断是否有足够 source anchor
- 一个 dashboard 或 output 是否应该吸收这个新边界

这类工作如果每次靠重新解释，就是系统失败。

## Source Prototype

This workflow was codified after a six-sample manual run:

- [content precision sample run, 2026-05-06](content-precision-sample-run-20260506.md)

Sample coverage:

- IBD diagnostic workup sequence
- IBD treatment branch order
- IBD claim-fit / route-fit boundary
- FIP diagnostic workup sequence
- FIP assay-performance boundary
- FIP regulatory route control

## When To Use This

Use this workflow when all are true:

1. The disease module is already source-card complete.
2. A narrow owner, dashboard line, topic page, or output claim needs promotion judgment.
3. The work is about `precision`, not broad bootstrap.
4. The likely output is a `promote / partial-promote / hold / needs source access` decision.

Common precision types:

| Precision Type | Question It Answers | Typical Home |
|---|---|---|
| `workup` | what sequence should the module preserve? | diagnostic memo, risk/recognition page, dashboard |
| `route-fit` | is this claim route-safe or only product-type-safe? | regulatory brief, route boundary memo |
| `assay` | what can this marker/test claim without leaderboard drift? | endpoint page, assay boundary memo |
| `treatment-order` | which branch leads, follows, or stays exploratory? | translation page, treatment memo |
| `image/table` | does a figure/table change a claim or only illustrate it? | source card, image manifest, topic page |
| `official-source` | does official regulatory text change the safe read? | regulatory source card, regulatory brief |
| `output-specific` | does a briefing/dossier/slides claim need tighter wording? | output file, dashboard, synthesis |

## When Not To Use This

Do not use this workflow for:

- first-pass source ingest
- broad disease bootstrap
- ordinary UI/front-door polish
- purely stylistic wording
- claims without source-card or worksheet anchors
- automatic promotion from chat output

If the issue is a new repeated operating rule, go to:

- [durable agent codification protocol](durable-agent-codification-protocol.md)

If the issue is whether one query result should be written back at all, use:

- [write-back promotion checklist](writeback-promotion-checklist.md)

## Workflow

### Step 1: Select 3-10 Real Candidates

Pick from the active queues, not from vague memory:

- [content-side densification queue](content-side-densification-queue.md)
- [cross-disease densification queue](cross-disease-densification-queue.md)
- disease-specific dashboards
- disease-specific source depth maps

Do not choose candidates just because a page exists.

Choose candidates where a decision would change how the module should now be read.

### Step 2: Read The Owner And Its Target Surface

For each candidate, read:

1. the narrow owner or memo
2. the target topic/dashboard/output page
3. at least one supporting source card or worksheet

If the candidate has no direct source/worksheet anchor, default to `hold`.

### Step 3: Classify The Precision Type

Assign one primary type:

- `workup`
- `route-fit`
- `assay`
- `treatment-order`
- `image/table`
- `official-source`
- `output-specific`

If two types compete, choose the one that controls the overclaim risk.

Example: FIP CSF RT-PCR is tempting as `assay`, but its real overclaim risk is branch placement, so the promotion language must preserve neurologic/ocular branch shift.

### Step 4: Decide Promotion State

Use this decision table:

| Decision | Use When | Write-Back Behavior |
|---|---|---|
| `promote` | repeated, structurally clarifying, source-anchored enough | update target topic/dashboard/output |
| `partial-promote` | safe boundary exists, but stronger claim is still thin | update only boundary wording and verify-next links |
| `hold` | useful but under-anchored, too broad, or one-off | leave as memo/control layer |
| `needs source access` | source access or official text is missing | stage blocker and do not promote |

The default is not promotion.

The default is the smallest durable movement that prevents future overclaim.

### Step 5: Stage In `inbox/`

Before touching canonical topic/output pages, write a staged note in `inbox/`.

The note must include:

- candidate list
- source anchors checked
- promotion decision
- target write-back surfaces
- what not to say
- whether this should become a health check

This keeps reviewable content movement separate from canonical truth edits.

### Step 6: After Approval, Write Back

On approval, update the smallest necessary canonical surfaces:

1. one-language topic page
2. dashboard
3. bilingual high-reuse page, only if reuse pressure is real
4. output file, only if the output claim changes
5. cross-disease queue/status map, only if module read changes

Do not update every related page just because the link graph exists.

### Step 7: Sync State

After write-back, sync:

- `last_compiled_at`
- `verification_status`
- `language_qa_status`, if language-facing text changed
- relevant queue or dashboard status
- `inbox/` decision state

Run:

```bash
python3 scripts/check_markdown_links.py
python3 scripts/health.py
```

If a check fails, fix the structural issue before calling the promotion complete.

## Promotion Output Template

Use this shape in the staged `inbox/` note:

```markdown
# Content Precision Promotion Batch, YYYY-MM-DD

## Classification

`方案 + 内容处理`

## Candidates

| # | Disease | Object | Precision Type | Source Anchors | Decision | Target Surfaces |
|---|---|---|---|---|---|---|

## Decisions

### N. [Object]

Source check:

Decision:

What to promote:

What not to say:

Write-back target:

## Health Check Read

Should this become a recurring check?
```

## Cron / Automation Rule

Do not cron automatic content promotion.

This workflow is judgment-heavy.

Good automation target:

- stale queue/dashboard mismatch
- broken links after write-back
- source-state drift
- candidate image references leaking into `local_assets`
- high-visibility pages missing traceability tables

Bad automation target:

- deciding that a claim should be promoted
- rewriting topic truth without approval
- treating `compiled` as decision-grade

If the drift can be detected mechanically, add a health check. If it requires judgment, keep it as workflow.

## Fast Test

If the user asks for the same kind of content promotion twice, the system should already know to start here.

If it does not, this workflow is not wired deeply enough.

## Related Pages

- [durable agent codification protocol](durable-agent-codification-protocol.md)
- [content-side densification queue](content-side-densification-queue.md)
- [cross-disease densification queue](cross-disease-densification-queue.md)
- [narrow-owner densification pattern](narrow-owner-densification-pattern.md)
- [query to write-back](query-to-writeback.md)
- [write-back promotion checklist](writeback-promotion-checklist.md)
- [source processing ledger 120](source-processing-ledger-120-20260421.md)

## One-Line Summary

When source cards are already full, content work should move through promotion judgment, not more one-off thickening.
