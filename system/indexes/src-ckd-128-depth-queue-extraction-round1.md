---
id: src-ckd-128-depth-queue-extraction-round1
type: system
topic: content-pipeline
question_type: depth-queue-extraction
source_ids: [src-ckd-128]
language: zh
last_compiled_at: 2026-06-19
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# src-ckd-128 深度队列提取，Round 1

## 证据边界

本 worksheet 仅使用 Crossref + PubMed abstract 和可用摘要文本。它不是全文 deep extraction。人工审阅后，它可以支持 source card 更新，但不能直接晋升为读者可见的临床结论。

## 来源元数据

| Field | Value |
|---|---|
| Source | `src-ckd-128` |
| Title | Urinary Fibroblast Growth Factor-23 and Soluble Alpha-Klotho in Cats with Chronic Kidney Disease |
| DOI | `10.1016/j.tvjl.2026.106652` |
| Provider | Crossref + PubMed abstract |
| Container | The Veterinary Journal |
| Year | 2026 |
| Current card status | `title_only` |
| Source family | original study |
| Detected sections | results |
| Detected endpoint/theme signals | biomarker, chronic kidney disease, fibroblast growth factor 23, phosphorus |

## 为什么值得读

值得优先打开，因为它可能把猫 CKD 的证据分支从常规肌酐、磷和分期，推进到 CKD-MBD、FGF23、Klotho 与磷调节轴。

## 方法 / 样本线索

样本/设计线索：13 只健康猫；71 只 CKD 猫；28 只 ACKD 猫；队列研究。 摘要原句线索：This study aimed to evaluate the urinary levels of FGF23 (uFGF23) and soluble α-Klotho (uKL) in cats at various stages of CKD, including acute decompensated chronic kidney disease (ACKD), and to assess their respective relationship with di...

## 主要结果线索

结果线索：尿 FGF23/尿肌酐比值随晚期 CKD 或急性失代偿 CKD 升高；该方向更适合解释 CKD-MBD 或矿物质代谢风险，而不是直接生成诊断阈值。

## 临床相关性线索

潜在临床意义：可帮助解释 CKD 矿物质代谢、FGF23/Klotho 生物标志物和风险分层。边界：除非阈值和验证队列清楚，否则不能写成独立诊断流程。

## 摘要原文片段（用于审计，不直接面向读者）

> Fibroblast growth factor 23 (FGF23) and α-Klotho play crucial roles in the pathogenesis of chronic kidney disease-mineral and bone disorder (CKD-MBD) due to their regulatory effects on phosphorus, calcium, parathyroid hormone, and calcitriol levels. Despite their importance, few studies have examined urinary concentrations of these compounds in fe...

## 目前不能晋升的内容

- 数字化临床建议
- 指南式推荐
- 面向主人的确定性承诺
- 未确认研究设计前写成强疗效结论
- 全文方法和结果细节尚未核对

## Source Card 修改建议

- 在人工审阅前，卡片最多保持 `abstract_weighted`，不要直接升为 deep_extracted。
- 候选端点/主题标签：biomarker, chronic kidney disease, fibroblast growth factor 23, phosphorus。
- 只有在完整摘要或全文核对后，才添加有边界的 `quoted_fact` 和 `source_supported_conclusion`。

## 下一步提取动作

- 人工审阅者应阅读完整摘要；若可访问，再读全文。
- 如果该来源控制一个证据分支，再用明确的 `quoted_fact`、`source_supported_conclusion` 和 `llm_inference` 更新 source card。
- 如果只能获得摘要级证据，保持 `decision_grade: no`。
