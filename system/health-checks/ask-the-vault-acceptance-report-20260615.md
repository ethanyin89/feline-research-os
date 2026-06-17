---
id: system-ask-the-vault-acceptance-report-20260615
type: health-check
topic: operating-system
question_type: acceptance
language: zh
last_compiled_at: 2026-06-15
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: route_pass
---

# Ask The Vault Acceptance Report, 2026-06-15

Suite: research
Execution mode: route-only
Backend: anthropic
Write-back: off
Acceptance status: route_pass

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
| Q1 | CKD mechanism spine | 0 | mechanism | mechanism-overview | yes | no | no-clear-failure | none | 29 | route-only | route-pass |
| Q2 | CKD endpoint selection | 0 | endpoints | endpoint-handbook | yes | no | no-clear-failure | none | 13 | route-only | route-pass |
| Q3 | CKD claim verification | 0 | claim_verification | verify-a-claim | yes | no | no-clear-failure | none | 24 | route-only | route-pass |
| Q4 | FIP diagnostic workup | 0 | recognition | risk-and-recognition | yes | no | no-clear-failure | none | 9 | route-only | route-pass |
| Q5 | HCM recognition versus endpoint | 0 | recognition | risk-and-recognition | yes | no | no-clear-failure | none | 10 | route-only | route-pass |
| Q6 | IBD versus lymphoma boundary | 0 | recognition | risk-and-recognition | yes | no | no-clear-failure | none | 9 | route-only | route-pass |
| Q7 | Cross-disease question | 0 | synthesis | disease-module-maturity-ladder | yes | no | provenance-miss | provenance | 0 | route-only | route-pass |
| Q8 | Regulatory question | 0 | regulatory | regulatory-brief | yes | no | no-clear-failure | none | 9 | route-only | route-pass |

Acceptance summary: 8/8 route checks; 0 execution failures; 1 provenance misses; 0 route misses. Status: route_pass. Route-only checks routing and source-surface availability; it does not judge final answer quality.

## Detailed Runs

## Q1. CKD mechanism spine

Question: `CKD 的核心机制主线是什么？`

Must see: 至少落到 CKD mechanism 强答案面，且至少 2 个真实 source ids。
Expected question_type: `mechanism`
Expected primary family: `mechanism-overview`
Expected strongest surface: `topics/ckd/mechanism-overview.md`

Exit code: `0`
Confidence: `route-only`
Source IDs found: `src-ckd-001, src-ckd-002, src-ckd-004, src-ckd-006, src-ckd-009, src-ckd-010, src-ckd-011, src-ckd-015, src-ckd-016, src-ckd-021, src-ckd-022, src-ckd-023, src-ckd-026, src-ckd-027, src-ckd-029, src-ckd-030, src-ckd-037, src-ckd-038, src-ckd-050, src-ckd-051, src-ckd-053, src-ckd-054, src-ckd-058, src-ckd-061, src-ckd-087, src-ckd-098, src-ckd-101, src-ckd-121, src-ckd-162`

Routing read:

- router question_type: `mechanism`
- first family: `mechanism-overview`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `topics/ckd/mechanism-overview.md`

stderr:

```text
[meta] ROUTER_QTYPE=mechanism
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=mechanism-overview
[meta] LOADED_PATHS=topics/ckd/mechanism-overview.md
```

Result excerpt:

```text
(empty)
```

## Q2. CKD endpoint selection

Question: `What endpoints are most usable for feline CKD efficacy evaluation, and why?`

Must see: 有 endpoint shortlist 和 why，不只是罗列。
Expected question_type: `endpoints`
Expected primary family: `endpoint-handbook`
Expected strongest surface: `topics/ckd/endpoint-handbook.md`

Exit code: `0`
Confidence: `route-only`
Source IDs found: `src-ckd-001, src-ckd-002, src-ckd-003, src-ckd-004, src-ckd-006, src-ckd-007, src-ckd-010, src-ckd-013, src-ckd-015, src-ckd-017, src-ckd-018, src-ckd-020, src-ckd-024`

Routing read:

- router question_type: `endpoints`
- first family: `endpoint-handbook`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `topics/ckd/endpoint-handbook.md`

stderr:

```text
[meta] ROUTER_QTYPE=endpoints
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=endpoint-handbook
[meta] LOADED_PATHS=topics/ckd/endpoint-handbook.md
```

Result excerpt:

```text
(empty)
```

## Q3. CKD claim verification

Question: `Verify whether SDMA should already be treated as a core early-detection anchor in this vault.`

Must see: 必须是 verification 风格，同时呈现支持与保留条件。
Expected question_type: `claim_verification`
Expected primary family: `verify-a-claim`
Expected strongest surface: `system/indexes/verify-a-claim.md`

