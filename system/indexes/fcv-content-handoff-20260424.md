---
id: system-fcv-content-handoff-20260424
type: system
topic: fcv
question_type: workflow
language: bilingual
last_compiled_at: 2026-04-24
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# FCV Content Handoff, 2026-04-24

这页只回答一个问题：

`如果当前 FCV 内容线要交给下一棒，最真实的执行断点是什么？`

## 类型判断

按 `$autoplan` 的四分法，这一棒不是新想法，也不是新方案。

它现在属于：

`检查 + 执行`

更准确地说，是：

`先确认 FCV source-card 真实状态，再沿当前 densification 队列继续推进，不要重新开 office-hours 式问答。`

## One-Line Rule

下一棒不要再做这件事：

`每补一张卡就停下来找用户确认`

Update note, 2026-04-28: this older handoff has been superseded on source-depth status. FCV is now `24/24` full/deep-extracted at the paper source-card layer. Use this document for historical branch rationale only, not for current partial-card counts.

下一棒应该做的是：

`沿 FCV 当前 owner map 连续 deep-extract，只有在方向变更或 scope 扩张时才上 gate`

## 30-Second Reality

- FCV 仍然是 `24/24` seed paper source cards.
- 当前 FCV 已到 `24/24` explicit full source-card depth，`24/24 deep_extracted`.
- 当前 FCV 不是 bootstrap from zero 了，已经有稳定的 branch owner 结构。
- broad control 层已经不空：
  - `src-fcv-004` practical guideline/control
  - `src-fcv-007` modern broad-control
  - `src-fcv-009` diagnosis/control bridge
- vaccine/endpoint 层也不再只是宽泛综述：
  - `src-fcv-003` breadth
  - `src-fcv-010` early field-fit stress test
  - `src-fcv-011` challenge protection
  - `src-fcv-012` serology-resistance prediction
  - `src-fcv-017` persistence-control
  - `src-fcv-022` cellular immunity
- therapy 层已经形成三段式：
  - `src-fcv-014` assay-stage discovery
  - `src-fcv-008` interferon-sensitivity caution
  - `src-fcv-018` first in vivo therapy
- recognition / extension 层也已经有 deep-extracted anchors：
  - `src-fcv-006`
  - `src-fcv-020`
  - `src-fcv-021`

## Current Source-Depth Reality

截至 `2026-04-24`：

- full / deep_extracted: all `src-fcv-001` through `src-fcv-024`

- remaining `partial / source_checked`: none

## What Was Just Completed

当前 round 已经完成并写回：

1. `src-fcv-007`
   modern broad-control anchor
2. `src-fcv-008`
   interferon-sensitivity caution anchor
3. `src-fcv-009`
   diagnosis/control bridge
4. `src-fcv-010`
   early field-fit stress test
5. `src-fcv-012`
   serology-resistance prediction
6. `src-fcv-014`
   assay-stage therapy discovery
7. `src-fcv-018`
   first in vivo therapy
8. FCV dashboards / source maps / owner memos
   已同步到当前 17-anchor 现实

## What Not To Re-Do

下一棒不要回头重做这些：

- 不要重新解释为什么 FCV 需要 branch separation
- 不要重写 FCV 高层结构页而不增加真实 source depth
- 不要再把 `src-fcv-008` / `014` / `018` 当成 first-pass therapy mentions
- 不要再把 `src-fcv-009` 当成只有一句 `PCR caution` 的轻卡
- 不要把 `src-fcv-010` 误写成 current-market vaccine ranking paper
- 不要把 `src-fcv-012` 升级成 universal no-booster policy paper
- 不要因为 `src-fcv-019` 看起来 broad 就把它升为高权重 owner

## Default Next Move

如果用户没有给更窄的新指令，最稳的默认下一棒是：

1. `src-fcv-013`
   因为它直接补 challenge branch，能和 `src-fcv-011` 形成更完整的 vaccine-protection pair
2. `src-fcv-024`
   因为它能加厚 field epidemiology / vaccine-failure interpretation
3. `src-fcv-005`
   因为它能把 geography-specific vaccine-fit 这一层补到更可复用

这三张比 `src-fcv-019` 值钱。

## Priority Order

### Tier A

- `src-fcv-013`
- `src-fcv-024`

### Tier B

- `src-fcv-005`
- `src-fcv-002`

### Tier C

- `src-fcv-016`
- `src-fcv-023`

### Keep Low

- `src-fcv-019`

