---
id: system-health-report-20260623
type: health-check
topic: operating-system
question_type: health
language: bilingual
last_compiled_at: 2026-06-23
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Vault Health Report, 2026-06-23

This report aggregates existing checks. It does not call an LLM and does not replace human review.

## Summary

| Check | Status | Read |
|---|---|---|
| Markdown links | PASS | PASS: checked 2624 markdown files, no local link issues found. |
| Query tests | PASS | 113 passed  \|  0 failed  \|  113 total |
| Ordinary-user vault eval | PASS | All ordinary-user free-mode samples passed without API calls. |
| Research Case integrity | PASS | 1/1 valid; 0 issues |
| Paper source cards | PASS | 1414 strict disease paper cards; baseline >= 246 |
| Regulation source cards | PASS | 14 regulation cards |
| Source IDs | PASS | 0 duplicates, 0 missing ids |
| Low-word paper cards | PASS | 0 cards below 700 words |
| Source schema fields | PASS | 0 cards missing required fields, 0 invalid field values |
| Source state consistency | PASS | 0 title-only depth/status conflicts |
| Source link proof | PASS | 0 source cards without DOI or URL |
| Source evidence policy | PASS | 0 source cards with empty evidence_policy |
| Source quoted-fact discipline | PASS | 0 quoted_fact items look interpretive |
| Compiled source refs | PASS | 0 invalid source refs |
| Reader page source_ids | PASS | 0 missing, 0 empty |
| Thin source usage | WARN | 31 reader/high-visibility pages use abstract-weighted or title-only sources |
| Thin source caveats | PASS | 0 thin-source pages without visible evidence-depth caveat |
| Title-only caveats | PASS | 0 pages cite title-only sources without visible caveat |
| Key-claim traceability | PASS | 0 high-value pages missing traceability table |
| Quantified claim traceability | PASS | 0 quantified reader pages missing traceability table |
| Reader quoted-fact discipline | PASS | 0 reader quoted_fact items look interpretive |
| High-visibility language QA | PASS | 0 high-visibility pages unchecked or missing |
| Obesity compiled guidance gate | PASS | 0 obesity reader pages exceed shell/source-indexed status |
| Decision-grade gate | PASS | 0 source-card violations |
| Candidate image gate | PASS | 0 candidate refs remain gated in local_assets frontmatter |
| Inbox backlog | PASS | 0 active files, 1 blocked/held files, 15 rejected audit files |
| Acceptance report | PASS | system/health-checks/ask-the-vault-acceptance-report-20260622.md; mode=executed; status=pass |
| Ordinary-user acceptance | PASS | system/health-checks/ordinary-user-acceptance-report-20260519.md; mode=executed; status=pass |
| Compile trigger | PASS | 39 changed source cards, 158 downstream files |
| API keys | PASS | present: OPENROUTER_API_KEY, OPENAI_API_KEY |
| V2 field quality | PASS | 340 V2 cards: A=91, B=249, C=0, F=0 |

## Source Card Reality

| Disease | Cards | extraction_depth | verification_status |
|---|---:|---|---|
| ckd | 197 | full: 32, partial: 165 | abstract_weighted: 56, deep_extracted: 32, title_only: 109 |
| fip | 242 | full: 30, partial: 212 | abstract_weighted: 22, deep_extracted: 30, title_only: 190 |
| hcm | 226 | full: 29, partial: 197 | abstract_weighted: 3, deep_extracted: 29, title_only: 194 |
| ibd | 126 | full: 24, partial: 102 | abstract_weighted: 1, deep_extracted: 24, title_only: 101 |
| diabetes | 121 | full: 28, partial: 93 | abstract_weighted: 86, deep_extracted: 27, title_only: 8 |
| fcv | 296 | full: 24, partial: 272 | abstract_weighted: 79, deep_extracted: 24, title_only: 193 |
| obesity | 95 | abstract_full: 1, full: 5, partial: 89 | abstract_weighted: 83, deep_extracted: 4, source_checked: 1, title_only: 7 |
| cancer | 111 | abstract: 28, deep: 32, full: 40, partial: 11 | abstract_weighted: 63, deep_extracted: 40, publisher_verified: 1, source_checked: 2, title_only: 5 |

## Image Reality

