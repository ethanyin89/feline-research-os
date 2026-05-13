# Handoff, 2026-05-06 Session

This is the current handoff for the next model.

## Task Type

按 `/autoplan`，当前任务属于：

`方案 + 内容处理`

不是想法，不是检查，也不是排查。

The user gave a hard operating rule:

`do not do one-off repeated work; manually run 3-10 real samples first; after approval, codify into a durable owner; only cron deterministic checks, not judgment-heavy content promotion.`

## Current Repo Reality

- This directory is not a git repo in the current shell. Do not rely on git diff/base branch.
- Content side is the active line, not frontend/UI polish.
- The repo now has `144` strict disease paper cards in health output: CKD, FIP, HCM, IBD, Diabetes, and FCV each show `24 full / 24 deep_extracted`.
- Regulation source cards: `14`.
- Health is active with one expected warning: one staged inbox file.
- Latest health report: [system/health-checks/health-report-20260506.md](system/health-checks/health-report-20260506.md)

## What Was Done In This Session

### 1. Manual prototype, then codified workflow

First, a 6-sample manual run was done across IBD/FIP:

- IBD diagnostic workup sequence
- IBD treatment branch order
- IBD claim-fit / route-fit boundary
- FIP diagnostic workup sequence
- FIP assay-performance boundary
- FIP regulatory route control

That prototype is now archived as:

- [system/indexes/content-precision-sample-run-20260506.md](system/indexes/content-precision-sample-run-20260506.md)

Then it was codified as the durable owner:

- [system/indexes/content-precision-promotion-workflow.md](system/indexes/content-precision-promotion-workflow.md)

This workflow is now linked from:

- [system/indexes/content-side-densification-queue.md](system/indexes/content-side-densification-queue.md)
- [system/indexes/cross-disease-densification-queue.md](system/indexes/cross-disease-densification-queue.md)
- [system/indexes/query-to-writeback.md](system/indexes/query-to-writeback.md)
- [system/indexes/narrow-owner-densification-pattern.md](system/indexes/narrow-owner-densification-pattern.md)

### 2. First real promotion batch was staged

The first real batch using the new workflow was staged, processed, and archived at:

- [inbox/rejected/processed/content-precision-promotion-batch-20260506.md](inbox/rejected/processed/content-precision-promotion-batch-20260506.md)

Do not treat the archived inbox note as a live backlog item. Its accepted findings were written into canonical targets later.

Batch decisions:

| # | Candidate | Decision |
|---|---|---|
| 1 | FIP neurologic workup branch boundary | `partial-promote / status-sync` |
| 2 | FIP neurologic rescue boundary | `partial-promote / status-sync` |
| 3 | IBD best-overall vs route-cleaner archetype | `partial-promote / status-sync` |
| 4 | FIP antiviral product-archetype route boundary | `needs source access` |
| 5 | FIP non-CSF assay-performance gap | `hold` |
| 6 | IBD jurisdiction-specific route interpretation | `needs source access` |

Key read:

- Many second-wave owners are already absorbed by target pages.
- No immediate canonical disease-page edits are needed from that batch.
- Next real content work should be official-source precision, not another memo-writing pass.

### 3. Small unrelated link fix

`.claude/skills/topic-recompile.md` had a placeholder markdown link:

`../../system/indexes/{disease}-{type}-memo.md`

The link checker treated it as real. It was converted to a code path example.

## Current Verification

Run status after the staged batch:

```bash
python3 scripts/check_markdown_links.py
```

Result:

`PASS: checked 773 markdown files, no local link issues found.`

```bash
python3 scripts/health.py
```

Result:

- health report generated at [system/health-checks/health-report-20260506.md](system/health-checks/health-report-20260506.md)
- status active
- historical note: this session originally had one active inbox file; it has since been processed and archived

## Next Move

Recommended next move:

`official-source precision batch for FIP regulatory current status`

Do this only with current official sources. Because this is regulatory/current-status work, browse or otherwise verify current official pages. Do not rely on old local assumptions.

Target checks:

1. Current Animal Drugs @ FDA / Green Book check for FIP antiviral entries.
2. GS-441524 office-stock nomination / list-status check.
3. EMA Article 23 eligibility screen for baseline GS-441524 FIP indication.

Stage results first in `inbox/`.

Do not directly edit:

- `topics/fip/regulatory-brief.md`
- `topics/fip/current-state-dashboard.md`
- any output briefing/dossier/slides

until the staged official-source batch is coherent.

## Files To Read First

1. [HANDOFF.md](HANDOFF.md)
2. [system/indexes/content-precision-promotion-workflow.md](system/indexes/content-precision-promotion-workflow.md)
3. [inbox/rejected/processed/content-precision-promotion-batch-20260506.md](inbox/rejected/processed/content-precision-promotion-batch-20260506.md)
4. [topics/fip/regulatory-brief.md](topics/fip/regulatory-brief.md)
5. [system/indexes/fip-antiviral-product-archetype-route-boundary-memo.md](system/indexes/fip-antiviral-product-archetype-route-boundary-memo.md)
6. [system/indexes/fip-baseline-gs-us-conditional-approval-eligibility-memo.md](system/indexes/fip-baseline-gs-us-conditional-approval-eligibility-memo.md)
7. [system/indexes/fip-baseline-gs-us-active-control-design-map-memo.md](system/indexes/fip-baseline-gs-us-active-control-design-map-memo.md)
8. [system/indexes/fip-baseline-gs-us-comparator-boundary-memo.md](system/indexes/fip-baseline-gs-us-comparator-boundary-memo.md)

## Do Not Do

- Do not reopen generic source-card thickening.
- Do not create another workflow before using the one just codified.
- Do not set cron for judgment-heavy promotion.
- Do not promote route claims without current official-source anchors.
- Do not let FIP treatment strength become regulatory legitimacy.
- Do not turn CSF RT-PCR into a generic FIP assay leaderboard.
- Do not treat IBD diet-first practical strength as jurisdiction readiness.

## One-Line State

The system now knows how to handle repeated post-full-source-card content promotion. The next model should run the official-source FIP regulatory precision batch and stage it, not write canonical route claims directly.
