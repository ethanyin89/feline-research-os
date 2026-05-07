---
id: system-durable-agent-codification-protocol
type: system
topic: operating-system
last_compiled_at: 2026-04-09
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
language: zh
---

# Durable Agent Codification Protocol

这页回答的是一个系统问题：

`怎样让这个 research OS 不靠同一类指令被重复下达，仍然能持续推进？`

它不是在讲某个病种。

它是在把一条更硬的 operating rule 写下来：

`不要做 one-off work。重复性工作第一次做完后，必须尽快被编成系统资产。`

## 最短结论

这件事按 `autoplan` 的分类，属于：

`方案`

不是检查，也不是排查。

因为你给的不是一个待验证事实，而是一条要改变当前项目 operating mode 的规则。

## 当前项目里，对 Garry Tan 那段话的正确翻译

OpenClaw 原文里说的是：

- 先手工做一次
- 用户认可后，变成 skill
- 如果是 recurring，就接进 cron

在当前 `feline-research-os` 里，不能机械照抄成：

- `SKILL.md`
- `openclaw cron add`

因为当前系统真正的可执行层不是 OpenClaw runtime。

当前项目里，对应物应该是：

- `system/indexes/` 里的 protocol / workflow / memo
- `system/prompts/` 里的 operating prompt
- `system/schemas/` 里的字段和页面约束
- `system/health-checks/` 里的持续纠偏
- `topics/*/current-state-dashboard.md` 里的下一步驱动

所以这套系统里的正确映射是：

`manual repetition -> accepted pattern -> codified system asset -> reused by default`

不是：

`manual repetition -> memory`

## 硬规则

从现在开始，当前项目里的重复性工作，默认遵守下面 4 条。

### 1. 不允许把明显会重复的工作永远当成一次性任务

如果某件事显然还会继续发生，比如：

- 新病种 disease shell 的建立
- source card 的 first-pass ingest
- high-value source 的 deep extraction
- compiled page 的 traceability 补齐
- language QA corrections
- output naming / language alignment

那它就不能永远停留在：

`这次我替你做完了`

它最终必须变成某种系统资产。

### 2. 第一次先手工做，小批量验证

不要一上来就把抽象规则写太满。

默认流程应该是：

1. 先在 `3-10` 个真实对象上手工跑一轮
2. 看输出是否稳定
3. 看用户是否认可这类结果
4. 再决定怎么固化

这件事当前项目其实已经这样做过多次，比如：

- CKD 的 deep extraction workflow
- verification status standard
- sentence-level traceability standard
- language QA rollout

## 3. 一旦模式稳定，就必须固化成唯一 owner

每类重复性工作，都应该有且只有一个主 owner。

也就是：

`MECE`

不能：

- 同一类工作有两套互相重叠的规则
- 或者没人负责，纯靠记忆

在当前项目里，允许的 owner 类型主要有 5 种：

| Owner Type | 当前项目里的对应物 | 适用场景 |
|---|---|---|
| protocol | `system/indexes/*-protocol.md` | 硬规则、分级、允许/禁止项 |
| workflow | `system/indexes/*-workflow.md` | 可重复执行的步骤流 |
| prompt | `system/prompts/*.md` | 模型运行时的固定行为约束 |
| schema | `system/schemas/*.md` | 页面字段、frontmatter、结构约束 |
| health check | `system/health-checks/` | 持续发现漂移、过期、越界 |

选择原则很简单：

- 如果核心问题是“什么能说、什么不能说”，用 `protocol`
- 如果核心问题是“按什么顺序做”，用 `workflow`
- 如果核心问题是“模型每次都该怎么执行”，用 `prompt`
- 如果核心问题是“页面必须长成什么样”，用 `schema`
- 如果核心问题是“怎么持续查错”，用 `health check`

## 4. 第二次再出现同类需求，默认应该复用系统资产

这条最关键。

如果同类事情第二次还需要用户完整重讲一遍，说明第一轮没有真正完成。

在当前项目里，“完成”不再只等于：

- 这一页写完了
- 这一批 source 卡建完了

更高一层的完成应该是：

- 这类工作以后怎么做，已经被系统接住了

## 当前项目的标准循环

从现在开始，适合当前项目的 durable cycle 应该写成：

1. `Concept`
   先说清楚这类工作要解决什么问题
2. `Prototype`
   在 `3-10` 个真实对象上手工跑一轮
3. `Evaluate`
   检查输出是否稳定、是否被接受
4. `Codify`
   固化成 protocol / workflow / prompt / schema / health check 之一
5. `Default Reuse`
   后续相同类型任务默认按这套资产继续
6. `Monitor`
   如果实际执行中出现漂移，再修资产本身

## 这条规则落到当前项目里，意味着什么

### 对 CKD

CKD 不是只产生内容。

CKD 已经产出了多类系统资产：

- deep extraction workflow
- claim audit protocol
- verification status standard
- sentence-level traceability standard
- language QA protocol

这说明 CKD 不只是 disease module。

它还是当前 vault 的：

`operating prototype`

### 对 FIP / IBD / HCM

后续新病种不应该再像 CKD 早期那样，靠大量逐步确认才能推进。

正确状态是：

- 默认复用 CKD 已经产出的系统资产
- 只在遇到真正的新型重复工作时，再跑一次 `concept -> prototype -> codify`

### 对我当前的执行方式

以后在当前项目里，如果我发现某类工作已经出现第二次或第三次，我默认应该追问的不是：

`这次要不要继续做？`

而是：

`这类工作该被哪个 system asset 接住？`

## 当前项目里的最小可执行判断

以后遇到重复任务时，先问这 3 个问题：

1. 这是不是明显还会继续发生？
2. 这类输出是不是已经稳定到可以复用？
3. 这件事应该归哪个唯一 owner？

如果三个答案分别是：

- 是
- 是
- 能说清

那就不应该只把它做完。

而应该把它：

`编进系统`

## 当前项目与原始 OpenClaw 说法的差异

有两个差异必须明确。

### 1. 当前项目的 durable asset 不只是一种 “skill”

在这个 vault 里，很多最值钱的复用资产不是 `SKILL.md`。

而是：

- protocol
- workflow
- prompt
- schema
- health check

### 2. 当前项目的“自动运行”不一定等于 cron

在 OpenClaw 里，cron 是主要自动化外壳。

在这个项目里，更真实的自动化形式是：

- 默认 operating mode 直接复用既有 workflow
- dashboard 持续把下一步显式挂出来
- health check 负责发现结构漂移
- 新病种自动继承旧病种打磨出的处理方式

所以对当前项目来说，更准确的话不是：

`every repeated task ends on a cron`

而是：

`every repeated task ends with a durable owner in the system`

## 当前最值得坚持的测试

以后判断这套 research OS 有没有变强，最值得看的不是“又多了几页”。

而是这个测试：

`如果同类事情第二次出现，系统是不是已经知道该怎么接住，而不是继续靠人重新提醒。`

## 一句话收口

这套项目从现在开始，不该只追求：

`内容越来越多`

而应该追求：

`重复工作越来越少靠重讲，越来越多靠系统资产复用。`