| Disease | Verified images | Candidate refs | Candidate refs in local_assets |
|---|---:|---:|---:|
| ckd | 8 | 0 | 0 |
| fip | 2 | 0 | 0 |
| hcm | 1 | 0 | 0 |
| ibd | 1 | 0 | 0 |
| diabetes | 1 | 0 | 0 |
| fcv | 0 | 0 | 0 |
| obesity | 0 | 0 | 0 |
| cancer | 6 | 0 | 0 |

## Inbox Backlog

- No active inbox files outside `.gitkeep`.

Blocked / held notes:
- inbox/obesity/content-precision-promotion-batch-20260515.md

Rejected / audit notes:
- inbox/rejected/nested-users-absolute-path-tree-20260421/README.md
- inbox/rejected/nested-users-absolute-path-tree-20260421/Users/jiawei/Desktop/insclaude/feline-research-os/outputs/briefings/out-ckd-briefing-20260408-round1-zh.md
- inbox/rejected/nested-users-absolute-path-tree-20260421/Users/jiawei/Desktop/insclaude/feline-research-os/outputs/briefings/out-ckd-briefing-20260408-round1.md
- inbox/rejected/nested-users-absolute-path-tree-20260421/Users/jiawei/Desktop/insclaude/feline-research-os/outputs/dossiers/out-ibd-dossier-20260409-v1-zh.md
- inbox/rejected/nested-users-absolute-path-tree-20260421/Users/jiawei/Desktop/insclaude/feline-research-os/raw/papers/src-ckd-004.md
- inbox/rejected/nested-users-absolute-path-tree-20260421/Users/jiawei/Desktop/insclaude/feline-research-os/system/indexes/src-ckd-023-deep-extraction-round1.md
- inbox/rejected/nested-users-absolute-path-tree-20260421/Users/jiawei/Desktop/insclaude/feline-research-os/topics/ckd/current-state-dashboard.md
- inbox/rejected/nested-users-absolute-path-tree-20260421/Users/jiawei/Desktop/insclaude/feline-research-os/topics/ckd/index.md
- inbox/rejected/nested-users-absolute-path-tree-20260421/Users/jiawei/Desktop/insclaude/feline-research-os/topics/ckd/mechanism-overview.md
- inbox/rejected/nested-users-absolute-path-tree-20260421/Users/jiawei/Desktop/insclaude/feline-research-os/topics/ckd/model-summary.md
- inbox/rejected/nested-users-absolute-path-tree-20260421/Users/jiawei/Desktop/insclaude/feline-research-os/topics/ckd/navigation.md
- inbox/rejected/processed/ckd-phosphorus-treatment-answer-20260517.md
- inbox/rejected/processed/content-precision-promotion-batch-20260506.md
- inbox/rejected/processed/expert-answer-review-sample-001-20260514.md
- inbox/rejected/processed/fip-gs441524-treatment-answer-20260517.md

## V2 Field Quality

Total cards with V2 fields: 340
Grade distribution: A=91, B=249, C=0, F=0

| Disease | V2 Count | A | B | C | F |
|---|---:|---:|---:|---:|---:|
| ckd | 38 | 17 | 21 | 0 | 0 |
| fip | 33 | 12 | 21 | 0 | 0 |
| hcm | 32 | 18 | 14 | 0 | 0 |
| ibd | 26 | 3 | 23 | 0 | 0 |
| diabetes | 26 | 3 | 23 | 0 | 0 |
| fcv | 58 | 7 | 51 | 0 | 0 |
| obesity | 16 | 5 | 11 | 0 | 0 |
| cancer | 111 | 26 | 85 | 0 | 0 |

## Thin Source Usage

