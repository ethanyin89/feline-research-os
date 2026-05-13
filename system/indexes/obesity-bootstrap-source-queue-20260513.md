---
id: obesity-bootstrap-source-queue-20260513
type: system
topic: obesity
question_type: source-queue
language: zh
last_compiled_at: 2026-05-13
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# Obesity Bootstrap Source Queue, 2026-05-13

This queue is derived from [feline diabetes / obesity intake manifest](feline-diabetes-obesity-intake-manifest-20260513.md).

The obesity section is new relative to the original 120-source project scope. Treat it as a bootstrap lane, not as already-compiled disease truth.

## Current Intake Read

| Class | Count | Handling |
|---|---:|---|
| new obesity candidates | 87 | queue for obesity bootstrap; 8 Tier A cards now first-pass ingested |
| shared-existing diabetes rows | 5 | cross-link to existing diabetes source cards |
| duplicate-in-sheet obesity rows | 5 | hold behind first occurrence |
| section label | 1 | not a source |

## Tier A — Obesity Shell Anchors

Read these first to decide the obesity module spine.

| Sheet Row | Proposed Role | Title | Locator |
|---:|---|---|---|
| 136 | feline-specific broad review | Feline obesity - prevalence, risk factors, pathogenesis, associated conditions and assessment: a review | `10.17221/145/2015-VETMED` |
| 135 | broad pathophysiology / epidemiology / management review | Canine and feline obesity: a review of pathophysiology, epidemiology, and clinical management | `10.2147/VMRR.S40868` |
| 134 | management overview | Canine and Feline Obesity Management | `10.1016/J.CVSM.2021.01.005` |
| 173 | newer epidemiology / associated pathology review | Overweight and obesity in domestic cats: epidemiological risk factors and associated pathologies | `10.1177/1098612X241285519` |
| 146 | prevention / target-population strategy | Identifying the target population and preventive strategies to combat feline obesity | `10.1177/1098612X241228042` |
| 174 | obesity management review | Management of obesity in cats | `10.2147/VMRR.S40869` |
| 190 | environment / behavior modification | Obesity Treatment: Environment and Behavior Modification | `10.1016/J.CVSM.2016.04.009` |
| 216 | insulin-sensitivity risk bridge | Insulin Sensitivity Decreases with Obesity, and Lean Cats with Low Insulin Sensitivity are at Greatest Risk of Glucose Intolerance with Weight Gain | `10.1053/JFMS.2001.0138` |

## Tier B — Epidemiology And Risk

| Sheet Row | Title | Locator |
|---:|---|---|
| 139 | A cross-sectional study to compare changes in the prevalence and risk factors for feline obesity between 1993 and 2007 in New Zealand | `10.1016/J.PREVETMED.2012.05.006` |
| 141 | Prevalence and risk factors for feline obesity in a first opinion practice in Glasgow, Scotland | `10.1016/J.JFMS.2010.05.011` |
| 142 | An investigation into the epidemiology of feline obesity in Great Britain: results of a cross-sectional study of 47 companion animal practises | `10.1136/VR.100953` |
| 144 | Risk factors identified for owner-reported feline obesity at around one year of age: Dry diet and indoor lifestyle | `10.1016/J.PREVETMED.2015.07.011` |
| 152 | Early-life risk factors identified for owner-reported feline overweight and obesity at around two years of age | `10.1016/J.PREVETMED.2017.05.010` |
| 178 | Overall prevalence of feline overweight/obesity in Japan as determined from a cross-sectional sample pool of healthy veterinary clinic-visiting cats in Japan | `10.3906/VET-1502-31` |
| 202 | Prevalence and risk factors of obesity in an urban population of healthy cats | `10.1016/J.JFMS.2008.07.002` |

## Tier C — Mechanism, Biomarkers, And Comorbid Branches

| Branch | Candidate Rows |
|---|---|
| adipokines / insulin resistance / endocrine | 140, 158, 162, 176, 189, 200, 207, 222, 224 |
| oxidative stress / inflammation / immune | 138, 147, 151, 153, 204 |
| microbiome / metabolomics / proteomics | 154, 161, 183, 186, 187, 196, 197, 199, 201 |
| cardiopulmonary / mobility / hepatic / kidney links | 164, 165, 184, 205, 208, 213, 227 |
| weight-loss interventions / management tools | 149, 155, 156, 157, 168, 169, 177, 180, 181, 194, 214, 215, 218, 220, 221, 223, 225, 226, 229, 230 |

## Shared Existing Sources

Do not duplicate these into new source cards unless a later obesity-specific extraction changes claim-fit:

| Sheet Row | Existing ID | Read |
|---:|---|---|
| 137 | `src-diabetes-005` | obese diabetic cat bridge |
| 185 | `src-diabetes-006` | diet and diabetes prevention/management |
| 206 | `src-diabetes-023` | cross-species diabetes / ketoacidosis context |
| 210 | `src-diabetes-016` | low carbohydrate versus high fiber diabetes diet debate |
| 212 | `src-diabetes-002` | older diabetes pathogenesis |

## First Module Shell

The first obesity topic layer now exists:

1. `topics/obesity/index.md`
2. `topics/obesity/navigation.md`
3. `topics/obesity/current-state-dashboard.md`

Do not create mechanism / recognition / endpoint / translation pages until Tier 1 obesity cards have deep extraction or a narrow compiled owner exists.

## Deep Extraction Candidates

Start with:

1. row 136, feline-specific obesity review
2. row 173, newer epidemiology / associated pathologies review
3. row 146, target population and prevention strategy
4. row 216, obesity-to-insulin-sensitivity bridge
5. row 223, weight-loss body composition / activity / microbiota study

These should define the first obesity spine: prevalence/risk, mechanism, management, diabetes bridge, and weight-loss endpoints.
