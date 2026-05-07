---
id: system-disease-module-bootstrap-workflow
type: system
topic: operating-system
last_compiled_at: 2026-04-10
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
language: zh
---

# Disease Module Bootstrap Workflow

这页回答的是一个非常具体的问题：

`当一个新病种第一次进入 vault 时，默认应该怎么启动，才不会每次都重新发明流程？`

这页是 workflow，不是原则页。

它是 [durable-agent-codification-protocol.md](durable-agent-codification-protocol.md) 在病种启动场景里的唯一 owner。

## 一句话版本

新病种进入系统时，默认走这 6 步：

`shell -> source index -> first-pass ingest -> first topic compile -> selective deep extraction -> compiled compression`

## 适用范围

这条 workflow 默认适用于：

- `FIP`
- `IBD`
- `HCM`
- 以及后续其他 feline disease module

前提是：

- 用户已经明确要纳入该病种
- 已经给到第一批 source seed

## 不适用范围

这条 workflow 不适用于：

- 单篇 source 的增补
- 已经成熟病种里的局部 densification
- 纯 regulatory corpus 导入
- 纯输出层翻译任务

那些情况应该分别归已有 owner：

- 单篇 source 导入，归 [compile-checklist.md](compile-checklist.md)
- 深提炼，归 [deep-extraction-workflow.md](deep-extraction-workflow.md)
- claim 边界，归 [claim-audit-protocol.md](claim-audit-protocol.md)
- promotion 判断，归 [write-back promotion checklist](writeback-promotion-checklist.md)

## Step 1: Build Disease Shell

先建立最小病种骨架。

至少要有：

- `topics/<disease>/index.md`
- `topics/<disease>/navigation.md`
- `topics/<disease>/current-state-dashboard.md`

如果这个 disease 从一开始就明显需要更清楚的主干，再同步建：

- `mechanism-overview.md`
- `translation-brief.md`
- `regulatory-brief.md`
- `synthesis-index.md`

### Exit Condition

这个病种不再只是一个名字，而是已经有进入点和状态页。

## Step 2: Build Source Index

把 seed corpus 先收进统一索引。

至少建立：

- `system/indexes/<disease>-source-index.md`
- `system/indexes/<disease>-reading-plan-round-1.md`

这一步不追求深度。

目标只是让所有 source 有：

- ID
- title
- primary layer
- evidence level
- 当前状态
- hierarchy placement

### Exit Condition

这个病种的 seed sources 都已经变成可追踪对象，而且不会在后面 compile 时因为来源类型混杂而被误升格。

## Step 3: First-Pass Ingest

把 seed corpus 全部变成 source cards。

目标不是：

- 一上来全深提炼

目标是：

- 先让每篇 source 都正式进入系统

至少完成：

- `raw/papers/src-xxx.md`
- one-line summary
- why it matters
- key findings
- limits / caveats
- linked entities
- source family / claim-fit judgment

### Exit Condition

病种的第一批文献不再有“只有索引，没有 source card”的空位。

同时，不再有“只有 source_kind 和 evidence_level，但不知道它该控制什么”的空位。

## Step 4: First Topic Compile

用 first-pass ingest 的 source card，先把病种主骨架搭起来。

默认优先考虑这几类 topic：

- mechanism
- recognition / endpoint
- translation
- regulatory
- synthesis

这一层只做：

- 主问题拆分
- 主分支命名
- 明显高复用概念归位

不要在这个阶段就追求：

- 极厚的 evidence density
- product-specific route memo
- bilingual rollout

### Exit Condition

病种主线已经成形，后续 deep extraction 有明确 write-back 目标。

## Step 5: Selective Deep Extraction

只挑最能改变上层结构的 source 做第一批 deep extraction。

优先级顺序通常是：

1. broad review / guideline anchor
2. 最强机制 anchor
3. 最强 recognition or endpoint anchor
4. 最强 translation / treatment anchor
5. 最容易造成 overclaim 的 boundary paper

不要一开始就追求：

- 全部文献都 deep-extracted

### Exit Condition

上层 compiled 页已经有足够强的 anchor，不再只是 title-led compile。

如果当前 seed corpus 已经被明确要求全部处理完，这一步的补充出口条件就是：

- current seed corpus `24 / 24` round-1 worksheet complete

一旦达到这条线，默认就不再把“补完 seed papers”当成下一步，而改看 beyond-seed densification。

## Step 6: Compiled Compression

当第一批 deep extraction 稳定后，再往上压 compiled 页。

默认优先：

- diagnostic-workup memo
- treatment-evidence memo
- branch-boundary memo
- one or two highest-value bridge memos

这一步的目标是：

- 把模块从 paper list 变成真正的 disease module

当某个 disease 从 broad topic compile 进入 densification 阶段后，默认优先压：

- 更窄的 order memo
- 更窄的 boundary memo

而不是继续只加更大的 summary memo。

如果这些更窄的 owner 已经开始重复出现，统一按：

- [narrow-owner densification pattern](narrow-owner-densification-pattern.md)

来读。

### Exit Condition

dashboard 上已经能清楚说明：

- strongest early branches
- still thin
- next moves

如果当前 seed corpus 已经 `24 / 24` 闭环，下一步默认 owner 不再是 bootstrap 本身，而是：

- [cross-disease-densification-queue.md](cross-disease-densification-queue.md)
- [narrow-owner densification pattern](narrow-owner-densification-pattern.md)

## 默认约束

### Constraint 1

新病种启动阶段，不默认进入 bilingual rollout。

先把英文 compiled layer 压厚，再考虑双语派生。

### Constraint 2

新病种启动阶段，不默认进入 product-specific route memo。

除非：

- translation branch 已经够厚
- regulatory corpus 已经够匹配

### Constraint 3

新病种启动阶段，不默认创建大量 entity。

只有当概念已经明显跨页复用，才值得升成 entity。

## 什么时候需要停下来重判

只有遇到下面几种情况，才需要离开默认 bootstrap workflow：

1. 病种定义本身有歧义
2. seed corpus 质量太弱
3. 主骨架有两种互斥组织方式
4. 用户要求提前进入高成本 regulatory / product 判断

除此之外，默认直接推进。

## 与 durable-agent 协议的关系

这条 workflow 本身，就是一次 codification。

也就是：

- CKD 早期 disease shell 搭建是 prototype
 
## Step 7: Post-Bootstrap State Sync

当一个病种补完下面任一动作之后：

- first briefing / dossier / slides family
- first bilingual compiled core stack
- first output language matrix

不要只更新病种内部页面。

还要同步更新：

- [multi-disease-llm-wiki-status-audit-20260410.md](multi-disease-llm-wiki-status-audit-20260410.md)
- [disease-module-maturity-ladder.md](disease-module-maturity-ladder.md)

### Exit Condition

病种自身现实，和 cross-disease owner 的现实一致。
- FIP 启动阶段是第二轮真实验证
- 到现在，这类工作已经足够稳定

所以它不该再只靠记忆。

它现在应该由这张 workflow 接住。

## 一句话收口

以后新病种的第一次进入，不该再是：

`重新想一遍怎么开始`

而应该是：

`默认按 bootstrap workflow 启动，再把真正新的问题单独升级成新 owner`

## Follow-On Owner

当病种已经过了 bootstrap 阶段，不要再继续用这张页判断“现在做到哪”。

后续成熟度判断，统一交给：

- [disease module maturity ladder](disease-module-maturity-ladder.md)
