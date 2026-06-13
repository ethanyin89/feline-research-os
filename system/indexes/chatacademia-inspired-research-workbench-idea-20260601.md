---
id: system-chatacademia-inspired-research-workbench-idea-20260601
type: system
topic: operating-system
question_type: idea
language: zh
last_compiled_at: 2026-06-01
verification_status: source_checked
decision_grade: no
language_qa_status: not_checked
owner: codex
status: active
---

# ChatAcademia-Inspired Research Workbench Idea, 2026-06-01

## Classification / 归类

按 `$autoplan` 入口判断，这件事现在属于：

`想法`

不是：

- `方案`：还没有确定要做哪几个功能、改哪些文件、成功标准是什么。
- `检查`：不是在验证现有系统是否出错。
- `排查`：没有 bug、错误日志、失败路径。

当前最合适的 gstack 流程是：

`office-hours style idea shaping -> write a narrow design memo -> only then run /autoplan`

也就是说，先把念头变成一个可审查的计划文件。现在直接进 full `/autoplan` 会过早，因为 `/autoplan` 是“计划审查器”，不是“想法收束器”。

## Source Check

参考对象：

- ChatAcademia homepage: https://www.chatacademia.com/
- Checked date: 2026-06-01

网站公开页声称它提供面向研究者的 specialized AI agents，并覆盖从 idea 到 publication 的研究流程。公开页列出的模块包括 Analysis Foundry、Impact Beacon、Brainstorm Research Questions、Identify Research Gaps、Find Novel Research Questions、Find Papers、Claim Evidence、Find Grants、Reading Assistant、Find Citations、Hallucination Checker、Paper Graph、Extract Data、Literature Overview、Research Verdict、Mock Peer Review、Study Steward、Seminar Architect 等。

公开页还声称它连接多个学术数据库和 grant sources，包括 PubMed、Google Scholar、Europe PMC、OpenAlex、Semantic Scholar、Crossref、Grants.gov、NIH RePORTER、CORDIS、UKRI，并支持 Zotero、Mendeley、Google Drive 等文件/文献库入口。

**Boundary:** 这里只把 ChatAcademia 当成产品形态参考，不把它的能力、准确率、数据库覆盖、用户数或商业数据当成已验证事实。没有登录 app 实测，不能假设这些 agents 的真实质量。

## One-Line Judgment

这个想法对 feline-research-os 有帮助，但危险点也很明确：

`不要复制 ChatAcademia 的 agent 列表；只吸收能加强 evidence workflow 的少数能力。`

feline-research-os 的核心不是“通用学术 AI 平台”，而是：

`source-aware, claim-traceable feline evidence operating system`

所以任何新增模块都必须服务于三件事：

1. 更快找到可靠来源
2. 更稳地把 claim 绑定到 evidence
3. 更清楚地暴露 gap / boundary / next action

如果一个功能只是“看起来像研究平台”，但不能改善这三件事，就不该进来。

## Screenshot Observation, 2026-06-01

用户在 ChatAcademia 里测试了一个 query：

`feline diabetes pk pre-clin trail`

截图中最有价值的产品点不是 agent 数量，而是它的思考路径可见：

1. 先解释它如何理解 query：把问题理解为 feline diabetes、pharmacokinetics、preclinical trial。
2. 再并行搜索多个数据库：Semantic Scholar、PubMed、ArXiv、Google Scholar、ERIC、Europe PMC、OpenAlex、Crossref。
3. 每个搜索动作可展开，能看到 query、limit、offset、year filter、result count。
4. PubMed 搜索返回了一个 2025 结果：`Comparative Pharmacological and Pharmaceutical Perspectives on Antidiabetic Therapies in Humans, Dogs, and Cats.`
5. 系统继续进入 clarification / follow-up reasoning，而不是只给一个最终答案。

**Why this matters:** 这正好击中 feline-research-os 的弱点。当前 Ask the Vault 已经有 provenance，但检索过程对普通用户仍然像黑箱。用户看到答案时能看到 source IDs，却不一定知道系统“查了哪里、没查到哪里、为什么只用了这些 source”。

**Boundary:** 截图只能证明这个交互形态存在，不能证明 ChatAcademia 的检索质量、数据库覆盖完整性或结果准确性。

## Product Lesson From Screenshot

应该吸收的不是：

`multi-database academic agent`

而是：

`transparent research trace`

也就是在 feline-research-os 里，每次回答或 claim verification 都显示一条可审计路径：

