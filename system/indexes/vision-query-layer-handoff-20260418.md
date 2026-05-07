---
title: Vision-Integrated Query Layer — Implementation Handoff
date: 2026-04-18
status: complete
branch: unknown
---

# Vision-Integrated Query Layer — Handoff Doc

Implementation of Approach B (vision attachment to Anthropic synthesis calls) for the Feline Research OS query pipeline. This doc exists so any model can pick up mid-session.

## What Was Built (Done)

| File | What Changed |
|------|-------------|
| `scripts/query.py` | Added `VISION_MAX_FILE_BYTES` constant, `_figure_type_from_filename()`, rewrote `resolve_local_assets()` with size + path-traversal guards + figure_type sorting, added `enrich_source_card_with_caption()`, added `run_query_core()` (shared DRY engine) |
| `.streamlit/config.toml` | Created — dark theme: `#0f1117` bg, `#16a34a` primary |

## What Remains (Pending — Human Task Only)

CKD pilot extraction is partially complete. Remaining asset work is now:
- unresolved source-access work for `src-ckd-013`
- verify against article figure/table labels before removing any `candidate-*` prefix
- once a real file is placed and linked in the source card, vision synthesis activates automatically (`VISION_INTEGRATION_ENABLED=True`)

## What Was Completed (2026-04-18)

All code tasks finished. Current repo test state verified on `2026-04-18`: `67/67` tests pass.

| Task | Status |
|------|--------|
| `main()` simplified to call `run_query_core()` | Done |
| `app.py` imports cleaned up, run_query() simplified | Done |
| CSS injection (Geist fonts, 720px max-width) | Done |
| 6 new test edge cases added + registered | Done |
| `enrich_source_card_with_caption()` wired into main() | Done |
| Test suite: 67/67 pass (current repo state verified 2026-04-18) | Done |

## Current Runtime Reality

- CKD pilot assets on disk: 8 verified files from `src-ckd-001`, `src-ckd-017`, `src-ckd-022`, and `src-ckd-024`
- Remaining live source-access blocker: `src-ckd-013`
- `src-ckd-022` no longer has a live model-design blocker; the earlier candidate was retired after accessible source-surface review
- Current shell check on `2026-04-18` found `ANTHROPIC_API_KEY` unset, so a live Step 5 demo was not run in this environment

---

## Original Pending Items (Archived)

### 1. Simplify `main()` in `scripts/query.py`

The `run_query_core()` function exists (line 812) but `main()` still contains the old duplicated routing/hop/synthesis block (lines 1026–1148). Replace that block with:

```python
    # Run query (routing → hops → synthesis)
    print("[info] Routing...", file=sys.stderr)
    result = run_query_core(
        client, args.question, VAULT_ROOT, source_index,
        disease_hint=args.disease,
        max_hops=args.max_hops,
        model=active_model,
    )
    answer = result["answer"]
    figures_used = result["figures_used"]
    disease = result["disease"]
    question_type = result["question_type"]
    hops_used = result["hops_used"]
    loaded_paths = result["loaded_paths"]

    print(f"[meta] ROUTER_QTYPE={question_type}", file=sys.stderr)
    print(f"[meta] ROUTER_DISEASE={disease}", file=sys.stderr)
    print(f"[meta] LOADED_PATHS={_render_loaded_paths_meta(loaded_paths, VAULT_ROOT)}", file=sys.stderr)
```

The rest of main() (answer print, figure footer, write-back block) stays unchanged.

### 2. Update `scripts/app.py`

a) Add import at top:
```python
from query import run_query_core
```

b) Replace `run_query()` body with call to `run_query_core()` + UI rendering.

c) Add CSS injection block after `st.set_page_config(...)`:
```python
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Geist+Sans:wght@400;500;600&family=Geist+Mono&display=swap');
html, body, [data-testid="stApp"] { font-family: 'Geist Sans', sans-serif; }
.chat-container { max-width: 720px; margin: 0 auto; }
code, .source-id { font-family: 'Geist Mono', monospace; font-size: 0.85em; }
</style>
""", unsafe_allow_html=True)
```

### 3. Add 6 test edge cases to `scripts/test_query.py`

Tests from `~/.gstack/projects/feline-research-os/jiawei-unknown-eng-review-test-plan-20260417-215643.md`:
- `_test_parse_local_assets_key_missing` — no `local_assets` key → `[]`
- `_test_resolve_local_assets_empty_source_ids` — empty list → `[]`
- `_test_resolve_local_assets_card_file_not_found` — missing card → `[]`
- `_test_write_back_no_figures_used_key_when_none` — `figures_used=None` → no key in frontmatter
- `_test_resolve_local_assets_skips_large_file` — >2MB file → `[]` (needs size guard, should now pass)
- `_test_resolve_local_assets_path_traversal_blocked` — `../../etc/passwd` → `[]` (needs guard, should now pass)

Register all 6 in the `__main__` block.

### 4. Wire `enrich_source_card_with_caption()` into write_back

In `write_back()` or at the call site in `main()`, after synthesis: for each figure in `figures_used` where `described_in_answer=True`, call:
```python
enrich_source_card_with_caption(fig["source_id"], fig["file"], fig["caption"], vault_root)
```

### 5. Run test suite

```bash
python3 scripts/test_query.py
```

Expected at the time of that implementation checkpoint: 47/47 pass (41 existing + 6 new). Current repo state is higher and should be verified against the live test suite, not this archived checkpoint.

## Key Constants / Identifiers

```python
VISION_INTEGRATION_ENABLED = True       # query.py
VISION_FIGURE_CAP = 4                   # max figures per synthesis call
VISION_MAX_FILE_BYTES = 2 * 1024 * 1024 # 2MB size guard
MODEL = "claude-opus-4-5-20251101"       # or current Anthropic model
```

## Architecture Summary

```
question
  → router_call()       # classifies disease + question_type + initial files
  → hop loop            # agent decides load_more / load_sources / synthesize
  → resolve_local_assets()  # maps loaded source IDs → verified PNG paths, sorted by figure_type
  → synthesis_call()    # attaches figures as base64 vision blocks (Anthropic only)
  → write_back()        # optional: writes answer + frontmatter to outputs/qa/
  → enrich_source_card_with_caption()  # optional: writes AI caption back to source card
```

`run_query_core()` encapsulates everything from router_call through synthesis_call.
`main()` and `app.py:run_query()` both call it.

## Human Task (Still Open)

Continue CKD pilot extraction only where unresolved:
- `src-ckd-013`
- verify against article figure/table labels
- remove `candidate-*` prefix only when verified

## Current Runtime Reality

As of `2026-04-21`, the code side is done and the CKD pilot has verified assets:

- `raw/images/ckd/` has 8 verified non-candidate files from `src-ckd-001`, `src-ckd-017`, `src-ckd-022`, and `src-ckd-024`
- `src-ckd-013` remains blocked by source access and must stay behind the `candidate-*` gate
- vision synthesis can attach verified CKD assets when the selected backend supports image inputs

## Files to Read for Context

- `scripts/query.py` lines 690–981 — `resolve_local_assets`, `enrich_source_card_with_caption`, `run_query_core`
- `scripts/app.py` — current run_query() implementation
- `scripts/test_query.py` — existing 41 tests
- `~/.gstack/projects/feline-research-os/jiawei-unknown-eng-review-test-plan-20260417-215643.md` — 6 new test bodies
