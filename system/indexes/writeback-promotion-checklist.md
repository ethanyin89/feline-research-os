---
id: writeback-promotion-checklist
type: system
topic: operating-system
question_type: workflow
language: bilingual
last_compiled_at: 2026-04-21
verification_status: compiled
decision_grade: provisional
language_qa_status: bilingual_checked
owner: codex
status: active
---

# Write-Back Promotion Checklist

这页回答的是一个很窄的问题：

`一个查询结果，到底该不该升成系统资产？`

这页是 operator checklist，不是 reader guide。

## One-Line Rule / 一句话规则

先默认：

- `chat-only`

只有满足 promotion 条件时，才升成：

- `topic update`
- `memo`
- `dashboard update`
- `navigation update`
- `bilingual compiled page`

## Step 1: Is It Repeated? / 它会不会重复出现

如果这个东西只回答了一次性困惑，先不要升。

更适合 promotion 的信号是：

- 同类问题已经重复出现
- 不同页面反复暴露同一个缺口
- 这个问题以后大概率还会继续被问

If the repeated thing is not just a claim or page update, but an operating pattern,
route it through [durable agent codification protocol](durable-agent-codification-protocol.md)
before choosing the final home.

## Step 2: Does It Clarify Structure? / 它有没有让结构更清楚

值得 promotion 的结果，通常不是“多了一段解释”，而是让结构变清楚了，比如：

- branch boundary 更清楚
- claim hierarchy 更清楚
- verification route 更清楚
- user entry path 更清楚

如果它只是更顺口，通常还不够。

## Step 3: Does It Have Evidence Enough? / 证据够不够

不要把这些东西直接 promotion：

- 没有 source anchor 的强结论
- 只是聊天里的推测
- wording 比证据更强的压缩句
- 还没有过 basic claim check 的判断

至少要能回答：

1. `它挂在哪一层证据上？`
2. `它是 orientation，还是 proof？`
3. `它有没有把原文压得更强？`

## Step 4: What Is The Smallest Durable Asset? / 最小可持续资产是什么

不要默认新建大页。

先问最小可持续资产是什么：

- 一条 dashboard 入口更新
- 一条 navigation 跳转
- 一张短 memo
- 一处 `Best Used For / Verify Next`
- 一张独立 compiled page

默认选最小、最稳、最容易复用的那个。

## Step 5: What Should Stay Chat-Only? / 什么该留在聊天里

这些结果通常只该留在聊天里：

- 只是为了这一轮对话更顺的改写
- 还没有 anchor 的 speculative leap
- 对整体结构没有复用价值的解释
- 会逼着系统长出一张空壳页的内容

## Promotion Decision / 升级决策

### Promote / 可以升

Promote when all three are true:

1. `repeated`
2. `structurally clarifying`
3. `evidence-safe enough`

### Hold / 暂缓

Hold when any one is true:

- still one-off
- still wording-first
- still under-anchored
- no obvious durable home

## Typical Homes / 常见落点

如果主要解决的是：

- repeated operating-workflow confusion
  Home: `durable-agent-codification-protocol`, then one protocol / workflow / prompt / schema / health check owner
- user entry confusion
  Home: `reader-start-here`, `ask-the-vault`, `question-router`, `dashboard`
- claim verification confusion
  Home: `verify-a-claim`, `compiled-vs-source-reading`, `source index`
- disease branch boundary confusion
  Home: `topic page`, `boundary memo`, `synthesis`
- recurring mid-layer densification confusion
  Home: a narrow `order / boundary / use-case / comparison` owner
- cross-language reuse confusion
  Home: bilingual compiled page or output language matrix

## Fast Operator Test / 维护者快速测试

在真的 promotion 之前，先问这 5 个问题：

1. `Will this matter again next week?`
2. `Does this make the system clearer, not just longer?`
3. `Is the claim anchored enough for this layer?`
4. `What is the smallest stable home for it?`
5. `Would forcing a new page create a shell without real reuse?`

如果前 4 个回答不稳，第 5 个又是 `yes`，那就先不要升。

## Related Pages / 相关页面

- [durable agent codification protocol](durable-agent-codification-protocol.md)
- [query to write-back](query-to-writeback.md)
- [narrow-owner densification pattern](narrow-owner-densification-pattern.md)
- [write-back promotion template](writeback-promotion-template.md)
- [promotion examples index](promotion-examples-index.md)
- [verify a claim](verify-a-claim.md)
- [claim audit protocol](claim-audit-protocol.md)
- [disease module bootstrap workflow](disease-module-bootstrap-workflow.md)

## One-Line Summary / 一句话总结

默认先把结果留在 chat 里，只有当它会重复出现、能澄清结构、而且证据足够安全时，才把它 promotion 成系统资产。
