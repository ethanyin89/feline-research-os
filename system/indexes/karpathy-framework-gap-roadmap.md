---
id: system-karpathy-framework-gap-roadmap
type: system
topic: ckd
last_compiled_at: 2026-04-08
owner: codex
status: active
language: zh
---

# Karpathy Framework Gap Roadmap

这页只回答一个问题：

`如果要确保当前 vault 持续在 Karpathy 的 LLM Knowledge Bases 框架内推进，还差哪 5 个具体能力？`

不是泛泛“还差很多”。

而是：

- 具体缺什么
- 为什么缺
- 现在在 vault 里对应哪一层
- 先补哪个最值钱

## 当前对齐度

当前 `feline-research-os` 已经对上 Karpathy 框架的大约 `60-70%`。

已经对上的是主骨架：

- raw
- compile
- output
- write-back
- health check

真正还缺的，不是更多内容层。

真正还缺的是：

`让这套系统从“能编译”走到“能持续可信地编译”的控制层和工具层。`

再进一步说，还缺的是：

`让重复工作尽快离开“再次下指令”状态，进入“被系统资产接住”状态`

## Gap 1: Verification Status Layer

### 现在缺什么

当前页面虽然有：

- `confidence`
- `status`
- `limits / caveats`

但还没有一个统一字段明确写：

- 这页是不是 abstract-weighted
- 是否 full-text reviewed
- 是否 deep extracted
- 是否 decision-grade

### 为什么这很关键

Karpathy 的框架天然会越用越厚。

如果没有 verification status，系统会越来越像：

- 内容越来越多
- 但没人知道哪些能直接信

这会让 compiled wiki 失去真正的研究价值。

### 最值钱的动作

给高价值页面增加统一标记，例如：

- `verification_status: abstract_weighted | source_checked | deep_extracted | audited`
- `decision_grade: no | provisional | yes`

### 优先级

`P0`

## Gap 2: Sentence-Level Traceability

### 现在缺什么

当前已经有：

- source_ids
- evidence map
- source card structure

但还没有做到：

- 关键句直接挂 source id
- 更细一点，关键句能回到 source 内的具体位置

### 为什么这很关键

Karpathy 的方法能跑起来，不代表它天然可审计。

一旦 topic / synthesis / output 越来越厚，page-level traceability 就会开始不够用。

### 最值钱的动作

从最高价值页面开始，不要全库一次性做。

优先给这些页加 sentence-level traceability：

- [synthesis-index.md](../../topics/ckd/synthesis-index.md)
- [translation-brief.md](../../topics/ckd/translation-brief.md)
- [regulatory-brief.md](../../topics/ckd/regulatory-brief.md)
- 核心 route memos

### 优先级

`P0`

## Gap 3: Language QA Layer

### 现在缺什么

你刚才已经抓到了最现实的问题。

当前系统有：

- bilingual policy
- bilingual rules

但还没有：

- 对中文输出做独立 QA
- 对双语输出做术语一致性检查
- 对“弱结论被翻成强结论”做专门检查

### 为什么这很关键

Karpathy 那个工作流里，LLM 维护 wiki 是核心。

一旦语言层不稳，用户就会开始合理怀疑：

- 事实边界也不稳

尤其对中文输出，这是不能回避的问题。

### 最值钱的动作

新增一个明确的 `language qa protocol`：

- 错别字检查
- 术语表
- 强弱语气审计
- bilingual drift 检查

### 优先级

`P0`

## Gap 4: Wiki-Native Retrieval Layer

### 现在缺什么

当前你已经有：

- navigation
- dashboard
- synthesis
- source index

但还没有一个真正稳定的：

- wiki-native search layer
- claim lookup layer
- entity / topic quick query layer

### 为什么这很关键

Karpathy 特别强调的一点是：

不一定要上 fancy RAG，
但系统自己要能把重要索引和摘要维护好。

你现在已经有索引雏形。
但还没有一个真正可以被 LLM 稳定调用的检索层。

### 最值钱的动作

不是先做复杂数据库。

而是先做一个很朴素但稳定的 wiki-native 工具层：

- source / topic / entity 索引统一入口
- claim 查找
- page 关系快速查询

### 优先级

`P1`

## Gap 5: Background Compile Discipline

### 现在缺什么

当前很多关键动作还是显式人工触发的：

- ingest
- deep extraction
- write-back
- trust audit
- route memo compile

### 为什么这很关键

Karpathy 的理想态更像：

- 新 source 进来
- 系统自动知道先去哪里编译
- 哪些页需要 refresh
- 哪些页应该提示 health check

如果一直靠“人每次提醒模型做下一步”，那它还是 workflow，不是 OS。

这也是当前项目和 Garry Tan 那条 durable-agent 原则真正接上的地方：

- 第一次先手工跑通
- 第二次之前把模式编成系统资产
- 后续默认复用，而不是继续靠重复提醒

### 最值钱的动作

不是一上来全自动。

而是先做最小后台编译纪律：

1. 新 source ingest 后，自动提示候选 write-back targets
2. 高价值 source 满足条件时，自动进入 deep extraction queue
3. 高价值 topic 变化后，提示哪些 output 可能过期

### 优先级

`P1`

## 优先级总表

| Priority | Gap | Why |
|---|---|---|
| P0 | Verification status layer | 不先标清楚“能信到哪”，系统会越写越虚 |
| P0 | Sentence-level traceability | 不补这一层，compiled 页很快会失去可审计性 |
| P0 | Language QA layer | 中文与双语输出是你当前最直接的信任触发点 |
| P1 | Wiki-native retrieval layer | 这是从“会写”走向“可持续问答”的关键 |
| P1 | Background compile discipline | 这是从 workflow 走向 OS 的关键 |

## 最推荐的执行顺序

### Round 1

- verification status
- sentence-level traceability
- language QA

这是第一组。

因为它们共同解决的是：

`可信度`

### Round 2

- wiki-native retrieval
- background compile discipline

这是第二组。

因为它们共同解决的是：

`规模化运行`

## 和当前 vault 的对应关系

### 已经有雏形的

- trust audit
  [ckd-accuracy-and-verifiability-audit.md](ckd-accuracy-and-verifiability-audit.md)

- claim discipline
  [claim-audit-protocol.md](claim-audit-protocol.md)

- compile workflow
  [deep-extraction-workflow.md](deep-extraction-workflow.md)

- LLM KB mapping
  [how-this-project-runs-via-llm-knowledge-bases.md](how-this-project-runs-via-llm-knowledge-bases.md)

### 还需要补成系统能力的

- verification status standard
- sentence-level citation standard
- language QA protocol
- retrieval tool layer
- compile queue / refresh logic

## 一句最终判断

如果你要确保这个项目始终在 Karpathy 的框架内推进，真正该盯的不是“还要不要继续 ingest 新文献”。

真正该盯的是：

`这套系统有没有越来越像一个可审计、可回写、可持续维护的知识编译器。`

现在答案是：

`已经在路上，但控制层还没补完。`
