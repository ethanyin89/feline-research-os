# Handoff, 2026-05-07 Content And Presentation

This is the focused handoff for the next model working on ordinary-user content and presentation.

## Task Type

按 `$autoplan`，当前任务属于：

`方案 + 普通用户可用性收敛`

不是继续堆内容，不是单点排查，也不是 UI 表面美化。当前目标是把已有内容、Ask the vault 路由、证据呈现和普通用户页面体验压成一个普通读者愿意使用的产品表面。

The user rule is binding:

`No one-off work. If a task will recur, first run 3-10 real samples manually, then codify it. Use cron only for deterministic automation, not judgment-heavy content promotion.`

## Current Reality

- This directory is now a git repo on branch `main`.
- Latest health report: [system/health-checks/health-report-20260507.md](system/health-checks/health-report-20260507.md)
- Health status is `active`.
- Query tests: `102 passed | 0 failed`.
- Markdown links: PASS, `782` markdown files.
- Ordinary-user acceptance has now passed the live OpenRouter suite:
  - [system/health-checks/ordinary-user-acceptance-report-20260507.md](system/health-checks/ordinary-user-acceptance-report-20260507.md)
  - Earlier durable route-only baseline: `6/6 route_pass`
  - Latest live OpenRouter rerun: `executed / pass`
  - Result: `6/6 automated pass-leaning answers`, `0` execution failures, `0` provenance misses, `0` route misses
- Current health warnings: none from inbox or ordinary-user acceptance.

## Product Judgment

The project is now structurally rich enough. The blocker is not lack of CKD/FIP/HCM/IBD/diabetes content.

The real user question is:

> Why would an ordinary reader use this instead of Wikipedia?

The answer direction is:

- source-aware synthesis across the vault
- visible distinction between evidence, synthesis, uncertainty, and inference
- natural routing from a user question into the right disease surface
- useful next step without requiring the user to browse markdown files

The next work should make that value obvious in the first screen and answer flow.

## What Changed Recently

### Ordinary-User Presentation Follow-Up

[scripts/app.py](scripts/app.py) now makes the ordinary-reader value proposition visible on first load:

- First screen says this is a source-aware feline wiki, not just a research chat.
- Example prompts now use 4 real ordinary-user acceptance questions:
  - `解释CKD`
  - `FIP怎么识别`
  - `IBD和淋巴瘤怎么区分`
  - `HCM是什么，为什么危险`
- Evidence labels are phrased for readers: quote / supported / inference.
- The trust block now shows readable source titles in addition to confidence and reading counts.
- The condition selector includes `FCV`, matching the sixth disease module now present in the vault.
- The chat input now asks for a natural feline health question instead of a research question.

### Ask The Vault Overview

[scripts/query.py](scripts/query.py) now has `overview` mode for broad ordinary-reader prompts:

- `解释CKD`
- `CKD`
- `HCM是什么，为什么危险`
- `我的猫肌酐升高，这个库能告诉我什么`

`overview` starts from:

- `topics/{disease}/current-state-dashboard.md`
- `topics/{disease}/synthesis-index.md`

It then uses compact context:

- compact topic-page excerpts
- compact source-card excerpts
- no figure attachments by default for overview

Manual live samples after compaction:

- `解释CKD`: about `4025` estimated tokens at synthesis.
- `HCM是什么，为什么危险`: about `2457` estimated tokens at synthesis.
- `我的猫肌酐升高，这个库能告诉我什么`: about `3669` estimated tokens at synthesis.

This is much cheaper than the earlier CKD overview path, which reached about `11k` loaded tokens.

### Provenance Handling

[scripts/query.py](scripts/query.py) now sanitizes provenance after synthesis:

- invalid source IDs are removed or downgraded
- informal Chinese source brackets containing real `src-*` IDs are normalized into machine-readable source tags
- loose `[llm_inference ...]` variants become `[llm_inference]`
- bare topic bracket references are downgraded

Do not remove this. It is a trust boundary.

### Acceptance Runner

[scripts/run_acceptance_checklist.py](scripts/run_acceptance_checklist.py) now supports:

```bash
python3 scripts/run_acceptance_checklist.py --suite ordinary-user --template-only
python3 scripts/run_acceptance_checklist.py --suite ordinary-user --route-only
OPENROUTER_DAILY_BUDGET_USD=1.00 OPENROUTER_MODEL=openai/gpt-4.1-mini .venv/bin/python scripts/run_acceptance_checklist.py --suite ordinary-user --backend openrouter
```

It also classifies runtime blockers:

- `backend-auth`
- `network`
- `rate-limit`

