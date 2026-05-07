# Handoff Document — 2026-04-24 Session

**Created by:** Codex (GPT-5)
**Timestamp:** 2026-04-24 Asia/Shanghai
**Purpose:** Give the next model one self-contained read of the current project reality.

---

## Read This First

If this document conflicts with old notes, trust the filesystem and these current surfaces first:

1. `system/health-checks/health-report-20260424.md`
2. `system/indexes/ask-the-vault-openrouter-runtime-playbook-20260424.md`
3. `topics/*/current-state-dashboard.md`
4. `system/indexes/*source-index*.md`

This repo is **not a git repository**. `git` commands fail here.

---

## Session Summary

This session had two real tracks:

1. **Ordinary-user Ask-the-vault runtime path**
2. **Content-side disease module continuation, especially FCV**

The backend path is now usable enough for local testing, and the FCV module is no longer bootstrap-empty.

---

## What Was Completed

### 1. Ask-the-vault runtime path was stabilized enough to test

What changed:

- OpenRouter error handling no longer falls through into low-level `NoneType` parser crashes.
- The runtime behavior was codified into a repo asset instead of staying as transient debugging context:
  - `system/indexes/ask-the-vault-openrouter-runtime-playbook-20260424.md`
- The stable default OpenRouter read is now:
  - `.venv` Streamlit
  - `OPENROUTER_DAILY_BUDGET_USD=1.00`
  - `OPENROUTER_MODEL=openai/gpt-4.1-mini`

What was learned from real API testing:

- Missing key handling is correct and should block early.
- `openai/gpt-5-mini` on the current OpenRouter chat-completions path returned `finish_reason='length'` with `message.content=None`.
- `openai/gpt-4.1-mini` can complete the same page flow and produce a real answer.

Important caveat:

- The backend path is working, but the **ordinary-user output surface still needs polish**:
  - provenance tags are too internal
  - footer language is too repo-facing
  - answer formatting is still more research-note than product-grade

Do **not** go back to real API testing unless the user asks. The latest user instruction was to stop there and continue content work.

### 2. Evidence-family / claim-fit policy was formalized

This used to be an implicit problem. It is now explicit repo policy:

- `system/indexes/source-hierarchy-and-claim-fit-policy.md`

This policy distinguishes source families such as:

- regulation / label / official guidance
- guideline / consensus
- review / synthesis review
- original study
- case series / case report
- commentary / promo / marketing

The important rule is that every source family now has:

- strongest safe use
- what it must not control
- whether it acts as anchor / support / context

This matters because future disease modules should **not** treat 24 user-provided links as flat peers.

### 3. FCV module was brought into the same fixed disease workflow

The FCV seed corpus is fully wired into the repo:

- `raw/papers/src-fcv-001.md` to `src-fcv-024.md`
- source index
- reading plan
- source depth map
- topic entry pages
- owner memos

Current FCV deep-extracted anchors are now **10**:

1. `src-fcv-001` modern shell review
2. `src-fcv-003` neutralisation breadth
3. `src-fcv-004` guideline/control
4. `src-fcv-006` field recognition
5. `src-fcv-011` challenge protection
6. `src-fcv-015` mechanism spine
7. `src-fcv-017` persistence-control
8. `src-fcv-020` enteric extension
9. `src-fcv-021` ocular extension
10. `src-fcv-022` cellular immunity

Key FCV owner surfaces:

- `topics/fcv/current-state-dashboard.md`
- `topics/fcv/risk-and-recognition.md`
- `system/indexes/fcv-source-index.md`
- `system/indexes/fcv-source-depth-map.md`
- `system/indexes/fcv-mechanism-control-memo.md`
- `system/indexes/fcv-recognition-architecture-memo.md`
- `system/indexes/fcv-vaccine-persistence-boundary-memo.md`

The FCV module should currently be read as:

- review/guideline anchors control shell
- original studies control branch detail
- commentary stays context-only
- do not flatten breadth, challenge protection, cellular immunity, and carrier-state control into one vaccine-success bucket

### 4. Health/test state was rerun after the latest FCV write-back

Current verification results:

- `python3 scripts/check_markdown_links.py` → PASS, `708` markdown files
- `python3 scripts/test_query.py` → PASS, `79/79`
- `python3 scripts/health.py` → wrote updated `system/health-checks/health-report-20260424.md`

---

## Current Ground Truth

### Health Summary

From `system/health-checks/health-report-20260424.md`:

| Check | Status |
|---|---|
| Markdown links | PASS |
| Query tests | PASS |
| Paper source cards | PASS |
| Regulation source cards | PASS |
| Thin source usage | PASS |
| High-visibility language QA | PASS |
| Acceptance report | WARN |
| API keys | WARN |
| Low-word paper cards | FAIL |

Current warnings/failures:

1. **Acceptance report is still blocked**
   - `OPENROUTER_API_KEY` missing in current shell
2. **API keys absent in current shell**
3. **Two paper cards are below 700 words**
   - health flags this as `Low-word paper cards: FAIL`

### Source Card Reality

Current disease-level reality:

| Disease | Cards | extraction_depth | verification_status |
|---|---:|---|---|
| CKD | 24 | full: 24 | deep_extracted: 24 |
| FIP | 24 | full: 24 | deep_extracted: 24 |
| HCM | 24 | full: 24 | deep_extracted: 23, source_checked: 1 |
| IBD | 24 | full: 24 | deep_extracted: 23, source_checked: 1 |
| Diabetes | 24 | full: 24 | deep_extracted: 24 |
| FCV | 24 | full: 10, partial: 14 | deep_extracted: 10, source_checked: 14 |

