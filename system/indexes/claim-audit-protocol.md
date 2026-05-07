---
id: system-claim-audit-protocol
type: system
topic: ckd
last_compiled_at: 2026-04-08
owner: codex
status: active
language: zh
---

# Claim Audit Protocol

这页不是介绍系统。

这页是硬规则。

它回答的是：

`这套 research OS 里，什么结论可以怎么用，必须核到什么程度，什么时候不能往外说。`

## 一句话版本

任何结论在外发、决策、注册、产品判断前，都必须先被分级。

不分级，就不应该被使用。

## 四级 Claim 等级

### Level A: Source-Quoted

定义：

- 原文明确说过
- 可以在 source card 的 `quoted_fact` 里找到
- 可以追溯到 DOI / URL /原始资料

允许用途：

- 直接引用
- 作为最稳的事实锚点
- 进入 topic / synthesis / output

最低要求：

- 必须能回到 source card
- source card 必须有有效链接或原始来源标识

### Level B: Source-Supported

定义：

- 不是原文逐字说的
- 但能由 source 明确支持
- 应写在 `source_supported_conclusion`

允许用途：

- topic 页主结论
- synthesis 页主结论
- briefing / dossier 的主分析层

最低要求：

- 至少要能明确指向一个或多个 source id
- 不得与 source 的 limits / caveats 冲突

### Level C: Working Inference

定义：

- 模型或研究者基于现有材料做出的工作判断
- 结构上应落在 `llm_inference`
- 包括 ranking、archetype、route memo、工作假设

允许用途：

- 内部研究导航
- 下一轮阅读计划
- 内部策略讨论

禁止用途：

- 不得伪装成已证实结论
- 不得直接当作 external-facing factual claim
- 不得直接支撑 decision-grade recommendation

### Level D: Decision-Grade Claim

定义：

- 不只是“看起来合理”
- 而是已经满足更高验证要求，可用于高风险判断

当前状态：

- 这套 CKD vault 里，大多数页面还没有达到这个等级

允许用途：

- 高风险产品方向判断
- 外部正式沟通
- product-specific regulatory recommendation

最低要求：

1. 必须建立在 Level A / B 为主的基础上
2. 关键句必须能回到 source
3. 关键 source 不能只是 abstract-weighted
4. 不确定性必须已经单独暴露
5. 不得存在 vault 自己已知的结构性缺口直接击穿结论

## 页面级使用规则

### Source Card

默认可承载：

- Level A
- Level B
- Level C

规则：

- `quoted_fact` 只能放 Level A
- `source_supported_conclusion` 只能放 Level B
- `llm_inference` 只能放 Level C

禁止：

- 在 source card 里把 inference 写成 quoted_fact
- 因为“常识上大概对”就越级

### Topic / Entity Page

默认可承载：

- Level B
- 部分 Level C

规则：

- 主结论优先来自 Level B
- Level C 只能放在：
  - `llm_inference`
  - `Conflicts / uncertainty`
  - `Gaps`

禁止：

- 没有 source_ids 的强结论
- 把 route-level reasoning 写成 final recommendation

### Synthesis Page

默认可承载：

- Level B
- 经过明确标注的 Level C

规则：

- 必须写明 Evidence Map
- 必须写明 uncertainty

禁止：

- 因为“跨页综合”就自动升级可信度

### Output Page

默认可承载：

- Level A
- Level B
- 少量明确标注的 Level C

规则：

- executive answer 不得比 evidence-backed points 更强
- uncertainty / limits 不能省略

禁止：

- 把 working inference 写成定论
- 把内部 ranking memo 直接改写成外部事实判断

## 什么时候必须回 source

以下情况，一律必须回 source card，最好再回原始文献。

1. 影响产品方向
2. 影响监管路径
3. 影响资金、时间、注册成本
4. 影响对外正式表述
5. 属于“最强”“最佳”“已证明”“推荐路径”这类高强度语言

## 什么时候必须回原文

以下情况，只看 topic / synthesis / output 不够。

1. 你要比较两条路径谁更优
2. 你要判断某干预是否“已证明”
3. 你要给出 jurisdiction-specific route recommendation
4. 你要对 source 的 limits 做精确判断
5. 当前 source card 标了：
   - `abstract-led`
   - `abstract-weighted`
   - `not full-text`

## 当前系统里的默认禁止项

在没有额外审计前，下面这些说法默认禁止：

1. `this is decision-grade`
2. `this is the best regulatory path`
3. `this intervention is proven disease-modifying`
4. `this marker definitively outranks the others`
5. `this memo can replace original-paper verification`

## Decision-Grade 的最低门槛

一个结论要想进入 decision-grade，至少满足下面 6 条中的 5 条。

1. 关键 source 不是只有 abstract 提炼
2. 至少一个高价值 source 做过 deep extraction
3. topic / memo 里已经显式写出 uncertainty
4. 没有已知的 evidence-depth warning 与该结论正面冲突
5. 结论能回到具体 source ids
6. 如果是中文/双语输出，已做过语言 QA

如果低于这个门槛，默认只能停留在：

`internal working judgment`

## 审计动作清单

每次要审一个高价值页面时，按这个顺序做。

1. 找出页面里的所有强结论
2. 给每条强结论打 Level A / B / C / D
3. 检查它是否能回到 source id
4. 检查相关 source 是否仍是 abstract-weighted
5. 检查页面里的 uncertainty 是否足够暴露
6. 检查页面语言是否比证据更强
7. 不能通过的句子，降级或删掉

## 当前 CKD vault 的默认页面等级

### 默认 A/B 优先

- source cards
- deep extraction worksheets

### 默认 B/C 混合

- topics
- entities
- synthesis memos

### 默认 C 为主

- treatment ranking memo
- product archetype memo
- route memos
- most slide / briefing compression layers

### 当前不应默认当 D 用

- product-specific regulatory advice
- final route recommendation
- broad disease-modification claims

## 外发规则

如果内容是：

- 发给外部合作方
- 发给管理层
- 发给潜在监管讨论对象
- 发给投资/BD对象

那么至少要满足：

1. 去掉未标注的 Level C 句子
2. 保留 uncertainty / limits
3. 高风险结论回到 source card 核一次
4. 中文或双语内容至少过一次语言 QA

否则默认不外发。

## 这页真正要执行的纪律

不是“尽量谨慎”。

而是：

`先分级，再使用；先回查，再外发；达不到 D，就不要假装它是 D。`

## 最值得配套的下一步

如果继续强化控制层，下一步最值钱的是：

- 给高价值 topic / memo 增加 `verification_status`
- 给 route memo 增加 `decision_grade: no`
- 给 bilingual outputs 增加单独 language QA 标记
