---
id: system-source-hierarchy-and-claim-fit-policy
type: system
topic: operating-system
last_compiled_at: 2026-04-24
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
language: zh
---

# Source Hierarchy And Claim-Fit Policy

这页回答的是一个系统级问题：

`同样都叫 source，但 guideline、review、single study、case series、official label、product page、editorial，到底谁能决定什么，谁只能当背景，谁默认不能撑强结论？`

这不是单病种问题。

这是整个 `feline-research-os` 的证据治理规则。

## 一句话版本

新 source 进入 vault 时，必须同时判断两件事：

1. `它是什么来源类型`
2. `它适合支撑什么类型的 claim`

如果只写了 `source_kind` 和 `evidence_level`，但没有判断 claim-fit，后面的 topic compile 很容易把弱 source 写得像强 source。

## 先讲核心原则

这套系统里，source 不是单轴排序。

不是说：

`guideline > review > study > case > web`

就结束了。

真正应该看的，是两个轴：

1. **Authority axis**
   这个 source 在它自己的类型里，是否是正式、可追溯、可复核的来源。
2. **Claim-fit axis**
   这个 source 最适合支撑哪一类结论，而不是“它看起来信息很多”。

比如：

- 官方 label 对 `indication / contraindication / warning / route / jurisdiction-specific status` 很强
- 但对 `disease-modifying superiority` 不强

再比如：

- broad review 对 `branch architecture / synthesis / field map` 很强
- 但对 `one numeric endpoint winner` 不强

所以这页不做一个平面的“谁高谁低”榜单。

它做的是：

`source family -> strongest safe use -> things it must not control`

## Level 1: Source Family Rules

### Family A: Official Regulation / Official Label / Official Guidance

包括：

- 法规
- 官方审批记录
- DailyMed / FDA / EMA / VMD / ministry label
- 官方 guidance / GFI / guideline

典型 frontmatter：

- `source_kind: regulation` 或 `guidance`
- `evidence_level: regulation | guidance | guideline`

最强适用：

- jurisdiction-specific approval status
- indication / contraindication / warning / route / label wording
- regulatory path boundary
- official eligibility / submission framing

不能主控：

- disease biology
- comparative efficacy winner
- real-world clinical superiority
- broad mechanism synthesis

一句话读法：

`官方 source 最强的是 label truth，不是 disease truth。`

### Family B: Guideline / Consensus / Practice Guidance

包括：

- ABCD guideline
- consensus statement
- society guidance
- practice-facing expert guideline

典型 frontmatter：

- `source_kind: paper` 或 `guidance`
- `evidence_level: guideline`

最强适用：

- workup order
- prevention / management architecture
- standard-of-care framing
- bounded practical recommendations

不能主控：

- product superiority
- frontier mechanism closure
- one-paper numeric endpoint ranking

一句话读法：

`guideline 最强的是 practice architecture，不是 product winner logic。`

### Family C: Broad Review / Systematic Review / Narrative Review

包括：

- broad disease review
- mechanism review
- systematic review
- umbrella-style synthesis

典型 frontmatter：

- `source_kind: paper`
- `evidence_level: review`

最强适用：

- disease shell / branch map
- mechanism spine
- recognition architecture
- evidence landscape
- finding where the real argument is

不能主控：

- label-level claims
- exact current-market status
- one-study-like treatment winner language unless source itself is systematic and the conclusion is still bounded

一句话读法：

`review 最强的是结构，不是最后一句话。`

### Family D: Original Study

包括：

- trial
- cohort
- case-control
- experimental study
- challenge study
- epidemiology field study

典型 frontmatter：

- `source_kind: paper`
- `evidence_level: original-study`

最强适用：

- specific endpoint ownership
- branch-specific effect or association
- mechanistic or epidemiologic anchor
- treatment / assay / biomarker / challenge detail

不能主控：

- automatic standard-of-care authority
- universal generalization outside study design
- cross-jurisdiction regulatory claims

一句话读法：

`single study 最强的是细节，不是总路线。`

### Family E: Case Series / Case Report

包括：

- rare phenotype report
- unexpected adverse event
- unusual disease extension
- early rescue signal

典型 frontmatter：

- `source_kind: paper`
- `evidence_level: case-series`

最强适用：

- rare but important awareness
- extension branch visibility
- failure mode / rescue / unusual presentation
- “this branch exists” level signal

不能主控：

- prevalence
- routine workup hierarchy
- final treatment ranking
- standard recommendation

一句话读法：

`case series 最强的是提醒你别漏掉，不是告诉你主路线。`

### Family F: Commentary / Editorial / Perspective / Product Promotion / Marketing Web

包括：

- editorial
- perspective piece
- special issue intro
- company product page
- promotional brochure
- non-official marketing page

典型 frontmatter：

- `source_kind: paper | web`
- `evidence_level: commentary`

