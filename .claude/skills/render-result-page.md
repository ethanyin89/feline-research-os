# Skill: Render Result Page

**Version:** 1.0.0
**Created:** 2026-06-11
**Purpose:** Design and content-generation contract for research result presentation
**Scope:** Presentation logic only. Does not execute paid APIs.

---

## When to Use This Skill

Use this skill when generating or reviewing any research result presentation:

| Surface Type | Use When | Primary User |
|--------------|----------|--------------|
| Overview / What-Is | Educational content about a disease, condition, or concept | Ordinary cat owner |
| Ranked Evidence / Decision Support | Comparing treatment options with evidence tiers | Veterinarian, advanced user |
| Ask the Vault Response | Real-time query with synthesized answer | Any user asking a question |

---

## Presentation Contract

### ResultPresentation

Every result surface consumes this structured model:

```text
ResultPresentation
├── context
│   ├── title: string
│   ├── subtitle: string
│   ├── audience: "ordinary" | "professional"
│   └── language: "zh" | "en"
├── evidence_profile
│   ├── authority_state: "automated" | "human_reviewed"
│   ├── direct_support_count: int
│   ├── supported_synthesis_count: int
│   ├── inference_count: int
│   ├── limited_source_count: int
│   └── unresolved_gap_count: int
├── primary_answer
│   ├── lead: string (first paragraph, always visible)
│   ├── sections[]: {title, content, citations[]}
│   └── inline_citations[]: {text, source_ref, provenance_type}
├── evidence
│   ├── source_cards[]: SourceDisplay[]
│   ├── boundary_notice: string
│   └── research_trace[]: {step, action, result}
└── next_actions[]: {label, action_type, target}
```

### SourceDisplay

User-facing source card structure:

```text
SourceDisplay
├── title: string (paper title, never internal ID)
├── canonical_url: string | null (DOI or PubMed URL)
├── publication_year: int
├── source_type_label: string (user-facing)
├── evidence_depth_label: string (user-facing)
└── limitations[]: string[]
```

---

## User-Facing Evidence Vocabulary

### REQUIRED: Always translate internal values to user-facing labels

| Internal Value | Ordinary-User Label | When to Show |
|----------------|---------------------|--------------|
| `deep_extracted`, `audited` | 已核查全文 | Source card depth tag |
| `source_checked` | 已核查来源 | Source card depth tag |
| `abstract_weighted` | 基于摘要 | Source card depth tag |
| `title_only` | 仅题录信息 | Source card depth tag + warning |
| `quoted_fact` | 直接来源 | Provenance breakdown |
| `source_supported_conclusion` | 来源支持 | Provenance breakdown |
| `llm_inference` | 分析推断 | Provenance breakdown + inline tag |

### FORBIDDEN: Never show these to ordinary users

- Internal source IDs: `src-ckd-003`, `src-cancer-045`
- Raw verification statuses: `abstract_weighted`, `deep_extracted`
- Raw provenance types: `quoted_fact`, `llm_inference`
- Confidence scores: `high`, `medium`, `low` (removed in V1)

---

## Surface Anatomy

### 1. Overview / What-Is

```text
Title + plain subtitle
  ↓
Quick answer (1-2 paragraphs, always visible)
  ↓
Key facts (3 cards with numbers/labels)
  ↓
Explore next (navigation cards to related topics)
  ↓
Sources and update status (collapsed by default)
  ↓
Boundary notice (what this page does NOT cover)
```

**Rules:**
- Trust is concise and does not interrupt the first explanation
- English is collapsed by default when Chinese is selected
- No global confidence badge
- Sources show paper titles with DOI links

### 2. Ranked Evidence / Decision Support

```text
Title + task context
  ↓
Evidence legend (tier colors + text labels)
  ↓
Top-ranked interventions (fully expanded)
  ↓
Conditional and thin-evidence items (collapsed)
  ↓
Comparison table
  ↓
Sources, limitations, and decision boundary
```

**Rules:**
- Every intervention states both "supported use" and "do not overclaim"
- Tier colors always accompanied by text labels (accessibility)
- Lower tiers collapsed by default
- Comparison table has stacked mobile representation

### 3. Ask the Vault Response

```text
Question echo
  ↓
Evidence profile (factual: source count, depth breakdown, authority state)
  ↓
Answer with inline citations
  ↓
Evidence limitations (when decision-relevant)
  ↓
Source cards
  ↓
Research trace (collapsed)
  ↓
Next research moves (2-4 specific suggestions)
```

**Rules:**
- NO global confidence badge (high/medium/low removed in V1)
- Evidence profile shows factual counts, not judgments
- Inline citations use paper titles, open canonical URL in new tab
- "Next research moves" must be task-specific, not generic "ask anything"

---

## State Matrix

