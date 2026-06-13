# Handoff: Ordinary-User HTTP Public Test - 2026-05-22

This is the focused handoff for the ordinary-user public test surface.

## Task Type

This is a `check / public test handoff`.

The Streamlit public quick-tunnel path is not dependable because the app shell reaches `HTTP 200` and `/_stcore/health = ok` but browser QA stays at Streamlit `CONNECTING`. The working path is now a plain HTTP test page that avoids Streamlit websockets.

## Current Working Link

Use this public URL for ordinary-user testing:

- `https://escape-cheaper-flashing-snow.trycloudflare.com`

Fallbacks:

- local machine: `http://127.0.0.1:8510`
- same Wi-Fi: not rechecked for the HTTP page

This URL points to [scripts/public_test_app.py](scripts/public_test_app.py), not the Streamlit app.

## Verification

- local HTTP app health: `http://127.0.0.1:8510/health` returned `ok`
- local browser QA rendered the full page text
- local real POST sample `解释CKD` returned a sourced CKD answer
- public health: `https://escape-cheaper-flashing-snow.trycloudflare.com/health` returned `ok`
- public homepage structure includes the old-app surfaces: Answer engine, Condition, Advanced settings, Find by keyword, Research Chat, Ask the vault, and bottom chat form
- public real POST sample `FIP怎么识别` returned a `fip / recognition` answer with 9 source ids in about 19 seconds

## What Changed

Added:

- [scripts/public_test_app.py](scripts/public_test_app.py)
- [.claude/skills/ordinary-user-public-test.md](.claude/skills/ordinary-user-public-test.md)

It is a minimal standard-library HTTP server:

- `GET /` renders an ordinary-user question form
- `GET /health` returns `ok`
- `POST /ask` calls `run_query_core()` through OpenRouter
- page presentation now mirrors the Streamlit app structure: sidebar controls, main research header, example prompts, bottom chat input, read path, trust block, provenance badges, and source titles
- no Streamlit
- no websocket
- no frontend build step

## Why This Exists

Three Streamlit quick-tunnel attempts failed the real browser criterion:

- public HTTP and health checks passed
- static Streamlit shell loaded
- browser state stayed `CONNECTING`
- local Streamlit on the same port reached `CONNECTED`

That makes Streamlit quick tunnels a false-positive availability check for this workflow. The HTTP page is not implemented with Streamlit components, but its public presentation now follows the Streamlit app's ordinary-user structure.

## Tool Boundary

gstack browse later failed with `No available port after 5 attempts in range 10000-60000`. Treat that as a browse-tool availability problem, not evidence that this page is broken. Current acceptance uses public `/health`, public homepage structure checks, and a real public `POST /ask` answer.

## Streamlit Budget Guard Follow-Up

The Streamlit screenshot showing every module/example question failing was traced to missing `OPENROUTER_DAILY_BUDGET_USD` in the running Streamlit process, not to disease routing. Three direct OpenRouter samples with explicit `--disease` were successful:

- CKD non-example: `ROUTER_DISEASE=ckd`, `ROUTER_QTYPE=endpoints`
- FIP example: `ROUTER_DISEASE=fip`, `ROUTER_QTYPE=recognition`
- HCM non-example: `ROUTER_DISEASE=hcm`, `ROUTER_QTYPE=overview`

[scripts/app.py](scripts/app.py) now mirrors Streamlit secrets into `os.environ` before importing the query layer, [.streamlit/secrets.example.toml](.streamlit/secrets.example.toml) documents the hosted deploy keys, and [scripts/check_openrouter_budget_guard.py](scripts/check_openrouter_budget_guard.py) preflights OpenRouter config without making an API call. A temporary Streamlit run on port `8513` with the budget guard returned `/_stcore/health = ok`.

## Tester Prompts

Use these exact prompts first:

1. `解释CKD`
2. `FIP怎么识别`
3. `HCM是什么，为什么危险`
4. `IBD和淋巴瘤怎么区分`
5. `糖尿病猫为什么会缓解`
6. `我的猫肌酐升高，这个库能告诉我什么`

## Next Work

1. Keep the HTTP public URL available while the server and tunnel processes stay alive.
2. Do not hand out Streamlit quick-tunnel links unless browser QA reaches `CONNECTED`.
3. For repeated public-link work, use `.claude/skills/ordinary-user-public-test.md` first.
4. If the Streamlit app shows a setup error for every module/question, run `scripts/check_openrouter_budget_guard.py` before debugging disease routing.
5. If this HTTP page is used again, update the runbook and consider turning it into the durable ordinary-user public test path.

## Files To Read First

1. [scripts/public_test_app.py](scripts/public_test_app.py)
2. [.claude/skills/ordinary-user-public-test.md](.claude/skills/ordinary-user-public-test.md)
3. [scripts/check_openrouter_budget_guard.py](scripts/check_openrouter_budget_guard.py)
4. [system/health-checks/streamlit-openrouter-budget-guard-investigation-20260522.md](system/health-checks/streamlit-openrouter-budget-guard-investigation-20260522.md)
5. [system/health-checks/ordinary-user-public-http-test-session-20260522.md](system/health-checks/ordinary-user-public-http-test-session-20260522.md)
6. [system/indexes/ordinary-user-public-test-runbook-20260521.md](system/indexes/ordinary-user-public-test-runbook-20260521.md)
7. [HANDOFF-2026-05-21-ORDINARY-USER-PUBLIC-TEST.md](HANDOFF-2026-05-21-ORDINARY-USER-PUBLIC-TEST.md)

## One Line

The current working public ordinary-user test link is the plain HTTP app at `https://escape-cheaper-flashing-snow.trycloudflare.com`; Streamlit quick tunnels remain unstable, and account-less Cloudflare quick tunnel URLs can expire.
