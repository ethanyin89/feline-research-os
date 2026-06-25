# Deep Extraction Batch Inventory - 2026-06-25

Purpose: reconcile the user's two Desktop deep-extract batches with the current repository state and the product requirement that every key generated judgment must trace back to a specific supporting passage.

Important correction: an earlier inventory mixed repository output layers with the user's batch definitions. The correct user-defined batches are:

- Batch 1: 8 diabetes model / endpoint / mechanism papers.
- Batch 2: 9 diabetes guideline / remission / treatment papers.

## Core Handling Requirement

These materials should not be treated as generic summaries. The explicit content requirement is:

> Every key judgment in generated content must be able to jump back to the original source and locate the exact paragraph supporting that judgment.

For Feline Research OS, this means each completed material should eventually support claim-level evidence trace:

- `claim`: the generated key judgment.
- `evidence_type`: `direct_source`, `source_supported`, or `analysis_inference`.
- `source_passages`: original passage text, source title/link, section or paragraph location, and highlight text.
- `why_it_supports`: why this passage supports the claim.

Current repository outputs are therefore classified separately:

- `raw deep extraction`: a deep-extraction artifact exists under `raw/deep-extractions/`.
- `worksheet`: a structured abstract or deep-extraction worksheet exists under `system/indexes/`.
- `gold paper card`: a paper card exists under `outputs/gold_standards/diabetes_model_endpoints/paper_cards/`.
- `source-card linked`: the source card has `local_assets` pointing to the deep-extraction artifact.
- `claim-level trace ready`: the source has at least one `source_passages` entry that can feed UI evidence trace; full batch coverage still requires a later pass.

## Batch 1: User-Defined First Batch, 8 Papers

Status summary: all 8 now have linked `raw/deep-extractions/` artifacts. Seven also remain represented through the diabetes model endpoint gold-standard package. None should be considered fully claim-level trace ready until source passages are normalized.

| # | Source | Title | Current repository representation | Current gap |
|---|---|---|---|---|
| 1 | `src-diabetes-025` | Feline Diabetes Is Associated with Deficits in Markers of Insulin Signaling in Peripheral Tissues | `raw/deep-extractions/ext-src-diabetes-025.md`; source card is `full/deep_extracted`; `local_assets` linked | initial `source_passages` added; expand trace coverage |
| 2 | `src-diabetes-003` | Feline Models of Type 2 Diabetes Mellitus | `raw/deep-extractions/ext-src-diabetes-003.md`; gold paper card `feline_models_t2dm_henson.md`; source card is `full/deep_extracted`; `local_assets` linked | needs passage-level trace extraction |
| 3 | `src-diabetes-040` / duplicate newer card `src-diabetes-121` | The Cat as a Model for Human Obesity and Diabetes | `raw/deep-extractions/ext-src-diabetes-040.md`; gold paper card `cat_as_model_for_human_obesity.md`; source card is `full/deep_extracted`; `local_assets` linked | duplicate source IDs and passage-level trace need normalization |
| 4 | `src-diabetes-055` | Insulin sensitivity in normal and diabetic cats | `raw/deep-extractions/ext-src-diabetes-055.md`; gold paper card `insulin_sensitivity_normal_diabetic.md`; source card is `full/deep_extracted`; `local_assets` linked | needs passage-level trace extraction |
| 5 | `src-diabetes-039` | Clinical usefulness of fructosamine measurements in diagnosing and monitoring feline diabetes mellitus | `raw/deep-extractions/ext-src-diabetes-039.md`; gold paper card `clinical_usefulness_fructosamine.md`; source card is `full/deep_extracted`; `local_assets` linked | needs passage-level trace extraction |
| 6 | `src-diabetes-069` | Point-of-care beta-hydroxybutyrate measurement for the diagnosis of feline diabetic ketoacidaemia | `raw/deep-extractions/ext-src-diabetes-069.md`; gold paper card `poc_bhb_dka.md`; source card is `full/deep_extracted`; `local_assets` linked | needs passage-level trace extraction |
| 7 | `src-diabetes-113` | Evaluation of routine hematology profile results and fructosamine, thyroxine, insulin, and proinsulin concentrations in lean, overweight, obese, and diabetic cats | `raw/deep-extractions/ext-src-diabetes-113.md`; gold paper card `eval_routine_hematology_fructosamine.md`; source card is `full/deep_extracted`; `local_assets` linked | needs passage-level trace extraction |
| 8 | `src-diabetes-086` | Routine kidney variables, glomerular filtration rate and urinary cystatin C in cats with diabetes mellitus, cats with chronic kidney disease and healthy cats | `raw/deep-extractions/ext-src-diabetes-086.md`; gold paper card `routine_kidney_variables.md`; source card is `full/deep_extracted`; `local_assets` linked | needs passage-level trace extraction |

