---
id: feline-diabetes-obesity-sheet-intake-sample-20260513
type: system
topic: content-pipeline
question_type: intake-sample
language: zh
last_compiled_at: 2026-05-13
verification_status: sampled
decision_grade: no
owner: codex
status: pending-approval
---

# Feline Diabetes / Obesity Sheet Intake Sample, 2026-05-13

## Classification

按 `$autoplan` 的路由判断，这件事属于：

`检查 + 内容处理流程`

它不是新想法，不是单纯方案评审，也不是 bug 排查。实际任务是把用户提供的 Google Sheet 文献清单对齐到现有 vault 规则：先去重、判定旧有来源、分配新 source owner，再决定哪些进入 first-pass ingest、哪些只作为 cross-link 或 later deep extraction。

## Project Memory Read

已读取 `~/.gstack/projects/feline-research-os/learnings.jsonl`。本次相关经验：

| Key | Applied Rule |
|---|---|
| `karpathy-gap-order` | 先做 source-depth/source-index，再做 densification。 |
| `image-ingest-gate` | 图像和表格材料不能直接当证据，必须等 human label verification。 |
| `research-lite-output-mode` | 面向普通用户时保留 provenance，但输出面不用技术脚注泛滥。 |

已读取现有 owner：

- `system/indexes/source-processing-ledger-120-20260421.md`
- `system/indexes/disease-module-bootstrap-workflow.md`
- `system/indexes/deep-extraction-workflow.md`
- `system/indexes/source-hierarchy-and-claim-fit-policy.md`
- `system/indexes/diabetes-source-index.md`
- `system/indexes/diabetes-obesity-body-condition-memo.md`
- `topics/diabetes/obesity-and-body-condition.md`

## Sheet Inventory

Source sheet:

- Spreadsheet: `feline diabetes & obesity`
- Spreadsheet id: `1Y-MSR39kW5F5J4OedcctdeHk0jhe1mbyvsK43Fcc7lk`
- Sheet tab: `工作表1`
- Range read: `A1:B1000`

Observed structure:

| Segment | Rows | Interpretation |
|---|---:|---|
| First diabetes seed block | 1-24 | Existing 24 diabetes references already represented as `src-diabetes-001` through `src-diabetes-024`. |
| Blank separator | 25 | Ignore. |
| Extended diabetes block | 26-130 | Mixed duplicate + new diabetes / diabetes-obesity references. |
| Blank separator | 131-132 | Ignore. |
| Obesity marker | 133 | Section label, not a source. |
| Obesity block | 134-230 | New obesity corpus, with some diabetes/shared-source overlaps. |

Non-empty rows: `227`.

## Manual Sample, 10 Rows

This is the required 3-10 item manual pass before codifying a reusable workflow. No source cards were bulk-created in this pass.

| Sheet Row | Title | DOI / URL | Sample Decision | Rationale |
|---:|---|---|---|---|
| 1 | Pathogenesis of Feline Diabetes | ScienceDirect URL | Existing: `src-diabetes-001` | First 24-row seed block already closed in the 120-source ledger. No new card. |
| 5 | Feline comorbidities: Pathophysiology and management of the obese diabetic cat | `10.1177/1098612X211021540` | Existing: `src-diabetes-005`; also obesity bridge | Already deep-extracted and currently owns diabetes obesity/body-condition logic. Do not duplicate blindly. |
| 26 | Feline Diabetes mellitus | `10.1177/1098612X14523187` | Duplicate: `src-diabetes-014` | Same title/DOI as seed row 14. No new source. |
| 27 | Feline Diabetes Is Associated with Deficits in Markers of Insulin Signaling in Peripheral Tissues | `10.3390/IJMS252313195` | New diabetes candidate | Mechanism / insulin-signaling source. Proposed first-pass slot after existing corpus, not deep extraction by default. |
| 33 | Current Understanding of Feline Diabetes: Part 2, Treatment | `10.1053/JFMS.2000.0057` | New diabetes candidate | Treatment architecture source. Likely useful for historical treatment framing; current recommendations must be controlled by newer guidelines/labels. |
| 47 | Velagliflozin, a once-daily, liquid, oral SGLT2 inhibitor, is effective as a stand-alone therapy for feline diabetes mellitus: the SENSATION study | `10.2460/JAVMA.24.03.0174` | New diabetes high-priority candidate | SGLT2 treatment study. Needs label/FOI boundary control before any treatment-ranking language. |
| 62 | ISFM Consensus Guidelines on the Practical Management of Diabetes Mellitus in Cats | `10.1177/1098612X15571880` | New diabetes high-priority candidate | Guideline/practice architecture source. Strong candidate for selective deep extraction after first-pass ingest. |
| 134 | Canine and Feline Obesity Management | `10.1016/J.CVSM.2021.01.005` | New obesity candidate | Broad management review. Useful for obesity module shell, but cross-species scope must be bounded. |
| 136 | Feline obesity - prevalence, risk factors, pathogenesis, associated conditions and assessment: a review | `10.17221/145/2015-VETMED` | New obesity Tier A candidate | Feline-specific broad review. Likely source-index Tier A for obesity bootstrap. |
| 137 | Feline comorbidities: Pathophysiology and management of the obese diabetic cat | `10.1177/1098612X211021540` | Existing shared source: `src-diabetes-005` | Same DOI as row 5. For obesity, create a cross-reference to existing source or a shared-source alias, not a second independent extraction. |

## Proposed Durable Workflow

If approved, codify this as a project source-intake skill instead of repeating manual work:

1. Read spreadsheet metadata and full `A:B` range.
2. Normalize DOI / URL:
   - lowercase DOI
   - strip trailing punctuation
   - resolve DOI-like URLs into DOI when obvious
   - preserve original URL in `links.url`
3. Match against existing `raw/papers/src-*.md` by DOI first, then exact normalized title.
4. Classify rows:
   - `existing`
   - `duplicate-in-sheet`
   - `new-diabetes`
   - `new-obesity`
   - `shared-diabetes-obesity`
   - `section-label`
5. Generate a reviewable intake manifest before writing any source cards.
6. For approved new rows, write first-pass source cards only. Do not deep-extract every source by default.
7. Select deep extraction only for guideline/review/backbone/control sources.
8. Update source index and source-depth map after cards exist.
9. Run health checks after file writes.

Suggested durable files after approval:

- `system/indexes/feline-literature-sheet-intake-workflow.md`
- `system/indexes/feline-diabetes-obesity-intake-manifest-20260513.md`
- optional skill file under the user's approved Codex skill location

## ID Policy Recommendation

Recommended:

- Keep existing diabetes IDs `src-diabetes-001` through `src-diabetes-024`.
- Continue new diabetes references from `src-diabetes-025`.
- Start obesity as its own module with `src-obesity-001`.
- For shared sources already present as diabetes cards, do not create duplicate evidence text. Use cross-links and owner notes unless the obesity module needs a distinct source card for a different claim-fit role.

Reason:

The existing vault is disease-module oriented, but duplicate DOI cards create maintenance risk. A shared-source owner note preserves traceability while keeping one evidence interpretation canonical.

## Cron Decision

No cron yet.

This is not a scheduled ingestion job. It is event-driven: user provides or updates a sheet. Cron would add noise unless the sheet becomes a living intake queue with frequent updates.

## Approval Gate

Before codifying:

1. Confirm whether obesity should become a first-class `topics/obesity/` module.
2. Confirm whether shared diabetes-obesity sources should be cross-linked to existing diabetes cards instead of duplicated as obesity cards.
3. Confirm whether the next pass should generate a full intake manifest only, or also create first-pass cards for approved new rows.
