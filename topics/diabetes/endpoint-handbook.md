---
id: topic-diabetes-endpoint-handbook
type: topic
topic: diabetes
species: feline
disease: diabetes mellitus
question_type: endpoints
source_ids: [src-diabetes-004, src-diabetes-005, src-diabetes-006, src-diabetes-007, src-diabetes-008, src-diabetes-011, src-diabetes-015, src-diabetes-016, src-diabetes-018, src-diabetes-022, src-diabetes-024]
last_compiled_at: 2026-05-06
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline Diabetes Endpoint Handbook

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| FE1 | Glycemic control is the core treatment-response endpoint family across diet, insulin, and adjunct branches. | B | src-diabetes-008, src-diabetes-015, src-diabetes-024 | monitoring architecture, not protocol ranking |
| FE2 | Remission is a core endpoint, but current evidence blocks single-predictor or single-protocol claims. | B | src-diabetes-007 | remission boundary, not predictor hierarchy |
| FE3 | Diet endpoints must separate carbohydrate, fiber, protein, insulin independence, insulin-dose reduction, and evidence quality. | B | src-diabetes-006, src-diabetes-015, src-diabetes-016, src-diabetes-022 | diet architecture, not universal prescription |
| FE4 | SGLT2 safety and current-label endpoints must preserve candidate selection and ketoacidosis/euglycemic-DKA monitoring. | B | src-diabetes-011 | treatment-safety boundary, not route-convenience claim |
| FE5 | Neuropathy and microvascular pathology are complication endpoints that should not disappear behind remission or glycemic-control framing. | B | src-diabetes-004, src-diabetes-018 | complication branch, not treatment-ranking endpoint |

## Evidence-Depth Caveat

This page sits on a fully deep-extracted diabetes source-card layer (24/24 papers). Key anchors: diet prevention/management review (`src-diabetes-006`), remission systematic review (`src-diabetes-007`), alpha-glucosidase plus low-carbohydrate diet study (`src-diabetes-008`), SGLT2 clinical review (`src-diabetes-011`), diet-comparison trial (`src-diabetes-015`), low-carbohydrate versus high-fiber review (`src-diabetes-016`), high-protein/low-carbohydrate diet study (`src-diabetes-022`), glargine U300 trial (`src-diabetes-024`), and neuropathy/microvascular anchors (`src-diabetes-004`, `src-diabetes-018`). This is now an endpoint handbook rather than a routing page.

## Core Takeaway

Diabetes endpoints should stay split by job: glycemic control, remission/insulin independence, diet-response architecture, treatment safety, body-condition state, and complication status. The page should not turn endpoint visibility into treatment ranking.

## Endpoint Hierarchy

### Endpoint 1: Glycemic Control

Glycemic markers and insulin needs are central response endpoints across diet, insulin, and adjunct treatment studies. Fructosamine, serum glucose, insulin discontinuation, and clinical response should not be collapsed into one outcome.

**Key boundary:** response tracking, not protocol superiority.

**Lead sources:** `src-diabetes-008`, `src-diabetes-015`, `src-diabetes-024`

### Endpoint 2: Remission And Insulin Independence

Remission is real and important, but evidence quality is moderate-to-poor and no single factor predicts remission. Non-insulin-dependent state should be tracked carefully but not automatically equated with a standardized remission endpoint.

**Key boundary:** endpoint visibility, not predictor or protocol ranking.

**Lead sources:** `src-diabetes-007`, `src-diabetes-015`

### Endpoint 3: Diet-Response Architecture

Diet endpoints cross prevention and management. Low-carbohydrate/low-fiber, high-fiber, and high-protein/low-carbohydrate signals need separate evidence labels and endpoint definitions.

**Key boundary:** diet affects endpoints, but current evidence does not support a universal prescription.

**Lead sources:** `src-diabetes-006`, `src-diabetes-015`, `src-diabetes-016`, `src-diabetes-022`

### Endpoint 4: Treatment Safety And Candidate Selection

