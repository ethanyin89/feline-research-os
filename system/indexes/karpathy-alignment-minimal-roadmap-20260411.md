---
id: system-karpathy-alignment-minimal-roadmap-20260411
type: system
topic: operating-system
question_type: plan
language: zh
last_compiled_at: 2026-04-11
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Karpathy Alignment Minimal Roadmap, 2026-04-11

这页只回答一个窄问题：

`如果要让这个项目更接近 Karpathy 想要的 LLM wiki，而且不重新发散成大平台，现在最小、最稳的升级顺序是什么？`

先读：

- [karpathy-difference-audit-20260411](karpathy-difference-audit-20260411.md)
- [karpathy-framework-gap-roadmap](karpathy-framework-gap-roadmap.md)
- [content-vs-frontend-collaboration-plan](content-vs-frontend-collaboration-plan.md)
- [karpathy-alignment-stop-rule-20260411](karpathy-alignment-stop-rule-20260411.md)

## 类型判断

这件事属于：

`方案`

不是再做一次检查。

因为差距已经基本看清了。

现在要解决的是：

- 先补哪一层
- 哪些先不做
- 怎么避免又做成一个“什么都想补”的空 roadmap

## 最短结论

如果目标是更接近 Karpathy 的 LLM wiki，最稳的路线不是：

- 先做更复杂的 UI
- 先做数据库
- 先做通用平台

而是 3 步：

1. `把 ask surface 从路由页压向答案面`
2. `把 retrieval 从页面入口压成统一 claim/entity/topic 查询层`
3. `把 write-back 与 stale-refresh 从人工感压成系统感`

一句话说：

`先补前台感知，再补工具层，再补后台默认行为。`

## 为什么不是先补更多内容

当前内容层已经不是最薄的地方。

现在最明显的差距不在：

- 页面不够多
- memo 不够多
- disease 不够多

而在：

- 用户问进去以后，还像不像在问一个活系统
- 用户能不能直接找到 claim / entity / topic 的最短答案面
- 用户能不能看见系统因为这次 query 变厚了

也就是：

`现在更该补查询体验和系统感，而不是继续横向扩页。`

## Round 1: Ask Surface Compression

### 目标

把当前的：

`query-guided navigation`

往前推成更像：

`question -> best answer surface`

### 这一轮具体补什么

不是重写前端。

而是先在内容层把最短答案面准备好。

优先做这 3 类资产：

1. `best answer surface`
   每个 disease 先明确：
   - 最强总览页
   - 最强 mechanism 页
   - 最强 workup 页
   - 最强 endpoint 页
   - 最强 treatment / regulatory 页

2. `answer-first prompts inside index pages`
   把 `ask-the-vault` 和 `question-router` 再往问题面压，不再只是“去哪页”。

3. `claim-first entry points`
   对最常见问题增加：
   - strongest current conclusion
   - what is still thin
   - verify next

### 这轮完成后的变化

用户会更少感到自己在“选页面类型”。

会更像：

`我问的是机制、诊断、endpoint、监管，系统马上把最合适的答案层抬出来。`

### 这轮不要做什么

- 不要先做 fancy chatbot shell
- 不要先改整套 UI
- 不要先做数据库检索

因为现在最缺的不是前端壳。

而是：

`内容层还没有把“最短答案面”压得足够明显。`

## Round 2: Unified Retrieval Layer

### 目标

把当前分散在：

- dashboard
- navigation
- source index
- synthesis
- verify-a-claim

里的查询入口，压成一个更统一的 retrieval 语法。

### 这一轮具体补什么

优先补 3 种查询，不要泛化。

#### 1. claim lookup

回答：

- 这个结论在哪？
- 最强支持来自哪几个 source？
- 应该先读 compiled page 还是 raw paper？

#### 2. entity lookup

回答：

- 这个 endpoint / mechanism / disease boundary 属于哪一层？
- 哪几页在高频使用它？
- 它当前是 core、support、frontier，还是 pending？

#### 3. topic relationship lookup

回答：

