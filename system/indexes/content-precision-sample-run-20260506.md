---
id: inbox-content-precision-sample-run-20260506
type: inbox
topic: content-pipeline
question_type: workflow
language: bilingual
last_compiled_at: 2026-05-06
verification_status: provisional
decision_grade: no
language_qa_status: light_checked
owner: codex
status: promoted
---

# Content Precision Sample Run, 2026-05-06

## Classification

按 `/autoplan`，这件事属于：

`方案 + 内容处理`

不是想法，不是检查，也不是排查。

原因：用户给的是一条新的 operating rule，不能再做 one-off content work。当前正确动作是先在真实内容对象上手动跑 `3-10` 个样本，判断模式是否稳定，再决定是否固化成 durable owner。

## User Rule Being Tested

> 不允许做一次性工作。如果某件事将来还会做，就先手动跑 3-10 个样本，批准后固化成技能文件。如果需要自动运行，就设 cron。测试标准：如果同一件事问两次，就失败。

当前 repo 的本地映射来自：

- [durable agent codification protocol](durable-agent-codification-protocol.md)
- [content-side densification queue](content-side-densification-queue.md)
- [cross-disease densification queue](cross-disease-densification-queue.md)

在这个 vault 里，批准前不直接写新 `SKILL.md`。先用 `inbox/` 承接样本结果。批准后再固化为唯一 owner，可能是 `workflow`、`protocol`、`health check` 或真正的 skill 文件。

## Sample Set

| # | Disease | Object | Precision Type | Source Check | Sample Verdict |
|---|---|---|---|---|---|
| 1 | IBD | `ibd-diagnostic-workup-memo.md` | workup sequence | `src-ibd-015`, `src-ibd-009` worksheets | promote as control layer; do not turn into universal biopsy rule |
| 2 | IBD | `ibd-treatment-branch-comparison-memo.md` | treatment branch order | `src-ibd-014`, `src-ibd-021` worksheets | stable; keep diet-first as practical anchor, not final drug ranking |
| 3 | IBD | `ibd-claim-fit-route-fit-boundary-memo.md` + regulatory page | route-fit boundary | regulatory page + treatment worksheets | stable; hold route memo, promote only product-type framing |
| 4 | FIP | `fip-diagnostic-workup-memo.md` | workup sequence | `src-fip-010`, `src-fip-022`, `src-fip-023` worksheets | stable; keep composite-support order, not one-test diagnosis |
| 5 | FIP | `fip-assay-performance-boundary-memo.md` | assay boundary | `src-fip-023`, `src-fip-010`, `src-fip-022` worksheets | stable; CSF numbers are branch-specific, not a cross-assay leaderboard |
| 6 | FIP | `fip-regulatory-brief.md` | official-source route control | regulatory brief + FIP route memos | stable but thin; next pass should be current approved-record / office-stock / EMA eligibility checks |

## Sample Findings

### 1. IBD Workup Sequence

The current workup memo is structurally sound. `src-ibd-015` supports the key boundary: paired duodenal and ileal sampling can change lymphoma detection, with poor duodenal-versus-ileal agreement and lymphoma sometimes found only by ileal biopsy. `src-ibd-009` supports report-language/workflow structure, but explicitly should not be treated as decision-grade diagnosis.

Decision: keep the memo as a control layer for workup sequence. Promote its logic into output pages only where the page is making a lymphoma-exclusion or biopsy-site claim. Do not promote it into a universal "all cats need ileal biopsy" rule.

### 2. IBD Treatment Branch Order

The branch-comparison memo is stable. `src-ibd-014` supports hydrolysed diet response as the cleanest current practical anchor, while still warning that this sits inside chronic-enteropathy / food-responsive overlap. `src-ibd-021` is useful for the broader treatment map, but should remain subordinate to feline-primary practical anchors.

Decision: keep `diet-first chronic-enteropathy management` as the safest compiled default. Do not turn it into idiopathic-IBD-specific certainty or final drug ranking.

