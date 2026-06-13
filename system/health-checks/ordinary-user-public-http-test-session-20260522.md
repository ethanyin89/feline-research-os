---
id: ordinary-user-public-http-test-session-20260522
type: health-check
topic: operating-system
question_type: public-test
language: bilingual
last_compiled_at: 2026-05-22
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Ordinary User Public HTTP Test Session, 2026-05-22

## Test Link

Public URL:

- `https://escape-cheaper-flashing-snow.trycloudflare.com`

Fallback URL:

- local machine: `http://127.0.0.1:8510`

This page is served by [scripts/public_test_app.py](../../scripts/public_test_app.py). It is not Streamlit and does not use websockets.

## Classification

This session is a `check / public test handoff`.

The goal is to give ordinary users a public page that actually renders and submits questions. The previous Streamlit quick-tunnel path passed health checks but did not hydrate in browser QA.

## Verification

| Check | Result |
|---|---|
| local HTTP health | `http://127.0.0.1:8510/health` returned `ok` |
| local homepage render | page includes sidebar controls, main research header, example prompts, and bottom chat form |
| local real POST | `解释CKD`, `disease=ckd`, `max_hops=2` returned a CKD answer with trust/source rendering |
| public HTTP health | `https://escape-cheaper-flashing-snow.trycloudflare.com/health` returned `ok` |
| public homepage render | page includes Answer engine, Condition, Advanced settings, Find by keyword, Research Chat, Ask the vault, and bottom chat form |
| public real POST | `FIP怎么识别`, `max_hops=2` returned `fip / recognition`, 9 source ids, about 19 seconds |
| scripted public check | `bash scripts/check_public_test_page.sh https://escape-cheaper-flashing-snow.trycloudflare.com` passed health, presentation, and real answer checks; latest real answer returned in about 18.6 seconds |

## Suggested Tester Tasks

Ask these exact questions first:

1. `解释CKD`
2. `FIP怎么识别`
3. `HCM是什么，为什么危险`
4. `IBD和淋巴瘤怎么区分`
5. `糖尿病猫为什么会缓解`
6. `我的猫肌酐升高，这个库能告诉我什么`

## Current Boundary

This public URL is for testing only. Do not treat it as production hosting. Account-less Cloudflare quick tunnel URLs can expire and may need to be recreated.

The HTTP page now mirrors the Streamlit app's presentation structure, but still avoids Streamlit/websockets because Streamlit quick tunnels stayed at `CONNECTING` in browser QA.

The repeated public verification has been codified in [scripts/check_public_test_page.sh](../../scripts/check_public_test_page.sh).

## One Line

The ordinary-user public test surface is working through the plain HTTP app at `https://escape-cheaper-flashing-snow.trycloudflare.com`.