- 这个 topic 和哪些 topic 强相关？
- 哪张 synthesis 页最适合作为入口？
- 哪个 output 已经过期风险最高？

### 这一轮最小落地形态

不是做服务端。

先做稳定 markdown 资产和稳定查询约定。

例如：

- `claim-lookup protocol`
- `entity-lookup index`
- `topic relationship quick map`

先让 LLM 能稳定调用。

之后前端或工具层再接。

### 这轮完成后的变化

系统会更少像：

`整理得很好的文件树`

更像：

`带有统一查询语法的 wiki`

## Round 3: Visible Thickening + Background Compile Discipline

### 目标

把现在维护者才能感觉到的：

- query thickens system
- some outputs are stale
- some pages now deserve refresh

变成更明显的系统行为。

### 这一轮具体补什么

#### 1. write-back visibility

明确记录：

- 本次查询沉淀成了什么
- 落到了哪一层
- 为什么值得写回

#### 2. stale output cues

明确告诉系统和读者：

- 哪些 output 建立在旧 compiled state 上
- 哪些 disease dashboard 需要 refresh
- 哪些 bilingual page 需要跟进

#### 3. compile queue visibility

把当前隐含在维护者脑中的下一步，压成显式队列：

- what should densify next
- what should refresh next
- what should hold and not expand

### 这一轮完成后的变化

用户会更容易感觉到：

`这个系统不是静态文档库，而是在持续生长。`

维护者也会更少依赖记忆来维持一致性。

## 三轮优先级为什么是这个顺序

原因很简单。

当前最大的缺口不是可信度。

可信度层已经相对强。

当前最大的缺口是：

`用户是否能明显感觉到这是一个活 wiki，而不是一组整理良好的页面。`

所以顺序必须是：

1. 先补用户第一感知最强的 `ask surface`
2. 再补真正支撑 ask-native 的 `retrieval layer`
3. 最后再补把系统感做实的 `visible thickening + background compile`

如果反过来做，风险很大：

- 后台补了很多
- 用户还是没感觉
- 项目继续像研究文档系统，而不是活 wiki

## 什么不要现在做

下面这些动作，现在都不该抢主线。

### 1. 不要先做通用平台化

现在最危险的误判就是：

`既然方法对了，就开始做通用 LLM knowledge base platform`

这会立刻把问题从可做，变成空。

### 2. 不要先开更多 disease

四病种已经足够说明语法能不能复用。

现在继续开新 disease，只会稀释：

- ask surface 收口
- retrieval 统一性
- control thickness

### 3. 不要先做更复杂的 front-end display

如果答案面和 retrieval 语法还没收口，先做复杂前端只会让演示更好看，不会让系统更像活 wiki。

### 4. 不要把内容主线重新拉回“普通用户入口打磨”

当前内容侧的默认分工已经很清楚：

- content side 负责 truth / write-back / system reality
- frontend side 负责 presentation shaping

所以内容侧现在最应该做的是：

`把 ask-native 所需的 truth-layer and retrieval-layer asset 先压出来`

不是再继续做 landing-page 化。

## 最小执行清单

如果只做最小版本，下一轮只要完成这 5 件事就够了：

1. 给四病种各自明确 `best answer surfaces`
2. 把 `ask-the-vault` 和 `question-router` 再压成更强的问题面
3. 新增一套最小 `claim / entity / topic` 检索约定页
4. 新增 `stale / refresh / write-back visibility` 的显式状态页
5. 把这些变化同步回 cross-disease status audit

## 成功标准

如果路线是对的，完成后应该出现这 4 个变化：

1. 普通用户更少点导航页，更多直接命中答案面
2. 维护者更少靠记忆找 claim / entity / topic 关系
3. write-back 变得可见，而不是只存在于维护者脑中
4. 四病种看起来更像一套统一语法，而不是四套不同成熟度的资料岛

## 一句话收口

如果要更接近 Karpathy 的 LLM wiki，现在最稳的路线不是继续横向长大。

而是：

`先把问题入口压成答案面，再把查询压成统一检索层，最后把系统变厚这件事做得真正可见。`
