# Design System — Feline Research OS

## Product Context
- **What this is:** Internal veterinary research intelligence tool — a Streamlit chat UI for querying a structured knowledge vault (Karpathy-style LLM wiki) about feline diseases
- **Who it's for:** Researchers, analysts, and ordinary readers who need a sourced first answer across CKD, FIP, HCM, IBD, Diabetes, and FCV; internal use only
- **Space/industry:** Veterinary research, biomedical knowledge management
- **Project type:** Internal research instrument (not a consumer product)

## Aesthetic Direction
- **Direction:** Industrial / Utilitarian
- **Decoration level:** Minimal — typography and the provenance badge system carry all visual weight; no gradients, no illustrations, no decorative shapes
- **Mood:** Precision research instrument. The tool should feel like something Karpathy would build for himself: dense, purposeful, no visual noise. Every element earns its place.
- **Key constraint:** The three provenance badge colors (green / amber / gray) are the ONLY semantic accent colors in the entire UI. Nothing competes with them.

## Typography
- **Display/Hero:** Inter 600, letter-spacing -0.025em — page titles, section headings
- **Body (prose):** Source Serif 4, 16px, line-height 1.75 — answer text, expander content (elegant editorial serif for readability)
- **Body (UI):** Inter 400, 14px, line-height 1.6 — sidebar, forms, general UI text
- **UI/Labels:** Inter 500, 13px — sidebar labels, selectbox text, button text, captions
- **Data/Metadata:** JetBrains Mono 400/500, 11–12.5px — source IDs, file paths, token counts, hop counts, confidence values, all `st.code()` content
- **Code:** JetBrains Mono (same as Data)
- **Loading:** Google Fonts — `https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400&display=swap`
- **Scale:**
  - xs: 11px (mono metadata, badge text)
  - sm: 13px (UI labels, sidebar captions)
  - md: 14–16px (body text, answer prose)
  - lg: 18px (section subheadings)
  - xl: 24px (page title)
  - 2xl: 28–36px (hero)

## Color
- **Approach:** Restrained dark-mode-first; badge colors carry all semantic weight
- **Background:** `#0a0c10` — primary page background (deeper, colder dark for better contrast)
- **Surface:** `#12151c` — sidebar, cards, expanders, input backgrounds
- **Surface 2:** `#1a1e28` — hover states, code blocks, nested surfaces
- **Border:** `#252a38` — all dividers, input borders, expander borders
- **Border (subtle):** `#1e222d` — header/sidebar borders, subtle separators
- **Primary text:** `#eceff4` — main readable text
- **Secondary text:** `#b8bfcc` — body prose, descriptions
- **Muted text:** `#7c8494` — labels, captions, placeholder text, metadata
- **Subtle text:** `#4a5064` — secondary metadata, disabled states

### Provenance Accents (the ONLY accent colors — do not add more)
| Role | Foreground | Background tint | Border tint |
|---|---|---|---|
| `quoted_fact` | `#10b981` | `rgba(16,185,129,0.1)` | `rgba(16,185,129,0.25)` |
| `source_supported_conclusion` | `#d97706` | `rgba(217,119,6,0.1)` | `rgba(217,119,6,0.25)` |
| `llm_inference` | `#6b7280` | `rgba(107,114,128,0.1)` | `rgba(107,114,128,0.25)` |

### Confidence Colors (derived from badge accents)
| Level | Color |
|---|---|
| high | `#10b981` |
| medium | `#d97706` |
| low | `#ef4444` |

- **Dark mode:** This IS dark mode. No light mode variant needed for internal use.

## Spacing
- **Base unit:** 8px
- **Density:** Comfortable (information-dense but not cramped; provenance badges need breathing room)
- **Scale:**
  - 2xs: 2px
  - xs: 4px
  - sm: 8px
  - md: 16px
  - lg: 24px
  - xl: 32px
  - 2xl: 48px
  - 3xl: 64px

## Layout
- **Approach:** Grid-disciplined; sidebar/main split is fixed
- **Sidebar width:** 240px (Streamlit default — do not override)
- **Main content max-width:** 720px (chat area; prevents wall-of-text on wide displays)
- **Grid:** N/A (Streamlit manages layout; override only via CSS injection)
- **Border radius:**
  - sm: 4px (badges, inline code, small tags)
  - md: 6px (inputs, buttons, expanders)
  - lg: 10px (cards, full app container when demoing)
  - full: 9999px (only for circular elements like avatars)