| State | Trigger | User Sees | Recovery Action |
|-------|---------|-----------|-----------------|
| `loading` | Retrieval or synthesis running | Named current step + progress | Wait or cancel |
| `supported-profile` | Direct, deep support | Evidence profile with linked claims | Inspect sources |
| `mixed-profile` | Mixed depth or synthesis | Profile + concise caveat | Inspect limitations |
| `sparse-profile` | Few sources or material inference | Warning label + prominent limits | Run deeper research |
| `partial-sources` | Some source metadata fails | Answer remains, affected source marked | Retry lookup |
| `title-only` | Source has no abstract/full text | Discovery-only label, excluded from support | Do not count toward claims |
| `no-direct-evidence` | No relevant source cards | Explicit abstention, no fake conclusion | Start literature intake |
| `empty-answer` | Synthesis returns blank | Named failure state | Retry or use local answer |
| `malformed-provenance` | Unknown provenance tags | Safe plain text + trace warning | Log and fallback |
| `source-link-missing` | No DOI/PMID/URL | Title + "链接不可用" | Expert metadata may show ID |
| `research-trace-missing` | Trace absent | Section omitted | No user-facing error |
| `bilingual-missing` | Translation absent | Selected language only | No empty expander |
| `long-answer` | Exceeds reading budget | Lead expanded, remainder collapsed | Expand sections |
| `mobile-320px` | Narrow viewport | One-column cards, stacked tables | Responsive layout |

---

## Interaction Rules

1. **Progressive disclosure:** Primary answer open; source metadata, trace, and lower-ranked evidence collapsed
2. **Citation behavior:** Display shortened paper title, open canonical URL in new tab. Missing URLs not rendered as fake links
3. **Copy behavior:** "Copy answer" copies readable text + linked source titles, excluding UI labels and internal IDs
4. **Next actions:** Offer 2-4 task-specific research moves. Generic "ask anything" is NOT acceptable
5. **Accessibility:**
   - Semantic headings (h1 > h2 > h3)
   - Keyboard-operable expanders
   - Visible focus indicators
   - 44px minimum touch targets
   - Color never carries meaning alone (always text labels)
6. **Responsive:** 720px max reading width; cards collapse to one column; tables provide stacked mobile representation

---

## Approved Examples

### Example 1: What-Is Page Header

```
标题：什么是猫慢性肾病？
副标题：基于 4 篇专业文献的综合解释
证据概况：[33篇来源] [自动生成]
```

### Example 2: Evidence Profile (NOT confidence badge)

```
基于 5 篇来源 | 3 篇已核查全文 | 2 篇基于摘要
自动生成，未经人工审核
```

### Example 3: Source Card

```
ISFM Consensus Guidelines on Feline CKD
已核查全文 | 2019 | J Feline Med Surg
[DOI ↗](https://doi.org/10.1177/1098612X19831519)
```

### Example 4: Provenance Breakdown

```
答案构成：
🟢 直接来源: 2处
🟡 来源支持: 3处
⚪ 分析推断: 1处
```

### Example 5: Inline Citation

```
肾脏处方粮是基础治疗 [ISFM Guidelines (2019) ↗]
```

### Example 6: Sparse Profile Warning

```
⚠️ 证据较薄
仅 1 篇来源 | 基于摘要分析
[🔍 运行更深入研究]
```

---

## Anti-Patterns

### NEVER DO

| Anti-Pattern | Why It's Wrong | Correct Approach |
|--------------|----------------|------------------|
| Show `src-ckd-003` | Internal ID meaningless to users | Show paper title + DOI link |
| Show `置信度：高` | Confidence badge removed in V1; semantics insufficient | Show factual evidence profile |
| Show `abstract_weighted` | Raw internal status | Show "基于摘要" |
| Show `llm_inference` | Raw internal status | Show "分析推断" |
| Render fake link for missing DOI | Broken UX | Show "链接不可用" |
| Generic "还有其他问题吗?" | Not task-specific | Offer 2-4 specific next moves |
| Color-only tier meaning | Accessibility failure | Always add text labels |
| `title-only` source counted as support | Misrepresents evidence | Exclude from support count, show warning |

---

## Validation Checklist

Before rendering any result page, verify:

- [ ] Zero `src-*` identifiers in default view
- [ ] Zero raw verification statuses (`abstract_weighted`, `deep_extracted`)
- [ ] Zero raw provenance types (`quoted_fact`, `llm_inference`)
- [ ] No global confidence badge (high/medium/low)
- [ ] All source cards have paper titles
- [ ] All linked sources have canonical URLs or explicit "链接不可用"
- [ ] Title-only sources marked as discovery-only
- [ ] Tier colors accompanied by text labels
- [ ] Touch targets minimum 44px
- [ ] Tables have mobile stacked representation

---

## References

- Visual prototype: `system/indexes/presentation-logic-test-page.html`
- Markdown samples: `system/indexes/content-presentation-logic-samples-20260611.md`
- Design system: `DESIGN.md`
- Plan: `PLAN-page-rendering-improvements.md`
