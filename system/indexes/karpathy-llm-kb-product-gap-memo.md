---
id: system-karpathy-llm-kb-product-gap-memo
type: system
topic: ckd
last_compiled_at: 2026-04-08
owner: codex
status: active
language: zh
---

# Karpathy LLM Knowledge Bases Product Gap Memo

这页不是在复述 Karpathy 那段话。

这页回答的是三个更实际的问题：

1. 这到底属于 `想法 / 方案 / 检查 / 排查` 里的哪一种
2. 你现在这个 vault，已经对上了多少
3. 如果真要把它做成产品，最窄的切口应该是什么

## 类型判断

这件事属于：

`想法`

不是方案，不是检查，也不是排查。

原因很简单。

Karpathy 那段描述的是一种工作方式和产品雏形：

- raw data 进入系统
- LLM 编译 wiki
- 再继续问、继续产出、继续回写
- 最后变成一个会复利的研究环境

这不是一个已经锁定边界的 implementation plan。
它是一个非常强的方法论种子。

## 这件事为什么值得认真看

因为它不是“再做一个笔记软件”。

它真正盯着的是一个很大的空白：

`知识工作者今天还没有一个真正以 LLM 为原生编译器的研究操作系统`

现在多数工具的问题是：

- 要么只是文件存储
- 要么只是聊天窗口
- 要么只是 RAG 包装
- 要么只是脚本拼起来的个人工作流

Karpathy 说的这一套，厉害的地方不在“有 wiki”。

厉害的地方在于：

`查询结果会沉淀回系统，系统会越用越厚，而且主要维护者是 LLM，不是人手工编辑。`

这才是产品感真正出现的地方。

## 你现在这个 vault，已经对上了多少

不是 0。

而且也不是“概念上像”。

更准确地说：

`你现在这个 feline-research-os 已经对上了 Karpathy 方案的大约 60-70% 结构。`

### 已经对上的部分

1. `raw -> source card -> topic/entity -> synthesis -> output -> write-back`
   这条主链已经在跑

2. 你已经有 Obsidian 作为 frontend

3. output 不是终点，而是会回写 topic / synthesis

4. health check 已经在做系统级纠偏

5. 你已经开始做 extra tools 的替代物
   比如：
   - source schema
   - deep extraction workflow
   - compile checklists
   - trust audit
   - claim audit protocol

### 还没对上的部分

1. 自动化还不够强

现在很多事情还是要靠我显式驱动：

- ingest
- deep extraction
- write-back
- claim audit

而 Karpathy 那个理想态里，很多维护动作应该更像后台编译。

2. 引用粒度还不够深

你现在更像：

- page-level traceability

不是：

- sentence-level auditability

3. search / retrieval 还是薄

你有 navigation、有 synthesis、有结构化 markdown。
但还没有一个真正稳定可复用的：

- wiki-native search layer
- claim lookup layer
- entity graph query layer

4. “可验证性”还在补，不是默认自带

这是你刚才最敏感地抓到的点。

系统已经比普通摘要堆强很多。
但还没强到：

- 默认 decision-grade
- 默认可外发
- 默认可替代原文核查

## 这个想法真正的用户是谁

不是所有人。

如果把用户说得太宽，这个方向就会死得很快。

最真实的第一批用户，不是“所有知识工作者”。

而是这类人：

- 有持续研究任务的人
- 需要反复累积、反复回查、反复输出的人
- 已经在用 Obsidian / markdown / papers / notes 的重度用户
- 对“单次聊天答案”不满足的人

你自己现在做的 feline CKD，就是一个很好的原型用户画像：

- 不是 casual search
- 不是一次性问答
- 是长期专题研究
- 需要 briefing、memo、slides、监管路径、证据分层

这类用户数量不算大，但痛点非常真。

## 最窄的产品切口是什么

不是“一开始就做通用 LLM knowledge base platform”。

那会很快变成一个边界巨大的空壳。

最窄、最真实、最能跑通的切口应该是：

`auditable research OS for high-stakes domain teams`

更具体一点：

- 医疗 / 生物 /药政 /产业研究
- 投资研究
- 法规与政策研究
- 复杂技术主题研究

这些领域共同特点是：

- 不只是想“找到答案”
- 更想“知道答案从哪来，能不能复查，能不能继续沉淀”

这就是你现在这个项目最有价值的启发。

不是“LLM 能帮我记笔记”。

而是：

`LLM 可以做知识编译，但只有在可审计和可回写的系统里，这件事才真的值钱。`

## 如果把它做成产品，真正的差异化不是什么

不是：

- 更大的 context window
- 更花的 graph view
- 更好看的 markdown 编辑器

这些都不是护城河。

真正的差异化应该是 4 个东西。

### 1. Compile Discipline

系统不是随便生成页面。

而是有明确层级：

- raw
- source
- topic
- synthesis
- output
- audit

### 2. Trust Controls

你已经补出来的这两页，其实就是产品核心：

- [CKD accuracy and verifiability audit](ckd-accuracy-and-verifiability-audit.md)
- [claim audit protocol](claim-audit-protocol.md)

这类东西不是“附属功能”。

这是这个产品和普通 AI notebook 最大的分水岭。

### 3. Write-Back Loop

所有查询和派生输出，都必须能沉淀回系统。

否则它只是一堆会过期的聊天记录。

### 4. Domain-Specific Operating Modes

不同领域要有不同 compile discipline。

比如：

- 研究型模式
- 监管型模式
- 投资 memo 模式
- literature review 模式

而不是一个通用空 prompt 走天下。

## 这个想法现在最大的风险

不是技术风险。

最大的风险是：

`看起来什么都能做，所以最后什么都不锋利。`

常见死法会是：

1. 做成一个大而全 workspace
2. 加很多 ingestion connector
3. 加很多 graph / search / chat 面板
4. 但没有真正解决：
   - 可信度
   - 编译纪律
   - 决策分层
   - 输出回写

那就只会得到一个更复杂的笔记工具。

## 如果按 YC / office-hours 的角度问，这个方向最硬的 forcing question 是什么

不是：

`能不能做出来`

而是：

`有没有一类用户会因为“可审计的知识编译”而明显换工具、明显改变工作流`

我认为答案是：

有。

但必须是高痛感、小而深的人群。

不是泛大众知识管理。

## 最值得做的第一版，不是平台，而是楔子

如果真把这件事往产品方向推，第一版不该是：

“一个通用知识库操作系统”

第一版更应该像：

`for one high-stakes workflow, build the best auditable LLM research loop`

例如：

- 医药 / 兽医文献研究 loop
- regulation route memo loop
- investment thesis research loop

然后把下面这套打磨到极强：

1. ingest
2. compile
3. ask
4. output
5. write-back
6. audit

这条链一旦在一个 vertical 里强到离谱，平台才会自然长出来。

## 对你当前项目最直接的启发

对你来说，这段 Karpathy 文本最有价值的地方，不是让你“再建一个新产品”。

而是帮你确认：

`你现在做的 feline-research-os，不是在瞎堆笔记，而是在摸一个真实产品形态。`

但也要很清醒：

你现在最薄弱的，不是 compile 层。

你现在最薄弱的，是：

- citation 粒度
- verification status
- language QA
- decision-grade gating

也就是说，你离“可用”已经不远。
你离“可信到能承载高风险研究判断”，还差控制层。

## 最后一句判断

如果用一句话压缩这个想法：

`Karpathy 提到的不是一个花哨工作流，而是一类还没被好好做出来的产品：auditable, write-back-native, LLM-operated research OS。`

而你现在这个 vault，已经不是在旁观这个方向了。

你已经在里面了。
