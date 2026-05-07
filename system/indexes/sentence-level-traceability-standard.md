---
id: system-sentence-level-traceability-standard
type: system
topic: ckd
last_compiled_at: 2026-04-08
owner: codex
status: active
language: zh
---

# Sentence-Level Traceability Standard

这页定义最小可用的 sentence-level traceability。

不是一步到位做到逐句脚注。

而是先规定：

`哪些页面必须把关键结论显式绑到 source ids。`

## 目标

把当前系统从：

- `page-level traceability`

推进到：

- `key-claim-level traceability`

这已经足够让高价值页面更可审计。

## 先做什么，不做什么

先做：

- 高价值页面里的关键强结论
- 每条结论后面挂对应 source ids
- 做成专门的小节或表格

先不做：

- 全文逐句脚注
- 页码级 citation
- 自动 citation engine

## 适用页面

第一批必须做的页面：

- synthesis
- translation brief
- regulatory brief
- ranking memo
- route memo

## 关键结论的定义

满足下面任一条，就算关键结论：

1. 带有方向判断
2. 带有比较关系
3. 带有“最强 / 最弱 / 最佳 / 不应 / 应该”这类强语气
4. 会影响产品、监管、投入、研究优先级

## 最小格式

每页增加一个小节：

`## Key-Claim Traceability`

用表格写：

| Claim ID | Key Claim | Claim Level | Supporting Source IDs | Notes |

其中：

- `Claim ID` 用 `T1 / T2` 或 `R1 / R2`
- `Claim Level` 用 `A / B / C`
- `Supporting Source IDs` 至少写 source ids
- `Notes` 写限制，例如：
  - `compiled from review-level sources`
  - `still route-level`
  - `not decision-grade`

## 执行规则

1. 没进表的强结论，默认不算完成 traceability
2. 如果某条结论只能靠 Level C 支撑，必须写清楚
3. 如果某条结论没有足够 source ids，就该降级表述
4. route memo 的表格里必须明确写 `not decision-grade`

## 当前第一批落地点

- [translation brief](../../topics/ckd/translation-brief.md)
- [regulatory brief](../../topics/ckd/regulatory-brief.md)
