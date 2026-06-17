# Researcher Presentation Layer Plan

Date: 2026-06-16
Branch: idea-chatacademia-research-workbench
Trigger: User behavior path review + internal researcher feedback
Status: P1 complete, P3 pending, P4 complete (decision tree UI)

## Problem

The current presentation layer does not match how researchers actually work with literature:

1. **No Impact Factor display** — researchers filter by IF first
2. **No citation count** — high-cited papers should rank higher
3. **No Abstract/Methods visibility** — researchers scan these before reading full text
4. **No Reference links** — references are key discovery paths
5. **No sorting controls** — researchers want to sort by IF/citations/year
6. **Broad question handling** — system accepts questions passively, no intent clarification
7. **Research trace hidden** — retrieval decisions buried in sidebar expander

## User Behavior Path (from internal researcher feedback)

```
明确需求 → 查询近几年文献 → 按影响因子筛选 → 优先阅读高IF文献
    ↓
阅读时关注：Abstract / Method
    ↓
参考文献(References)作为延伸阅读线索
    ↓
高被引文献获得更高权重
    ↓
正文中的引用标记关联到参考文献
```

## Current State

| Field | Data Layer | Presentation | Researcher Need |
|-------|------------|--------------|-----------------|
| `journal` | ✓ exists | SourceDisplay | required |
| `publication_year` | ✓ exists | source card | required |
| `doi`/`pmid`/`pmcid` | ✓ exists | linkable | required |
| `authors` | ✓ exists | SourceDisplay | secondary |
| `evidence_level` | ✓ exists | translated label | required |
| **`impact_factor`** | ✗ missing | none | **critical** |
| **`citation_count`** | ✗ missing | none | **critical** |
| **`abstract`** | △ partial | key_findings substitute | **critical** |
| **`methods`** | ✗ missing | none | critical |
| **`references`** | ✗ missing | none | **critical** |

## Implementation Tasks

### Phase 1: Data Layer Enhancement (P1)

#### Task 1.1: Add metadata fields to SourceSnapshot schema

File: `core/schemas.py`

```python
# Add to SourceSnapshot dataclass
impact_factor: Optional[float] = None
citation_count: Optional[int] = None
abstract_text: str = ""
methods_summary: str = ""
reference_ids: List[str] = field(default_factory=list)
```

#### Task 1.2: Add metadata fields to SourceDisplay

File: `core/result_presentation.py`

```python
# Add to SourceDisplay dataclass
impact_factor: Optional[float] = None
impact_factor_label: str = ""  # e.g., "IF: 2.3"
citation_count: Optional[int] = None
citation_count_label: str = ""  # e.g., "被引: 847"
abstract_text: str = ""
methods_summary: str = ""
reference_ids: List[str] = field(default_factory=list)
```

#### Task 1.3: Create metadata enrichment skill

**This is repeatable work — must be skillified.**

Create: `.claude/skills/enrich-source-metadata/SKILL.md`

Purpose: Fetch IF and citation count from external APIs for source cards.

Data sources:
- **Citation count**: Semantic Scholar API (free, no auth required)
- **Impact Factor**: Scimago Journal Rank (free, scrape or local cache)

Manual sample run: 3-10 source cards before skillification.

#### Task 1.4: Source card frontmatter enrichment

Update source card markdown files to include new fields:

```yaml
---
# ... existing fields ...
impact_factor: 2.3
citation_count: 847
abstract: |
  Background: ...
  Methods: ...
  Results: ...
  Conclusions: ...
methods_summary: "Retrospective cohort study of 123 cats..."
references:
  - src-ckd-012
  - src-ckd-018
  - pmid:12345678  # external reference not in vault
---
```

### Phase 2: Presentation Layer (P1)

#### Task 2.1: Enhanced source card rendering

File: `scripts/app.py` or dedicated `render_source_card_v2()`

Display structure:
```
┌─────────────────────────────────────────────────────────┐
│ 📄 ISFM CKD Guidelines (2016)                           │
│ Journal of Feline Medicine and Surgery                  │
│ IF: 2.3 | 被引: 847 | guideline                         │
├─────────────────────────────────────────────────────────┤
│ [摘要 ▾] [方法 ▾] [参考文献 (23) ▾]                      │
└─────────────────────────────────────────────────────────┘
```