If a live run reports `blocked-runtime:backend-auth`, fix OpenRouter auth. Do not change content or routing in response to that report.

[scripts/app.py](scripts/app.py) now also shows the exact Streamlit restart command when OpenRouter is selected without the local budget guard:

```bash
OPENROUTER_DAILY_BUDGET_USD=1.00 OPENROUTER_MODEL=openai/gpt-4.1-mini .venv/bin/python -m streamlit run scripts/app.py
```

This addresses the UI failure mode where the sidebar says `OPENROUTER_DAILY_BUDGET_USD not set` and the user has no copyable local action.

## Live Acceptance Status

Before the latest sanitizer changes, a full OpenRouter ordinary-user run reached `5/6` pass-leaning. The only miss was OU4 (`IBD和淋巴瘤怎么区分`) using informal Chinese source formatting rather than machine-readable source tags.

That sanitizer issue has now been fixed in code and tested.

A full ordinary-user live rerun on 2026-05-07 now passes with OpenRouter:

```text
OPENROUTER_DAILY_BUDGET_USD=1.00 OPENROUTER_MODEL=openai/gpt-4.1-mini .venv/bin/python scripts/run_acceptance_checklist.py --suite ordinary-user --backend openrouter
→ executed / pass
→ 6/6 automated pass-leaning answers
→ 0 execution failures, 0 provenance misses, 0 route misses
```

Route-only can still be rerun to verify deterministic routing, but the current durable report is a live executed pass.

## Six Ordinary-User Acceptance Prompts

Use these exact samples. Do not invent a new suite unless these become insufficient after a real run.

1. `解释CKD`
2. `FIP怎么识别`
3. `HCM是什么，为什么危险`
4. `IBD和淋巴瘤怎么区分`
5. `糖尿病猫为什么会缓解`
6. `我的猫肌酐升高，这个库能告诉我什么`

Pass means:

- at least 5/6 acceptable live answers
- no execution failures
- no provenance misses
- no route misses
- overview questions start from `current-state-dashboard`
- recognition/endpoints questions are not flattened into generic overview

## Next Work For Content + Presentation

Do this in order.

1. Keep compact overview context as default.
2. Inspect the actual Streamlit ordinary-user page with the 6 prompts during normal UI QA.
3. Continue answer readability improvements without changing source truth:
   - make “why this instead of Wikipedia” visible in the answer flow
   - make evidence/uncertainty/next-step cues readable to non-experts
   - keep source details available without forcing ordinary users to parse source IDs
4. Only after multiple clean live runs should any deterministic scheduled check be considered.

## Do Not Do

- Do not restart broad content thickening.
- Do not treat route-only `route_pass` as final live answer quality.
- Do not change content because OpenRouter auth fails.
- Do not remove provenance sanitizer.
- Do not hide uncertainty to make answers feel smoother.
- Do not create a one-off test page or ad hoc sample list; use the codified 6 prompts.
- Do not cron judgment-heavy content or answer-quality decisions.

## Verification Commands

Run these before handing off again:

```bash
.venv/bin/python scripts/test_query.py
python3 scripts/run_acceptance_checklist.py --suite ordinary-user --route-only
python3 scripts/check_markdown_links.py
python3 scripts/health.py
python3 -m py_compile scripts/query.py scripts/test_query.py scripts/run_acceptance_checklist.py scripts/health.py
```

Expected current baseline:

- query tests: `102 passed | 0 failed`
- ordinary-user route-only: `route_pass` when run in route-only mode
- ordinary-user live OpenRouter: `executed / pass`
- markdown links: PASS
- health: `active`, ordinary-user acceptance PASS

## Files To Read First

1. [system/indexes/ordinary-user-karpathy-gap-recovery-plan-20260506.md](system/indexes/ordinary-user-karpathy-gap-recovery-plan-20260506.md)
2. [system/indexes/ordinary-user-acceptance-checklist-20260506.md](system/indexes/ordinary-user-acceptance-checklist-20260506.md)
3. [scripts/query.py](scripts/query.py)
4. [scripts/app.py](scripts/app.py)
5. [scripts/run_acceptance_checklist.py](scripts/run_acceptance_checklist.py)
6. [scripts/health.py](scripts/health.py)
7. [system/health-checks/health-report-20260507.md](system/health-checks/health-report-20260507.md)
8. [system/health-checks/ordinary-user-acceptance-report-20260507.md](system/health-checks/ordinary-user-acceptance-report-20260507.md)

## One Line

The next model should continue ordinary-user presentation QA from a passing live OpenRouter baseline; route-only remains useful for deterministic routing, but the current durable report is live executed pass.
