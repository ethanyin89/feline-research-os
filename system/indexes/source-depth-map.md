---
id: source-depth-map
type: index
topic: system
question_type: navigation
language: bilingual
last_compiled_at: 2026-06-20
confidence: high
verification_status: compiled
owner: codex
status: active
---

# Source Depth Map — Multi-Disease

## 用途 / How to Use

**为了快速找到该深挖哪些 source card：** 先看 disease-level reality，再看 disease-specific queue。
**为了在 context 有限时决定先读哪张：** 先读 status/depth 都明确的 source cards；缺字段时读对应 round-1 worksheet。
**为了指导下一步 linting/densification 工作：** 先修 schema/state drift，再做新的 content densification。

Load this when deciding which source cards to prioritize under context limits.

2026-06-20 reality sync:

- The vault now has `1414` strict disease paper source cards across CKD, FIP, HCM,
  IBD, Diabetes, FCV, and obesity.
- CKD now has its original `24` full seed cards plus `26` partial extension intake
  cards from the user-provided `feline CKD` Google Sheet. Use
  [ckd-source-index.md](ckd-source-index.md).
- The old user-confirmed seed scope was 5 disease modules x 24 paper sources:
  [120 source processing ledger](source-processing-ledger-120-20260421.md). That
  seed scope remains fully explicit at source-card depth.
- The old user-facing `96` scope is tracked separately as CKD / FIP / HCM / IBD:
  [legacy 96 source processing ledger](legacy-96-source-processing-ledger-20260421.md).
- FCV has joined the explicit full-depth seed set: `24/24` source cards are
  `full` and `deep_extracted`. Use [fcv-source-depth-map.md](fcv-source-depth-map.md).
- Diabetes now has a `24`-card full seed corpus plus `94` partial extension cards.
  Use [diabetes-source-depth-map.md](diabetes-source-depth-map.md).
- Obesity now has `87` partial source cards and no decision-grade deep-extracted
  cards. Use [obesity-source-depth-map.md](obesity-source-depth-map.md).
- `status:` and `extraction_depth:` are different fields. Missing `extraction_depth`
  is schema debt, not proof that the card was never processed.
- FIP is `24/24` explicit `full` at source-card layer after the 2026-04-22
  thickening pass. Use [fip-source-depth-map.md](fip-source-depth-map.md).
- IBD is `24/24` explicit `full` at source-card layer after the 2026-04-23
  `src-ibd-009` source-check pass. Use [ibd-source-depth-map.md](ibd-source-depth-map.md).

Depth definitions:

- **full**: source card explicitly says `extraction_depth: full`
- **partial**: source card explicitly says `extraction_depth: partial`
- **missing depth**: source card has no `extraction_depth` field; read the round-1
  worksheet before treating it as shallow
- **stub**: source card is still `status: ingested` or explicitly extraction-incomplete

Verification-status read:

- **deep_extracted**: card has explicit full-depth source-card write-back and is marked as deep extracted
- **source_checked**: source page or source text was checked directly for the relevant card-level claims
- **abstract_weighted**: card is reusable at source-card depth, but its strongest details are still abstract-led rather than full-text compressed
- **title_only**: card is usable only as orientation until source detail is recovered
- **missing**: older source card predates this frontmatter field; do not treat as shallow, but backfill before using as a decision-grade anchor

---

## 2026-06-20 Cross-Disease Snapshot

