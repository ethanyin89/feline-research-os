---
id: system-disease-module-maturity-ladder
type: system
topic: operating-system
question_type: workflow
language: zh
last_compiled_at: 2026-04-23
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Disease Module Maturity Ladder

这页回答的是另一个非常具体的问题：

`一个 disease module 到底做到哪一层，应该怎么统一判断，而不是每次重新靠感觉描述？`

这页不是 bootstrap 页。

这页是 bootstrap 之后的统一成熟度 owner。

## 为什么这页现在必须存在

反复执行之后，已经出现了稳定重复动作：

- 建 shell
- 建 source index
- 做 source cards
- 做 selective deep extraction
- 压 compiled memo
- 接 dashboard / navigation / synthesis
- 再接 briefing / dossier / slides
- 再接 bilingual compiled
- 再接 output language matrix
- 再接 verify / write-back / promotion / health-check

如果这套动作继续只靠记忆，后面判断每个 disease 的状态就会越来越乱。

所以现在应该把它固化成一条统一 maturity ladder。

## 一句话版本

默认把 disease module 的成熟度分成 7 层：

`shell -> compile -> extraction -> memo -> output -> bilingual -> control`

但从现在开始，还要额外看一条新的成熟信号：

`second-wave narrow-owner signal`

## Level 1: Shell

### What exists

- `topics/<disease>/index.md`
- `navigation.md`
- `current-state-dashboard.md`
- 最小主干 topic pages

### Exit Condition

这个 disease 已经不是一个名字，而是一个能进入的模块。

## Level 2: First Compile

### What exists

- full seed corpus mapped
- source index
- reading plan
- full source-card layer
- first topic compile

### Exit Condition

这个 disease 不再只是 paper list，而是已经有主骨架。

## Level 3: Selective Deep Extraction

### What exists

- broad review / guideline anchor 已 deep-extracted
- strongest mechanism anchor 已 deep-extracted
- strongest recognition / endpoint anchor 已 deep-extracted
- strongest treatment / translation anchor 已 deep-extracted
- at least one overclaim-boundary paper 已 deep-extracted

### Exit Condition

上层 compile 不再只是 title-led。

## Level 4: Compiled Memo Layer

### What exists

至少应有其中 3 类：

- diagnostic-workup memo
- treatment-evidence memo
- branch-boundary memo
- bridge memo
- genotype / severity memo
- endpoint-separation memo

### Exit Condition

这个 disease 已经不是“topic page 拼盘”，而是有可复用的 compiled compression。

## Level 5: Output Layer

### What exists

最少先有：

- briefing `working-en`
- briefing `-en`
- briefing `-zh`

更强版本再加：

- dossier `working-en / en / zh`
- slides `working-en / en / zh`

### Exit Condition

这个 disease 已经不只是 compiled wiki pages，而是已经长出真正 output surface。

## Level 6: Bilingual Compiled Layer

### What exists

高复用页开始双语化，例如：

- dashboard bilingual
- synthesis bilingual
- mechanism bilingual
- recognition bilingual
- endpoint bilingual
- translation bilingual

### Exit Condition

跨语言复用已经不再只靠输出文件，而是进入 compiled page 层。

## Level 7: Control Layer

### What exists

- output language matrix
- verify / claim lookup route
- query-to-writeback visibility
- promotion checklist
- promotion examples
- health checks
- language QA or traceability where relevant

### Exit Condition

这个 disease 不只可读，也已经进入：

`auditable, write-back-native, controlled module`

## Second-Wave Narrow-Owner Signal

### What exists

不是再额外加一整层。

它是 Level 7 之上的一个更硬信号，用来判断一个 module 是否开始进入：

`control-inside-control`

也就是第一层窄 owner 已经存在并被 topic / dashboard / synthesis 吸收之后，又开始出现更窄的 owner，用来回答：

- branch 内部更硬的 boundary
- branch shift 到底在哪个 gate 上发生
- 两个不同轴上的 winner 不能混成一个结论时，分别谁赢
- 如果只能再推进一步，下一张 priority memo 应该给谁

### Exit Condition

当一个 disease 开始稳定地产出这类 second-wave owner，并且这些 owner 已经反写回主干页时，就说明它不只是有 control layer。

它已经开始进入：

`self-compressing, second-wave densification territory`

## 如何使用这条梯子

以后每次判断一个 disease module 到哪一步，不要再说泛泛的：

- `started`
- `working`
- `quite mature`

而应该直接说：

- `CKD is at Level 7`
- `IBD is at Level 7, but regulatory still thin`
- `HCM is between Level 6 and Level 7`
- `FIP is between Level 6 and Level 7`

如果已经开始出现第二层窄 owner，则要再补一句：

- `and now showing second-wave narrow-owner signal`

这样状态判断会立刻清楚很多。

## 当前五病种放在哪

### CKD

`Level 7`

原因：

- compiled spine 很厚
- briefing / dossier / slides 都有
- bilingual compiled 有
- output matrix 有
- audit / QA / traceability / route memo 都已进入控制层
- route layer 现在也开始出现更窄的稳定 comparison owner，例如 `archetype-route cleanliness`
- 第二层信号也已经出现，例如 `next route-memo priority`

所以 CKD 现在不是只有 Level 7。

它已经开始表现出：

`Level 7 with second-wave priority-signal`