最强适用：

- context
- terminology
- market-awareness clue
- “go find the real source” 的导航功能

不能主控：

- efficacy
- safety
- hierarchy
- recommendation
- decision-grade route

一句话读法：

`commentary / promo 只能当 context，不是 decision-bearing evidence anchor。`

## Level 2: Claim-Fit Table

| Source family | Strongest safe use | Can support topic architecture? | Can support numeric/detail claim? | Can support regulatory / label claim? | Can support ranking / recommendation? |
|---|---|---:|---:|---:|---:|
| official regulation / label | label truth, route boundary, jurisdiction status | limited | limited | yes | only for official label wording, not comparative winner |
| guideline / consensus | practical order, workup, prevention/management frame | yes | bounded | sometimes, if official/consensus text directly says so | bounded, not product winner |
| broad/systematic review | architecture, synthesis, branch map | yes | bounded | no | usually no, unless explicitly systematic and still bounded |
| original study | branch-specific detail, endpoint ownership | yes | yes | no | only very bounded, never auto-generalized |
| case series / case report | rare branch visibility, rescue warning | limited | limited | no | no |
| commentary / promo / marketing | context only | limited | no | no | no |

## Level 3: Promotion Rules

### Rule 1

topic 页的主骨架，优先由：

- guideline
- broad review
- strongest original-study anchor

共同决定。

不要让：

- commentary
- product page
- lone case series

来控制 topic 的主线。

### Rule 2

如果问题是：

- `这个病怎么组织`
- `workup 顺序怎么排`
- `主要 branch 有哪些`

优先读：

- guideline
- broad review
- consensus

不是先读单篇 study。

### Rule 3

如果问题是：

- `某 endpoint 到底测了什么`
- `某干预具体改善了什么`
- `某 biomarker 的 performance detail 是什么`

优先读：

- original study
- deep extraction worksheet

不是先读 review 的一句总结。

### Rule 4

如果问题是：

- `某产品现在能不能这么说`
- `某适应症、route、warning 是否是官方可写内容`

优先读：

- official label
- official regulation
- official guidance

不是 review，不是 conference，不是 product page。

### Rule 5

case series 和 commentary 默认都不进入高位 owner。

它们通常只配做：

- boundary note
- extension branch
- caution box
- context row

## Level 4: FCV 这次暴露出来的典型问题

你这次给 FCV 的 24 篇里，天然就是混合包：

- guideline: `src-fcv-004`
- broad review: `src-fcv-001`, `src-fcv-002`, `src-fcv-007`, `src-fcv-009`, `src-fcv-015`
- original study: `src-fcv-003`, `006`, `011`, `012`, `017`, `022` 等
- commentary/editorial context: `src-fcv-019`

如果没有这页规则，系统很容易出两种错：

1. 把 commentary 写得像 evidence anchor
2. 把 single study 写得像 final disease architecture owner

这正是你指出来的问题。

## Level 5: Ingest 时必须新增的判断

以后每张新 source card，在 Stage 1 / Stage 2 至少要补这 4 个判断。

### A. Source Family

它属于哪一类：

- official regulation / label
- guideline / consensus
- broad review
- original study
- case series
- commentary / promo

### B. Strongest Safe Use

它最适合支撑：

- disease architecture
- endpoint detail
- regulatory truth
- boundary / extension
- context only

### C. What It Must Not Control

必须显式写一句：

`this source should not control ...`

### D. Promotion Priority

它是：

- anchor
- support
- context

还是：

- do-not-promote

## 最小执行规则

以后新病种 bootstrap 时，不允许只写：

- `source_kind`
- `evidence_level`

就算完成。

至少还要在 source card 正文里写明：

1. 它是哪个 family
2. strongest safe use 是什么
3. what it must not control

否则后续 compile 很容易误升格。

## 对现有系统的直接影响

### 对 `source-schema.md`

Schema 至少要明说：

- `source_kind` 不是 authority 排名
- `evidence_level` 不是 claim-fit 判断的替代物

### 对 `compile-checklist.md`

Ingest 阶段必须加入：

- source family classification
- strongest safe use
- what it must not control
- anchor / support / context judgment

### 对 `disease-module-bootstrap-workflow.md`

Step 2 和 Step 3 以后都要默认做 hierarchy placement，而不是只建卡不定级。

## 当前默认禁止项

没有做 family / claim-fit 判断前，默认禁止：

1. 用 commentary / promo 控制 topic 主结论
2. 用 label source 控制 disease biology
3. 用单篇 study 直接写 final standard-of-care
4. 用 case series 写 prevalence 或 main route order
5. 因为 source 信息量大，就把它升成 owner

## 最后一句

source 的强弱，不只取决于“它是不是论文”。

取决于：

`它是什么 family，它最适合支撑什么 claim，它不该控制什么。`

这才是这套 vault 应该采用的等级规则。
