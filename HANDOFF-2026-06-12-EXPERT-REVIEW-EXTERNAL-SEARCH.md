# Handoff: Expert Review Loop + External Search Integration

**Date:** 2026-06-12
**Branch:** `idea-chatacademia-research-workbench`
**Status:** DONE, implementation and browser acceptance complete

## Summary

Implemented the three-phase plan for enhancing the expert review loop and integrating external search capabilities:

1. **Phase 1** - Display real verification results from harness loop
2. **Phase 2** - External search (PubMed/Crossref) when local results sparse
3. **Phase 3** - II.Inc style search depth mode selector

## Files Modified

| File | Changes |
|------|---------|
| `scripts/app.py` | Added verification badge, depth warning, external search toggle, depth selector, enhanced research trace |
| `scripts/query.py` | Added `is_local_search_sparse()`, reusable external search trace builder, external search integration, `allow_external_search` parameter |
| `scripts/harness_loop.py` | Added `explicit_search_depth` parameter and exposed real verifier messages |
| `scripts/test_query.py` | Added external-search sparse gating and `needs_intake` trace tests |

## New UI Elements

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
│  此模式要求更多来源或来源多样性...                        │
├─────────────────────────────────────────────────────────┤
│  ▸ Research trace                                       │
│    1. Interpreted query: disease=ckd; question_type=... │
│    2. Searched vault: scope=raw; limit=5; results=3     │
│    3. External search (PubMed/Crossref): query=...      │  ← NEW
│       PUBMED  Feline CKD phosphorus...  DOI:... needs intake │
├─────────────────────────────────────────────────────────┤
│  ▸ 验证结果 / Expert Review                              │
│    ✓ Passed                                             │
│    Task: endpoint_selection · Depth: standard           │
│    ✓ Search depth contract: Satisfied                   │
│    (gaps and verification messages if any)              │
│    ──────────────────────────────                       │
│    Manual review checkpoints...                         │
│    [Download review prompt]                             │
└─────────────────────────────────────────────────────────┘
```

## Verification Tests

### Completed 2026-06-12

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

### Phase 1: Harness Results Display

```bash
PORT=8514 scripts/run_test_page.sh
# Ask: "解释CKD"
# Expected: Expert review loop shows verification status, task type, depth
```

Browser result:

- `Passed`
- `Task: quick_explanation`
- `Depth: quick`
- `Search depth contract: Satisfied`
- real verifier check messages render in the expanded review panel

### Phase 2: External Search

```bash
# Enable "Search PubMed/Crossref if local results sparse" in sidebar
# Ask: "feline hyperthyroidism treatment" (not in vault)
# Expected: Research trace shows PubMed/Crossref results with "needs intake"
```

Browser result:

- works in the default `Vault Search (free)` engine
- 10 PubMed/Crossref candidates returned during acceptance
- each candidate displayed as `needs intake`
- external candidates remain trace-only and are not promoted to vault evidence

Fix made during acceptance: the checkbox was previously passed only to paid API
engines. The free local engine now invokes the same gated external search path when
fewer than three local source cards are loaded.

### Phase 3: Depth Modes

```bash
# Select "Deep" mode in sidebar
# Enable external search
# Ask: "feline hyperthyroidism treatment"
# Expected: sparse local evidence shows depth contract warning
```

Browser result:

- `Depth: deep`
- `Search depth contract: Not satisfied`
- visible `深度研究模式深度合约未满足` warning
- concrete failure displayed: `evidence 2/3`

The original `"解释CKD"` example is not a valid warning test. It performs two
observable retrieval rounds and loads both source cards and topic synthesis, so the
Deep contract correctly passes.

## Architecture Notes

### Data Flow

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

### SearchDepth Enum Values

| Mode | Value | Behavior |
|------|-------|----------|
| Auto | `None` | TaskEvaluator auto-detects from question |
| Quick | `"quick"` | 0-1 searches, simple explanation |
| Standard | `"standard"` | 2-3 sources, at least 2 types |
| Deep | `"deep"` | 2+ rounds with gap reflection |
| Audit | `"evidence_audit"` | Must include contrary evidence |

### External Search (Gated)

- Uses existing `scripts/external_search.py`
- PubMed via NCBI E-utilities (free, no API key)
- Crossref via public API (free, no API key)
- Results marked as "needs intake" - not vault evidence until processed
- Default: OFF (free mode preserved)

## Constraints Compliance

- **OpenRouter $1/day**: External search uses free PubMed/Crossref APIs
- **Free Vault Search**: Always available, external is opt-in
- **No one-off work**: Deep mode manual trigger until validated

## Known Limitations

1. External search results are informational only - cannot be cited as vault evidence
2. Depth contract warning is informational - does not block answer generation
3. External search adds ~2-3 seconds latency (API calls)

## Remaining Optional Work

1. Consider adding an explicit intake action for external results. Do not label it
   "Import to Vault" unless it runs the normal source-card validation workflow.
2. Consider adding a progress indicator during the external network calls.
