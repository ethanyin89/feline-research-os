# Handoff: Public Test Link Refresh - 2026-05-25

This is the focused handoff for the ordinary-user public test link after the previous Cloudflare quick tunnel expired.

## Task Type

This is a `check / public test handoff`.

The user asked to continue the ordinary-user test-page work. The first thing checked was whether the previous temporary URL was still usable.

## Current Working Link

Use this public URL for ordinary-user testing:

- `https://required-properly-bush-mileage.trycloudflare.com`

Fallback:

- local machine: `http://127.0.0.1:8510`

This URL points to [scripts/public_test_app.py](scripts/public_test_app.py), not the Streamlit app.

## What Happened Today

1. Previous public URL failed DNS:
   - `https://escape-cheaper-flashing-snow.trycloudflare.com/health`
   - failure: `Could not resolve host`
2. OpenRouter preflight still passed:
   - `OPENROUTER_API_KEY`
   - `OPENROUTER_DAILY_BUDGET_USD=1.00`
   - `OPENROUTER_MODEL=openai/gpt-4.1-mini`
3. Local HTTP app was still running:
   - `http://127.0.0.1:8510/health` returned `ok`
   - local listener PID observed: `30240`
4. No old temporary Streamlit verification service was running on `8513`.
5. A new Cloudflare quick tunnel was created:
   - `https://required-properly-bush-mileage.trycloudflare.com`
6. New public health check returned `ok`.

## Verification Status

Completed:

- local HTTP health: `ok`
- public HTTP health: `ok`
- OpenRouter budget preflight: pass

Not completed:

- `bash scripts/check_public_test_page.sh https://required-properly-bush-mileage.trycloudflare.com`

The full scripted public check was started, but the user intentionally interrupted the turn before it completed. Do not mark presentation or real-answer checks as passed for the 2026-05-25 URL until this script is rerun successfully.

## Running Processes To Keep

Keep the local HTTP app and the new Cloudflare tunnel running if the user still needs the link:

- local app: `scripts/public_test_app.py` on port `8510`
- tunnel: `cloudflared tunnel --url http://127.0.0.1:8510`

The current quick tunnel is account-less and temporary. It can expire with DNS failures or `Unauthorized: Tunnel not found`.

## Next Step

Run:

```bash
bash scripts/check_public_test_page.sh https://required-properly-bush-mileage.trycloudflare.com
```

Acceptance requires all three sections to pass:

1. `== health ==`
2. `== presentation ==`
3. `== real answer ==`

If it passes, update [system/health-checks/ordinary-user-public-http-test-session-20260522.md](system/health-checks/ordinary-user-public-http-test-session-20260522.md) or create a new 2026-05-25 health-check record.

## Files To Read First

1. [scripts/public_test_app.py](scripts/public_test_app.py)
2. [scripts/check_public_test_page.sh](scripts/check_public_test_page.sh)
3. [scripts/check_openrouter_budget_guard.py](scripts/check_openrouter_budget_guard.py)
4. [.claude/skills/ordinary-user-public-test.md](.claude/skills/ordinary-user-public-test.md)
5. [HANDOFF-2026-05-22-ORDINARY-USER-HTTP-PUBLIC-TEST.md](HANDOFF-2026-05-22-ORDINARY-USER-HTTP-PUBLIC-TEST.md)

## One Line

The previous quick tunnel expired; the current health-checked public URL is `https://required-properly-bush-mileage.trycloudflare.com`, but the full scripted presentation and real-answer check still needs to be rerun because the previous run was interrupted.