### IBD

`Level 7`

原因：

- 24 / 24 deep extraction complete
- 24 / 24 paper cards are now `deep_extracted`
- compiled memo 很厚
- briefing / dossier / slides 都有
- bilingual compiled 页面覆盖高复用主干
- output matrix 和 language QA 已存在
- regulatory branch 现在也开始出现更窄的稳定 owner，例如 `claim-fit / route-fit boundary`
- 第二层信号也已经出现，例如 `best overall vs route-cleaner archetype`

所以 IBD 现在不是只有 Level 7。

它已经开始表现出：

`Level 7 with second-wave two-winner signal`

### HCM

`Level 6.5 到 7`

原因：

- compiled memo 已存在
- briefing / dossier / slides 已有 `working-en / en / zh`
- bilingual compiled 已经很广
- output matrix 已有，但 overall control thickness 仍略薄于 CKD / IBD
- biomarker / frontier / regulatory branch 现在已经开始出现更窄的稳定 owner，例如 `biomarker use-case`
- 第二层信号也已经出现，例如 `AI augmentation boundary` 和 `product-type separation`

所以 HCM 现在不该再简单写成 Level 6.x。

更准确的是：

`late Level 6.5 moving into Level 7, with second-wave boundary signal`

### FIP

`Level 6.5 到 7`

原因：

- 24 / 24 deep extraction complete
- briefing / dossier / slides 都有
- bilingual compiled 主干已经成形
- output layer 和 topic spine 已经对齐
- control layer 仍略薄于 CKD / IBD
- 但第一层 narrow owner 已经足够厚
- 第二层信号也已经出现，例如 `neurologic workup gate` 和 `neurologic rescue boundary`

所以 FIP 现在更准确的是：

`late Level 6.5 moving into Level 7, with second-wave gate-and-boundary signal`

### Diabetes

`starter Level 5`

原因：

- 24-source seed corpus 已经 mapped
- source index 已存在
- reading plan 已存在
- 24 / 24 first-pass source cards 已存在
- 24 / 24 round-1 worksheets 已存在，且 24 / 24 source cards 已是 explicit full source-card depth；paper-card verification overlay 现在是 24 deep_extracted
- 4 张 U.S. SGLT2 regulatory / label source cards 已存在：Bexacat / Senvelgo FDA FOI + DailyMed current labels
- 2 张 SGLT2 label-section worksheets 已存在：Bexacat / Senvelgo label-section extraction
- narrow memo 层已存在并继续加厚：remission、diet architecture、endocrine-secondary diabetes、neuropathy、SGLT2 safety/regulatory boundary、SGLT2 primary FDA source、SGLT2 current-label control、SGLT2 label-section comparison、treatment branch comparison、diagnostic/monitoring workup、obesity/body-condition、breed-risk、pancreatitis
- topic spine 已扩展到 20 页，包括 dashboard、first bilingual dashboard、mechanism、recognition、endpoint、translation、regulatory boundary、synthesis，以及 diagnostic/workup、diet、remission、treatment map、obesity/body-condition、endocrine-secondary、pancreatitis、neuropathy/complications、epidemiology/breed-risk、SGLT2 label-control 分支
- first output layer 已存在：briefing / dossier / slides 都已有 `working-en / en / zh`
- first high-reuse bilingual compiled dashboard 已存在
- conflict-register boundary audit 已存在，覆盖 disease model、remission/diet、SGLT2 route/safety、obesity sequencing、breed-risk denominator
- 但还没有 broad topic/output-level clinical compression、full label section extraction、broad bilingual compiled family、或成熟 control layer

所以 Diabetes 当前不是成熟模块，而是：

`starter Level 5, with topic-count parity, first high-reuse bilingual dashboard, clean deep-extracted paper-card coverage, and U.S. SGLT2 FOI/current-label/label-section control started, but not topic/output clinically mature or bilingual mature`

## 默认推进顺序

如果某个 disease 到了：

### Level 2

下一步默认做：

- selective deep extraction

### Level 3

下一步默认做：

- compiled memos

### Level 4

下一步默认做：

- output layer

### Level 5

下一步默认做：

- bilingual compiled on highest-reuse pages

### Level 6

下一步默认做：

- output language matrix
- highest-reuse bilingual compiled pages
- disease dashboard / navigation / synthesis 的状态回写
- cross-disease audit 与 maturity ladder 的同步回写

### Level 7

下一步默认做：

- selective densification only
- if seed corpus is already `24 / 24` round-1 complete, do not reopen bootstrap-style completion loops
- cross-disease priority should be read from [cross-disease-densification-queue.md](cross-disease-densification-queue.md)
- if frontend and content are split, content-side default should be read from [content-side-densification-queue.md](content-side-densification-queue.md)

不要再继续机械加页。

## 和 bootstrap workflow 的关系

- [disease-module-bootstrap-workflow.md](disease-module-bootstrap-workflow.md)
  负责病种第一次进入系统
- 这张 maturity ladder
  负责病种进入系统后，如何判断它现在到了哪一层

两张页一起用，才不会混淆：

- `怎么开始`
- `现在做到哪`

## 一句话收口

以后 disease module 的状态不该再靠印象描述。

应该默认用这条梯子判断：

`它现在在哪一层，下一层默认该做什么，哪一层还没有发生。`
