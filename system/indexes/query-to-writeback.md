---
id: query-to-writeback
type: index
topic: system
question_type: workflow
language: bilingual
last_compiled_at: 2026-04-21
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: active
---

# Query To Write-Back

这页回答的是：

`为什么一次查询不只是拿到一个答案，而是可能让整个系统变厚？`

## Short Rule / 最短规则

在这个 vault 里，一次好的查询不应该只停在：

- `我问了`
- `系统答了`

更完整的路径是：

- `我问了`
- `系统先用已有 compiled 层回答`
- `如果问题逼出了稳定的新结构，就回写成系统资产`

## The Core Difference / 核心区别

普通聊天式回答更像：

- `one query -> one answer`

这个项目更想做的是：

- `one query -> one answer -> one clearer system`

也就是：

`查询不是只消费知识，也可能生产更稳的知识结构。`

## The Actual Path / 真实路径

最常见的路径是：

1. 用户先从 [ask the vault](ask-the-vault.md) 或 [question router](question-router.md) 进入
2. 先落到某个 `dashboard / topic / synthesis` 页
3. 如果当前页已经能回答，就停在这里
4. 如果问题把旧结构顶开了，就继续回 `source card / deep extraction / raw paper`
5. 如果新的 reading 反复出现，而且边界已经够稳，就回写到系统里

## What Usually Gets Written Back / 最常见会回写什么

最常见会沉淀成系统资产的，不是零散句子，而是这些东西：

- 一个更清楚的 branch boundary
- 一个更稳的 claim hierarchy
- 一个更窄的 `order / boundary / use-case / comparison` owner
- 一张新的 bilingual compiled page
- 一张新的 memo
- 某个 dashboard 或 navigation 的入口更新
- 某条 `Best Used For / Verify Next` 使用边界

## What Usually Does Not Get Written Back / 最常见不会直接回写什么

这些东西通常不该直接升成系统资产：

- 一次性的随口判断
- 还没有 paper anchor 的强结论
- 只是更好听、但没有更强证据的话术
- 只对某一次聊天有用、但没有重复价值的表述

## Good Write-Back Test / 好的回写判断

如果一个查询结果同时满足下面 3 条，就更值得回写：

1. 它不是只回答一个人当下的困惑，而是之后还会重复被问
2. 它让系统结构变得更清楚，而不是只是多了一段说明
3. 它能被放回 `topic / synthesis / memo / dashboard` 的某一层

## Repeated Work Rule / 重复性工作规则

这页处理的是 `query -> write-back`。

更上层的 owner 是：

- [durable agent codification protocol](durable-agent-codification-protocol.md)

那页负责一条更硬的规则：

`manual repetition -> accepted pattern -> codified system asset -> reused by default`

所以如果同类问题第二次又出现，不要只问：

- `这次怎么回答？`

要先问：

- `它是不是已经稳定到需要一个 durable owner？`
- `它应该落到 protocol / workflow / prompt / schema / health check / memo / dashboard 哪一层？`

If you want the operator-facing promotion gate, use:

- [write-back promotion checklist](writeback-promotion-checklist.md)

If you want the recurring densification pattern that now appears across diseases, use:

- [narrow-owner densification pattern](narrow-owner-densification-pattern.md)

If the module is already source-card complete and the real question is whether a
narrow owner should promote upward into dashboard/topic/output layers, use:

- [content precision promotion workflow](content-precision-promotion-workflow.md)

If you want real `promote / hold / partial promotion` examples, use:

- [promotion examples index](promotion-examples-index.md)

## Real Examples In This Vault / 这个 vault 里的真实例子

### Example 1 / 例子 1

查询先问：

- `普通用户现在到底该从哪里进？`

它最后没有只变成一段解释。

它回写成了：

- [reader start here](reader-start-here.md)
- [ask the vault](ask-the-vault.md)
- [question router](question-router.md)

### Example 2 / 例子 2

查询先问：

- `compiled page 和原文献到底怎么一起用？`

它最后回写成了：

- [compiled pages vs original papers](compiled-vs-source-reading.md)
- [verify a claim](verify-a-claim.md)

### Example 3 / 例子 3

查询先问：

- `IBD 这些相邻疾病到底该不该塞进核心主干？`

它最后回写成了：

- extension branch memo
- bilingual extension page
- dashboard / navigation 的边界更新

## Best Reader Behavior / 对普通用户最好的用法

如果你是普通读者，最好的用法不是自己负责回写。

你要做的是：

1. 先问更具体的问题
2. 看系统现在能不能已经回答
3. 如果发现边界不清、入口缺失、claim 太平，记录这个缺口
4. 让这个缺口变成下一轮 compile 或 write-back 的候选

## One-Line Summary / 一句话总结

这个 vault 想做的不是 `query and forget`，而是 `query, verify, compress, and write back when the structure becomes stable`.
