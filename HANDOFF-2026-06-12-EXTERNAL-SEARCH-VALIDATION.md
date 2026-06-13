# Handoff: External Search Validation and Expert Review Fix

**Date:** 2026-06-12  
**Branch:** `idea-chatacademia-research-workbench`  
**Status:** DONE, browser-validated

## Summary

This session finished the expert-review and external-search pass for the Ask the Vault surface. The free Vault Search path now triggers PubMed/Crossref when local results are sparse, the research trace shows those external candidates as `needs intake`, and the expert review panel now shows real verifier messages instead of a generic placeholder.

## What Changed

| File | Change |
|------|--------|
| `scripts/query.py` | Added reusable external-search trace building and wired sparse-result external search into the free/local path |
| `scripts/app.py` | Passed the external-search toggle into the local path and rendered the new trace entries |
| `scripts/harness_loop.py` | Exposed real verifier messages in the harness result so the UI can show them |
| `scripts/test_query.py` | Added regression tests for sparse-result gating and external-search trace output |
| `HANDOFF-2026-06-12-EXPERT-REVIEW-EXTERNAL-SEARCH.md` | Updated the previous handoff with the verified browser results |

## Verified Behavior

### 1. Expert Review display

CKD explanation flow now shows:

- `Passed`
- `Task: quick_explanation`
- `Depth: quick`
- `Search depth contract: Satisfied`

The verifier messages are visible in the review panel, not just the overall status.

### 2. External search

For a sparse query such as `feline hyperthyroidism treatment`:

- the free Vault Search path now triggers PubMed/Crossref
- external candidates are shown in the research trace
- each external result is marked `needs intake`
- external results are not treated as vault evidence yet

### 3. Deep-mode warning

With `Deep` selected and sparse evidence, the UI shows:

- `Search depth contract: Not satisfied`
- the warning `深度研究模式深度合约未满足`
- a concrete failure like `evidence 2/3`

The earlier CKD sample is not a valid warning test because it already satisfies the deep contract.

## Verification

```text
python3 scripts/test_query.py
113 passed | 0 failed

PYTHONPATH=. python3 core/test_harness_loop.py
All tests passed

python3 -m py_compile scripts/app.py scripts/query.py scripts/harness_loop.py scripts/test_query.py
passed

git diff --check -- scripts/app.py scripts/query.py scripts/harness_loop.py scripts/test_query.py
passed
```

Browser acceptance was also run against the local Streamlit app:

- CKD explanation flow rendered correctly
- the sparse `feline hyperthyroidism treatment` query returned PubMed/Crossref candidates
- Deep mode displayed the contract warning when the evidence was thin

## Current Worktree Notes

- The repo is still very dirty with a large amount of unrelated content and source-card work.
- Do not run cleanup or reset commands.
- Treat the current session as a continuation of the existing worktree, not a clean branch.

## Remaining Optional Work

1. Add a progress indicator while external search is running.
2. Add an explicit intake action for external candidates, but only if it follows the normal source-card validation path.
3. Keep the deep-mode warning example tied to a genuinely sparse query, not CKD overview prompts that already satisfy the contract.

## Safe Restart

If the next operator needs to pick this up, the shortest path is:

```bash
git status --short
python3 scripts/test_query.py
PORT=8514 scripts/run_test_page.sh
```

