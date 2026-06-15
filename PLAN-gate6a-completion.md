<!-- /autoplan restore point: /Users/jiawei/.gstack/projects/feline-research-os/idea-chatacademia-research-workbench-autoplan-restore-20260615-142823.md -->

# Plan: Gate 6A Completion — RetrievalEvent Integration & Explicit-Save UI

**Status:** READY_FOR_REVIEW
**Branch:** `idea-chatacademia-research-workbench`
**Created:** 2026-06-15
**Design Doc:** N/A (implementation phase of approved Phase 6)
**Prerequisites:** Schema v2, RecordStore enhancements (COMPLETE)

## What Was Built (Complete)

Gate 6A core infrastructure is already implemented and tested:

### core/schemas.py (v2)

| Schema | Purpose |
|--------|---------|
| `SCHEMA_VERSION = 2` | Forward-compatible migrations |
| `RetrievalEvent` | Tracks actual search events (truthful scope) |
| `SourceSnapshot` | Captures source metadata at retrieval time with fingerprint |
| `ResearchClaim` | Unit of selection, validation, promotion (Gate 6B) |
| `PromotionStatus` | `record_only → candidate → validated → promoted → rejected` |
| `FreshnessStatus` | `current → stale → superseded` |
| `ClaimProvenance` | `quoted_fact`, `source_supported_conclusion`, `inference` |

### core/record_store.py

| Feature | Purpose |
|---------|---------|
| Commit manifest | SHA-256 hashes for JSON and Markdown after successful dual-write |
| `verify_record_integrity()` | Checks manifest hashes match file contents |
| Reconciliation queue | Tracks interrupted writes for recovery |
| `list_reconciliation_queue()` | Lists pending reconciliation entries |
| Atomic writes | POSIX temp file + fsync + rename pattern |
| Path containment | Prevents path traversal attacks |

### Test Coverage

```
python3 scripts/test_query.py           → 113 passed
PYTHONPATH=. python3 core/test_harness_loop.py → All tests passed
PYTHONPATH=. python3 scripts/test_research_record_store.py → All tests passed
PYTHONPATH=. python3 scripts/test_claim_promotion.py → All tests passed
PYTHONPATH=. python3 scripts/test_validated_claim_store.py → All tests passed
```

## What Remains (This Plan)

### Task 1: Wire RetrievalEvent into Query Flow

**Files:** `scripts/query.py`, `scripts/app.py`

In `scripts/query.py`:
- After vault search executes, create `RetrievalEvent` with:
  - `engine`: "vault" or "pubmed" or "crossref"
  - `query`: actual query string executed
  - `scope`: "raw/papers", "topics", "indexes"
  - `candidate_count`: total results before filtering
  - `retained_ids`: source IDs kept for synthesis
  - `excluded_ids`: source IDs filtered out
  - `filters_applied`: list of filter names applied
- Return retrieval events as part of query result

In `scripts/app.py`:
- Receive retrieval events from query flow
- Display "Sources searched" panel showing:
  - Which engines were queried
  - How many candidates found
  - How many retained vs excluded
  - What filters were applied
- This is the "truthful scope" requirement: never claim searches that didn't happen

### Task 2: Wire SourceSnapshot into Query Flow

**Files:** `scripts/query.py`, `core/source_metadata.py`

In `scripts/query.py`:
- For each retained source, create `SourceSnapshot` with:
  - `content_fingerprint`: SHA-256 of source card content
  - Metadata fields from `source_metadata.py` resolver
  - Quality dimensions (source_family, species, extraction_depth, verification_status)
  - Claim-fit policy (safe_claim_types, prohibited_claim_types, decision_grade)
- Attach snapshots to the transient Research Record

This enables:
- Presentation: translate source IDs to user-facing labels
- Validation: check claim-fit before promotion
- Freshness: fingerprint comparison for stale detection

### Task 3: Build Explicit-Save UI

**Files:** `scripts/app.py`

Current state: Query completion creates a transient Research Record. User can discard or save.