### 3. IBD Route-Fit Boundary

The regulatory page and route-fit memo agree: IBD is ready for product-type-first framing, not jurisdiction recommendation. The useful distinction is now `best overall archetype` versus `future route-cleaner candidate`.

Decision: promote claim-fit / route-fit separation in dashboards and regulatory overview language. Hold route-level memos until official-source regulatory material and route-fit evidence are thicker.

### 4. FIP Workup Sequence

The diagnostic-workup memo is stable. `src-fip-022` keeps mutation detection as a real utility branch. `src-fip-010` prevents mutation testing from becoming certainty language. `src-fip-023` keeps CSF RT-PCR inside neurologic/ocular branch logic.

Decision: keep FIP diagnosis as composite-support architecture. Clinicopathology and disease-form suspicion lead; mutation testing strengthens after suspicion; CSF belongs after neurologic/ocular branch shift.

### 5. FIP Assay Boundary

The assay memo has the right shape. The only extracted numeric assay-performance detail strong enough for direct reuse is currently the CSF branch: specificity `100%`, PPV `100%`, overall sensitivity `42.1%`, NPV `57.7%`, and neurologic/ocular sensitivity `85.7%` from the worksheet for `src-fip-023`.

Decision: use CSF numbers only for branch-specific positive support. Do not build a cross-assay leaderboard until mutation assays, serology, and acute-phase markers have comparable full-text performance extraction.

### 6. FIP Regulatory Route Control

The FIP regulatory brief is stronger than IBD's because it has jurisdiction-aware official-source framing and FIP-specific FDA compounded-GS context. It is still not route advice. The page itself already names the next real work: current approved-record / office-stock nomination checks, EMA Article 23 eligibility, China implementing notices, and UK route mapping.

Decision: next FIP regulatory pass should be official-source precision, not more treatment-branch prose. Start with current U.S. approved-record / office-stock status and EMA Article 23 eligibility for baseline GS-441524.

## Pattern Observed Across Samples

The repeating work is not "make source cards fuller." That layer is already complete at `120/120` source cards.

The repeating work is:

`narrow owner -> source-anchor check -> promote / hold / partial-promote -> dashboard/topic/output write-back`

The key judgment is whether a narrow owner is:

- safe enough to promote upward
- only safe as a control layer
- too thin and should stay parked

## Proposed Durable Owner After Approval

If this sample is approved, the right durable asset should be:

`system/indexes/content-precision-promotion-workflow.md`

Owner type: `workflow`

Why workflow, not prompt:

- the main problem is sequence and decision routing
- source-anchor checks must happen before promotion
- output is a repeatable promotion/hold decision, not just model tone

Minimum workflow steps:

1. Select `3-10` candidate narrow owners from current queues.
2. For each owner, read the owner page, target dashboard/topic page, and at least one supporting worksheet/source card.
3. Classify precision type: `workup`, `route-fit`, `assay`, `treatment-order`, `image/table`, `official-source`, or `output-specific`.
4. Decide: `promote`, `partial-promote`, `hold`, or `needs source access`.
5. Stage proposed write-back in `inbox/`, not direct topic edits.
6. After user approval, update topic/dashboard/output owners and sync queue/status maps.
7. If the same drift is measurable, add a health check.

## Cron / Automation Read

Do not set cron yet.

Reason: this is judgment-heavy content promotion, not a deterministic recurring command. Automating it before approval would create fake confidence.

Good future automation target:

- weekly health check that flags stale queue/dashboard disagreement
- not automatic content promotion

Possible later command:

`python3 scripts/health.py`

But only after the workflow owner defines what stale state means.

## Approval Gate

This sample run recommends codifying the observed pattern as:

`content-precision-promotion-workflow.md`

Approved by user instruction `continue` on 2026-05-06 and codified as:

- [content precision promotion workflow](content-precision-promotion-workflow.md)
