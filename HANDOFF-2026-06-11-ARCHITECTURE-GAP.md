# Handoff: Architecture Gap Analysis 2026-06-11

**Status:** Context Recovery Complete — Implementation Gap Identified
**Branch:** `idea-chatacademia-research-workbench`
**Date:** 2026-06-11
**Critical Reference:** `/Users/jiawei/Downloads/260606-handoff(1).md` — **June 6 Complete Architecture**

---

## Context Loss Acknowledgment

**June 6, 2026** produced a comprehensive 534-line architecture document for Feline Research OS. This document defined:

- Six-layer architecture
- Research Agent Answer Pattern (7 components)
- Research Record schema (full YAML spec)
- Evidence Card schema (with PMID/PMCID/DOI fields)
- Harness Loop (RALPH) for complex tasks
- Search Depth Controller
- Tool Laziness prevention
- Agent Profiles
- MVP implementation roadmap

**Today (June 11)** I was acting like reading the Research OS materials for the first time. This is a process failure — the handoff documents were not properly transferred across sessions.

---

## What June 6 Already Defined

### 1. Research Agent Answer Pattern (Standard Output)

```
1. Query interpretation — 系统如何理解用户问题
2. Retrieval scope — 检索来源、检索策略、优先级
3. Ranked evidence cards — 排序后的证据卡片
4. Why this matters — 每条证据的使用价值
5. Quick take — 证据地图或领域地图总结
6. Gaps / uncertainty — 缺口与不确定性
7. Next research moves — 下一步研究分支
```

### 2. Six-Layer Architecture

```
1. Human-in-the-loop Research Workspace
2. Professional Team Mode (Strategist → Coordinator → Associates → Verifier)
3. Research Pipeline (query → retrieval → compression → reflection → synthesis)
4. Research Record (persistent structured output)
5. Retrieval Memory (low-cost state recovery)
6. Data Quality & Verification
```

### 3. Evidence Card Schema

```yaml
evidence_card_id: string
title: string
source_type: pubmed | pmc | guideline | internal_note | protocol | uploaded_file
source_id: PMID/PMCID/DOI/file_path/url  # ← Key: DOI is already specified
species: cat | dog | human | mouse | mixed | unknown
disease: string
study_type: guideline | review | original_research | case_series | internal_protocol | other
biomarkers: [string]
use_case: [diagnosis, enrollment, efficacy_endpoint, safety_monitoring, prognosis, model_validation]
key_finding: string
limitations: string
evidence_strength: high | medium | low
last_reviewed: date
```

### 4. Research Record Schema

```yaml
record_id: string
timestamp: datetime
user_request: string
task_type: literature_review | protocol_design | evidence_check | biomarker_mapping | model_evaluation | pk_design | other
species: cat
disease: FIP | CKD | HCM | FCGS | obesity | dermatology | other
scope: string
retrieval_sources: [pubmed, pmc, internal_knowledge_base, guideline, uploaded_file]
selected_evidence: [evidence_card_id]
excluded_evidence: [{reason}]
key_decisions: [decision]
uncertainties: [uncertainty]
output_path: string
verifier_status: passed | failed | needs_human_review
next_steps: [action]
handoff_summary: string
```

### 5. Harness Loop (RALPH)

```
user_request
  → task_evaluation
  → initial_answer / draft
  → gap_check_against_original_requirement
  → revision
  → independent_verification
  → final_answer
  → save_research_record
```

---

## Implementation Status Check

### Already Exists ✅

| Component | Location | Status |
|-----------|----------|--------|
| Source cards with DOI | `raw/papers/src-*.md` | DOI in `links.doi` field ✅ |
| Source URL | `raw/papers/src-*.md` | URL in `links.url` field ✅ |
| Evidence level | `raw/papers/src-*.md` | `evidence_level: review` etc. ✅ |
| Species tagging | `raw/papers/src-*.md` | `species: feline` ✅ |
| Disease tagging | `raw/papers/src-*.md` | `diseases: [CKD]` etc. ✅ |
| Endpoints | `raw/papers/src-*.md` | `endpoints: [...]` array ✅ |
| Evidence policy | `raw/papers/src-*.md` | `quoted_fact`, `source_supported_conclusion`, `llm_inference` ✅ |
| Basic Streamlit app | `scripts/app.py` | Running but lacks Research OS pattern |

