---
id: system-multi-model-collaboration-boundary
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

# Multi-Model Collaboration Boundary

这页只回答一个窄问题：

`如果两个模型同时在这个 vault 里跑 gstack，怎样避免互相冲突？`

更具体的一个常见分工场景，见：

- [content vs frontend collaboration plan](content-vs-frontend-collaboration-plan.md)

## One-Line Rule / 一句话规则

默认把：

`same repo + same time + same write surface`

视为会冲突。

如果没有明确边界，就不要让两个模型同时写入。

## What Usually Collides / 最容易撞车的地方

- 同时改同一批 markdown 页面
- 同时更新 dashboard / audit / queue / matrix 这类状态页
- 同时改同一个 disease module 的 navigation 和 topic pages
- 同时生成或回写同一个 output family
- 同时运行会写本地状态的 gstack workflow

最危险的不是 merge conflict 本身。

而是：

`两个模型都在把系统往不同方向收口。`

## Default Safe Modes / 默认安全模式

### Mode 1: One Writer, One Reader

最稳。

- 一个模型负责写入
- 另一个模型只做 audit / review / second opinion

适合：

- 当前主线已经明确
- 你只想让另一个模型帮忙挑错或补判断

### Mode 2: Split By Write Scope

可以，但必须先写清边界。

例如：

- model A: `topics/hcm/**`
- model B: `system/indexes/**`

或者：

- model A: `outputs/**`
- model B: `topics/**`

只有 write set 明确不重叠时才安全。

### Mode 3: Serial Handoff

也稳。

先让一个模型跑完一轮：

`edit -> test -> state write-back`

然后再让另一个模型继续。

适合：

- 两边都需要写
- 但你不想维护并行冲突

## Modes To Avoid / 应避免的模式

### 1. Same Disease, Same Round

不要让两个模型同时改同一个 disease 的：

- dashboard
- navigation
- synthesis
- translation
- regulatory

这是最容易造成状态回写互相覆盖的地方。

### 2. Same Owner Pages

不要让两个模型同时改：

- `README`
- cross-disease audit
- maturity ladder
- densification queue
- system workflow pages

这些页是全局 owner。

一旦双写，最容易出现“局部现实”和“全局现实”不一致。

### 3. Parallel Status Writing

不要一边补内容，一边让另一个模型同时更新 status / queue / audit。

正确顺序应该是：

`content first -> status write-back after`

## Default Recommendation / 默认建议

如果你只是想让另一个模型也参与，默认推荐：

`one writer, one reviewer`

也就是：

- 当前主模型继续写 vault
- 另一个模型只读当前结果，给审计、拆分建议、或 challenge

这样最接近“有第二个脑子”，但不会让系统状态打架。

## If You Really Want Two Writers / 如果你真的要双写

至少先满足这 3 条：

1. disjoint write scope
2. one shared handoff note
3. one final integrator

也就是：

- 两边写不同文件
- 都知道当前 round 的任务边界
- 最后只有一个模型负责收口和状态回写

如果做不到这 3 条，就不要双写。

## Minimal Handoff Template / 最小交接模板

双模型协作前，至少先写清：

- `current round goal`
- `writer A scope`
- `writer B scope`
- `forbidden files`
- `who writes status pages`
- `who runs final tests`

## One-Sentence Close / 一句话收口

多模型同时跑不是不能做，但默认不该并写；最稳的做法是一个写，一个审，或者严格分开 write scope 后再串行收口。
