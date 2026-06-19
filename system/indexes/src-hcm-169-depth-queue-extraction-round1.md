---
id: src-hcm-169-depth-queue-extraction-round1
type: system
topic: content-pipeline
question_type: depth-queue-extraction
source_ids: [src-hcm-169]
language: zh
last_compiled_at: 2026-06-19
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-hcm-169 深度队列提取，Round 1

## 证据边界

本 worksheet 仅使用 Crossref 和可用摘要文本。它不是全文 deep extraction。人工审阅后，它可以支持 source card 更新，但不能直接晋升为读者可见的临床结论。

## 来源元数据

| Field | Value |
|---|---|
| Source | `src-hcm-169` |
| Title | Assessment of longitudinal systolic function using tissue motion annular displacement in cats with hypertrophic cardiomyopathy: a prospective case-control study |
| DOI | `10.1177/1098612x251320240` |
| Provider | Crossref |
| Container | Journal of Feline Medicine and Surgery |
| Year | 2025 |
| Current card status | `title_only` |
| Source family | original study |
| Detected sections | aim, methods, results, conclusions |
| Detected endpoint/theme signals | none mechanically detected |

## 为什么值得读

值得优先打开，因为它检验新的超声心动图功能测量是否能补充 HCM 的壁厚表型标签，可能影响随访和功能评估。

## 方法 / 样本线索

样本/设计线索：26 只对照猫；21 只 HCM 猫；前瞻性研究。 摘要原句线索：Objectives The aim of this study was to investigate left ventricular (LV) longitudinal systolic function in cats with hypertrophic cardiomyopathy (HCM) and healthy control cats using tissue motion annular displacement (TMAD). Methods The s...

## 主要结果线索

结果线索：研究关注 HCM 猫的纵向收缩功能评估；需要进一步核对该指标与传统超声参数、疾病严重度或结局之间的关系。

## 临床相关性线索

潜在临床意义：用于心脏病表型和随访评估。边界：功能测量需要重复性和结局关联，才能影响常规决策。

## 摘要原文片段（用于审计，不直接面向读者）

> Objectives The aim of this study was to investigate left ventricular (LV) longitudinal systolic function in cats with hypertrophic cardiomyopathy (HCM) and healthy control cats using tissue motion annular displacement (TMAD). Methods The study included 26 control cats and 21 HCM cats. All cats underwent assessment using two-dimensional echocardiog...

## 目前不能晋升的内容

- 数字化临床建议
- 指南式推荐
- 面向主人的确定性承诺
- 全文方法和结果细节尚未核对

## Source Card 修改建议

- 在人工审阅前，卡片最多保持 `abstract_weighted`，不要直接升为 deep_extracted。
- 候选端点/主题标签：needs human endpoint assignment。
- 只有在完整摘要或全文核对后，才添加有边界的 `quoted_fact` 和 `source_supported_conclusion`。

## 下一步提取动作

- 人工审阅者应阅读完整摘要；若可访问，再读全文。
- 如果该来源控制一个证据分支，再用明确的 `quoted_fact`、`source_supported_conclusion` 和 `llm_inference` 更新 source card。
- 如果只能获得摘要级证据，保持 `decision_grade: no`。
