# Plan: ChatAcademia-Inspired Research Workbench

**Status:** MVP IMPLEMENTED; search-depth execution contract completed 2026-06-11
**Branch:** idea-chatacademia-research-workbench
**Design Doc:** `ARCHITECTURE.md`
**Date:** 2026-06-09

## Background

Based on analysis of II (Intelligent Internet) materials provided on 2026-06-06:
- CommonGround Kernel: durable work records
- psql_bm25s: low-cost retrieval of accumulated state
- RALPH/Zenith: harness loops preventing premature completion
- II-Thought: data quality and verifiability
- II-Researcher: research pipeline with query evaluation
- Common Ground: human-in-the-loop workspace
- Master Plan: sovereign AI and open knowledge
- II-Search: multi-step search behavior

The goal is to transform `feline-research-os` from a Streamlit Q&A tool into a **Research OS** - a system where every research task generates retrievable, verifiable, inheritable records.

## What This Plan Delivers

1. **ARCHITECTURE.md** - Six-layer architecture documentation
2. **Research Record Schema** - Durable task records (not just answers)
3. **Evidence Card Schema** - Structured knowledge units with species/evidence tagging
4. **Harness Loop (Feline-RALPH)** - Draft → gap_check → revision → verification
5. **Search Depth Controller** - Prevent tool laziness
6. **Query Evaluation** - Freshness/Plurality/Completeness/Species-specificity
7. **Agent Roles** - Strategist/Coordinator/Associates/Verifier (YAML-configurable)
8. **Benchmark Questions** - 20 initial test questions for regression

## Implementation Strategy

### Phase 1: Infrastructure Foundation

**Tasks:**
1. Create `core/` directory structure
2. Implement Research Record persistence (`core/record_store.py`)
3. Implement Evidence Card schema (`core/evidence_card.py`)
4. Create task evaluator (`core/task_evaluator.py`)

**Files:**
- `/core/__init__.py`
- `/core/record_store.py`
- `/core/evidence_card.py`
- `/core/task_evaluator.py`
- `/core/schemas.py`

### Phase 2: Harness Loop

**Tasks:**
1. Implement gap checker (`core/gap_checker.py`)
2. Implement verifier (`core/verifier.py`)
3. Create harness loop controller

**Verifier Checkpoints:**
- Species boundary check
- Evidence source citation check
- Endpoint type distinction check
- Protocol completeness check (for design tasks)

### Phase 3: Search Depth Control

**Tasks:**
1. [x] Implement search depth controller (`core/search_depth_controller.py`)
2. [x] Add minimum observable retrieval requirements by task type
3. [x] Integrate the contract with the Harness Loop and Streamlit query result
4. [x] Record unmet contracts as `needs_human_review` without blocking answers

**Depth Rules:**
- Quick: 0-1 searches
- Standard: 2-3 sources, 2+ source types
- Deep: 2+ rounds with gap reflection
- Evidence Audit: must include contrary evidence

### Phase 4: Research Console Integration

**Tasks:**
1. Add Research Record view to Streamlit
2. Add Harness Loop visualization
3. Add Verifier status display
4. Add benchmark question runner

## Relationship to Codex Work

This plan is designed to **run in parallel** with Codex development:

| This Plan (Claude) | Codex Potential Focus |
|-------------------|----------------------|
| ARCHITECTURE.md | Agent profile YAML definitions |
| Core schemas | Prompt engineering for agents |
| Harness loop logic | Visual direction exploration |
| Benchmark questions | Evidence Card examples |

**Merge Strategy:**
- Both branches work on separate layers
- Core schemas are the integration point
- Research Record and Evidence Card formats must align
- Agent profiles can be developed in parallel

## Constraints

- No breaking changes to existing app.py functionality
- Extend existing source card frontmatter, don't replace
- Models remain replaceable (no model-specific code)
- All new code goes in `/core/` initially

## Success Criteria

1. ARCHITECTURE.md documents complete six-layer architecture
2. Research Record schema implemented and tested
3. Evidence Card schema extends existing source cards
4. At least one harness loop path working in Research Console
5. Search depth controller enforces minimum search for complex tasks
6. 20 benchmark questions documented

## Decision Audit Trail

| # | Decision | Rationale | Principle |
|---|----------|-----------|-----------|
| 1 | Extend source cards rather than replace | Preserve existing 100+ source cards | Backwards compatibility |
| 2 | Core logic in `/core/` not Streamlit | Separation of concerns | Clean architecture |
| 3 | YAML agent profiles | Configurable without code changes | Flexibility |
| 4 | Species verification as hard requirement | Domain-specific safety | Feline-specific value |
| 5 | Harness loop for complex tasks only | Avoid overhead on simple queries | Pragmatic |

## Risks

1. **Scope creep** - The II materials are comprehensive; must focus on MVP
2. **Codex conflict** - Need clear layer separation for parallel work
3. **Performance** - Harness loop adds latency; must be opt-in for complex tasks
4. **Adoption** - Existing users expect current behavior; gradual migration needed

## Open Questions

Resolved:

1. Research Records use JSON as the machine record plus generated Markdown for
   human review.
2. Research Records remain separate from `outputs/qa/`; the record may reference
   an output path rather than replacing the output artifact.
3. YAML agent profiles are deferred. The later business-critical Autoplan
   explicitly excludes adding an agent framework before a repeated workflow is
   proven.
4. Partial verification maps to `needs_human_review`; critical failures map to
   `failed`.

---

## GSTACK REVIEW REPORT

| Review | Status | Notes |
|--------|--------|-------|
| CEO Review | SUPERSEDED | Covered by the 2026-06-06 business-critical Autoplan and human-authority boundary |
| Design Review | SUPERSEDED | Research Cases design review defines the current primary workflow |
| Eng Review | PASS_WITH_FOLLOW_UP | Core records, harness, verifier, benchmark, and search-depth contract are implemented |
| DX Review | N/A | Internal tool, no external developer experience |

## Implementation Reality: 2026-06-11

Completed:

- `core/` Research Record, Evidence Card, TaskEvaluator, GapChecker, Verifier,
  and SearchDepthController;
- JSON and Markdown record persistence;
- Streamlit Research Records workspace;
- query-result Harness integration;
- 20-question benchmark;
- search-depth contracts for Quick, Standard, Deep, and Evidence Audit;
- Evidence Audit classification priority for explicit review/verification asks.

The SearchDepthController verifies actual execution rather than trusting the
assigned label. It checks evidence count, retrieval rounds, source-family
plurality, gap reflection, and counterevidence for audit tasks.

Verification completed without paid APIs:

- `python3 core/test_harness_loop.py` — PASS;
- `python3 scripts/benchmark_runner.py` — 20/20;
- `python3 scripts/test_query.py` — 111/111;
- Python compilation and `git diff --check` — PASS.

Remaining work is product validation, not missing MVP infrastructure:

- exercise the workflow with real users and repeated research cases;
- improve trace semantics if external retrieval is enabled;
- bulk Evidence Card conversion only when a concrete retrieval use case requires
  it;
- keep YAML agent profiles deferred until role configuration solves a measured
  problem.