#### Task 2.2: Sorting controls in sidebar

File: `scripts/app.py`

```python
sort_options = {
    "relevance": "相关性（默认）",
    "year_desc": "发表时间（近→远）",
    "if_desc": "影响因子（高→低）",
    "citations_desc": "被引次数（高→低）",
}
sort_by = st.radio("排序方式", list(sort_options.values()))
```

#### Task 2.3: Research trace front-and-center

Move key retrieval info from sidebar expander to answer area top:

```
🔍 检索路径：ckd_researcher_overview → 6 篇来源 → 深度：standard
```

#### Task 2.4: Answer mode chip (from previous plan)

For broad questions like `解释CKD`, show mode selector:

```
[普通解读 ▾] → 切换到：研究者视角 | 治疗证据 | 机制详解
```

### Phase 3: Reference Graph (P3)

#### Task 3.1: Reference link display

In expanded source card, show clickable references:

```
参考文献 (23):
├─ [1] Smith et al. 2014 → src-ckd-012 ✓ (库内已有)
├─ [2] Jones et al. 2015 → src-ckd-018 ✓ (库内已有)
├─ [3] Brown et al. 2012 → ✗ (未收录)
└─ ...
```

#### Task 3.2: Citation graph index

Create: `system/indexes/citation-graph.json`

Structure:
```json
{
  "src-ckd-004": {
    "cites": ["src-ckd-012", "src-ckd-018"],
    "cited_by": ["src-ckd-024", "src-ckd-030"]
  }
}
```

### Phase 4: Decision Tree UI (P4)

**User Insight (2026-06-16):** 决策树向的内容在适当的地方出现会对研究者或用户有帮助。

The vault already contains decision-tree-like content:
- `topics/*/treatment-branch-map.md` — treatment decision branches
- `topics/*/navigation.md` — "Route By Question" sections
- `topics/*/risk-and-recognition.md` — diagnostic pathways

This phase surfaces this content prominently in the UI.

#### Task 4.1: Question Intent Classification

File: `scripts/query.py`

When user asks a broad question like "CKD治疗" or "diabetes insulin", detect intent category:
- **diagnostic** → route to risk-and-recognition + mechanism
- **treatment** → route to treatment-branch-map
- **monitoring** → route to endpoint-handbook
- **overview** → route to navigation page

```python
INTENT_CATEGORIES = {
    "diagnostic": ["诊断", "识别", "检测", "症状", "diagnosis", "recognize", "detect"],
    "treatment": ["治疗", "用药", "insulin", "treatment", "therapy", "药物"],
    "monitoring": ["监测", "复查", "指标", "monitor", "followup", "endpoint"],
}
```

#### Task 4.2: Decision Tree Card Component

File: `scripts/app.py`

Render decision tree cards for branch-map and navigation pages:

```
┌─────────────────────────────────────────────────────────────┐
│ 🌳 治疗决策路径 / Treatment Decision Path                    │
├─────────────────────────────────────────────────────────────┤
│ 您的问题涉及治疗选择。以下是分支路径：                        │
│                                                              │
│ ┌─ 饮食管理 → [diet-architecture.md]                        │
│ ├─ 胰岛素治疗 → [insulin protocol]                          │
│ ├─ SGLT2 口服药 → [sglt2-label-control.md]                  │
│ └─ 缓解评估 → [remission-boundaries.md]                     │
│                                                              │
│ 每个分支有独立的证据层级和适用条件。                          │
└─────────────────────────────────────────────────────────────┘
```

**Design Spec (per DESIGN.md):**
- Container: `st.container()` with border `#2d3147`, border-radius md (6px)
- Title: Geist 500, 15px (md), `#e8eaf0`
- Branch links: Geist 400, 13px (sm), `#8b90a0` (muted), hover `#e8eaf0`
- Tree connectors: Geist Mono 400, 12px, `#4a4f64` (subtle)
- Footer note: Geist 400, 11px, `#8b90a0`
- Spacing: 16px (md) internal padding, 8px (sm) between branches
- No new accent colors - use existing provenance colors if needed

#### Task 4.3: "Route By Question" Widget

File: `scripts/app.py`

For topics with navigation.md, show a clickable "Route By Question" widget:

```
🔀 不确定从哪里开始？ / Not sure where to start?
├─ 如果您想了解发病机制 → [mechanism-overview]
├─ 如果您想了解诊断流程 → [diagnostic-workup]
├─ 如果您想了解治疗选择 → [treatment-branch-map]
└─ 如果您想追溯某项声明 → [verify-a-claim]
```

**Design Spec (per DESIGN.md):**
- Container: `st.expander()` with default collapsed state
- Title: Geist 500, 13px (sm), `#8b90a0`
- Routes: `st.button()` styled as text links, Geist 400, 13px
- Tree connectors: Geist Mono 400, 12px, `#4a4f64`
- Placement: below the answer area, before source cards
- Width: max 720px (matches chat area max-width)

#### Task 4.4: Index existing decision trees

Create: `system/indexes/decision-tree-index.json`

```json
{
  "diabetes": {
    "treatment_branch": "topics/diabetes/treatment-branch-map.md",
    "navigation": "topics/diabetes/navigation.md",
    "diagnostic_route": "topics/diabetes/diagnostic-monitoring-workup.md"
  },
  "ckd": {
    "navigation": "topics/ckd/navigation.md",
    "diagnostic_route": "topics/ckd/risk-and-recognition.md"
  }
}
```

#### Task 4.5: Edge Case Handling

**Fallback behavior:**
- If no intent detected → show generic "Route By Question" widget
- If navigation.md missing for topic → skip Route By Question widget, log warning
- If decision-tree-index.json missing entry → graceful degradation, no widget
- Mixed intent keywords (e.g., "治疗诊断") → pick first matched category

**Error states:**
- Malformed navigation.md → skip parsing, use fallback
- Empty topic folder → no decision tree UI rendered

#### Acceptance Criteria (P4)

| Feature | Test |
|---------|------|
| Intent detection | "治疗" triggers treatment branch display |
| Decision tree card | Branch-map content renders as clickable tree |
| Route By Question | Navigation.md "Route By Question" sections display as widget |
| Index | decision-tree-index.json lists all navigable decision content |
| Fallback | Unknown intent shows generic navigation widget |
| Graceful degradation | Missing navigation.md doesn't crash app |

#### Test Plan (P4)

```python
# tests/test_intent_classification.py
def test_treatment_intent_detected():
    assert classify_intent("CKD治疗方案") == "treatment"

def test_diagnostic_intent_detected():
    assert classify_intent("如何诊断FIP") == "diagnostic"

def test_unknown_intent_fallback():
    assert classify_intent("random question") == "overview"

def test_mixed_intent_first_match():
    # "治疗" appears first
    assert classify_intent("治疗与诊断") == "treatment"

# tests/test_decision_tree_rendering.py
def test_decision_tree_card_renders():
    # Mock navigation.md content
    # Assert rendered HTML contains tree structure

def test_missing_navigation_graceful():
    # Topic without navigation.md
    # Assert no crash, widget not rendered
```

## Skillification Plan

### Skill 1: enrich-source-metadata

**Trigger**: New source card added, or batch enrichment request

**Input**: Source card path or source_id

**Output**: Updated frontmatter with IF + citation_count

**External APIs**:
- Semantic Scholar: `https://api.semanticscholar.org/v1/paper/{doi}`
- Scimago: local CSV cache or scrape

**Manual samples before skillification**: 5 source cards

### Skill 2: extract-references

**Trigger**: Deep extraction of a source card

**Input**: Source card with full text or PDF

**Output**: `references` field populated with:
- Internal source IDs (if match found)
- External identifiers (pmid, doi) for unmatched

**Manual samples before skillification**: 5 source cards

### Skill 3: build-citation-graph

**Trigger**: After reference extraction, or on-demand

**Input**: All source cards with `references` field

**Output**: `system/indexes/citation-graph.json`

**Cron**: Weekly rebuild or on source card change

## Acceptance Criteria

| Feature | Test |
|---------|------|
| IF display | Source card shows "IF: X.X" when data exists |
| Citation count | Source card shows "被引: N" when data exists |
| Sorting | Sidebar radio changes result order |
| Abstract expand | Click shows abstract text |
| Methods expand | Click shows methods summary |
| Reference list | Expand shows linked references |
| Research trace | Visible in answer area, not hidden |
| Answer mode | Chip appears for broad questions |
| Intent detection (P4) | "治疗" triggers treatment branch display |
| Decision tree card (P4) | Branch-map content renders as clickable tree |
| Route By Question (P4) | Navigation.md sections display as widget |

