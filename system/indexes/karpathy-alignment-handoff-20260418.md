---
title: Karpathy LLM Wiki Alignment — Full Handoff
date: 2026-04-18
status: active
from: claude-opus-4-6 (session 2)
to: codex (next session)
---

# Karpathy LLM Wiki Alignment — Handoff to Codex

## 30 秒现状

项目已从 Karpathy 7 层框架的 ~4/7 对齐推进到 **7/7 全部对齐**。不再有架构层面的缺失，剩下的全部是执行层面的内容工作和运维配置。

## 验证命令（先跑这 5 条）

```bash
python3 scripts/test_query.py                                    # 68/68 pass as of 2026-04-21
find raw/images -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" \) | wc -l  # 8 images
python3 scripts/search.py "phosphorus" --scope raw --limit 3     # search tool works
python3 scripts/compile_trigger.py --sources src-ckd-001 --json | python3 -m json.tool | head -5  # compile trigger works
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' | python3 scripts/mcp_server.py  # MCP server works
```

## 数字快照（2026-04-18 核实；2026-04-22 Diabetes sync updated counts）

| 指标 | 数值 |
|------|------|
| 总 .md 文件 | 638（不含误写的 nested `Users/` duplicate tree） |
| Paper source cards | 120（CKD 24 / FIP 24 / HCM 24 / IBD 24 / Diabetes 24） |
| Regulation source cards | 14 |
| Topic pages | 83 |
| System indexes | 308 |
| Deep extraction files | 120（5 disease modules × 24） |
| Verified images on disk | 8（全部 CKD） |
| Candidate image references（未下载/未验证） | CKD 2 / FIP 10 / HCM 10 / IBD 10 / Diabetes 1 |
| Marp slides | 15（5 disease × en/zh/working） |
| matplotlib 图表 | 3（endpoint-radar / source-coverage / maturity-bar） |
| 测试 | 68/68 pass |
| Conflict register tensions | 13（覆盖 19 source cards） |
| Unresolved questions | ~15 条（来自 6 张 source cards） |

### Source card 提取状态

| 病种 | extracted / deep_extracted | ingested | 说明 |
|------|---------------------------|----------|------|
| CKD | 24 | 0 | 全部完成 |
| HCM | 24 | 0 | 全部完成 |
| FIP | 24 | 0 | 24 / 24 round-1 worksheet 已完成，source cards 已回写为 `deep_extracted` |
| IBD | 24 | 0 | 24 / 24 round-1 worksheet 已完成，source cards 已回写为 `deep_extracted` |
| Diabetes | 24 | 0 | 24 / 24 round-1 worksheet 已完成，source cards 为 `extracted`，且 24 / 24 已是 explicit `full`；2026-04-21 已进入 briefing / dossier / slides output surface |

## 本轮新建文件

| 文件 | 作用 | 行数 |
|------|------|------|
| `scripts/search.py` | 全文搜索，支持 regex / scope / LLM format；被 query.py 自动调用做 search pre-heat | 216 |
| `scripts/compile_trigger.py` | 检测 source card 变更 → 输出下游 recompile queue；支持 git diff / --since / --sources | 234 |
| `scripts/mcp_server.py` | MCP server，暴露 vault_search / compile_check / source_list；JSON-RPC over stdio | 245 |
| `scripts/charts.py` | matplotlib 图表生成：endpoint-radar / source-coverage / maturity-bar | 316 |

## 本轮更新文件

| 文件 | 变更 |
|------|------|
| `scripts/query.py` | +search pre-heat、+`--save-to-inbox` flag、+`write_to_inbox()`、synthesis question_type 路由改为 None（不过滤） |
| `scripts/test_query.py` | 54 → 68 tests |
| `system/indexes/conflict-register.md` | 5 → 13 tensions，全 24 张 CKD deep-extraction 审阅完成 |
| `system/indexes/karpathy-gap-analysis.md` | 差距矩阵从 04-11 更新到 04-18 |
| `requirements.txt` | +matplotlib |
| `README.md` | +search.py 用法、+`--save-to-inbox` 示例 |

## 代码架构图

