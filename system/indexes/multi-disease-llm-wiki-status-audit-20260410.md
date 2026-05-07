---
id: system-multi-disease-llm-wiki-status-audit-20260410
type: system
topic: operating-system
question_type: audit
language: zh
last_compiled_at: 2026-04-24
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Multi-Disease LLM Wiki Status Audit, 2026-04-10

这页回答的是一个非常具体的问题：

`CKD、FIP、IBD、HCM、Diabetes 现在分别做到哪一层？整体上，项目现在到底有多像之前理解的 LLM wiki？`

## 类型判断

这件事属于：

`检查`

因为当前不是在提新方案，也不是在排查某个坏点。

当前是在盘：

- 4 个 disease module 的执行进度
- 哪些层已经真实存在
- 整体像不像一个 `ask-native, write-back-native, auditable` 的 LLM wiki

当前还要加一条现实边界：

- 内容主线和前端展现现在已经开始分开处理

## 最短结论

如果只看底层骨架，这个项目已经明显在那条路上了。

如果看前台产品感和多病种一致性，它还没有完全到位。

更准确的说法是：

`整体已经进入 LLM wiki 的工作方式，但还没有进入一个五病种都成熟对齐的 LLM wiki 成熟态。`

但这句现在也需要补一个新现实：

`CKD / FIP / IBD / HCM 已经开始出现 second-wave narrow-owner signal；Diabetes 进入 starter Level 5，已有 24 / 24 round-1 worksheets、第一层 narrow memo、Bexacat / Senvelgo 的 U.S. FDA FOI 和 DailyMed current-label source cards、SGLT2 label-section worksheets、第一组 briefing / dossier / slides output，以及第一张高复用 bilingual compiled dashboard。`

## 五病种执行状态总表

| Disease | Seed Corpus | Deep Extraction | Core Compiled Spine | Outputs | Bilingual Compiled | Current Maturity |
|---|---|---|---|---|---|---|
| CKD | 24 sources mapped | 24 deep extractions | thick | briefing + dossier + slides, all `working-en / en / zh` | real and usable | highest |
| FIP | 24 sources mapped | 24 deep extractions | thick | briefing + dossier + slides, all `working-en / en / zh` | dashboard + synthesis + mechanism + recognition + translation + endpoint + regulatory now exist | output-and-bilingual aligned, control improving but still thinner |
| IBD | 24 sources mapped | 24 deep extractions | thick | briefing + dossier + slides, all `working-en / en / zh` | high-reuse pages exist | strongest all-around |
| HCM | 24 sources mapped | 24 deep extractions | mid-thick and coherent | briefing + dossier + slides, all `working-en / en / zh` | broad compiled bilingual layer exists | fast-rising, now output-aligned |
| Diabetes | 24 sources mapped | 24 round-1 worksheets + 4 U.S. SGLT2 regulatory/label sources + 2 label-section worksheets | first shell plus 13 narrow memos + 20 topic pages | briefing + dossier + slides, all `working-en / en / zh` | first high-reuse dashboard exists | starter Level 5 |

## Disease-By-Disease Read

### CKD

CKD 现在最接近完整 disease module。

它已经不仅有：

- source cards
- topic pages
- compiled memos

而且还有：

- working-English / derived-English / Chinese-facing outputs
- slides
- bilingual compiled pages
- product-archetype 和 route memo
- trust / audit / language-QA / traceability 这类 control layer

所以 CKD 现在更像：

`一个成熟的 compiled research module`

不是只是一组整理过的页面。

而且 CKD 最近也开始把 regulatory / route 线压成更窄的比较 owner：

- `treatment product archetype`
- `archetype-route cleanliness`
- `next route-memo priority`

也就是 CKD 现在不只是有多张 route memo，而是开始明确区分：

`best-supported archetype` 和 `cleanest route-fit archetype`

而且已经开始进一步回答：

`如果只能再推进一步，下一张 route memo 应该给谁`

### FIP

FIP 现在已经不再是 compile-strong, output-light。