| Disease | Source cards | Status reality | Explicit full | Explicit partial | Missing depth field | Worksheets | Verification-status overlay | Current read |
|---|---|---|---|---|---|---|---|---|
| CKD | 197 | `51 abstract_weighted, 35 deep_extracted, 2 source_checked, 109 title_only` | 37 | 160 | 0 | 24 seed worksheets plus 31 extension worksheets (25 structured round 1 + 2 abstract round 2 + 4 full-text deep extractions) | `51 abstract_weighted, 35 deep_extracted, 2 source_checked, 109 title_only` | Seed corpus remains mature; full-text extension depth now covers metabolomics, guarded phosphorus intervention, probiotic-pilot boundaries, and a feline fibroblast/TGF-beta model |
| FIP | 242 | `21 abstract_weighted, 30 deep_extracted, 191 title_only` | 30 | 212 | 0 | 24 | `21 abstract_weighted, 30 deep_extracted, 191 title_only` | Separate FIP depth map exists; all source cards now explicit full depth |
| HCM | 226 | `32 deep_extracted, 194 title_only` | 32 | 194 | 0 | 24 | `32 deep_extracted, 194 title_only` | Separate HCM depth map exists; all source cards now explicit full depth and deep-extracted |
| IBD | 126 | `25 deep_extracted, 101 title_only` | 25 | 101 | 0 | 24 | `25 deep_extracted, 101 title_only` | Separate IBD depth map exists; all source cards are explicit full and deep-extracted |
| DIABETES | 121 | `85 abstract_weighted, 28 deep_extracted, 8 title_only` | 29 | 92 | 0 | 24 seed worksheets plus extension structured-abstract worksheets where available | `85 abstract_weighted, 28 deep_extracted, 8 title_only` | Seed corpus is full; extension corpus is navigation/source-check material only, not compiled decision-grade evidence |
| FCV | 296 | `77 abstract_weighted, 26 deep_extracted, 193 title_only` | 26 | 270 | 0 | 24 | `77 abstract_weighted, 26 deep_extracted, 193 title_only` | Separate FCV depth map exists; core source-card layer is full, but image assets and output-level branches remain thinner |
| OBESITY | 95 | `82 abstract_weighted, 5 deep_extracted, 1 source_checked, 7 title_only` | 7 | 88 | 0 | 44 structured-abstract worksheets, 43 title-only cards, 4 deep extraction worksheets | `82 abstract_weighted, 5 deep_extracted, 1 source_checked, 7 title_only` | All 4 Tier 1 priority cards deep-extracted (001, 004, 005, 008); 5-branch architecture complete with 4 pages + 4 bilingual versions |
| CANCER | 111 | `68 abstract_weighted, 35 deep_extracted, 1 publisher_verified, 2 source_checked, 5 title_only` | 73 | 10 | 28 | 29 structured-abstract worksheets, 43 deep extraction worksheets | `68 abstract_weighted, 35 deep_extracted, 1 publisher_verified, 2 source_checked, 5 title_only` | Core oncology branches outlined; most high-visibility cancer sources Triaged and verified |

## Default Next Moves

1. **Obesity:** use [obesity-source-depth-map.md](obesity-source-depth-map.md).
   All `4` Tier 1 priority cards deep-extracted (001, 004, 005, 008). Architecture
   complete: mechanism-overview, risk-and-recognition, prevention, diabetes-bridge
   (all with bilingual versions). Next priority: Tier 2 management context sources
   (src-obesity-080) if intervention detail is needed, or assessment-methods page
   after body condition full-text extraction.
2. **Diabetes:** use [diabetes-source-depth-map.md](diabetes-source-depth-map.md).
   The `24`-card seed corpus is full; the `94`-card extension corpus should stay
   source-check/structured-abstract material until a narrow clinical, regulatory,
   obesity, or output-order question justifies deeper extraction.
3. **FCV:** use [fcv-source-depth-map.md](fcv-source-depth-map.md). The `24`-card
   source layer is full; next gains are field-effectiveness, label/regulatory,
   therapy, image, or output-specific precision.
4. **IBD / FIP / HCM:** use their disease-specific maps. All three are explicit
   full at seed source-card depth, so move only on full-text, official-source,
   image/table, or output-specific precision that changes branch order.
5. **CKD:** seed depth-field cleanup complete as of 2026-04-21. The Google Sheet extension now has 4 `deep_extracted`, 2 `source_checked`, 19 `abstract_weighted`, and 1 `title_only` card. `src-ckd-032` remains the only metadata-depth blocker.

---

## CKD Detail Table — Legacy Template

This section is the original CKD detail table. It remains useful as a mature template,
but its older "full" judgment predates the stricter explicit `extraction_depth` audit
above.

---

## Tier 1 — CRITICAL (stub + high citations)

No CKD source cards remain in `stub` after the 2026-04-11 completion pass.

---

## Tier 2 — PARTIAL (ingested body + incomplete frontmatter)

No CKD source cards remain in `partial` after the 2026-04-11 completion pass.

---

## Tier 3 — FULL (extracted, verbatim data present)

These cards have verbatim quoted facts with numbers in frontmatter evidence_policy.
Read these first under context limits for highest information density.

