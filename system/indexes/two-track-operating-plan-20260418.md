---
id: system-two-track-operating-plan-20260418
type: system
topic: operating-system
question_type: workflow
language: bilingual
last_compiled_at: 2026-04-18
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Two-Track Operating Plan, 2026-04-18

这页只回答一个问题：

`这个 repo 现在到底该按哪两条主线继续，而不是继续被单一 vision demo 牵着走？`

## Classification / 任务归类

按 `$autoplan`，这件事属于：

`方案`

不是想法，不是检查，也不是排查。

因为当前需要锁定的是 repo 级 owner 和执行顺序，不是再判断某个旧 blocker 是否存在。

## One-Line Summary / 一句话总结

当前 repo 的默认主线应该固定成两条：

- `Track A = 120-source content pipeline`
- `Track B = ordinary-user usage surface`

其中默认 owner 仍然是：

- `content side owns truth, evidence, write-back, and system state`
- `frontend side owns presentation, interaction, and ordinary-user polish`

## Current Reality / 当前现实

2026-04-18 当前盘上现实；2026-04-21 复核后已更新数字：

- `raw/papers/` 有 `120` 张 paper source cards
- CKD `24/24` source cards 已是 `status: extracted`
- FIP `24/24` source cards 已回写为 `status: deep_extracted`
- IBD `24/24` source cards 已回写为 `status: deep_extracted`
- HCM `24/24` source cards 已是 `status: extracted`
- Diabetes `24/24` source cards 已是 `status: extracted`
- `system/indexes/` 里已有 `120` 个 round-1 deep-extraction worksheets
- `raw/images/` 当前只有 `8` 张 verified images，全部来自 CKD
- `scripts/app.py` 的普通用户前门已经补到可用，但 ask-native 产品感还没完全收口

## Track A / 内容主线

### Default Goal

这条线的目标不是继续证明架构可行。

这条线现在的目标是：

`把 120 张 source cards 按固定流程继续压成稳定的 disease module truth layer`

### Fixed Workflow / 固定流程

对新一轮重复性内容工作，默认直接走这条链：

`source card -> deep extraction -> narrow-owner densification -> inbox write-back -> dashboard/state write-back -> health check`

对应 owner 页：

- [disease-module bootstrap workflow](disease-module-bootstrap-workflow.md)
- [deep-extraction workflow](deep-extraction-workflow.md)
- [cross-disease densification queue](cross-disease-densification-queue.md)
- [content-side densification queue](content-side-densification-queue.md)
- [AI content workflow](../protocols/ai-content-workflow.md)

### No-Reconfirm Rule / 不反复确认规则

这条线里，下面这些重复步骤默认不需要再逐项找用户确认：

- 同病种 source card 的 round-1 deep extraction
- 已经明确 owner 的 narrow memo densification
- inbox staging
- dashboard / current-state write-back
- queue / status reality 同步

只有遇到下面情况才停下来重判：

1. source access blocker
2. source 本身有结构歧义
3. 两个上层组织方式互相冲突
4. truth claim 会被改写，而不是只补密度

### Best Next Content Queue / 当前最值得继续的内容队列

默认按这个顺序走：

1. continue `FIP / IBD` round-1 worksheet -> memo / dashboard / synthesis / unresolved write-back
2. after each bounded batch, sync `conflict-register`, `unresolved-questions`, and then broader owners like `source-depth-map`
3. `HCM / FIP / IBD` candidate image access only when it does not interrupt the main content line
4. keep writing source-card truth state upward into topic / dashboard / cross-disease owners

### What Track A Should Not Re-Center On

- 不要把 `CKD image gate` 继续当成 repo 唯一主任务
- 不要把普通用户前门继续当成内容侧默认 owner
- 不要为了看起来“全病种对称”而先铺双语 family

## Track B / 普通用户使用面

### Default Goal

这条线的目标不是继续加入口页。

这条线的目标是：

`让普通用户更自然地从问题进入系统，而不是先学 vault 结构`

### What Is Already Done

当前已经落地：

- Streamlit empty state
- example question chips
- provenance guide
- `How this works` onboarding
- sidebar vault search
- search result preview and query-context handoff
- structured error states
- `Copy markdown`
- sidebar `Save as .md`

相关文件：

- [scripts/app.py](../../scripts/app.py)
- [ux improvement handoff](ux-improvement-handoff-20260418.md)
- [ordinary-user usage guide bilingual](ordinary-user-usage-guide-bilingual.md)

### Main Remaining Gap

这条线当前最主要剩余缺口仍然是：

`它已经是 query-guided navigation，但还没有完全变成 ask-native product surface`

所以后续普通用户线默认优先：

1. 压缩二级入口重复
2. 继续让提问面赢过导航面
3. 让 disease navigation 更少暴露 operator noise
4. 在装好 `streamlit` 的 shell 里补 live smoke test

### What Track B Should Not Do

- 不要静默改内容 truth claim
- 不要改 dashboard / queue / audit reality
- 不要把 README 继续扩成 maintainer 和普通用户混写的长门面

## Safe Execution Order / 安全顺序

默认顺序固定为：

`content truth move -> content write-back -> frontend presentation pass -> final integration`

不要反过来。

否则 presentation 会立刻被内容 reality 打旧。

## Handoff Rule / 交接规则

后续模型接手时，默认先读：

1. 本页
2. [karpathy alignment handoff, 2026-04-18](karpathy-alignment-handoff-20260418.md)
3. [ux improvement handoff, 2026-04-18](ux-improvement-handoff-20260418.md)
4. [content vs frontend collaboration plan](content-vs-frontend-collaboration-plan.md)

如果只接内容线，再加读：

- [content-side densification queue](content-side-densification-queue.md)

如果只接普通用户线，再加读：

- [ordinary-user LLM wiki usability audit, 2026-04-10](ordinary-user-llm-wiki-usability-audit-20260410.md)

## One-Sentence Close / 一句话收口

这个 repo 现在最稳的继续方式不是“继续 vision demo”，而是：

`hold the content pipeline as the main production line, and treat ordinary-user UX as the parallel front-door line`
