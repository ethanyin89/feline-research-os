---
id: system-health-report-20260423
type: health-check
topic: operating-system
question_type: health
language: bilingual
last_compiled_at: 2026-04-23
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Vault Health Report, 2026-04-23

This report aggregates existing checks. It does not call an LLM and does not replace human review.

## Summary

| Check | Status | Read |
|---|---|---|
| Markdown links | PASS | PASS: checked 656 markdown files, no local link issues found. |
| Query tests | PASS | 75 passed  \|  0 failed  \|  75 total |
| Paper source cards | PASS | 120 strict disease paper cards |
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
| Thin source usage | WARN | 65 reader/high-visibility pages use abstract-weighted or title-only sources |
| Thin source caveats | PASS | 0 thin-source pages without visible evidence-depth caveat |
| Title-only caveats | PASS | 0 pages cite title-only sources without visible caveat |
| Key-claim traceability | PASS | 0 high-value pages missing traceability table |
| Quantified claim traceability | PASS | 0 quantified reader pages missing traceability table |
| Reader quoted-fact discipline | PASS | 0 reader quoted_fact items look interpretive |
| High-visibility language QA | PASS | 0 high-visibility pages unchecked or missing |
| Decision-grade gate | PASS | 0 source-card violations |
| Candidate image gate | PASS | 0 candidate refs remain gated in local_assets frontmatter |
| Inbox backlog | PASS | 0 active files, 11 rejected audit files |
| Acceptance report | WARN | system/health-checks/ask-the-vault-acceptance-report-20260423.md; mode=blocked-missing-key:OPENROUTER_API_KEY; status=blocked |
| Compile trigger | PASS | 2 changed source cards, 47 downstream files |
| API keys | WARN | no API keys in current shell |

## Source Card Reality

| Disease | Cards | extraction_depth | verification_status |
|---|---:|---|---|
| ckd | 24 | full: 24 | deep_extracted: 24 |
| fip | 24 | full: 24 | deep_extracted: 24 |
| hcm | 24 | full: 24 | abstract_weighted: 23, source_checked: 1 |
| ibd | 24 | full: 24 | abstract_weighted: 9, deep_extracted: 14, source_checked: 1 |
| diabetes | 24 | full: 24 | abstract_weighted: 23, deep_extracted: 1 |

## Image Reality

| Disease | Verified images | Candidate refs | Candidate refs in local_assets |
|---|---:|---:|---:|
| ckd | 8 | 0 | 0 |
| fip | 1 | 0 | 0 |
| hcm | 1 | 0 | 0 |
| ibd | 1 | 0 | 0 |
| diabetes | 1 | 0 | 0 |

## Inbox Backlog

- No active inbox files outside `.gitkeep`.

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

## Thin Source Usage

