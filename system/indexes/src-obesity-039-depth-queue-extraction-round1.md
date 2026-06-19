---
id: src-obesity-039-depth-queue-extraction-round1
type: system
topic: content-pipeline
question_type: depth-queue-extraction
source_ids: [src-obesity-039]
language: zh
last_compiled_at: 2026-06-19
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-obesity-039 深度队列提取，Round 1

## 证据边界

本 worksheet 仅使用 Crossref 和可用摘要文本。它不是全文 deep extraction。人工审阅后，它可以支持 source card 更新，但不能直接晋升为读者可见的临床结论。

## 来源元数据

| Field | Value |
|---|---|
| Source | `src-obesity-039` |
| Title | Prevalence and factors associated with overweight and obesity in cats in veterinary hospitals in France during the COVID-19 pandemic |
| DOI | `10.1177/1098612x241305924` |
| Provider | Crossref |
| Container | Journal of Feline Medicine and Surgery |
| Year | 2025 |
| Current card status | `abstract_weighted` |
| Source family | original study |
| Detected sections | methods, results, conclusions |
| Detected endpoint/theme signals | weight, body condition, obesity, overweight, activity, prevention |

## 为什么值得读

值得优先打开，因为它可支撑猫肥胖的流行率和风险因素框架；但必须先看清采样框、BCS 方法和疫情期间就诊选择偏倚。

## 方法 / 样本线索

样本/设计线索：274 只猫；原始研究。 摘要原句线索：Objectives The present study aimed to determine the evolution of the percentage of overweight and obese cats during the COVID-19 pandemic in France, and to identify factors associated with excess weight to inform the development of targete...

## 主要结果线索

结果线索：该研究提供猫超重/肥胖的流行率或相关因素信息；应重点核对采样框、BCS 阈值、生活方式变量和偏倚来源。

## 临床相关性线索

潜在临床意义：用于肥胖预防、筛查和风险因素沟通。边界：流行率估计高度依赖采样框和体况评分方法。

## 摘要原文片段（用于审计，不直接面向读者）

> Objectives The present study aimed to determine the evolution of the percentage of overweight and obese cats during the COVID-19 pandemic in France, and to identify factors associated with excess weight to inform the development of targeted prevention strategies. Methods Cat owners visiting the veterinary hospitals of Maisons-Alfort and Toulouse b...

## 目前不能晋升的内容

- 数字化临床建议
- 指南式推荐
- 面向主人的确定性承诺
- 未确认研究设计前写成强疗效结论
- 全文方法和结果细节尚未核对

## Source Card 修改建议

- 在人工审阅前，卡片最多保持 `abstract_weighted`，不要直接升为 deep_extracted。
- 候选端点/主题标签：weight, body condition, obesity, overweight, activity, prevention。
- 只有在完整摘要或全文核对后，才添加有边界的 `quoted_fact` 和 `source_supported_conclusion`。

## 下一步提取动作

- 人工审阅者应阅读完整摘要；若可访问，再读全文。
- 如果该来源控制一个证据分支，再用明确的 `quoted_fact`、`source_supported_conclusion` 和 `llm_inference` 更新 source card。
- 如果只能获得摘要级证据，保持 `decision_grade: no`。
