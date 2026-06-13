---
id: ordinary-user-public-test-session-20260520
type: health-check
topic: operating-system
question_type: public-test
language: bilingual
last_compiled_at: 2026-05-20
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Ordinary User Public Test Session, 2026-05-20

## Test Link

Public URL:

- `https://associated-rent-resort-tap.trycloudflare.com`

Fallback URLs:

- local machine: `http://localhost:8503`
- same Wi-Fi, last known: `http://192.168.110.44:8503`

This is a temporary Cloudflare quick tunnel. It only works while both processes are running:

1. Streamlit Ask the Vault on port `8503`
2. `cloudflared tunnel --url http://127.0.0.1:8503`

## Classification

This session is a `check / public test handoff`.

It is not a new product idea, not a plan review, and not a bug investigation. The goal is to let an ordinary user open Ask the Vault and run real questions without touching the repository.

## Verification

| Check | Result |
|---|---|
| local Streamlit health | `http://127.0.0.1:8503/_stcore/health` returned `ok` |
| public tunnel health | `https://associated-rent-resort-tap.trycloudflare.com/_stcore/health` returned `ok` |
| public HTTP status | `HTTP/2 200` |
| ordinary-user live acceptance | [ordinary-user-acceptance-report-20260519](ordinary-user-acceptance-report-20260519.md), `executed/pass`, 6/6 pass-leaning |

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

Do not make clinical decisions from the app output. The app is a research navigation and synthesis surface; provenance tags and source pages remain part of the answer.

## Repeat-Work Rule

This is manual public-test-link sample `2/3-10`.

This is also live ordinary-user acceptance sample `2/3-10` for the public-link workflow.

Do not codify a new public-link skill or cron job yet. If this workflow is repeated successfully across 3-10 real test sessions, then create a durable runbook or script for:

1. starting Streamlit on an available test port
2. starting a temporary tunnel
3. verifying `/_stcore/health`
4. writing the public test session report