| Step | Feline OS Translation |
|------|-----------------------|
| Interpret query | 把用户问题拆成 disease / concept / task / evidence need |
| Search internal vault | 显示搜了哪些 topic pages 和 source cards |
| Search external sources, optional | 只在用户明确要求 fresh / outside evidence 时调用 PubMed/Crossref |
| Show filters | disease, year, extraction_depth, verification_status, decision_grade |
| Show result count | found / not found / excluded because title_only or candidate |
| Ask clarification | 当 query 里有 typo 或概念歧义时，先澄清 |

这个比做 20 个 agents 更重要。

## New Candidate Mode: Research Trace

在原来的 3-mode 产品形态上，可以加一个横向能力，而不是新增一个大模块：

`Research Trace`

它不是单独入口，而是 Ask / Verify Claim / Find Gap 的共同输出层。

每次回答都可以显示：

```text
Interpreted as:
  disease: diabetes
  task: pharmacokinetics / preclinical evidence
  source need: paper-level evidence

Searched:
  topics/diabetes: 12 hits
  raw/papers/src-diabetes-*: 7 hits
  system/indexes/source-depth-map: checked

Excluded:
  title_only cards: 3
  no matching source_ids: 4

Used:
  src-diabetes-...

Confidence:
  abstract-level / full extraction / needs source search
```

This is the product move.

It makes the system feel more research-native without weakening the no-fake-data rule.

## Six Forcing Questions

### 1. 谁真的会痛？

当前最真实的用户不是泛学术研究者，而是：

- 维护者：需要持续 ingest、extract、compile、health check。
- 普通读者：需要问一个 feline disease 问题，得到带来源边界的答案。
- 研究合作者：需要快速知道某个 disease branch 证据强弱、缺口、下一步材料。

所以需求不是“我要 20 个研究 agents”。

真实需求更窄：

`我想知道这个 vault 里某个 claim 到底有没有证据，证据够不够，缺哪类 paper。`

### 2. 现在的替代方案是什么？

项目已有这些能力：

| Need | Existing Feline-Research-OS Surface |
|------|-------------------------------------|
| Find papers | source cards, reading plans, PubMed E-utilities workflow |
| Literature overview | disease synthesis indexes, dashboards, branch pages |
| Claim evidence | key-claim traceability tables, source_ids, evidence_policy |
| Hallucination check | provenance tags, health checks, title-only / thin-source gates |
| Extract data | deep extraction worksheets, structured abstract extraction files |
| Reading assistant | Streamlit Ask the Vault, query.py, search.py |
| Research verdict | decision_grade gating, confidence, verification_status |
| Paper graph | implicit source_ids graph, not yet visualized |

This is important. The project is not missing a product category. It is missing a small number of sharper workbench surfaces.

### 3. 最窄 wedge 是什么？

Do not build an agent marketplace.

The narrow wedge should be:

`Claim Evidence Workbench`

输入：

- 一个 claim
- 一个 disease/module
- 可选 source IDs

输出：

- 支持这个 claim 的 source cards
- 每个 source 的 evidence depth
- 是否有 quantified claim traceability
- 是否只能说 abstract-level
- 是否需要 deep extraction
- 是否应该写入 topic page

为什么是这个：

- 和现有 `source_ids` / `evidence_policy` / health checks 对齐。
- 直接服务 no-fake-data 规则。
- 不需要新数据库或新 UI 大改。
- 能复用 `scripts/search.py`, `scripts/query.py`, source cards, topic pages。

### 4. 哪些模块可以吸收？

Priority 1, close to current system:

| ChatAcademia-Like Module | Feline OS Translation | Why It Fits |
|--------------------------|-----------------------|-------------|
| Claim Evidence | Claim Evidence Workbench | 直接加强 no-fake-data 和 traceability |
| Hallucination Checker | Answer/claim verifier | 已有 provenance tags，可产品化 |
| Extract Data | Source-card extraction assistant | 已有 deep extraction / structured abstract 工作流 |
| Literature Overview | Disease branch overview generator | 已有 synthesis-index，可变成 ask-native surface |
| Research Verdict | Evidence verdict card | 对应 decision_grade / confidence / verification_status |
| Reading Assistant | Ask the Vault reading mode | 已有 Streamlit + query.py |

Priority 2, useful but not first:

| ChatAcademia-Like Module | Feline OS Translation | Constraint |
|--------------------------|-----------------------|------------|
| Paper Graph | Source-to-claim graph | 先用 static graph/report，不急着做 interactive UI |
| Identify Research Gaps | Gap finder per disease branch | 必须基于 source-depth-map，不许凭空生成 |
| Find Novel Research Questions | Research question generator | 只能生成 candidate questions，不能冒充 novelty proof |
| Mock Peer Review | Internal critique of outputs | 适合 dossiers/briefings，不适合 raw source facts |
| Study Steward | Evidence pipeline steward | 可能对应 health check dashboard |