## Motion
- **Approach:** Minimal-functional — only the `st.status()` spinner is intentional motion; no entrance animations
- **Easing:** ease-out (enter), ease-in (exit)
- **Duration:**
  - micro: 50–100ms (hover state color changes)
  - short: 150–200ms (expander open/close)
  - Spinner: 0.8s linear infinite

## Streamlit Implementation

### config.toml
Create `.streamlit/config.toml`:

```toml
[theme]
base = "dark"
backgroundColor = "#0f1117"
secondaryBackgroundColor = "#1a1d27"
textColor = "#e8eaf0"
primaryColor = "#16a34a"
font = "monospace"
```

Note: `font = "monospace"` is the closest Streamlit built-in to a monospace-accented stack. Geist requires CSS injection.

### CSS Injection (app.py — canonical, as of 2026-04-18)

```python
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600&family=Geist+Mono:wght@400;500&display=swap');

/* Base font */
html, body, [class*="css"] {
  font-family: 'Geist', system-ui, sans-serif !important;
  font-size: 15px;
  line-height: 1.7;
}

/* Monospace: code, source IDs, file paths */
code, pre, .stCode, [data-testid="stCode"] {
  font-family: 'Geist Mono', monospace !important;
  font-size: 12px !important;
}

/* Captions and metadata in muted mono */
.stCaption, [data-testid="stCaptionContainer"] {
  font-family: 'Geist Mono', monospace !important;
  font-size: 11px !important;
  color: #8b90a0 !important;
}

/* Chat answer max-width */
[data-testid="stChatMessageContent"] {
  max-width: 720px;
}

/* Figure captions under st.image() */
[data-testid="stImage"] figcaption,
[data-testid="stImageCaption"] {
  font-family: 'Geist Mono', monospace !important;
  font-size: 11px !important;
  color: #8b90a0 !important;
  margin-top: 4px;
}
</style>
""", unsafe_allow_html=True)
```

**Important:** Google Fonts serves this as `family=Geist` (not `Geist+Sans`). The CSS `font-family` value is `'Geist'` not `'Geist Sans'`.

## Provenance Badges — Explicit Spec

Badges are rendered via `render_provenance()` in `app.py:73-77` using inline HTML spans. These are the only accent elements in the UI.

| Property | Value |
|----------|-------|
| `font-size` | `0.75em` (≈ 11px at body 15px) |
| `font-family` | inherit (Geist, not Mono) |
| `font-weight` | 400 |
| `padding` | `1px 6px` |
| `border-radius` | `3px` (sm: 4px from border-radius scale — 3px is current; align to 4px if restyling) |
| `white-space` | `nowrap` |
| `vertical-align` | `middle` (implicit via inline) |

Badge color values are defined in the Color section above. Do not add new badge types or accent colors without explicitly updating this section and the Color section.

## Figures (Vision Layer — added 2026-04-18)

Figures are displayed inline in the assistant chat bubble via `st.image()` when `described_in_answer: true` in the synthesis response. This section defines how they should look.

### Figure Container

- Display: below the answer text, separated by `st.divider()` (renders as a 1px `#2d3147` line)
- Layout: up to 3 figures in a column grid (`st.columns(min(n, 3))`)
- Max columns: 3; overflow wraps to next row
- No figure border or card treatment — images float directly on `#0f1117`

### Figure Captions

Format: `[src-ckd-001]` — source ID only, no descriptive text in caption
- Font: Geist Mono 400, 11px
- Color: `#8b90a0` (muted text)
- Margin-top: 4px from image bottom

Rationale: the source ID is the provenance anchor. Adding a description would duplicate the answer text that already described the figure.

### Figure Sizing

- `st.image()` uses container width by default — do not set `width=` explicitly
- For narrow figures (mechanism schematics, flow diagrams): they will naturally render smaller inside the column container. That's correct.
- For wide figures (outcome tables, forest plots): they expand to fill the column. That's also correct.

### CSS Targeting (already in CSS injection)

```css
[data-testid="stImage"] figcaption,
[data-testid="stImageCaption"] {
  font-family: 'Geist Mono', monospace !important;
  font-size: 11px !important;
  color: #8b90a0 !important;
  margin-top: 4px;
}
```

## Empty State

When no conversation exists yet, the chat area shows a structured empty state instead of a blank page. This is the user's first impression and their 30-second orientation.