SGLT2 and insulin branches require safety endpoints. SGLT2 discussion must keep residual beta-cell function, candidate selection, ketonuria/ketoacidosis monitoring, and euglycemic DKA risk above route convenience.

**Key boundary:** safety and label-control endpoints, not oral-route superiority.

**Lead sources:** `src-diabetes-011`, `src-diabetes-024`

### Endpoint 5: Body Condition And Sequencing

Body weight and muscle condition connect obesity, insulin resistance, diet, and management. Current presentation may include weight and muscle loss, so endpoint sequencing matters.

**Key boundary:** body-condition endpoint, not automatic caloric restriction.

**Lead sources:** `src-diabetes-005`, `src-diabetes-006`

### Endpoint 6: Complication Status

Neuropathy, motor conduction deficits, myelinated fiber density, and microvascular pathology create a chronic-complication endpoint branch.

**Key boundary:** complication architecture, not screening recommendation or treatment reversibility claim.

**Lead sources:** `src-diabetes-004`, `src-diabetes-018`

## Source-Layer Reality

| Source | Role | Status |
|---|---|---|
| src-diabetes-004 | neuropathy clinical and tissue-pathology endpoint | deep_extracted |
| src-diabetes-005 | obesity/body-condition endpoint and sequencing branch | deep_extracted |
| src-diabetes-006 | diet prevention/management evidence-quality frame | deep_extracted |
| src-diabetes-007 | remission systematic-review boundary | deep_extracted |
| src-diabetes-008 | alpha-glucosidase plus low-carbohydrate diet response endpoints | deep_extracted |
| src-diabetes-011 | SGLT2 treatment safety and candidate-selection gateway | deep_extracted |
| src-diabetes-015 | direct diet-comparison glycemic and insulin-independence endpoints | deep_extracted |
| src-diabetes-016 | low-carbohydrate versus high-fiber diet debate | deep_extracted |
| src-diabetes-018 | endoneurial microvascular complication endpoint | deep_extracted |
| src-diabetes-022 | high-protein/low-carbohydrate insulin-requirement endpoint | deep_extracted |
| src-diabetes-024 | glargine U300 glycemic, hypoglycemia, and remission signals | deep_extracted |

## Current Owner Memo

- [diabetes remission boundary memo](../../system/indexes/diabetes-remission-boundary-memo.md)
- [diabetes diet architecture memo](../../system/indexes/diabetes-diet-architecture-memo.md)
- [diabetes treatment branch comparison memo](../../system/indexes/diabetes-treatment-branch-comparison-memo.md)
- [diabetes diagnostic monitoring workup memo](../../system/indexes/diabetes-diagnostic-monitoring-workup-memo.md)
- [diabetes neuropathy boundary memo](../../system/indexes/diabetes-neuropathy-boundary-memo.md)
- [diabetes SGLT2 safety/regulatory boundary memo](../../system/indexes/diabetes-sglt2-safety-regulatory-boundary-memo.md)

## Guardrail

Do not use endpoints to rank treatments by superiority. Glycemic control, remission, insulin independence, diet response, SGLT2 safety, hypoglycemia, body condition, and complications are different endpoint families and must stay separated.

## What The Module Can Say Safely

- glycemic control is the core response endpoint family
- remission is important but predictor-weak
- diet endpoints require evidence labels and endpoint separation
- SGLT2 endpoints must preserve ketoacidosis and candidate-selection gates
- neuropathy and microvascular pathology are real complication endpoints

## What The Module Should Not Say Yet

- do not rank insulin protocols or diet protocols from this endpoint page alone
- do not claim a single remission predictor
- do not promote oral route as inherently better
- do not treat biochemical hypoglycemia, clinical hypoglycemia, remission, and glycemic control as the same outcome
- do not use complication endpoints to claim treatment prevention effects without direct evidence

## Current Role

Use this page as the diabetes endpoint handbook. The source-card layer is complete at 24/24 deep-extracted papers. Next gains come from guideline/full-text precision where monitoring cadence, remission definitions, insulin comparisons, or SGLT2 label gates need decision-grade detail.
