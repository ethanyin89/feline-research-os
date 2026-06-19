---
id: src-diabetes-035-depth-queue-extraction-round1
type: system
topic: content-pipeline
question_type: depth-queue-extraction
source_ids: [src-diabetes-035]
language: zh
last_compiled_at: 2026-06-19
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-diabetes-035 深度队列提取，Round 1

## 证据边界

本 worksheet 仅使用 Crossref 和可用摘要文本。它不是全文 deep extraction。人工审阅后，它可以支持 source card 更新，但不能直接晋升为读者可见的临床结论。

## 来源元数据

| Field | Value |
|---|---|
| Source | `src-diabetes-035` |
| Title | Velagliflozin, a once-daily, liquid, oral SGLT2 inhibitor, is effective as a stand-alone therapy for feline diabetes mellitus: the SENSATION study |
| DOI | `10.2460/javma.24.03.0174` |
| Provider | Crossref |
| Container | Journal of the American Veterinary Medical Association |
| Year | 2024 |
| Current card status | `abstract_weighted` |
| Source family | original study |
| Detected sections | objective, animals, procedures, results, clinical relevance |
| Detected endpoint/theme signals | insulin, glucose, safety, effectiveness |

## 为什么值得读

值得优先打开，因为它直接关系到猫糖尿病口服 SGLT2 抑制剂单药治疗路径，可能改变治疗选择、监测和排除标准的表达。

## 方法 / 样本线索

样本/设计线索：252 只客户饲养猫；158 只猫；35 只猫；18 只猫；前瞻性研究。 摘要原句线索：Abstract OBJECTIVE To investigate safety and effectiveness of velagliflozin oral solution as sole therapy in naïve and previously insulin-treated diabetic cats. ANIMALS 252 client-owned cats receiving ≥ 2 doses of velagliflozin; 214 (85%)...

## 主要结果线索

结果线索：该研究测试口服 SGLT2 抑制剂作为猫糖尿病单药治疗的有效性和安全性；需要重点核对排除标准、酮症风险和监测要求。

## 临床相关性线索

潜在临床意义：用于猫糖尿病治疗路径选择。边界：安全排除条件和监测标准与降糖效果同等重要。

## 摘要原文片段（用于审计，不直接面向读者）

> Abstract OBJECTIVE To investigate safety and effectiveness of velagliflozin oral solution as sole therapy in naïve and previously insulin-treated diabetic cats. ANIMALS 252 client-owned cats receiving ≥ 2 doses of velagliflozin; 214 (85%) naïve diabetics and 38 (15%) insulin-treated diabetics. PROCEDURES Prospective, baseline-controlled, open-labe...

## 目前不能晋升的内容

- 数字化临床建议
- 指南式推荐
- 面向主人的确定性承诺
- 全文方法和结果细节尚未核对

## Source Card 修改建议

- 在人工审阅前，卡片最多保持 `abstract_weighted`，不要直接升为 deep_extracted。
- 候选端点/主题标签：insulin, glucose, safety, effectiveness。
- 只有在完整摘要或全文核对后，才添加有边界的 `quoted_fact` 和 `source_supported_conclusion`。

## 下一步提取动作

- 人工审阅者应阅读完整摘要；若可访问，再读全文。
- 如果该来源控制一个证据分支，再用明确的 `quoted_fact`、`source_supported_conclusion` 和 `llm_inference` 更新 source card。
- 如果只能获得摘要级证据，保持 `decision_grade: no`。
