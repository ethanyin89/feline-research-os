---
id: src-fip-070-depth-queue-extraction-round1
type: system
topic: content-pipeline
question_type: depth-queue-extraction
source_ids: [src-fip-070]
language: zh
last_compiled_at: 2026-06-19
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-fip-070 深度队列提取，Round 1

## 证据边界

本 worksheet 仅使用 Crossref 和可用摘要文本。它不是全文 deep extraction。人工审阅后，它可以支持 source card 更新，但不能直接晋升为读者可见的临床结论。

## 来源元数据

| Field | Value |
|---|---|
| Source | `src-fip-070` |
| Title | Retrospective study and outcome of 307 cats with feline infectious peritonitis treated with legally sourced veterinary compounded preparations of remdesivir and GS-441524 (2020–2022) |
| DOI | `10.1177/1098612x231194460` |
| Provider | Crossref |
| Container | Journal of Feline Medicine and Surgery |
| Year | 2023 |
| Current card status | `title_only` |
| Source family | original study |
| Detected sections | aim, methods, results, conclusions |
| Detected endpoint/theme signals | none mechanically detected |

## 为什么值得读

值得优先打开，因为它是较大规模真实世界 FIP 抗病毒治疗结局来源；若病例定义、剂量、缓解、复发和生存数据清楚，会直接影响治疗证据边界。

## 方法 / 样本线索

样本/设计线索：307 只猫；回顾性研究。 摘要原句线索：The aim of the present study was to describe the treatment of FIP using legally sourced veterinary-prescribed regulated veterinary compounded products containing known amounts of remdesivir (injectable) or GS-441524 (oral tablets). Methods...

## 主要结果线索

结果线索：摘要显示研究纳入 307 只 FIP 猫，并报告治疗反应与初始治疗期末存活相关；但回顾性真实世界数据不能直接等同随机疗效证明。

## 临床相关性线索

潜在临床意义：用于 FIP 抗病毒治疗预期、缓解和复发沟通。边界：回顾性或非对照证据不能当作随机疗效证明。

## 摘要原文片段（用于审计，不直接面向读者）

> Objectives Feline infectious peritonitis (FIP) is a serious disease that arises due to feline coronavirus infection. The nucleoside analogues remdesivir and GS-441524 can be effective in its treatment, but most studies have used unregulated products of unknown composition. The aim of the present study was to describe the treatment of FIP using leg...

## 目前不能晋升的内容

- 数字化临床建议
- 指南式推荐
- 面向主人的确定性承诺
- 从回顾性数据推出因果疗效
- 未确认研究设计前写成强疗效结论
- 全文方法和结果细节尚未核对

## Source Card 修改建议

- 在人工审阅前，卡片最多保持 `abstract_weighted`，不要直接升为 deep_extracted。
- 候选端点/主题标签：needs human endpoint assignment。
- 只有在完整摘要或全文核对后，才添加有边界的 `quoted_fact` 和 `source_supported_conclusion`。

## 下一步提取动作

- 人工审阅者应阅读完整摘要；若可访问，再读全文。
- 如果该来源控制一个证据分支，再用明确的 `quoted_fact`、`source_supported_conclusion` 和 `llm_inference` 更新 source card。
- 如果只能获得摘要级证据，保持 `decision_grade: no`。
