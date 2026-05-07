---
id: system-ask-the-vault-acceptance-fault-tree-20260416
type: system
topic: operating-system
question_type: fault-tree
language: zh
last_compiled_at: 2026-04-16
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Ask The Vault Acceptance Fault Tree, 2026-04-16

这页只回答一个操作问题：

`如果 acceptance 跑出来有失败项，应该先修什么，后修什么？`

核心原则只有一句：

`先修路由，再修答案面，再修压缩，最后才补内容。`

不要一看到答案差，就立刻去加新文档。

很多失败根本不是 content gap，而是 question_type 判错、page family 命中错，或者 answer compression 把已有证据压坏了。

## 最短处理顺序

按这个顺序排：

1. `qtype-miss`
2. `family-miss`
3. `answer-compression-miss`
4. `provenance-miss`
5. `content-miss`
6. `write-back-miss`

如果前一层没过，不要直接跳去修后一层。

## Layer 1: qtype-miss

定义：

`问题类型一开始就判错了。`

常见表现：

- verification 问题被当成 generic summary
- cross-disease 问题被当成单病种问答
- boundary 问题被当成普通 disease overview
- regulatory 问题被当成通用研发问题

优先检查：

- `ROUTER_QTYPE`
- 问题 wording 是否触发了错误 heuristics
- `question_type -> page family` 的映射是否过粗

先修动作：

1. 修 `query.py` 的问题类型识别
2. 补 question pattern 到 qtype 的显式规则
3. 必要时把高风险问题降级到 conservative answer mode

不要先做：

- 先补 topic 内容
- 先改 UI

## Layer 2: family-miss

定义：

`question_type 对了，但 first family 命中错了。`

常见表现：

- mechanism 题先落 dashboard
- endpoint 题先落 generic index
- regulatory 题先落单个 `src-reg-*`
- cross-disease 题先拼两张单病种 page

优先检查：

- `FIRST_FAMILY`
- `ROUTER_FILES`
- [ask-the-vault router hit map](ask-the-vault-router-hit-map-20260416.md)

先修动作：

1. 调整 family 排序
2. 给高价值 family 更高权重
3. 在高风险题型里禁掉明显偏航的 family

不要先做：

- 先写更多 disease page
- 先做 answer wording 润色

## Layer 3: answer-compression-miss

定义：

`检索基本对了，但最终答案没有把最短答案面说清楚。`

常见表现：

- 有 loaded files，但输出仍然泛泛
- 罗列 facts，没有形成 shortlist / boundary / spine
- 把 diagnosis marker、endpoint、recognition signal 混成一层

优先检查：

- strongest answer surface 是否已被命中
- 回答模板是否要求“先给结论，再给支撑”
- 输出是否把跨页信息压成了噪音

先修动作：

1. 先看 [ask-the-vault priority answer surfaces](ask-the-vault-priority-answer-surfaces-20260416.md)
2. 补 answer scaffold，不要先补内容
3. 对 shortlist / comparison / boundary 题单独加回答骨架

不要先做：

- 看到答案空就立刻扩库

## Layer 4: provenance-miss

定义：

`答案看似像样，但 provenance tag 或 source id 已经失真。`

常见表现：

- source id 不存在
- inference 被伪装成 `quoted_fact`
- 结论段完全无 tag
- uncertainty 消失

优先检查：

- provenance tag 生成逻辑
- `source_ids` 是否来自真实 loaded files
- verification/boundary 问题是否保留保守表述

先修动作：

1. 修 tag discipline
2. 修 source id 映射
3. 对高风险问法强制保留 uncertainty sentence

## Layer 5: content-miss

定义：

`路由对了，答案骨架也对了，但库里真的没有足够强的 compiled surface。`

常见表现：

- 已命中正确 family，但仍只能给弱回答
- strongest answer surface 本身过薄
- 只能退回 source cards，无法形成 operator-level answer

优先检查：

- 当前 family 下有没有可直接回答问题的 compiled page
- 是不是缺 memo / handbook / overview 这一层，而不是缺 raw papers

先修动作：

1. 先补最短强答案面
2. 再补 supporting memo
3. 最后才考虑进一步 densification

不要先做：

- 大面积扩 disease coverage
- 一次性开很多新 page family

## Layer 6: write-back-miss

定义：

`答案本身可用，但写回产物不稳定，不适合默认开启。`

常见表现：

- frontmatter 缺字段
- slug 漂移
- 文件名覆盖重要结果
- 保留了一次性问答噪音

先修动作：

1. 保持 `write-back` 默认关闭
2. 修 frontmatter contract
3. 修 slug 稳定性
4. 提高保留门槛，只保存高价值答案

## Quick Triage

看到失败时，先问这 4 个问题：

1. `ROUTER_QTYPE` 对不对
2. `FIRST_FAMILY` 对不对
3. strongest answer surface 有没有命中
4. provenance 有没有失真

只有前 4 个都大致没问题，才把失败判成真 content gap。

## Mapping By Question

### Q1 / Q2

先怀疑：

- `family-miss`
- `answer-compression-miss`

后怀疑：

- `content-miss`

### Q3

先怀疑：

- `qtype-miss`
- `provenance-miss`

### Q4 / Q5 / Q6

先怀疑：

- `qtype-miss`
- `family-miss`

### Q7

先怀疑：

- `qtype-miss`
- `family-miss`

如果硬答得很满，再怀疑：

- `provenance-miss`

### Q8

先怀疑：

- `qtype-miss`
- `family-miss`

然后才怀疑：

- `content-miss`

## Operator Rule

后面跑 acceptance 时，按下面的判定纪律执行：

1. 先标失败类型
2. 再决定修哪一层
3. 一次只修一个主因
4. 修完立刻回跑同一题

不要在一次失败后，同时做路由、内容、UI 三种修改。

这样才看得出到底哪一层真的生效。
