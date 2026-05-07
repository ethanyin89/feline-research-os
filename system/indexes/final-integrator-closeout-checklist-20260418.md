---
id: system-final-integrator-closeout-checklist-20260418
type: system
topic: operating-system
question_type: checklist
language: zh
last_compiled_at: 2026-04-18
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Final Integrator Closeout Checklist, 2026-04-18

这页只回答一个问题：

`如果你是这一轮最后负责收口的模型，停笔前到底要检查什么？`

## 类型判断

按 `$autoplan` 的四分法，这件事属于：

`检查`

不是新方案。

因为现在不是重新决定方向，而是确保最后写回的现实和 repo 真实状态一致。

## One-Line Rule

最后收口的人，不是“再做一点”。

最后收口的人要做的是：

`确认现实、统一叙述、然后停在真实边界上。`

## What Final Integrator Owns

默认只负责 3 件事：

1. 判断 blocker 还在不在
2. 把所有 handoff / plan / checklist 写成同一个现实
3. 明确下一棒的窄范围

如果这 3 件事没做，最后一手就不算收口。

## Closeout Checklist

### 1. Filesystem Reality Check

先跑：

```bash
find raw/images -maxdepth 2 -type f | sort
```

问自己：

- 真实图片文件有没有出现？
- 还是只有 README？

不要跳过这步。

### 2. Plan Reality Check

再看：

```bash
sed -n '78,100p' PLAN.md
```

确认：

- `Step 2` 还是不是 `BLOCKED on human`
- `Step 5` 有没有仍然明确依赖 `Step 2`
- 有没有任何一句话已经和文件系统现实冲突

### 3. Checklist Reality Check

再看：

```bash
sed -n '54,72p' system/indexes/ckd-image-download-checklist-20260417.md
```

确认：

- 有没有哪一行可以诚实地从 `Downloaded = no` 改成 `yes`
- 有没有哪一行已经能从 `Verified against article label = no` 改成 `yes`

如果不能，就不要改。

### 4. Handoff Consistency Check

至少核对这几页是不是在讲同一个现实：

- [HANDOFF.md](../../HANDOFF.md)
- [usage-limit-emergency-handoff-20260417.md](usage-limit-emergency-handoff-20260417.md)
- [model-continuity-handoff-20260417.md](model-continuity-handoff-20260417.md)
- [codex-next-session-prompt.md](codex-next-session-prompt.md)

只要其中一页还在讲旧现实，下一位模型就容易走歪。

### 5. Scope Drift Check

最后问：

- 我有没有顺手去改别的 disease？
- 我有没有顺手重写脚本？
- 我有没有把 blocker 文案扩成新的方案文档？

如果答案是 `yes`，大概率已经 drift 了。

### 6. Stop Condition Check

最后一定要写清楚：

- 如果素材还没出现，为什么现在必须停
- 如果素材出现了，下一位模型只该改哪些文件

不要把停笔理由写成抽象句子。
写成具体边界。

## Current Closeout For This Repo

截至 `2026-04-21`，这个 repo 的正确 closeout 现实是：

- vision integration code 已完成
- 4 个 disease 的 image-ingest skeleton 已完成
- `raw/images/ckd/` 有 8 个已验证非 candidate 图片/表格资产
- `src-ckd-013` 仍然被 source-access 卡住，不能去掉 `candidate-*` gate
- 下一棒应继续处理 `src-ckd-013` 或扩展 FIP/HCM/IBD 图片验证，不要把未核对图片升为真实资产

## When To Update This Checklist

只有两种情况值得更新这页：

1. closeout 规则本身变了
2. 当前 repo 的主要 blocker 已经换了

如果只是今天又验证了一次 blocker 还在，不要重写这页。

## Related Pages

- [Root handoff](../../HANDOFF.md)
- [Usage-limit emergency handoff, 2026-04-17](usage-limit-emergency-handoff-20260417.md)
- [Model continuity handoff, 2026-04-17](model-continuity-handoff-20260417.md)
- [Vision-integrated query layer handoff, 2026-04-18](vision-query-layer-handoff-20260418.md)
- [Multi-model collaboration boundary](multi-model-collaboration-boundary.md)

## One-Line Summary

最终收口不是“再补一点内容”。

而是：

`把文件系统现实、PLAN、checklist、handoff 四件事写成同一个真相。`