Defer / probably no:

| Module | Why Not Now |
|--------|-------------|
| Find Grants | 当前项目不是 grant discovery 产品 |
| Seminar Architect | 输出型功能，离核心 evidence workflow 太远 |
| Poster Forge | presentation layer，容易分散 |
| Impact Beacon | 定义不清，容易变成空泛 scoring |
| Generic brainstorming | 已可用普通 LLM，没必要内建 |

### 5. 什么会让 6 个月后看起来很蠢？

最蠢的路线：

`把 ChatAcademia 的 20 个模块照抄成 sidebar 菜单。`

后果：

- 普通用户前门重新变复杂。
- 维护者多出一堆半成品按钮。
- no-fake-data 边界被“novel question / gap / verdict”这类高幻觉任务冲淡。
- Streamlit UI 变成功能陈列，而不是 research workflow。

更稳的路线：

`把 20 个模块压缩成 3 个 vault-native workbench modes。`

## Recommended Product Shape

### Mode 1: Ask

现有 Ask the Vault 的自然延续。

用户任务：

- 问一个 disease 问题
- 要一个 sourced answer
- 看 provenance 和 source list

不要加太多。

### Mode 2: Verify Claim

这是最值得做的新增模式。

用户任务：

- 输入一句 claim
- 系统回答：supported / weak / unsupported / needs extraction
- 给 source IDs、evidence depth、boundary

这个模式吸收：

- Claim Evidence
- Hallucination Checker
- Research Verdict
- Screenshot lesson: show the verification trace, not just the verdict

### Mode 3: Find Gap

这是第二个值得做的新增模式，但必须严格。

用户任务：

- 选 disease 或 branch
- 系统列出 coverage gaps
- 每个 gap 必须绑定到 source-depth-map / extraction_depth / topic page claim holes

这个模式吸收：

- Identify Research Gaps
- Find Novel Research Questions
- Literature Overview
- Paper Graph, but only as report first
- Screenshot lesson: show which internal/external search surfaces were checked and where the gap actually comes from

## Expansion Firewall

新增能力必须过这 7 条门：

1. 是否减少 fake-data 风险？
2. 是否复用已有 source cards / topic pages / health checks？
3. 是否输出 source IDs？
4. 是否暴露 evidence depth？
5. 是否能写入 inbox 而不是直接改 truth pages？
6. 是否能用 1 个 disease module 做小实验？
7. 是否不会增加普通用户入口数量？

任何答案为 no 的功能，默认不做。

## First Experiment

最小实验不是新 UI。

先做一个 CLI / report：

```bash
python3 scripts/claim_evidence_workbench.py \
  --claim "Feline mammary carcinoma is often triple-negative/basal-like" \
  --disease cancer
```

预期输出：

- matched topic claims
- matched source IDs
- evidence depth per source
- verification_status per source
- boundary statement
- recommended action: safe / needs deeper extraction / unsupported
- research trace: interpreted query, searched surfaces, excluded weak hits, used sources

如果这个 CLI 在 cancer mammary carcinoma 上能给出靠谱结果，再考虑放进 Streamlit。

## What Is Not In Scope

不做：

- grant search
- generic academic agent marketplace
- automatic novelty scoring without source grounding
- citation generation per sentence unless source IDs are already known
- visual paper graph UI before static graph/report proves useful
- replacing current source-card workflow
- direct write-back into `topics/**` from a new agent

## Decision

当前决策：

`Research Trace is now accepted as a small cross-cutting product layer. Do not build the larger workbench yet. Shape Claim Evidence Workbench as the next narrow plan.`

Implemented first slice, 2026-06-01:

- `scripts/query.py` now returns a structured `research_trace` for routing, vault search, source loading, hop decisions, evidence loading, figure checks, and synthesis.
- `scripts/app.py` now renders a collapsed Research trace per answer and preserves it in chat history.
- README now documents Research trace as an audit trail.

下一步如果要继续：

1. 写一个 narrow implementation plan for `Claim Evidence Workbench`
2. 明确 affected files
3. 明确 test plan
4. 然后再运行完整 `/autoplan`

## One-Sentence Close

ChatAcademia 的启发是对的，但 feline-research-os 应该吸收的是 `claim-grounded research workflow`，不是 `many-agent product surface`。