New UI elements:
1. **Save Research Record button** — visible after query completion
2. **Title input** — user-editable record title (default: first 50 chars of request)
3. **Duplicate check** — if equivalent record exists, show warning with options:
   - Save as new version (increment `record_version`)
   - Update existing record
   - Cancel
4. **Save confirmation** — show record ID and verification status

### Task 4: Display Retrieval Events in UI

**Files:** `scripts/app.py`

Add expandable "Query Scope" section showing:
- Retrieval events (what was searched)
- Source snapshots (what was found)
- Filters applied
- Excluded sources with reasons

This makes the research process transparent (II-Agent reference pattern).

## Architecture Diagram

```
Query Submission
    │
    ▼
router_call() + hop_call()
    │
    ▼
RetrievalEvent[] ← NEW: track actual search events
    │
    ▼
build_source_index() → loaded source IDs
    │
    ▼
SourceSnapshot[] ← NEW: capture metadata at retrieval time
    │
    ▼
synthesis_call() → answer with provenance
    │
    ▼
HarnessLoop.finalize_record() → Transient ResearchRecord (zero persistence)
    │
    ├── Cancel → discard
    │
    └── explicit Save → RecordStore.save()
                            │
                            ├── JSON + hash
                            ├── Markdown + hash
                            └── Commit manifest
```

## Integration Sequence Diagram (Added per /autoplan review)

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  app.py     │    │  query.py   │    │harness_loop │    │record_store │
└──────┬──────┘    └──────┬──────┘    └──────┬──────┘    └──────┬──────┘
       │                  │                  │                  │
       │ run_query_core() │                  │                  │
       │─────────────────>│                  │                  │
       │                  │                  │                  │
       │                  │ vault_search()   │                  │
       │                  │─────────────┐    │                  │
       │                  │             │    │                  │
       │                  │<────────────┘    │                  │
       │                  │                  │                  │
       │                  │ CREATE RetrievalEvent               │
       │                  │ (engine, query, scope,              │
       │                  │  candidate_count, retained_ids,     │
       │                  │  excluded_ids, filters_applied)     │
       │                  │                  │                  │
       │                  │ try_load_source()│                  │
       │                  │─────────────┐    │                  │
       │                  │             │    │                  │
       │                  │<────────────┘    │                  │
       │                  │                  │                  │
       │                  │ CREATE SourceSnapshot               │
       │                  │ (source_id, content_fingerprint,    │
       │                  │  title, source_family, species...)  │
       │                  │                  │                  │
       │ result dict with │                  │                  │
       │ retrieval_events │                  │                  │
       │ source_snapshots │                  │                  │
       │<─────────────────│                  │                  │
       │                  │                  │                  │
       │ finalize_record(retrieval_events,   │                  │
       │                  source_snapshots)  │                  │
       │─────────────────────────────────────>                  │
       │                  │                  │                  │
       │                  │ Transient ResearchRecord            │
       │<─────────────────────────────────────                  │
       │                  │                  │                  │
       │ [User clicks Save]                  │                  │
       │                  │                  │                  │
       │                  │                  │ save(record)     │
       │─────────────────────────────────────────────────────────>
       │                  │                  │                  │
       │                  │                  │ Path + manifest  │
       │<─────────────────────────────────────────────────────────
       │                  │                  │                  │
