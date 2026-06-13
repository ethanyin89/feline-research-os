# ChatAcademia Research Workbench - Merge Guide

**Branch:** idea-chatacademia-research-workbench
**Date:** 2026-06-09
**Status:** Ready for merge coordination with Codex

## Overview

This branch implements the ChatAcademia Research Workbench architecture based on II (Intelligent Internet) design principles. The implementation adds a harness loop (Feline-RALPH) that wraps query processing with task evaluation, gap checking, verification, and durable research record storage.

## Files Created

### Core Infrastructure (`core/`)

| File | Lines | Purpose |
|------|-------|---------|
| `__init__.py` | 40 | Module exports |
| `schemas.py` | 440 | ResearchRecord, EvidenceCard, TaskType, SearchDepth, etc. |
| `record_store.py` | 302 | JSON + Markdown persistence for research records |
| `evidence_card.py` | 395 | Evidence Card management with source card integration |
| `task_evaluator.py` | 420 | Bilingual query classification (Chinese/English) |
| `gap_checker.py` | 316 | Harness loop gap detection |
| `verifier.py` | 378 | Independent verification, species boundary checks |
| `test_harness_loop.py` | 182 | End-to-end tests |

### Scripts (`scripts/`)

| File | Lines | Purpose |
|------|-------|---------|
| `harness_loop.py` | ~180 | HarnessLoop class integrating all core modules |
| `research_record_ui.py` | ~250 | Streamlit Research Records workspace UI |
| `benchmark_runner.py` | ~220 | 20 benchmark question runner |

### Storage (`system/`)

| Directory | Purpose |
|-----------|---------|
| `system/research-records/json/` | JSON research records |
| `system/research-records/markdown/` | Markdown research records |
| `system/health-checks/benchmark-harness-*.json` | Benchmark results |

## Files Modified

### `scripts/app.py`

1. Added import: `from harness_loop import get_harness_loop, format_harness_summary`
2. Added import: `from research_record_ui import render_research_records`
3. Added workspace option: "Research Records" in workspace selector
4. Added harness loop integration in query processing (after write-back)
5. Added `harness_result` to `session_state.last_meta`

## Architecture Alignment

The implementation aligns with the six-layer architecture in `ARCHITECTURE.md`:

| Layer | Implementation |
|-------|---------------|
| Layer 1: Human-in-the-Loop | Research Records UI shows all decisions |
| Layer 2: Professional Team | TaskEvaluator assigns task types |
| Layer 3: Research Pipeline | HarnessLoop orchestrates the flow |
| Layer 4: Research Record | ResearchRecord + RecordStore |
| Layer 5: Retrieval Memory | EvidenceCard + EvidenceCardStore |
| Layer 6: Data Quality | GapChecker + Verifier |

## Key Features

1. **Task Evaluation** - Bilingual pattern matching for 9 task types
2. **Search Depth Control** - 4 levels: Quick, Standard, Deep, Evidence Audit
3. **Gap Checking** - Protocol/endpoint/literature/PK checklists
4. **Verification** - Species boundary, evidence grounding, uncertainty disclosure
5. **Durable Records** - Every query generates a retrievable record

## Benchmark Results

**20 benchmark questions: 100% pass rate**

| Task Type | Count |
|-----------|-------|
| endpoint_selection | 7 |
| model_evaluation | 7 |
| protocol_design | 3 |
| pk_design | 2 |
| other | 1 |

## Integration Points for Codex

If Codex has parallel work, here are the integration points:

1. **Agent Profiles** - If Codex created agent YAML definitions, they can be loaded by TaskEvaluator
2. **Prompt Engineering** - If Codex created prompts, they can be used in the pipeline
3. **Visual Direction** - If Codex created UI designs, they can be applied to research_record_ui.py
4. **Evidence Card Examples** - If Codex created examples, they can be loaded by EvidenceCardStore

## Testing

```bash
# Run harness loop tests
python3 core/test_harness_loop.py

# Run benchmark
python3 scripts/benchmark_runner.py

# Run health check
python3 scripts/health.py
```

## No Breaking Changes

The implementation follows the principle from ARCHITECTURE.md:
- New architecture layers extend, not replace existing code
- Existing query.py continues to work
- Harness loop is an optional wrapper around existing functionality
- All 111 query tests continue to pass

## Next Steps

1. **Codex Merge** - Coordinate on any parallel work
2. **UI Polish** - Apply visual direction to Research Records workspace
3. **Agent Profiles** - Add YAML-based agent configuration
4. **Evidence Cards** - Bulk import from existing source cards
