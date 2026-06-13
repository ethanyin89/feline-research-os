# Handoff: Phase 6 Presentation And Research Flywheel Closeout

**Date:** 2026-06-12
**Branch:** `idea-chatacademia-research-workbench`
**Status:** `DONE_WITH_CONCERNS`
**Plan:** [PLAN-page-rendering-improvements.md](PLAN-page-rendering-improvements.md)

## Read This First

This handoff is the latest state for the Phase 6 presentation, Research Record,
claim-promotion, and validated-claim work.

The repository worktree is heavily dirty with unrelated content changes. Do not use
bulk reset, checkout, add, or commit operations. Limit edits to the files named here.

## Product Model Now Implemented

```text
real source cards
  -> research question
  -> retrieval and synthesis
  -> transient Research Record
  -> explicit user save
  -> claim selection
  -> independent claim validation
  -> human-confirmed promotion
  -> validated claim store
  -> stale exclusion when source content changes
```

A saved Research Record remains workflow context. It does not become evidence
automatically. Only source-traced, human-selected, validated claims enter the reusable
knowledge channel.

## Completed Work

### 6A: Explicit Research Record Save

- `scripts/harness_loop.py`
  - query finalization returns a transient record
  - query completion no longer writes a Research Record automatically
- `core/record_store.py`
  - explicit save boundary
  - atomic writes, duplicate checks, path containment, and rollback
- `scripts/app.py`
  - explicit `Save Research Record`
- `scripts/research_record_ui.py`
  - record browser and validated-claim statistics

### 6B: Claim Selection And Validation Draft

- `core/claim_promotion.py`
  - extracts exact claim candidates from provenance-tagged answer lines
  - blocks inference-only claims
  - validates source mapping and target allowlist
  - produces a draft without mutating the knowledge base
- `scripts/app.py`
  - claim selection, target selection, validation results, and confirmation state

### 6C: Promotion, Freshness, And Reuse

- `core/validated_claim_store.py`
  - promotion manifests
  - validated claim JSON and Markdown
  - SHA-256 source fingerprints
  - stale queue and stale exclusion
  - validated-only query channel
  - target Markdown page generation and rebuild
- generated target pages use:
  - `Promotion Judgment`
  - `Key-Claim Traceability`
  - `Source Coverage`
  - `Boundary`
- `scripts/app.py`
  - explicit human-confirmed `Apply Promotion`

### Presentation And Six-Dimension Source Disclosure

- `core/source_metadata.py`
  - shared metadata loading now includes available authors, publication date, PMID,
    PMCID, DOI, source kind, evidence level, species, decision grade, tags, disease,
    model, endpoint, jurisdiction, and local asset metadata
- `core/result_presentation.py`
  - `SourceDisplay` carries source family, species boundary, extraction depth,
    verification state, decision grade, deterministic safest use, and overclaim boundary
  - DOI, PubMed, PMC, and safe URL fallback
- `scripts/app.py`
  - V2 source cards display source family, species, decision grade, and safest use
- `core/static_result_renderer.py`
  - static fixtures use the same source-card metadata

## Presentation Rollout State

`USE_RESULT_PRESENTATION_V2` now defaults to enabled in `scripts/app.py`.

- normal local or hosted startup uses V2
- `scripts/run_test_page.sh` explicitly exports `USE_RESULT_PRESENTATION_V2=1`
- rollback remains available with `USE_RESULT_PRESENTATION_V2=0`
- the legacy renderer has not been removed

README documents the default and rollback behavior.

## Local Page Verification

Local test server:

```text
http://localhost:8514
```

Verified on 2026-06-12:

- Streamlit started with `USE_RESULT_PRESENTATION_V2=1`
- `GET /_stcore/health` returned `ok`
- `GET /` returned `HTTP 200`
- browser-rendered page showed:
  - Ask / Research Cases / Research Records workspaces
  - Vault Search as the default free engine
  - 617 sources
  - 172 topic pages
  - 8 diseases
  - example questions and chat input
- no paid API call was made

Residual browser finding:

- one Streamlit frontend console error from the recording/waveform component:
  `wavesurfer ... Container not found`
- the main text interface still rendered and remained interactive
- treat this as a non-blocking frontend dependency issue unless audio recording becomes
  an intended workflow

## Hosted Streamlit Verification

Target:

`https://feline-research-os-3fzhk6zhd2mgvj8rxlbvou.streamlit.app/`

Observed on 2026-06-12:

- root URL returned `HTTP 303` to Streamlit authentication
- `~/+/` returned `HTTP 200` for the Streamlit shell

This proves the deployment endpoint is alive. It does **not** prove that the authenticated
app is running the current worktree or that V2 source cards are visible online.

Do not state that hosted acceptance passed until an authenticated browser session verifies:

1. the V2 answer path is active;
2. visible citations use paper titles instead of `src-*`;
3. source cards show available quality dimensions;
4. Research Records and claim promotion workspaces load;
5. no blocking console errors occur.

## Verification Commands Passed

```bash
python3 -m py_compile \
  core/source_metadata.py \
  core/result_presentation.py \
  core/static_result_renderer.py \
  core/validated_claim_store.py \
  scripts/app.py

PYTHONPATH=. python3 scripts/test_result_presentation.py
PYTHONPATH=. python3 scripts/test_validated_claim_store.py
PYTHONPATH=. python3 scripts/test_claim_promotion.py
PYTHONPATH=. python3 scripts/test_research_record_store.py
PYTHONPATH=. python3 core/test_harness_loop.py
bash -n scripts/run_test_page.sh
```

All listed tests passed. `git diff --check` passed for the files changed in this lane.

## Key Tests

- `scripts/test_result_presentation.py`
  - source and claim counts remain distinct
  - unknown depth is not promoted
  - safe canonical URL fallback
  - optional source metadata and PMC fallback
  - visible provenance uses titles, not internal IDs
  - overview and ranked fixtures contain no internal-token leakage
- `scripts/test_research_record_store.py`
  - save/load, duplicate detection, containment, rollback
- `scripts/test_claim_promotion.py`
  - extraction, validated draft, inference blocking, target blocking
- `scripts/test_validated_claim_store.py`
  - promotion, target page generation, stale exclusion, missing-source blocking
- `core/test_harness_loop.py`
  - query finalization performs zero persistence

## Remaining Work

1. Run authenticated hosted Streamlit acceptance against the current deployed revision.
2. Confirm the hosted revision includes these local changes. The current dirty worktree
   has not been established as deployed.
3. Decide whether to keep or suppress the non-blocking Streamlit recording component
   console error.
4. After hosted acceptance, consider removing the legacy renderer. Do not remove it
   before that gate.

## Safe Restart Sequence

```bash
cd /Users/jiawei/Desktop/insclaude/feline-research-os

PYTHONPATH=. python3 scripts/test_result_presentation.py
PYTHONPATH=. python3 scripts/test_validated_claim_store.py
PYTHONPATH=. python3 scripts/test_claim_promotion.py

PORT=8514 scripts/run_test_page.sh
```

Use Vault Search for no-cost smoke testing. Do not select OpenRouter until the dashboard
limit is confirmed at `$1/day`.

## Bottom Line

The local V2 presentation and Phase 6 Research Record-to-validated-claim path are
implemented and regression-tested. The hosted endpoint is alive but remains
`acceptance pending` because authentication prevented inspection of the deployed app
content.
