---
id: system-ask-the-vault-acceptance-report-20260416
type: health-check
topic: operating-system
question_type: acceptance
language: zh
last_compiled_at: 2026-04-16
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: template
---

# Ask The Vault Acceptance Report, 2026-04-16

Execution mode: template-only
Backend: openrouter
Write-back: off

Pass rule reminder:

1. 8 个核心问题里至少 6 个答案可接受
2. 0 个答案出现伪造 source id
3. 0 个答案把明显推断伪装成 `quoted_fact`
4. 至少 4 个答案能把用户直接带到最短答案面
5. `--write-back` 产物 frontmatter 完整且文件名稳定
6. 至少 1 个 cross-disease 问题被明确降级处理，而不是乱猜

## Scoreboard

| ID | Topic | Exit | QType | First Family | Strongest Surface | Clear Miss | Failure Type | Next Fix Layer | Source IDs | Confidence | Initial Read |
|---|---|---:|---|---|---|---|---|---|---:|---|---|
| Q1 | CKD mechanism spine | — | mechanism | mechanism-overview | pending | pending | pending | pending | — | — | pending |
| Q2 | CKD endpoint selection | — | endpoints | endpoint-handbook | pending | pending | pending | pending | — | — | pending |
| Q3 | CKD claim verification | — | claim_verification | verify-a-claim | pending | pending | pending | pending | — | — | pending |
| Q4 | FIP diagnostic workup | — | recognition | risk-and-recognition | pending | pending | pending | pending | — | — | pending |
| Q5 | HCM recognition versus endpoint | — | recognition | risk-and-recognition | pending | pending | pending | pending | — | — | pending |
| Q6 | IBD versus lymphoma boundary | — | recognition | risk-and-recognition | pending | pending | pending | pending | — | — | pending |
| Q7 | Cross-disease question | — | synthesis | disease-module-maturity-ladder | pending | pending | pending | pending | — | — | pending |
| Q8 | Regulatory question | — | regulatory | regulatory-brief | pending | pending | pending | pending | — | — | pending |

## Detailed Runs

## Q1. CKD mechanism spine

Question: `CKD 的核心机制主线是什么？`

Must see: 至少落到 CKD mechanism 强答案面，且至少 2 个真实 source ids。
Expected question_type: `mechanism`
Expected primary family: `mechanism-overview`
Expected strongest surface: `topics/ckd/mechanism-overview.md`

Status: pending

Routing read:

- router question_type: pending
- first family: pending
- strongest surface hit: pending
- clear miss: pending
- failure type: pending
- next fix layer: pending

Result excerpt:

_Not executed yet._

## Q2. CKD endpoint selection

Question: `What endpoints are most usable for feline CKD efficacy evaluation, and why?`

Must see: 有 endpoint shortlist 和 why，不只是罗列。
Expected question_type: `endpoints`
Expected primary family: `endpoint-handbook`
Expected strongest surface: `topics/ckd/endpoint-handbook.md`

Status: pending

Routing read:

- router question_type: pending
- first family: pending
- strongest surface hit: pending
- clear miss: pending
- failure type: pending
- next fix layer: pending

Result excerpt:

_Not executed yet._

## Q3. CKD claim verification

Question: `Verify whether SDMA should already be treated as a core early-detection anchor in this vault.`

Must see: 必须是 verification 风格，同时呈现支持与保留条件。
Expected question_type: `claim_verification`
Expected primary family: `verify-a-claim`
Expected strongest surface: `system/indexes/verify-a-claim.md`

Status: pending

Routing read:

- router question_type: pending
- first family: pending
- strongest surface hit: pending
- clear miss: pending
- failure type: pending
- next fix layer: pending

Result excerpt:

_Not executed yet._

## Q4. FIP diagnostic workup

Question: `What is the current diagnostic workup architecture for feline FIP?`

Must see: 不能把 diagnosis 简化成单一 assay。
Expected question_type: `recognition`
Expected primary family: `risk-and-recognition`
Expected strongest surface: `topics/fip/risk-and-recognition.md`

Status: pending

Routing read:

- router question_type: pending
- first family: pending
- strongest surface hit: pending
- clear miss: pending
- failure type: pending
- next fix layer: pending

Result excerpt:

_Not executed yet._

## Q5. HCM recognition versus endpoint

Question: `For feline HCM, what should be separated between recognition and endpoints?`

Must see: 承认 recognition 和 endpoint 是两层。
Expected question_type: `recognition`
Expected primary family: `risk-and-recognition`
Expected strongest surface: `topics/hcm/risk-and-recognition.md`

Status: pending

Routing read:

- router question_type: pending
- first family: pending
- strongest surface hit: pending
- clear miss: pending
- failure type: pending
- next fix layer: pending

Result excerpt:

_Not executed yet._

## Q6. IBD versus lymphoma boundary

Question: `Where is the current IBD versus small-cell lymphoma boundary in this vault?`

Must see: 应该像 boundary answer，不应像 generic disease summary。
Expected question_type: `recognition`
Expected primary family: `risk-and-recognition`
Expected strongest surface: `topics/ibd/risk-and-recognition.md`

Status: pending

Routing read:

- router question_type: pending
- first family: pending
- strongest surface hit: pending
- clear miss: pending
- failure type: pending
- next fix layer: pending

Result excerpt:

_Not executed yet._

## Q7. Cross-disease question

Question: `Compare CKD and HCM on the maturity of their endpoint architecture.`

Must see: 要么稳妥回答，要么诚实降级，不能假精确。
Expected question_type: `synthesis`
Expected primary family: `disease-module-maturity-ladder`
Expected strongest surface: `system/indexes/disease-module-maturity-ladder.md`

Status: pending

Routing read:

- router question_type: pending
- first family: pending
- strongest surface hit: pending
- clear miss: pending
- failure type: pending
- next fix layer: pending

Result excerpt:

_Not executed yet._

## Q8. Regulatory question

Question: `What is the current regulatory path surface for feline CKD programs across China, FDA, and VMD?`

Must see: 至少承认 jurisdiction split。
Expected question_type: `regulatory`
Expected primary family: `regulatory-brief`
Expected strongest surface: `topics/ckd/regulatory-brief.md`

Status: pending

Routing read:

- router question_type: pending
- first family: pending
- strongest surface hit: pending
- clear miss: pending
- failure type: pending
- next fix layer: pending

Result excerpt:

_Not executed yet._
