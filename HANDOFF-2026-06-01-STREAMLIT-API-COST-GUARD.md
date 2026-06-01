---
id: handoff-2026-06-01-streamlit-api-cost-guard
type: handoff
topic: streamlit-app
language: en
last_compiled_at: 2026-06-01
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Streamlit API Cost Guard Handoff, 2026-06-01

## Current Branch

- Branch: `idea-chatacademia-research-workbench`
- Base commit at session start: `edbe864 feat(cancer): upgrade Tulsa registry and update branch pages`
- Remote: `origin https://github.com/ethanyin89/feline-research-os.git`
- `main` and `origin/main` currently point at `edbe864`.

## User Problem

The user tested simple Chinese inquiries such as:

- `猫肥胖症siRNA药效评价`
- `猫肥胖症siRNA`

The app answered in English and spent OpenRouter API cost even though the result was basically a vault-search/gap answer. The user asked why API should be used and requested debugging plus updating the public Streamlit app:

`https://feline-research-os-3fzhk6zhd2mgvj8rxlbvou.streamlit.app/`

## Changes Made

### `scripts/query.py`

- Added CJK language detection with `prefers_chinese(question)`.
- API synthesis prompt now says to answer in the user's language.
- Added obesity and cancer disease inference patterns.
- Added local no-API query path:
  - `local_search_terms`
  - `aggregate_vault_search`
  - `source_card_disease_matches`
  - `run_local_query_core`
- `run_local_query_core`:
  - does not call Anthropic/OpenRouter/Ollama
  - searches local raw source cards and topic pages
  - returns `answer_mode: local_search`
  - uses `hops_used: 0`
  - records Research trace entries containing `api_calls=0`
  - answers Chinese questions in Chinese
  - correctly treats `obesity + siRNA` as a missing direct-evidence gap instead of fabricating drug-efficacy conclusions

### `scripts/app.py`

- Added `Vault Search (free)` as the default answer engine.
- Changed fresh app loads from API-first to local-search-first.
- Preserves Anthropic/OpenRouter/Ollama as explicit choices.
- Added Streamlit secrets mirroring into `os.environ` before importing `query.py`.
- Added Research trace renderer and persisted trace in chat history/session state.
- Added `Obesity` and `Cancer` to the condition selector.
- Added paid API lock:
  - When `Anthropic (API)` or `OpenRouter (API)` is selected, user must tick `Allow paid API synthesis for this session`.
  - If not ticked, `run_query()` stops before `make_client()` / `run_query_core()`.
  - This prevents stale browser state such as `?backend=openrouter` from silently spending tokens.

### `README.md`

- Documented Streamlit secrets for OpenRouter.
- Documented default `Vault Search (free)`.
- Documented paid API confirmation checkbox.
- Documented `api_calls=0` in Research trace for free local-search mode.

## Local Verification Completed

Commands passed:

```bash
python3 -m py_compile scripts/app.py scripts/query.py scripts/health.py
python3 scripts/health.py
```

Health report path:

```text
system/health-checks/health-report-20260601.md
```

Health summary:

- Query tests: PASS, 107/107
- Source schema: PASS
- Source refs: PASS
- Reader page source_ids: PASS
- High-visibility language QA: PASS
- Decision-grade gate: PASS
- Only expected warning remains: `Thin source usage`.

Local smoke test:

```bash
.venv/bin/python -m streamlit run scripts/app.py --server.headless true --server.port 8505
curl -s -I http://localhost:8505
```

Result:

- Streamlit returned `HTTP/1.1 200 OK`.
- Local text inspection showed default `Answer engine` is `Vault Search (free)`.
- Local text inspection showed app status `engine no API`.
- Switching to `OpenRouter (API)` displayed:
  - `Allow paid API synthesis for this session`
  - `Paid API synthesis is locked. Use Vault Search for free lookup, or tick the checkbox above to spend tokens intentionally.`
- Because local test server lacked `OPENROUTER_DAILY_BUDGET_USD`, it also correctly warned that the budget guard was missing.

Direct no-API function test:

```bash
python3 - <<'PY'
from pathlib import Path
from scripts.query import build_source_index, build_source_weights, run_local_query_core
root=Path('.')
idx=build_source_index(root)
weights=build_source_weights(root)
for q in ['猫肥胖症siRNA药效评价', 'feline obesity siRNA efficacy evaluation']:
    res=run_local_query_core(q, root, idx, source_weights=weights)
    print(q, res['disease'], res['hops_used'], res['loaded_source_ids'][:4])
    print(res['answer'].split('\n', 1)[0])
    print([x['detail'] for x in res['research_trace'] if 'api_calls' in x['detail']])
PY
```

Observed:

- Chinese question returned Chinese answer.
- `disease=obesity`.
- `hops_used=0`.
- Research trace included `api_calls=0`.
- It did not claim siRNA efficacy evidence exists.

## Important Caveat

The worktree contains many unrelated existing changes and untracked files from cancer extraction, public-test work, and previous sessions. Do not blindly commit the whole tree if the goal is only to deploy the API-cost guard.

Relevant minimal files for the API-cost guard deployment:

- `scripts/app.py`
- `scripts/query.py`
- `README.md`

Potentially relevant but not required for the Streamlit behavior:

- `system/health-checks/health-report-20260601.md` is generated and currently untracked.

## Deployment State

Not deployed yet in this handoff.

Need to update:

`https://feline-research-os-3fzhk6zhd2mgvj8rxlbvou.streamlit.app/`

Likely deployment path:

1. Determine whether Streamlit Cloud watches `main` or this feature branch. The repo default branch could not be checked via `gh repo view` under sandbox because GitHub API access hit a local proxy permission error.
2. If Streamlit watches `main`, commit the minimal API-cost guard files and push to `origin main`, or merge/cherry-pick only those files into `main` first.
3. If Streamlit watches `idea-chatacademia-research-workbench`, push this branch.
4. After deploy, open the public app and verify:
   - default engine is `Vault Search (free)`
   - app status says `engine no API`
   - `猫肥胖症siRNA` in free mode returns Chinese local-search/gap answer with Research trace `api_calls=0`
   - selecting `OpenRouter (API)` shows the paid API checkbox
   - without checking the box, a submitted query is blocked before any API call

## Suggested Next Commands

Inspect minimal diff:

```bash
git diff -- scripts/app.py scripts/query.py README.md
```

Commit only deployment files:

```bash
git add scripts/app.py scripts/query.py README.md
git commit -m "fix(streamlit): default to free vault search and gate paid APIs"
```

Push the branch that Streamlit watches:

```bash
git push origin HEAD
```

If Streamlit watches `main`, use a clean path to bring only these files to `main`; avoid including unrelated source-card/cancer extraction changes unless the user explicitly wants that broader update deployed.

## Last Local Server

The last local Streamlit smoke-test server was started on port `8505`. If still running, stop it:

```bash
lsof -ti tcp:8505
kill <pid>
```

