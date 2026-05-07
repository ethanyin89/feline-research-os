---
id: system-ask-the-vault-router-hit-map-20260416
type: system
topic: operating-system
question_type: routing
language: zh
last_compiled_at: 2026-04-16
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Ask The Vault Router Hit Map, 2026-04-16

这页只回答一个窄问题：

`当 ask-the-vault 收到一个问题时，router 理论上应该先命中哪一类 page family，哪些命中算明显偏航？`

## 类型判断

这件事属于：

`检查辅助路由`

不是新产品方案。

它只是把：

`question_type -> primary family -> secondary family -> obvious miss`

压成一张验收图。

## Why This Page Exists

现在 acceptance 已经有：

- [ask-the-vault acceptance checklist](ask-the-vault-acceptance-checklist-20260416.md)
- [ask-the-vault priority answer surfaces](ask-the-vault-priority-answer-surfaces-20260416.md)

但还缺一块：

`如果答错了，到底是答案压缩错，还是一开始 router 就把问题送错地方？`

这页就是为了解决这个。

## Fast Rule

先不要只看“回答像不像样”。

先看：

1. `question_type` 判得对不对
2. primary page family 有没有命中
3. secondary support family 有没有补上

如果第 1 步就错，后面答得再漂亮也容易是假对。

## Router Hit Table

| Question shape | Expected `question_type` | Primary page family | Secondary support family | Clear miss |
|---|---|---|---|---|
| mechanism spine / core vs speculative | `mechanism` | `topics/<disease>/mechanism-overview*.md` | `system/indexes/best-answer-surfaces.md` | 先掉到 dashboard 或 translation |
| recognition / diagnostic workup / lead vs support | `recognition` | `topics/<disease>/risk-and-recognition*.md` | disease `synthesis-index` or dedicated workup memo | 先掉到 mechanism |
| endpoints / markers / operational vs support | `endpoints` | `topics/<disease>/endpoint-handbook*.md` | endpoint / outcome memo | 先掉到 generic index |
| treatment / translation / practical vs exploratory | `treatment` | `topics/<disease>/translation-brief*.md` or IBD treatment evidence | treatment branch memo | 先掉到 dashboard |
| regulatory / route-fit / jurisdiction split | `regulatory` | `topics/<disease>/regulatory-brief*.md` | `system/indexes/regulatory-source-index.md` | 只掉到单一 `src-reg-*` |
| best current structured overview | `synthesis` | `topics/<disease>/synthesis-index*.md` | current-state dashboard | 先掉到 source card |
| verify this claim / where does it come from | `claim_verification` | `system/indexes/verify-a-claim.md` | disease source index / compiled-vs-source-reading | 直接跳 raw paper |
| strong / thin / what next | `synthesis` | `topics/<disease>/current-state-dashboard*.md` | best-answer-surfaces / synthesis-index | 先掉到 single source |
| cross-disease maturity / compare modules | `synthesis` | `system/indexes/disease-module-maturity-ladder.md` | cross-disease audit pages | 直接拼接两张单病种 page |

## Acceptance Focus

对当前这轮验收，最该盯的 4 类偏航是：

1. `Q1` mechanism 问题先掉到 dashboard
2. `Q2` endpoint 问题先掉到 generic CKD page
3. `Q7` cross-disease maturity 问题先掉到两张单病种 endpoint page
4. `Q8` regulatory 问题只读到单一法规 source

这 4 种都属于：

`router miss first, answer quality second`

## What To Log During Runs

后面跑 acceptance 时，每题至少记这 4 个点：

1. router 返回的 `question_type`
2. `files_to_load` 里第一个 page family
3. 最终 answer 实际像哪一类 page family
4. 有没有 clear miss

最少写成：

```text
Q2
question_type: endpoints
first family: endpoint-handbook
answer felt like: endpoint-handbook + outcome memo
clear miss: no
```

## Triage Order

如果一题失败，按这个顺序看：

1. `question_type` 是否偏了
2. primary family 是否偏了
3. answer 是否没先给最短结论
4. 只有前 3 条都对，才怀疑 page 内容本身不够硬

## Relationship To Other Pages

- [question-router](question-router.md)
  定义问题入口层
- [ask-the-vault](ask-the-vault.md)
  定义普通用户问法入口
- [best-answer-surfaces](best-answer-surfaces.md)
  定义当前最强答案面
- [ask-the-vault priority answer surfaces](ask-the-vault-priority-answer-surfaces-20260416.md)
  定义最影响验收通过率的 4 道题

## One-Line Summary

这页不是告诉你答案是什么。

它告诉你：

`这道题理论上应该先落到哪类页面，哪些落点一看就是路由偏航。`
