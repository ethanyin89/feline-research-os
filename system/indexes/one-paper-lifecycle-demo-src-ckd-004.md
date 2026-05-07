---
id: system-one-paper-lifecycle-demo-src-ckd-004
type: system
topic: ckd
last_compiled_at: 2026-04-08
owner: codex
status: active
language: zh
---

# 单篇文献如何在这套系统里跑完整一圈：`src-ckd-004`

如果你还没有完全理解这套系统怎么运转，不要先看全部结构。

先看一篇文献怎么“走完一生”。

这页做的就是这件事。

我们拿这篇最关键的 guideline 当例子：

- [src-ckd-004.md](../../raw/papers/src-ckd-004.md)

## 先看最终答案

这篇文献在系统里的路径是：

`raw source -> source card -> deep extraction -> topic write-back -> synthesis -> output`

如果你把这 6 步看懂，整个 vault 的运转方式你就懂了一半以上。

## Step 1: 它先作为原始资料进入系统

起点是：

- [src-ckd-004.md](../../raw/papers/src-ckd-004.md)

这一步对应 Karpathy 说的：

`raw data`

在当前项目里，它不是“扔一个链接进去就结束”。

而是先变成一个可引用的 source object。

你在这个 source card 里会看到：

- 标题
- DOI / URL
- evidence level
- one-line summary
- `quoted_fact`
- `source_supported_conclusion`
- `llm_inference`

所以这一步已经不只是“资料存档”。

它已经是第一层结构化编译。

## Step 2: 它被识别成高价值文献

不是所有 source 都会被深挖。

这篇会被深挖，是因为它满足：

- guideline
- 高频复用
- 影响 diagnosis / endpoint / treatment / early detection

也就是：

它不只是“有用”，而是“会被反复引用”。

所以它进入了 deep extraction。

## Step 3: deep extraction 把它从 source 变成可复用资产

对应文件：

- [src-ckd-004-deep-extraction-round1.md](src-ckd-004-deep-extraction-round1.md)

这一步对应 Karpathy 方案里更深的 compile。

这里不是一句摘要。

而是把这篇文献拆开，问：

- 它每个单元到底在讲什么
- 真正的主张是什么
- 隐含前提是什么
- 哪些细节值得保留
- 什么可以回写，什么还不能回写

这一步的意义不是“写更多字”。

而是把边界压清楚。

比如在这篇里，最关键的新边界就是：

- `SDMA` 有价值
- 但不能被写成 standalone screening shortcut

这就是 deep extraction 的价值。

## Step 4: 它的结论不会直接污染全库，而是保守回写

deep extraction 完成后，不是直接到处复制粘贴。

而是按 promotion check，回写到真正需要它的 topic 页。

这篇目前最典型的回写目标有：

- [early-detection.md](../../topics/ckd/early-detection.md)
- [endpoint-handbook.md](../../topics/ckd/endpoint-handbook.md)
- [sdma-positioning.md](../../topics/ckd/sdma-positioning.md)

这一步对应的其实就是：

`compile wiki`

但注意，不是“整篇复制过去”。

而是只把已经足够稳定的结论往上升。

比如：

- older-cat serial surveillance
- creatinine + USG 仍然是 practical core
- SDMA 是 adjunctive support，不是 one-test solution

## Step 5: 它再和别的核心文献一起，被压成 synthesis

一篇文献很少能单独构成总结论。

所以这篇又被拿去和另外两篇核心文献一起压成：

- [core-paper-synthesis-memo-ckd-round1.md](core-paper-synthesis-memo-ckd-round1.md)

这里你会看到一个更像 Karpathy 所说的 compiled state：

- `004` 给 operational clinical logic
- `010` 给 clinicopathology bridge
- `011` 给 fibrosis-centered mechanism frame

这一步说明：

系统不是“论文 A 说了什么、论文 B 说了什么”的罗列。

而是在做跨 source 压缩。

## Step 6: synthesis 再进入 outputs

当这些结论足够稳定，它们再进入：

- briefing
- dossier
- slides

比如：

- [out-ckd-briefing-20260408-round1-working-en.md](../../outputs/briefings/out-ckd-briefing-20260408-round1-working-en.md)
- [out-ckd-dossier-20260408-v1-working-en.md](../../outputs/dossiers/out-ckd-dossier-20260408-v1-working-en.md)

这一步对应 Karpathy 说的：

`Instead of terminal answers, render files`

也就是说，最后不是停在聊天窗口里。

而是沉成可继续引用的文件。

## Step 7: output 不是终点，还会反过来推动 topic 变厚

这也是你最容易忽略的一步。

比如：

- 输出里发现 SDMA 一直是薄弱点
- 那就会反过来逼出：
  [sdma-positioning.md](../../topics/ckd/sdma-positioning.md)

这说明输出不是“展示层”这么简单。

它也在驱动知识库继续演化。

这就对应 Karpathy 说的：

`my own explorations and queries always add up in the knowledge base`

## 用一句话再讲一次这一圈

拿 `src-ckd-004` 来说，这一圈其实就是：

1. 先有原始资料  
2. 变成 source card  
3. 对高价值 source 做 deep extraction  
4. 把稳定结论保守回写到 topic  
5. 再和别的核心 source 一起压成 synthesis  
6. 再进入 briefing / dossier / slides  
7. 再反过来推动 topic 和 entity 继续变厚

## 这和普通“做笔记”有什么不同

普通做笔记更像：

- 看一篇
- 写一篇摘要
- 放在那里

这套系统不是这样。

它更像：

- 看一篇
- 把它接到 source layer
- 判断是否值得 deeper compile
- 只把稳定信息向上晋升
- 把多篇 source 压成一个可复用中间层
- 再派生成 output
- 再用 output 反推系统缺口

所以它不是笔记流。

它是编译流。

## 你现在最值得怎么读

按这个顺序在 Obsidian 里点：

1. [src-ckd-004.md](../../raw/papers/src-ckd-004.md)
2. [src-ckd-004-deep-extraction-round1.md](src-ckd-004-deep-extraction-round1.md)
3. [early-detection.md](../../topics/ckd/early-detection.md)
4. [sdma-positioning.md](../../topics/ckd/sdma-positioning.md)
5. [core-paper-synthesis-memo-ckd-round1.md](core-paper-synthesis-memo-ckd-round1.md)
6. [out-ckd-briefing-20260408-round1-working-en.md](../../outputs/briefings/out-ckd-briefing-20260408-round1-working-en.md)

你按这个顺序看，就能真的看到一篇文献是怎么被“编译”进系统的。

## 你真正需要记住的只有一句

在这个项目里，LLM 不是“替你回答问题的人”。

它更像：

`把原始资料不断编译成更高层知识对象的编译器。`