### Layout

```
┌─────────────────────────────────────────────────┐
│                                                 │
│              Ask the vault                      │  ← st.title, Geist 600, xl (24px)
│                                                 │
│  158 sources · 140 topic pages · 6 diseases     │  ← Geist Mono 400, 11px, #8b90a0
│                                                 │
│  ┌─────────────────────────────────────────┐    │
│  │  Try asking:                            │    │  ← Geist 400, 13px, #8b90a0
│  │                                         │    │
│  │  ○ 解释CKD                               │    │  ← clickable example chips
│  │  ○ FIP怎么识别                           │    │
│  │  ○ IBD和淋巴瘤怎么区分                   │    │
│  │  ○ HCM是什么，为什么危险                 │    │
│  │                                         │    │
│  └─────────────────────────────────────────┘    │
│                                                 │
│  ┌──────────────────────────────────────┐       │
│  │  Evidence labels:                    │       │  ← Geist 400, 13px, #8b90a0
│  │  ■ quote     — source wording        │       │  ← #16a34a badge
│  │  ■ supported — supported synthesis   │       │  ← #ca8a04 badge
│  │  ■ inference — beyond direct support │       │  ← #6b7280 badge
│  └──────────────────────────────────────┘       │
│                                                 │
│  [Ask a natural feline health question...]      │  ← st.chat_input
└─────────────────────────────────────────────────┘
```

### Example Question Chips

- Rendered as `st.button()` with `use_container_width=False`
- Font: Geist 400, 13px, `#e8eaf0`
- Background: `#1a1d27` (Surface)
- Border: 1px solid `#2d3147`
- Border-radius: md (6px)
- Hover: background shifts to `#222535` (Surface 2)
- On click: populates `st.chat_input` and triggers `run_query()`
- 4 examples, drawn from the ordinary-user acceptance set (kept to 4 by user decision)

### Vault Stats Line

- Rendered below the title via `st.caption()`
- Font: Geist Mono 400, 11px
- Color: `#8b90a0` (muted text)
- Content: dynamically computed from `len(source_index)`, topic page count, disease count
- Format: `{n} sources · {m} topic pages · 6 diseases`
- Separator: ` · ` (middle dot, not bullet)

### Provenance Guide

- Rendered as a compact block below example chips
- Each badge type shown with its actual rendered badge + one-line explanation
- Only appears in empty state, not after conversation starts
- This is the only place the system explains what the colors mean

## Search UI

`search.py` currently exists as CLI only. The Streamlit UI should expose vault search as a sidebar feature so users can keyword-search without formulating a full question.

### Placement

- Sidebar, below the Backend/Disease/Max hops controls
- Above the "Files loaded" expander
- Separated by `st.divider()`

### Components

```
┌─── Sidebar ──────────────┐
│  ...existing controls...  │
│  ─────────────────────── │
│  Search vault             │  ← Geist 500, 13px
│  [keyword...        ] 🔍 │  ← st.text_input + button
│  Scope: ○ All ○ Raw      │  ← st.radio, horizontal
│         ○ Topics          │
│                           │
│  ┌──────────────────────┐│
│  │ src-ckd-004 (12 hits)││  ← search result cards
│  │ ISFM CKD Guidelines  ││
│  │ "...phosphorus..."   ││  ← snippet, Geist Mono 11px
│  ├──────────────────────┤│
│  │ src-ckd-001 (8 hits) ││
│  │ ...                  ││
│  └──────────────────────┘│
│  ─────────────────────── │
│  Files loaded (3)    ▶   │
│  ...                      │
└──────────────────────────┘
```

### Search Result Cards

- Container: `st.expander()` or stacked `st.container()` blocks
- Title: source ID in Geist Mono 400, 12px, `#e8eaf0`
- Subtitle: paper title in Geist 400, 11px, `#8b90a0`
- Snippet: matched text with keyword highlighted, Geist Mono 400, 11px
- Hit count: Geist Mono 400, 11px, `#4a4f64`
- Max results displayed: 5 (matches `search.py` default `--limit 5`)
- Click behavior: opens the source card in a new main-area panel, or loads it as context for the next question

### Scope Radio

- Options: All / Raw / Topics
- Maps to `search.py --scope` parameter
- Default: All
- Style: `st.radio(horizontal=True)`, follows Streamlit dark theme

### Integration with Query

