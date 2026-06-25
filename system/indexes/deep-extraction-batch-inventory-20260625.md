# Deep Extraction Batch Inventory - 2026-06-25

Purpose: reconcile Desktop deep-extract drafts, repository deep-extraction files, and gold-standard content outputs after the 2026-06-23 to 2026-06-25 diabetes material batches.

## Current Repository State

- Latest content-layer cleanup commit: `469f1c7 docs(health): add health report 2026-06-25`.
- Worktree was clean after committing the health report.
- `HANDOFF-2026-06-24-DIABETES-BATCH2-LITERATURE.md` is now stale for Batch 2 because later commit `f69c486` completed the final 3 Batch 2 files.

## Batch 1: Diabetes Model Endpoint Gold Standard

Status: complete as gold-standard outputs.

Location: `outputs/gold_standards/diabetes_model_endpoints/`

Paper cards:

| Desktop draft | Repository artifact | Status |
|---|---|---|
| Feline Models of Type 2 Diabetes Mellitus | `paper_cards/feline_models_t2dm_henson.md` | complete in gold-standard layer |
| The Cat as a Model for Human Obesity and Diabetes | `paper_cards/cat_as_model_for_human_obesity.md` | complete in gold-standard layer |
| Insulin sensitivity in normal and diabetic cats | `paper_cards/insulin_sensitivity_normal_diabetic.md` | complete in gold-standard layer |
| Clinical usefulness of fructosamine measurements in diagnosing and monitoring feline diabetes mellitus | `paper_cards/clinical_usefulness_fructosamine.md` | complete in gold-standard layer |
| Point-of-care beta-hydroxybutyrate measurement for the diagnosis of feline diabetic ketoacidaemia | `paper_cards/poc_bhb_dka.md` | complete in gold-standard layer |
| Evaluation of routine hematology profile results and fructosamine, thyroxine, insulin, and proinsulin concentrations | `paper_cards/eval_routine_hematology_fructosamine.md` | complete in gold-standard layer |
| Routine kidney variables, glomerular filtration rate and urinary cystatin C in cats with diabetes mellitus | `paper_cards/routine_kidney_variables.md` | complete in gold-standard layer |

Supporting outputs:

- `evidence_map.md`
- `endpoint_selection_guide.md`
- `protocol_reference.md`
- `research_workspace_gold.md`

Note: these were not migrated one-for-one into `raw/deep-extractions/`; they exist as the diabetes model endpoint gold-standard package.

## Batch 2: Diabetes Deep Extractions

Status: complete in `raw/deep-extractions/`.

The 2026-06-24 handoff recorded Batch 2 as 3/6 complete, but later commit `f69c486` completed the remaining 3 files. Actual status is 6/6.

| Source | Title | Deep extraction artifact | Status |
|---|---|---|---|
| `src-diabetes-111` / legacy slug `src-diabetes-marshall-2009` | Treatment of newly diagnosed diabetic cats with glargine insulin improves glycaemic control and results in higher probability of remission than protamine zinc and lente insulins | `raw/deep-extractions/ext-src-diabetes-marshall-2009-glargine.md` | complete |
| `src-diabetes-091` / legacy slug `src-diabetes-rothlin-2023` | Survival, remission, and quality of life in diabetic cats | `raw/deep-extractions/ext-src-diabetes-rothlin-2023-survival-qol.md` | complete |
| `src-diabetes-054` / legacy slug `src-diabetes-zini-2010` | Predictors of clinical remission in cats with diabetes mellitus | `raw/deep-extractions/ext-src-diabetes-zini-2010-remission-predictors.md` | complete |
| `src-diabetes-011` | SGLT2 inhibitor use in the management of feline diabetes mellitus | `raw/deep-extractions/ext-src-diabetes-011.md` | complete |
| `src-diabetes-024` | Insulin glargine 300 U/ml for the treatment of feline diabetes mellitus | `raw/deep-extractions/ext-src-diabetes-024.md` | complete |
| `src-diabetes-035` | Velagliflozin, a once-daily, liquid, oral SGLT2 inhibitor, is effective as a stand-alone therapy for feline diabetes mellitus: the SENSATION study | `raw/deep-extractions/ext-src-diabetes-035.md` | complete |

## Additional Desktop Deep Extracts Already Represented

| Desktop draft | Repository status |
|---|---|
| Feline Diabetes Is Associated with Deficits in Markers of Insulin Signaling in Peripheral Tissues. 2024 | `raw/deep-extractions/ext-src-diabetes-025.md`; source card `raw/papers/src-diabetes-025.md` points to it |
| Left Atrioventricular Coupling Index in Feline Hypertrophic Cardiomyopathy | `raw/deep-extractions/ext-src-hcm-076.md` |
| Prevalence of Hypertrophic Cardiomyopathy and ALMS1 Variant in Sphynx Cats in New Zealand | `raw/deep-extractions/ext-src-hcm-205.md`; duplicate older slug `ext-src-hcm-sphinx.md` also exists |

## True Remaining Gaps From The Desktop Set

These Desktop deep-extract drafts exist, but current source cards do not yet point to a matching `raw/deep-extractions/` artifact:

| Source | Title | Current source-card state | Suggested next action |
|---|---|---|---|
| `src-diabetes-050` | ISFM Consensus Guidelines on the Practical Management of Diabetes Mellitus in Cats | `extraction_depth: partial`, `verification_status: abstract_weighted`, `local_assets: []` | promote Desktop draft into `raw/deep-extractions/` and update source card |
| `src-diabetes-087` | 2018 AAHA Diabetes Management Guidelines for Dogs and Cats | `extraction_depth: partial`, `verification_status: abstract_weighted`, `local_assets: []` | promote Desktop draft into `raw/deep-extractions/` and update source card |

The remission systematic review (`src-diabetes-007`) is already marked `extraction_depth: full` and `verification_status: deep_extracted`, but `local_assets: []`. It has a repository worksheet at `system/indexes/src-diabetes-007-deep-extraction-round1.md`; decide whether to also promote the Desktop draft into `raw/deep-extractions/` for consistency.

## Content-Layer Recommendation

Use a narrow normalization pass before creating new synthesis:

1. Promote `src-diabetes-050` and `src-diabetes-087` from Desktop drafts into `raw/deep-extractions/`.
2. Update both source cards to `extraction_depth: full`, `verification_status: deep_extracted`, and add `local_assets`.
3. Decide whether `src-diabetes-007` should get a `raw/deep-extractions/` mirror or remain represented by its existing worksheet.
4. Remove or ignore duplicate slug artifacts only after checking references; do not delete them during the normalization pass.
