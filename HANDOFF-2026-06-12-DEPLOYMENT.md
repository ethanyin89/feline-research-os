# Handoff: Expert Review Loop + External Search Deployment

**Date:** 2026-06-12
**Branch:** `idea-chatacademia-research-workbench`
**Commit:** `2cc2a84`
**Status:** DEPLOYED TO GITHUB

## Summary

Deployed the Expert Review Loop and External Search integration to GitHub. All tests pass, local UI verified, code pushed to remote.

## Commit Contents

```
feat: add Expert Review Loop and External Search integration

20 files changed, 7328 insertions(+), 263 deletions(-)
```

### Core Modules Added (`core/`)

| File | Purpose |
|------|---------|
| `schemas.py` | Research Record, Evidence Card, Task types |
| `task_evaluator.py` | Query classification and depth assignment |
| `search_depth_controller.py` | Execution contract enforcement |
| `gap_checker.py` | Evidence gap detection |
| `verifier.py` | Answer verification with checkpoints |
| `record_store.py` | Research Record persistence |
| `evidence_card.py` | Structured evidence units |
| `result_presentation.py` | User-facing presentation model |
| `source_metadata.py` | DOI/PMID/URL resolution |
| `claim_promotion.py` | Claim validation and promotion |
| `validated_claim_store.py` | Validated claim retrieval |
| `static_result_adapter.py` | Overview and ranking adapters |
| `static_result_renderer.py` | Deterministic HTML output |
| `test_harness_loop.py` | Harness integration tests |

### Scripts Added/Modified

| File | Changes |
|------|---------|
| `scripts/app.py` | +835 lines: Search depth selector, external search toggle, verification badges, depth warnings |
| `scripts/query.py` | +123 lines: `is_local_search_sparse()`, external search integration, `allow_external_search` parameter |
| `scripts/harness_loop.py` | New: `explicit_search_depth` parameter, real verifier messages |
| `scripts/external_search.py` | New: PubMed and Crossref API clients |
| `scripts/test_query.py` | +61 lines: External search and needs_intake tests |

## New UI Features

### Sidebar (Advanced Settings)

```
[Search depth]  (•) Auto  ( ) Quick  ( ) Standard  ( ) Deep  ( ) Audit

[Agent depth]   ████████░░ 3

[ ] Auto-save answers
[ ] Search PubMed/Crossref if local results sparse
```

### Answer Display

```
┌─────────────────────────────────────────────────────────┐
│  Answer text with provenance tags...                    │
├─────────────────────────────────────────────────────────┤
│  Evidence Profile: 5 sources · 3 quoted · 2 inferred   │
├─────────────────────────────────────────────────────────┤
│  ✓ 验证通过 | ✓ 深度合约满足                              │
├─────────────────────────────────────────────────────────┤
│  ⚠️ 深度研究模式深度合约未满足 (if applicable)           │
├─────────────────────────────────────────────────────────┤
│  ▸ Research trace                                       │
│    1. Interpreted query: disease=ckd; question_type=... │
│    2. Searched vault: scope=raw; limit=5; results=3     │
│    3. External search (PubMed/Crossref): query=...      │
│       PUBMED  Feline CKD phosphorus...  DOI:... needs intake │
├─────────────────────────────────────────────────────────┤
│  ▸ 验证结果 / Expert Review                              │
│    ✓ Passed                                             │
│    Task: endpoint_selection · Depth: standard           │
│    ✓ Search depth contract: Satisfied                   │
└─────────────────────────────────────────────────────────┘
```

## Test Results

```
python3 scripts/test_query.py
113 passed | 0 failed

PYTHONPATH=. python3 core/test_harness_loop.py
All tests passed

PYTHONPATH=. python3 scripts/test_result_presentation.py
8 tests passed

PYTHONPATH=. python3 scripts/test_claim_promotion.py
All claim promotion tests passed

PYTHONPATH=. python3 scripts/test_validated_claim_store.py
All validated claim store tests passed

PYTHONPATH=. python3 scripts/test_research_record_store.py
All Research Record store tests passed
```

## Local UI Verification

Screenshots captured at:
- `/tmp/feline-test-home.png` - Home page with Ask the vault
- `/tmp/feline-test-advanced.png` - Advanced settings expanded
- `/tmp/feline-test-answer.png` - CKD explanation answer

Verified:
- Search depth selector (Auto/Quick/Standard/Deep/Audit) visible
- External search checkbox visible
- Free Vault Search returns answers with source citations
- Answer display shows provenance and source links

## Deployment

**Pushed to:** `origin/idea-chatacademia-research-workbench`

The Streamlit Cloud app at `https://feline-research-os-3fzhk6zhd2mgvj8rxlbvou.streamlit.app/` will update automatically if configured to deploy from this branch.

If deployed from `main`, merge is required:
```bash
git checkout main
git merge idea-chatacademia-research-workbench
git push origin main
```

## Architecture

```
User question
    ↓
run_query_core(allow_external_search=bool)
    ↓
Local vault search
    ↓
is_local_search_sparse()? ──yes──→ search_pubmed() + search_crossref()
    ↓                                        ↓
research_trace with external items ←─────────┘
    ↓
harness.evaluate_query(explicit_search_depth=str|None)
    ↓
harness.process_query_result()
    ↓
harness_result dict
    ↓
render_answer_block_v2(harness_result=dict)
    ↓
render_verification_badge()
render_depth_contract_warning()
render_expert_review_loop(harness_result=dict)
```

## Remaining Work

### Gate 6A (Next Phase)

From PLAN-page-rendering-improvements.md Phase 6:

1. Schema version + backward-compatible migrations
2. RetrievalEvent and SourceSnapshot
3. Pure harness finalization with zero persistence
4. Atomic RecordStore + commit manifest + reconciliation
5. Explicit-save UI + duplicate/version handling

### Deferred

- Gate 6B: Claim selection and validation drafts
- Gate 6C: Promotion and validated reuse
- Protected live API acceptance test (requires $1/day OpenRouter cap)

## Constraints

- **OpenRouter $1/day**: External search uses free PubMed/Crossref APIs only
- **Free Vault Search**: Always available without API costs
- **No one-off work**: Deep mode manual trigger until validated

## Files Not Committed

692 files remain uncommitted (content updates, documentation, additional scripts). The deployment commit focused on core functionality required for the Expert Review Loop and External Search features.
