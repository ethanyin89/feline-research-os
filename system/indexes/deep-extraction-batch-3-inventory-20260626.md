# Deep Extraction Batch 3 Inventory - 2026-06-26

Purpose: track the first three materials from the user's third diabetes/obesity deep-extract batch and keep duplicate source IDs from becoming separate evidence owners.

## Core Handling Rule

These materials follow the same rule as the previous diabetes batches:

- preserve the desktop deep extraction as a raw artifact;
- attach it to the canonical source card through `links.local_assets`;
- add initial `source_passages` so generated claims can resolve to supporting passages;
- keep duplicate source IDs as aliases, not independent evidence text;
- do not claim full paragraph-level original-source audit until every generated judgment has been checked against the original article paragraph or figure.

## Batch 3, First 3 Materials

| # | Canonical Source | Duplicate / Alias IDs | Title | Raw Deep Extraction | Current Status | Remaining Gap |
|---|---|---|---|---|---|---|
| 1 | `src-diabetes-028` | `src-obesity-095` | Comparative Aspects of Human, Canine, and Feline Obesity and Factors Predicting Progression to Diabetes | `raw/deep-extractions/ext-src-diabetes-028.md` | source card upgraded to `full/deep_extracted`; obesity alias linked to same artifact; initial `source_passages` added | decide whether to retire or keep `src-obesity-095`; map MDPI sections to stable paragraph/figure anchors |
| 2 | `src-diabetes-005` | `src-diabetes-119` | Feline comorbidities: Pathophysiology and management of the obese diabetic cat | `raw/deep-extractions/ext-src-diabetes-005.md` | canonical diabetes card refreshed; duplicate alias linked to same artifact; initial `source_passages` added | update downstream topic copy that still uses older 40% obesity wording; add original PDF/page paragraph anchors if needed |
| 3 | `src-obesity-027` | none | GLUT4 but not GLUT1 expression decreases early in the development of feline obesity | `raw/deep-extractions/ext-src-obesity-027.md` | obesity card upgraded to `full/deep_extracted`; V2 fields added; initial `source_passages` added | full Elsevier article audit still needed for biopsy, diet, and Western blot method details |

## Corrected Progress View

- Desktop deep extracts represented in repo: 3/3.
- Canonical source cards linked to raw artifacts: 3/3.
- Duplicate/alias cards linked where relevant: 2/2 alias groups.
- Initial passage-library coverage: 3/3.
- Full paragraph-level original-source trace ready: not complete.

## Content Boundaries To Preserve

- Obesity and insulin resistance are not sufficient to predict diabetes progression; beta-cell compensation/failure and hepatic glucose output must remain explicit.
- Obese diabetic cat management should not default to immediate caloric restriction when active disease-related weight loss or muscle loss is present.
- The GLUT4 paper is early mechanism evidence for obesity-related insulin resistance; it is not proof that obesity inevitably progresses to diabetes.

