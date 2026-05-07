---
id: system-ask-the-vault-priority-answer-surfaces-20260416
type: system
topic: operating-system
question_type: navigation
language: zh
last_compiled_at: 2026-04-16
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Ask The Vault Priority Answer Surfaces, 2026-04-16

这页只回答一个窄问题：

`在 8 个 acceptance questions 里，最容易影响通过率的 4 题，当前应该优先落到哪些答案面？`

## 类型判断

这件事属于：

`检查辅助导航`

不是新方案，也不是内容扩写。

它的作用只是：

`把题目 -> 最强答案面 -> 次级支撑面 -> 常见误判`

压成一张 operator map。

## Why This Page Exists

现在 `query.py`、`app.py`、tests 都已经在。

真正会拖慢验收的，往往不是代码报错，而是这几种混淆：

- 问的是 mechanism，结果先掉到 dashboard
- 问的是 endpoint shortlist，结果掉到 generic CKD page
- 问的是 cross-disease maturity，结果去拼接两张 disease page
- 问的是 regulatory split，结果只读到单一 jurisdiction

这页就是为了解决这个。

## Fast Rule

对验收来说：

- `Q1` 不该先去 dashboard
- `Q2` 不该先去 generic translation brief
- `Q7` 不该先去单病种 topic page
- `Q8` 不该先去单一法规 source 或单病种机制页

## Priority Map

| Question | Primary answer surface | Secondary support surface | Why this is the right landing zone | Common wrong landing zone |
|---|---|---|---|---|
| Q1 CKD mechanism spine | [topics/ckd/mechanism-overview.md](../../topics/ckd/mechanism-overview.md) | [system/indexes/best-answer-surfaces.md](best-answer-surfaces.md) | 这页已经把 lesion backbone、mechanism-endpoint bridge、source ids 压在一起，最接近“最短机制答案面” | `current-state-dashboard.md` |
| Q2 CKD endpoint selection | [topics/ckd/endpoint-handbook.md](../../topics/ckd/endpoint-handbook.md) | [system/indexes/ckd-outcome-architecture-memo.md](ckd-outcome-architecture-memo.md) | endpoint shortlist、bucket、matrix 都在这里，最像直接回答“which endpoints and why” | `topics/ckd/index.md` |
| Q7 CKD vs HCM endpoint maturity | [system/indexes/disease-module-maturity-ladder.md](disease-module-maturity-ladder.md) | [system/indexes/cross-disease-second-wave-narrow-owner-audit.md](cross-disease-second-wave-narrow-owner-audit.md) | 这题本质是 cross-disease maturity，不是单病种 endpoint content QA | `topics/ckd/endpoint-handbook.md` + `topics/hcm/endpoint-handbook.md` 直接拼接 |
| Q8 CKD regulatory path surface | [topics/ckd/regulatory-brief.md](../../topics/ckd/regulatory-brief.md) | [system/indexes/regulatory-source-index.md](regulatory-source-index.md) | 这页已经按 China / FDA / EMA / VMD 压了 jurisdiction split 和 route questions | 单一 `src-reg-*` source card |

## Q1 Notes

### What good looks like

- answer 一开始就承认 `fibrosis / tubulointerstitial lesion backbone`
- 至少给出 2 个以上真实 source ids
- 能区分 lesion backbone、watchlist mediators、llm inference

### What failure usually means

如果 Q1 失败，优先怀疑：

1. router 没把 mechanism 问题送进 `mechanism-overview`
2. synthesis 先铺背景，没压最短答案

先不要怀疑 topic 内容本身不够。

## Q2 Notes

### What good looks like

- answer 直接出现 core shortlist
- 明确 `diagnosis/staging`、`monitoring/prognosis`、`efficacy/treatment` 不是一层
- 至少触到 phosphorus / proteinuria / SBP / creatinine trend / SDMA 的层级关系

### What failure usually means

如果 Q2 失败，优先怀疑：

1. retrieval 没把 `endpoint-handbook` 作为主面
2. answer 被 broader CKD overview 冲淡

只有在这两条排除后，才考虑 endpoint page 自身要再压短。

## Q7 Notes

### What good looks like

- answer 一开始就承认这是 cross-disease maturity question
- 用 `Level 7 / Level 6.5-7 / second-wave signal` 这种统一语言
- 如果 retrieval 不稳，会诚实降级，而不是假装精确

### What failure usually means

如果 Q7 失败，通常不是内容缺。

更可能是：

1. router 误把它当成 disease endpoint question
2. synthesis 没切到 cross-disease system owner

这题最忌讳“看起来回答很多，实际上只是把两页 endpoint handbook 拼在一起”。

## Q8 Notes

### What good looks like

- answer 一开始就按 jurisdiction split
- 至少承认 `China / FDA / EMA / VMD` 不是一条线
- route question 和 evidence package question 分开说

### What failure usually means

如果 Q8 失败，优先怀疑：

1. retrieval 掉进单一法规 source
2. synthesis 把 route-fit 写成 generic regulatory paragraph

不是先怀疑 regulatory brief 本身不存在。

## Triage Order During Acceptance

如果这 4 题里有失败，不要乱修。

按这个顺序判断：

1. primary answer surface 有没有被加载
2. secondary support surface 有没有一起进入
3. answer 有没有先给最短结论
4. 只有前 3 条都对，还失败，才回头改 page 内容

## One-Line Summary

这页不是增加内容厚度。

它只是把最关键的 4 道验收题，先钉死到当前最强答案面，避免后面把 retrieval 错误看成内容错误。