除非用户明确要 literature-context page，否则不要优先 deep-extract `src-fcv-019`。

## Why `src-fcv-013` Next

因为当前 vaccine branch 虽然已经有：

- breadth
- early field-fit stress test
- challenge protection
- serology
- persistence
- cellular immunity

但 challenge branch 还是更偏单锚点，由 `src-fcv-011` 扛主力。

`src-fcv-013` 会带来的价值不是“再多一张 vaccine paper”，而是：

`让 challenge/protection 这一层从单锚点变成双锚点`

这样 endpoint handbook 和 vaccine-persistence memo 才更稳。

## Current Write Scope For The Next Model

如果下一棒继续 FCV densification，推荐写入范围只保持在：

- `raw/papers/src-fcv-013.md`
- `raw/papers/src-fcv-024.md`
- `raw/papers/src-fcv-005.md`
- `system/indexes/src-fcv-013-deep-extraction-round1.md`
- `system/indexes/src-fcv-024-deep-extraction-round1.md`
- `system/indexes/src-fcv-005-deep-extraction-round1.md`
- `system/indexes/fcv-source-depth-map.md`
- `system/indexes/fcv-source-index.md`
- `system/indexes/fcv-vaccine-persistence-boundary-memo.md`
- `topics/fcv/endpoint-handbook.md`
- `topics/fcv/current-state-dashboard.md`

不要默认扩到全 repo。

## Verification Commands

交接后先跑：

```bash
python3 scripts/health.py
python3 - <<'PY'
from pathlib import Path
import re
for p in sorted(Path('raw/papers').glob('src-fcv-*.md')):
    text = p.read_text(encoding='utf-8')
    sid = re.search(r'^id:\s*(.+)$', text, re.M).group(1)
    depth = re.search(r'^extraction_depth:\s*(.+)$', text, re.M).group(1)
    ver = re.search(r'^verification_status:\s*(.+)$', text, re.M).group(1)
    if depth != 'full':
        title = re.search(r'^title:\s*"(.+)"$', text, re.M)
        print(f'{sid}\t{depth}\t{ver}\t{title.group(1) if title else ""}')
PY
sed -n '1,120p' system/indexes/fcv-source-depth-map.md
```

你应该看到：

- FCV `full: 24`
- FCV `partial: 0`
- no FCV seed paper cards remain in the partial list

## Handoff Prompt

直接给下一棒这段：

```text
You are working in this repo:
/Users/jiawei/Desktop/insclaude/feline-research-os

Read these files first:
1. system/indexes/fcv-content-handoff-20260424.md
2. system/indexes/fcv-source-depth-map.md
3. system/indexes/fcv-source-index.md
4. topics/fcv/current-state-dashboard.md
5. topics/fcv/endpoint-handbook.md
6. system/indexes/fcv-vaccine-persistence-boundary-memo.md

Current date: 2026-04-28

Your role:
WRITER FOR ONE NARROW SCOPE ONLY

Task type:
check + execute

Current round goal:
recompile downstream FCV topic pages against the completed source-card layer without reopening architecture or re-asking routine confirmation questions

Current reality you must respect:
- FCV is already at 24/24 full deep-extracted paper-card depth
- broad control, recognition, therapy, and most major vaccine branches already have deep anchors
- the next highest-value gap is no longer remaining partial cards, but downstream synthesis and ordinary-user presentation

Default next move:
1. recompile topics/fcv/current-state-dashboard.md and bilingual counterpart
2. recompile topics/fcv/synthesis-index.md and bilingual counterpart
3. reconcile endpoint, mechanism, recognition, translation, and regulatory pages against the now-complete source-card layer

Write scope:
- system/indexes/fcv-source-depth-map.md
- system/indexes/fcv-source-index.md
- system/indexes/fcv-vaccine-persistence-boundary-memo.md
- topics/fcv/endpoint-handbook.md
- topics/fcv/current-state-dashboard.md

Do not:
- reopen FCV architecture from zero
- treat src-fcv-019 as a priority decision owner
- ask the user for confirmation after every routine source-card promotion
- touch unrelated disease modules

Do:
- keep write-back consistent with the actual card state
- keep vaccine claims below final ranking language
- keep challenge, breadth, serology, persistence, and therapy as separate endpoint families
```

## One-Line Close

下一棒最该做的不是再解释 FCV 怎么分层。

而是：

`把下游 FCV 主题页同步到 24/24 full/deep-extracted 的真实来源层。`