```

**Key integration points:**

1. **RetrievalEvent creation:** In `run_query_core()` immediately after `vault_search()` or `external_search()` returns
2. **SourceSnapshot creation:** In `try_load_source()` when computing `context_parts`, store fingerprint alongside
3. **Parameter passing:** Add `retrieval_events: List[RetrievalEvent]` and `source_snapshots: List[SourceSnapshot]` to `finalize_record()` signature
4. **Return contract:** `run_query_core()` returns `{"retrieval_events": [...], "source_snapshots": [...], ...}`

## UI State Table (Added per /autoplan review)

### Save Flow States

| State | Trigger | UI Response | Next State |
|-------|---------|-------------|------------|
| `idle` | Default after query completion | Save button enabled, no message | — |
| `saving` | User clicks Save | Button shows spinner, text "保存中... / Saving..." | success/error/duplicate |
| `success` | Save completes | Green toast "已保存: {record_id} / Saved: {record_id}", button changes to "已保存 ✓ / Saved ✓" | idle (for new query) |
| `duplicate_warning` | Equivalent record found | Amber alert above button with 2 options | idle/saving |
| `error` | Exception during save | Red toast with error message, button re-enabled | idle |
| `disabled` | No transient record exists | Button grayed out, tooltip "完成查询后可保存 / Complete a query to save" | — |

### Duplicate Warning Options

When equivalent record exists:
1. Display amber warning: "已存在类似记录: {record_id} ({date}) / Similar record exists: {record_id} ({date})"
2. Show "查看已有记录 / View existing" link (scrolls to record browser)
3. Save button changes to "保存为新版本 / Save as New Version"

### Query Scope Panel States

| State | Trigger | UI Response |
|-------|---------|-------------|
| `collapsed` | Default | Summary line visible: "搜索了 3 个引擎，42 候选 → 8 保留 / Searched 3 engines, 42 candidates → 8 retained" |
| `expanded` | User clicks header | Full breakdown: retrieval events, source snapshots, filters, excluded sources |
| `empty` | Zero retrieval events | Warning: "未执行搜索 / No search executed" |

## Bilingual Label Table (Added per /autoplan review)

### Task 3: Save UI Labels

| Element | Chinese | English |
|---------|---------|---------|
| Save button | 保存研究记录 | Save Research Record |
| Save button (saved state) | 已保存 ✓ | Saved ✓ |
| Save button (saving state) | 保存中... | Saving... |
| Title input label | 记录标题 | Record Title |
| Title input placeholder | 输入标题或使用默认 | Enter title or use default |
| Duplicate warning | 已存在类似记录 | Similar record exists |
| View existing link | 查看已有记录 | View existing |
| Save as new version | 保存为新版本 | Save as New Version |
| Success message | 已保存 | Saved |
| Error message | 保存失败 | Save failed |

### Task 4: Query Scope Labels

| Element | Chinese | English |
|---------|---------|---------|
| Panel title | 搜索范围 | Search Coverage |
| Summary pattern | 搜索了 {n} 个引擎，{m} 候选 → {k} 保留 | Searched {n} engines, {m} candidates → {k} retained |
| Retrieval events header | 检索事件 | Retrieval Events |
| Source snapshots header | 来源快照 | Source Snapshots |
| Excluded sources header | 已排除 | Excluded |
| Filters applied | 已应用过滤器 | Filters Applied |
| Engine label | 搜索引擎 | Search Engine |
| Candidates | 候选结果 | Candidates |
| Retained | 保留 | Retained |
| vault engine | 本地知识库 | Local Vault |
| pubmed engine | PubMed | PubMed |
| crossref engine | CrossRef | CrossRef |

## UI Wireframe (Added per /autoplan review)

```
┌─────────────────────────────────────────────────────────────────┐
│  [Answer with provenance badges]                                │
│  ────────────────────────────────────────────────────────────── │
│                                                                 │
│  [Evidence Profile v2 panel]                                    │
│  ────────────────────────────────────────────────────────────── │
│                                                                 │
│  ▶ 搜索范围 / Search Coverage                          [NEW]   │
│    "搜索了 2 个引擎，45 候选 → 6 保留"                          │
│  ────────────────────────────────────────────────────────────── │
│                                                                 │
│  [Sources Section v2 - existing cards]                          │
│  ────────────────────────────────────────────────────────────── │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  记录标题 / Record Title                                 │   │
│  │  ┌─────────────────────────────────────────────────────┐│   │
│  │  │ CKD早期检测生物标志物研究...                          ││   │
│  │  └─────────────────────────────────────────────────────┘│   │
│  │                                                         │   │
│  │  [⚠ 已存在类似记录: rr-20260610... / View existing]     │   │
│  │                                                         │   │
│  │  [ 保存为新版本 / Save as New Version ]                  │   │
│  └─────────────────────────────────────────────────────────┘   │
│  ────────────────────────────────────────────────────────────── │
│                                                                 │
│  ▶ 专家评审 / Expert Review (expandable)                       │
└─────────────────────────────────────────────────────────────────┘
```

## Constraints

- **No automatic persistence** — Records only saved on explicit user action
- **Pure harness finalization** — `finalize_record()` performs zero I/O
- **OpenRouter $1/day** — Budget cap required for live acceptance tests
- **Backward compatibility** — v1 records load correctly with defaults

## Success Criteria

1. `RetrievalEvent` created for every vault/pubmed/crossref search
2. `SourceSnapshot` created for every retained source
3. UI shows "Query Scope" with retrieval events and source snapshots
4. Explicit "Save Research Record" button functional
5. Duplicate check warns before creating equivalent records
6. All tests continue to pass (113+)
7. No regression in presentation layer

## Files to Modify

| File | Changes |
|------|---------|
| `scripts/query.py` | Add RetrievalEvent/SourceSnapshot creation |
| `scripts/app.py` | Add Query Scope panel, explicit-save UI |
| `core/source_metadata.py` | Ensure all fields available for SourceSnapshot |

## Files to Create

None — all required modules exist.

## Deferred to Gate 6B

- Claim selection UI
- Promotion validation
- Target selection

## Deferred to Gate 6C

- Human-confirmed patch application
- Promotion manifest
- Stale-dependency queue
- Validated-claim retrieval channel

---

## Phase 1: CEO Review (/autoplan)

### Premises Confirmed

| Premise | Status |
|---------|--------|
| Explicit save over auto-save | CONFIRMED |
| Traceability is core value | CONFIRMED |
| RetrievalEvent/SourceSnapshot infrastructure for 6B/6C | CONFIRMED |
| Bilingual UI required | CONFIRMED |

### CEO Dual Voices

**CLAUDE SUBAGENT (CEO — strategic independence):**

| Finding | Severity | Fix |
|---------|----------|-----|
| Plan emphasizes infrastructure over user-facing value | Medium | Lead with Task 4 UI; add user stories |
| Integration point (`finalize_record`) underspecified | High | Add sequence diagram |
| No success metrics defined | High | Define quantitative criteria |
| Alternatives not analyzed | Medium | Add "Considered Alternatives" section |
| Bilingual UI requirements not mentioned | Medium | Add to Task 3/4 specs |

**CODEX SAYS:** Unavailable [usage limit exceeded]

```
CEO DUAL VOICES — CONSENSUS TABLE:
═══════════════════════════════════════════════════════════════
  Dimension                           Claude  Codex  Consensus
  ──────────────────────────────────── ─────── ─────── ─────────
  1. Premises valid?                   PARTIAL N/A    [subagent-only]
  2. Right problem to solve?           YES     N/A    [subagent-only]
  3. Scope calibration correct?        PARTIAL N/A    [subagent-only]
  4. Alternatives sufficiently explored? NO    N/A    [subagent-only]
  5. Competitive/market risks covered? YES     N/A    [subagent-only]
  6. 6-month trajectory sound?         PARTIAL N/A    [subagent-only]
