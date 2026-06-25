# Handoff: Source-Grounded Research Workspace

Date: 2026-06-25
Branch: main
Commit: `47b3428`
Classification: UI/UX Simplification + Evidence Trace Infrastructure

## What Shipped

Phase 1-3 of the Source-Grounded Research Workspace plan is complete and pushed to remote.

### Phase 1: Homepage Radical Simplification

**Before:**
- Verbose title: "证据研究工作台"
- 5+ content blocks on homepage: disease topics, history, provenance guide, how it works, stats
- Mode labels: "快速问" / "深度研究"

**After:**
- Minimal title: "今天想研究什么？"
- Only 3 elements on main area: title + input + mode buttons + example chips
- Mode labels: "快速解释" / "深度研究" (symmetric naming)
- Secondary content moved to sidebar or removed entirely

**User Feedback Source:** `/Users/jiawei/Desktop/还是太复杂.md`

Core principle from user feedback:
> 首页应该像 agent.ii.inc / research agent 的入口，而不是像知识库 dashboard。
> Homepage should be a "research question input box", not a "system introduction page".

### Phase 2: Result Page Conclusion-First Structure

**Before:** 5-tab layout
- 任务摘要
- 证据地图
- 核心发现
- 模型与药效评价价值
- 缺口与下一步

**After:** Conclusion-first with expanders
- 直接结论 (displayed directly, not in expander)
- 依据哪些文献 (expander)
- 对模型与药效评价有什么用 (expander)
- 还不确定什么 (expander)
- 检索范围 (expander, collapsed by default)

### Phase 3: Evidence Trace Infrastructure

Added `EvidenceTrace` dataclass for claim-level source passage tracing:

```python
@dataclass
class EvidenceTrace:
    trace_id: str
    claim_id: str
    claim_text: str
    source_id: str
    source_title: str
    evidence_type: str  # quoted_fact, source_supported_conclusion, llm_inference
    evidence_label: str  # 直接来源, 来源支持, 分析推断
    quoted_passage: str
    highlight_text: str
    canonical_url: str = ""
    section: str = ""
```

Added source metadata parsing for evidence snippets:
- `quoted_facts` - direct quotes from source
- `supported_conclusions` - source-supported conclusions
- `llm_inferences` - model inferences requiring review

## Files Modified

| File | Changes |
|------|---------|
| `scripts/app.py` | EMPTY_STATE_INTRO_HTML simplified, render_empty_state() reduced to 2 calls, render_evidence_traces_v2() added |
| `scripts/workspace_tabs.py` | 5-tab → conclusion-first expanders |
| `core/result_presentation.py` | EvidenceTrace dataclass, build_evidence_traces_from_text() |
| `core/source_metadata.py` | nested_frontmatter_list(), frontmatter_text() for YAML parsing |
| `scripts/research_mode.py` | Minor import adjustments |
| `scripts/test_result_presentation.py` | 14 tests, all passing |
| `PLAN-source-grounded-research-workspace.md` | Full plan document |

## What's NOT Shipped (Phase 4)

**Phase 4: Paper Card Passage Library** - Deferred

This phase would add optional `source_passages` support to deep extraction cards:

```yaml
source_passages:
  - passage_id: p-abstract-001
    section: Abstract
    quoted_passage: "..."
    highlight_text: "..."
    supports_claim_types:
      - model_evaluation
    evidence_type: quoted_fact
```

Not critical for current usage. Existing cards work without passage libraries.

## Verification

### Quick Check

```bash
cd /Users/jiawei/Desktop/insclaude/feline-research-os
source .venv/bin/activate
PYTHONPATH=. python3 scripts/test_result_presentation.py
# Expected: 14/14 PASS
```

### Visual Check

```bash
.venv/bin/streamlit run scripts/app.py --server.port 8503
# Open http://localhost:8503
# Verify:
# 1. Homepage shows "今天想研究什么？" (not "证据研究工作台")
# 2. Only title + input + modes + examples on main area
# 3. Click "解释CKD" → result shows conclusion first
```

## Design Decisions

1. **Homepage as input box, not dashboard** - Following user feedback, removed all explanatory content from first viewport

2. **Symmetric mode labels** - Changed "快速问" to "快速解释" for symmetry with "深度研究"

3. **Conclusion-first results** - User sees the answer immediately, details are in expanders

4. **Evidence trace in presentation layer** - Traces attached to ResultPresentation, not persisted records (safer migration path)

5. **No internal ID exposure** - `src-*` IDs never shown to readers, only human-readable titles

## Related Documents

- Plan: `PLAN-source-grounded-research-workspace.md`
- User feedback: `/Users/jiawei/Desktop/还是太复杂.md`
- Design system: `DESIGN.md` (dark utilitarian, preserved)

## Screenshots Reference

Homepage simplified:
- `/tmp/feline-homepage-simplified.png` (captured during QA)

Result page (CKD explanation):
- `/tmp/feline-result-ckd.png` (captured during QA)

## Next Steps (If Continuing This Line)

1. **Phase 4 (optional):** Add passage library support to deep extraction cards
2. **Evidence trace UI:** Add "查看原文依据" buttons next to claim chips when trace data exists
3. **Highlight rendering:** Yellow mark for `highlight_text` inside `quoted_passage`
4. **Inference warning:** Show "需要人工复核" for `分析推断` type claims

## Do Not Regress To

- Adding explanatory panels back to homepage main area
- Using 5-tab result structure
- Exposing `src-*` IDs in reader-facing text
- Treating "证据研究工作台" as the product name (it's "今天想研究什么？" now)
