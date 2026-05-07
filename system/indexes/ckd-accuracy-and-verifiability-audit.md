---
id: system-ckd-accuracy-and-verifiability-audit
type: system
topic: ckd
last_compiled_at: 2026-04-08
verification_status: audited
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
language: zh
---

# CKD 研究大脑的准确性与可核验性审计

这页回答的不是 CKD 内容本身。

这页回答的是：

`这套研究系统现在到底可信到什么程度？`

以及：

`哪些内容可以核验，哪些内容只能当工作判断？`

## 先给最短结论

当前这套 CKD research OS 不是“自动正确”的。

它更准确的状态是：

`部分可核验，部分可追溯，部分仍然只是工作层推断`

所以它已经不是一个黑箱，但也还远远不是一个“可直接替代原文核查”的系统。

## 为什么你刚才会警觉，是对的

你提到我中文回复里有错别字，这个警觉是对的。

因为错别字本身未必等于事实错误。
但它确实说明：

- 输出层可能出现粗糙问题
- 语言层会影响你对系统严谨度的判断
- 如果表述质量失控，用户会合理怀疑事实边界也可能失控

所以要分开看：

1. `语言层瑕疵`
   比如错别字、句子不顺、翻译漂移

2. `事实层瑕疵`
   比如把推断写成证据、把 review 写成 primary study、把 route-level 误写成 product-specific

第一类不一定直接证明第二类已经发生。  
但第一类确实是第二类风险的预警信号。

## 当前系统里，哪些机制是在降低幻觉风险

### 1. source card 有显式边界

source schema 已经强制分成：

- `quoted_fact`
- `source_supported_conclusion`
- `llm_inference`

这是当前最重要的防线。

因为它至少在结构上逼系统回答：

- 哪些是文献明确说的
- 哪些是从文献支持出来的结论
- 哪些只是模型工作推断

如果没有这一层，这套系统会立刻退化成普通摘要堆。

### 2. topic page 不是只写结论，也写不确定性

topic schema 里要求有：

- `Evidence Map`
- `Conflicts / uncertainty`
- `Gaps`
- `Next sources to ingest`

这很重要。

因为它让 topic 页不会只像“知识条目”，而会暴露：

- 它靠哪些 source 立起来
- 哪些地方还没补完
- 哪些结论其实还不稳

### 3. output 层也保留 evidence policy

briefing / dossier / slides 这些 output schema 也保留：

- `quoted_fact`
- `source_supported_conclusion`
- `llm_inference`

这说明系统没有把“正式输出”当成可以脱离证据边界的层。

这点是对的。

### 4. deep extraction 不是默认动作，而是高价值 source 才做

`deep extraction workflow` 明确写了：

- 不是每篇 paper 都深提炼
- 只有高复用、高价值 source 才进入深提炼
- promotion 要保守

这会降低“薄 source 被写出厚结论”的概率。

### 5. health check 已经在做结构级纠偏

health check 不只是查断链。
它已经明确在查：

- 旧话术残留
- 证据深度不均
- model / regulatory 被写得比 source 更强

这说明系统已经有自检意识，而不是只会累积内容。

## 但当前系统还没有强到哪里

下面这些问题，当前都是真实存在的。

### 1. 很多 source 还是 abstract-weighted

这在 health check 里已经被明确点出来了。

这意味着：

- 某些 source card 还不是全文级掌握
- topic 页的信心有时会跑在 source 深度前面

所以：

`可追溯`
不等于
`已充分验证`

### 2. topic 页没有逐句 citation 粒度

现在的 topic 页通常有 `source_ids` 和 `Evidence Map`。

这比普通笔记强很多。
但它还没有做到：

- 每个关键句子直接挂具体 source 位置
- 每个重要判断可以一跳回到原句级证据

所以目前更像：

`page-level traceability`

而不是：

`sentence-level auditability`

### 3. compiled layer 的判断仍可能超前

例如：

- treatment ranking
- product archetype
- route memo

这些页是有价值的。
但它们本质上是：

`工作层决策辅助`

不是“官方结论页”。

尤其 regulatory 这条线，当前 vault 自己也已经承认：

- 还是 route-level 为主
- 不是 decision-grade
- 缺 CKD-specific official guidance

所以这类页面必须被当成：