═══════════════════════════════════════════════════════════════
```

### CEO Auto-Decisions

| # | Decision | Principle | Rationale |
|---|----------|-----------|-----------|
| 1 | Add bilingual labels to Task 3/4 | P1 (completeness) | Recent commits show bilingual work; UI must match |
| 2 | Add sequence diagram for integration points | P5 (explicit) | Current spec too vague on where events created |
| 3 | Add success metrics | P1 (completeness) | Cannot measure value without metrics |

**Phase 1 complete.** Claude subagent: 5 findings. Codex: unavailable. Passing to Phase 2.

---

## Phase 2: Design Review (/autoplan)

### CLAUDE SUBAGENT (Design — UX independent review)

| Finding | Severity | Fix |
|---------|----------|-----|
| Information hierarchy completely unspecified | CRITICAL | Add wireframe showing element placement |
| Missing state specifications (loading, error, success) | HIGH | Add state table for save flow |
| User journey has emotional dead ends (Query Scope rationale) | HIGH | Frame as user benefit "Search Coverage" |
| Duplicate check UX ambiguous | MEDIUM | Simplify to 2 paths |
| Bilingual labels missing from Task 3/4 | MEDIUM | Add label mapping table |
| Query Scope panel layout not specified | MEDIUM | Add layout specification |
| Integration with existing harness loop UI unclear | MEDIUM | Add integration notes |
| SourceSnapshot display not designed | MEDIUM | Add display spec |
| Title input default behavior underspecified | LOW | Specify smart truncation |
| Success criteria are developer-facing only | LOW | Add user-facing criteria |

### Design Auto-Decisions

| # | Decision | Principle | Rationale |
|---|----------|-----------|-----------|
| 4 | Add wireframe for UI layout | P5 (explicit) | Implementer needs placement guidance |
| 5 | Add bilingual label table | P1 (completeness) | System is bilingual |
| 6 | Simplify duplicate check to 2 paths | P5 (explicit) | Fewer options = clearer UX |

**Phase 2 complete.** Claude subagent: 10 findings. Passing to Phase 3.

---

## Phase 3: Eng Review (/autoplan)

### CLAUDE SUBAGENT (Eng — architecture review)

| Finding | Severity | Fix |
|---------|----------|-----|
| Missing integration contract for `finalize_record()` | HIGH | Add explicit parameters and sequence diagram |
| `run_query_core()` returns untyped dict | MEDIUM | Define typed return with retrieval events |
| Fingerprint computation timing unclear | MEDIUM | Track fingerprints during source load |
| `find_equivalent_record()` scans all records | LOW | Add TODO for index in Gate 6D |
| Empty `retained_ids` and exclusion tracking | MEDIUM | Allow empty, document exclusion deferral |
| Concurrent save race condition | MEDIUM | Add optimistic locking on `record_version` |
| Manifest not verified on load | LOW | Add optional `verify_on_load` |
| Reconciliation queue never processed | MEDIUM | Add reconciliation logic to plan |
| No integration test for full query-to-save flow | HIGH | Add `test_gate6a_integration.py` |
| No test for duplicate detection UI | MEDIUM | Add UI flow tests |
| No test for partial write recovery | MEDIUM | Add failure injection tests |
| Path traversal in `RetrievalEvent.query` | LOW | Sanitize or document as untrusted |
| Fingerprint excludes metadata | LOW | Document or include metadata |
| Bilingual UI labels missing | MEDIUM | Add label mapping |
| `SourceSnapshot` fields not in parser | MEDIUM | Extend parser or mark optional |
| `app.py` modifications not scoped | LOW | Add wireframe/session state schema |

### Eng Auto-Decisions

| # | Decision | Principle | Rationale |
|---|----------|-----------|-----------|
| 7 | Add integration test | P1 (completeness) | Critical path must be tested |
| 8 | Add sequence diagram for data flow | P5 (explicit) | Current spec too vague |
| 9 | Mark SourceSnapshot claim-fit fields as optional | P3 (pragmatic) | Gate 6B will populate |

**Phase 3 complete.** Claude subagent: 16 findings. Passing to Phase 3.5.

---

## Phase 3.5: DX Review (/autoplan)

### CLAUDE SUBAGENT (DX — developer experience review)

| Finding | Severity | Fix |
|---------|----------|-----|
| 6+ step setup to hello world | HIGH | Add quickstart script |
| No Python version validation | MEDIUM | Add preflight check |
| Inconsistent `generate_id()` across schemas | MEDIUM | Add ID to SourceSnapshot |
| Path vs str type hint ambiguity | MEDIUM | Update type hint |
| No CLI for record operations | HIGH | Add `scripts/records.py` |
| Generic exceptions without actionable context | CRITICAL | Define RecordStoreError hierarchy |
| Path traversal error lacks context | HIGH | Add specific error message |
| Silent failure on malformed records | MEDIUM | Add `strict` parameter |
| No copy-paste examples in schemas | HIGH | Add docstring examples |
| README mixes audiences | MEDIUM | Restructure by audience |
| Plan lacks integration sequence diagram | MEDIUM | Add sequence diagram |
| No schema version override for debugging | MEDIUM | Add `force_load` parameter |
| Atomic writes not configurable | LOW | Add `atomic_writes` parameter |

### DX Auto-Decisions

| # | Decision | Principle | Rationale |
|---|----------|-----------|-----------|
| 10 | Add docstring examples to v2 schemas | P1 (completeness) | Developers need copy-paste guidance |
| 11 | Defer CLI to Gate 6B | P6 (action) | Core functionality first |
| 12 | Add error context to path traversal | P5 (explicit) | Security errors need clarity |

**Phase 3.5 complete.** DX overall: 5/10. TTHW: ~6 min → target 3 min. Passing to Final Gate.

---

<!-- AUTONOMOUS DECISION LOG -->
## Decision Audit Trail

| # | Phase | Decision | Classification | Principle | Rationale |
|---|-------|----------|----------------|-----------|-----------|
| 1 | CEO | Add bilingual labels to Task 3/4 | Mechanical | P1 | Recent commits show bilingual work |
| 2 | CEO | Add sequence diagram for integration | Mechanical | P5 | Spec too vague |
| 3 | CEO | Add success metrics | Mechanical | P1 | Cannot measure value |
| 4 | Design | Add wireframe for UI layout | Mechanical | P5 | Implementer needs guidance |
| 5 | Design | Add bilingual label table | Mechanical | P1 | System is bilingual |
| 6 | Design | Simplify duplicate check to 2 paths | Taste | P5 | Fewer options = clearer UX |
| 7 | Eng | Add integration test | Mechanical | P1 | Critical path must be tested |
| 8 | Eng | Add sequence diagram | Mechanical | P5 | Spec too vague |
| 9 | Eng | Mark claim-fit fields optional | Mechanical | P3 | Gate 6B will populate |
| 10 | DX | Add docstring examples | Mechanical | P1 | Developers need guidance |
| 11 | DX | Defer CLI to Gate 6B | Mechanical | P6 | Core functionality first |
| 12 | DX | Add error context to path traversal | Mechanical | P5 | Security errors need clarity |

---

## Verification Commands

```bash
# Unit tests
python3 scripts/test_query.py
PYTHONPATH=. python3 scripts/test_research_record_store.py
PYTHONPATH=. python3 core/test_harness_loop.py

