# Deep Extraction Batch 3 Inventory - 2026-06-26

Purpose: track the user's third diabetes/obesity deep-extract batch and keep duplicate or mismatched source IDs from becoming separate evidence owners.

## Core Handling Rule

These materials follow the same rule as the previous diabetes batches:

- preserve the desktop deep extraction as a raw artifact;
- attach it to the canonical source card through `links.local_assets`;
- add initial `source_passages` so generated claims can resolve to supporting passages;
- keep duplicate source IDs as aliases, not independent evidence text;
- do not claim full paragraph-level original-source audit until every generated judgment has been checked against the original article paragraph or figure.

## Batch 3 Materials Processed So Far

| # | Canonical Source | Duplicate / Alias IDs | Title | Raw Deep Extraction | Current Status | Remaining Gap |
|---|---|---|---|---|---|---|
| 1 | `src-diabetes-028` | `src-obesity-095` | Comparative Aspects of Human, Canine, and Feline Obesity and Factors Predicting Progression to Diabetes | `raw/deep-extractions/ext-src-diabetes-028.md` | source card upgraded to `full/deep_extracted`; obesity alias linked to same artifact; initial `source_passages` added | decide whether to retire or keep `src-obesity-095`; map MDPI sections to stable paragraph/figure anchors |
| 2 | `src-diabetes-005` | `src-diabetes-119` | Feline comorbidities: Pathophysiology and management of the obese diabetic cat | `raw/deep-extractions/ext-src-diabetes-005.md` | canonical diabetes card refreshed; duplicate alias linked to same artifact; initial `source_passages` added | update downstream topic copy that still uses older 40% obesity wording; add original PDF/page paragraph anchors if needed |
| 3 | `src-obesity-027` | none | GLUT4 but not GLUT1 expression decreases early in the development of feline obesity | `raw/deep-extractions/ext-src-obesity-027.md` | obesity card upgraded to `full/deep_extracted`; V2 fields added; initial `source_passages` added | full Elsevier article audit still needed for biopsy, diet, and Western blot method details |
| 4 | `src-obesity-008` | none | Insulin Sensitivity Decreases with Obesity, and Lean Cats with Low Insulin Sensitivity are at Greatest Risk of Glucose Intolerance with Weight Gain | `raw/deep-extractions/ext-src-obesity-008.md` | existing deep-extracted card refreshed with desktop raw artifact; initial `source_passages` added | do not convert Si/Sg/fasting insulin signals into clinical screening thresholds without prospective validation |
| 5 | `src-obesity-030` | none | Metabolic Profiles of Feline Obesity Revealed by Untargeted and Targeted Mass Spectrometry-Based Metabolomics Approaches | `raw/deep-extractions/ext-src-obesity-030.md` | obesity card upgraded to `full/deep_extracted`; initial `source_passages` added | keep glycine/citrulline/LPC/TG signals as candidate metabolomics findings, not diagnostic thresholds |
| 6 | `src-obesity-011` | none | The cat as a model for human obesity: insights into depot-specific inflammation associated with feline obesity | `raw/deep-extractions/ext-src-obesity-011.md` | obesity card upgraded to `full/deep_extracted`; initial `source_passages` added | preserve local adipose tissue versus blood marker distinction and SAT/VAT model boundary |
| 7 | `src-obesity-049` | none | Association between Gut Microbiota and Metabolic Health and Obesity Status in Cats | `raw/deep-extractions/ext-src-obesity-049.md` | obesity card upgraded to `full/deep_extracted`; initial `source_passages` added | keep bacterial-family signals as limited associations, not microbiome intervention targets |
| 8 | `src-obesity-066` | none | The effect of obesity and subsequent weight reduction on cardiac morphology and function in cats | `raw/deep-extractions/ext-src-obesity-066.md` | obesity card upgraded to `full/deep_extracted`; initial `source_passages` added | frame obesity as cardiac morphology/HCM interpretation confounder, not proven HCM cause |
| 9 | `src-obesity-005` | none | Identifying the target population and preventive strategies to combat feline obesity | `raw/deep-extractions/ext-src-obesity-005.md` | existing prevention anchor refreshed with full-text desktop raw artifact and initial `source_passages` | preserve kitten growth/nutrition boundary; do not convert review synthesis into universal DER prescription |
| blocked | `src-obesity-022` | none | Obesity-induced changes in gene expression in feline adipose and skeletal muscle tissue | none | desktop file title points to this source, but body content duplicates `src-obesity-008`; source card left unchanged | request/capture the correct deep extract before upgrading `src-obesity-022` |

## Corrected Progress View

- Valid desktop deep extracts represented in repo: 9/9 processed.
- Canonical source cards linked to raw artifacts: 9/9 processed.
- Duplicate/alias cards linked where relevant: 2/2 alias groups.
- Initial passage-library coverage: 9/9 processed.
- Blocked due to desktop content/title mismatch: 1 (`src-obesity-022`).
- Full paragraph-level original-source trace ready: not complete.

## Content Boundaries To Preserve

- Obesity and insulin resistance are not sufficient to predict diabetes progression; beta-cell compensation/failure and hepatic glucose output must remain explicit.
- Obese diabetic cat management should not default to immediate caloric restriction when active disease-related weight loss or muscle loss is present.
- The GLUT4 paper is early mechanism evidence for obesity-related insulin resistance; it is not proof that obesity inevitably progresses to diabetes.
- Feline obesity metabolomics findings are candidate research signals; they are not validated diagnostic panels or owner-facing screening thresholds.
- The depot-specific inflammation paper supports local adipose tissue inflammation and SAT/VAT model-boundary claims, not systemic cytokine or insulin-sensitivity claims.
- Gut microbiota findings support limited candidate-family associations; they do not justify microbiome testing, probiotics, antibiotics, or diet interventions.
- Obesity-related cardiac morphology findings should be used as HCM interpretation context, not as proof that obesity causes primary HCM.
- Prevention guidance for kittens must preserve growth-stage nutrition and should not collapse into adult obesity weight-loss advice.
