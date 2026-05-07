---
id: system-narrow-owner-densification-pattern
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

# Narrow-Owner Densification Pattern

这页只回答一个很窄的问题：

`当 disease module 已经有厚的 topic page 和 memo 之后，下一轮 densification 最稳的动作通常是什么？`

## One-Line Rule / 一句话规则

当 broad compile 已经成立后，下一轮默认不要再开更大的 summary page。

先问：

`有没有一个反复出现的窄问题，可以被压成一个更小的 owner？`

最常见的窄 owner 类型是：

- `order`
- `boundary`
- `use-case`
- `comparison`

## Why This Pattern Exists / 为什么会出现这个模式

到中后期，最常重复的缺口通常不再是：

- 这个病种有没有页面
- 这个主题有没有 summary

而变成：

- 哪个分支该先读
- 哪个边界不能被压平
- 同一个对象在不同 use case 下到底做什么
- 两个看起来都合理的分支，哪一个更干净，为什么

这些问题继续塞回大页里，结构会越来越糊。

所以更好的默认动作是：

`把重复问题压成一个更窄、更稳定、更可复用的 owner`

## The Four Common Shapes / 四种最常见形状

### 1. Order Owner

用来回答：

- 哪个分支先行
- 哪个支持层只能跟随
- 哪个对象只有在 branch shift 之后才出现

Example:

- FIP: [fip-support-order-memo](fip-support-order-memo.md)

### 2. Boundary Owner

用来回答：

- 哪个 claim 不能越线
- 哪个 assay / branch 只能停在有边界的支持层
- 哪个 regulatory layer 还不能 promotion

Examples:

- FIP: [fip-assay-performance-boundary-memo](fip-assay-performance-boundary-memo.md)
- IBD: [ibd-claim-fit-route-fit-boundary-memo](ibd-claim-fit-route-fit-boundary-memo.md)

### 3. Use-Case Owner

用来回答：

- 同一个 branch 里的对象其实不是一回事
- 它们分别适合哪个 job

Example:

- HCM: [hcm-biomarker-use-case-memo](hcm-biomarker-use-case-memo.md)

### 4. Comparison Owner

用来回答：

- 两个看起来都合理的读法并不等价
- `strongest` 不等于 `cleanest`
- `route-fit` 不等于 `claim-fit`

Example:

- CKD: [ckd-archetype-route-cleanliness-memo](ckd-archetype-route-cleanliness-memo.md)

## When A Second-Wave Narrow Owner Is Worth It / 什么情况下值得做第二层窄 owner

当第一层 owner 已经存在，而且真正重复的问题变成：

- branch 内部更硬的边界
- branch shift 的真正触发点
- 两个不同轴上的 winner 到底如何分开
- 如果只能再做一步，下一张应该给谁

这时就值得继续压一层更窄的 owner。

Recent examples:

- HCM: [hcm-ai-augmentation-boundary-memo](hcm-ai-augmentation-boundary-memo.md)
- FIP: [fip-neurologic-workup-branch-boundary-memo](fip-neurologic-workup-branch-boundary-memo.md)
- FIP: [fip-neurologic-rescue-boundary-memo](fip-neurologic-rescue-boundary-memo.md)
- CKD: [ckd-next-route-memo-priority-memo](ckd-next-route-memo-priority-memo.md)
- IBD: [ibd-best-overall-vs-route-cleaner-archetype-memo](ibd-best-overall-vs-route-cleaner-archetype-memo.md)

## Fast Operator Test / 维护者快速判断

如果一个 recurring gap 同时满足下面 3 条，就优先考虑窄 owner，而不是更大的 summary page：

1. 问题已经重复出现
2. 它本质上是在逼一个结构判断，而不是逼更多背景信息
3. 最小可持续资产可以是一张短 memo，而不是一个新 page family

如果重复出现的不是 disease/content 判断，而是“这类工作怎么执行”，不要在这里开 memo。
先回到 [durable agent codification protocol](durable-agent-codification-protocol.md)，判断它应该被固化成 protocol、workflow、prompt、schema，还是 health check。

如果窄 owner 已经存在，当前问题是它能不能上升到 dashboard/topic/output 层，走：

- [content precision promotion workflow](content-precision-promotion-workflow.md)

## What This Pattern Prevents / 这个模式在阻止什么

- 阻止大页继续变厚但不变清楚
- 阻止一个 branch 同时承担太多不同问题
- 阻止 “已经有很多 memo” 被误读成 “已经有最终答案”
- 阻止系统为了 densification 长出低复用的大 summary shell

## Where To Write Back / 应该回写到哪里

窄 owner 写完之后，默认最小回写范围是：

1. 对应的 one-language topic page
2. 对应的 bilingual high-reuse page
3. current-state dashboard
4. cross-disease audit or densification queue, if the pattern changes how the module should now be read

## Relationship To Other Owners / 和其他 owner 的关系

- [durable agent codification protocol](durable-agent-codification-protocol.md)
  owns the higher-level rule for turning repeated work into a reusable system asset
- [query-to-writeback](query-to-writeback.md)
  explains why repeated questions can become system assets
- [write-back promotion checklist](writeback-promotion-checklist.md)
  decides whether a result should promote at all
- [disease-module bootstrap workflow](disease-module-bootstrap-workflow.md)
  says when broad compile should give way to narrower compression
- [cross-disease broad-page split audit](cross-disease-broad-page-split-audit.md)
  shows which older broad pages now look ready for this move
- [cross-disease second-wave narrow-owner audit](cross-disease-second-wave-narrow-owner-audit.md)
  shows what the next-wave move looks like after first-layer memos already exist
- this page
  says what that narrower compression most often looks like

## One-Line Summary / 一句话总结

当模块已经够厚时，最稳的下一步通常不是更大的 summary，而是更小的 `order / boundary / use-case / comparison` owner。
