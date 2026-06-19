# HANDOFF: P3 Reference Graph Implementation

**Date:** 2026-06-17
**Branch:** idea-chatacademia-research-workbench
**Status:** COMPLETE

---

## Summary

P3 Reference Graph from `PLAN-researcher-presentation-layer.md` is now complete:
- **Task 3.1**: Reference link display with vault status indicators
- **Task 3.2**: Citation graph index (`system/indexes/citation-graph.json`)
- **Task 3.3**: "Cited By" display showing papers that cite the current paper

---

## What Was Built

### 1. Citation Graph Index (`system/indexes/citation-graph.json`)

New index file tracking paper-to-paper citation relationships:

```json
{
  "version": "1.0",
  "last_updated": "2026-06-17",
  "description": "Citation graph tracking which papers cite which other papers in the vault",
  "papers": {
    "src-ckd-004": {
      "title": "ISFM Consensus Guidelines...",
      "year": 2016,
      "citation_count": 161,
      "cites": [],
      "cited_by": ["src-ckd-010", "src-ckd-011", "src-ckd-024"],
      "cites_external": []
    }
  },
  "stats": {
    "total_papers_indexed": 4,
    "total_internal_citations": 4,
    "papers_with_cites": 3,
    "papers_with_cited_by": 1
  }
}
```

**Note:** The graph currently contains seed data for 4 CKD papers. Additional papers will be populated during deep extraction.

### 2. Citation Graph Query Functions (`scripts/query.py`)

New functions added after line 247:

| Function | Purpose |
|----------|---------|
| `load_citation_graph()` | Load and cache citation graph from disk |
| `get_paper_citations(source_id)` | Get citation info for a paper (cites, cited_by, external) |
| `get_citation_summary(source_id)` | Human-readable summary ("被引: 161 \| 引用库内: 3") |
| `get_reference_links(source_id)` | Reference links for UI with vault status |
| `get_cited_by_links(source_id)` | Papers that cite this paper, sorted by citation count |

### 3. Enhanced Source Card UI (`scripts/app.py`)

Updated `render_source_card_v2()` with:

1. **4-button expander layout** (lines 2908-2936):
   - 📄 摘要/Abstract
   - 🔬 方法/Methods
   - 📚 参考文献/References
   - 🔗 被引用/Cited By (NEW)

2. **Reference display with vault status** (lines 2950-2980):
   - ✓ 库内 (green badge) - paper is in vault
   - ✗ 未收录 (red badge) - external reference

3. **Cited By display** (lines 2983-2999):
   - Shows papers that cite the current paper
   - Displays citation count badge
   - Sorted by citation count (most cited first)
   - Orange accent color (#f59e0b)

---

## Test Page

**URL:** http://localhost:8501

**How to test P3 features:**

1. Ask a CKD question (e.g., "解释CKD" or "what is feline CKD")
2. Look at the source cards in the results
3. For papers in the citation graph (like src-ckd-004):
   - Click "📚 参考文献" to see references with vault status
   - Click "🔗 被引用" to see citing papers with citation counts

**Example paper to test:** ISFM Consensus Guidelines (src-ckd-004)
- Has 3 papers that cite it: src-ckd-010, src-ckd-011, src-ckd-024
- Citation count: 161

---

## Files Changed

| File | Changes |
|------|---------|
| `system/indexes/citation-graph.json` | NEW - Citation graph index with seed data |
| `scripts/query.py` | +80 lines - Citation graph functions |
| `scripts/app.py` | +25 lines - "Cited By" button and display |

---

## Tests

All tests pass: **127/127**
- 113 query tests
- 4 research mode tests
- 10 intent classification tests

---

## What's Next

1. **Deep Extraction Integration**: During paper deep extraction, populate `cites` and `cites_external` fields by parsing reference sections
2. **Expand Citation Graph**: Add more papers to the graph as they are processed
3. **Citation Network Visualization**: Future enhancement to visualize citation relationships

---

## Verification Commands

```bash
# Check syntax
python3 -m py_compile scripts/app.py scripts/query.py

# Run tests
python3 scripts/test_query.py

# Verify citation graph exists
cat system/indexes/citation-graph.json | python3 -m json.tool

# Start app
streamlit run scripts/app.py --server.port 8501
```

---

## Related Documents

- Plan: `PLAN-researcher-presentation-layer.md` (P3 Reference Graph section)
- Design doc: `~/.gstack/projects/feline-research-os/idea-chatacademia-research-workbench-design-20260617.md`
- QA report: `.gstack/qa-reports/qa-report-localhost-2026-06-17.md`
