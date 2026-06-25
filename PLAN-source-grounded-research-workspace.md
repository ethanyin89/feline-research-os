# Plan: Source-Grounded Research Workspace

Date: 2026-06-25
Branch: main
Classification: 方案
Routing: `/autoplan` intake, then CEO + Design + Eng review before implementation
Base branch: main

## Why This Exists

The current product problem is not that the vault lacks research capability. The problem is that the UI still exposes internal system architecture before the user has started a task.

Three user observation notes define the next product move:

- `/Users/jiawei/Desktop/目前观察到的问题.md` — 首页用了专业术语，新用户不知道这是什么
- `/Users/jiawei/Desktop/生成内容中的每一个关键判断，都能一键回到原文，并且定位到支撑该判断的具体段落。.md` — 核心信任机制
- `/Users/jiawei/Desktop/还是太复杂.md` — **最新反馈：即使改了术语，信息层级仍然太多**

**最新反馈核心判断：** 当前首页仍然像"系统介绍页"，而不是"研究问题输入器"。用户一打开要同时理解：从一个研究问题开始、核心工作流、深度研究、快速问、疾病专题与研究简报、历史回答、证据标签指南、工作原理。这些都对，但不应该同时出现在首页。

**参考设计：** agent.ii.inc / Consensus / Biotech AI 的首页都只做三件事：
1. 用户现在要问什么
2. 选择一种工作模式
3. 给几个低认知成本的示例入口

The product principle:

> 首页应该是「研究问题输入器」，不是「系统介绍页」。
> 专业性不要堆在首页，而要体现在结果里：证据标签、原文追踪、Evidence Card、Research Record。

## Current State Read

Project handoff says the repo is a two-track plan, content pipeline plus ordinary-user usage surface. This task belongs to the ordinary-user/researcher usage surface, not the diabetes batch content line.

Relevant current implementation:

- `scripts/app.py`
  - `EMPTY_STATE_INTRO_HTML` still opens with `证据研究工作台`.
  - `render_empty_state()` places explanation before action.
  - `render_answer_block_v2()` already routes answers through `ResultPresentation`.
  - `render_source_card_v2()` already renders source cards, links, abstract, methods, references, and cited-by.
  - `render_user_facing_provenance()` already translates internal provenance tags into user-facing Chinese labels.
- `scripts/workspace_tabs.py`
  - Research Workspace still defaults to five tabs: `任务摘要`, `证据地图`, `核心发现`, `模型与药效评价价值`, `缺口与下一步`.
  - This matches the observed screenshot problem: too many first-level choices.
- `core/schemas.py`
  - `ResearchClaim` already exists with `claim_id`, `source_ids`, `provenance`, `supported_use`, and `boundary`.
  - It does not yet store source passage location, quote span, or highlight target.
- `core/result_presentation.py`
  - `SourceDisplay` already stores source metadata.
  - `InlineCitation` exists, but it is citation-level, not claim-level source-passage trace.

## Premises

1. Keep retrieval, evidence labels, deep extraction, Research Records, and source-card parsing intact.
2. Simplify the first screen by changing wording and hierarchy, not by removing capability.
3. Treat source tracing as a first-class evidence object, not a decorative citation chip.
4. Do not make internal `src-*` IDs reader-facing.
5. Avoid live paid API checks unless the acceptance path truly needs it and budget guards are active.

## User-Facing Goal

### 首页目标

研究者打开 app，只看到三块内容：

```text
今天想研究什么？

输入一个猫病、模型、文献或药效评价问题。
系统会帮你找依据、提炼结论，并标出原文出处。

[输入框]
例如：提炼猫糖尿病模型的关键评价指标

[快速解释]  [深度研究]

常用任务：
[提炼模型评价指标] [比较诊断/分期指标] [梳理治疗研究终点] [分析一篇文献]
```

**首页不应该展示：**
- 疾病专题与研究简报 → 移到侧边栏
- 历史回答 → 移到侧边栏
- 证据标签指南 → 移到结果页引用旁的小问号
- 工作原理 → 移到设置/关于
- 1428 sources · 181 topic pages → 隐藏或极小字体

### 结果页目标

结果默认只显示三个区块：

```text
1. 结论 — 直接告诉我该怎么看
2. 依据 — 列出支撑结论的文献，可点开原文段落
3. 下一步 — 告诉我还要补什么、适合怎么用

[展开完整研究过程] ← 折叠里放详细内容
```

### 证据追踪目标

