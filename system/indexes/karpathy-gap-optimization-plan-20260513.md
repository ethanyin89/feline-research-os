---
id: system-karpathy-gap-optimization-plan-20260513
type: system
topic: operating-system
question_type: plan
language: zh
last_compiled_at: 2026-05-13
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
source_context:
  - Google Sheet: feline diabetes & obesity, 工作表1 A:B, 2026-05-13
  - system/indexes/feline-diabetes-obesity-intake-manifest-20260513.md
  - system/health-checks/health-report-20260513.md
  - system/indexes/karpathy-gap-analysis.md
  - system/indexes/karpathy-artifact-gap-check.md
  - system/indexes/ordinary-user-karpathy-gap-recovery-plan-20260506.md
---

# Karpathy Gap Optimization Plan, 2026-05-13

这页回答一个具体问题：

`当前 feline-research-os 和 Karpathy LLM Wiki 式项目相比，差距在哪里，下一步怎么优化？`

## Classification

这件事属于：

`检查 + 方案`

不是想法：目标形态已经很清楚，就是 Karpathy LLM Wiki 的三层/多层模式。

不是排查：没有单点 bug。

不是直接内容处理：Google Sheet 已经进入 intake manifest 和 obesity first-pass source cards，这次关注系统形态差距。

## External Reference Snapshot

Karpathy LLM Wiki 模式的核心判断来自当前公开页面和项目说明：

- immutable raw sources
- LLM 维护 compiled wiki
- schema/workflow 文件约束 agent 怎么 ingest、query、lint
- query 后沉淀回 wiki
- lint 找 stale、orphan、missing cross-reference、contradiction
- AI-consumable exports, such as `llms.txt`, `.json`, graph, or MCP tools

参考过的外部页面：

- `https://llmwiki.app/`
- `https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f`
- `https://www.freshcrate.ai/projects/llm-wiki`

## Sheet Reality Used In This Check

Google Sheet `feline diabetes & obesity` 当前读到：

- tab: `工作表1`
- range sampled/read: `A1:B240`
- classified rows in manifest: `227`
- diabetes segment rows: `129`
- obesity segment rows: `97`
- existing rows: `35`
- new diabetes candidates: `94`
- new obesity candidates: `87`
- shared existing rows: `5`
- duplicate-in-sheet rows: `5`
- section labels: `1`

Current repo state after prior intake:

- Diabetes remains a mature 24-card module.
- Obesity has 8 first-pass source cards, all partial.
- Obesity pages are intentionally source-indexed shells, not reader guidance.

## 8-Sample Gap Audit

This is the manual 3-10 sample pass required before codifying another recurring workflow.

| # | Sample | Evidence | Gap | Severity | Optimization |
|---:|---|---|---|---|---|
| 1 | Raw layer | `raw/papers/src-obesity-001.md` is a source card, not the immutable article/PDF/web clip | `raw/` currently mixes source-card truth with source archive semantics | High | Split policy into `raw/source-cards` semantics or add `raw/archive/` for immutable originals with checksum/acquisition metadata |
| 2 | Obesity shell | `topics/obesity/index.md`, `current-state-dashboard.md`, health thin-source WARN | Obesity exists as a compiled shell but is not yet a normal reader module | High | Block ordinary obesity routing until Tier A deep extraction creates at least one narrow compiled owner |
| 3 | MCP surface | `scripts/mcp_server.py` docstring advertises `vault_query`, but tools list omits it | AI-consumable query layer is overclaimed | High | Either implement `vault_query` around `run_query_core()` or remove the claim and mark MCP as search/compile/source-list only |
| 4 | Health severity | `system/health-checks/health-report-20260513.md` says active and "No immediate structural action" while thin-source and compile-trigger WARN-like facts exist | Health passes too cleanly for structural state | High | Add actionable severity gates for thin reader surfaces, changed-source recompile queues, stale pages, and bootstrap modules |
| 5 | Compile automation | `scripts/compile_trigger.py` works manually; no repo CI/hook/cron is active | Compile discipline still depends on operator memory | High | Run 3-10 clean manual report-mode samples, then add non-destructive scheduled health/compile check |
| 6 | Write-back closure | `query.py` can write `outputs/qa` and inbox, but promotion remains manual rhythm | Query results can be saved, but system growth is not visible enough | Medium-High | Add a reviewed promotion queue mapping saved answers to target topic/entity pages with accepted/held/rejected states |
| 7 | Intake durability | `scripts/literature_sheet_intake.py` is diabetes/obesity-marker oriented; workflow references external memory/skill paths | Sheet intake is codified but still brittle for new disease markers | Medium | Move repeatable disease-marker rules into repo-owned config and require approval-state transition before source-card creation |
| 8 | AI exports / static wiki surface | No `site/`, `llms.txt`, `graph.jsonld`, page `.json`, sitemap, or search index artifact exists | The vault is Obsidian/CLI-readable, not yet broadly AI-consumable as a static LLM wiki | Medium | Add a small static export prototype for 3-5 pages before building a full site |

