# Handoff: June 6 Architecture Recovery 2026-06-11

**Status:** Context Recovery Complete — Awaiting User Decision
**Branch:** `idea-chatacademia-research-workbench`
**Date:** 2026-06-11 22:45
**Critical Discovery:** June 6 完整架构设计从未实施

---

## 本次Session核心发现

### 1. Context丢失确认

用户发现我像第一次阅读 Research OS 材料。经核实：

- **June 6 (2026-06-06)** 产出了 534 行完整架构文档
- 该文档定义了 Research Agent Answer Pattern、六层架构、Evidence Card schema、Research Record schema、Harness Loop 等
- **后续 session 均未读取该文档**，导致重复发散

证据：`/Users/jiawei/Downloads/260606-handoff(1).md`

### 2. 今日工作实为重复

| 今天的"发现" | June 6 已定义 |
|-------------|--------------|
| DOI链接必须真实 | `source_id: PMID/PMCID/DOI` |
| 需要 research value statement | "Why this matters" 组件 |
| 需要 Quick take | 第5组件 |
| 需要 Next research moves | 第7组件 |
| 需要结构化输出 | 完整7组件模式 |

### 3. DOI问题已修复

测试页面的占位符链接已替换为真实DOI：
- `10.1177/1098612X19831519` — ISFM Guidelines
- `10.1177/1098612X13495241` — Current Therapies
- `10.1177/1098612X13495234` — Pathophysiology

---

## June 6 架构核心摘要

### Research Agent Answer Pattern（标准输出）

```
1. Query interpretation — 系统如何理解问题
2. Retrieval scope — 检索来源、策略、优先级
3. Ranked evidence cards — 排序后的证据卡片
4. Why this matters — 每条证据的使用价值
5. Quick take — 证据地图总结
6. Gaps / uncertainty — 缺口与不确定性
7. Next research moves — 下一步研究分支
```

### 六层架构

```
1. Human-in-the-loop Research Workspace
2. Professional Team Mode (Strategist → Coordinator → Associates → Verifier)
3. Research Pipeline (query → retrieval → compression → reflection → synthesis)
4. Research Record (persistent structured output)
5. Retrieval Memory (low-cost state recovery)
6. Data Quality & Verification
```

### Evidence Card Schema

```yaml
evidence_card_id: string
title: string
source_type: pubmed | pmc | guideline | internal_note | protocol | uploaded_file
source_id: PMID/PMCID/DOI/file_path/url
species: cat | dog | human | mouse | mixed | unknown
disease: string
study_type: guideline | review | original_research | case_series | other
biomarkers: [string]
use_case: [diagnosis, enrollment, efficacy_endpoint, safety_monitoring, prognosis, model_validation]
key_finding: string
limitations: string
evidence_strength: high | medium | low
last_reviewed: date
```

### Harness Loop (RALPH)

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

## 当前实施状态

### 已存在 ✅

| 组件 | 位置 | 状态 |
|------|------|------|
| Source cards with DOI | `raw/papers/src-*.md` | `links.doi` 字段存在 |
| Source URL | `raw/papers/src-*.md` | `links.url` 字段存在 |
| Evidence level | `raw/papers/src-*.md` | `evidence_level` 字段存在 |
| Species tagging | `raw/papers/src-*.md` | `species: feline` 存在 |
| Disease tagging | `raw/papers/src-*.md` | `diseases: [CKD]` 存在 |
| Evidence policy | `raw/papers/src-*.md` | `quoted_fact`, `source_supported_conclusion`, `llm_inference` 存在 |
| 测试页面 | `system/indexes/presentation-logic-test-page.html` | DOI已修复 |

### 未实施 ❌

| 组件 | June 6 定义 | 当前状态 |
|------|------------|---------|
| Research Agent Answer Pattern | 7组件结构化输出 | 未实施 |
| Research Record 持久化 | YAML schema | 无实现 |
| Harness Loop | 7步验证流程 | 无实现 |
| Search Depth Controller | quick/standard/deep/audit | 无实现 |
| Verifier rules | 物种、证据、方案检查 | 无实现 |
| Agent Profiles | 8个专家角色 | 无实现 |
| PMID/PMCID | 标准字段 | 部分缺失 |
| use_case | 使用场景分类 | 缺失 |
| biomarkers | 生物标志物数组 | 缺失 |

---

## 待决问题

June 6 文档结尾提出的问题从未被回答：

> "下一步你希望我把这些材料收束成 Feline Research OS v0.1 Architecture，还是直接转成 Streamlit 项目的模块/文件结构和实现路线？"

**选项：**

**A) 创建 `ARCHITECTURE.md`** — 把 June 6 设计固化到仓库中，未来 session 可直接读取

**B) 实施路线图** — 把 June 6 schemas 映射到 `scripts/` 和 `raw/papers/` 的代码改动

**C) 两者都做** — 先 ARCHITECTURE.md，再实施路线图

---

## 关键文件位置

| 文件 | 用途 |
|------|------|
| `/Users/jiawei/Downloads/260606-handoff(1).md` | **权威来源** — June 6 完整架构 (534行) |
| `/Users/jiawei/Desktop/raw-2.md` | Research OS 理念文档 |
| `HANDOFF-2026-06-11-ARCHITECTURE-GAP.md` | 本次 gap 分析 |
| `system/indexes/presentation-logic-test-page.html` | 测试页面（DOI已修复）|
| `raw/papers/src-ckd-003.md` | Source card 示例（有DOI）|

---

## 流程修复建议

### 防止未来 Context 丢失

1. **ARCHITECTURE.md 必须在仓库内** — 不能只在外部 handoff 文件
2. **关键 schema 必须在仓库内** — 不能只在对话中
3. **Handoff 文档必须引用仓库文件** — 不能是唯一副本

### 推荐的仓库结构（来自 June 6）

```
/pages
  1_Research_Console.py
  2_Evidence_Cards.py
  3_Research_Records.py
  4_Verifier_Dashboard.py

/core
  task_evaluator.py
  search_depth_controller.py
  retrieval.py
  evidence_card.py
  gap_checker.py
  verifier.py
  record_store.py
  synthesis.py

/data
  research_records/
  evidence_cards/
  verifier_rules/

/prompts
  strategist.md
  evidence_extractor.md
  gap_checker.md
  verifier.md
  final_synthesizer.md
```

---

## Resume Instructions

1. **读取本文档**获取 context
2. **读取 June 6 原始文档**（如需细节）：`/Users/jiawei/Downloads/260606-handoff(1).md`
3. **确认用户选择**：A (ARCHITECTURE.md) / B (实施路线图) / C (两者)
4. **执行选择的路径**

---

## 约束备忘

```
1. June 6 架构是权威来源 — 不要重新发散
2. DOI 链接必须真实可用 — 占位符不可接受
3. Source cards 已有 70% 数据 — 补充而非重建
4. Research Agent Answer Pattern 是核心差异化 — 优先实施
5. 下一步应收束而非发散
```

---

**Created:** 2026-06-11 22:45
**By:** Claude Code
**Key Insight:** June 6 架构完整但从未实施；今日工作是重复发现

