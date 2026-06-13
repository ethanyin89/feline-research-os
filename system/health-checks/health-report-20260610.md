---
id: system-health-report-20260610
type: health-check
topic: operating-system
question_type: health
language: bilingual
last_compiled_at: 2026-06-10
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: needs_attention
---

# Vault Health Report, 2026-06-10

This report aggregates existing checks. It does not call an LLM and does not replace human review.

## Summary

| Check | Status | Read |
|---|---|---|
| Markdown links | FAIL | FAIL: 2 markdown link issue(s) found. |
| Query tests | PASS | 111 passed  \|  0 failed  \|  111 total |
| Ordinary-user vault eval | FAIL | - 猫癌症是什么: sources, answer_quality |
| Paper source cards | PASS | 541 strict disease paper cards; baseline >= 246 |
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
| Thin source usage | WARN | 7 reader/high-visibility pages use abstract-weighted or title-only sources |
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
| Compile trigger | PASS | 12 changed source cards, 45 downstream files |
| API keys | WARN | no API keys in current shell |

## Source Card Reality

| Disease | Cards | extraction_depth | verification_status |
|---|---:|---|---|
| ckd | 50 | abstract_full: 2, full: 28, partial: 20 | abstract_weighted: 19, deep_extracted: 28, source_checked: 2, title_only: 1 |
| fip | 28 | full: 26, partial: 2 | abstract_weighted: 2, deep_extracted: 26 |
| hcm | 24 | full: 24 | deep_extracted: 24 |
| ibd | 24 | full: 24 | deep_extracted: 24 |
| diabetes | 118 | full: 24, partial: 94 | abstract_weighted: 86, deep_extracted: 24, title_only: 8 |
| fcv | 103 | full: 24, partial: 79 | abstract_weighted: 79, deep_extracted: 24 |
| obesity | 92 | abstract_full: 1, full: 4, partial: 87 | abstract_weighted: 80, deep_extracted: 4, source_checked: 1, title_only: 7 |
| cancer | 102 | abstract: 33, deep: 50, full: 18, partial: 1 | abstract_weighted: 80, deep_extracted: 18, publisher_verified: 1, source_checked: 2, title_only: 1 |

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

## Thin Source Usage

`abstract_weighted` and `title_only` sources can support cautious synthesis, but should not be read as full-text or decision-grade proof.
- topics/cancer/current-state-dashboard.md: src-cancer-052 (abstract_weighted), src-cancer-055 (abstract_weighted), src-cancer-060 (abstract_weighted), src-cancer-064 (abstract_weighted)
- topics/cancer/injection-site-sarcoma.md: src-cancer-047 (abstract_weighted)
- topics/cancer/lymphoma.md: src-cancer-065 (abstract_weighted), src-cancer-048 (abstract_weighted), src-cancer-075 (abstract_weighted), src-cancer-029 (abstract_weighted), src-cancer-018 (abstract_weighted), src-cancer-026 (abstract_weighted), src-cancer-042 (abstract_weighted), src-cancer-044 (abstract_weighted), src-cancer-060 (abstract_weighted), src-cancer-084 (abstract_weighted), src-cancer-086 (abstract_weighted), src-cancer-102 (abstract_weighted)
- topics/cancer/mammary-carcinoma.md: src-cancer-009 (abstract_weighted), src-cancer-012 (abstract_weighted), src-cancer-025 (abstract_weighted), src-cancer-015 (abstract_weighted), src-cancer-022 (abstract_weighted), src-cancer-028 (abstract_weighted), src-cancer-013 (abstract_weighted), src-cancer-005 (abstract_weighted), src-cancer-016 (abstract_weighted), src-cancer-017 (abstract_weighted), src-cancer-020 (abstract_weighted), src-cancer-034 (abstract_weighted), src-cancer-036 (abstract_weighted), src-cancer-038 (abstract_weighted), src-cancer-041 (abstract_weighted), src-cancer-043 (abstract_weighted), src-cancer-045 (abstract_weighted), src-cancer-049 (abstract_weighted), src-cancer-050 (abstract_weighted), src-cancer-052 (abstract_weighted), src-cancer-069 (abstract_weighted), src-cancer-081 (abstract_weighted), src-cancer-090 (abstract_weighted), src-cancer-091 (abstract_weighted), src-cancer-100 (abstract_weighted), src-cancer-101 (abstract_weighted)
- topics/cancer/oral-squamous-cell-carcinoma.md: src-cancer-046 (abstract_weighted), src-cancer-031 (abstract_weighted), src-cancer-055 (abstract_weighted), src-cancer-071 (abstract_weighted), src-cancer-073 (abstract_weighted), src-cancer-074 (abstract_weighted), src-cancer-080 (abstract_weighted)
- topics/cancer/registry-and-prevalence.md: src-cancer-007 (abstract_weighted), src-cancer-064 (abstract_weighted)
- topics/fip/index.md: src-fip-025 (abstract_weighted), src-fip-027 (abstract_weighted)

## Next Actions

- Run live acceptance once `OPENROUTER_API_KEY` or `ANTHROPIC_API_KEY` is present.
- Fix `scripts/ordinary_user_vault_eval.py` failures before trusting the public ordinary-user surface.