- When a user searches and then asks a question, the search results should inform the query context
- This mirrors the existing `search pre-heat` in `query.py` but makes it visible and user-controlled

## Onboarding / First Run

The first time a user opens the Streamlit app, they need to understand 3 things in 30 seconds:

1. **What this does** — ask a natural feline disease question, get a compact sourced answer
2. **What the colors mean** — green = quoted, amber = supported, gray = beyond evidence
3. **How to start** — click an example or type a question

### Implementation

The empty state (defined above) IS the onboarding. No separate onboarding flow, no modal, no tutorial wizard. The empty state communicates everything a new user needs.

If additional context is needed:
- A collapsible "How this works" section below the provenance guide in empty state
- Content: 3-4 sentences max
- "This tool searches six feline disease modules in the vault. It routes to compiled topic pages and source cards, writes a compact answer, and tags each claim with its evidence level. Green tags are close to source wording. Amber tags are supported synthesis. Gray tags mean the answer goes beyond the loaded sources."
- Font: Geist 400, 13px, `#8b90a0`
- Collapsed by default after first visit (use `st.session_state` or localStorage)

### What NOT to build

- No account creation or login
- No multi-step tutorial
- No tooltip tour
- No "getting started" modal
- The tool should be self-evident from the empty state alone

## Error & Edge States

Currently, errors render as generic Streamlit `st.error()` / `st.warning()` boxes. These should be more informative and actionable.

### Disease Detection Failure

**Current:** `"Could not detect disease from your question. Select a disease in the sidebar and try again."`

**Improved:**
- Icon: none (Streamlit warning box is sufficient)
- Message: "I couldn't figure out which disease you're asking about. Try selecting **CKD**, **FIP**, **HCM**, **IBD**, **Diabetes**, or **FCV** in the sidebar, then ask again."
- Below the warning: re-display the example question chips (same as empty state) so the user has an immediate next action
- Font: follows Streamlit warning box defaults (Geist injection applies)

### API / Backend Failure

**Current:** `"Query failed: {e}"`

**Improved format:**
```
Query failed: [error type]

What happened: [1-sentence plain English explanation]
What to try:
  · Check your API key is set correctly
  · Try switching to Ollama (local) in the sidebar
  · If using Ollama, make sure it's running: ollama serve
```

- Render as `st.error()` with the structured message
- Include the raw error in a collapsed `st.expander("Technical details")`
- Font: body text in Geist 400, technical details in Geist Mono 11px

### Empty Results / Low Confidence

When the system returns an answer but with `confidence: low`:
- Show the answer normally
- Below the answer, add a muted note: `st.caption("⚠ Low confidence — this answer relies heavily on LLM inference beyond the loaded evidence.")`
- Font: Geist Mono 400, 11px, `#ca8a04` (amber, matching the supported conclusion badge)

### No Source Cards Loaded

If the routing step finds 0 relevant source cards:
- Do not synthesize (garbage in, garbage out)
- Show: "No source cards matched your question. Try rephrasing, or select a specific disease in the sidebar."
- Re-display example chips

## Copy / Export Actions

Users get a good answer and want to share it with colleagues. Currently there's no way to do this from the UI.

### Copy Markdown Button

- Placement: below each assistant message, right-aligned
- Label: "Copy markdown" (Geist 400, 11px, `#8b90a0`)
- Style: text button (no background, no border), hover color `#e8eaf0`
- Behavior: copies the raw markdown answer (with provenance tags intact) to clipboard via `st.components.v1.html()` with a clipboard JS snippet
- Feedback: button text changes to "Copied" for 2 seconds, color `#16a34a`

### Export to File

- Placement: sidebar, in the "Last query debug" expander
- Label: "Save as .md"
- Behavior: writes the answer to `outputs/qa/` using the existing `write_back()` function
- This already exists as the "Write answer to outputs/qa/" checkbox, but it should also be available as a one-click action after seeing the answer

### What NOT to build

- No PDF export (over-engineering for internal tool)
- No "share link" (no server, no URLs)
- No email integration
- Keep it simple: copy to clipboard + save to vault

