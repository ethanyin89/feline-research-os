# Handoff: Result Presentation Contract - Phase 5 Static Adapters Complete

**Date:** 2026-06-12
**Branch:** `idea-chatacademia-research-workbench`
**Status:** Phase 5 static adapter work complete; protected live Ask the Vault acceptance remains
**Plan:** `PLAN-page-rendering-improvements.md`

## Completed

- Fixed source-count versus claim-count semantics in `core/result_presentation.py`.
- Added explicit unknown metadata handling.
- Added shared source metadata resolution in `core/source_metadata.py`.
- Added strict overview and ranked adapters in `core/static_result_adapter.py`.
- Added deterministic responsive HTML rendering in `core/static_result_renderer.py`.
- Added CLI entrypoint: `scripts/render_static_result_page.py`.
- Migrated:
  - `topics/ckd/what-is-ckd.md`
  - `system/indexes/ckd-treatment-ranking-memo.md`
- Generated:
  - `outputs/presentation/ckd-what-is.html`
  - `outputs/presentation/ckd-treatment-ranking.html`
- Updated Ask the Vault V2 to show paper titles and translated provenance labels instead
  of internal IDs in visible answers and downloads.

## Verification

```bash
python3 -m py_compile \
  core/result_presentation.py \
  core/source_metadata.py \
  core/static_result_adapter.py \
  core/static_result_renderer.py \
  scripts/render_static_result_page.py \
  scripts/app.py \
  scripts/test_result_presentation.py

PYTHONPATH=. python3 scripts/test_result_presentation.py
```

Result: 7/7 tests passed.

Browser QA:

- 375x812: pass, stacked tables, no horizontal overflow
- 768x1024: pass
- 1280x720: pass
- console errors: none on either fixture
- visible `src-*`, raw verification status, raw provenance token: none

## Key Architecture

```text
approved Markdown fixture
        |
        +--> strict overview adapter
        |
        +--> strict ranked adapter
                 |
                 v
        ResultPresentation models
                 |
                 v
       deterministic HTML renderer
                 |
                 v
       visible-text leak validation
```

The adapters are intentionally strict. Do not turn them into a generic Markdown parser.

## Remaining Work

Run one protected live Ask the Vault acceptance with V2 enabled:

```bash
USE_RESULT_PRESENTATION_V2=1 \
OPENROUTER_DAILY_BUDGET_USD=1.00 \
OPENROUTER_MODEL=openai/gpt-4.1-mini \
.venv/bin/python -m streamlit run scripts/app.py
```

Before running, confirm the OpenRouter dashboard limit is `$1/day`. Do not mark the live
path accepted without that safeguard.

Verify:

1. visible answer and download contain titles, not `src-*`;
2. evidence profile source count is deduplicated;
3. DOI, PMID, URL fallback, and unavailable-link states render correctly;
4. figures and expert review loop still work;
5. old renderer remains available by disabling the feature flag.

Only after this live gate passes should the feature flag and legacy renderer be removed.