从 dashboard 看，24 条 source 已建卡，而且 24 / 24 都已经进入 round-1 deep extraction；机制、识别、病型分支、clinicopathology、mutation boundary、treatment evidence 这些都已经成形；同时 briefing、dossier、slides 现在也已经覆盖 `working-en / en / zh`，而 bilingual compiled core stack 也已经起出来了。

所以 FIP 当前更像：

`一个已经完成从 compile-heavy module 到 output-and-bilingual-started wiki module 跃迁的病种`

它现在更真实的缺口是：

- broader bilingual family 还没铺开
- regulatory 仍然是 thin boundary page
- control-layer densification 还没追上 CKD / IBD

但它最近已经有了一个更像 CKD / IBD 的 densification 方向：

- `support-order memo`
- `assay-performance boundary memo`
- `neurologic workup gate`
- `neurologic rescue boundary`

也就是 FIP 现在不只是有 `diagnostic ambiguity` 这句大框架，而是已经开始把 endpoint / workup 的控制层压成：

`what leads first` 和 `what each assay branch is actually allowed to claim`

并且进一步压成：

`when ordinary workup must shift into neurologic branch`

以及：

`when neurologic treatment is no longer baseline antiviral care but a different rescue category`

### IBD

IBD 现在是最完整的全链路病种之一。

它已经同时有：

- 24 / 24 deep extraction complete
- core topic spine
- compiled memos
- `working-en / en / zh` briefing, dossier, slides
- bilingual compiled pages covering dashboard, synthesis, mechanism, recognition, endpoint, treatment, regulatory, extension

所以 IBD 现在不只是 compile 成熟。

它已经接近：

`一个真的可以 ask, reuse, verify, and derive outputs 的 disease wiki module`

但它最近也开始把 regulatory 薄层压成更窄的 owner：

- `treatment product archetype`
- `claim-fit / route-fit boundary`
- `best overall vs route-cleaner archetype`

也就是 IBD 现在不只是知道 `product-type-first`，而是开始明确区分：

`best overall archetype` 和 `future route-cleaner archetype`

所以 IBD 现在的 regulatory branch 不再只是 thin layer。

它已经开始进入：

`two-winner comparison territory`

### HCM

HCM 的推进速度仍然很快，而且现在已经补上了最后一个明显 output 缺口。

当前已经有：

- 24 条 source seed
- 24 条 deep extraction
- mechanism / recognition / endpoint / translation / regulatory / synthesis 主干
- 8 张 compiled memo
- briefing + dossier + slides 的 `working-en / en / zh`
- 一整圈 bilingual compiled pages

但 HCM 仍然明显处在：

- source thickness 没有 IBD / FIP 那么深
- regulatory 仍然是边界页
- overall control thickness 还没到 CKD / IBD

但它最近也已经开始出现更窄的 densification owner：

- `frontier augmentation`
- `biomarker use-case`
- `AI augmentation boundary`
- `product-type separation`

也就是 HCM 现在不只是有更厚的 endpoint / workup compile，而是开始把 marker branch 压成：

`which marker does what job`

并且进一步压成：

`AI can augment recognition and endpoint reading, but cannot replace structure-first phenotype definition`

以及：

`the first regulatory move is product-type separation, not jurisdiction comparison`

所以它现在属于：

`已经进入真实 output-and-bilingual phase，但还没进入高密度成熟 phase`

### Diabetes

Diabetes 是 2026-04-20 新进入 vault 的第五个 disease module。

当前已经有：

- 24 条 source seed
- 24 张 first-pass source cards
- 24 张 round-1 worksheets 已完成，24 / 24 source cards 已是 explicit full，且 paper-card verification overlay 现在是 24 deep_extracted
- source index
- reading plan
- current-state dashboard
- mechanism / recognition / endpoint / translation / regulatory boundary / synthesis 主干
- 13 张 narrow memo：remission、diet architecture、endocrine-secondary diabetes、neuropathy、SGLT2 safety/regulatory boundary、SGLT2 primary FDA source、SGLT2 current-label control、SGLT2 label-section comparison、treatment branch comparison、diagnostic/monitoring workup、obesity/body-condition、breed-risk、pancreatitis
- 4 张 U.S. regulatory / label source cards：Bexacat / Senvelgo FDA FOI + DailyMed current labels
- 2 张 SGLT2 label-section worksheets：Bexacat / Senvelgo current-label section extraction
- query router 和 UI condition selector 已经认识 `diabetes`

