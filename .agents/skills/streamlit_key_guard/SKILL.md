---
name: streamlit_key_guard
description: Prevention and static verification of Streamlit Duplicate Element Key hazards in multi-turn chat applications.
---

# Streamlit Widget Key Guard

This skill provides guidelines and automated tools to ensure Streamlit widget key uniqueness. In multi-turn chat screens, Streamlit re-executes the rendering code for every message in the history. If a widget key is static or only depends on a static identifier (like a document ID or filename) without incorporating a conversation-turn prefix or message-index prefix, Streamlit will crash with a `StreamlitDuplicateElementKey` exception.

## Crucial Naming Standards for Widgets

Whenever you define an interactive Streamlit element (e.g., `st.button`, `st.selectbox`, `st.checkbox`, `st.text_input`, etc.) inside a function or loop that could be repeated across chat turns:

1. **Always specify `key`**: Never rely on Streamlit's default auto-generated keys when a widget is inside loops or helper functions.
2. **Incorporate `key_prefix`**: Ensure the rendering function accepts a `key_prefix: str` parameter. Pass it down from the main chat history loop (which typically uses `f"history-{i}"` or `f"live-{len(messages)}"`).
3. **Format string widget keys**: Prepend the `key_prefix` to the widget key, e.g., `key=f"{key_prefix}-my-action"`.
4. **Distinguish toggle state**: If you store widget toggle state in `st.session_state` (e.g. for expanding/collapsing abstract sections), name the session state keys with the prefix too, e.g. `state_key = f"show_abs_{key_prefix}_{card_id}"`. This avoids one message turn's toggle affecting another turn's toggle.

## Running Verification

To statically analyze python files in the project for potential Streamlit key issues, run the verification script:

```bash
.venv/bin/python .agents/skills/streamlit_key_guard/scripts/lint_streamlit_keys.py
```
