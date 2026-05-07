---
id: verify-a-claim
type: index
topic: system
question_type: query
language: bilingual
last_compiled_at: 2026-04-09
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: active
---

# Verify A Claim

这页是给这种情况用的：

`我已经看到一个结论了，但我现在想知道，这句话到底从哪来，稳不稳，要回哪层去核实。`

## Short Rule / 最短规则

先不要问：

- `这篇文献讲了什么`

先问：

- `这个具体结论现在挂在哪一层`
- `我要回 topic、source card，还是 raw paper`

## Step 1 / 第一步

先判断你手里拿的是哪一类结论：

1. `dashboard / briefing` 里的压缩结论
2. `topic / synthesis` 里的结构化结论
3. 你自己脑中记住的一句判断

如果是 1，默认不要直接信到最底。

如果是 2，通常已经更接近真实边界。

如果是 3，先回到系统里找它目前最接近的 compiled page。

## Step 2 / 第二步

用这 3 个问题拆它：

1. `这句话是在说 orientation，还是在说 proof？`
2. `这句话是在说 lead evidence，还是 support evidence？`
3. `这句话是在说 current working reading，还是 paper-level exact claim？`

## Step 3 / 第三步

按这个顺序回查：

1. 先回对应的 `topic` 或 `synthesis`
2. 再回 `source index`
3. 再回 `source card / deep extraction`
4. 最后回 `raw paper`

## Best Verification Routes / 最稳的核查路径

### CKD

- dashboard or overview first:
  [current-state-dashboard](../../topics/ckd/current-state-dashboard.md)
- structured compiled layer:
  [synthesis-index](../../topics/ckd/synthesis-index.md)
- source map:
  [CKD source index](../../system/indexes/ckd-source-index.md)

### FIP

- dashboard or overview first:
  [current-state-dashboard](../../topics/fip/current-state-dashboard.md)
- structured compiled layer:
  [synthesis-index](../../topics/fip/synthesis-index.md)
- source map:
  [FIP source index](../../system/indexes/fip-source-index.md)

### IBD

- dashboard or overview first:
  [current-state-dashboard](../../topics/ibd/current-state-dashboard.md)
- structured compiled layer:
  [synthesis-index](../../topics/ibd/synthesis-index.md)
- source map:
  [IBD source index](../../system/indexes/ibd-source-index.md)

## Good Claim Questions / 好的 claim 核查问法

不要只问：

- `这个对不对？`

更好的问法是：

- `这个结论当前是在 compiled orientation 层，还是已经有 paper-level anchor？`
- `这个说法是 lead evidence，还是 support evidence？`
- `这句话应该回哪一层核实，topic 还是 raw paper？`
- `这句话有没有被压得比原文更强？`

## Typical Example / 典型例子

如果你看到一句：

- `IBD treatment branch is now real enough to structure`

你不应该直接跳去问：

- `那是不是已经能强结论推荐治疗？`

你应该先问：

- `这里的 real enough to structure，指的是 topic architecture，还是强疗效证据？`

然后回：

- [treatment-evidence-bilingual](../../topics/ibd/treatment-evidence-bilingual.md)
- [IBD treatment evidence memo](../../system/indexes/ibd-treatment-evidence-memo.md)
- 相关 source cards and deep extraction pages

## One-Line Summary / 一句话总结

Claim lookup 的核心不是“再找一篇文献”，而是先判断这句话当前位于哪一层，再回正确的证据层核实。
