---
id: system-content-vs-frontend-collaboration-plan
type: system
topic: operating-system
question_type: workflow
language: bilingual
last_compiled_at: 2026-04-11
verification_status: compiled
decision_grade: provisional
language_qa_status: bilingual_checked
owner: codex
status: active
---

# Content vs Frontend Collaboration Plan

这页只回答一个窄问题：

`如果当前这边只处理内容，Claude 那边只处理前端展现，最稳的分工方式是什么？`

先读：

- [multi-model collaboration boundary](multi-model-collaboration-boundary.md)
- [multi-model handoff template](multi-model-handoff-template.md)

## Classification / 任务归类

按 `$autoplan`，这件事属于：

`方案`

不是想法，不是检查，也不是排查。

因为这里要解决的不是“要不要这样做”，而是：

`两边已经决定并行协作后，边界怎么定，顺序怎么走，谁负责最终收口。`

## One-Line Split / 一句话分工

默认分成两条线：

- `this side = content truth and content write-back`
- `Claude side = frontend presentation and user-facing display`

只有当某个改动同时影响内容结构和展现结构时，才需要显式交接。

## This Side Owns / 这边负责什么

这边默认负责：

- source ingestion 和 source card
- deep extraction worksheet
- disease memo / comparison memo / boundary memo
- topic pages 的事实收口和 evidence framing
- outputs 的内容正确性
- status / audit / queue / maturity / workflow 页
- README 里与系统规则、证据边界、协作规则有关的部分

一句话说：

`内容层、证据层、状态层，都归这边。`

## Claude Side Owns / Claude 负责什么

Claude 默认负责：

- frontend layout
- visual hierarchy
- navigation presentation
- interaction flow
- styling and readability polish
- component-level display decisions
- landing surface and presentation-layer simplification

一句话说：

`展现层、交互层、可视层，都归 Claude。`

## What Claude Should Not Change By Default / Claude 默认不该碰什么

如果没有明确授权，Claude 不应默认改：

- source-derived claims
- evidence ranking
- memo conclusions
- disease status statements
- audit / queue / workflow reality
- source coverage numbers
- cross-disease state write-back

也就是：

`Claude can reshape presentation, but should not silently rewrite truth claims.`

## What This Side Should Not Do By Default / 这边默认不该碰什么

如果没有明确需要，这边不应默认去改：

- frontend visual system
- styling details
- component polish
- presentation-layer layout experiments
- UI interaction choices that do not change content truth

也就是：

`this side should not keep reaching upward into presentation decisions that Claude already owns.`

## Shared Gray Zone / 共享灰区

下面这些地方最容易跨界：

- `README`
- `reader-start-here`
- `ask-the-vault`
- `question-router`
- disease `navigation.md`

这些页既有内容组织，又有用户入口属性。

默认规则是：

`content side defines information architecture`

`frontend side defines presentation shape`

如果两边都要改这些页，就不要同时写。

## Safe Execution Order / 安全执行顺序

默认顺序应该是：

`content decision -> content write-back -> frontend presentation pass -> final integration`

不要反过来。

因为如果先做前端展现，再让内容层改结论、改分层、改 owner，前端就会立刻过时。

## Recommended Working Mode / 推荐工作模式

当前这个项目，默认推荐：

`one content writer + one frontend writer + one final integrator`

具体就是：

- 这边负责内容和状态现实
- Claude 负责前端展现
- 最后只留一个模型负责 README / status / final verification 的收口

如果没有指定，默认让内容侧做最终 integrator。

## Minimal File Boundary / 最小文件边界

更稳的默认边界是：

### Content Side

- `raw/**`
- `entities/**`
- `topics/**` 里所有内容事实页
- `outputs/**`
- `system/indexes/**`
- `system/prompts/**`
- `system/health-checks/**`

### Frontend Side

- 前端 repo 或前端显示层文件
- 组件、样式、页面框架、展示逻辑
- 不承载证据真值的 presentation-only 页面

如果前端也直接读这个 vault，那就额外加一条：

`frontend writer should avoid direct edits to system owner pages unless explicitly assigned`

## Forbidden Concurrent Writes / 禁止并发双写

下面这些文件默认不要双写：

- `README.md`
- `system/indexes/multi-disease-llm-wiki-status-audit-20260410.md`
- `system/indexes/disease-module-maturity-ladder.md`
- `system/indexes/cross-disease-densification-queue.md`
- `system/indexes/ordinary-user-llm-wiki-usability-audit-20260410.md`
- any disease `navigation.md`

这些页一旦双写，最容易出现：

`content reality and presentation reality drifting apart`

## Recommended Handoff Prompt / 推荐交接语义

最推荐的交接不是：

`please continue the repo`

而是：

`you own frontend presentation only; do not change content claims or status reality`

如果要更具体，可以写成：

- round goal
- frontend scope
- forbidden truth pages
- who owns final status write-back

## One-Sentence Close / 一句话收口

这条分工可以并行跑，但前提不是“两个模型一起改”，而是：

`one side owns truth, one side owns presentation, and only one side writes final reality back into the system`