```
scripts/
├── query.py          (1192 行) — 核心 Q&A pipeline：route → hop → search pre-heat → synthesize
│   ├── imports search.py            — 自动 pre-filter 相关 source cards
│   ├── write_back()                 — → outputs/qa/
│   └── write_to_inbox()             — → inbox/{disease}/ (NEW)
├── search.py         (216 行)  — 全文搜索，vault_search() 可独立或被 import
├── compile_trigger.py (234 行) — source card 变更检测 → recompile queue
├── mcp_server.py     (245 行)  — MCP server，3 个 tools
├── charts.py         (316 行)  — matplotlib 图表生成
├── app.py            (400 行)  — Streamlit chat UI
├── test_query.py     — 68 tests as of 2026-04-21
└── run_acceptance_checklist.py      — 验收检查
```

## query.py 关键机制

### figure_type routing

文件名格式：`src-{disease}-{id}-{figure_type}-{description}.ext`

第 4 段（0-indexed [3]）是 figure_type。当前在磁盘上的 8 张图：

| 文件 | figure_type | 哪些 question_type 会展示 |
|------|-------------|------------------------|
| src-ckd-001-mechanism-schematic.jpg | mechanism | mechanism |
| src-ckd-001-mechanism-risk-factor-summary.jpg | mechanism | mechanism |
| src-ckd-017-imaging-pathology-classification-panel.jpg | imaging | recognition |
| src-ckd-017-outcome-upc-by-subtype-table.png | outcome | endpoints, treatment, regulatory |
| src-ckd-022-outcome-time-course-gfr-creatinine-table.png | outcome | endpoints, treatment, regulatory |
| src-ckd-022-pathology-histopath-findings-table.png | pathology | synthesis（无过滤） |
| src-ckd-024-outcome-biomarker-comparison-table.png | outcome | endpoints, treatment, regulatory |
| src-ckd-024-outcome-biomarker-landscape.jpeg | outcome | endpoints, treatment, regulatory |

`synthesis` question_type 的 figure_type_hint 是 `None`，不做过滤，展示所有可用图。

### search pre-heat

query.py routing 之后、hop loop 之前，自动调用 `vault_search(question, scope="raw", limit=5)`，把搜索到的 source cards 自动 load 进 context。这意味着即使 router LLM 遗漏了某个相关 source card，搜索层也能补上。

### provenance badges

三级：
- `[quoted_fact: src-ckd-001]` — 绿色 #16a34a，直接引用
- `[source_supported_conclusion: src-ckd-001, src-ckd-024]` — 琥珀色 #ca8a04，基于证据推断
- `[llm_inference]` — 灰色 #6b7280，超出证据的推理

### media_type 推导

`_EXT_TO_MEDIA_TYPE` dict：.jpg/.jpeg → image/jpeg，.png → image/png，.gif → image/gif，.webp → image/webp。

## Karpathy 7 层对齐状态

| 层 | 工具/文件 | 状态 |
|----|----------|------|
| Data ingest | raw/papers/ + raw/images/ | ✅ 120 paper cards + 8 verified images |
| Compile | topics/ + compile_trigger.py | ✅ 83 topic pages + 自动 recompile queue |
| Wiki (IDE) | Obsidian | ✅ |
| Q&A agent | query.py + search.py | ✅ route + hop + search pre-heat + vision + provenance |
| Output | slides + charts.py + write-back | ✅ 15 slides + 3 charts + inbox write-back |
| Linting | linting-schedule.md + checklist scripts | ⚠️ 定义完整，cron/CI 未配置 |
| Extra tools | search.py + mcp_server.py | ✅ 全文搜索 + MCP |

## 给 Codex 的任务清单（按优先级）

### P0：内容工作（不需要 API key）

1. **Continue FIP / IBD memo-level write-back / state sync**
   - 24 / 24 round-1 worksheet 已存在，下一步不是重做 worksheet
   - dashboard / synthesis / unresolved 的第一轮 state sync 已开始
   - 下一步继续把 worksheet 的结构判断回写到 memo owners、`source-depth-map` 和更广的系统 state

