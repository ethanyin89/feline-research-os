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
- `claim-level trace ready`: not yet complete for this batch unless a future pass adds passage-level trace objects.

## Batch 1: User-Defined First Batch, 8 Papers

Status summary: all 8 are represented somewhere in the repo, but only Patra 2024 has a linked `raw/deep-extractions/` artifact. Seven are represented mainly through the diabetes model endpoint gold-standard package. None should be considered fully claim-level trace ready until source passages are normalized.

| # | Source | Title | Current repository representation | Current gap |
|---|---|---|---|---|
| 1 | `src-diabetes-025` | Feline Diabetes Is Associated with Deficits in Markers of Insulin Signaling in Peripheral Tissues | `raw/deep-extractions/ext-src-diabetes-025.md`; source card is `full` and `deep_extracted`; `local_assets` linked | needs passage-level trace extraction |
| 2 | `src-diabetes-003` | Feline Models of Type 2 Diabetes Mellitus | `system/indexes/src-diabetes-003-deep-extraction-round1.md`; gold paper card `feline_models_t2dm_henson.md`; source card is `full` and `deep_extracted` but `local_assets: []` | source-card asset link and passage-level trace missing |
| 3 | `src-diabetes-040` / duplicate newer card `src-diabetes-121` | The Cat as a Model for Human Obesity and Diabetes | gold paper card `cat_as_model_for_human_obesity.md`; structured worksheet exists for `src-diabetes-040`; newer duplicate `src-diabetes-121` is marked `full/deep_extracted` | duplicate source IDs and passage-level trace need normalization |
| 4 | `src-diabetes-055` | Insulin sensitivity in normal and diabetic cats | gold paper card `insulin_sensitivity_normal_diabetic.md`; structured worksheet exists | source card remains `partial/abstract_weighted`; raw deep extraction and trace missing |
| 5 | `src-diabetes-039` | Clinical usefulness of fructosamine measurements in diagnosing and monitoring feline diabetes mellitus | gold paper card `clinical_usefulness_fructosamine.md`; structured worksheet exists | source card remains `partial/abstract_weighted`; raw deep extraction and trace missing |
| 6 | `src-diabetes-069` | Point-of-care beta-hydroxybutyrate measurement for the diagnosis of feline diabetic ketoacidaemia | gold paper card `poc_bhb_dka.md`; structured worksheet exists | source card remains `partial/abstract_weighted`; raw deep extraction and trace missing |
| 7 | `src-diabetes-113` | Evaluation of routine hematology profile results and fructosamine, thyroxine, insulin, and proinsulin concentrations in lean, overweight, obese, and diabetic cats | gold paper card `eval_routine_hematology_fructosamine.md`; structured worksheet exists | source card remains `partial/abstract_weighted`; raw deep extraction and trace missing |
| 8 | `src-diabetes-086` | Routine kidney variables, glomerular filtration rate and urinary cystatin C in cats with diabetes mellitus, cats with chronic kidney disease and healthy cats | gold paper card `routine_kidney_variables.md`; structured worksheet exists | source card remains `partial/abstract_weighted`; raw deep extraction and trace missing |

Batch 1 supporting package:

- `outputs/gold_standards/diabetes_model_endpoints/evidence_map.md`
- `outputs/gold_standards/diabetes_model_endpoints/endpoint_selection_guide.md`
- `outputs/gold_standards/diabetes_model_endpoints/protocol_reference.md`
- `outputs/gold_standards/diabetes_model_endpoints/research_workspace_gold.md`

## Batch 2: User-Defined Second Batch, 9 Papers

Status summary: 6 of 9 have raw deep-extraction artifacts. Two guideline papers only have structured abstract worksheets. The remission systematic review has an existing deep-extraction worksheet and source card marked full, but no `raw/deep-extractions/` mirror or `local_assets` link.