Exit code: `0`
Confidence: `route-only`
Source IDs found: `src-ckd-001, src-ckd-002, src-ckd-003, src-ckd-004, src-ckd-005, src-ckd-006, src-ckd-007, src-ckd-008, src-ckd-009, src-ckd-010, src-ckd-011, src-ckd-012, src-ckd-013, src-ckd-014, src-ckd-015, src-ckd-016, src-ckd-017, src-ckd-018, src-ckd-019, src-ckd-020, src-ckd-021, src-ckd-022, src-ckd-023, src-ckd-024`

Routing read:

- router question_type: `claim_verification`
- first family: `verify-a-claim`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `system/indexes/verify-a-claim.md, topics/ckd/current-state-dashboard.md`

stderr:

```text
[meta] ROUTER_QTYPE=claim_verification
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=verify-a-claim
[meta] LOADED_PATHS=system/indexes/verify-a-claim.md,topics/ckd/current-state-dashboard.md
```

Result excerpt:

```text
(empty)
```

## Q4. FIP diagnostic workup

Question: `What is the current diagnostic workup architecture for feline FIP?`

Must see: 不能把 diagnosis 简化成单一 assay。
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

## Q5. HCM recognition versus endpoint

Question: `For feline HCM, what should be separated between recognition and endpoints?`

Must see: 承认 recognition 和 endpoint 是两层。
Expected question_type: `recognition`
Expected primary family: `risk-and-recognition`
Expected strongest surface: `topics/hcm/risk-and-recognition.md`

Exit code: `0`
Confidence: `route-only`
Source IDs found: `src-hcm-001, src-hcm-002, src-hcm-008, src-hcm-009, src-hcm-010, src-hcm-012, src-hcm-013, src-hcm-021, src-hcm-023, src-hcm-024`

Routing read:

- router question_type: `recognition`
- first family: `risk-and-recognition`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `topics/hcm/risk-and-recognition.md`

stderr:

```text
[meta] ROUTER_QTYPE=recognition
[meta] ROUTER_DISEASE=hcm
[meta] FIRST_FAMILY=risk-and-recognition
[meta] LOADED_PATHS=topics/hcm/risk-and-recognition.md
```

Result excerpt:

```text
(empty)
```

## Q6. IBD versus lymphoma boundary

Question: `Where is the current IBD versus small-cell lymphoma boundary in this vault?`

Must see: 应该像 boundary answer，不应像 generic disease summary。
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

## Q7. Cross-disease question

Question: `Compare CKD and HCM on the maturity of their endpoint architecture.`

Must see: 要么稳妥回答，要么诚实降级，不能假精确。
Expected question_type: `synthesis`
Expected primary family: `disease-module-maturity-ladder`
Expected strongest surface: `system/indexes/disease-module-maturity-ladder.md`

Exit code: `0`
Confidence: `route-only`
Source IDs found: `none`

Routing read:

- router question_type: `synthesis`
- first family: `disease-module-maturity-ladder`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `provenance-miss`
- next fix layer: `provenance`
- loaded paths: `system/indexes/disease-module-maturity-ladder.md, system/indexes/cross-disease-second-wave-narrow-owner-audit.md`

stderr:

```text
[meta] ROUTER_QTYPE=synthesis
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=disease-module-maturity-ladder
[meta] LOADED_PATHS=system/indexes/disease-module-maturity-ladder.md,system/indexes/cross-disease-second-wave-narrow-owner-audit.md
```

Result excerpt:

```text
(empty)
```

## Q8. Regulatory question

Question: `What is the current regulatory path surface for feline CKD programs across China, FDA, and VMD?`

Must see: 至少承认 jurisdiction split。
Expected question_type: `regulatory`
Expected primary family: `regulatory-brief`
Expected strongest surface: `topics/ckd/regulatory-brief.md`

Exit code: `0`
Confidence: `route-only`
Source IDs found: `src-reg-001, src-reg-002, src-reg-003, src-reg-004, src-reg-005, src-reg-006, src-reg-007, src-reg-008, src-reg-009`

Routing read:

- router question_type: `regulatory`
- first family: `regulatory-brief`
- strongest surface hit: `yes`
- clear miss: `no`
- failure type: `no-clear-failure`
- next fix layer: `none`
- loaded paths: `topics/ckd/regulatory-brief.md`

stderr:

```text
[meta] ROUTER_QTYPE=regulatory
[meta] ROUTER_DISEASE=ckd
[meta] FIRST_FAMILY=regulatory-brief
[meta] LOADED_PATHS=topics/ckd/regulatory-brief.md
```

Result excerpt:

```text
(empty)
```
