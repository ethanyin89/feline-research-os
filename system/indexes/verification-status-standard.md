---
id: system-verification-status-standard
type: system
topic: ckd
last_compiled_at: 2026-04-08
owner: codex
status: active
language: zh
---

# Verification Status Standard

这页定义统一字段，不是解释页。

它解决的问题是：

`每个高价值页面现在到底核到了哪一步。`

## 必加字段

对高价值 `source / topic / output / memo`，统一增加两个 frontmatter 字段：

- `verification_status`
- `decision_grade`

## verification_status 取值

### `title_only`

适用：

- 只确认到题名 / DOI / 基础书目信息
- 尚未核对摘要或全文细节

含义：

- 只能作为方向性索引
- 不可支撑机制、疗效、诊断或路径判断

### `abstract_weighted`

适用：

- 主要基于摘要、引言、可见片段
- 还没做全文级整理

含义：

- 可作为导航
- 不可默认当强证据页

### `source_checked`

适用：

- source card 结构完整
- 关键事实已整理
- 但未进入 deep extraction

含义：

- 可作为 topic compile 的基础
- 高风险判断仍建议回原文

### `deep_extracted`

适用：

- 已有 deep extraction worksheet
- 已做 promotion check

含义：

- 当前 vault 里最稳的 source 级状态之一

### `compiled`

适用：

- topic / synthesis / memo / output 这类 compiled 页
- 已完成一轮结构化编译

含义：

- 可用于研究工作流
- 不等于已审计

### `audited`

适用：

- 已按 claim audit protocol 做过专门审计
- 关键强结论已检查

含义：

- 当前 vault 里最高的页面级状态
- 但也不自动等于 `decision_grade: yes`

## decision_grade 取值

### `no`

含义：

- 不可作为高风险最终判断

默认适用：

- 大多数 topic
- 大多数 outputs
- ranking / archetype / route memos

### `provisional`

含义：

- 可以作为强工作判断
- 但仍需补验证才能外发或定案

### `yes`

含义：

- 满足 claim-audit protocol 里的更高门槛
- 可以进入高风险判断层

当前状态：

- 当前 CKD vault 默认不应轻易使用这个值

## 默认映射

| Page Type | Default verification_status | Default decision_grade |
|---|---|---|
| source card, title-led only | title_only | no |
| source card, abstract-led | abstract_weighted | no |
| source card,整理完成但未 deep extract | source_checked | no |
| deep extraction worksheet | deep_extracted | no |
| topic / synthesis | compiled | no |
| audited topic / synthesis | audited | provisional |
| output | compiled | no |
| route memo / ranking memo / archetype memo | compiled | no |

## 当前执行规则

1. 没有这两个字段的高价值页，默认按最低信任处理
2. `verification_status: audited` 不自动等于 `decision_grade: yes`
3. 任何 route memo，若无额外声明，默认 `decision_grade: no`
4. 任何 abstract-weighted source，不得支撑最终推荐路径
