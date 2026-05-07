---
id: system-ask-the-vault-page-test-handoff-20260423
type: handoff
topic: ask-the-vault
question_type: workflow
language: bilingual
last_compiled_at: 2026-04-23
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Ask the Vault Page-Test Handoff, 2026-04-23

This is the active handoff for the next model taking over the `Ask the vault`
live-page work.

The current task is a `check` first, then a gated `live test`.

Do **not** run a real OpenRouter / Anthropic model call until the user confirms
after the non-live page test report.

## User Instruction To Preserve

The user asked:

> 先走完完整的页面测试，之后找我确认后，再执行真实页面测试。

Interpretation:

1. Finish a full page-level test first.
2. Report results and ask the user for confirmation.
3. Only after explicit confirmation, run the real page test once.

Earlier instruction still applies:

- No fake data.
- Use real sources already in the vault.
- Normal coding / checking should use subscription tools, not paid API calls.
- Only real page acceptance may use a real API.
- For OpenRouter, both controls are required:
  - OpenRouter dashboard daily budget cap: `$1/day`.
  - Project env guard: `OPENROUTER_DAILY_BUDGET_USD=1.00` or lower.

## Repo And Runtime

Repo path:

```text
/Users/jiawei/Desktop/insclaude/feline-research-os
```

Python app:

```text
scripts/app.py
scripts/query.py
```

Streamlit entry:

```bash
.venv/bin/streamlit run scripts/app.py
```

OpenRouter run command documented in README:

```bash
OPENROUTER_API_KEY=<key> OPENROUTER_DAILY_BUDGET_USD=1.00 OPENROUTER_MODEL=openai/gpt-5-mini python -m streamlit run scripts/app.py
```

## What Changed In This Round

### 1. API Cost Guard

Project policy was added so OpenRouter cannot be used accidentally without the
local budget guard.

Important files:

- `CLAUDE.md`
- `.env.example`
- `README.md`
- `scripts/query.py`
- `scripts/app.py`
- `scripts/run_acceptance_checklist.py`
- `scripts/run_day1_acceptance.sh`
- `scripts/test_query.py`
- `system/indexes/ask-the-vault-day-1-runbook-20260416.md`

Core behavior:

- `validate_openrouter_budget()` rejects missing, non-numeric, non-positive, or
  above-`1.00` `OPENROUTER_DAILY_BUDGET_USD`.
- Streamlit blocks OpenRouter if the budget guard is absent or invalid.
- Acceptance scripts preflight the same guard before live runs.

### 2. Streamlit Error Persistence

Bug fixed in `scripts/app.py`:

- Before: a failed query rendered an error, then the bottom input always called
  `st.rerun()`, clearing the failure state.
- After: `run_query(question) -> bool`; the app reruns only after success.

This is why the UI now shows persistent failures instead of returning to a
blank state.

### 3. Error Visibility

Bug fixed in `scripts/app.py`:

- Backend exceptions now update the Streamlit status row with a short error:
  `Query failed: ...`.
- `Error details` is expanded by default.
- Common API-key shapes are redacted before display.
- Multi-line HTML notices are stripped line-by-line before `st.markdown()` so
  Streamlit does not render them as a code block.

Relevant functions:

- `render_query_error()`
- `sanitize_error_detail()`
- `query_error_label()`
- `render_notice()`

### 4. Backend Default

Bug / friction fixed in `scripts/app.py`:

- Fresh loads prefer `OpenRouter (API)` when `OPENROUTER_API_KEY` exists in the
  Streamlit process.
- If query params explicitly say `backend=anthropic`, the page still respects
  that current choice.

Reason: this project is now budget-guarded around OpenRouter for live page
acceptance.

## What Was Verified

These checks completed locally and do not call an LLM:

```bash
python3 scripts/test_query.py
```

Result:

```text
73 passed | 0 failed | 73 total
```

```bash
python3 -m py_compile scripts/app.py scripts/query.py scripts/run_acceptance_checklist.py scripts/health.py scripts/search.py
```

Result: passed.

```bash
python3 scripts/check_markdown_links.py
```

Result:

```text
PASS: checked 653 markdown files, no local link issues found.
```

```bash
python3 scripts/health.py
```

Generated:

```text
system/health-checks/health-report-20260423.md
```

Summary:

- Markdown links: PASS.
- Query tests: PASS.
- Paper source cards: PASS.
- Regulation source cards: PASS.
- Source IDs: PASS.
- Source schema/state/evidence policy checks: PASS.
- Acceptance report: WARN, blocked because current Codex shell did not have
  `OPENROUTER_API_KEY`.
- API keys: WARN, no API keys in the current shell.

## Real UI Observations From User Screenshots

### Anthropic Error

When the sidebar selected `Anthropic (API)`, the page correctly failed with:

```text
ANTHROPIC_API_KEY not set
```

This is expected because Anthropic was selected and the Streamlit process did
not have `ANTHROPIC_API_KEY`.

### OpenRouter Error

When the sidebar selected `OpenRouter (API)`, with green budget notice visible,
the real page failed with:

```text
expected string or bytes-like object, got 'NoneType'
```

This is the next unresolved issue.

Do not assume this is fake-data related. It is likely a runtime handling bug
around an OpenRouter response field being `None`, or a parser receiving `None`
where it expects text. The exact failing line was not captured before handoff.

The next model should inspect:

- `scripts/query.py` `_chat()`
- `scripts/query.py` routing / synthesis calls using `parse_json_block()`
- any code path applying `re.*` to a model response
- OpenRouter responses where `resp.choices[0].message.content` can be `None`

Likely defensive fix:

- Treat `None` model content as an explicit backend error with a clear message,
  not as input to regex parsing.
- Preserve the raw non-secret response shape in error details if possible.

## Page Test Status

Full browser page test is **not complete**.

What happened:

1. Code-level checks completed.
2. A local Streamlit instance was started on:

   ```text
   http://127.0.0.1:8503
   ```

   Environment used for this non-live page test:

   ```bash
   HOME=/tmp/feline-page-test-home
   OPENROUTER_DAILY_BUDGET_USD=1.00
   OPENROUTER_MODEL=openai/gpt-5-mini
   ```

   No real API key was provided by Codex.

3. The local server started successfully.
4. gstack browse had sandbox port issues and needed elevated execution.
5. Before the full browser walkthrough was completed, the user stopped the turn
   and requested this handoff document.
6. The temporary Streamlit test server on port `8503` was stopped. `lsof` showed
   no listener afterward.

Do not claim page QA passed. Continue it.

## Recommended Next Model Workflow

### Phase 1: Finish Non-Live Page Test

Start a local test server without real API keys:

```bash
mkdir -p /tmp/feline-page-test-home
env HOME=/tmp/feline-page-test-home OPENROUTER_DAILY_BUDGET_USD=1.00 OPENROUTER_MODEL=openai/gpt-5-mini .venv/bin/streamlit run scripts/app.py --server.port 8503 --server.address 127.0.0.1 --server.headless true --browser.gatherUsageStats false
```

If sandbox blocks local port binding, request approval and run elevated.

Browser checklist:

1. Load `http://127.0.0.1:8503`.
2. Confirm header, example questions, provenance guide, and sidebar render.
3. Confirm no console errors.
4. Confirm no failed static/network requests other than expected Streamlit
   internal noise.
5. Test `Anthropic (API)` with no Anthropic key:
   - Ask a question.
   - Expected: visible error block, expanded details, no rerun-clear.
6. Test `OpenRouter (API)` with no OpenRouter key:
   - Ask a question.
   - Expected: visible `OPENROUTER_API_KEY not set`, no API call.
7. Test OpenRouter with budget missing if possible:
   - Start without `OPENROUTER_DAILY_BUDGET_USD`.
   - Expected: budget guard blocks before query.
8. Test sidebar search:
   - Search `phosphorus` or `SDMA`.
   - Expected: real source/topic results, selected reading panel, no fake data.
9. Test responsive screenshots:
   - Desktop.
   - Mobile around `375x812`.
10. Stop the local server.

After this, report findings to the user and ask for confirmation before the
real API test.

### Phase 2: Only After User Confirms, Run One Real Page Test

Preconditions:

- User confirms to proceed.
- OpenRouter dashboard daily cap is `$1/day`.
- Streamlit process has:

  ```bash
  OPENROUTER_API_KEY=<real key>
  OPENROUTER_DAILY_BUDGET_USD=1.00
  OPENROUTER_MODEL=openai/gpt-5-mini
  ```

Real-page flow:

1. Select `OpenRouter (API)`.
2. Confirm green notice:

   ```text
   OpenRouter key loaded. Project daily budget guard: $1.00.
   ```

3. Ask exactly once:

   ```text
   IBD 的诊断排除流程是什么？
   ```

4. If it succeeds:
   - Confirm answer appears.
   - Confirm provenance tags appear.
   - Confirm cited source IDs are real local source cards.
   - Save screenshot / notes.
5. If it fails:
   - Capture the full `Error details`.
   - Do not retry repeatedly without diagnosing.

## Suggested Prompt For The Next Model

```text
You are taking over:

/Users/jiawei/Desktop/insclaude/feline-research-os

Read first:
system/indexes/ask-the-vault-page-test-handoff-20260423.md
HANDOFF.md

Task:
Finish the non-live page-level test for Ask the vault. Do not run a real
OpenRouter or Anthropic model call yet. After the non-live page test, report
findings and ask me for confirmation before the one real OpenRouter page test.

Important:
- No fake data.
- Do not create mock answer content.
- Real API only after confirmation.
- OpenRouter must have dashboard $1/day cap and project env
  OPENROUTER_DAILY_BUDGET_USD=1.00.
- The unresolved real error is:
  expected string or bytes-like object, got 'NoneType'
```

## Current One-Line State

The code-level checks pass, the page error handling is improved, but full
browser QA is not finished and the real OpenRouter path still has an unresolved
`NoneType` runtime failure.
