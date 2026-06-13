---
id: streamlit-openrouter-budget-guard-investigation-20260522
type: health-check
topic: operating-system
question_type: investigation
language: bilingual
last_compiled_at: 2026-05-22
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Streamlit OpenRouter Budget Guard Investigation, 2026-05-22

## Classification

This was a `debug / investigation`, not a content or idea task.

The reported symptom: in the Ask the Vault Streamlit page, after selecting a module/condition, both example and non-example questions returned the same setup error.

## Root Cause

The screenshot error is caused by missing OpenRouter budget guard configuration:

- `OPENROUTER_DAILY_BUDGET_USD` was not present in the running Streamlit process
- the app correctly blocked live OpenRouter calls before query execution
- therefore all questions failed the same way, regardless of selected disease/module

This was not a disease-router or source-search failure.

## Manual Samples

Three real OpenRouter samples were run after setting the budget guard:

| Sample | Command shape | Result |
|---|---|---|
| CKD non-example | `scripts/query.py '关于CKD的临床终点' --backend openrouter --disease ckd --max-hops 1` | routed to `ROUTER_DISEASE=ckd`, `ROUTER_QTYPE=endpoints`, loaded `topics/ckd/endpoint-handbook.md` and CKD source cards |
| FIP example | `scripts/query.py 'FIP怎么识别' --backend openrouter --disease fip --max-hops 1` | routed to `ROUTER_DISEASE=fip`, `ROUTER_QTYPE=recognition`, loaded `topics/fip/risk-and-recognition.md` and FIP source cards |
| HCM non-example | `scripts/query.py 'HCM为什么会突然危险' --backend openrouter --disease hcm --max-hops 1` | routed to `ROUTER_DISEASE=hcm`, `ROUTER_QTYPE=overview`, loaded HCM topic pages and `src-hcm-024` |

## Fix

[scripts/app.py](../../scripts/app.py) now mirrors supported Streamlit secrets into `os.environ` before importing the query layer:

- `ANTHROPIC_API_KEY`
- `OPENROUTER_API_KEY`
- `OPENROUTER_DAILY_BUDGET_USD`
- `OPENROUTER_MODEL`
- `ENABLE_OLLAMA`

This lets hosted Streamlit deployments use Streamlit secrets while preserving the same query-layer budget guard used by local shell runs.

[scripts/check_openrouter_budget_guard.py](../../scripts/check_openrouter_budget_guard.py) now preflights the same OpenRouter config without making an API call.

## Operator Action

For hosted Streamlit, set these app secrets and redeploy/restart:

```toml
OPENROUTER_API_KEY = "sk-or-..."
OPENROUTER_DAILY_BUDGET_USD = "1.00"
OPENROUTER_MODEL = "openai/gpt-4.1-mini"
```

For local Streamlit, use:

```bash
OPENROUTER_API_KEY=<key> scripts/run_test_page.sh
```

Before restarting, verify config with:

```bash
OPENROUTER_API_KEY=<key> OPENROUTER_DAILY_BUDGET_USD=1.00 python scripts/check_openrouter_budget_guard.py
```

## Boundary

If the same setup error appears after this change, first verify that the running process has been restarted after setting secrets/env vars. Do not debug disease routing until the sidebar says the OpenRouter key and project daily budget guard are loaded.