Batch 1 supporting package:

- `outputs/gold_standards/diabetes_model_endpoints/evidence_map.md`
- `outputs/gold_standards/diabetes_model_endpoints/endpoint_selection_guide.md`
- `outputs/gold_standards/diabetes_model_endpoints/protocol_reference.md`
- `outputs/gold_standards/diabetes_model_endpoints/research_workspace_gold.md`

## Batch 2: User-Defined Second Batch, 9 Papers

Status summary: all 9 now have linked `raw/deep-extractions/` artifacts. The prior gap for the two guideline papers and remission systematic review has been normalized.

| # | Source | Title | Current repository representation | Current gap |
|---|---|---|---|---|
| 1 | `src-diabetes-050` | ISFM Consensus Guidelines on the Practical Management of Diabetes Mellitus in Cats | `raw/deep-extractions/ext-src-diabetes-050.md`; source card is `full/deep_extracted`; `local_assets` linked | initial `source_passages` added; expand trace coverage |
| 2 | `src-diabetes-087` | 2018 AAHA Diabetes Management Guidelines for Dogs and Cats | `raw/deep-extractions/ext-src-diabetes-087.md`; source card is `full/deep_extracted`; `local_assets` linked | needs passage-level trace extraction |
| 3 | `src-diabetes-007` | Systematic review of feline diabetic remission: Separating fact from opinion | `raw/deep-extractions/ext-src-diabetes-007.md`; source card is `full/deep_extracted`; `local_assets` linked | needs passage-level trace extraction |
| 4 | `src-diabetes-054` | Predictors of clinical remission in cats with diabetes mellitus | `raw/deep-extractions/ext-src-diabetes-zini-2010-remission-predictors.md`; source card is `full/deep_extracted`; `local_assets` linked | needs passage-level trace extraction |
| 5 | `src-diabetes-091` | Survival, remission, and quality of life in diabetic cats | `raw/deep-extractions/ext-src-diabetes-rothlin-2023-survival-qol.md`; source card is `full/deep_extracted`; `local_assets` linked | needs passage-level trace extraction |
| 6 | `src-diabetes-111` | Treatment of newly diagnosed diabetic cats with glargine insulin improves glycaemic control and results in higher probability of remission than protamine zinc and lente insulins | `raw/deep-extractions/ext-src-diabetes-marshall-2009-glargine.md`; source card is `full/deep_extracted`; `local_assets` linked | needs passage-level trace extraction |
| 7 | `src-diabetes-024` | Insulin glargine 300 U/ml for the treatment of feline diabetes mellitus | `raw/deep-extractions/ext-src-diabetes-024.md`; source card is `full/deep_extracted`; `local_assets` linked | needs passage-level trace extraction |
| 8 | `src-diabetes-035` | Velagliflozin, a once-daily, liquid, oral SGLT2 inhibitor, is effective as a stand-alone therapy for feline diabetes mellitus: the SENSATION study | `raw/deep-extractions/ext-src-diabetes-035.md`; source card is `full/deep_extracted`; `local_assets` linked | initial `source_passages` added; expand trace coverage |
| 9 | `src-diabetes-011` | SGLT2 inhibitor use in the management of feline diabetes mellitus | `raw/deep-extractions/ext-src-diabetes-011.md`; source card is `full/deep_extracted`; `local_assets` linked | needs passage-level trace extraction |

## Corrected Progress View

Across the user's 17 named materials:

- Material represented in repo: 17/17.
- Raw deep-extraction artifact exists: 17/17.
- Gold-standard paper card exists: 7/17, all from Batch 1 except Patra 2024.
- Source card currently linked to a raw artifact: 17/17.
- Claim-level source-passage trace ready: 3/17 with initial passage-library coverage (`src-diabetes-025`, `src-diabetes-035`, `src-diabetes-050`).

This means the remaining work is no longer "deep extract or not." The real remaining work is expanding passage-level traceability from the 3-source pilot to all 17 materials.

## Recommended Next Pass

Do this before writing new synthesis content:

1. Expand passage-level evidence trace:
   - For each key claim used in research output, create source passage entries with title, URL/DOI, section or paragraph location, highlighted text, and why the passage supports the claim.
   - Use evidence labels consistently: `direct_source`, `source_supported`, and `analysis_inference`.

2. Resolve duplicate identities:
   - `The Cat as a Model for Human Obesity and Diabetes`: `src-diabetes-040` vs `src-diabetes-121`.
   - Patra 2024: `src-diabetes-025` vs `src-diabetes-120` in later manifests.

3. Only after passage trace, use these batches for a high-confidence Research Workspace answer or endpoint synthesis.
