---
id: ask-the-vault
type: index
topic: system
question_type: query
language: bilingual
last_compiled_at: 2026-05-17
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: active
---

# Ask The Vault

这页不是按文件夹组织的。

这页是按问题组织的。

If you want the Karpathy-style feeling of "ask first, then enter the knowledge base," start here.

If you are a brand-new reader and do not yet know what kind of question you have, go back to:

- [reader start here](reader-start-here.md)

If you want a cross-disease router first, use:

- [question router](question-router.md)

If you want one page that maps the strongest answer surface for each disease and question type, use:

- [best answer surfaces](best-answer-surfaces.md)

If you want to understand how a good query can turn into a stronger system asset, use:

- [query to write-back](query-to-writeback.md)

If an answer looks useful but needs domain-expert pressure-testing, use the in-app
`Expert review loop` under the answer. It exports a prompt for manual review and keeps
the result out of source evidence until it is staged and checked.

## Short Rule / 最短规则

不要先想：

- 我该点哪个文件

先想：

- 我现在到底要问什么

这页是二级入口，不是普通读者的唯一前门。

## Fastest Answer Surfaces / 最快答案面

如果你不想先学结构，直接从这些问题进：

- `What is X?` / `什么是X？` / `解释一下X`
  Open the disease `what-is-*` page (plain-language explanation)
- `What is the strongest current overall read for this disease?`
  Open the disease `current-state-dashboard`
- `What is the current best structured overview?`
  Open the disease `synthesis-index`
- `Which claims should I verify back in the papers?`
  Open [verify-a-claim](verify-a-claim.md)
- `How does this query become system write-back if it keeps recurring?`
  Open [query-to-write-back](query-to-writeback.md)
- `Which page is the strongest answer surface for this disease and question type?`
  Open [best-answer-surfaces](best-answer-surfaces.md)

如果你已经知道问题属于哪一层，再往下选。

## 0. I Want A Simple Explanation / 我想要简单解释

Ask:

- `What is feline obesity?` / `什么是猫肥胖？` / `解释一下猫肥胖`
- `What is feline cancer?` / `什么是猫癌症？` / `解释一下猫癌症`
- `What is CKD?` / `什么是猫慢性肾病？` / `解释一下猫肾病`
- `What is FIP?` / `什么是猫传腹？` / `解释一下猫传染性腹膜炎`
- `What is IBD?` / `什么是猫炎症性肠病？` / `解释一下猫IBD`
- `What is diabetes?` / `什么是猫糖尿病？` / `解释一下猫糖尿病`

Open the disease `what-is-*` page for plain-language explanation:

- Obesity: [what-is-obesity](../../topics/obesity/what-is-obesity.md)
- Cancer: [what-is-cancer](../../topics/cancer/what-is-cancer.md)
- CKD: [what-is-ckd](../../topics/ckd/what-is-ckd.md)
- FIP: [what-is-fip](../../topics/fip/what-is-fip.md)
- IBD: (pending — currently use [current-state-dashboard](../../topics/ibd/current-state-dashboard.md))
- HCM: (pending — currently use [current-state-dashboard](../../topics/hcm/current-state-dashboard.md))
- Diabetes: (pending — currently use [current-state-dashboard](../../topics/diabetes/current-state-dashboard.md))
- FCV: (pending — currently use [current-state-dashboard](../../topics/fcv/current-state-dashboard.md))

## 1. I Want The Fastest Disease Read / 我想最快读懂一个病种

Ask:

- `What is the current strongest CKD reading?`
- `What is the current strongest FIP reading?`
- `What is the current strongest IBD reading?`
- `What is the current strongest HCM reading?`
- `What is the current strongest Diabetes reading?`
- `What is the current strongest FCV reading?`
- `What is the current strongest Obesity reading?`
- `What is the current strongest Cancer reading?`

Open:

- CKD: [current-state-dashboard](../../topics/ckd/current-state-dashboard.md)
- FIP: [current-state-dashboard](../../topics/fip/current-state-dashboard.md)
- IBD: [current-state-dashboard](../../topics/ibd/current-state-dashboard.md)
- HCM: [current-state-dashboard](../../topics/hcm/current-state-dashboard.md)
- Diabetes: [current-state-dashboard](../../topics/diabetes/current-state-dashboard.md)
- FCV: [current-state-dashboard](../../topics/fcv/current-state-dashboard.md)
- Obesity: [current-state-dashboard](../../topics/obesity/current-state-dashboard.md)
- Cancer: [current-state-dashboard](../../topics/cancer/current-state-dashboard.md)

## 2. I Want The Current Best Structured Overview / 我想看当前最稳的大图

Ask:

- `What is the current structured reading of this disease area?`

Open:

- CKD: [synthesis-index](../../topics/ckd/synthesis-index.md)
- FIP: [synthesis-index](../../topics/fip/synthesis-index.md)
- IBD: [synthesis-index](../../topics/ibd/synthesis-index.md)
- HCM: [synthesis-index](../../topics/hcm/synthesis-index.md)
- Diabetes: [synthesis-index](../../topics/diabetes/synthesis-index.md)
- Cancer: [synthesis-index](../../topics/cancer/synthesis-index.md)
- FCV: [synthesis-index](../../topics/fcv/synthesis-index.md)
- Obesity: (not yet compiled — use [mechanism-overview](../../topics/obesity/mechanism-overview.md) for architecture)

## 3. I Want A Specific Mechanism Answer / 我想问机制问题

Ask:

- `What is the current mechanism spine?`
- `What is core, and what is still speculative?`

Open:

- CKD: [mechanism-overview](../../topics/ckd/mechanism-overview.md)
- FIP: [mechanism-overview](../../topics/fip/mechanism-overview.md)
- IBD: [mechanism-overview-bilingual](../../topics/ibd/mechanism-overview-bilingual.md)
- HCM: [mechanism-overview](../../topics/hcm/mechanism-overview.md)
- Diabetes: [mechanism-overview](../../topics/diabetes/mechanism-overview.md)
- FCV: [mechanism-overview](../../topics/fcv/mechanism-overview.md)
- Obesity: [mechanism-overview](../../topics/obesity/mechanism-overview.md)

## 4. I Want A Recognition Or Diagnostic Answer / 我想问识别或诊断问题

Ask:

- `What is the current recognition logic?`
- `What is exclusion-first, and what is only support?`

Open:

- CKD: [risk-and-recognition](../../topics/ckd/risk-and-recognition.md)
- FIP: [risk-and-recognition](../../topics/fip/risk-and-recognition.md)
- IBD: [risk-and-recognition-bilingual](../../topics/ibd/risk-and-recognition-bilingual.md)
- HCM: [risk-and-recognition](../../topics/hcm/risk-and-recognition.md)
- Diabetes: [risk-and-recognition](../../topics/diabetes/risk-and-recognition.md)
- FCV: [risk-and-recognition](../../topics/fcv/risk-and-recognition.md)
- Obesity: [risk-and-recognition](../../topics/obesity/risk-and-recognition.md)

## 5. I Want An Endpoint Or Marker Answer / 我想问 endpoint 或 marker

Ask:

- `Which endpoints are operational?`
- `Which markers are support only?`
- `Which markers are frontier, not routine?`

Open:

- CKD: [endpoint-handbook](../../topics/ckd/endpoint-handbook.md)
- FIP: [endpoint-handbook](../../topics/fip/endpoint-handbook.md)
- IBD: [endpoint-handbook-bilingual](../../topics/ibd/endpoint-handbook-bilingual.md)
- HCM: [endpoint-handbook](../../topics/hcm/endpoint-handbook.md)
- Diabetes: [endpoint-handbook](../../topics/diabetes/endpoint-handbook.md)
- FCV: [endpoint-handbook](../../topics/fcv/endpoint-handbook.md)
- Obesity: (not yet compiled — see [diabetes-bridge](../../topics/obesity/diabetes-bridge.md) for insulin mechanism)

## 6. I Want A Treatment Or Translation Answer / 我想问治疗或转化问题

Ask:

- `What can the treatment branch currently defend?`
- `What is practical, and what is still exploratory?`

Open:

- CKD: [translation-brief](../../topics/ckd/translation-brief.md)
- FIP: [translation-brief](../../topics/fip/translation-brief.md)
- IBD: [treatment-evidence-bilingual](../../topics/ibd/treatment-evidence-bilingual.md)
- HCM: [translation-brief](../../topics/hcm/translation-brief.md)
- Diabetes: [translation-brief](../../topics/diabetes/translation-brief.md)
- FCV: [translation-brief](../../topics/fcv/translation-brief.md)
- Obesity: (not yet compiled — see [prevention](../../topics/obesity/prevention.md) for prevention strategy)

## 7. I Want A Regulatory Answer / 我想问监管问题

Ask:

- `How far can the current regulatory reading go?`
- `What is route-fit, and what is still too thin?`

Open:

- CKD: [regulatory-brief](../../topics/ckd/regulatory-brief.md)
- FIP: [regulatory-brief](../../topics/fip/regulatory-brief.md)
- IBD: [regulatory-brief-bilingual](../../topics/ibd/regulatory-brief-bilingual.md)
- HCM: [regulatory-brief](../../topics/hcm/regulatory-brief.md)
- Diabetes: [regulatory-brief](../../topics/diabetes/regulatory-brief.md)
- FCV: [regulatory-brief](../../topics/fcv/regulatory-brief.md)
- Obesity: (not yet compiled)

## 8. I Want To Verify A Claim In The Papers / 我想回原文核对 claim

Ask:

- `Which page should orient me first, and which paper should I verify after that?`

Open:

- [compiled pages vs original papers](compiled-vs-source-reading.md)
- [verify a claim](verify-a-claim.md)
- disease `navigation`
- disease `source index`

## 9. I Want The System To Tell Me What Is Strong, Thin, Or Next / 我想直接知道什么最强、最薄、下一步看哪

Ask:

- `What is already strong in this disease module?`
- `What is still thin?`
- `What should I read or verify next?`

Open:

- CKD: [current-state-dashboard](../../topics/ckd/current-state-dashboard.md)
- FIP: [current-state-dashboard](../../topics/fip/current-state-dashboard.md)
- IBD: [current-state-dashboard](../../topics/ibd/current-state-dashboard.md)
- HCM: [current-state-dashboard](../../topics/hcm/current-state-dashboard.md)
- Diabetes: [current-state-dashboard](../../topics/diabetes/current-state-dashboard.md)
- FCV: [current-state-dashboard](../../topics/fcv/current-state-dashboard.md)
- Obesity: [current-state-dashboard](../../topics/obesity/current-state-dashboard.md)

## Good Query Pattern / 好的提问模式

Bad:

- `Tell me about CKD`

Better:

- `What is the strongest current CKD endpoint conclusion?`
- `What is still thin in FIP diagnosis?`
- `How strong is the IBD treatment branch right now?`
- `Which IBD claims should I verify in the raw papers?`
- `What is the current HCM phenotype-recognition spine?`
- `What is still thin in the FIP regulatory branch?`
- `What is the best current IBD answer surface for treatment hierarchy?`

## One-Line Summary / 一句话总结

The right front door is no longer "pick a file." It is "ask a bounded question, then open the strongest answer surface."