| Source ID   | Title (short)                                              | Citations | Words | Depth    | Notes |
|------------|-------------------------------------------------------------|-----------|-------|----------|-------|
| src-ckd-004 | ISFM Consensus Guidelines (Diagnosis & Management)         | **93**    | 1370  | **full** | Diagnosis core, serial surveillance, renal-diet and phosphate-binder detail now extracted |
| src-ckd-010 | Histomorphometry and Markers of Renal Dysfunction          | **75**    | 1277  | **full** | Stronger methods detail and lesion-to-endpoint consequence mapping now captured |
| src-ckd-003 | Current Therapies — What Is Achievable?                   | 65        | 1112  | **full** | Treatment hierarchy now bounded: renal diet first, adjuncts separated, benazepril caution added |
| src-ckd-001 | Pathophysiology and Risk Factors                          | 27        | 972   | **full** | Fibrosis-centered mechanism backbone, risk-based screening logic, and complication breadth now extracted |
| src-ckd-002 | Diagnosis, Staging and Screening                          | 25        | 954   | **full** | Routine-diagnosis vs early-detection boundary and GFR-vs-USG operational hierarchy now extracted |
| src-ckd-005 | New Horizons — Where Do We Go From Here?                 | 22        | 1088  | **full** | Early-detection-as-strategy, targeted-screening contexts, and conservative intervention hierarchy now extracted |
| src-ckd-012 | Case-Control Study of Risk Factors Associated with Feline and Canine Chronic Kidney Disease | 19 | 954 | **full** | Owner-observed polyuria/polydipsia recognition layer and missed-earlier-diagnosis signal now extracted |
| src-ckd-008 | Feline chronic kidney disease: Can we move from treatment to prevention? | 13 | 1042 | **full** | Prevention-boundary logic, species-specific caution, and date-bounded hypertension tension now extracted |
| src-ckd-007 | Therapies for Feline Chronic Kidney Disease: What is the Evidence? | 45 | 1162 | **full** | Evidence-grading control source now extracted; weak-evidence branches and UPC thresholds captured |
| src-ckd-006 | Treatment Options for Hyperphosphatemia in Feline CKD: What's Out there? | 44 | 1109 | **full** | Phosphorus bridge logic, PTH hidden-burden note, and diet-first hierarchy now extracted |
| src-ckd-009 | Feline comorbidities: The intermingled relationship between chronic kidney disease and hypertension | 41 | 1040 | **full** | SBP-proteinuria-target-organ junction and implementation-gap logic now extracted |
| src-ckd-011 | Renal fibrosis in feline chronic kidney disease: Known mediators and mechanisms of injury | 40 | 1129 | **full** | Fibrosis backbone, TGF-beta watchlist, and cat-specific mediator ceiling now extracted |
| src-ckd-013 | What outcomes should be measured in feline chronic kidney disease treatment trials? Establishing a core outcome set for research | 35 | 1268 | **full** | Trial-outcome architecture, consensus method, and minimum-breadth boundary now extracted |
| src-ckd-017 | Clinicopathologic and pathologic characteristics of feline proteinuric kidney disease | 32 | 960 | **full** | Proteinuria compartment logic, ICGN prevalence, and UPC-boundary interpretation now extracted |
| src-ckd-018 | Early Detection via 3-hydroxykynurenine + ML               | 33        | 969   | **full** | Best extracted card: AUC 0.844, SVM AUC 0.929, longitudinal cohort data |
| src-ckd-021 | (CKD source #21)                                            | 21        | 832   | **full** | — |
| src-ckd-024 | Renal biomarkers in cats: A review of the current status in chronic kidney disease | 26 | 1084 | **full** | SDMA/GFR/UPC boundary logic and broader biomarker-field expansion now extracted |
| src-ckd-020 | Ultrasonography of the feline kidney: Technique, anatomy and changes associated with disease | 22 | 765 | **full** | Imaging workup realism now extracted without promoting ultrasound into the endpoint core |
| src-ckd-016 | Chronic Kidney Disease in Aged Cats: Clinical Features, Morphology, and Proposed Pathogeneses | 16 | 1145 | **full** | Aged-cat tubulointerstitial natural-history frame and initiation-versus-progression split now extracted |
| src-ckd-022 | Chronic Renal Changes After a Single Ischemic Event in an Experimental Model of Feline Chronic Kidney Disease | 19 | 1086 | **full** | Experimental ischemia model, function-plus-lesion trajectory, and translational bounds now extracted |
| src-ckd-014 | (CKD source #14)                                            | 27        | 795   | **full** | — |
| src-ckd-015 | (CKD source #15)                                            | 28        | 701   | **full** | — |
| src-ckd-019 | (CKD source #19)                                            | 17        | 702   | **full** | — |
| src-ckd-023 | (CKD source #23)                                            | 13        | 739   | **full** | — |

---

## Deepening Priority Queue

Order for next densification passes, based on citation × depth gap:

1. **COMPLETED 2026-04-11:** `src-ckd-004` -> full
2. **COMPLETED 2026-04-11:** `src-ckd-003` -> full
3. **COMPLETED 2026-04-11:** `src-ckd-010` -> full
4. **COMPLETED 2026-04-11:** `src-ckd-007` -> full
5. **COMPLETED 2026-04-11:** `src-ckd-006` -> full
6. **COMPLETED 2026-04-11:** `src-ckd-009` -> full
7. **COMPLETED 2026-04-11:** `src-ckd-011` -> full
8. **COMPLETED 2026-04-11:** `src-ckd-013` -> full
9. **COMPLETED 2026-04-11:** `src-ckd-017` -> full
10. **COMPLETED 2026-04-11:** `src-ckd-024` -> full
11. **COMPLETED 2026-04-11:** `src-ckd-020` -> full
12. **COMPLETED 2026-04-11:** `src-ckd-001` -> full
13. **COMPLETED 2026-04-11:** `src-ckd-002` -> full
14. **COMPLETED 2026-04-11:** `src-ckd-005` -> full
15. **COMPLETED 2026-04-11:** `src-ckd-012` -> full
16. **COMPLETED 2026-04-11:** `src-ckd-008` -> full
17. **COMPLETED 2026-04-11:** `src-ckd-016` -> full
18. **COMPLETED 2026-04-11:** `src-ckd-022` -> full

After deepening these 18, recompile to staging first: `inbox/ckd/mechanism-overview.md`,
`inbox/ckd/endpoint-handbook.md`, `inbox/ckd/model-map.md`,
`inbox/ckd/translation-brief.md`, and `inbox/ckd/early-detection.md`.

---

## Extraction Depth Field

Source cards should have `extraction_depth: full | partial | stub` in frontmatter.
If missing, treat as `stub`. Field should be added during each deepening pass.

---

## Coverage Summary

This summary uses explicit `extraction_depth` fields only. It intentionally does not treat missing fields as `stub`; missing fields are schema debt that must be resolved against the completed worksheets.

| Disease | Total Source Cards | explicit full | explicit partial | missing depth | stub | Coverage read |
|---|---|---|---|---|---|---|
| CKD | 197 | 37 | 160 | 0 | 0 | Seed corpus remains mature; full-text extension depth now covers metabolomics, guarded phosphorus intervention, probiotic-pilot boundaries, and a feline fibroblast/TGF-beta model |
| FIP | 242 | 30 | 212 | 0 | 0 | Separate FIP depth map exists; all source cards now explicit full depth |
| HCM | 226 | 32 | 194 | 0 | 0 | Separate HCM depth map exists; all source cards now explicit full depth and deep-extracted |
| IBD | 126 | 25 | 101 | 0 | 0 | Separate IBD depth map exists; all source cards are explicit full and deep-extracted |
| DIABETES | 121 | 29 | 92 | 0 | 0 | Seed corpus is full; extension corpus is navigation/source-check material only, not compiled decision-grade evidence |
| FCV | 296 | 26 | 270 | 0 | 0 | Separate FCV depth map exists; core source-card layer is full, but image assets and output-level branches remain thinner |
| OBESITY | 95 | 7 | 88 | 0 | 0 | All 4 Tier 1 priority cards deep-extracted (001, 004, 005, 008); 5-branch architecture complete with 4 pages + 4 bilingual versions |
| CANCER | 111 | 73 | 10 | 28 | 0 | Core oncology branches outlined; most high-visibility cancer sources Triaged and verified |

---

## Year Metadata Coverage

| Disease | Year Coverage | Notes |
|---|---|---|
| CKD | 96/197 (48%) | Complete |
| FIP | 82/242 (33%) | Complete |
| HCM | 48/226 (21%) | Complete |
| IBD | 39/126 (30%) | Complete |
| DIABETES | 121/121 (100%) | Complete |
| FCV | 131/296 (44%) | Complete |
| OBESITY | 92/95 (96%) | Complete |
| CANCER | 104/111 (93%) | Complete |

Year metadata enables temporal filtering for recency-weighted extraction priority.

## Maintenance

Recompile this file after each batch of source card deepening.
Update `last_compiled_at` and adjust tier placements as cards move from stub → partial → full.
