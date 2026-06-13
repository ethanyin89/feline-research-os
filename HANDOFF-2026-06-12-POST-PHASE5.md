# Handoff: Post Phase 5 Result Presentation

**Date:** 2026-06-12  
**Branch:** `idea-chatacademia-research-workbench`  
**Status:** Phase 5 static adapters complete; protected live Ask the Vault acceptance still pending  
**Plan:** [PLAN-page-rendering-improvements.md](/Users/jiawei/Desktop/insclaude/feline-research-os/PLAN-page-rendering-improvements.md)

## What Changed

- `core/result_presentation.py`
  - fixed source-count vs claim-count semantics
  - added explicit unknown / unavailable evidence states
  - added safe URL fallback and user-facing provenance translation
- `core/source_metadata.py`
  - added shared source metadata resolution
  - DOI / PMID / URL priority handled centrally
- `core/static_result_adapter.py`
  - strict overview and ranked adapters
  - no generic Markdown parsing
- `core/static_result_renderer.py`
  - deterministic responsive HTML renderer
  - visible-text leak validation
- `scripts/render_static_result_page.py`
  - CLI for generating static presentation pages
- `scripts/app.py`
  - Ask the Vault now renders translated provenance and titles in the visible answer path
- Content migrated
  - [topics/ckd/what-is-ckd.md](/Users/jiawei/Desktop/insclaude/feline-research-os/topics/ckd/what-is-ckd.md)
  - [system/indexes/ckd-treatment-ranking-memo.md](/Users/jiawei/Desktop/insclaude/feline-research-os/system/indexes/ckd-treatment-ranking-memo.md)

## Generated Artifacts

- [outputs/presentation/ckd-what-is.html](/Users/jiawei/Desktop/insclaude/feline-research-os/outputs/presentation/ckd-what-is.html)
- [outputs/presentation/ckd-treatment-ranking.html](/Users/jiawei/Desktop/insclaude/feline-research-os/outputs/presentation/ckd-treatment-ranking.html)

## Verification

- `python3 -m py_compile` passed for the changed core and script files
- `PYTHONPATH=. python3 scripts/test_result_presentation.py` passed: `7/7`
- `PYTHONPATH=scripts:. python3 scripts/test_authority_containment.py` passed: `5/5`
- `PYTHONPATH=scripts:. python3 scripts/test_query.py` passed: `111/111`
- `git diff --check` passed
- Browser QA passed at mobile, tablet, and desktop widths with no console errors

## Remaining Gate

The only remaining acceptance gate is a protected live Ask the Vault run with `USE_RESULT_PRESENTATION_V2=1`.

Do not remove the feature flag or legacy renderer until this passes:

```bash
USE_RESULT_PRESENTATION_V2=1 \
OPENROUTER_DAILY_BUDGET_USD=1.00 \
OPENROUTER_MODEL=openai/gpt-4.1-mini \
.venv/bin/python -m streamlit run scripts/app.py
```

Before running, confirm the OpenRouter dashboard is capped at `$1/day`.

## Next Steps

1. Run the protected live Ask the Vault acceptance.
2. Verify the visible answer and download contain titles, not `src-*`.
3. Verify DOI / PMID / URL fallback and unavailable-link states.
4. Keep the old renderer until the live gate passes.

## Notes For the Next Agent

- The adapters are intentionally strict; do not generalize them into one parser.
- The current work is about presentation semantics, not retrieval or grading.
- Existing generated pages can be used as acceptance fixtures.
