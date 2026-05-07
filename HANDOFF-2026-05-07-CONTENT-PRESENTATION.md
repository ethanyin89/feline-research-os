# Handoff, 2026-05-07 Content And Presentation

This is the focused handoff for the next model working on ordinary-user content and presentation.

## Task Type

按 `$autoplan`，当前任务属于：

`方案 + 普通用户可用性收敛`

不是继续堆内容，不是单点排查，也不是 UI 表面美化。当前目标是把已有内容、Ask the vault 路由、证据呈现和普通用户页面体验压成一个普通读者愿意使用的产品表面。

The user rule is binding:

`No one-off work. If a task will recur, first run 3-10 real samples manually, then codify it. Use cron only for deterministic automation, not judgment-heavy content promotion.`

## Current Reality

- This directory is not a git repo in the current shell.
- Latest health report: [system/health-checks/health-report-20260507.md](system/health-checks/health-report-20260507.md)
- Health status is `active`.
- Query tests: `102 passed | 0 failed`.
- Markdown links: PASS, `781` markdown files.
- Ordinary-user acceptance is currently `route-only` pass, not post-sanitizer live pass:
  - [system/health-checks/ordinary-user-acceptance-report-20260507.md](system/health-checks/ordinary-user-acceptance-report-20260507.md)
  - `Execution mode: route-only`
  - `Acceptance status: route_pass`
- The only health warning is the active inbox backlog.

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

## Why Live Acceptance Is Not Currently Final

Before the latest sanitizer changes, a full OpenRouter ordinary-user run reached `5/6` pass-leaning. The only miss was OU4 (`IBD和淋巴瘤怎么区分`) using informal Chinese source formatting rather than machine-readable source tags.

That sanitizer issue has now been fixed in code and tested.

A targeted live rerun of OU4 after the fix was blocked by OpenRouter:

```text
401 User not found
```

So the latest durable report was reset to route-only `route_pass`. Do not claim post-sanitizer full live pass until OpenRouter auth is stable and the full suite runs.

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

1. Stabilize OpenRouter auth and rerun the full ordinary-user live suite.
2. If live suite passes, keep compact overview context as default.
3. Inspect the actual Streamlit ordinary-user page with the 6 prompts.
4. Improve the first-screen value proposition and answer readability without changing source truth:
   - make “why this instead of Wikipedia” visible in the answer flow
   - make evidence/uncertainty/next-step cues readable to non-experts
   - keep source details available without forcing ordinary users to parse source IDs
5. Only after multiple clean live runs should any deterministic scheduled check be considered.

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
- ordinary-user route-only: `route_pass`
- markdown links: PASS
- health: `active`

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

The next model should make the ordinary-user value visible in content and presentation, but first must rerun the full live suite after OpenRouter auth is stable; route-only pass is not final product proof.
