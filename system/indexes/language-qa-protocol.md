---
id: system-language-qa-protocol
type: system
topic: ckd
last_compiled_at: 2026-04-08
owner: codex
status: active
language: zh
---

# Language QA Protocol

这页不是写作建议。

这页是控制层规则。

它回答的是：

`哪些页面必须做语言质检，质检要检查什么，过不了就不能当高可信入口。`

## 一句话版本

语言质量不是 cosmetic。

在这个 vault 里，语言层失控会直接伤害：

- 可读性
- 跨语言一致性
- 用户对事实边界的信任

所以高可见页面必须有显式 `language_qa_status`。

## 必加字段

对高可见 `topic / output / memo / dashboard / bilingual page`，统一增加：

- `language_qa_status`

可选补充：

- `language_qa_notes`

## language_qa_status 取值

### `unchecked`

适用：

- 新写完但还没做语言复核
- 内容结构可用，但不应作为高信任入口

含义：

- 可以内部继续工作
- 不应当成推荐入口页

### `light_checked`

适用：

- 单语 compiled page
- 已检查错别字、术语一致性、强度措辞、明显病句

含义：

- 可作为稳定入口页
- 但不等于做过双语一致性审核

### `bilingual_checked`

适用：

- bilingual page
- translated output
- 任何同时承载中英文语义映射的页面

最低要求：

1. 中英文核心结论方向一致
2. 不允许一边更强、一边更保守
3. 术语映射稳定
4. 无明显错别字或语病

含义：

- 当前语言 QA 里最高的常规页面状态

### `not_applicable`

适用：

- 原始 source card
- 原文保持原始语言且不承担双语入口任务的页面

含义：

- 不进入当前语言 QA 优先队列

## 哪些问题必须查

### 1. 错别字与病句

包括：

- 明显中文错别字
- 残缺句
- 重复词
- 中英文夹杂造成的语法断裂

### 2. 术语一致性

重点看：

- 同一概念是否被多种中文说法混用
- `endpoint / marker / outcome / signal` 是否被混写
- `route / path / pathway / strategy` 是否漂移

### 3. 强度漂移

重点看：

- 英文是 `suggests / supports / may`
- 中文却被写成 `证明 / 已确定 / 最佳`

这是最危险的语言层错误之一。

### 4. 双语不对称

重点看：

- 中文版多写了结论
- 英文版删掉了 limits
- 一边写 `usable`
- 另一边写成 `strong`

### 5. 语气膨胀

重点看：

- 为了让文本“更像总结”而自动变得更绝对
- working inference 被语言风格误写成定论

## 哪些页面优先做

### P0

- dashboard
- bilingual dashboard
- synthesis
- bilingual synthesis
- translation brief
- regulatory brief
- external-facing output

### P1

- ranking memo
- route memo
- archetype memo
- overview page

### P2

- 其他内部工作页

## 与 Claim Audit 的关系

Language QA 不能替代 claim audit。

但它能拦住一类非常危险的失真：

`事实还没变，话术先变强了。`

所以顺序应当是：

1. claim 分级
2. traceability 检查
3. language QA
4. 再决定能不能当高信任入口或外发草稿

## 当前执行规则

1. 高可见页面如果没有 `language_qa_status`，默认按 `unchecked` 看待
2. bilingual 页面默认不允许停留在 `unchecked`
3. 任一页面若存在明显错别字或强度漂移，不得标记为 `light_checked` 或 `bilingual_checked`
4. `bilingual_checked` 不等于 `decision_grade: yes`
5. 语言更顺，不代表证据更强

## 当前最需要警惕的一句话

`语言质量可以提升信任感，但不能伪造证据强度。`