| # | Source | Title | Current repository representation | Current gap |
|---|---|---|---|---|
| 1 | `src-diabetes-050` | ISFM Consensus Guidelines on the Practical Management of Diabetes Mellitus in Cats | structured worksheet `src-diabetes-050-structured-abstract-round1.md`; source card is `partial/abstract_weighted` | promote Desktop deep extract to raw artifact; update source card; add passage-level trace |
| 2 | `src-diabetes-087` | 2018 AAHA Diabetes Management Guidelines for Dogs and Cats | structured worksheet `src-diabetes-087-structured-abstract-round1.md`; source card is `partial/abstract_weighted` | promote Desktop deep extract to raw artifact; update source card; add passage-level trace |
| 3 | `src-diabetes-007` | Systematic review of feline diabetic remission: Separating fact from opinion | worksheet `src-diabetes-007-deep-extraction-round1.md`; source card is `full/deep_extracted` | decide whether to mirror Desktop draft into raw artifact; add `local_assets`; add passage-level trace |
| 4 | `src-diabetes-054` | Predictors of clinical remission in cats with diabetes mellitus | raw artifact `ext-src-diabetes-zini-2010-remission-predictors.md` | raw artifact uses legacy source ID; source card remains `partial/abstract_weighted` with no `local_assets`; trace missing |
| 5 | `src-diabetes-091` | Survival, remission, and quality of life in diabetic cats | raw artifact `ext-src-diabetes-rothlin-2023-survival-qol.md` | raw artifact uses legacy source ID; source card remains `partial/abstract_weighted` with no `local_assets`; trace missing |
| 6 | `src-diabetes-111` | Treatment of newly diagnosed diabetic cats with glargine insulin improves glycaemic control and results in higher probability of remission than protamine zinc and lente insulins | raw artifact `ext-src-diabetes-marshall-2009-glargine.md` | raw artifact uses legacy source ID; source card remains `partial/abstract_weighted` with no `local_assets`; trace missing |
| 7 | `src-diabetes-024` | Insulin glargine 300 U/ml for the treatment of feline diabetes mellitus | raw artifact `ext-src-diabetes-024.md`; source card is `full/deep_extracted`; `local_assets` linked | passage-level trace missing |
| 8 | `src-diabetes-035` | Velagliflozin, a once-daily, liquid, oral SGLT2 inhibitor, is effective as a stand-alone therapy for feline diabetes mellitus: the SENSATION study | raw artifact `ext-src-diabetes-035.md`; `local_assets` linked | source card is `full` but still `abstract_weighted`; passage-level trace missing |
| 9 | `src-diabetes-011` | SGLT2 inhibitor use in the management of feline diabetes mellitus | raw artifact `ext-src-diabetes-011.md`; source card is `full/deep_extracted`; `local_assets` linked | passage-level trace missing |

## Corrected Progress View

Across the user's 17 named materials:

- Material represented in repo: 17/17.
- Raw deep-extraction artifact exists: 7/17.
- Gold-standard paper card exists: 7/17, all from Batch 1 except Patra 2024.
- Source card currently linked to a raw artifact: 4/17 (`src-diabetes-025`, `src-diabetes-011`, `src-diabetes-024`, `src-diabetes-035`).
- Claim-level source-passage trace ready: 0/17 as a normalized batch capability.

This means the remaining work is not simple "deep extract or not." The real remaining work is normalization for source-grounded retrieval and passage-level traceability.

## Recommended Next Pass

Do this before writing new synthesis content:

1. Normalize Batch 2 source cards:
   - Add raw artifacts for `src-diabetes-050` and `src-diabetes-087`.
   - Decide whether to create a raw mirror for `src-diabetes-007`.
   - Update `src-diabetes-054`, `src-diabetes-091`, and `src-diabetes-111` so their raw artifacts use current source IDs or are linked through `local_assets`.
   - Update `src-diabetes-035` verification status if the raw extraction is accepted as full deep extraction.

2. Normalize Batch 1 representation:
   - Either promote the 7 gold-standard paper cards into raw deep-extraction assets, or explicitly treat `outputs/gold_standards/diabetes_model_endpoints/` as a valid content layer and link source cards to those artifacts.
   - Resolve duplicate identity for `The Cat as a Model for Human Obesity and Diabetes` (`src-diabetes-040` vs `src-diabetes-121`) and Patra 2024 (`src-diabetes-025` vs `src-diabetes-120` in later manifests).

3. Add passage-level evidence trace:
   - For each key claim used in research output, create source passage entries with title, URL/DOI, section or paragraph location, highlighted text, and why the passage supports the claim.
   - Use evidence labels consistently: `direct_source`, `source_supported`, and `analysis_inference`.

4. Only after the above, use these batches for a high-confidence Research Workspace answer or endpoint synthesis.
