---
id: ordinary-user-vault-sample-run-20260601
type: health-check
topic: streamlit-app
question_type: ordinary-user-eval
language: bilingual
last_compiled_at: 2026-06-01
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Ordinary User Vault Sample Run, 2026-06-01

## Classification

This task is a **check + investigation** problem.

It is not just an idea problem: the product already exists and the user has live failure evidence.
It is not just a plan problem: the app must be tested against ordinary-user questions.
It is not just a code bug: the main failure is that a normal person experiences the vault as a hit-list machine instead of an answer surface.

## Rule From User

Do not do a one-off fix. If this will recur, first run 3-10 manual samples. Only after the sample standard is approved should it become a skill file. If it needs automatic execution, add scheduling separately.

## Manual Sample Set

The first manual run used six ordinary-user prompts:

| Prompt | Expected user job |
|---|---|
| `解释CKD` | broad disease starter explanation |
| `FIP怎么识别` | recognition/diagnostic-boundary starter |
| `HCM是什么，为什么危险` | disease explanation plus risk framing |
| `IBD和淋巴瘤怎么区分` | practical differential-boundary answer |
| `猫肥胖症siRNA` | no-direct-evidence gap answer without fabrication |
| `What endpoints are usable for feline CKD efficacy evaluation?` | endpoint starter answer |

## Initial Failure Pattern

Before the fix:

- `解释CKD`: usable local explanation after the first CKD-specific patch.
- `FIP怎么识别`: failed, returned topic-page hit list.
- `HCM是什么，为什么危险`: failed, returned topic-page hit list while metadata misleadingly said `local_explanation`.
- `IBD和淋巴瘤怎么区分`: failed, routed to `cancer` because lymphoma overrode IBD.
- `猫肥胖症siRNA`: passed as a gap answer, with no direct-evidence claim.
- `What endpoints are usable for feline CKD efficacy evaluation?`: failed, returned hit list instead of endpoint explanation.

## Fix Implemented

Added deterministic free-mode answer surfaces in `scripts/app.py`:

- `ckd_overview`
- `ckd_endpoint`
- `fip_recognition`
- `hcm_overview`
- `ibd_lymphoma`

Also fixed IBD-vs-lymphoma disease inference so `IBD和淋巴瘤怎么区分` routes to `ibd`, not `cancer`.

These surfaces do not call APIs. They reuse compiled vault claims and source IDs only.

## Repeatable Check

Created:

```bash
.venv/bin/python scripts/ordinary_user_vault_eval.py
```

The script checks:

- expected disease routing
- expected answer mode
- expected answer surface
- `api_calls=0`
- minimum loaded source IDs
- at least 3 visible answer sections
- no hit-list-only answer for ordinary-user explanation prompts

## Current Result

All six samples pass locally after the fix.

The sample standard should be reviewed before turning this into a formal skill file or scheduled check.
