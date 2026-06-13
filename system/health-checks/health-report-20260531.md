---
id: system-health-report-20260531
type: health-check
topic: operating-system
question_type: health
language: bilingual
last_compiled_at: 2026-05-31
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: needs_attention
---

# Vault Health Report, 2026-05-31

This report aggregates existing checks. It does not call an LLM and does not replace human review.

## Summary

| Check | Status | Read |
|---|---|---|
| Markdown links | PASS | PASS: checked 1277 markdown files, no local link issues found. |
| Query tests | PASS | 107 passed  \|  0 failed  \|  107 total |
| Paper source cards | PASS | 325 strict disease paper cards; baseline >= 144 |
| Regulation source cards | PASS | 14 regulation cards |
| Source IDs | PASS | 0 duplicates, 0 missing ids |
| Low-word paper cards | PASS | 0 cards below 700 words |
| Source schema fields | PASS | 0 cards missing required fields, 0 invalid field values |
| Source state consistency | PASS | 0 title-only depth/status conflicts |
| Source link proof | PASS | 0 source cards without DOI or URL |
| Source evidence policy | PASS | 0 source cards with empty evidence_policy |
| Source quoted-fact discipline | PASS | 0 quoted_fact items look interpretive |
| Compiled source refs | FAIL | 36 invalid source refs |
| Reader page source_ids | PASS | 0 missing, 0 empty |
| Thin source usage | PASS | 0 reader/high-visibility pages use abstract-weighted or title-only sources |
| Thin source caveats | PASS | 0 thin-source pages without visible evidence-depth caveat |
| Title-only caveats | PASS | 0 pages cite title-only sources without visible caveat |
| Key-claim traceability | PASS | 0 high-value pages missing traceability table |
| Quantified claim traceability | PASS | 0 quantified reader pages missing traceability table |
| Reader quoted-fact discipline | PASS | 0 reader quoted_fact items look interpretive |
| High-visibility language QA | WARN | 2 high-visibility pages unchecked or missing |
| Obesity compiled guidance gate | PASS | 0 obesity reader pages exceed shell/source-indexed status |
| Decision-grade gate | PASS | 0 source-card violations |
| Candidate image gate | PASS | 0 candidate refs remain gated in local_assets frontmatter |
| Inbox backlog | PASS | 0 active files, 1 blocked/held files, 15 rejected audit files |
| Acceptance report | PASS | system/health-checks/ask-the-vault-acceptance-report-20260428.md; mode=executed; status=pass |
| Ordinary-user acceptance | PASS | system/health-checks/ordinary-user-acceptance-report-20260519.md; mode=executed; status=pass |
| Compile trigger | PASS | 102 changed source cards, 39 downstream files |
| API keys | WARN | no API keys in current shell |

## Source Card Reality

| Disease | Cards | extraction_depth | verification_status |
|---|---:|---|---|
| ckd | 24 | full: 24 | deep_extracted: 24 |
| fip | 24 | full: 24 | deep_extracted: 24 |
| hcm | 24 | full: 24 | deep_extracted: 24 |
| ibd | 24 | full: 24 | deep_extracted: 24 |
| diabetes | 118 | full: 24, partial: 94 | abstract_weighted: 59, deep_extracted: 24, title_only: 35 |
| fcv | 24 | full: 24 | deep_extracted: 24 |
| obesity | 87 | full: 4, partial: 83 | abstract_weighted: 41, deep_extracted: 4, title_only: 42 |

## Image Reality

| Disease | Verified images | Candidate refs | Candidate refs in local_assets |
|---|---:|---:|---:|
| ckd | 8 | 0 | 0 |
| fip | 1 | 0 | 0 |
| hcm | 1 | 0 | 0 |
| ibd | 1 | 0 | 0 |
| diabetes | 1 | 0 | 0 |
| fcv | 0 | 0 | 0 |
| obesity | 0 | 0 | 0 |

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

## Compiled Provenance Issues