## Files Changed

| File | Change |
|------|--------|
| `core/schemas.py` | Add IF, citation_count, abstract, methods, references fields |
| `core/result_presentation.py` | Add fields to SourceDisplay, build_source_display() |
| `scripts/app.py` | Sorting controls, research trace display, source card v2, decision tree UI |
| `scripts/query.py` | Intent classification for decision tree routing |
| `.claude/skills/enrich-source-metadata/SKILL.md` | New skill |
| `.claude/skills/extract-references/SKILL.md` | New skill |
| `system/indexes/citation-graph.json` | New index |
| `system/indexes/decision-tree-index.json` | New index (P4) |

## Decision Audit Trail

| # | Decision | Classification | Principle | Rationale |
|---|----------|----------------|-----------|-----------|
| 1 | Use Semantic Scholar for citations | Mechanical | Pragmatic | Free API, good coverage |
| 2 | Use Scimago for IF | Mechanical | Pragmatic | Free, no auth |
| 3 | Skillify metadata enrichment | Mechanical | DRY | Will run on every new source |
| 4 | P1 sorting before P3 graph | Mechanical | Bias toward action | Sorting is pure UI, fast win |
| 5 | Manual 5 samples before skill | Mechanical | Explicit over clever | Validate API behavior first |
| 6 | Add P4 Decision Tree UI | User Choice | Completeness | User insight: decision trees help researchers navigate |
| 7 | Intent classification simple keywords | Mechanical | Explicit over clever | Keyword match before ML complexity |
| 8 | Reuse existing navigation.md structure | Mechanical | DRY | Content already exists, just need UI surfacing |

## Implementation Order

1. **Now**: Manual sample run of metadata enrichment (5 source cards)
2. **After approval**: Skillify `enrich-source-metadata`
3. **Then**: Schema changes + presentation layer
4. **Then**: Reference extraction skill
5. **Later (P3)**: Citation graph
6. **Later (P4)**: Decision tree UI — intent detection, decision tree cards, Route By Question widget

---

## GSTACK REVIEW REPORT

| Review | Status | Findings |
|--------|--------|----------|
| CEO | PASS | Scope expanded per user insight: P4 decision tree UI added |
| Design | PASS | Source card v2 + decision tree card + Route By Question widget defined; design specs added per DESIGN.md |
| Eng | PASS | Schema changes + skill plan + intent classification + edge case handling + test plan clear |
| DX | SKIP | No true developer-facing scope (SKILL.md are internal tools, not public APIs) |

### /autoplan Review (2026-06-16)

**Premise Gate:** User chose to expand scope with P4 Decision Tree UI phase.

**User Insight Incorporated:**
> "决策树向的内容在适当的地方出现会对研究者或用户有帮助"
> Decision-tree-like content at appropriate places would help researchers/users.

**Existing Decision Tree Content Identified:**
- `topics/*/treatment-branch-map.md` — treatment branches with "Route By Question"
- `topics/*/navigation.md` — hierarchical navigation with quick helpers
- `topics/*/risk-and-recognition.md` — diagnostic pathways

**P4 Tasks Added:**
1. Intent classification in query.py (diagnostic/treatment/monitoring/overview)
2. Decision tree card component in app.py with design specs
3. Route By Question widget for navigation pages with design specs
4. decision-tree-index.json for indexing navigable decision content
5. Edge case handling for missing/malformed content
6. Test plan for intent classification and rendering

**Review Scores:**
- CEO: PASS — Researcher behavior path addressed; P4 adds strategic navigation value
- Design: 8/10 — Components spec'd per DESIGN.md; tree connectors use approved typography
- Eng: 8/10 — Architecture clean; edge cases documented; test plan included
- DX: N/A — Internal tools only

**Decisions Made:** 8 total (7 mechanical, 1 user choice)

**Implementation Order:**
1. P1 (complete): Sorting controls, metadata display, research trace ✓
2. P3 (pending): Reference graph + citation index
3. P4 (added): Decision tree UI — intent detection, tree cards, Route By Question