但它还没有：

- full-text compiled memos
- full label section extraction for Bexacat / Senvelgo
- broad bilingual compiled family
- mature control-layer owner

所以 Diabetes 现在属于：

`starter Level 5, with output family, first high-reuse bilingual dashboard, and U.S. SGLT2 FOI/current-label/label-section control started, but not clinical full-text or bilingual mature`

## 新的成熟信号

这轮最重要的新变化不是又多了几张 memo。

而是四个成熟模块已经开始出现一种更一致的成熟信号，而第五个 Diabetes 模块刚完成 bootstrap：

`first-wave narrow owner 之后，系统开始主动产出 second-wave narrow owner`

这些 second-wave owner 主要落在 4 种类型：

- branch-internal boundary
- branch-shift gate
- two-winner comparison
- next-step priority memo

这意味着当前系统的 densification 已经不再只是：

`发现 broad page 太大 -> 压成 first-wave narrow owner`

而是开始进入：

`第一层 owner 已经成立 -> 再把真正卡住系统的下一个结构判断单独压出来`

这比单纯 page count 增长更像成熟度提升。

## 和“之前理解的 LLM wiki”相比，到底满足了多少

如果把之前目标压成 5 个条件，现在的满足情况大致是这样：

### 1. Ask-first front door

`基本满足`

已经存在：

- [ask the vault](ask-the-vault.md)
- [question router](question-router.md)
- [reader start here](reader-start-here.md)
- 各 disease dashboard 的 `Top Questions`

也就是现在不再必须从文件树进入。

但它仍然主要是：

`query-guided document navigation`

还不是：

`真正的 ask-native active surface`

### 2. Raw -> compile -> output -> write-back

`明确满足`

这条链现在已经不只是概念，而是被真实跑出来了。CKD / FIP / IBD / HCM 都已经进入这条链的真实执行状态；Diabetes 目前处于 source-card + topic-shell + 24 / 24 round-1 worksheets + narrow memo layer + U.S. SGLT2 FOI/current-label/label-section control + first output family + first high-reuse bilingual dashboard 阶段，下一步只在外部输出或复用压力需要时做 non-U.S. regulatory、clinical full-text deepening 或更窄的 bilingual compiled derivative。

### 3. Claim verification and trust boundary

`明显满足`

已经存在：

- [verify a claim](verify-a-claim.md)
- [compiled pages vs original papers](compiled-vs-source-reading.md)
- promotion checklist / examples
- language matrix
- health checks

这块是当前系统最强的地方之一。

### 4. Query can thicken the system

`部分满足，而且机制已经存在`

已经有：

- [query to write-back](query-to-writeback.md)
- [write-back promotion checklist](writeback-promotion-checklist.md)
- promotion examples

也就是说逻辑已经存在。

但用户能否直接“感受到这次查询让系统变厚”，现在还不够强。

### 5. Multi-disease consistency

`还没有完全满足`

真正明显的不一致现在已经缩小了。

当前四个成熟病种都已经进入：

- briefing / dossier / slides
- output language matrix

而真正剩下的不一致主要变成：

- deep extraction 密度不齐
- compiled memo 厚度不齐
- bilingual family 覆盖范围不齐
- regulatory 与 control-layer 厚度不齐

所以现在更像：

`一套强骨架 + 不同病种成熟度不同`

还不是：

`五病种都已经对齐的统一成熟 wiki`

但如果只看内容侧的结构演化，当前已经可以更具体地说：

`四个成熟病种都不再只是 seed-complete modules，而是已经开始进入 second-wave densification modules；Diabetes 是新进入的 starter Level 5 module`

## 当前最准确的总判断

如果一定要压成一句话：

`这个项目已经进入 LLM wiki 的工作方式，但还没有进入 LLM wiki 的整齐成熟态。`

