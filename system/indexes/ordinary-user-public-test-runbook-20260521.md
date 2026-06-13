---
id: ordinary-user-public-test-runbook-20260521
type: system
topic: operating-system
question_type: runbook
language: bilingual
last_compiled_at: 2026-05-22
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Ordinary User Public Test Runbook, 2026-05-21

## What This Is / 这是什么

**EN**  
This runbook exists for one repeated job, taking the ordinary-user test page and making it reachable through a temporary public link for real testers.

**ZH**  
这份 runbook 只管一件会重复的事，把普通用户测试页面，通过临时公网链接交给真实测试者。

Current working path:

- plain HTTP app: [scripts/public_test_app.py](../../scripts/public_test_app.py)

Do not use the Streamlit quick-tunnel path as the default public handoff unless browser QA reaches `CONNECTED`.

The HTTP app must preserve the ordinary-user presentation shape of the Streamlit app: sidebar controls, main research header, example prompts, bottom chat input, read path, trust block, provenance badges, and source titles.

## When To Use It / 什么时候用

Use it when:

- you need a fresh test port
- you need a temporary public URL for non-maintainers
- you need to verify the public page still answers `/health`
- you need to write a short test-session record for the next person

不要在这里做这些事：

- 不要把判断型问题自动化成 cron
- 不要为了起页而改内容 truth
- 不要把一次报错直接升级成新方案

## Preconditions / 前提

1. `OPENROUTER_DAILY_BUDGET_USD=1.00`
2. `OPENROUTER_MODEL=openai/gpt-4.1-mini`
3. `cloudflared` binary is available at `/tmp/cloudflared-bin/cloudflared`
4. `scripts/public_test_app.py` exists in the repo

If the current port is busy, pick a new one. The recent live samples used:

- `8510`
- `8512`

## Standard Workflow / 标准流程

### 1. Start the HTTP page

Pick a free port and start the app:

```bash
OPENROUTER_DAILY_BUDGET_USD=1.00 OPENROUTER_MODEL=openai/gpt-4.1-mini .venv/bin/python scripts/public_test_app.py --host 127.0.0.1 --port 8510
```

If that port is busy, try another free port and keep the budget guard in the same shell.

### 2. Verify local health

Check the local page first:

```bash
curl -sS --max-time 10 http://127.0.0.1:8510/health
curl -sS --max-time 20 http://127.0.0.1:8510/ | rg -n "Feline Research OS|Answer engine|Condition|Advanced settings|Find by keyword|Research Chat|Ask the vault|chat-form"
```

You want `ok` and visible matches for the old-app presentation structure.

### 3. Create a temporary tunnel

```bash
/tmp/cloudflared-bin/cloudflared tunnel --url http://127.0.0.1:8510
```

Copy the `trycloudflare.com` URL that it prints.

### 4. Verify the public link

Preferred:

```bash
bash scripts/check_public_test_page.sh https://YOUR-TUNNEL.trycloudflare.com
```

Manual equivalent:

```bash
curl -sS --max-time 15 https://YOUR-TUNNEL.trycloudflare.com/health
curl -sS --max-time 20 https://YOUR-TUNNEL.trycloudflare.com/ | rg -n "Feline Research OS|Answer engine|Condition|Advanced settings|Find by keyword|Research Chat|Ask the vault|chat-form"
curl -sS --max-time 180 -X POST --data-urlencode 'question=FIP怎么识别' --data-urlencode 'disease=auto' --data-urlencode 'max_hops=2' https://YOUR-TUNNEL.trycloudflare.com/ask | rg -n "chat-message user|answer-card|Confidence:|Sources|fip|recognition|Read path"
```

You want `ok`, the expected presentation structure, and one real answer with trust/source rendering.

### 5. Hand the link to a tester

Give them the public URL and these six prompts:

1. `解释CKD`
2. `FIP怎么识别`
3. `HCM是什么，为什么危险`
4. `IBD和淋巴瘤怎么区分`
5. `糖尿病猫为什么会缓解`
6. `我的猫肌酐升高，这个库能告诉我什么`

### 6. Write the session record

Create or update a file under `system/health-checks/` with:

- the public URL
- local fallback
- same-Wi-Fi fallback if known
- the health checks
- the six prompts
- what the tester said
- the current repeat-work boundary

## What Good Looks Like / 结果应该长什么样

- ordinary users can open the URL without repo access
- the page shows the normal Ask the Vault surface, not a budget warning
- the health endpoint returns `ok`
- public HTML includes the old-app surfaces: Answer engine, Condition, Advanced settings, Find by keyword, Research Chat, Ask the vault, and bottom chat form
- a real POST returns an answer card with read path, confidence/trust block, provenance badges, and source titles
- the session record points the next person to the current live URL

## Known Issue / 已知问题

Quick Cloudflare tunnels created during this session reached `HTTP/2 200` and `/_stcore/health = ok`, but browser QA on the public URL stayed at Streamlit `CONNECTING`. The same app reached `CONNECTED` on `http://127.0.0.1:8504`.

Until the public browser state reaches `CONNECTED`, treat the Streamlit quick tunnel as unstable for ordinary-user handoff.

Account-less Cloudflare quick tunnel URLs can expire quickly. If curl starts returning DNS failures or tunnel logs show `Unauthorized: Tunnel not found`, recreate the tunnel and update the handoff URL. Do not treat a dead tunnel as a content or rendering bug.

## Streamlit Fallback / Streamlit 分支

Use Streamlit only for local testing or if browser QA confirms the public quick tunnel reaches Streamlit `CONNECTED`:

```bash
OPENROUTER_API_KEY=<key> OPENROUTER_DAILY_BUDGET_USD=1.00 .venv/bin/python scripts/check_openrouter_budget_guard.py
PORT=8504 OPENROUTER_DAILY_BUDGET_USD=1.00 ./scripts/run_test_page.sh
```

Do not hand a Streamlit public URL to ordinary users based only on `HTTP 200` or `/_stcore/health = ok`.

If hosted Streamlit shows the setup error for every module/question, set `OPENROUTER_API_KEY`, `OPENROUTER_DAILY_BUDGET_USD`, and `OPENROUTER_MODEL` in Streamlit secrets, redeploy/restart, and rerun the preflight before debugging disease routing.

## What Not To Do / 不要做什么

- don't start cron for this workflow yet; quick tunnel URLs are temporary and should be supervised unless a named tunnel is configured
- don't auto-promote judgment-heavy UI state
- don't overwrite older public-test notes without keeping the date-specific record
- don't treat a dead tunnel as a content problem

## Sample Boundary / 样本边界

This runbook is justified by 3 real public-link samples:

1. 2026-05-19
2. 2026-05-20
3. 2026-05-21

This workflow has now been promoted into [.claude/skills/ordinary-user-public-test.md](../../.claude/skills/ordinary-user-public-test.md). Cron still does not belong here unless a named tunnel or durable deploy target is configured.

## One Line

Start the HTTP page, tunnel it, verify health plus presentation plus one real answer, hand the URL to a tester, and write the session record.
