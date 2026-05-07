# Handoff, 2026-05-06 Session 2

This is the current handoff for the next model.

## Task Type

按 `$autoplan`，当前任务属于：

`方案 + 普通用户可用性收敛`

不是纯想法，不是单点检查，也不是故障排查。现在的核心问题已经变成：怎样把现有内容和问答链路，压成普通用户真正能看懂、能继续点下去的产品表面。

The user also set a hard operating rule:

`do not do one-off work; if something will happen again, manually run 3-10 real samples first, then codify it after approval. Use cron only for deterministic automation, not judgment-heavy content promotion.`

## Current Repo Reality

- This directory is still not a git repo in the current shell. Do not rely on git diff/base branch.
- Content work is not the main blocker anymore, the user-facing ask flow is.
- The repo health report is green except for the expected inbox warning.
- Latest health report: [system/health-checks/health-report-20260507.md](system/health-checks/health-report-20260507.md)
- `scripts/health.py` now includes a dedicated `Ordinary-user acceptance` row, backed by the ordinary-user acceptance report.
- The Streamlit test page is live at `http://localhost:8501`.

## What Was Done In This Session

### 1. Ordinary-user recovery plan was written

I added a dedicated recovery plan for the Karpathy-style ordinary-user gap:

- [system/indexes/ordinary-user-karpathy-gap-recovery-plan-20260506.md](system/indexes/ordinary-user-karpathy-gap-recovery-plan-20260506.md)

The plan now explicitly says the gap is not raw content volume. The gap is the content serving layer:

- routing
- synthesis contract
- evidence presentation
- ordinary-user acceptance

### 2. Ask-the-vault was changed to support broad ordinary-user questions

`scripts/query.py` now has an `overview` mode for broad reader prompts like `解释CKD` and exact disease-name prompts like `CKD`.

What changed:

- broad prompts route to `overview`
- `overview` loads a lighter starter bundle:
  - `current-state-dashboard.md`
  - `synthesis-index.md`
- synthesis now has an overview answer contract:
  - direct answer
  - reader meaning
  - key evidence
  - uncertainty
  - useful next step
- source-id parsing now handles both comma and semicolon separated tags

### 3. The UI trust surface was tightened

`scripts/app.py` now does a few things better for normal users:

- replaces the generic low-confidence note with a trust block that explains why confidence is low or medium
- shows claim-tag coverage and readings loaded
- shows the sources section from loaded source ids when available
- replaces the deprecated `st.components.v1.html()` clipboard widget with a Streamlit markdown download action
- root `start.md` and `reader-start-here.md` now say why this vault is useful compared with Wikipedia

### 4. Regression tests were extended

`scripts/test_query.py` now locks in the new behavior:

- `解释CKD` routes to `overview`
- exact disease-name prompts route to `overview`
- overview starter bundle is the expected 2-page CKD bundle
- semicolon-separated source ids parse correctly

Current result:

```bash
.venv/bin/python scripts/test_query.py
```

Current result after ordinary-user suite wiring:

```bash
.venv/bin/python scripts/test_query.py
```

Result: `99 passed | 0 failed | 99 total`

### 5. Ordinary-user acceptance checklist was codified

A dedicated manual acceptance checklist now exists for the broad-reader flow:

- [system/indexes/ordinary-user-acceptance-checklist-20260506.md](system/indexes/ordinary-user-acceptance-checklist-20260506.md)

This checklist captures the 6 sample prompts the next model should keep reusing:

- `解释CKD`
- `FIP怎么识别`
- `HCM是什么，为什么危险`
- `IBD和淋巴瘤怎么区分`
- `糖尿病猫为什么会缓解`
- `我的猫肌酐升高，这个库能告诉我什么`

The durable runner now supports this suite:

```bash
python3 scripts/run_acceptance_checklist.py --suite ordinary-user --template-only
python3 scripts/run_acceptance_checklist.py --suite ordinary-user --route-only
OPENROUTER_DAILY_BUDGET_USD=1.00 OPENROUTER_MODEL=openai/gpt-4.1-mini .venv/bin/python scripts/run_acceptance_checklist.py --suite ordinary-user --backend openrouter
```

Ordinary-user report generated at:

- [system/health-checks/ordinary-user-acceptance-report-20260507.md](system/health-checks/ordinary-user-acceptance-report-20260507.md)

Current latest status: `route_pass`.

Current latest route-only suite result:

- 6/6 automated pass-leaning answers
- 0 execution failures
- 0 provenance misses
- 0 route misses
- execution mode: `route-only`

The acceptance result is also wired into the daily health report:

- [system/health-checks/health-report-20260507.md](system/health-checks/health-report-20260507.md), row `Ordinary-user acceptance | PASS`

Important: `route_pass` only means the 6 ordinary-user questions hit the expected question type and strongest answer surface. `executed/pass` means the live suite ran and met the automated acceptance gates, but it is still not a substitute for human product judgment.

### 6. Live acceptance improved the product feel, then overview context was reduced

I ran the live OpenRouter ordinary-user suite after enabling network access. The earlier sandboxed attempt failed with `Operation not permitted`; the elevated run succeeded. The earlier `401 User not found` did not reproduce in this run.

