---
id: ordinary-user-public-test-session-20260521
type: health-check
topic: operating-system
question_type: public-test
language: bilingual
last_compiled_at: 2026-05-21
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Ordinary User Public Test Session, 2026-05-21

## Test Link

Public URL:

- `https://pulled-would-excellent-sorted.trycloudflare.com`

Fallback URLs:

- local machine: `http://localhost:8504`
- same Wi-Fi: `http://192.168.77.32:8504`

This is a temporary Cloudflare quick tunnel. It only works while both processes are running:

1. Streamlit Ask the Vault on port `8504`
2. `cloudflared tunnel --url http://127.0.0.1:8504`

## Classification

This session is a `check / public test handoff`.

It is not a new product idea, not a plan review, and not a bug investigation. The goal is to let an ordinary user open Ask the Vault and run real questions without touching the repository.

## Verification

| Check | Result |
|---|---|
| local Streamlit health | `http://127.0.0.1:8504/_stcore/health` returned `ok` |
| local browser state | Streamlit app reached `CONNECTED` in Chrome |
| same-Wi-Fi health | `http://192.168.77.32:8504/_stcore/health` returned `ok` |
| public tunnel health | `https://pulled-would-excellent-sorted.trycloudflare.com/_stcore/health` returned `ok` |
| public HTTP status | `HTTP/2 200` |
| ordinary-user live acceptance | [ordinary-user-acceptance-report-20260519](ordinary-user-acceptance-report-20260519.md), `executed/pass`, 6/6 pass-leaning |
| public browser state | quick tunnels stayed at `CONNECTING` in Chrome, including `quic` and `http2` variants |

## Suggested Tester Tasks

Ask these exact questions first:

1. `解释CKD`
2. `FIP怎么识别`
3. `HCM是什么，为什么危险`
4. `IBD和淋巴瘤怎么区分`
5. `糖尿病猫为什么会缓解`
6. `我的猫肌酐升高，这个库能告诉我什么`

The acceptance runner has verified that these six prompts execute through the OpenRouter backend and return pass-leaning answers with real source ids. Human testers should still judge readability, trust, and whether the answer gives a useful next step.

## What Testers Should Report

Ask testers for:

- which question they asked
- whether the answer was understandable on first read
- whether evidence/provenance felt visible enough
- whether they knew what to do next
- any confusing UI text, missing loading state, or broken interaction

## Current Boundary

This public URL is for testing only. Do not treat it as production hosting.

Current note: the local app is healthy, but the public quick-tunnel path is not hydrating in browser QA. Do not hand the public URL to an ordinary user as a dependable surface yet.

Do not make clinical decisions from the app output. The app is a research navigation and synthesis surface; provenance tags and source pages remain part of the answer.

## Repeat-Work Rule

This is manual public-test-link sample `3/3-10`.

This is also live ordinary-user acceptance sample `3/3-10` for the public-link workflow.

This is now the threshold where a durable runbook or skill file is justified after approval. Do not codify judgment-heavy promotion into cron.

## Next Durable Step

Create a reusable runbook for:

1. starting Streamlit on an available test port
2. starting a temporary tunnel
3. verifying `/_stcore/health`
4. writing the public test session report

## One Line

The public test surface is back online on a fresh tunnel, and this is the third real sample, so the workflow is now ready for codification after approval.
