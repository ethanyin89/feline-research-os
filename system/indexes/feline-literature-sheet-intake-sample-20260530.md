---
id: feline-literature-sheet-intake-sample-20260530
type: system
topic: content-pipeline
question_type: intake-sample
language: zh
last_compiled_at: 2026-05-30
verification_status: sampled
decision_grade: no
owner: codex
status: pending-approval
---

# Feline Literature Sheet Intake Sample, 2026-05-30

## Classification

按 `$autoplan` 路由判断，这件事属于：

`检查 + 内容处理流程`

不是新产品想法，不是实现方案评审，也不是 bug 排查。实际任务是把用户增补的 Google Sheet 文献清单对齐到现有 vault：先读表、去重、判断是否已有 source card，再决定是否进入 first-pass ingest。

本次只做 intake sample 和 manifest。未批量创建 evidence-bearing source cards。

## Project Memory Read

已读取：

- `~/.gstack/projects/feline-research-os/learnings.jsonl`
- `system/indexes/source-processing-ledger-120-20260421.md`
- `system/indexes/disease-module-bootstrap-workflow.md`
- `system/indexes/source-hierarchy-and-claim-fit-policy.md`
- existing disease source indexes / depth maps by local scan

应用规则：

| Rule | Applied Decision |
|---|---|
| 先 source index / manifest，再 densification | 本次先生成 intake manifest，不直接 deep extraction。 |
| 3-10 row sample gate | 本页手动抽样 10 行，覆盖 existing、shared-existing、new module、false-positive risk。 |
| Source hierarchy | guideline/review/backbone/control source 才可能进入 selective deep extraction；普通 study 默认 first-pass。 |
| No cron by default | Sheet 是事件驱动增补队列，还不是定时同步源。 |

## Sheet Inventory

Source sheet:

- Spreadsheet title: `feline-research-os`
- Spreadsheet id: `1Y-MSR39kW5F5J4OedcctdeHk0jhe1mbyvsK43Fcc7lk`
- URL: `https://docs.google.com/spreadsheets/d/1Y-MSR39kW5F5J4OedcctdeHk0jhe1mbyvsK43Fcc7lk/edit`

Observed tabs:

| Tab | Non-empty rows | Current vault state | Interpretation |
|---|---:|---|---|
| `feline diabetes & obesity` | 227 | `src-diabetes-001..118`, `src-obesity-001..087` exist | Already represented. Refresh manifest should mostly classify as existing/shared. |
| `feline FCV` | 24 | `src-fcv-001..024` exist | Existing FCV seed set, no new card creation. |
| `feline cancer` | 111 | no `src-cancer-*` cards | New candidate module, but needs scope filtering before source cards. |

## Manual Sample, 10 Rows

| Tab | Row | Title | Locator | Sample Decision | Rationale |
|---|---:|---|---|---|---|
| diabetes & obesity | 1 | Pathogenesis of Feline Diabetes | ScienceDirect URL | Existing: `src-diabetes-001` | Seed row already represented. No new card. |
| diabetes & obesity | 5 | Feline comorbidities: Pathophysiology and management of the obese diabetic cat | `10.1177/1098612X211021540` | Existing/shared: `src-diabetes-005` | Diabetes-obesity bridge already exists. Do not duplicate evidence text. |
| diabetes & obesity | 136 old-sheet equivalent | Feline obesity - prevalence, risk factors, pathogenesis, associated conditions and assessment: a review | `10.17221/145/2015-VETMED` | Existing: `src-obesity-001` | Obesity Tier A review already bootstrapped. |
| FCV | 1 | An Update on Feline Calicivirus | `10.17236/SAT00346` | Existing: `src-fcv-001` | Matches existing FCV source card. |
| FCV | 4 | Feline Calicivirus Infection: ABCD Guidelines on Prevention and Management | Sage URL / DOI in URL | Existing: `src-fcv-004` | Guideline card exists and has round-1 worksheet. |
| FCV | 18 | Identification of prevalent Feline Calicivirus strains and novel antiviral efficacy of CpG49 stimulus in Feline Calicivirus-infected cats | PubMed URL | Existing: `src-fcv-018` | Existing FCV card. Could later be source-checked, but not a new intake item. |
| cancer | 1 | Feline Oncogenomics: What Do We Know about the Genetics of Cancer in Domestic Cats? | MDPI URL | New cancer candidate | Broad genetics/oncology review. Good shell candidate if cancer becomes a first-class module. |
| cancer | 2 | A prospective investigation of the prevalence and prognostic significance of weight loss and changes in body condition in feline cancer patients | Sage URL | Shared-existing: `src-obesity-085` | Existing obesity card already owns body-condition/cancer cachexia bridge. Cross-link, do not duplicate blindly. |
| cancer | 9 | The Histologic Classification of 602 Cases of Feline Lymphoproliferative Disease using the National Cancer Institute Working Formulation | Sage URL | New cancer candidate | Likely lymphoma-side anchor. Claim-fit should be disease-form/pathology, not modern universal treatment authority. |
| cancer | 20 | Letrozole + ribociclib versus letrozole + placebo as neoadjuvant therapy for ER+ breast cancer (FELINE trial). | ASCO DOI | Out-of-scope risk | `FELINE` appears to be a human oncology trial acronym, not feline cat evidence. Needs exclusion review before ingest. |

## Proposed Durable Workflow

This is now a repeatable event-driven intake path:

1. Read Google Sheet metadata and export each tab to CSV.
2. For each tab, record exact row count and title/locator columns.
3. Run 3-10 row manual sample covering existing, shared-existing, new candidate, duplicate, and out-of-scope risk.
4. Generate a reviewable manifest with `scripts/literature_sheet_intake.py`.
5. Review `new-*`, `shared-existing`, `duplicate-in-sheet`, and likely out-of-scope rows before any source-card writes.
6. If source cards are approved, write only first-pass cards first.
7. Run metadata / abstract availability sample before broader source-check.
8. Select deep extraction only for guideline, broad review, backbone mechanism, treatment-control, or high-reuse boundary sources.

## Current Decision

- `diabetes & obesity`: refresh manifest only. No new card creation expected.
- `FCV`: refresh manifest only. No new card creation expected.
- `cancer`: treat as a new candidate disease/module queue, not as approved source-card work yet.
- Cron: no. This is event-driven sheet intake, not a scheduled living queue.

## Approval Gate

Before source-card creation or skill-file hardening, confirm:

1. Should `feline cancer` become a first-class disease/module namespace with `src-cancer-*`?
2. Should cancer row 20 and similar acronym/false-positive rows be excluded before manifest-to-card conversion?
3. Should shared rows, such as `src-obesity-085`, stay as cross-links instead of duplicate cancer cards?