# Syntax check
python3 -m py_compile scripts/query.py scripts/app.py core/schemas.py core/record_store.py

# Local page verification
PORT=8514 scripts/run_test_page.sh

# Integration test (new, per Eng review)
PYTHONPATH=. python3 scripts/test_gate6a_integration.py
```

---

## GSTACK REVIEW REPORT

**Status:** APPROVED_WITH_MODIFICATIONS
**Date:** 2026-06-15
**Reviewer:** /autoplan (subagent-only mode, Codex unavailable)

### Summary

Gate 6A Completion plan approved with critical documentation additions:
- Integration sequence diagram (added)
- UI state table (added)
- Bilingual label mapping (added)
- UI wireframe (added)

### Review Statistics

| Phase | Findings | Critical | High | Auto-Decided |
|-------|----------|----------|------|--------------|
| CEO | 5 | 0 | 2 | 3 |
| Design | 10 | 1 | 2 | 3 |
| Eng | 16 | 0 | 2 | 3 |
| DX | 13 | 1 | 4 | 3 |
| **Total** | **44** | **2** | **10** | **12** |

### Cross-Phase Themes Addressed

1. **Integration sequence diagram** — ADDED
2. **Bilingual UI labels** — ADDED
3. **Error handling** — DEFERRED to implementation (add RecordStoreError)

### Premises Confirmed

- Explicit save over auto-save: ✓
- Traceability is core value: ✓
- RetrievalEvent/SourceSnapshot for 6B/6C: ✓
- Bilingual UI required: ✓

### Next Steps

1. Implement Task 1: Wire RetrievalEvent into query flow (per sequence diagram)
2. Implement Task 2: Wire SourceSnapshot into query flow
3. Implement Task 3: Build explicit-save UI (per wireframe and state table)
4. Implement Task 4: Display Query Scope panel
5. Add `test_gate6a_integration.py`
6. Run full test suite before merge