每个关键判断有证据标签，可点开原文：

```text
[直接来源] 查看原文依据
```

点开后显示：

- paper title
- canonical link
- source section or paragraph location
- original passage
- highlighted support sentence
- why this passage supports the claim
- evidence type: `直接来源`, `来源支持`, or `分析推断`

## Proposed Scope

### Phase 1: Home Page Radical Simplification

Files:

- `scripts/app.py`
- `scripts/check_research_mode_presentation.py` or a new focused presentation check

Changes:

1. **主标题改为** `今天想研究什么？` （不是「从一个研究问题开始」— 太正式）
2. **副标题精简为**：`输入一个猫病、模型、文献或药效评价问题。系统会帮你找依据、提炼结论，并标出原文出处。`
3. **模式按钮改为**：`快速解释` / `深度研究`（不是「快速问」— 与「深度研究」不对称）
4. **示例任务只保留 4-5 个卡片**：
   - `提炼模型评价指标`
   - `比较诊断/分期指标`
   - `梳理治疗研究终点`
   - `分析一篇文献`
   - `构建文献图谱`（可选）
5. **从首页主体移除**：
   - 疾病专题与研究简报 → 侧边栏
   - 历史回答 → 侧边栏
   - 证据标签指南 → 删除或移到结果页
   - 工作原理 → 删除或移到设置
   - 核心工作流说明面板 → 删除
   - 1428 sources · 181 topic pages → 隐藏
6. **侧边栏精简为**：首页、历史任务、疾病专题、设置

Acceptance:

- 首页主体只有：标题 + 输入框 + 模式按钮 + 4-5 个示例任务
- 首页不展示证据标签指南、工作原理、疾病专题列表
- 首页不展示「核心工作流」「从一个研究问题开始」等系统说明
- 现有 quick-start 和 research 示例仍能正常触发
- Streamlit widget keys 无重复

### Phase 2: Result Page Simplification

Files:

- `scripts/workspace_tabs.py`
- `scripts/app.py`
- `scripts/test_result_presentation.py`
- `scripts/check_research_mode_presentation.py`

Changes:

结果页默认只显示三个区块，详细内容折叠：

```text
1. 结论 — 直接展示，不折叠
2. 依据 — 折叠，标题显示来源数量
3. 下一步 — 折叠

[展开完整研究过程] — 里面放原来的详细内容
```

Implementation:

- `结论` section 直接展示（不在 expander 里）
- `依据` 和 `下一步` 在 expander 里，默认折叠
- 原来的 `对模型/药效评价有什么用`、`检索范围` 等内容移到「展开完整研究过程」里
- 或者完全删除，因为这些内容对内部 researcher 不是第一需求

Acceptance:

- 结果页第一屏只有：结论 + 依据（折叠）+ 下一步（折叠）
- 不展示 5 个 tab
- 详细研究过程可选展开

### Phase 3: Claim-Level Evidence Trace

Files:

- `core/schemas.py`
- `core/result_presentation.py`
- `scripts/app.py`
- `scripts/research_mode.py`
- `scripts/test_result_presentation.py`
- `scripts/test_research_record_store.py` if persisted records change

Add a structured evidence trace object. Suggested shape:

```python
@dataclass
class EvidenceTrace:
    trace_id: str
    claim_id: str
    source_id: str
    source_title: str
    canonical_url: str = ""
    evidence_type: str = "source_supported_conclusion"
    source_role: str = ""
    quoted_passage: str = ""
    highlight_text: str = ""
    section: str = ""
    paragraph_id: str = ""
    why_it_supports_the_claim: str = ""
```

Attach traces to `ResearchClaim` or to the presentation contract. The safer first implementation is presentation-side attachment, because existing persisted records may not all have passage data.

Rendering:

- Inline evidence chips keep the existing provenance colors.
- Add `查看原文依据` beside claim-level chips when trace data exists.
- Open an expander or drawer-like panel below the claim.
- Highlight `highlight_text` inside `quoted_passage` with a restrained yellow mark.
- For `分析推断`, show `需要人工复核` and do not pretend the passage directly states the claim.

Fallback behavior:

- If no passage exists, show `来源可打开，但未定位到具体段落`.
- If the source has no canonical URL, still show title and local evidence text.
- If a claim cites multiple sources, show a compact list of evidence cards.

Acceptance:

- At least one deterministic fixture answer renders a claim with a clickable/expandable source passage.
- The highlighted sentence appears inside the passage.
- The UI never exposes raw `src-*` IDs in reader-facing prose.
- Inference-only claims cannot be rendered as directly sourced.

