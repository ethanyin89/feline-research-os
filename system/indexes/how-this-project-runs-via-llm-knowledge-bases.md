---
id: system-how-this-project-runs-via-llm-kb
type: system
topic: ckd
last_compiled_at: 2026-04-08
owner: codex
status: active
language: zh
---

# 这个项目是怎么按 Karpathy 的 LLM Knowledge Bases 运转的

这页不是讲 CKD 内容本身。

这页回答的是另一个问题：

`这个 vault 到底是怎么工作的？`

如果你已经看过 Karpathy 那段话，但还没有把它和当前项目对上，这页就是给你看的。

## 先说一句最短的话

这个项目的运转方式是：

`原始资料 -> source card -> topic / entity -> synthesis -> output -> write-back -> health check`

Obsidian 只是前台。

真正的“操作系统”是这一串 markdown 文件和它们之间的编译关系。

而当前更进一步的现实是：

`CKD 已经把这条链跑成了第一套可复用病种模块`

并且现在还要再加一条更硬的 operating rule：

`重复性工作不能长期停留在一次性执行，稳定后必须编成系统资产`

## Karpathy 方案，对应到当前项目是什么

| Karpathy 的环节 | 当前项目里的对应物 | 现在放在哪里 |
|---|---|---|
| raw data | 原始论文、法规、资料链接、clip | `raw/` |
| compile wiki | source card、topic page、entity card | `raw/` + `topics/` + `entities/` |
| ask the wiki | 用已有 topic / synthesis / navigation 来回答问题 | `topics/ckd/` |
| output files | briefing、dossier、slides、bilingual pages | `outputs/` |
| file outputs back into wiki | 经过 review 后，把稳定结论回写到 topic/entity | `topics/` + `entities/` |
| lint / health check | 查断链、旧话术、证据越权、双语漂移 | `system/health-checks/` |
| extra tools | compile checklist、deep extraction、bilingual policy、operating prompt | `system/indexes/` + `system/prompts/` |
| IDE frontend | Obsidian | 你本地打开的这个 vault |

## 当前项目不是怎么运转的

先反过来说，会更清楚。

它现在不是这样运转的：

- 不是“把所有 PDF 丢进去，然后直接问模型”
- 不是“靠一个通用 RAG 黑盒返回答案”
- 不是“先做一个大而全数据库，再慢慢填”
- 不是“raw 全部翻译成双语后再整理”

它现在更像：

- 先把资料变成可以引用的 source card
- 再把重复出现的信号压成 topic / entity
- 再把 topic 压成 synthesis / briefing / dossier / slides
- 再通过 health check 防止系统越写越乱

这就是它和普通“资料堆”最大的区别。

## 现在这套 vault 的真实工作流

### 第一步：原始资料进入 raw 层

比如一篇论文、一条法规、一个指南链接。

它们先进入：

- `raw/papers/`
- `raw/regulations/`

这一步的目标不是总结。

只是让资料先“存在于系统里”，并且能被找到。

## 第二步：每份资料先变成 source card

Karpathy 说的 compile，不是一下子直接写总论。

在这个项目里，第一层 compile 是：

`原始资料 -> source card`

source card 里会分开写：

- `quoted_fact`
- `source_supported_conclusion`
- `llm_inference`

这一步很关键。

因为这就是当前系统防止“模型把猜测写成事实”的主边界。

## 第三步：source card 再被编译成 topic 和 entity

当多个 source card 在讲同一件事时，才往上升。

比如：

- `renal fibrosis` 被升成机制主线
- `proteinuria / phosphorus / SBP` 被升成 bridge variables
- `SDMA` 被升成一个需要单独界定边界的 endpoint 问题

所以：

- `entities/` 放稳定知识对象
- `topics/` 放围绕问题编译出来的工作页

这一步就是 Karpathy 所说的 wiki compile，在当前项目里的主战场。

## 第四步：topic 再被压成 synthesis 和 outputs

Karpathy 说，LLM 不一定只输出聊天文本，它可以输出 markdown、slides、图片。

当前项目就是这么做的。

topic 之上，又有两层：

### synthesis 层

这是“给系统自己用的压缩层”。

比如：

- [synthesis-index.md](../../topics/ckd/synthesis-index.md)
- [core-paper-synthesis-memo-ckd-round1.md](core-paper-synthesis-memo-ckd-round1.md)

这层不是最终展示材料。

它更像“当前共识缓存”。

### output 层

这是“给人看、给讨论用”的派生层。

比如：

- briefing
- dossier
- slides
- bilingual pages

放在：

- `outputs/`

这一步对应的就是 Karpathy 说的：

`Instead of getting answers in text/terminal, render files`

而现在对新病种来说，这条 compile 链也已经不再只是隐含经验。

它已经开始被明确接成 workflow owner，例如：

- [disease-module-bootstrap-workflow.md](disease-module-bootstrap-workflow.md)

## 第五步：输出不是终点，还会回写

这也是 Karpathy 那段里很重要的一句：

`my own explorations and queries always add up in the knowledge base`

当前项目也是这样。

如果你想看这个逻辑在当前 vault 里被压成什么前台用法，可以直接看：

