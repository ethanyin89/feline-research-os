---
id: system-cross-disease-broad-page-split-audit
type: system
topic: operating-system
question_type: workflow
language: bilingual
last_compiled_at: 2026-04-10
verification_status: compiled
decision_grade: provisional
language_qa_status: bilingual_checked
owner: codex
status: active
---

# Cross-Disease Broad-Page Split Audit

这页只回答一个问题：

`四病种里，哪些旧的大页现在已经厚到更适合拆成窄 owner？`

## One-Line Summary / 一句话总结

当前最值得拆的，不是 dashboard，也不是 synthesis。

最容易继续拿大页硬扛重复判断的，是几张 `translation brief`。

## Why These Pages Matter / 为什么先看这些页

这些页已经不再只是解释：

- 这个病种有没有 translation branch

它们现在同时在扛：

- treatment branch ordering
- efficacy boundary
- branch-to-branch comparison
- translational overclaim control

如果继续把这些重复判断都塞在同一页里，结构会重新变糊。

## Executed Split Pass / 已执行的拆分轮

### HCM

**Broad page**

- [topics/hcm/translation-brief.md](../../topics/hcm/translation-brief.md)

**Why it is starting to over-carry**

- it already carries targeted frontier, older conventional branch, and therapy skepticism at once
- it already says flat hierarchy is still too strong
- it already behaves more like a comparison page than a simple translation summary

**Result**

- completed as `comparison`

**Created memo**

- [hcm-treatment-branch-comparison-memo](hcm-treatment-branch-comparison-memo.md)

### FIP

**Broad page**

- [topics/fip/translation-brief.md](../../topics/fip/translation-brief.md)

**Why it is starting to over-carry**

- it already separates preclinical antiviral foundation, natural-disease anchor, package logic, neurologic rescue, and durability
- it explicitly says branch comparison is still missing
- the page is now doing both translation overview and antiviral branch comparison work

**Result**

- completed as `comparison`

**Created memo**

- [fip-antiviral-branch-comparison-memo](fip-antiviral-branch-comparison-memo.md)

### IBD

**Broad page**

- [topics/ibd/translation-brief.md](../../topics/ibd/translation-brief.md)

**Why it is starting to over-carry**

- it already separates direct practical anchor, broad overview context, and exploratory translational branch
- it is now stable enough to support branch ordering, not just treatment existence
- it still carries this ordering only as embedded prose

**Result**

- completed as `comparison`

**Created memo**

- [ibd-treatment-branch-comparison-memo](ibd-treatment-branch-comparison-memo.md)

### CKD

**Broad page**

- [topics/ckd/translation-brief.md](../../topics/ckd/translation-brief.md)

**Why it is starting to over-carry**

- it already carries treatment ranking, outcome architecture, implementation friction, and disease-modification caution
- several narrower owners already exist beneath it
- the remaining repeated pressure is no longer more treatment summary, but a cleaner disease-modification boundary

**Result**

- completed as `boundary`

**Created memo**

- [ckd-disease-modification-boundary-memo](ckd-disease-modification-boundary-memo.md)

## Default Rule From This Audit / 这张审计页导出的默认规则

如果某张 broad page 同时满足下面 3 条，就优先拆分：

1. it already has stable subbranches
2. the repeated user question is now branch comparison or boundary control
3. the missing asset can be a short memo rather than another page family

## What This Audit Now Shows / 这轮审计现在说明了什么

这一轮 broad-page split 已经完成。

当前更准确的默认动作不再是“继续找候选”，而是：

1. when a broad page starts carrying repeated branch comparison, compress it into a `comparison` owner
2. when a broad page starts carrying repeated overclaim control, compress it into a `boundary` owner
3. after the split, write back to topic page, dashboard, bilingual high-reuse page, and cross-disease owner in the same pass

## Relationship To Other Owners / 和其他 owner 的关系

- [narrow-owner densification pattern](narrow-owner-densification-pattern.md)
  explains the general move
- [cross-disease densification queue](cross-disease-densification-queue.md)
  explains which disease should densify next
- this page
  explains which older broad pages are now the best split targets

## One-Sentence Close / 一句话收口

下一轮最稳的跨病种 densification，不是再开更多 broad page，而是把已经开始过载的 translation brief 拆成更窄的 `comparison` 或 `boundary` owner。