### Phase 4: Paper Card Passage Library

Files:

- `raw/deep-extractions/*.md`
- `scripts/deep_extraction.py`
- `scripts/research_mode.py`
- optional new helper in `core/`

Add optional `source_passages` support to deep extraction parsing:

```yaml
source_passages:
  - passage_id: p-abstract-001
    section: Abstract
    quoted_passage: "..."
    highlight_text: "..."
    supports_claim_types:
      - model_evaluation
      - efficacy_endpoint
    evidence_type: quoted_fact
    chinese_explanation: "..."
```

This should be optional. Existing cards without passage libraries must keep working.

Acceptance:

- Deep-extracted cards can feed passage-level traces.
- Existing deep extraction files do not break.
- Parsing errors degrade to source-level citation, not app failure.

## Not In Scope

- Rewriting retrieval.
- Replacing the current vault/source-card architecture.
- Bulk passage extraction for all 1,400+ sources in this pass.
- Adding a new paid API dependency.
- Making a light-mode redesign.
- Changing the content truth of diabetes/HCM/CKD cards while doing UI work.

## What Already Exists

| Need | Existing asset | Gap |
|---|---|---|
| User-facing evidence labels | `PROVENANCE_LABELS`, `render_user_facing_provenance()` | Labels are not yet claim-level expandable traces |
| Source cards with links | `SourceDisplay`, `render_source_card_v2()` | Links go to source, not exact passage |
| Claims as durable units | `ResearchClaim` | No passage location/highlight fields |
| Research result renderer | `render_answer_block_v2()` | Result still reads like a report plus source list |
| Workspace result structure | `scripts/workspace_tabs.py` | Too many first-level tabs |
| Design system | `DESIGN.md` | Must keep dark utilitarian style, no consumer landing-page rewrite |

## Architecture Diagram

```text
User question
    |
    v
scripts/app.py
    |
    v
scripts/research_mode.py
    |
    +--> source cards / deep extractions
    |
    v
core/result_presentation.py
    |
    +--> Answer sections
    +--> SourceDisplay
    +--> EvidenceProfile
    +--> EvidenceTrace          (new)
    |
    v
scripts/app.py renderer
    |
    +--> direct conclusion
    +--> evidence chips
    +--> "查看原文依据"
    +--> highlighted source passage
```

## Failure Modes Registry

| Failure | User impact | Prevention |
|---|---|---|
| Source-level citation is presented as passage-level support | Researcher trusts an unsupported claim | Require `quoted_passage` + `highlight_text` for `查看原文依据` |
| `分析推断` looks like direct evidence | Overclaiming | Render inference with review warning and no direct-source wording |
| Home page becomes a generic chat clone | Loses research identity | Keep evidence label guide and source count, but below the primary action |
| Five-tab result persists | User still does not know where to start | Default to `直接结论`, demote evidence details |
| Streamlit duplicate widget keys | Runtime break in repeated source cards | Include `key_prefix`, claim id, and source id in every trace button |
| Existing records break schema loading | Old saved records fail to render | Make trace fields optional and version-tolerant |
| Raw `src-*` IDs leak | User sees internal machinery | Reuse `user_visible_source_label()` and existing leakage checks |

## Test Plan

Run static tests:

```bash
python3 -m py_compile scripts/app.py scripts/research_mode.py core/result_presentation.py core/schemas.py
PYTHONPATH=. python3 scripts/test_result_presentation.py
python3 scripts/check_research_mode_presentation.py
python3 scripts/test_query.py
python3 .agents/skills/streamlit_key_guard/scripts/lint_streamlit_keys.py
```

Add or extend tests:

- Home empty state does not contain `证据研究工作台`.
- Result presentation includes `直接结论`.
- Evidence trace fixture renders `查看原文依据`.
- Highlight text is present inside quoted passage.
- Inference claim shows review boundary.
- Internal IDs do not leak into visible answer text.

Live/browser QA:

- Start local Streamlit only after implementation.
- Test at least:
  - `提炼猫糖尿病模型的关键评价指标`
  - `比较 CKD 诊断与分期指标的研究价值`
- Verify first viewport and result top with screenshots.

## Current Implementation Status

Based on git diff analysis, significant work has already been done but not committed:

### Phase 1: Home Page — PARTIALLY DONE, NEEDS MORE CUTS
- ✅ Changed `<h1>证据研究工作台</h1>` → `<h1>从一个研究问题开始</h1>`
- ✅ Changed `🔬 研究工作台` → `🔬 深度研究`
- ✅ Changed `⚡ 快速理解` → `⚡ 快速问`
- ❌ **Still too much on homepage** — 需要继续删除：疾病专题、历史回答、证据标签指南、工作原理、核心工作流面板
- ❌ 主标题应改为 `今天想研究什么？`（更轻）
- ❌ 模式按钮应改为 `快速解释` / `深度研究`（对称）

### Phase 2: Result Page — DONE
- ✅ Changed from 5 tabs to conclusion-first sections with expanders
- ✅ `直接结论` is now first (not in expander)
- ✅ Other sections in expanders: `依据哪些文献`, `对模型与药效评价有什么用`, `还不确定什么`, `检索范围`

### Phase 3: Claim-Level Evidence Trace — MOSTLY DONE
- ✅ `EvidenceTrace` dataclass implemented
- ✅ `build_evidence_traces_from_text()` implemented
- ✅ `render_evidence_traces_v2()` + CSS highlight implemented
- ✅ `source_metadata.py` parses `evidence_policy` from frontmatter
- ✅ Tests pass

### Phase 4: Paper Card Passage Library — NOT STARTED
- ❌ `source_passages` schema not implemented

## Review Notes

### CEO Review (Updated)

**核心判断正确：** 产品的稀缺资源是研究者信任，不是更多的首页标签。原文追踪比首页简化更有杠杆，因为它改变的是「研究者能否审计答案」。

**最新反馈要求更激进的首页简化：** 即使改了术语，信息层级仍然太多。首页应该是「研究问题输入器」，不是「系统介绍页」。参考 agent.ii.inc / Consensus / Biotech AI 的首页设计。

### Design Review (Updated)

**交互原则值得学：** agent.ii.inc / Consensus 的首页都只做三件事：用户现在要问什么、选择工作模式、给几个示例入口。

**视觉方向不变：** 保持 dark utilitarian 设计系统，不学 agent.ii.inc 的 warm beige 皮肤。provenance colors 仍是唯一的语义色彩。

### Engineering Review (Updated)

**Phase 1 需要继续实现：** 从 `render_empty_state()` 中删除更多内容块。
**Phase 2-3 基本完成：** 只需要测试和微调。
**Phase 4 可以延后：** 不阻塞核心体验。

## Decision Audit Trail

| # | Phase | Decision | Classification | Principle | Rationale | Rejected |
|---|---|---|---|---|---|---|
| 1 | Intake | Classify as `方案` | Mechanical | Bias toward action | No bug trace exists; user supplied product observations and desired experience | Treating it as排查 |
| 2 | Scope | Combine UI simplification with evidence trace | Taste | Choose completeness | The ask starts with entry clarity but the real trust loop completes only at claim verification | Only changing homepage copy |
| 3 | Architecture | Add optional `EvidenceTrace` instead of rewriting source cards | Mechanical | Explicit over clever | Existing schema already has claims and source displays; optional trace minimizes migration risk | New retrieval architecture |
| 4 | Design | Preserve dark utilitarian design system | Mechanical | DRY | `DESIGN.md` is explicit and the project is an internal research instrument | Copying agent.ii.inc visual skin |
| 5 | Implementation | Start with deterministic fixtures and local tests | Mechanical | Boil lakes | This feature must not depend on live paid model output to be testable | Manual-only browser validation |
| 6 | Phase 1 Update | Radical homepage simplification | Taste | Explicit over clever | User feedback says current version still feels like "system intro page" not "research input box" | Keeping current homepage structure |

## GSTACK REVIEW REPORT

| Review | Trigger | Why | Runs | Status | Findings |
|--------|---------|-----|------|--------|----------|
| CEO Review | `/autoplan` intake | Scope & strategy | 2 | NEEDS_UPDATE | Homepage needs more aggressive simplification per latest feedback |
| Design Review | `/autoplan` intake | UI/UX gaps | 2 | PASS_WITH_CONSTRAINTS | Copy interaction principle from agent.ii.inc, not visual skin |
| Eng Review | `/autoplan` intake | Architecture & tests | 2 | PASS_WITH_FOLLOW_UP | Phase 2-3 done, Phase 1 needs more cuts, Phase 4 deferred |

**VERDICT:** PHASE 1 NEEDS REWORK. READY TO IMPLEMENT AFTER CONFIRMING HOMEPAGE CUTS.

