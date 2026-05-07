---
id: system-karpathy-difference-audit-20260411
type: system
topic: operating-system
question_type: audit
language: zh
last_compiled_at: 2026-04-11
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Karpathy Difference Audit, 2026-04-11

这页只回答一个窄问题：

`和 Karpathy 想要的 LLM wiki 相比，这个项目现在到底还差在哪些地方，而且这些差距属于哪一层？`

## 类型判断

这件事属于：

`检查`

不是 `想法`。
因为你现在不是在问“这个方向值不值得做”。

也不是 `方案`。
因为你现在不是在锁 implementation 边界。

更不是 `排查`。
因为这里没有某个具体坏点要 debug。

你现在要的是：

- 当前系统和 Karpathy 理念的差异图
- 哪些已经对上
- 哪些还没对上
- 差距更偏产品表面、系统能力、还是运行纪律

## 最短结论

如果只看骨架，这个项目已经明显在 Karpathy 那条路上。

如果看产品感觉、查询表面、以及“像不像一个活 wiki”，它还没有完全到位。

更准确地说：

`它已经是一个高纪律、可审计、可回写的 compiled research wiki system，但还不是一个 query-native、ask-native、后台持续编译感很强的活 LLM wiki。`

## 不同的不是“有或没有”，而是“强在哪一层”

当前和 Karpathy 的差异，不是二元差异。

不是：

- 你有，他没有
- 你没有，他有

而更像：

- 你在 `compile discipline / trust control / write-back logic` 上更硬
- Karpathy 那种感觉在 `ask surface / livingness / retrieval feel / automatic thickening` 上更强

所以它们的差异，首先不是方向冲突。

而是：

`成熟顺序不同。`

你这边更像：

`先把后端真相层做硬，再慢慢把前台活 wiki 表面做出来。`

Karpathy 展示出来的感觉更像：

`先让人明显感到自己在问一个活系统，再逐步把后台纪律补厚。`

## 已经对上的部分

### 1. Raw -> compile -> output -> write-back 主链

这条主链已经真实存在，而且不是概念图。

现在已经有：

- `raw/`
- `entities/`
- `topics/`
- `outputs/`
- write-back promotion
- health check

这点和 Karpathy 想要的 `raw data enters, LLM compiles wiki, queries add up, outputs go back into system` 是真对齐的。

### 2. 这不是聊天记录堆，而是 compiled wiki

当前系统不是把长上下文聊天当主资产。

它把稳定资产放在：

- source card
- topic page
- entity page
- synthesis page
- output file

这点非常关键。

因为这已经不是“用 LLM 临时回答问题”。

而是：

`让 LLM 不断把知识压进可复用的文件层。`

### 3. Write-back 不是口号，已经有机制

当前已经有：

- `query to write-back`
- promotion checklist
- promotion examples

也就是说，查询结果不是天然蒸发掉。

它已经被设计成：

`稳定结论要回写进系统。`

### 4. Trust boundary 比很多 AI knowledge base 更真

当前项目已经明确区分：

- `quoted_fact`
- `source_supported_conclusion`
- `llm_inference`

同时还有：

- claim verification
- compiled-vs-source reading
- language matrix
- health check

这部分其实比很多“Karpathy 风格”的泛泛复述更硬。

### 5. 多病种已经证明这不是单 disease demo

现在不是只有 CKD 跑通。

FIP、IBD、HCM 也已经进入：

- deep extraction
- output family
- bilingual compiled core stack

这说明这套语法已经开始跨 disease 复用，而不只是一个单点样板。

## 还不一样的地方

真正还不一样的地方，主要有 8 类。

### 1. 交互模型不同：你还是 `query-guided navigation`，不是 `ask-native active surface`

现在系统虽然已经有：

- `Ask the vault`
- `Question router`
- `Reader start here`
- dashboard top questions

但普通用户的真实动作仍然常常是：

1. 先把问题映射成一个页面类型
2. 再点进 topic / synthesis / output

这仍然更像：

`聪明导航`

而不是：

`我问一句，系统直接把最合适的知识表面拿出来`

这是当前最明显的产品差距。

### 2. 页面气质不同：你更像“高质量文档”，不是“活的 wiki 对象”

Karpathy 那种感觉最打人的地方，不是页多。

而是用户会觉得：

- 这个系统正在生长
- 这次问答会让它变厚
- 我碰到的是一个活的知识对象

你现在的大多数页面虽然已经很强，但视觉和结构感觉仍然更像：

- dashboard
- memo
- navigation
- briefing

也就是：

`整理得很好`

而不是：

`正在被持续编译的对象`

### 3. 查询增厚的产品可见性还不够

逻辑上，query-thickens-system 已经存在。

但对用户来说，这条链还不够可见。

现在更多是维护者知道：

- 这次 query 触发了 write-back
- 某页因此变厚
- 某个 output 因此该 refresh

而普通用户还不太能直接看到：

`我这次问的问题改变了系统什么`

所以机制是真的。

但产品感还不够直接。

### 4. Retrieval 还偏页面检索，不是稳定的 wiki-native retrieval