### Source Card vs. June 6 Evidence Card Schema

| June 6 Field | Current Source Card | Gap |
|--------------|---------------------|-----|
| `source_id: PMID/PMCID/DOI` | `links.doi` only | Missing PMID/PMCID |
| `biomarkers: [...]` | Not in frontmatter | **Gap** |
| `use_case: [diagnosis, enrollment, ...]` | Not present | **Gap** |
| `evidence_strength: high/medium/low` | Has `evidence_level` | Different concept |
| `key_finding` | Has "One-Line Summary" | Partial match |
| `limitations` | Has "Limits / Caveats" section | Partial match |
| `last_reviewed` | Not present | **Gap** |

**Key Insight:** Source cards are 70% aligned with June 6 schema. Main gaps are `use_case`, `biomarkers`, and PMID/PMCID.

### NOT Implemented ❌

| Component | June 6 Spec | Current State |
|-----------|-------------|---------------|
| Research Agent Answer Pattern | 7-component structured output | Not implemented |
| Research Record persistence | YAML schema defined | No implementation |
| Evidence Card schema | Full spec with use_case, biomarkers | Partial metadata in source cards |
| Harness Loop | 7-step verification flow | No implementation |
| Search Depth Controller | quick/standard/deep/audit modes | No implementation |
| Tool Laziness prevention | Multi-step retrieval requirement | No implementation |
| Verifier rules | Species, evidence, protocol checks | No implementation |
| Agent Profiles | 8 specialist roles defined | No implementation |

---

## Today's Work vs. June 6 Design

| Today's "Discovery" | June 6 Status |
|---------------------|---------------|
| DOI links must be real | Already specified: `source_id: PMID/PMCID/DOI` |
| Need research value statement | Already defined: "Why this matters" component |
| Need Quick take section | Already defined: component #5 |
| Need Next research moves | Already defined: component #7 |
| Need structured output | Full 7-component pattern defined |

**Conclusion:** Today was rediscovery, not discovery.

---

## Gap Priority

### P0: Implement Research Agent Answer Pattern

The June 6 document specified:
> "借鉴 II-Commons 页面截图，建议 feline-research-os 标准输出结构"

This is the core differentiation. Current implementation outputs plain text answers instead of structured research entries.

### P1: Evidence Card Schema Alignment

Source cards exist but don't match the June 6 Evidence Card schema. Need to:
1. Verify which fields already exist
2. Add missing fields (use_case, biomarkers, evidence_strength)
3. Ensure PMID/PMCID/DOI coverage

### P2: Research Record Implementation

Each query should generate a persistent record. Currently no persistence layer.

### P3: Harness Loop for Complex Tasks

The gap_check → revision → verification flow is not implemented.

---

## Recommended Next Step

The June 6 document ends with:

> "下一步你希望我把这些材料收束成 Feline Research OS v0.1 Architecture，还是直接转成 Streamlit 项目的模块/文件结构和实现路线？"

This question was never answered. The user needs to choose:

**A) Create `ARCHITECTURE.md`** — Consolidate June 6 design into a living architecture document in the repo

**B) Implementation Roadmap** — Map June 6 schemas to actual code changes in scripts/ and raw/papers/

**C) Both** — ARCHITECTURE.md first, then implementation roadmap

---

## File References

| File | Purpose |
|------|---------|
| `/Users/jiawei/Downloads/260606-handoff(1).md` | **Authoritative** June 6 architecture (534 lines) |
| `/Users/jiawei/Desktop/raw-2.md` | Research OS philosophy document |
| `system/indexes/presentation-logic-test-page.html` | Today's test page (needs DOI fix) |
| `raw/papers/src-ckd-003.md` | Example source card with existing DOI |

---

## Process Fix

To prevent future context loss:

1. **ARCHITECTURE.md must exist in repo** — Not in external handoff files
2. **Critical schemas belong in repo** — Not in conversation-only documents
3. **Handoff documents must reference repo files** — Not contain the only copy

---

**Created:** 2026-06-11 22:30
**By:** Claude Code (After reading June 6 handoff)
**Key Insight:** June 6 architecture was complete; implementation never started

