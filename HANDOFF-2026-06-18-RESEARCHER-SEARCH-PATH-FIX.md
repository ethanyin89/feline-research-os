# HANDOFF: Researcher Search Path Fix

Date: 2026-06-18
Branch: idea-chatacademia-research-workbench
Status: COMPLETE

## Classification

This task is **检查 + 方案落地**, not a pure visual redesign.

The user reviewed the current research search path from a researcher perspective and identified three issues:

1. after clicking search, the page scrolls directly to the bottom, which violates reading habits;
2. retrieval/query content may be English, but the output should be Chinese;
3. `ui-ux-pro-max` had been installed before and should inform visual/UX judgment.

## Product Judgment

For a researcher, the post-search path should be:

1. submit query;
2. see task classification / research contract;
3. start reading the answer from the top;
4. inspect evidence cards, methods, references, and cited-by links;
5. optionally expand trace/audit details.

Jumping directly to the bottom after the first search breaks this path because it puts the user near the input instead of at the beginning of the result.

## What Changed

### 1. Reworked first-search input flow

File: `scripts/app.py`

The first implementation removed the forced rerun after query completion:

```python
if run_query(user_question):
    st.rerun()
```

After:

```python
run_query(user_question)
```

Reason:

`run_query()` already renders the assistant answer in the current run and appends it to `st.session_state.messages`. Forcing another rerun rebuilds the chat history and can push the browser toward the bottom/chat input. Removing the rerun preserves the immediate reading path.

After browser QA, one more issue appeared: if the user clicked an example chip from the empty state, the empty-state content had already been rendered above the answer. The final fix:

- moved `st.chat_input(...)` capture before `show_empty_state` is computed;
- changed `queue_question(...)` so example chips set `pending_question` and immediately `st.rerun()`;
- bottom input handling now only processes `st.session_state.pending_question`.

This makes both typed chat input and example-chip search enter the same path: pending question first, empty state hidden, answer rendered from the top.

### 2. Decoupled research-query language from output language

File: `scripts/app.py`

Research Mode now uses `prefers_chinese(question)` for output language instead of `detect_chinese(question)`.

This means an English query such as:

```text
search the latest papers about feline HCM, prioritize high-impact journals
```

can still return a Chinese research report by default. Users can still explicitly request English with phrases like `answer in English`.

### 3. Confirmed `ui-ux-pro-max` installation and applied relevant principles

Local skill found at:

```text
/Users/jiawei/.claude/skills/ui-ux-pro-max
```

The key applicable principles for this task:

- preserve scroll behavior and avoid unexpected navigation jumps;
- keep content priority aligned with the user's task;
- use progressive disclosure for audit details;
- avoid overwhelming the first reading pass;
- preserve accessibility and readable hierarchy.

This task did not need a large visual redesign. The right first fix was interaction flow and language behavior.

## Verification

Commands run:

```bash
python3 -m py_compile scripts/app.py scripts/research_mode.py scripts/query.py
python3 scripts/test_research_mode.py --verbose
python3 scripts/test_query.py
```

Results:

- `py_compile`: pass
- Research Mode health check: pass
- Query suite: 113 passed, 0 failed

Manual output check:

- English research query now returns Chinese Research Mode output by default.

Browser QA:

- Local test server: `PORT=8514 scripts/run_test_page.sh`
- Browser automation opened `http://localhost:8514/?qa=searchpath-3`
- Clicked the English Research Mode example: `search the latest papers about feline CKD, prioritize high-impact journals`
- Final DOM check:
  - `scrollY = 0`
  - `hasEmptyPrompt = false`
  - `hasContract = true`
  - `hasChineseReport = true`

The local Streamlit test server was stopped after QA.

## Remaining Follow-Up

The scroll fix removes the most likely cause of bottom-jump behavior, but visual browser QA should still confirm the exact viewport behavior in Streamlit.

Recommended next QA:

1. start local app;
2. submit an English research query;
3. confirm the viewport remains at or near the generated answer top;
4. confirm the Research Contract panel appears before the literature report;
5. confirm output language is Chinese unless English is explicitly requested.
