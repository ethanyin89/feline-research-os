# /ordinary-user-vault-eval — Free-Mode Ordinary User Vault Eval

Use this when the user asks whether Ask the vault works for normal users, whether a public/Streamlit answer is confusing, whether free mode is useful, or when changing `scripts/app.py`, `scripts/query.py`, routing, answer modes, source-card loading, or Streamlit answer rendering.

## Classification

Treat this as **check + investigation** unless there is a crash.

The target is not "does one query return something". The target is:

- ordinary person asks a natural question
- default `Vault Search (free)` does not call an API
- answer is an answer, not only a source/page hit list
- answer shows source-backed claims or an explicit gap
- research trace says `api_calls=0`

## Required First Step

Run the deterministic no-API eval:

```bash
cd /Users/jiawei/Desktop/insclaude/feline-research-os
.venv/bin/python scripts/ordinary_user_vault_eval.py
```

This is the canonical local check for the free ordinary-user answer surface.

It currently covers:

- `解释CKD`
- `FIP怎么识别`
- `HCM是什么，为什么危险`
- `IBD和淋巴瘤怎么区分`
- `猫肥胖症siRNA`
- `What endpoints are usable for feline CKD efficacy evaluation?`

## Pass Standard

All samples must pass:

- expected disease route
- expected answer mode/surface
- `api_calls=0`
- minimum loaded source IDs
- at least 3 answer sections
- no hit-list-only answer for explanation/recognition/differential/endpoint prompts

## If It Fails

Do not patch one sample blindly.

1. Classify the failure:
   - routing miss
   - hit-list-only answer
   - missing direct-evidence gap not explicit
   - API-cost guard regression
   - language mismatch
   - source-loading regression
2. Add or update the smallest deterministic answer surface in `scripts/app.py`.
3. Re-run `.venv/bin/python scripts/ordinary_user_vault_eval.py`.
4. Run `python3 scripts/health.py` and confirm the summary includes:
   - `Ordinary-user vault eval | PASS | All ordinary-user free-mode samples passed without API calls.`
5. Update `system/health-checks/ordinary-user-vault-sample-run-YYYYMMDD.md` if the sample set or standard changed.

## Public Streamlit Check

For hosted Streamlit, first verify load/default state:

```bash
/Users/jiawei/.claude/skills/gstack/browse/dist/browse chain 'goto https://feline-research-os-3fzhk6zhd2mgvj8rxlbvou.streamlit.app/~/+/ | wait [data-testid="stChatInputTextArea"] | text'
```

Must show:

- `Vault Search (free)`
- `engine no API`

Browser automation against Streamlit chat input can be flaky. If gstack can load the page but cannot submit, do not treat that alone as app failure. Use the local deterministic eval as the acceptance path, and record the browser limitation in the handoff.

## Do Not

- Do not switch default back to OpenRouter/API to get a nicer answer.
- Do not fabricate source claims to make a sample pass.
- Do not add a new disease answer surface without first adding it to the manual sample set or explaining why it is out of scope.
- Do not commit unrelated cancer extraction or health-report generated files while fixing this path.