2. **src-ckd-013 candidate 图片下载**
   - 2 张 candidate 在 source card 里但磁盘上不存在
   - 之前 blocked on ScienceDirect 403 / Nottingham repository Cloudflare challenge
   - DOI: `https://www.sciencedirect.com/science/article/abs/pii/S0167587721000921`

### P1：运维配置

3. **git pre-commit hook 配置 compile_trigger.py**
   - 在 `.git/hooks/pre-commit` 里加 `python3 scripts/compile_trigger.py`
   - 或者用 CI 跑

4. **linting cron 启动**
   - `system/health-checks/linting-schedule.md` 已定义规范
   - 需要实际配置定期执行

### P2：内容质量

5. **FIP/HCM/IBD candidate 图片下载**
   - FIP: 10 candidate references across source cards
   - HCM: 10 candidate references across source cards
   - IBD: 10 candidate references across source cards
   - These are references, not verified files on disk; preserve the `candidate-` gate until each image/table is checked against the source label.

6. **conflict / unresolved / source-depth owners 扩展到 FIP / HCM / IBD**
   - FIP / IBD 当前没有发现需要仲裁的直接 source-to-source conflict
   - 下一步重点是 unresolved questions 和 broader owner state，而不是硬造冲突条目

7. **Diabetes owner-state integration**
   - Diabetes 已有 `24/24` source cards 和 `24/24` round-1 worksheets
   - 2026-04-21 已补第一套 briefing / dossier / slides outputs，并完成 24/24 explicit full source-card depth
   - 下一步不是重做 extraction 或普通 source-card thickening，而是只在输出需要时做 non-U.S. regulatory deepening 或 full-text clinical deepening

### P3：可选优化

8. **vault_query MCP tool**
   - 当前 mcp_server.py 暴露了 search/compile/source_list
   - 完整的 route+hop+synthesize 需要 API key，可以加为第 4 个 tool

9. **更多 chart 类型**
   - conflict-register heatmap
   - source card extraction progress dashboard
   - cross-disease endpoint comparison

## 约束条件（每次交给新模型前必须传达）

```
1. 不用 RAG / 向量检索。专科兽医词汇会破坏余弦相似度，架构决策已锁定。
2. 路由机制：query.py → question-router.md → topic pages + source cards。
3. 三层证据标签必须保留：[quoted_fact] / [source_supported_conclusion] / [llm_inference]
4. 文件名规范：src-{disease}-{id}-{figure_type}-{description}.ext
5. candidate- 前缀 = 未验证，不会进入 vision pipeline。去掉前缀前必须核对原文 figure/table 标签。
6. 测试基线：python3 scripts/test_query.py（68/68 pass）
7. AI 写的 wiki 页面先进 inbox/，人工确认后 promote — 见 system/protocols/ai-content-workflow.md
8. 不要伪造 figure 编号。如果没有打开原文核对，不要把 candidate-xxx 改成 fig1/table2。
```

## 不要重做

- scripts/query.py（1192 行，稳定）
- scripts/search.py（稳定）
- scripts/compile_trigger.py（稳定）
- scripts/mcp_server.py（稳定）
- scripts/charts.py（稳定）
- scripts/test_query.py（68 tests 全过）
- CKD source cards（24/24 extracted）
- HCM source cards（24/24 extracted，3 张 frontmatter disease label 待统一）
- CKD deep-extraction files（24/24 完成）
- FIP deep-extraction files（24/24 完成）
- conflict-register CKD section（13 tensions 完成）

## 关键文件速查

| 用途 | 文件 |
|------|------|
| 差距分析 | `system/indexes/karpathy-gap-analysis.md` |
| 冲突登记 | `system/indexes/conflict-register.md` |
| 未解问题 | `system/indexes/unresolved-questions.md` |
| 深挖队列 | `system/indexes/source-depth-map.md` |
| 图片 manifest | `system/indexes/ckd-image-ingest-manifest-20260416.md` |
| 下载检查 | `system/indexes/ckd-image-download-checklist-20260417.md` |
| AI 内容流程 | `system/protocols/ai-content-workflow.md` |
| Linting 规范 | `system/health-checks/linting-schedule.md` |
| 问题路由 | `system/indexes/question-router.md` |
| 深挖 prompt | `system/prompts/deep-extraction-prompt-v1.md` |