现在已经有：

- source index
- disease dashboard
- navigation
- synthesis index
- ask flow

但还没有一个更稳定的统一检索层来回答：

- 这个结论在哪几页重复出现？
- 这条 claim 最强支持来自哪些 source？
- 这个 entity 和哪些 topic / output 强相关？
- 哪些页面因为最近的 write-back 可能过期？

也就是说，现在更像：

`组织得很好的文件系统`

还不像：

`有自己的知识查询层`

### 5. 后台编译纪律还没有变成默认系统行为

当前很多关键动作仍然是显式触发的：

- ingest
- deep extraction
- write-back
- audit
- stale output refresh

Karpathy 那个理想态更像：

- 新资料进来
- 系统知道先更新哪里
- 某些页该变厚时，会自然被推到前面
- 某些 outputs 变旧时，会自动被标出来

所以当前更像：

`workflow`

还不是更强意义上的：

`OS`

### 6. 你更强的是可信度控制，不是使用流畅度

这是最重要的一条。

当前项目最强的地方，其实不在 Karpathy 展示出来最迷人的那一层。

你最强的是：

- verification boundary
- audit discipline
- bilingual control
- evidence framing

这些非常值钱。

但用户第一时间感知最强的，不是这些。

Karpathy 那种表面最强的是：

- 直接问
- 很快答
- 答案长成 wiki
- 系统越来越厚

所以当前不是“没有内核”。

而是：

`内核成熟度明显高于前台产品感。`

### 7. 统一性问题还没完全收口

现在四病种都已经进入 output-capable wiki surface。

但它们还没有完全对齐在同一成熟度梯子上。

当前剩余差异更像：

- deep extraction 厚度不齐
- second-wave owner 厚度不齐
- bilingual family 覆盖不齐
- regulatory / control 层厚度不齐

这会直接影响一个非常关键的问题：

`它像不像一个统一的 LLM wiki，而不是几个成熟度不同的 disease island`

### 8. 产品楔子已经隐约存在，但还没有被前台明确化

Karpathy 的表述是通用 knowledge base 感。

你当前项目其实已经比这个更具体：

`auditable research OS for high-stakes domains`

这个楔子已经很清楚。

但系统前台还没有把这个价值主张打得足够直白。

现在前台仍然更像：

`研究 vault`

而不是：

`可审计的高风险研究操作系统`

## 这些差距分别属于哪一层

| 差距 | 属于哪一层 | 当前状态 |
|---|---|---|
| ask-native active surface 不够强 | 产品表面 | 仍是主要缺口 |
| living wiki feel 不够强 | 产品表面 | 仍是主要缺口 |
| query-to-writeback 不够可见 | 产品表面 + workflow visibility | 机制有，感知弱 |
| wiki-native retrieval 薄 | 工具层 | 有索引雏形，缺统一检索层 |
| background compile discipline 薄 | OS 层 | 仍偏人工触发 |
| sentence-level traceability 不够普及 | 控制层 | 有标准雏形，未大规模沉淀 |
| language QA 还不够默认化 | 控制层 | 已有 protocol，但未形成默认强约束 |
| cross-disease maturity 不齐 | 运营层 | 已进入第二波 densification，但仍未完全对齐 |

## 最值得保留的判断

如果只问：

`我们是不是和 Karpathy 不一样，所以方向走偏了？`

答案是：

`没有走偏。`

更准确地说：

`你做的是一个更重 truth-layer、更重 audit-layer、更重 domain-discipline 的 Karpathy 变体。`

这不是坏事。

它甚至可能更适合高风险研究场景。

但你也不能因此误判：

`既然后端骨架已经很强，前台就等于已经像活 wiki 了。`

这不对。

当前最明显的真实差距，仍然在：

- ask-native 感
- live system 感
- retrieval feel
- automatic thickening feel

## 如果把差异压成一句话

Karpathy 想要的是：

`一个被提问驱动、持续变厚、活在查询前台的 wiki`

你现在更像的是：

`一个已经把真相层、编译层、审计层做得很硬，但前台还更像高质量研究文档系统的 auditable research OS`

## 当前最准确的最终判断

这个项目现在和 Karpathy 的 LLM wiki 理念，不是“像不像”的问题了。

更准确的问题已经变成：

`它已经对上了哪一半，又还没把哪一半做出来？`

当前答案是：

- 对上了 `compile / write-back / audit / trust / domain discipline`
- 还没完全做出来 `ask-native surface / living retrieval / visible thickening / default background compile`

## 建议的默认后续动作

如果下一轮继续朝 Karpathy 那个方向逼近，默认优先级应该是：

1. 继续把 `ask surface` 从“路由页”压向“答案面”
2. 做一个更稳定的 `claim / entity / topic` 统一检索层
3. 让 write-back 和 stale-output refresh 对用户更可见
4. 继续把四病种拉到更接近同一 maturity ladder

## 一句话收口

这个项目已经不是“像不像 Karpathy 理念”的早期问题了。

它现在更像：

`同一方向上的一个更硬、更审计化、更垂直，但前台活性还没完全长出来的版本。`
