# Handoff: Ordinary-User Public Test Link and Live Acceptance - 2026-05-20

This is the focused handoff for the next model working on the ordinary-user test surface.

## Task Type

This is a `check / public test handoff`.

The goal is not to invent a new plan. The goal is to keep the ordinary-user surface reachable, documented, and verified for real readers.

The user rule is binding:

`No one-off work. If a task will recur, first run 3-10 real samples manually, then codify it. Use cron only for deterministic automation, not judgment-heavy content promotion.`

## Current Reality

- Public test URL: `https://associated-rent-resort-tap.trycloudflare.com`
- Local fallback: `http://localhost:8503`
- Same Wi-Fi fallback, last known: `http://192.168.110.44:8503`
- Streamlit health: `ok` at `/_stcore/health`
- Public tunnel health: `HTTP/2 200`
- Streamlit process is now on port `8503`
- `cloudflared` is a temporary quick tunnel and only works while the process stays alive
- The earlier `gain-challenged-bra-offices.trycloudflare.com` tunnel died and was replaced by this new one.

## Live Acceptance Status

- Ordinary-user acceptance report: [system/health-checks/ordinary-user-acceptance-report-20260519.md](system/health-checks/ordinary-user-acceptance-report-20260519.md)
- Status: `executed/pass`
- Score: `6/6 pass-leaning answers`
- Provenance misses: `0`
- Route misses: `0`

## What Changed This Session

### Public Test Session

[system/health-checks/ordinary-user-public-test-session-20260520.md](system/health-checks/ordinary-user-public-test-session-20260520.md)

This file now records:

- the public tunnel URL
- local and same-Wi-Fi fallback URLs
- the health checks
- the six ordinary-user first-test prompts
- the current repeat-work boundary for public-link testing
- the recovered `8503` tunnel after the earlier `8502` tunnel stopped responding

### Health Report

[system/health-checks/health-report-20260521.md](system/health-checks/health-report-20260521.md)

This report now shows:

- `Ordinary-user acceptance | PASS`
- `Inbox backlog | PASS`
- `Thin source usage | PASS`
- `Obesity compiled guidance gate | PASS`

### Usage Guide

[system/indexes/ordinary-user-usage-guide-bilingual.md](system/indexes/ordinary-user-usage-guide-bilingual.md)

It now reflects:

- current disease choices including `FCV` and `Obesity`
- the fact that a temporary public test link should be opened directly by testers

## What Testers Should Use

Use these exact prompts first:

1. `解释CKD`
2. `FIP怎么识别`
3. `HCM是什么，为什么危险`
4. `IBD和淋巴瘤怎么区分`
5. `糖尿病猫为什么会缓解`
6. `我的猫肌酐升高，这个库能告诉我什么`

Ask testers to report:

- which question they asked
- whether the answer was understandable on first read
- whether evidence/provenance was visible enough
- whether they knew what to do next
- whether any UI text or loading state was confusing

## Next Work

1. Keep the public URL available while the tunnel stays alive.
2. If the user wants another round of real ordinary-user testing, use the same six prompts before changing anything.
3. Do not codify a new public-link skill or cron job yet. This workflow has only one live sample run, and the user explicitly wants repeated work proven before automation.

## Files To Read First

1. [system/health-checks/ordinary-user-public-test-session-20260520.md](system/health-checks/ordinary-user-public-test-session-20260520.md)
2. [system/health-checks/ordinary-user-acceptance-report-20260519.md](system/health-checks/ordinary-user-acceptance-report-20260519.md)
3. [system/health-checks/health-report-20260521.md](system/health-checks/health-report-20260521.md)
4. [system/indexes/ordinary-user-usage-guide-bilingual.md](system/indexes/ordinary-user-usage-guide-bilingual.md)

## One Line

The ordinary-user page is reachable by public URL again and has a live executed acceptance pass; keep it documented and available, do not over-automate it yet.
