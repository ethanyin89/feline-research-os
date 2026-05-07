---
id: system-karpathy-alignment-stop-rule-20260411
type: system
topic: operating-system
question_type: plan
language: zh
last_compiled_at: 2026-04-11
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Karpathy Alignment Stop Rule, 2026-04-11

这页只回答一个窄问题：

`如果一直说 continue，这轮工作到底什么时候应该停，不能无限继续下去？`

先读：

- [karpathy-alignment-minimal-roadmap-20260411](karpathy-alignment-minimal-roadmap-20260411.md)
- [disease-module-maturity-ladder](disease-module-maturity-ladder.md)
- [cross-disease-densification-queue](cross-disease-densification-queue.md)

## 类型判断

按 `$autoplan`，这件事属于：

`方案`

不是检查。

因为现在不是在重新判断“差在哪里”。

现在是在定：

- 什么叫这一轮完成
- 什么叫该暂停
- 什么叫该切到下一轮，而不是继续在同一轮里扩写

## 最短结论

`continue` 不应该靠感觉停。

它至少要有 3 层 stop rule：

1. `turn stop`
   这一回合该不该停
2. `round stop`
   这一阶段该不该停
3. `program stop`
   整个 Karpathy 对齐工作什么时候不再是当前主线

如果没有这 3 层，`continue` 很容易退化成：

- 再补一页
- 再补一个索引
- 再补一个 memo

最后没有明确收口。

## Level 1: Turn Stop / 单回合什么时候停

单回合应该在下面 3 条同时满足时停：

### 1. 当前承诺的最小动作已经落盘

不是只在聊天里说了。

必须已经形成系统资产，例如：

- 新索引页
- 新审计页
- 被更新的入口页
- 被回写的状态页

### 2. 基本验证已经跑过

至少做到：

- local markdown link check 通过
- 文案没有和现有状态页明显冲突
- 新页有明确 owner 和用途

### 3. 下一步已经从“模糊继续”变成“明确 owner”

也就是停下来时要能清楚说：

- 下一轮是继续 `ask surface`
- 还是切到 `retrieval`
- 还是切到 `visible thickening`

如果这一步说不清，就说明当前回合还没真正收口。

## Level 2: Round Stop / 一轮什么时候停

这次 Karpathy 对齐路线被压成了 3 轮：

1. ask surface compression
2. unified retrieval layer
3. visible thickening + background compile discipline

每一轮都要有自己的 exit condition。

### Round 1 Exit Condition

Round 1 不是“所有入口页都改完”才算结束。

Round 1 应该在下面 4 条满足时停：

1. 已经存在一个统一的 `best answer surfaces` owner
2. `reader-start-here / ask-the-vault / question-router` 都已经改成更明显的 answer-first language
3. 四病种都已经能被直接映射到：
   - fastest overall read
   - best structured overview
   - mechanism surface
   - recognition surface
   - endpoint surface
   - treatment surface
   - regulatory surface
4. 再继续改入口页，带来的已经主要是措辞收益，而不是结构收益

也就是：

`当入口层已经从“路由页”变成“答案面地图”，Round 1 就应该停。`

### Round 2 Exit Condition

Round 2 不该因为“想做更完整检索”而无限延长。

它应该在下面 3 条满足时停：

1. claim lookup 有稳定入口
2. entity lookup 有稳定入口
3. topic relationship lookup 有稳定入口

并且：

- 这些入口已经能被 LLM 稳定调用
- 不再只是分散在零碎页面里的隐性能力

### Round 3 Exit Condition

Round 3 应该在下面 3 条满足时停：

1. write-back visibility 已经存在明确 owner
2. stale output / refresh cues 已经存在明确 owner
3. compile queue visibility 已经不再主要靠维护者记忆

做到这一步，就已经从：

`系统会变厚，但只有维护者知道`

推进到：

`系统为什么变厚、哪里变厚、什么该刷新，已经是显式状态`

## Level 3: Program Stop / 整条 Karpathy 对齐主线什么时候停

这条主线不该永远是默认主线。

它应该在下面判断成立时退出当前最高优先级。

### Program Exit Condition

当这 4 条都成立时，Karpathy 对齐可以从“主线任务”降级成“维护任务”：

1. ask-native 前门已经基本成立
2. retrieval 不再主要靠页面记忆和人工导航
3. write-back / stale refresh 已经可见
4. 四病种在 maturity ladder 上已经没有明显结构性失衡

这时候就不该继续再说：

`继续做 Karpathy 对齐`

而应该切换成：

- disease-specific densification
- selective retrieval refinement
- frontend presentation polish
- new vertical or new corpus

## 当前这轮已经做到哪

截至 `2026-04-11`，当前最准确的状态是：

### Round 1

`接近完成，但还没正式宣告完成`

因为已经做了：

- [karpathy-difference-audit-20260411](karpathy-difference-audit-20260411.md)
- [karpathy-alignment-minimal-roadmap-20260411](karpathy-alignment-minimal-roadmap-20260411.md)
- [best-answer-surfaces](best-answer-surfaces.md)
- `reader-start-here`
- `ask-the-vault`
- `question-router`

但还差最后一个明确动作：

`把 Round 1 完成条件写回 roadmap 或状态页，正式宣告入口层收口。`

### Round 2

`尚未开始`

因为 claim/entity/topic 的统一 retrieval 还没形成显式 owner。

### Round 3

`尚未开始`

因为 visible thickening 和 stale-refresh 现在还主要存在于维护者视角。

## 当前最合理的 stop

所以如果问：

`现在继续到什么时候该停？`

当前最合理的答案是：

`把 Round 1 的 exit condition 明确写回状态页，然后停。`

不要在同一轮里直接滑进：

- claim lookup 细化
- entity retrieval 细化
- refresh cue 细化

因为那已经是 Round 2 或 Round 3 了。

## Default Rule For Future Continues / 以后继续时的默认规则

以后如果用户只说 `continue`，默认不要无限展开。

默认动作应该是：

1. 先判断当前正在做的是哪一轮
2. 只做这一轮剩下的最小闭环动作
3. 一旦该轮 exit condition 满足，就停，并明确说下一轮是什么

不要把：

- Round 1 的尾巴
- Round 2 的开头
- Round 3 的雏形

混在一次 continue 里一起做。

## One-Line Summary / 一句话总结

`continue` 的尽头不是“没东西可写了”，而是“这一轮的 exit condition 已经满足，下一轮应该换 owner 了”。 