`abstract_weighted` and `title_only` sources can support cautious synthesis, but should not be read as full-text or decision-grade proof.
- topics/cancer/injection-site-sarcoma.md: src-cancer-047 (abstract_weighted)
- topics/cancer/lymphoma.md: src-cancer-065 (abstract_weighted), src-cancer-048 (abstract_weighted), src-cancer-075 (abstract_weighted), src-cancer-029 (abstract_weighted), src-cancer-026 (abstract_weighted), src-cancer-042 (abstract_weighted), src-cancer-044 (abstract_weighted), src-cancer-060 (abstract_weighted), src-cancer-084 (abstract_weighted), src-cancer-086 (abstract_weighted), src-cancer-102 (abstract_weighted)
- topics/cancer/mammary-carcinoma.md: src-cancer-025 (abstract_weighted), src-cancer-028 (abstract_weighted), src-cancer-020 (abstract_weighted), src-cancer-034 (abstract_weighted), src-cancer-041 (abstract_weighted), src-cancer-043 (abstract_weighted), src-cancer-045 (abstract_weighted), src-cancer-050 (abstract_weighted), src-cancer-052 (abstract_weighted), src-cancer-090 (abstract_weighted)
- topics/cancer/oral-squamous-cell-carcinoma.md: src-cancer-046 (abstract_weighted), src-cancer-055 (abstract_weighted), src-cancer-071 (abstract_weighted), src-cancer-073 (abstract_weighted), src-cancer-074 (abstract_weighted), src-cancer-080 (abstract_weighted)
- topics/cancer/registry-and-prevalence.md: src-cancer-064 (abstract_weighted)
- topics/cancer/synthesis-index.md: src-cancer-006 (abstract_weighted), src-cancer-020 (abstract_weighted), src-cancer-026 (abstract_weighted), src-cancer-027 (abstract_weighted), src-cancer-028 (abstract_weighted), src-cancer-034 (abstract_weighted), src-cancer-035 (abstract_weighted), src-cancer-037 (abstract_weighted), src-cancer-039 (abstract_weighted), src-cancer-041 (abstract_weighted), src-cancer-042 (abstract_weighted), src-cancer-043 (abstract_weighted), src-cancer-044 (abstract_weighted), src-cancer-045 (abstract_weighted), src-cancer-046 (abstract_weighted), src-cancer-047 (abstract_weighted), src-cancer-050 (abstract_weighted), src-cancer-051 (abstract_weighted), src-cancer-052 (abstract_weighted), src-cancer-053 (abstract_weighted), src-cancer-055 (abstract_weighted), src-cancer-060 (abstract_weighted), src-cancer-064 (abstract_weighted), src-cancer-065 (abstract_weighted), src-cancer-066 (abstract_weighted), src-cancer-071 (abstract_weighted), src-cancer-072 (abstract_weighted), src-cancer-073 (abstract_weighted), src-cancer-074 (abstract_weighted), src-cancer-077 (abstract_weighted)
- topics/ckd/index-bilingual.md: src-ckd-051 (abstract_weighted), src-ckd-053 (abstract_weighted), src-ckd-054 (abstract_weighted)
- topics/ckd/index.md: src-ckd-051 (abstract_weighted), src-ckd-053 (abstract_weighted), src-ckd-054 (abstract_weighted)
- topics/ckd/mechanism-overview.md: src-ckd-037 (abstract_weighted), src-ckd-038 (abstract_weighted), src-ckd-051 (abstract_weighted), src-ckd-053 (abstract_weighted), src-ckd-054 (abstract_weighted), src-ckd-058 (abstract_weighted), src-ckd-061 (abstract_weighted), src-ckd-087 (title_only), src-ckd-098 (title_only), src-ckd-101 (title_only), src-ckd-121 (title_only), src-ckd-162 (title_only)
- topics/ckd/synthesis-index.md: src-ckd-051 (abstract_weighted), src-ckd-053 (abstract_weighted), src-ckd-054 (abstract_weighted)
- topics/diabetes/acromegaly-differential-bilingual.md: src-diabetes-036 (abstract_weighted), src-diabetes-061 (abstract_weighted), src-diabetes-075 (abstract_weighted), src-diabetes-090 (abstract_weighted), src-diabetes-092 (abstract_weighted), src-diabetes-114 (abstract_weighted)
- topics/diabetes/acromegaly-differential.md: src-diabetes-036 (abstract_weighted), src-diabetes-061 (abstract_weighted), src-diabetes-075 (abstract_weighted), src-diabetes-090 (abstract_weighted), src-diabetes-092 (abstract_weighted), src-diabetes-114 (abstract_weighted)
- topics/diabetes/index.md: src-diabetes-085 (abstract_weighted), src-diabetes-118 (abstract_weighted), src-diabetes-119 (abstract_weighted)
- topics/diabetes/mechanism-overview.md: src-diabetes-085 (abstract_weighted), src-diabetes-118 (abstract_weighted), src-diabetes-119 (abstract_weighted)
- topics/diabetes/pancreatitis-comorbidity.md: src-diabetes-118 (abstract_weighted)
- topics/diabetes/remission-predictors-matrix-bilingual.md: src-diabetes-054 (abstract_weighted), src-diabetes-078 (abstract_weighted), src-diabetes-091 (abstract_weighted), src-diabetes-111 (abstract_weighted)
- topics/diabetes/remission-predictors-matrix.md: src-diabetes-054 (abstract_weighted), src-diabetes-078 (abstract_weighted), src-diabetes-091 (abstract_weighted), src-diabetes-111 (abstract_weighted)
- topics/diabetes/risk-and-recognition.md: src-diabetes-118 (abstract_weighted)
- topics/diabetes/sglt2-inhibitor-protocol-bilingual.md: src-diabetes-035 (abstract_weighted)
- topics/diabetes/sglt2-inhibitor-protocol.md: src-diabetes-035 (abstract_weighted)
- topics/diabetes/synthesis-index.md: src-diabetes-085 (abstract_weighted), src-diabetes-118 (abstract_weighted), src-diabetes-119 (abstract_weighted)
- topics/fcv/index.md: src-fcv-025 (abstract_weighted), src-fcv-026 (abstract_weighted), src-fcv-027 (abstract_weighted), src-fcv-028 (abstract_weighted), src-fcv-029 (abstract_weighted), src-fcv-030 (abstract_weighted), src-fcv-031 (abstract_weighted), src-fcv-032 (abstract_weighted), src-fcv-033 (abstract_weighted), src-fcv-034 (abstract_weighted), src-fcv-035 (abstract_weighted), src-fcv-036 (abstract_weighted), src-fcv-037 (abstract_weighted), src-fcv-038 (abstract_weighted), src-fcv-039 (abstract_weighted), src-fcv-040 (abstract_weighted), src-fcv-041 (abstract_weighted), src-fcv-042 (abstract_weighted), src-fcv-043 (abstract_weighted), src-fcv-044 (abstract_weighted), src-fcv-045 (abstract_weighted), src-fcv-046 (abstract_weighted), src-fcv-047 (abstract_weighted), src-fcv-048 (abstract_weighted), src-fcv-049 (abstract_weighted), src-fcv-050 (abstract_weighted), src-fcv-051 (abstract_weighted), src-fcv-052 (abstract_weighted), src-fcv-053 (abstract_weighted), src-fcv-054 (abstract_weighted), src-fcv-055 (abstract_weighted), src-fcv-056 (abstract_weighted), src-fcv-057 (abstract_weighted), src-fcv-058 (abstract_weighted), src-fcv-059 (abstract_weighted), src-fcv-060 (abstract_weighted), src-fcv-061 (abstract_weighted), src-fcv-062 (abstract_weighted), src-fcv-063 (abstract_weighted), src-fcv-064 (abstract_weighted), src-fcv-065 (abstract_weighted), src-fcv-066 (abstract_weighted), src-fcv-067 (abstract_weighted), src-fcv-068 (abstract_weighted), src-fcv-069 (abstract_weighted), src-fcv-070 (abstract_weighted), src-fcv-071 (abstract_weighted), src-fcv-072 (abstract_weighted), src-fcv-073 (abstract_weighted), src-fcv-074 (abstract_weighted), src-fcv-075 (abstract_weighted), src-fcv-076 (abstract_weighted), src-fcv-077 (abstract_weighted), src-fcv-078 (abstract_weighted), src-fcv-079 (abstract_weighted), src-fcv-080 (abstract_weighted), src-fcv-081 (abstract_weighted), src-fcv-082 (abstract_weighted), src-fcv-083 (abstract_weighted), src-fcv-084 (abstract_weighted), src-fcv-085 (abstract_weighted), src-fcv-086 (abstract_weighted), src-fcv-087 (abstract_weighted), src-fcv-088 (abstract_weighted), src-fcv-089 (abstract_weighted), src-fcv-090 (abstract_weighted), src-fcv-091 (abstract_weighted), src-fcv-092 (abstract_weighted), src-fcv-093 (abstract_weighted), src-fcv-094 (abstract_weighted), src-fcv-095 (abstract_weighted), src-fcv-096 (abstract_weighted), src-fcv-097 (abstract_weighted), src-fcv-098 (abstract_weighted), src-fcv-099 (abstract_weighted), src-fcv-100 (abstract_weighted), src-fcv-101 (abstract_weighted), src-fcv-102 (abstract_weighted), src-fcv-103 (abstract_weighted)
- topics/fcv/mechanism-overview.md: src-fcv-025 (abstract_weighted), src-fcv-026 (abstract_weighted), src-fcv-027 (abstract_weighted), src-fcv-028 (abstract_weighted), src-fcv-029 (abstract_weighted), src-fcv-032 (abstract_weighted), src-fcv-034 (abstract_weighted), src-fcv-038 (abstract_weighted), src-fcv-039 (abstract_weighted), src-fcv-045 (abstract_weighted)
- topics/fip/index.md: src-fip-025 (abstract_weighted), src-fip-027 (abstract_weighted), src-fip-029 (abstract_weighted), src-fip-030 (abstract_weighted), src-fip-032 (abstract_weighted), src-fip-033 (abstract_weighted), src-fip-034 (abstract_weighted), src-fip-035 (abstract_weighted), src-fip-037 (abstract_weighted), src-fip-038 (abstract_weighted), src-fip-039 (abstract_weighted), src-fip-040 (abstract_weighted), src-fip-041 (abstract_weighted), src-fip-042 (abstract_weighted), src-fip-043 (abstract_weighted), src-fip-044 (abstract_weighted), src-fip-045 (abstract_weighted), src-fip-046 (abstract_weighted), src-fip-047 (abstract_weighted), src-fip-048 (abstract_weighted), src-fip-049 (abstract_weighted)
- topics/fip/mechanism-overview.md: src-fip-047 (abstract_weighted), src-fip-048 (abstract_weighted), src-fip-049 (abstract_weighted)
- topics/fip/synthesis-index.md: src-fip-025 (abstract_weighted), src-fip-027 (abstract_weighted), src-fip-029 (abstract_weighted), src-fip-030 (abstract_weighted), src-fip-032 (abstract_weighted), src-fip-033 (abstract_weighted), src-fip-034 (abstract_weighted), src-fip-035 (abstract_weighted), src-fip-037 (abstract_weighted), src-fip-038 (abstract_weighted), src-fip-039 (abstract_weighted), src-fip-040 (abstract_weighted), src-fip-041 (abstract_weighted), src-fip-042 (abstract_weighted), src-fip-043 (abstract_weighted), src-fip-044 (abstract_weighted), src-fip-045 (abstract_weighted), src-fip-046 (abstract_weighted), src-fip-047 (abstract_weighted), src-fip-048 (abstract_weighted), src-fip-049 (abstract_weighted)
- topics/fip/treatment-overview.md: src-fip-029 (abstract_weighted), src-fip-030 (abstract_weighted), src-fip-032 (abstract_weighted), src-fip-033 (abstract_weighted), src-fip-034 (abstract_weighted), src-fip-035 (abstract_weighted), src-fip-037 (abstract_weighted), src-fip-038 (abstract_weighted), src-fip-039 (abstract_weighted), src-fip-040 (abstract_weighted), src-fip-041 (abstract_weighted), src-fip-042 (abstract_weighted)
- topics/obesity/index.md: src-obesity-085 (abstract_weighted), src-obesity-088 (abstract_weighted), src-obesity-089 (abstract_weighted), src-obesity-090 (abstract_weighted)
- topics/obesity/mechanism-overview.md: src-obesity-085 (abstract_weighted), src-obesity-088 (abstract_weighted), src-obesity-089 (abstract_weighted), src-obesity-090 (abstract_weighted)
- topics/obesity/weight-loss-energy-calibration-bilingual.md: src-obesity-089 (abstract_weighted), src-obesity-094 (abstract_weighted)
- topics/obesity/weight-loss-energy-calibration.md: src-obesity-089 (abstract_weighted), src-obesity-094 (abstract_weighted)

## Next Actions

- No immediate structural action from this report.