更细一点：

- CKD：接近成熟模板
- IBD：接近成熟模板，甚至在 bilingual reuse 上更强
- HCM：已完成从 shell 到 output+bilingual 的跃迁，但还在 densification 阶段
- FIP：已完成从 compile-heavy 到 output+bilingual core stack 的跃迁，但 control 和 broader family 仍偏薄
- Diabetes：进入 starter Level 5，已有 output family 和第一张高复用 bilingual dashboard；下一步只在外部输出或复用压力需要时做 non-U.S. regulatory、clinical full-text deepening 或更窄的 bilingual derivative；临床 full-text extraction 仍未完成

## 最大缺口不在内容量，而在对齐度

当前最大的缺口不是：

- 文献不够多
- 页数不够多

真正的缺口现在更准确地说是：

`四个成熟病种虽然都已经进入 output-capable wiki surface，但还没有在 densification 与 control 厚度上完全对齐；Diabetes 已完成 seed-scope abstract extraction 并开始 memo 层，但还没进入 output/control 阶段`

也就是：

- 有的 deep extraction 已接近满格
- 有的 bilingual compiled 只覆盖 core stack
- 有的 regulatory / route 层仍然很薄
- 有的 control layer 更像成熟模板

这会直接影响“像不像一个统一的 LLM wiki”。

因为真正像的前提不是某一个病种很强。

而是：

`同一套 ask -> compile -> output -> verify -> write-back 语法，能跨病种稳定复用。`

## 发现的重复动作，已经应该固化

这次回写后，一个新的稳定重复动作已经很清楚了：

`当某个 disease 补完 output family 或 bilingual core stack 之后，必须立刻回写 cross-disease audit 和 maturity ladder。`

否则会持续出现一种假象：

- 病种本身已经推进了
- 但 system owner 还停在旧现实

这一步以后不该再靠记忆补。

它应该变成固定流程：

1. 更新 disease dashboard / navigation / matrix
2. 更新 cross-disease audit
3. 更新 maturity ladder 的病种分层
4. 再决定下一步是 densification 还是 supermodule

如果决定继续 densification，默认 owner 应改看：

- [cross-disease-densification-queue.md](cross-disease-densification-queue.md)
- [content-side-densification-queue.md](content-side-densification-queue.md)

## 现在更准确的默认分工

当前更准确的系统现实已经变成：

- 内容侧继续负责 truth, evidence, memo, output content, and status write-back
- 前端侧负责 ordinary-user presentation and display shaping

这意味着下一轮如果继续推进内容，不应该再把“普通用户入口够不够顺”当成内容主线。

内容主线现在更准确地说是：

`在四个成熟病种 seed-scope 已闭环之后，继续把窄 owner、control thickness、和跨病种状态同步做厚；对 Diabetes 则只在外部输出需要时做 selective full-text/label deepening`

## 现在最该做的，不是再发散

现在最该做的不是再开更多 disease，也不是继续无边界补 memo。

最该做的是把四个成熟病种拉到更接近同一 maturity ladder，同时让 Diabetes 从第一层 memo 进入 selective full-text/label deepening。

最明显的顺序现在已经变成：

1. 维持四个成熟病种 `24 / 24 round-1` 的现实同步
2. Diabetes 只在外部输出需要时做 full label extraction、non-U.S. regulatory check、或治疗/肥胖 sequencing full-text review
3. 成熟病种默认转入 beyond-seed densification
4. 优先补更窄的 `order / boundary / use-case / comparison` owner
5. 只在 reuse pressure 明确时再扩 bilingual family 或 supermodule

## 一句话收口

这个项目现在已经部分满足之前理解的 LLM wiki，而且在底层 discipline 上做得比很多“AI knowledge base”更真。

但如果按全库整体来算，它目前更像：

`一个已经跑通 seed-to-output-to-control 方法、完成四个成熟病种 seed-scope 闭环、并开始接入第五个 Diabetes 模块的 auditable research wiki system`

而不是一个已经全线整齐完成的成熟 LLM wiki。
