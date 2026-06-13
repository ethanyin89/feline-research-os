---
id: system-health-report-20260603
type: health-check
topic: operating-system
question_type: health
language: bilingual
last_compiled_at: 2026-06-03
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: needs_attention
---

# Vault Health Report, 2026-06-03

This report aggregates existing checks. It does not call an LLM and does not replace human review.

## Summary

| Check | Status | Read |
|---|---|---|
| Markdown links | PASS | PASS: checked 1290 markdown files, no local link issues found. |
| Query tests | PASS | 111 passed  \|  0 failed  \|  111 total |
| Ordinary-user vault eval | PASS | All ordinary-user free-mode samples passed without API calls. |
| Paper source cards | PASS | 427 strict disease paper cards; baseline >= 246 |
| Regulation source cards | PASS | 14 regulation cards |
| Source IDs | PASS | 0 duplicates, 0 missing ids |
| Low-word paper cards | PASS | 0 cards below 700 words |
| Source schema fields | FAIL | 0 cards missing required fields, 1 invalid field values |
| Source state consistency | PASS | 0 title-only depth/status conflicts |
| Source link proof | PASS | 0 source cards without DOI or URL |
| Source evidence policy | PASS | 0 source cards with empty evidence_policy |
| Source quoted-fact discipline | PASS | 0 quoted_fact items look interpretive |
| Compiled source refs | PASS | 0 invalid source refs |
| Reader page source_ids | PASS | 0 missing, 0 empty |
| Thin source usage | WARN | 6 reader/high-visibility pages use abstract-weighted or title-only sources |
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
| Acceptance report | PASS | system/health-checks/ask-the-vault-acceptance-report-20260428.md; mode=executed; status=pass |
| Ordinary-user acceptance | PASS | system/health-checks/ordinary-user-acceptance-report-20260519.md; mode=executed; status=pass |
| Compile trigger | PASS | 14 changed source cards, 4 downstream files |
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
| cancer | 102 | abstract: 69, full: 6, partial: 27 | abstract_weighted: 74, deep_extracted: 6, not_pubmed_indexed: 1, publisher_verified: 1, title_only: 20 |

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
| cancer | 0 | 0 | 0 |

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

## Source Schema Issues

- raw/papers/src-cancer-030.md: `verification_status: not_pubmed_indexed` is outside the allowed set

## Thin Source Usage

`abstract_weighted` and `title_only` sources can support cautious synthesis, but should not be read as full-text or decision-grade proof.
- topics/cancer/current-state-dashboard.md: src-cancer-052 (abstract_weighted), src-cancer-054 (abstract_weighted), src-cancer-055 (abstract_weighted), src-cancer-056 (abstract_weighted), src-cancer-060 (abstract_weighted), src-cancer-061 (abstract_weighted), src-cancer-062 (abstract_weighted), src-cancer-064 (abstract_weighted)
- topics/cancer/injection-site-sarcoma.md: src-cancer-047 (abstract_weighted)
- topics/cancer/lymphoma.md: src-cancer-063 (abstract_weighted), src-cancer-065 (abstract_weighted), src-cancer-068 (abstract_weighted), src-cancer-048 (abstract_weighted), src-cancer-075 (abstract_weighted), src-cancer-029 (abstract_weighted), src-cancer-018 (abstract_weighted), src-cancer-026 (abstract_weighted), src-cancer-042 (abstract_weighted), src-cancer-044 (abstract_weighted), src-cancer-060 (abstract_weighted)
- topics/cancer/mammary-carcinoma.md: src-cancer-009 (abstract_weighted), src-cancer-012 (abstract_weighted), src-cancer-025 (abstract_weighted), src-cancer-015 (abstract_weighted), src-cancer-022 (abstract_weighted), src-cancer-028 (abstract_weighted), src-cancer-013 (abstract_weighted), src-cancer-005 (abstract_weighted), src-cancer-016 (abstract_weighted), src-cancer-017 (abstract_weighted), src-cancer-020 (abstract_weighted), src-cancer-032 (abstract_weighted), src-cancer-034 (abstract_weighted), src-cancer-036 (abstract_weighted), src-cancer-038 (abstract_weighted), src-cancer-041 (abstract_weighted), src-cancer-043 (abstract_weighted), src-cancer-045 (abstract_weighted), src-cancer-049 (abstract_weighted), src-cancer-050 (abstract_weighted), src-cancer-052 (abstract_weighted), src-cancer-054 (abstract_weighted), src-cancer-056 (abstract_weighted)
- topics/cancer/oral-squamous-cell-carcinoma.md: src-cancer-095 (abstract_weighted), src-cancer-046 (abstract_weighted), src-cancer-031 (abstract_weighted), src-cancer-021 (abstract_weighted), src-cancer-055 (abstract_weighted), src-cancer-061 (abstract_weighted), src-cancer-062 (abstract_weighted)
- topics/cancer/registry-and-prevalence.md: src-cancer-007 (abstract_weighted), src-cancer-064 (abstract_weighted)

## Next Actions

- Run live acceptance once `OPENROUTER_API_KEY` or `ANTHROPIC_API_KEY` is present.
- Fix source-card schema fields before compiling downstream topic/output pages.
