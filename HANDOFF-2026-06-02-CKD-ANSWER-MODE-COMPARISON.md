# Handoff: CKD Answer Mode Comparison — 2026-06-02

## Classification

This was **check + investigation**, triggered by ordinary-user testing across three answer modes:

1. `Vault Search (free)`
2. API synthesis inside Ask the vault
3. Wikipedia / 維基百科

The user observed that answers differed strongly. The important product failure was not that Wikipedia differs from the vault. That is expected. The failure was that API synthesis could look narrower than free mode, because one screenshot showed `Readings loaded: 1`.

## Finding

Free mode is stable:

- `.venv/bin/python scripts/ordinary_user_vault_eval.py`
- Result: 6/6 PASS, all `api_calls=0`

The API path had a retrieval-width bug for broad overview questions.

In `scripts/query.py`, `run_query_core()` already loads overview topic pages such as:

- `topics/ckd/current-state-dashboard.md`
- `topics/ckd/synthesis-index.md`

Those pages have rich `source_ids` frontmatter, but the API path only fell back to those IDs when **zero** source cards were loaded. If search preheat loaded exactly one source card, such as `src-ckd-004`, fallback did not run. The hop agent could then synthesize with one source.

That explains the user-visible bad feel: API mode could spend money and still show weaker evidence breadth than free mode.

## Fix

Commit pushed to `origin/main`:

- `5929458 fix(query): preload overview source baseline for api synthesis`

Changed:

- `scripts/query.py`
  - Added `OVERVIEW_MIN_SOURCE_CARDS = 4`
  - Added `source_ids_from_topic_frontmatter(...)`
  - In API `overview` routing, preload source cards from loaded topic-page `source_ids` until at least 4 source cards are loaded before hop/synthesis.
- `scripts/test_query.py`
  - Added regression test for the case where `src-ckd-004` is already loaded and topic frontmatter should fill the remaining baseline cards without duplicates.

## Verification

Ran:

```bash
python3 -m py_compile scripts/query.py scripts/test_query.py
python3 scripts/test_query.py
.venv/bin/python scripts/ordinary_user_vault_eval.py
python3 scripts/health.py
```

Results:

- `scripts/test_query.py`: 108 passed / 0 failed
- ordinary-user free-mode eval: 6/6 PASS, all `api_calls=0`
- health: exit code 0
- health summary: query tests 108 passed / 0 failed, ordinary-user vault eval PASS

Do not commit generated `system/health-checks/health-report-20260602.md` as part of this thread.

## Product Interpretation

Wikipedia is a public encyclopedia page: broad, stable, human-edited, and not constrained to this vault's source-card evidence model.

Free vault is now a deterministic local answer surface: fast, no API, intentionally compact, with source IDs and explicit uncertainty.

API vault should be used when the user wants synthesis across vault evidence. It should not be narrower than free mode for broad overview questions. This fix makes the API path load a minimum evidence baseline before synthesis.

## Remaining Risk

This does not guarantee API and Wikipedia will agree. They should not always agree. The target is:

- API answer has enough loaded vault evidence to be worth paying for.
- The answer clearly shows evidence breadth, uncertainty, and source trace.
- If the user asks a broad CKD question, API mode should not show `Readings loaded: 1` unless the vault truly has only one relevant source.

## Dirty Worktree Boundary

There are still unrelated pre-existing modified/untracked files, especially cancer extraction work, public-test artifacts, `scripts/health.py`, and generated health reports. Do not include them in this thread unless explicitly scoped.