- [query to write-back](query-to-writeback.md)

举例：

- 先做出 briefing
- briefing 发现 `hypertension` 应该变成核心分支
- 然后回写出 [hypertension-and-comorbidity.md](../../topics/ckd/hypertension-and-comorbidity.md)

再比如：

- 深提炼三篇核心文献
- 先得到 3 份 worksheet
- 再压出 core-paper memo
- 再回写到 synthesis-index

这就不是“一次性总结”，而是“查询会沉淀回系统”。

## 第六步：health check 负责防止系统失真

Karpathy 说的 linting / health checks，在当前项目里对应：

- [health-check-report-20260408-round1.md](../health-checks/health-check-report-20260408-round1.md)
- [health-check-report-20260408-round2.md](../health-checks/health-check-report-20260408-round2.md)
- [health-check-report-20260408-round3.md](../health-checks/health-check-report-20260408-round3.md)

它们查的不是“语法错误”这么简单。

而是：

- 旧话术有没有残留
- 某个结论有没有写得比证据更强
- topic 有没有漂移
- 双语版本有没有把原意强化
- 哪些页还停在 seed / thin 状态

这一步很像“知识库的单元测试 + lint + consistency check”。

## 一个具体例子，拿 `src-ckd-004` 来看

如果只讲抽象流程，会还是有点空。

拿 `ISFM guideline` 这篇来举例。

它在系统里的路径大概是：

1. 原始资料进入 raw/source 层  
   [src-ckd-004.md](../../raw/papers/src-ckd-004.md)

2. 它被判定为高价值 source，不只做 first-pass ingest，还做 deep extraction  
   [src-ckd-004-deep-extraction-round1.md](src-ckd-004-deep-extraction-round1.md)

3. deep extraction 的结果回写 source card  
   于是 source card 不再只是“有链接的摘要卡”

4. 再回写 topic  
   比如：
   - [early-detection.md](../../topics/ckd/early-detection.md)
   - [endpoint-handbook.md](../../topics/ckd/endpoint-handbook.md)
   - [sdma-positioning.md](../../topics/ckd/sdma-positioning.md)

5. 再和别的核心文献一起，被压成 synthesis  
   [core-paper-synthesis-memo-ckd-round1.md](core-paper-synthesis-memo-ckd-round1.md)

6. 再进入 output  
   - briefing
   - dossier
   - slides

这就是一篇核心文献在这套系统里的“生命路径”。

## Obsidian 在这里到底扮演什么角色

Obsidian 不是数据库引擎。

也不是推理引擎。

它更像：

- 浏览器
- 文件 IDE
- 结构化笔记前台

## 当前和 Karpathy 分享最明显的不一样是什么

如果只看当前产物表面，你会很容易觉得：

`这更像一个高纪律的研究文档系统，而不是一个 query-native 的活 wiki。`

这是对的。

当前系统更成熟的是：

- compile discipline
- audit / trust control
- write-back 结构

而还没完全长出来的是：

- ask surface
- claim lookup surface
- query-driven living wiki feel

也就是说，现在更强的是底层控制层，不是前台产品感。

专门的检查页在这里：

- [Karpathy artifact gap check](karpathy-artifact-gap-check.md)

你在 Obsidian 里看到的是：

- raw
- source cards
- topic pages
- outputs
- graph

但真正让它“运转”的，是背后的编译规则和 write-back 纪律。

所以如果用一句话说：

`Obsidian 是前台，Markdown 文件关系是中间层，LLM 是编译器。`

## 当前项目和 Karpathy 方案已经对上的地方

已经对上的部分：

1. raw 层已经有了
2. compiled wiki 层已经有了
3. outputs 层已经有了
4. write-back 机制已经有了
5. health check 已经有了
6. deep extraction 这种“高价值 source 加厚机制”也已经有了
7. bilingual 现在也已经限制在 compiled/output 层，没污染 raw

所以它不是“还没开始用 Karpathy 的方法”。

而是：

`已经在用，而且已经做成了一个更强领域约束的版本。`

## 当前项目和 Karpathy 方案还没有完全做到的地方

还没完全做到的部分主要是密度，而不是架构：

- source depth 还不均衡
- model layer 还偏薄
- treatment primary-study density 还不够
- SDMA 这种局部问题还在继续收口

也就是说，问题不是“轮子没装上”。

问题是“车已经能跑，但发动机还没继续加大排量”。

## 你作为使用者，应该怎么理解这套系统

最简单的理解方式不是把它当成“知识库”。

而是把它当成 4 层东西：

1. `raw`
   原始材料仓

2. `compiled`
   LLM 编译过的中间知识层

3. `outputs`
   给人看的派生成果层

4. `checks`
   防止系统失真的质量层

你以后每次加资料，不是在“存一篇文献”。

你是在推动这 4 层再转一圈。

## 最后一句最实用的话

Karpathy 那套方法，在这个项目里不是抽象理念。

它现在已经变成：

`compile checklist + deep extraction workflow + topic/entity promotion + output derivation + health check`

这 5 个动作一起运行。

这就是当前项目真正的工作方式。