Example observed result for `解释CKD`:

- `ROUTER_QTYPE=overview`
- `ROUTER_DISEASE=ckd`
- `FIRST_FAMILY=current-state-dashboard`
- Loaded 2 CKD starter pages + preheated source cards

The answer changed from a short summary into a wiki-style starter answer. It now has:

- direct explanation
- reader meaning
- evidence bullets
- unknowns
- suggested next reading

After that, the overview path was compacted:

- `scripts/query.py` now uses compact topic-page context for `overview` questions.
- `scripts/query.py` now uses compact source-card excerpts for `overview` questions.
- `overview` no longer attaches figures by default.
- provenance tags are sanitized after synthesis:
  - invalid source IDs are removed or downgraded
  - informal Chinese source brackets containing real `src-*` IDs are normalized into machine-readable tags
  - loose `[llm_inference ...]` variants are normalized to `[llm_inference]`

Manual live samples after compaction:

- `解释CKD`: synthesized 5 files at about `4025` estimated tokens; valid `src-*` tags only.
- `HCM是什么，为什么危险`: synthesized 5 files at about `2457` estimated tokens after sanitizer; invalid `src-hcm-mechanism` did not survive.
- `我的猫肌酐升高，这个库能告诉我什么`: synthesized 5 files at about `3669` estimated tokens; bare topic brackets are now sanitized in code.

Attempted full live suite after compaction:

- A full OpenRouter ordinary-user run wrote `ordinary-user-acceptance-report-20260507.md` with `5/6` pass-leaning before the sanitizer normalization for informal Chinese source brackets.
- The single miss was OU4 provenance formatting, not route quality.
- After adding the normalization, a targeted OU4 live rerun was blocked by OpenRouter `401 User not found`.
- Because backend auth became unstable, the latest durable report was reset to route-only `route_pass` rather than pretending the post-fix full live suite has passed.

The acceptance runner now treats this class of problem explicitly:

- `scripts/run_acceptance_checklist.py` classifies runtime blockers as `backend-auth`, `network`, or `rate-limit`.
- On runtime blockers it stops the suite early and reports `blocked-runtime:*`, instead of turning every question into a fake content failure.
- `scripts/test_query.py` includes tests for the runtime blocker classifier.

### 7. Acceptance report link hygiene was fixed

The live report exposed a recurring health issue: model answers can include relative Markdown links, and when those answers are embedded in `system/health-checks`, repo-wide markdown lint sees false broken links.

Fix made:

- `scripts/run_acceptance_checklist.py` now strips Markdown link syntax inside stored result excerpts while preserving the visible text and target path.
- The current ordinary-user report was patched so `python3 scripts/check_markdown_links.py` stays green.

## Current Constraint

The live overview path is now much lighter: CKD overview dropped from roughly `11k` loaded tokens to roughly `4k` on a manual live sample. The next model should not add more overview content until the post-sanitizer full live suite can run cleanly.

## What The Screenshots Show

Three screenshots were checked:

- English `explain feline CKD`
- Chinese `解释猫CKD`
- Wikipedia Chinese CKD page

The product is now usable as a research starter, but the remaining question is still real:

Why would a normal reader use this instead of Wikipedia?

Answer direction:

- because it gives source-aware synthesis across the vault
- because it can surface evidence and uncertainty directly
- because it can route into disease-specific subpages without manual navigation

But that value still has to be made obvious in the first screen, not just true under the hood.

## Next Move

The next model should do three things:

1. Restore or stabilize OpenRouter auth and rerun the full ordinary-user live suite. If the report says `blocked-runtime:backend-auth`, fix auth instead of changing content.
2. If live passes, keep the compact overview context as the default.
3. Decide whether this should become cron only after the live suite has multiple clean runs. Do not cron judgment-heavy content promotion.

Recommended acceptance prompts:

1. `解释CKD`
2. `FIP怎么识别`
3. `HCM是什么，为什么危险`
4. `IBD和淋巴瘤怎么区分`
5. `糖尿病猫为什么会缓解`
6. `我的猫肌酐升高，这个库能告诉我什么`

## Files To Read First

1. [system/indexes/ordinary-user-karpathy-gap-recovery-plan-20260506.md](system/indexes/ordinary-user-karpathy-gap-recovery-plan-20260506.md)
2. [scripts/query.py](scripts/query.py)
3. [scripts/app.py](scripts/app.py)
4. [scripts/test_query.py](scripts/test_query.py)
5. [scripts/health.py](scripts/health.py)
6. [system/health-checks/health-report-20260507.md](system/health-checks/health-report-20260507.md)
7. [system/health-checks/ordinary-user-acceptance-report-20260507.md](system/health-checks/ordinary-user-acceptance-report-20260507.md)

## Do Not Do

- Do not restart broad content thickening.
- Do not treat the current win as "done". It is not.
- Do not build a one-off sample runner unless the same sample class keeps recurring.
- Do not move the problem back into memo-writing.
- Do not lose the new trust block and overview routing while polishing other areas.

## One Line

The vault now answers broad reader questions better and the overview path is much cheaper. The latest durable ordinary-user report is route-only pass; the next step is to stabilize OpenRouter auth and rerun the full live suite after the provenance sanitizer changes.
