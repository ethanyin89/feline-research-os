---
id: system-ordinary-user-acceptance-report-20260507
type: health-check
topic: operating-system
question_type: acceptance
language: zh
last_compiled_at: 2026-05-07
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: route_pass
---

# Ordinary User Acceptance Report, 2026-05-07

Suite: ordinary-user
Execution mode: route-only
Backend: anthropic
Write-back: off
Acceptance status: route_pass

Pass rule reminder:

1. 6 个普通用户问题里至少 5 个答案可接受
2. 每个通过答案都要有真实 source ids
3. overview 问题要落到 current-state-dashboard 起步面
4. recognition / endpoints 问题不能被误判成 generic overview
5. answer 要能被普通读者扫读，并给出 next step

## Scoreboard

| ID | Topic | Exit | QType | First Family | Strongest Surface | Clear Miss | Failure Type | Next Fix Layer | Source IDs | Confidence | Initial Read |
|---|---|---:|---|---|---|---|---|---|---:|---|---|
| OU1 | CKD overview | 0 | overview | current-state-dashboard | yes | no | no-clear-failure | none | 33 | route-only | route-pass |
| OU2 | FIP recognition | 0 | recognition | risk-and-recognition | yes | no | no-clear-failure | none | 9 | route-only | route-pass |
| OU3 | HCM overview and risk | 0 | overview | current-state-dashboard | yes | no | no-clear-failure | none | 24 | route-only | route-pass |
| OU4 | IBD versus lymphoma boundary | 0 | recognition | risk-and-recognition | yes | no | no-clear-failure | none | 9 | route-only | route-pass |
| OU5 | Diabetes remission | 0 | endpoints | endpoint-handbook | yes | no | no-clear-failure | none | 11 | route-only | route-pass |
| OU6 | Elevated creatinine worry | 0 | overview | current-state-dashboard | yes | no | no-clear-failure | none | 33 | route-only | route-pass |

Acceptance summary: 6/6 route checks; 0 execution failures; 0 provenance misses; 0 route misses. Status: route_pass. Route-only checks routing and source-surface availability; it does not judge final answer quality.

## Detailed Runs

## OU1. CKD overview

Question: `解释CKD`

Must see: 普通用户能看懂的 CKD starter answer，证据和 next step 可见。
Expected question_type: `overview`
Expected primary family: `current-state-dashboard`
Expected strongest surface: `topics/ckd/current-state-dashboard.md`

Exit code: `0`
Confidence: `route-only`
Source IDs found: `src-ckd-001, src-ckd-002, src-ckd-003, src-ckd-004, src-ckd-005, src-ckd-006, src-ckd-007, src-ckd-008, src-ckd-009, src-ckd-010, src-ckd-011, src-ckd-012, src-ckd-013, src-ckd-014, src-ckd-015, src-ckd-016, src-ckd-017, src-ckd-018, src-ckd-019, src-ckd-020, src-ckd-021, src-ckd-022, src-ckd-023, src-ckd-024, src-reg-001, src-reg-002, src-reg-003, src-reg-004, src-reg-005, src-reg-006, src-reg-007, src-reg-008, src-reg-009`

Routing read:

- router question_type: `overview`
- first family: `current-state-dashboard`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `topics/ckd/current-state-dashboard.md, topics/ckd/synthesis-index.md`

stderr:

```text
[meta] ROUTER_QTYPE=overview
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=current-state-dashboard
[meta] LOADED_PATHS=topics/ckd/current-state-dashboard.md,topics/ckd/synthesis-index.md
```

Result excerpt:

```text
(empty)
```

## OU2. FIP recognition

Question: `FIP怎么识别`

Must see: 识别 / workup 逻辑，不是 generic disease summary。
Expected question_type: `recognition`
Expected primary family: `risk-and-recognition`
Expected strongest surface: `topics/fip/risk-and-recognition.md`

Exit code: `0`
Confidence: `route-only`
Source IDs found: `src-fip-003, src-fip-005, src-fip-006, src-fip-007, src-fip-008, src-fip-012, src-fip-015, src-fip-020, src-fip-023`

Routing read:

- router question_type: `recognition`
- first family: `risk-and-recognition`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `topics/fip/risk-and-recognition.md`

stderr:

```text
[meta] ROUTER_QTYPE=recognition
[meta] ROUTER_DISEASE=fip
[meta] FIRST_FAMILY=risk-and-recognition
[meta] LOADED_PATHS=topics/fip/risk-and-recognition.md
```

Result excerpt:

```text
(empty)
```

## OU3. HCM overview and risk

Question: `HCM是什么，为什么危险`

Must see: 解释为什么危险，而不是只给病名定义。
Expected question_type: `overview`
Expected primary family: `current-state-dashboard`
Expected strongest surface: `topics/hcm/current-state-dashboard.md`