## CEO Review

The core strategic issue is not "more feline content".

The repo already has strong evidence discipline: source cards, traceability, health checks, provenance tags, disease dashboards, and query tests. That is the part many LLM wiki products fake.

The gap is that the product surface still feels more like a disciplined research document warehouse than a living query-native wiki.

Highest leverage reframing:

`Turn the system from "well-governed markdown vault" into "ask-first compiled wiki with visible maintenance loops."`

## Existing Leverage

| Need | Existing Asset | Reuse |
|---|---|---|
| Search | `scripts/search.py` | Keep. It is already the naive search layer. |
| Query | `scripts/query.py`, `scripts/app.py` | Keep. Improve route/load/output contract, do not rewrite. |
| Compile queue | `scripts/compile_trigger.py` | Keep. Add severity gates and scheduled/report-mode wrappers. |
| Health | `scripts/health.py` | Keep. Add stricter structural states instead of separate lint scripts first. |
| Intake | `scripts/literature_sheet_intake.py`, global feline intake skill | Keep. Add repo config before expanding beyond diabetes/obesity. |
| Trust | `verification_status`, `decision_grade`, provenance tags | Keep. Surface more visibly in query/static exports. |
| Promotion | `outputs/qa`, `inbox/`, `query-to-writeback.md` | Keep. Add queue state and target mapping. |

## Dream State

```text
CURRENT
  raw/source cards + topics + query UI + health
  but many maintenance loops remain manual

THIS PLAN
  tighten raw/archive semantics
  block immature modules from ordinary routing
  expose true MCP capability
  make health warnings actionable
  prototype static AI exports
  define promotion queue

12-MONTH IDEAL
  drop source -> source archive + source card -> compile queue
  query -> answer -> reviewed write-back candidate
  health -> stale/contradiction/recompile dashboard
  static site + llms.txt + graph.jsonld + MCP tools
  user experiences a living wiki, not a folder tree
```

## Eng Review

### Architecture

```text
Google Sheet / papers / web
        |
        v
intake manifest  ->  source cards  ->  deep extraction
        |                 |                  |
        v                 v                  v
source queue      compile_trigger.py   topics/entities/outputs
        |                 |                  |
        v                 v                  v
health.py         MCP/search/query      Streamlit + future static export
```

The architecture is sound. The weak points are state transitions:

- manifest `pending-review` to accepted source-card creation
- partial source card to deep-extracted source card
- query answer to reviewed write-back
- changed source to required recompile
- compiled page to stale/active lifecycle

### Test Strategy

Current tests are good for code contracts:

- `python3 scripts/test_query.py` passes 102/102.
- MCP tool list returns three tools.
- compile trigger returns downstream queue for obesity sample sources.

Missing tests:

- MCP docstring and tools list consistency.
- Obesity ordinary routing should be blocked or explicitly caveated while only partial cards exist.
- Health should not say "No immediate structural action" when changed source queue or bootstrap thin-source reader pages exist.
- Static export smoke test once export prototype exists.

## Design Review

No direct UI redesign is required before the next content/system slice.

The important design decision is information hierarchy:

1. Ask/search surface first.
2. Trust explanation second.
3. Source trail third.
4. Maintainer controls last.

The repo has already moved in this direction through `start.md` and `scripts/app.py`. The next visible improvement should be living-state cues:

- "this module is mature"
- "this module is source-indexed only"
- "this answer created a write-back candidate"
- "this page may be stale because source cards changed"

## Optimization Plan

### P0: Make The Current State Honest

1. Fix MCP overclaim:
   - either implement `vault_query`
   - or edit docs/docstring to say MCP is search/compile/source-list only

2. Add obesity routing gate:
   - ordinary obesity questions should route to a caveated bootstrap answer
   - do not let obesity look equivalent to CKD/FIP/HCM/IBD/Diabetes/FCV until deep extraction exists

3. Update health action logic:
   - thin source usage in high-visibility pages should produce a concrete next action
   - compile-trigger changed-source queue should be visible as action, not buried under active status

### P1: Close The Living Wiki Loop

4. Build reviewed write-back queue:
   - input: `outputs/qa/` and `inbox/`
   - output: accepted/held/rejected rows with target topic/entity page
   - first run: 3-10 saved answers only

5. Add page lifecycle fields:
   - `freshness_status: current | stale_candidate | stale`
   - `last_source_change_checked_at`
   - `writeback_state: none | candidate | reviewed | promoted`

6. Add repo-owned intake config:
   - disease markers
   - segment names
   - ID prefixes
   - source-card start number policy

### P2: Make It AI-Consumable

7. Prototype static export for 3-5 pages:
   - `site/index.html`
   - `site/llms.txt`
   - `site/graph.jsonld`
   - per-page `.txt` / `.json`
   - do not build full frontend first

8. Add MCP `vault_query` only after the CLI route is stable in no-surprise mode:
   - first expose a route-only or dry-run query tool
   - then expose live synthesis with API-key/budget guard

### P3: Automation

9. Do not cron judgment-heavy content promotion.

10. Cron/launchd is appropriate only for deterministic checks:
    - markdown links
    - query tests
    - health report
    - compile trigger report

Before enabling scheduled automation, run 3-10 manual samples:

```bash
python3 scripts/health.py
python3 scripts/compile_trigger.py --since 1 --json
python3 scripts/check_markdown_links.py
python3 scripts/test_query.py
```

If those stay stable, install a local scheduled report job that writes a timestamped report under `system/health-checks/` or a non-git runtime log. Do not auto-edit topic pages from cron.

## Decision Audit Trail

| # | Decision | Classification | Principle | Rationale | Rejected |
|---:|---|---|---|---|---|
| 1 | Treat this as check + plan | Mechanical | Explicit over clever | The task asks for gap analysis and optimization, not direct feature build | Treat as bug |
| 2 | Use 8-sample manual audit before codifying more automation | Mechanical | No one-off work | The user explicitly requires 3-10 samples before skill/script hardening | Full rewrite |
| 3 | Do not create another skill yet | Mechanical | Bias toward durability | Existing feline intake skill exists; this gap workflow needs approval after sample audit | Immediate skill sprawl |
| 4 | Do not set cron yet | Taste | Boil lakes, not oceans | Deterministic health automation is appropriate, but scheduled job should follow 3-10 clean manual samples and user approval | Cron judgment-heavy content |
| 5 | Prioritize MCP honesty and health severity before static export | Mechanical | User outcome first | A truthful query/lint surface matters before prettier exports | Build full site first |

## Current Recommendation

Do the next slice in this order:

1. Fix `scripts/mcp_server.py` capability truth.
2. Add a health action when bootstrap/thin-source reader pages exist.
3. Add obesity ordinary-routing guard.
4. Run the deterministic checks 3 times clean.
5. Then decide whether to install scheduled local health/compile reporting.

This is the smallest path from "research OS that works when carefully operated" to "living LLM wiki that keeps itself honest."

## Test Page

Static test page:

- [Karpathy gap test page](../../outputs/karpathy-gap-test-page-20260513.html)

This page is a local visual harness for the 8-sample gap audit. It is not the production static export.