`structured internal reasoning`

而不是：

`final truth`

### 4. bilingual / 中文输出层存在表述漂移风险

只要有翻译，就一定有漂移风险。

系统虽然已经有 bilingual policy，但当前仍然没有做到：

- 每次双语输出都有独立 proofread
- 每次中文重写都有术语一致性检查
- 每次外显回复都经过语言 QA

你刚才看到的错别字，就是这一层的现实提醒。

## 我给这套系统当前可信度的分层

### A 层，当前最可信

- `raw source cards`
- 尤其是已经做过 deep extraction 的 source

原因：

- 有 DOI / URL
- 有 source-level structure
- 有明确的 limits / caveats

### B 层，可信但要回查

- `topic pages`
- `entity cards`
- `synthesis pages`

原因：

- 已经有 source_ids 和 uncertainty 结构
- 但仍然是 compiled judgment

用法：

- 可以当高质量研究导航
- 不能当“无需回原文”的最终证据

### C 层，工作层价值高，但不能当定稿

- `briefing`
- `dossier`
- `slides`
- `treatment ranking memo`
- `product archetype memo`
- `route memos`

原因：

- 这些页最适合帮助思考、沟通、讨论、定下一轮阅读重点
- 但它们离 source 更远
- 也最容易混入 framing 和策略判断

### D 层，当前必须特别保守

- 任何 product-specific regulatory recommendation
- 任何跨 jurisdiction 的最终路径建议
- 任何“已证明 disease modification”的强表述

当前 vault 还没有强到这个程度。

## 现在最稳的使用规则

如果你要把这套系统当“行业研究大脑”用，我建议你只按下面规则使用。

### 规则 1

先看 compiled page，再回查 source card。

不要反过来只看 compiled page 就停。

### 规则 2

凡是影响判断的钱、时间、注册路径、产品方向的结论，都必须至少回查到：

- source card
- 最好再到原始文献

### 规则 3

优先相信：

- `quoted_fact`
- `source_supported_conclusion`

比优先相信：

- `llm_inference`
- executive summary
- route memo wording

### 规则 4

看到这些信号时，自动降一级信任：

- `confidence: medium`
- `abstract-led`
- `route-level not product-specific`
- `still thin`
- `watchlist`
- `not decision-grade`

### 规则 5

如果某页的表述比它引用的 source 更强，这页就应该被视为：

`需要重审`

而不是“先用着再说”。

## 这套系统现在更像什么

它现在更像：

- 一个有证据边界的研究操作系统
- 一个可追踪的内部知识编译器
- 一个高质量研究导航层

而不是：

- 一个自动正确的行业事实机
- 一个可以跳过原文的最终裁判
- 一个直接替代专家审阅的系统

## 当前最缺的，不是更多内容，而是更强验证

如果真要把它升级成你说的那种“随时调用的行业研究大脑”，下一阶段最值钱的不是继续加页数。

而是加下面 4 个控制层。

### 1. sentence-level citation

至少给高价值 topic 页和 memo 页增加：

- 关键结论 -> 具体 source id
- 最好再到段落级或页码级

### 2. verification status

给每页明确标：

- `abstract-weighted`
- `full-text-reviewed`
- `deep-extracted`
- `decision-grade: no/yes`

### 3. language QA

把中文和双语输出加一层单独检查：

- 错别字
- 术语一致性
- 是否把弱结论翻成强结论

### 4. claim audit

对高价值页面做一个机械检查：

- 每条强结论能不能回溯到 source
- 哪些句子没有明确证据支撑
- 哪些地方 inference 越权

## 最终判断

这套系统当前是：

`有结构地降低了幻觉风险，但还没有把验证做完`

所以我的判断不是“它已经准确”，也不是“它不可信”。

更准确的说法是：

`它已经从黑箱摘要器，进化成了可审计的研究工作台，但还不是可直接依赖的最终裁判。`

## 下一步最值得做什么

如果你要优先解决“信不信得过”这个问题，下一步最值钱的不是继续加 CKD 内容。

而是做一张：

`claim-audit protocol`

专门规定：

- 哪些页必须逐条回 source
- 哪些页允许工作推断
- 什么叫 decision-grade
- 什么叫 only-for-internal-thinking

这样这个“研究大脑”才会从“会写”走到“可控”。