`abstract_weighted` and `title_only` sources can support cautious synthesis, but should not be read as full-text or decision-grade proof.
- outputs/briefings/out-diabetes-briefing-20260421-round1-en.md: src-diabetes-005 (abstract_weighted), src-diabetes-006 (abstract_weighted), src-diabetes-007 (abstract_weighted), src-diabetes-010 (abstract_weighted), src-diabetes-011 (abstract_weighted), src-diabetes-013 (abstract_weighted), src-diabetes-014 (abstract_weighted), src-diabetes-015 (abstract_weighted), src-diabetes-020 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- outputs/briefings/out-diabetes-briefing-20260421-round1-working-en.md: src-diabetes-005 (abstract_weighted), src-diabetes-006 (abstract_weighted), src-diabetes-007 (abstract_weighted), src-diabetes-009 (abstract_weighted), src-diabetes-010 (abstract_weighted), src-diabetes-011 (abstract_weighted), src-diabetes-012 (abstract_weighted), src-diabetes-013 (abstract_weighted), src-diabetes-014 (abstract_weighted), src-diabetes-015 (abstract_weighted), src-diabetes-020 (abstract_weighted), src-diabetes-022 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- outputs/briefings/out-diabetes-briefing-20260421-round1-zh.md: src-diabetes-005 (abstract_weighted), src-diabetes-006 (abstract_weighted), src-diabetes-007 (abstract_weighted), src-diabetes-010 (abstract_weighted), src-diabetes-011 (abstract_weighted), src-diabetes-013 (abstract_weighted), src-diabetes-014 (abstract_weighted), src-diabetes-015 (abstract_weighted), src-diabetes-020 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- outputs/briefings/out-hcm-briefing-20260410-round1-en.md: src-hcm-001 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-006 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-015 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-024 (abstract_weighted)
- outputs/briefings/out-hcm-briefing-20260410-round1-working-en.md: src-hcm-001 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-006 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-015 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-024 (abstract_weighted)
- outputs/briefings/out-hcm-briefing-20260410-round1-zh.md: src-hcm-001 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-006 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-015 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-024 (abstract_weighted)
- outputs/dossiers/out-diabetes-dossier-20260421-v1-en.md: src-diabetes-005 (abstract_weighted), src-diabetes-006 (abstract_weighted), src-diabetes-007 (abstract_weighted), src-diabetes-010 (abstract_weighted), src-diabetes-011 (abstract_weighted), src-diabetes-013 (abstract_weighted), src-diabetes-014 (abstract_weighted), src-diabetes-015 (abstract_weighted), src-diabetes-020 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- outputs/dossiers/out-diabetes-dossier-20260421-v1-working-en.md: src-diabetes-004 (abstract_weighted), src-diabetes-005 (abstract_weighted), src-diabetes-006 (abstract_weighted), src-diabetes-007 (abstract_weighted), src-diabetes-009 (abstract_weighted), src-diabetes-010 (abstract_weighted), src-diabetes-011 (abstract_weighted), src-diabetes-012 (abstract_weighted), src-diabetes-013 (abstract_weighted), src-diabetes-014 (abstract_weighted), src-diabetes-015 (abstract_weighted), src-diabetes-018 (abstract_weighted), src-diabetes-020 (abstract_weighted), src-diabetes-022 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- outputs/dossiers/out-diabetes-dossier-20260421-v1-zh.md: src-diabetes-005 (abstract_weighted), src-diabetes-006 (abstract_weighted), src-diabetes-007 (abstract_weighted), src-diabetes-010 (abstract_weighted), src-diabetes-011 (abstract_weighted), src-diabetes-013 (abstract_weighted), src-diabetes-014 (abstract_weighted), src-diabetes-015 (abstract_weighted), src-diabetes-020 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- outputs/dossiers/out-hcm-dossier-20260410-v1-en.md: src-hcm-001 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-006 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-015 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-024 (abstract_weighted)
- outputs/dossiers/out-hcm-dossier-20260410-v1-working-en.md: src-hcm-001 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-006 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-015 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-024 (abstract_weighted)
- outputs/dossiers/out-hcm-dossier-20260410-v1-zh.md: src-hcm-001 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-006 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-015 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-024 (abstract_weighted)
- topics/diabetes/complications-neuropathy.md: src-diabetes-004 (abstract_weighted), src-diabetes-018 (abstract_weighted)
- topics/diabetes/current-state-dashboard-bilingual.md: src-diabetes-002 (abstract_weighted), src-diabetes-003 (abstract_weighted), src-diabetes-004 (abstract_weighted), src-diabetes-005 (abstract_weighted), src-diabetes-006 (abstract_weighted), src-diabetes-007 (abstract_weighted), src-diabetes-008 (abstract_weighted), src-diabetes-009 (abstract_weighted), src-diabetes-010 (abstract_weighted), src-diabetes-011 (abstract_weighted), src-diabetes-012 (abstract_weighted), src-diabetes-013 (abstract_weighted), src-diabetes-014 (abstract_weighted), src-diabetes-015 (abstract_weighted), src-diabetes-016 (abstract_weighted), src-diabetes-017 (abstract_weighted), src-diabetes-018 (abstract_weighted), src-diabetes-019 (abstract_weighted), src-diabetes-020 (abstract_weighted), src-diabetes-021 (abstract_weighted), src-diabetes-022 (abstract_weighted), src-diabetes-023 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- topics/diabetes/current-state-dashboard.md: src-diabetes-002 (abstract_weighted), src-diabetes-003 (abstract_weighted), src-diabetes-004 (abstract_weighted), src-diabetes-005 (abstract_weighted), src-diabetes-006 (abstract_weighted), src-diabetes-007 (abstract_weighted), src-diabetes-008 (abstract_weighted), src-diabetes-009 (abstract_weighted), src-diabetes-010 (abstract_weighted), src-diabetes-011 (abstract_weighted), src-diabetes-012 (abstract_weighted), src-diabetes-013 (abstract_weighted), src-diabetes-014 (abstract_weighted), src-diabetes-015 (abstract_weighted), src-diabetes-016 (abstract_weighted), src-diabetes-017 (abstract_weighted), src-diabetes-018 (abstract_weighted), src-diabetes-019 (abstract_weighted), src-diabetes-020 (abstract_weighted), src-diabetes-021 (abstract_weighted), src-diabetes-022 (abstract_weighted), src-diabetes-023 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- topics/diabetes/diagnostic-monitoring-workup.md: src-diabetes-005 (abstract_weighted), src-diabetes-010 (abstract_weighted), src-diabetes-013 (abstract_weighted), src-diabetes-014 (abstract_weighted), src-diabetes-020 (abstract_weighted), src-diabetes-021 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- topics/diabetes/diet-architecture.md: src-diabetes-006 (abstract_weighted), src-diabetes-007 (abstract_weighted), src-diabetes-015 (abstract_weighted), src-diabetes-016 (abstract_weighted), src-diabetes-022 (abstract_weighted)
- topics/diabetes/endocrine-secondary-diabetes.md: src-diabetes-013 (abstract_weighted), src-diabetes-020 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- topics/diabetes/endpoint-handbook.md: src-diabetes-004 (abstract_weighted), src-diabetes-006 (abstract_weighted), src-diabetes-007 (abstract_weighted), src-diabetes-008 (abstract_weighted), src-diabetes-011 (abstract_weighted), src-diabetes-015 (abstract_weighted), src-diabetes-016 (abstract_weighted), src-diabetes-018 (abstract_weighted), src-diabetes-022 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- topics/diabetes/epidemiology-and-breed-risk.md: src-diabetes-009 (abstract_weighted), src-diabetes-012 (abstract_weighted), src-diabetes-023 (abstract_weighted)
- topics/diabetes/index.md: src-diabetes-002 (abstract_weighted), src-diabetes-003 (abstract_weighted), src-diabetes-004 (abstract_weighted), src-diabetes-005 (abstract_weighted), src-diabetes-006 (abstract_weighted), src-diabetes-007 (abstract_weighted), src-diabetes-008 (abstract_weighted), src-diabetes-009 (abstract_weighted), src-diabetes-010 (abstract_weighted), src-diabetes-011 (abstract_weighted), src-diabetes-012 (abstract_weighted), src-diabetes-013 (abstract_weighted), src-diabetes-014 (abstract_weighted), src-diabetes-015 (abstract_weighted), src-diabetes-016 (abstract_weighted), src-diabetes-017 (abstract_weighted), src-diabetes-018 (abstract_weighted), src-diabetes-019 (abstract_weighted), src-diabetes-020 (abstract_weighted), src-diabetes-021 (abstract_weighted), src-diabetes-022 (abstract_weighted), src-diabetes-023 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- topics/diabetes/mechanism-overview.md: src-diabetes-002 (abstract_weighted), src-diabetes-003 (abstract_weighted), src-diabetes-005 (abstract_weighted), src-diabetes-013 (abstract_weighted), src-diabetes-019 (abstract_weighted), src-diabetes-020 (abstract_weighted)
- topics/diabetes/obesity-and-body-condition.md: src-diabetes-005 (abstract_weighted), src-diabetes-006 (abstract_weighted)
- topics/diabetes/pancreatitis-comorbidity.md: src-diabetes-010 (abstract_weighted), src-diabetes-023 (abstract_weighted)
- topics/diabetes/regulatory-brief.md: src-diabetes-011 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- topics/diabetes/remission-boundaries.md: src-diabetes-007 (abstract_weighted), src-diabetes-015 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- topics/diabetes/risk-and-recognition.md: src-diabetes-005 (abstract_weighted), src-diabetes-009 (abstract_weighted), src-diabetes-010 (abstract_weighted), src-diabetes-012 (abstract_weighted), src-diabetes-013 (abstract_weighted), src-diabetes-020 (abstract_weighted), src-diabetes-023 (abstract_weighted)
- topics/diabetes/sglt2-label-control.md: src-diabetes-011 (abstract_weighted)
- topics/diabetes/synthesis-index.md: src-diabetes-002 (abstract_weighted), src-diabetes-003 (abstract_weighted), src-diabetes-004 (abstract_weighted), src-diabetes-005 (abstract_weighted), src-diabetes-006 (abstract_weighted), src-diabetes-007 (abstract_weighted), src-diabetes-008 (abstract_weighted), src-diabetes-009 (abstract_weighted), src-diabetes-010 (abstract_weighted), src-diabetes-011 (abstract_weighted), src-diabetes-012 (abstract_weighted), src-diabetes-013 (abstract_weighted), src-diabetes-014 (abstract_weighted), src-diabetes-015 (abstract_weighted), src-diabetes-016 (abstract_weighted), src-diabetes-017 (abstract_weighted), src-diabetes-018 (abstract_weighted), src-diabetes-019 (abstract_weighted), src-diabetes-020 (abstract_weighted), src-diabetes-021 (abstract_weighted), src-diabetes-022 (abstract_weighted), src-diabetes-023 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- topics/diabetes/translation-brief.md: src-diabetes-006 (abstract_weighted), src-diabetes-007 (abstract_weighted), src-diabetes-008 (abstract_weighted), src-diabetes-011 (abstract_weighted), src-diabetes-015 (abstract_weighted), src-diabetes-016 (abstract_weighted), src-diabetes-017 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- topics/diabetes/treatment-branch-map.md: src-diabetes-006 (abstract_weighted), src-diabetes-007 (abstract_weighted), src-diabetes-008 (abstract_weighted), src-diabetes-011 (abstract_weighted), src-diabetes-015 (abstract_weighted), src-diabetes-016 (abstract_weighted), src-diabetes-017 (abstract_weighted), src-diabetes-022 (abstract_weighted), src-diabetes-024 (abstract_weighted)
- topics/hcm/cardiomyopathy-boundary-bilingual.md: src-hcm-001 (abstract_weighted), src-hcm-005 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-018 (abstract_weighted), src-hcm-021 (abstract_weighted)
- topics/hcm/current-state-dashboard-bilingual.md: src-hcm-001 (abstract_weighted), src-hcm-002 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-005 (abstract_weighted), src-hcm-006 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-011 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-014 (abstract_weighted), src-hcm-015 (abstract_weighted), src-hcm-016 (abstract_weighted), src-hcm-017 (abstract_weighted), src-hcm-018 (abstract_weighted), src-hcm-019 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-021 (abstract_weighted), src-hcm-022 (abstract_weighted), src-hcm-023 (abstract_weighted), src-hcm-024 (abstract_weighted)
- topics/hcm/current-state-dashboard.md: src-hcm-001 (abstract_weighted), src-hcm-002 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-005 (abstract_weighted), src-hcm-006 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-011 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-014 (abstract_weighted), src-hcm-015 (abstract_weighted), src-hcm-016 (abstract_weighted), src-hcm-017 (abstract_weighted), src-hcm-018 (abstract_weighted), src-hcm-019 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-021 (abstract_weighted), src-hcm-022 (abstract_weighted), src-hcm-023 (abstract_weighted), src-hcm-024 (abstract_weighted)
- topics/hcm/diagnostic-workup-bilingual.md: src-hcm-001 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-021 (abstract_weighted), src-hcm-023 (abstract_weighted)
- topics/hcm/endpoint-handbook-bilingual.md: src-hcm-006 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-017 (abstract_weighted), src-hcm-019 (abstract_weighted), src-hcm-023 (abstract_weighted), src-hcm-024 (abstract_weighted)
- topics/hcm/endpoint-handbook.md: src-hcm-006 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-017 (abstract_weighted), src-hcm-019 (abstract_weighted), src-hcm-023 (abstract_weighted), src-hcm-024 (abstract_weighted)
- topics/hcm/genotype-severity-bilingual.md: src-hcm-001 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-012 (abstract_weighted)
- topics/hcm/index.md: src-hcm-001 (abstract_weighted), src-hcm-002 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-005 (abstract_weighted), src-hcm-006 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-011 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-014 (abstract_weighted), src-hcm-015 (abstract_weighted), src-hcm-016 (abstract_weighted), src-hcm-017 (abstract_weighted), src-hcm-018 (abstract_weighted), src-hcm-019 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-021 (abstract_weighted), src-hcm-022 (abstract_weighted), src-hcm-023 (abstract_weighted), src-hcm-024 (abstract_weighted)
- topics/hcm/mechanism-overview-bilingual.md: src-hcm-001 (abstract_weighted), src-hcm-002 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-016 (abstract_weighted), src-hcm-019 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-022 (abstract_weighted), src-hcm-024 (abstract_weighted)
- topics/hcm/mechanism-overview.md: src-hcm-001 (abstract_weighted), src-hcm-002 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-016 (abstract_weighted), src-hcm-019 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-022 (abstract_weighted), src-hcm-024 (abstract_weighted)
- topics/hcm/phenotype-remodeling-bridge-bilingual.md: src-hcm-001 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-024 (abstract_weighted)
- topics/hcm/regulatory-brief-bilingual.md: src-hcm-001 (abstract_weighted), src-hcm-002 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-005 (abstract_weighted), src-hcm-006 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-011 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-014 (abstract_weighted), src-hcm-015 (abstract_weighted), src-hcm-016 (abstract_weighted), src-hcm-017 (abstract_weighted), src-hcm-018 (abstract_weighted), src-hcm-019 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-021 (abstract_weighted), src-hcm-022 (abstract_weighted), src-hcm-023 (abstract_weighted), src-hcm-024 (abstract_weighted)
- topics/hcm/regulatory-brief.md: src-hcm-001 (abstract_weighted), src-hcm-002 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-005 (abstract_weighted), src-hcm-006 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-011 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-014 (abstract_weighted), src-hcm-015 (abstract_weighted), src-hcm-016 (abstract_weighted), src-hcm-017 (abstract_weighted), src-hcm-018 (abstract_weighted), src-hcm-019 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-021 (abstract_weighted), src-hcm-022 (abstract_weighted), src-hcm-023 (abstract_weighted), src-hcm-024 (abstract_weighted)
- topics/hcm/risk-and-recognition-bilingual.md: src-hcm-001 (abstract_weighted), src-hcm-002 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-021 (abstract_weighted), src-hcm-023 (abstract_weighted), src-hcm-024 (abstract_weighted)
- topics/hcm/risk-and-recognition.md: src-hcm-001 (abstract_weighted), src-hcm-002 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-021 (abstract_weighted), src-hcm-023 (abstract_weighted), src-hcm-024 (abstract_weighted)
- topics/hcm/synthesis-index-bilingual.md: src-hcm-001 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-006 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-011 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-014 (abstract_weighted), src-hcm-015 (abstract_weighted), src-hcm-017 (abstract_weighted), src-hcm-019 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-021 (abstract_weighted), src-hcm-022 (abstract_weighted), src-hcm-023 (abstract_weighted), src-hcm-024 (abstract_weighted)
- topics/hcm/synthesis-index.md: src-hcm-001 (abstract_weighted), src-hcm-002 (abstract_weighted), src-hcm-004 (abstract_weighted), src-hcm-005 (abstract_weighted), src-hcm-006 (abstract_weighted), src-hcm-007 (abstract_weighted), src-hcm-008 (abstract_weighted), src-hcm-009 (abstract_weighted), src-hcm-010 (abstract_weighted), src-hcm-011 (abstract_weighted), src-hcm-012 (abstract_weighted), src-hcm-013 (abstract_weighted), src-hcm-014 (abstract_weighted), src-hcm-015 (abstract_weighted), src-hcm-016 (abstract_weighted), src-hcm-017 (abstract_weighted), src-hcm-018 (abstract_weighted), src-hcm-019 (abstract_weighted), src-hcm-020 (abstract_weighted), src-hcm-021 (abstract_weighted), src-hcm-022 (abstract_weighted), src-hcm-023 (abstract_weighted), src-hcm-024 (abstract_weighted)
- topics/hcm/translation-brief-bilingual.md: src-hcm-008 (abstract_weighted), src-hcm-011 (abstract_weighted), src-hcm-014 (abstract_weighted), src-hcm-015 (abstract_weighted)
- topics/hcm/translation-brief.md: src-hcm-008 (abstract_weighted), src-hcm-011 (abstract_weighted), src-hcm-014 (abstract_weighted), src-hcm-015 (abstract_weighted)
- topics/ibd/current-state-dashboard-bilingual.md: src-ibd-002 (abstract_weighted), src-ibd-005 (abstract_weighted), src-ibd-006 (abstract_weighted), src-ibd-008 (abstract_weighted), src-ibd-018 (abstract_weighted), src-ibd-020 (abstract_weighted), src-ibd-021 (abstract_weighted), src-ibd-023 (abstract_weighted), src-ibd-024 (abstract_weighted)
- topics/ibd/current-state-dashboard.md: src-ibd-002 (abstract_weighted), src-ibd-005 (abstract_weighted), src-ibd-006 (abstract_weighted), src-ibd-008 (abstract_weighted), src-ibd-018 (abstract_weighted), src-ibd-020 (abstract_weighted), src-ibd-021 (abstract_weighted), src-ibd-023 (abstract_weighted), src-ibd-024 (abstract_weighted)
- topics/ibd/extension-branches-bilingual.md: src-ibd-018 (abstract_weighted), src-ibd-020 (abstract_weighted), src-ibd-023 (abstract_weighted), src-ibd-024 (abstract_weighted)
- topics/ibd/index.md: src-ibd-002 (abstract_weighted), src-ibd-005 (abstract_weighted), src-ibd-006 (abstract_weighted), src-ibd-008 (abstract_weighted), src-ibd-018 (abstract_weighted), src-ibd-020 (abstract_weighted), src-ibd-021 (abstract_weighted), src-ibd-023 (abstract_weighted), src-ibd-024 (abstract_weighted)
- topics/ibd/mechanism-overview-bilingual.md: src-ibd-006 (abstract_weighted), src-ibd-024 (abstract_weighted)
- topics/ibd/mechanism-overview.md: src-ibd-006 (abstract_weighted), src-ibd-024 (abstract_weighted)
- topics/ibd/regulatory-brief-bilingual.md: src-ibd-005 (abstract_weighted), src-ibd-021 (abstract_weighted)
- topics/ibd/regulatory-brief.md: src-ibd-005 (abstract_weighted), src-ibd-021 (abstract_weighted)
- topics/ibd/risk-and-recognition-bilingual.md: src-ibd-024 (abstract_weighted)
- topics/ibd/risk-and-recognition.md: src-ibd-024 (abstract_weighted)
- topics/ibd/synthesis-index-bilingual.md: src-ibd-002 (abstract_weighted), src-ibd-005 (abstract_weighted), src-ibd-006 (abstract_weighted), src-ibd-008 (abstract_weighted), src-ibd-018 (abstract_weighted), src-ibd-020 (abstract_weighted), src-ibd-021 (abstract_weighted), src-ibd-023 (abstract_weighted), src-ibd-024 (abstract_weighted)
- topics/ibd/synthesis-index.md: src-ibd-002 (abstract_weighted), src-ibd-005 (abstract_weighted), src-ibd-006 (abstract_weighted), src-ibd-008 (abstract_weighted), src-ibd-018 (abstract_weighted), src-ibd-020 (abstract_weighted), src-ibd-021 (abstract_weighted), src-ibd-023 (abstract_weighted), src-ibd-024 (abstract_weighted)
- topics/ibd/translation-brief-bilingual.md: src-ibd-005 (abstract_weighted), src-ibd-021 (abstract_weighted)
- topics/ibd/translation-brief.md: src-ibd-005 (abstract_weighted), src-ibd-021 (abstract_weighted)
- topics/ibd/treatment-evidence-bilingual.md: src-ibd-005 (abstract_weighted), src-ibd-021 (abstract_weighted)

## Next Actions

- Run live acceptance once `OPENROUTER_API_KEY` or `ANTHROPIC_API_KEY` is present.