## Decisions Log
| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-04-17 | Dark-mode-first | Internal research tool; less eye strain for evening/night work; signals precision instrument over clinical portal |
| 2026-04-17 | Geist for entire stack | Code-adjacent content (source IDs, file paths, hop counts) is scattered throughout; one font family handles both prose and technical strings coherently |
| 2026-04-17 | Badge colors as only accents | The provenance system (quoted_fact / supported / llm_inference) is the primary differentiating UI element; making it the only accent source makes it feel intentional and primary, not incidental |
| 2026-04-17 | No interactive accent color (no blue primary) | Streamlit handles button/interactive states; custom blue would compete with badge accents; primary color in config.toml set to #16a34a (quoted_fact green) to keep interactive states coherent |
| 2026-04-17 | 720px max-width for chat area | Research answers are prose-dense; unconstrained width produces difficult reading lines on wide displays |
| 2026-04-18 | Corrected font import to `family=Geist` | Google Fonts serves the Vercel Geist font as `Geist`, not `Geist+Sans`. The earlier injection used the wrong identifier and would silently fall back to system-ui. |
| 2026-04-18 | Body 15px/1.7 and caption 11px/Mono codified in CSS | Makes the typographic scale explicit at the DOM level rather than relying on Streamlit defaults, which differ across versions. |
| 2026-04-18 | Source ID as sole figure caption | Keeps provenance atomic — the source ID is the reference; any description lives in the answer text already. Adding a second description would create duplication. |
| 2026-04-18 | No border/card treatment for inline figures | Figures sit on the raw `#0f1117` background. A card would add visual weight and make figures feel like embedded embeds rather than evidence integrated into the answer. |
| 2026-04-18 | Empty state with example chips | New users see a blank page and don't know what to ask. Clickable examples give them a 30-second path to their first meaningful query. |
| 2026-04-18 | Provenance guide in empty state only | The badge color system is the core differentiator but never explained in-app. Showing it once in empty state (not persistently) teaches without cluttering. |
| 2026-04-18 | Search UI in sidebar | search.py exists as CLI only. Sidebar search covers "I want to find a keyword" without formulating a full question. Different intent than Q&A. |
| 2026-04-18 | No onboarding wizard | The empty state IS the onboarding. Modal tutorials and tooltip tours add friction for a tool that should be self-evident. |
| 2026-04-18 | Structured error messages | Generic "Query failed: {e}" is useless to non-developers. Plain English + actionable next steps + collapsed technical details. |
| 2026-04-18 | Copy markdown button per answer | Researchers need to share findings with colleagues. Clipboard copy with provenance tags intact is the minimal viable export. |
| 2026-04-27 | Research-lite output mode | Normal users get cleaner answers: inline provenance badges preserved (they're the value), but technical footers (Files loaded, Source cards cited) removed. Sources section shows paper titles instead of src-xxx IDs. Section heading "Uncertainty / Limits" softened to "What we don't know yet". |
| 2026-04-27 | Figure captions as paper titles | Figure captions now show paper title (e.g., "ISFM CKD Guidelines") instead of source ID (e.g., "src-ckd-001"). More readable for ordinary users. |
| 2026-04-27 | Clean Sources section | New Sources section at end of each answer shows unique paper titles, not technical IDs. Audit trail preserved in sidebar metadata for power users. |
| 2026-04-27 | Source weighting system | Combined score = evidence_level × verification_status. Tiers: high (7-10) for guidelines/reviews with deep extraction, medium (4-7) for original studies, low (0-4) for case reports or abstract-only. Synthesis prompt instructs model to prefer higher-weighted sources when conflicting; acknowledge limitations when citing low-weight sources. |
| 2026-06-17 | Research Mode "Best Papers" ranking standard | Defined explicit ranking formula with 4 weighted factors: evidence_level (35%), recency (25%), source_kind (25%), extraction_depth (15%). See "Research Mode Ranking" section below. |

## Research Mode — "Best Papers" 排序标准

### 设计目的

当用户在 Research Mode 中搜索文献时，系统返回 "Best recent papers"、"Top clinical papers" 等分类结果。用户需要理解：**为什么这篇排在前面？** 排序必须有明确、可解释的标准。

### 排序公式

```
ranking_score = (evidence_level × 0.35) + (recency × 0.25) + (source_kind × 0.25) + (extraction_depth × 0.15)
```

### 四个排序因子

#### 1. Evidence Level（证据等级）— 权重 35%

| 等级 | 分数 | 说明 |
|------|------|------|
| `meta-analysis` | 10 | 荟萃分析 |
| `systematic-review` | 9 | 系统综述 |
| `rct` | 8 | 随机对照试验 |
| `guideline` | 8 | 专业指南（如 ISFM, IRIS） |
| `original-study` | 6 | 原始研究 |
| `review` | 5 | 综述（非系统性） |
| `case-series` | 3 | 病例系列 |
| `case-report` | 2 | 个案报告 |
| `expert-opinion` | 1 | 专家意见 |
| (未标注) | 0 | 无证据等级标注 |

**原理**: 遵循循证医学金字塔。Meta-analysis 和 systematic-review 代表最高级别的证据综合。

#### 2. Recency（时效性）— 权重 25%

| 年份 | 分数 |
|------|------|
| 2024-2026 | 10 |
| 2021-2023 | 8 |
| 2018-2020 | 6 |
| 2015-2017 | 4 |
| 2010-2014 | 2 |
| <2010 | 1 |

**原理**: 兽医学研究快速演进，近 3 年的研究更可能反映当前最佳实践。但经典指南（如 IRIS CKD staging）即使较旧仍保持高权重，因为 evidence_level 得分高。

#### 3. Source Kind（文献类型）— 权重 25%

| 类型 | 分数 | 说明 |
|------|------|------|
| `guideline` | 10 | 专业指南（ISFM, IRIS, ACVIM consensus） |
| `paper` | 7 | 同行评审论文 |
| `review-article` | 6 | 综述文章 |
| `regulatory` | 5 | 监管文件（FDA/EMA 兽药批准） |
| `product-info` | 3 | 产品说明书 |
| `marketing` | 1 | 宣传材料 |
| `internal-doc` | 2 | 内部文档 |

**原理**: 专业指南代表领域共识，同行评审论文提供原始证据，产品/宣传材料可信度较低。

**用户提供的类型映射**:
- 综述 → `review-article` (分数 6)
- 产品说明 → `product-info` (分数 3)
- 宣传 → `marketing` (分数 1)
- 监管 → `regulatory` (分数 5)
- 论文 → `paper` (分数 7)
- 内部文档 → `internal-doc` (分数 2)

#### 4. Extraction Depth（提取深度）— 权重 15%

| 状态 | 分数 | 说明 |
|------|------|------|
| 有 `quoted_facts` + `supported_conclusions` | 10 | 完整深度提取 |
| 有 `one_line_summary` | 6 | 有摘要 |
| 仅有 frontmatter | 3 | 仅元数据 |
| 仅标题 | 1 | 最小信息 |

**原理**: 提取深度越高，系统能给用户提供的信息越丰富，引用价值越高。

### 外部指标（可选增强）

如果卡片中有以下字段，可作为加成因子：

| 字段 | 加成 | 说明 |
|------|------|------|
| `citation_count` ≥ 100 | +0.5 | 高引用论文 |
| `impact_factor` ≥ 5 | +0.3 | 高影响因子期刊 |

**计算**: `final_score = ranking_score + citation_bonus + if_bonus`

**注意**: citation_count 和 impact_factor 目前在 citation-graph.json 中仅有部分数据，不作为主排序依据，仅作为加成。

### 分类展示

Research Mode 输出按以下分类展示，每个分类内部按 ranking_score 排序：

1. **Best recent papers** — 综合排名前 10，不限类型
2. **Top clinical/therapeutic** — endpoints 含 `treatment`、`therapy`、`management` 的论文
3. **Top diagnostic** — endpoints 含 `diagnosis`、`biomarker`、`staging` 的论文
4. **Latest from PubMed** — 外部搜索结果（独立排序，不与本地混合）

### 用户可见性

排序标准对用户透明。在 UI 中：

1. **不显示具体分数** — 避免过度技术化
2. **显示关键标签** — 如 `[综述]`、`[2024]`、`[高引用]`
3. **可选**: hover 显示排序因子的文字说明

### 与现有系统的兼容

| 现有字段 | 对应排序因子 |
|----------|--------------|
| `evidence_level` | Evidence Level |
| `source_kind` | Source Kind |
| `year` | Recency |
| `quoted_facts` 存在 | Extraction Depth |
| `citation_count` (citation-graph.json) | Citation Bonus |

### 实现检查点

- [ ] `research_mode.py` 中的 `rank_sources()` 函数更新为新公式
- [ ] 添加 `source_kind` 到排序因子
- [ ] 添加 extraction_depth 计算
- [ ] 可选: 读取 citation-graph.json 加成高引用论文
- [ ] UI 标签显示关键排序因子
