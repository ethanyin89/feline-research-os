---
id: system-ask-the-vault-acceptance-checklist-20260416
type: system
topic: operating-system
question_type: checklist
language: zh
last_compiled_at: 2026-04-16
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Ask The Vault Acceptance Checklist, 2026-04-16

这页只回答一个窄问题：

`现在 ask-the-vault 已经有了 query.py 和 app.py，下一步怎么判断它是否真的可用，而不是“代码看起来已经写完”？`

## 类型判断

这件事属于：

`检查`

不是再发散想法，也不是排查故障。

现在最缺的不是新架构，而是一个稳定的验收面。

## 最短结论

先不要继续加更复杂的 agent 行为。

先用一组固定问题，验证 4 件事：

1. 能不能稳定路由到对的 disease 和 topic
2. 能不能给出足够具体的 answer surface
3. provenance tag 有没有失真
4. write-back 会不会把垃圾写进库里

只要这 4 件事还没过，就不应该继续放大前端或 agent loop。

最容易影响通过率的 4 题，先看：

- [ask-the-vault priority answer surfaces](ask-the-vault-priority-answer-surfaces-20260416.md)
- [ask-the-vault router hit map](ask-the-vault-router-hit-map-20260416.md)
- [ask-the-vault acceptance fault tree](ask-the-vault-acceptance-fault-tree-20260416.md)
- [ask-the-vault day-1 runbook](ask-the-vault-day-1-runbook-20260416.md)

## Pass Gate

只有同时满足下面 6 条，才算 v1 通过：

1. 8 个核心问题里至少 6 个答案可接受
2. 0 个答案出现伪造 source id
3. 0 个答案把明显推断伪装成 `quoted_fact`
4. 至少 4 个答案能把用户直接带到最短答案面，而不是泛泛 topic 导航
5. `--write-back` 产物 frontmatter 完整，且文件名稳定
6. 至少 1 个 cross-disease 问题被明确降级处理，而不是乱猜

## How To Run

CLI first. UI second.

先用：

```bash
python3 scripts/test_query.py
python3 scripts/query.py "CKD 的核心机制主线是什么？" --backend openrouter
python3 scripts/query.py "What endpoints are most usable for feline CKD efficacy evaluation?" --backend openrouter
```

如果 CLI 都不稳，先别测 Streamlit。

如果你不想手工跑 8 次，直接用：

```bash
python3 scripts/run_acceptance_checklist.py --template-only
python3 scripts/run_acceptance_checklist.py --backend openrouter
```

再用：

```bash
python3 -m streamlit run scripts/app.py
```

手工输入同样的问题，检查答案面、badge、sidebar files loaded、write-back。

## Gold Questions

### Q1. CKD mechanism spine

问题：

`CKD 的核心机制主线是什么？`

必须看到：

- 落到 `topics/ckd/mechanism-overview.md` 或同层级强答案面
- 至少 2 个真实 source ids
- 明确区分直接事实和归纳

失败信号：

- 只给泛泛综述
- 没有 source ids
- 只重复 dashboard 语言

### Q2. CKD endpoint selection

问题：

`What endpoints are most usable for feline CKD efficacy evaluation, and why?`

必须看到：

- endpoint shortlist，不只是罗列
- explanation of why
- 最好能触达 `endpoint-handbook` 或 outcome memo

失败信号：

- 把 diagnosis marker 和 efficacy endpoint 混成一层
- 没有 tradeoff

### Q3. CKD claim verification

问题：

`Verify whether SDMA should already be treated as a core early-detection anchor in this vault.`

必须看到：

- answer 明确是 verification 风格
- 引用支持和保留条件同时出现
- 不能把 frontier signal 说成 settled fact

失败信号：

- 只有单边结论
- 完全没有 uncertainty

### Q4. FIP diagnostic workup

问题：

`What is the current diagnostic workup architecture for feline FIP?`

必须看到：

- 落到 FIP workup / recognition 强页
- answer 不是只讲某个 assay
- 至少 1 个 source-backed boundary

失败信号：

- 直接把 diagnosis 等同于 PCR
- 回答只是一段教科书式背景

### Q5. HCM recognition versus endpoint

问题：

`For feline HCM, what should be separated between recognition and endpoints?`

必须看到：

- 承认 recognition 和 endpoint 是两层
- 提到分层边界，而不是一锅炖

失败信号：

- 把 biomarker / imaging / endpoint 全部混写

### Q6. IBD versus lymphoma boundary

问题：

`Where is the current IBD versus small-cell lymphoma boundary in this vault?`

必须看到：

- 指向 IBD boundary memo 或对应 compiled surface
- 能说明这是 boundary question，不是 generic disease summary

失败信号：

- 回答像百科
- 没有边界语言

### Q7. Cross-disease question

问题：

`Compare CKD and HCM on the maturity of their endpoint architecture.`

必须看到：

- 明确说明这是 cross-disease
- 如果当前 retrieval 不稳，要保守降级
- 最好引用 maturity ladder / cross-disease audit

失败信号：

- 假装精确但其实只拼接两页
- 完全不承认跨病种 retrieval 风险

### Q8. Regulatory question

问题：

`What is the current regulatory path surface for feline CKD programs across China, FDA, and VMD?`

必须看到：

- 至少承认 jurisdiction split
- 不把三地监管路径混成一个答案

失败信号：

- 只输出 generic regulatory paragraph
- 没有 jurisdiction boundary

## Write-Back Gate

只有下列 5 条都满足，才允许默认打开 write-back：

1. 输出文件 frontmatter 完整
2. `source_ids` 都能在库里解析到真实文件
3. body 中没有裸结论段落完全无 provenance tag
4. 文件名 slug 稳定且不会重复覆盖重要结果
5. answer 值得保留，不是一次性问答噪音

否则：

`write-back 继续保持默认关闭`

## Scorecard

每次验收都记这 5 个分：

| Dimension | Pass Rule |
|---|---|
| Routing accuracy | disease + answer surface 基本正确 |
| Evidence hygiene | source ids 真实，tag 使用克制 |
| Answer compression | 先给最短答案，不先铺背景 |
| Cross-disease honesty | 不会在不稳时装作很稳 |
| Write-back safety | 不把低质量回答直接写回库 |

## What To Do Next

如果 8 题里有 3 题以上失败，下一步不要补 UI。

先补：

1. best-answer surface
2. unified retrieval layer
3. write-back gate discipline

如果 8 题里至少 6 题通过，再考虑：

1. 更顺手的 Streamlit UX
2. 更好的 cross-disease retrieval
3. 更可见的 stale-refresh / thickening 提示
