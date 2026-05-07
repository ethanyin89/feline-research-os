---
id: system-multi-model-handoff-template
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

# Multi-Model Handoff Template

这页只回答一个问题：

`如果要把当前 round 的一部分交给另一个模型，最稳的 prompt 应该怎么写？`

先读：

- [multi-model collaboration boundary](multi-model-collaboration-boundary.md)
- [content vs frontend collaboration plan](content-vs-frontend-collaboration-plan.md)

## One-Line Rule / 一句话规则

不要把整个 repo 直接丢给另一个模型。

交给它的应该是：

`one narrow role + one narrow goal + one narrow write scope`

## Template A: Read-Only Reviewer / 只读审计版

适合：

- 你想让另一个模型挑错
- 你不想让它改文件
- 当前主模型仍然负责写入

直接复制：

```text
You are working in this repo:

/Users/jiawei/Desktop/insclaude/feline-research-os

Read this boundary file first:
system/indexes/multi-model-collaboration-boundary.md

Current date:
<fill current date>

Your role:
READ-ONLY REVIEWER

Do not edit files.
Do not update status pages.
Do not run write-back workflow.

Current round goal:
<one sentence>

Focus only on these files:
<exact file list>

Do not review the whole repo.
Do not expand scope unless one of the files above directly forces it.

Answer these questions:
1. What is still too heavy, duplicated, or unclear?
2. Which single page is currently doing too much?
3. What are the top 3 concrete simplifications or corrections you recommend next?
4. Which things should stay, and which should be demoted or removed?

Output format:
- one-paragraph verdict
- findings ordered by severity
- exact file paths and section names
- short recommended next moves
```

## Template B: Narrow Writer / 窄写入版

适合：

- 你确实想让另一个模型改文件
- 但你要把它锁在一个很窄的写入范围里

直接复制：

```text
You are working in this repo:

/Users/jiawei/Desktop/insclaude/feline-research-os

Read this boundary file first:
system/indexes/multi-model-collaboration-boundary.md

Current date:
<fill current date>

Your role:
WRITER FOR ONE NARROW SCOPE ONLY

Current round goal:
<one sentence>

Your write scope:
<exact file or exact directory>

Forbidden files:
README.md
system/indexes/multi-disease-llm-wiki-status-audit-20260410.md
system/indexes/disease-module-maturity-ladder.md
system/indexes/cross-disease-densification-queue.md
<add any other forbidden files>

Do:
- inspect only files in your write scope
- make only changes needed for this round goal
- avoid renames unless required
- do not update global status pages
- do not touch files outside the write scope

At the end, return:
1. what you changed
2. why
3. risks or open questions
4. exact files touched
```

## Template C: Split-Scope Two-Writer Setup / 双写分区版

只有在你真的要双写时才用。

```text
Shared repo:
/Users/jiawei/Desktop/insclaude/feline-research-os

Boundary file:
system/indexes/multi-model-collaboration-boundary.md

Current round goal:
<one sentence>

Writer A scope:
<scope A>

Writer B scope:
<scope B>

Forbidden to both:
README.md
system/indexes/multi-disease-llm-wiki-status-audit-20260410.md
system/indexes/disease-module-maturity-ladder.md
system/indexes/cross-disease-densification-queue.md

Status pages are written only by:
<one model only>

Final test runner:
<one model only>

Final integrator:
<one model only>
```

## Template D: Content Writer + Frontend Writer / 内容写手 + 前端写手版

适合：

- 一个模型负责内容 truth
- 另一个模型负责前端展现
- 你想避免“前端优化顺手改了内容结论”

直接复制：

```text
Shared repo:
/Users/jiawei/Desktop/insclaude/feline-research-os

Read first:
system/indexes/multi-model-collaboration-boundary.md
system/indexes/content-vs-frontend-collaboration-plan.md

Current round goal:
<one sentence>

Content writer owns:
- source-derived claims
- memo conclusions
- topic truth
- outputs content
- status and audit write-back

Frontend writer owns:
- layout
- navigation presentation
- visual hierarchy
- interaction flow
- readability polish

Frontend writer must not change:
- source coverage numbers
- disease status claims
- memo conclusions
- audit reality

Shared gray-zone files:
- README.md
- system/indexes/reader-start-here.md
- system/indexes/ask-the-vault.md
- system/indexes/question-router.md
- topics/*/navigation.md

Who owns final reality write-back:
<one model only>

Who runs final tests:
<one model only>
```

## What To Fill In Every Time / 每次都要自己补的字段

- `current date`
- `current round goal`
- `exact file list` or `exact write scope`
- any extra `forbidden files`
- who owns final status write-back

这些不补，prompt 就会重新变松。

## Good Example / 好例子

```text
Your role:
READ-ONLY REVIEWER

Current round goal:
Audit whether the ordinary-user front door is now simple enough.

Focus only on these files:
- README.md
- system/indexes/reader-start-here.md
- topics/fip/navigation.md
- topics/hcm/navigation.md
```

## Bad Example / 坏例子

```text
Please continue improving this repo.
```

问题就在这里：

- 没有角色
- 没有边界
- 没有 write scope
- 没有 forbidden files

这类 prompt 最容易和主线冲突。

## One-Sentence Close / 一句话收口

最稳的 handoff 不是“继续做项目”，而是“在这一个窄范围里，以这一个角色，解决这一个问题”。