Exit code: `0`
Confidence: `route-only`
Source IDs found: `src-hcm-001, src-hcm-002, src-hcm-003, src-hcm-004, src-hcm-005, src-hcm-006, src-hcm-007, src-hcm-008, src-hcm-009, src-hcm-010, src-hcm-011, src-hcm-012, src-hcm-013, src-hcm-014, src-hcm-015, src-hcm-016, src-hcm-017, src-hcm-018, src-hcm-019, src-hcm-020, src-hcm-021, src-hcm-022, src-hcm-023, src-hcm-024`

Routing read:

- router question_type: `overview`
- first family: `current-state-dashboard`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `topics/hcm/current-state-dashboard.md, topics/hcm/synthesis-index.md`

stderr:

```text
[meta] ROUTER_QTYPE=overview
[meta] ROUTER_DISEASE=hcm
[meta] FIRST_FAMILY=current-state-dashboard
[meta] LOADED_PATHS=topics/hcm/current-state-dashboard.md,topics/hcm/synthesis-index.md
```

Result excerpt:

```text
(empty)
```

## OU4. IBD versus lymphoma boundary

Question: `IBD和淋巴瘤怎么区分`

Must see: boundary answer，不是百科式概览。
Expected question_type: `recognition`
Expected primary family: `risk-and-recognition`
Expected strongest surface: `topics/ibd/risk-and-recognition.md`

Exit code: `0`
Confidence: `route-only`
Source IDs found: `src-ibd-003, src-ibd-004, src-ibd-009, src-ibd-010, src-ibd-015, src-ibd-016, src-ibd-017, src-ibd-019, src-ibd-024`

Routing read:

- router question_type: `recognition`
- first family: `risk-and-recognition`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `topics/ibd/risk-and-recognition.md`

stderr:

```text
[meta] ROUTER_QTYPE=recognition
[meta] ROUTER_DISEASE=ibd
[meta] FIRST_FAMILY=risk-and-recognition
[meta] LOADED_PATHS=topics/ibd/risk-and-recognition.md
```

Result excerpt:

```text
(empty)
```

## OU5. Diabetes remission

Question: `糖尿病猫为什么会缓解`

Must see: 解释缓解不是治愈，并落到结果 / 缓解解释面。
Expected question_type: `endpoints`
Expected primary family: `endpoint-handbook`
Expected strongest surface: `topics/diabetes/endpoint-handbook.md`

Exit code: `0`
Confidence: `route-only`
Source IDs found: `src-diabetes-004, src-diabetes-005, src-diabetes-006, src-diabetes-007, src-diabetes-008, src-diabetes-011, src-diabetes-015, src-diabetes-016, src-diabetes-018, src-diabetes-022, src-diabetes-024`

Routing read:

- router question_type: `endpoints`
- first family: `endpoint-handbook`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `topics/diabetes/endpoint-handbook.md, topics/diabetes/remission-boundaries.md, topics/diabetes/complications-neuropathy.md`

stderr:

```text
[meta] ROUTER_QTYPE=endpoints
[meta] ROUTER_DISEASE=diabetes
[meta] FIRST_FAMILY=endpoint-handbook
[meta] LOADED_PATHS=topics/diabetes/endpoint-handbook.md,topics/diabetes/remission-boundaries.md,topics/diabetes/complications-neuropathy.md
```

Result excerpt:

```text
(empty)
```

## OU6. Elevated creatinine worry

Question: `我的猫肌酐升高，这个库能告诉我什么`

Must see: 直接面向读者解释风险，并给出下一步页面。
Expected question_type: `overview`
Expected primary family: `current-state-dashboard`
Expected strongest surface: `topics/ckd/current-state-dashboard.md`

Exit code: `0`
Confidence: `route-only`
Source IDs found: `src-ckd-001, src-ckd-002, src-ckd-003, src-ckd-004, src-ckd-005, src-ckd-006, src-ckd-007, src-ckd-008, src-ckd-009, src-ckd-010, src-ckd-011, src-ckd-012, src-ckd-013, src-ckd-014, src-ckd-015, src-ckd-016, src-ckd-017, src-ckd-018, src-ckd-019, src-ckd-020, src-ckd-021, src-ckd-022, src-ckd-023, src-ckd-024, src-reg-001, src-reg-002, src-reg-003, src-reg-004, src-reg-005, src-reg-006, src-reg-007, src-reg-008, src-reg-009`

Routing read:

- router question_type: `overview`
- first family: `current-state-dashboard`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `topics/ckd/current-state-dashboard.md, topics/ckd/synthesis-index.md`

stderr:

```text
[meta] ROUTER_QTYPE=overview
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=current-state-dashboard
[meta] LOADED_PATHS=topics/ckd/current-state-dashboard.md,topics/ckd/synthesis-index.md
```

Result excerpt:

```text
(empty)
```