- system/indexes/src-cancer-002-deep-extraction-round1.md: unknown source id `src-cancer-002`
- system/indexes/src-cancer-003-deep-extraction-round1.md: unknown source id `src-cancer-003`
- system/indexes/src-cancer-003-structured-abstract-round1.md: unknown source id `src-cancer-003`
- system/indexes/src-cancer-004-deep-extraction-round1.md: unknown source id `src-cancer-004`
- system/indexes/src-cancer-004-structured-abstract-round1.md: unknown source id `src-cancer-004`
- system/indexes/src-cancer-005-structured-abstract-round1.md: unknown source id `src-cancer-005`
- system/indexes/src-cancer-008-deep-extraction-round1.md: unknown source id `src-cancer-008`
- system/indexes/src-cancer-008-structured-abstract-round1.md: unknown source id `src-cancer-008`
- system/indexes/src-cancer-009-structured-abstract-round1.md: unknown source id `src-cancer-009`
- system/indexes/src-cancer-019-deep-extraction-round1.md: unknown source id `src-cancer-019`
- system/indexes/src-cancer-019-structured-abstract-round1.md: unknown source id `src-cancer-019`
- system/indexes/src-cancer-021-structured-abstract-round1.md: unknown source id `src-cancer-021`
- system/indexes/src-cancer-025-structured-abstract-round1.md: unknown source id `src-cancer-025`
- system/indexes/src-cancer-040-deep-extraction-round1.md: unknown source id `src-cancer-040`
- system/indexes/src-cancer-040-structured-abstract-round1.md: unknown source id `src-cancer-040`
- system/indexes/src-cancer-046-structured-abstract-round1.md: unknown source id `src-cancer-046`
- topics/cancer/cox-prognosis-markers.md: unknown source id `src-cancer-003`
- topics/cancer/lymphoma.md: unknown source id `src-cancer-004`
- topics/cancer/lymphoma.md: unknown source id `src-cancer-008`
- topics/cancer/lymphoma.md: unknown source id `src-cancer-063`
- topics/cancer/lymphoma.md: unknown source id `src-cancer-068`
- topics/cancer/mammary-carcinoma.md: unknown source id `src-cancer-004`
- topics/cancer/mammary-carcinoma.md: unknown source id `src-cancer-019`
- topics/cancer/mammary-carcinoma.md: unknown source id `src-cancer-003`
- topics/cancer/oral-squamous-cell-carcinoma.md: unknown source id `src-cancer-004`
- topics/cancer/oral-squamous-cell-carcinoma.md: unknown source id `src-cancer-095`
- topics/cancer/registry-and-prevalence.md: unknown source id `src-cancer-002`
- topics/cancer/registry-and-prevalence.md: unknown source id `src-cancer-007`
- topics/cancer/suspected-cancer-workflow.md: unknown source id `src-cancer-040`
- topics/cancer/suspected-cancer-workflow.md: unknown source id `src-cancer-004`
- topics/cancer/synthesis-index.md: unknown source id `src-cancer-002`
- topics/cancer/synthesis-index.md: unknown source id `src-cancer-003`
- topics/cancer/synthesis-index.md: unknown source id `src-cancer-004`
- topics/cancer/synthesis-index.md: unknown source id `src-cancer-008`
- topics/cancer/synthesis-index.md: unknown source id `src-cancer-019`
- topics/cancer/synthesis-index.md: unknown source id `src-cancer-040`

## High-Visibility Language QA Gaps

Unchecked high-visibility pages can make source-supported claims sound stronger than the evidence.
- topics/cancer/current-state-dashboard.md: `language_qa_status: missing`
- topics/cancer/synthesis-index.md: `language_qa_status: not_checked`

## Next Actions

- Run live acceptance once `OPENROUTER_API_KEY` or `ANTHROPIC_API_KEY` is present.
- Fix invalid `source_ids` before trusting compiled topic/output pages.
- Language-QA high-visibility pages so source-supported claims do not become overstrong through wording drift.