### Compile Reality

- `Compile trigger`: `120 changed source cards, 335 downstream files`

This is a system-state fact, not a fresh failure introduced by the latest FCV patch.

---

## Most Important Repo Assets Added or Updated

### Runtime / ask-the-vault

- `system/indexes/ask-the-vault-openrouter-runtime-playbook-20260424.md`
- `system/indexes/ordinary-user-usage-guide-bilingual.md`
- `system/indexes/ask-the-vault-day-1-runbook-20260416.md`
- `scripts/query.py`
- `scripts/test_query.py`
- `scripts/app.py`

### System policy

- `system/indexes/source-hierarchy-and-claim-fit-policy.md`
- `system/schemas/source-schema.md`
- `system/indexes/compile-checklist.md`
- `system/indexes/disease-module-bootstrap-workflow.md`

### FCV

- `system/indexes/fcv-source-index.md`
- `system/indexes/fcv-reading-plan-round-1.md`
- `system/indexes/fcv-source-depth-map.md`
- `topics/fcv/index.md`
- `topics/fcv/navigation.md`
- `topics/fcv/current-state-dashboard.md`
- `topics/fcv/mechanism-overview.md`
- `topics/fcv/risk-and-recognition.md`
- `topics/fcv/endpoint-handbook.md`
- `topics/fcv/translation-brief.md`
- `topics/fcv/regulatory-brief.md`

Deep-extraction worksheets added this session window:

- `system/indexes/src-fcv-001-deep-extraction-round1.md`
- `system/indexes/src-fcv-003-deep-extraction-round1.md`
- `system/indexes/src-fcv-011-deep-extraction-round1.md`
- `system/indexes/src-fcv-020-deep-extraction-round1.md`
- `system/indexes/src-fcv-021-deep-extraction-round1.md`

Plus existing earlier FCV deep-extraction anchors already integrated:

- `system/indexes/src-fcv-004-deep-extraction-round1.md`
- `system/indexes/src-fcv-006-deep-extraction-round1.md`
- `system/indexes/src-fcv-015-deep-extraction-round1.md`
- `system/indexes/src-fcv-017-deep-extraction-round1.md`
- `system/indexes/src-fcv-022-deep-extraction-round1.md`

---

## Current Operating Rules That Matter

These were reinforced by the user during the session and should be honored by the next model:

1. **Repeated workflow should continue without repeated confirmation**
   - especially disease content execution
2. **`$autoplan` is being used as a routing cue**
   - usually classify the request as one of:
     - 想法
     - 方案
     - 检查
     - 排查
   - then proceed
3. **For the current phase, content work is the default priority**
   - not more live API testing
4. **When runtime debugging becomes reusable repo knowledge, prefer repo assets/runbooks over inventing a new skill**
5. **Do not trust stale handoff text over live files**
   - verify current reality first if there is conflict

---

## Pending / Deferred Work

### Highest-value next work

1. **Continue FCV deep extraction**
   - strongest immediate next candidates:
     - `src-fcv-002` for classic broad review compression
     - `src-fcv-014` / `src-fcv-018` for therapy branch
     - `src-fcv-005` / `src-fcv-024` for epidemiology / vaccine-failure routing

2. **Finish remaining HCM and IBD one-card gaps**
   - HCM: 1 card still `source_checked`
   - IBD: 1 card still `source_checked`

3. **Clean ordinary-user output formatting**
   - only when the user turns back to frontend/product work
   - main issues:
     - raw provenance tags
     - internal footer language
     - overly long answer formatting

### Lower-level but real backlog

4. **Resolve low-word paper cards flagged by health**
5. **Run live acceptance only when API keys are intentionally provided**
6. **Keep source-family / claim-fit language flowing into new disease source cards**

---

## Recommended Restart Paths

### If the next request is content continuation

Start from:

- `topics/fcv/current-state-dashboard.md`
- `system/indexes/fcv-source-index.md`
- `system/indexes/fcv-source-depth-map.md`

Then deep-extract the next FCV anchor and write back into:

- source card
- source depth map
- source index
- owner memo
- current-state-dashboard
- relevant branch page

### If the next request is ordinary-user/runtime

Start from:

- `system/indexes/ask-the-vault-openrouter-runtime-playbook-20260424.md`
- `scripts/query.py`
- `scripts/app.py`
- `system/health-checks/ask-the-vault-acceptance-report-20260423.md`

Stable local start command for real OpenRouter testing:

```bash
cd /Users/jiawei/Desktop/insclaude/feline-research-os
source .venv/bin/activate
export OPENROUTER_API_KEY='your-key'
export OPENROUTER_DAILY_BUDGET_USD=1.00
export OPENROUTER_MODEL='openai/gpt-4.1-mini'
python -m streamlit run scripts/app.py
```

---

## Quick Command Block

```bash
cd /Users/jiawei/Desktop/insclaude/feline-research-os
source .venv/bin/activate
python3 scripts/check_markdown_links.py
python3 scripts/test_query.py
python3 scripts/health.py
```

---

## Final Read

The project is not in a broken state. It is in a **content-heavy continuation state**:

- core 5 disease modules are largely mature
- FCV is now an active 6th module with real structure and 10 deep anchors
- Ask-the-vault backend path has been debugged enough to work, but the product surface still needs cleanup later
- the next practical move is to keep pushing content, not to reopen solved runtime debugging unless the user asks

*End of handoff. Next model: read this file first, then continue from Pending / Deferred Work or follow the newest user request.*