## Link Check Output

```text
/Users/jiawei/Desktop/insclaude/feline-research-os/.claude/skills/cancer-deep-extract.md:133: missing target: ../../system/indexes/{source-id}-deep-extraction-round1.md
/Users/jiawei/Desktop/insclaude/feline-research-os/.claude/skills/cancer-topic-update.md:63: missing target: ../../system/indexes/{source-id}-deep-extraction-round1.md

FAIL: 2 markdown link issue(s) found.
```

## Ordinary-User Vault Eval Output

```text
# Ordinary User Vault Eval

## 解释CKD
- status: FAIL
- disease: ckd
- mode: local_explanation
- surface: ckd_overview
- sources: 4
- cited_sources: 4
- sections: 7
- quality_missing: 猫 CKD/慢性肾脏疾病, 怎么发现/判断/recognized, USG/尿比重, UPCR/蛋白尿, renal diet/肾脏专用饮食, 不能/Do not, Wikipedia/维基百科, 下一步/Next Step
- first_line: 这是本地 vault 的猫慢性肾病解释，不是 API 综合回答；本次没有调用 API。 [inference]

## the explanation of feline CKD
- status: FAIL
- disease: ckd
- mode: local_explanation
- surface: ckd_overview
- sources: 5
- cited_sources: 4
- sections: 7
- quality_missing: Researcher Lens, How It Is Recognized, USG, SDMA, Do Not Overstate, Wikipedia, Next Step
- first_line: This is a local vault CKD explanation, not API synthesis. No API call was made. [inference]

## current understanding of feline CKD
- status: FAIL
- disease: ckd
- mode: local_explanation
- surface: ckd_researcher_overview
- sources: 25
- cited_sources: 11
- sections: 8
- quality_missing: Researcher Lens, How It Is Recognized, Do Not Overstate, Next Step
- first_line: This is a local vault CKD researcher overview, not API synthesis. No API call was made. [llm_inference]

## what should a researcher know about feline CKD
- status: FAIL
- disease: ckd
- mode: local_explanation
- surface: ckd_researcher_overview
- sources: 25
- cited_sources: 11
- sections: 8
- quality_missing: Researcher Lens, diagnostic markers, prognostic markers, Do Not Overstate, Next Step
- first_line: This is a local vault CKD researcher overview, not API synthesis. No API call was made. [llm_inference]

## FIP怎么识别
- status: FAIL
- disease: fip
- mode: local_explanation
- surface: fip_recognition
- sources: 3
- cited_sources: 3
- sections: 3
- quality_missing: 不能靠一个症状/one-symptom/one-test, effusive/non-effusive, 诊断/diagnostic
- first_line: 这是本地 vault 的 FIP 识别解释，不是 API 综合回答；本次没有调用 API。 [inference]

## current understanding of feline FIP
- status: FAIL
- disease: fip
- mode: local_explanation
- surface: fip_overview
- sources: 3
- cited_sources: 3
- sections: 6
- quality_missing: Researcher Lens, decision model, diagnostic uncertainty, Do Not Overstate
- first_line: This is a local FIP overview, not API synthesis. No API call was made. [inference]

## what should a researcher know about feline FIP
- status: FAIL
- disease: fip
- mode: local_explanation
- surface: fip_overview
- sources: 3
- cited_sources: 3
- sections: 6
- quality_missing: Researcher Lens, presentation, testing, treatment timing, ocular
- first_line: This is a local FIP overview, not API synthesis. No API call was made. [inference]

## feline FIP disease model overview
- status: FAIL
- disease: fip
- mode: local_explanation
- surface: fip_overview
- sources: 3
- cited_sources: 3
- sections: 6
- quality_missing: disease form, diagnostic-test boundaries, antiviral-era actionability, Do Not Overstate
- first_line: This is a local FIP overview, not API synthesis. No API call was made. [inference]

## HCM是什么，为什么危险
- status: FAIL
- disease: hcm
- mode: local_explanation
- surface: hcm_overview
- sources: 4
- cited_sources: 4
- sections: 7
- quality_missing: 为什么危险/Why It Is Risky, 不能/should not, 下一步/Next Step
- first_line: 这是本地 vault 的猫心肌病解释，不是 API 综合回答；本次没有调用 API。 [inference]

## what should a researcher know about feline HCM
- status: FAIL
- disease: hcm
- mode: local_explanation
- surface: hcm_overview
- sources: 4
- cited_sources: 4
- sections: 7
- quality_missing: Researcher Lens, structural phenotype, AI screening, genotype, treatment evidence, intervention hierarchy, Next Step
- first_line: This is a local vault HCM explanation, not API synthesis. No API call was made. [inference]

## current understanding of feline HCM
- status: FAIL
- disease: hcm
- mode: local_explanation
- surface: hcm_overview
- sources: 4
- cited_sources: 4
- sections: 7
- quality_missing: Researcher Lens, phenotype definition, remodeling, Why It Is Risky, Next Step
- first_line: This is a local vault HCM explanation, not API synthesis. No API call was made. [inference]

## IBD和淋巴瘤怎么区
... clipped ...
```
