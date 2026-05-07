---
id: src-diabetes-015
type: source
title: "Comparison of a low carbohydrate-low fiber diet and a moderate carbohydrate-high fiber diet in the management of feline diabetes mellitus"
source_kind: paper
species: feline
diseases: [diabetes mellitus]
models: []
endpoints: [glycemic-control, remission]
jurisdictions: []
evidence_level: original-study
year: 2006
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [diabetes, diet, low-carbohydrate, high-fiber, original-study]
links:
  doi: "10.1016/j.jfms.2005.08.004"
  url: "https://doi.org/10.1016/j.jfms.2005.08.004"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Crossref abstract reports 63 diabetic cats randomized to two canned diet groups for 16 weeks."
    - "By week 16, 22/31 LC-LF cats and 13/32 MC-HF cats had reverted to a non-insulin-dependent state."
    - "Crossref abstract reports 32 cats assigned to moderate-carbohydrate/high-fiber food and 31 assigned to low-carbohydrate/low-fiber food."
    - "Crossref abstract reports serum glucose and fructosamine decreased in both diet groups."
    - "Crossref abstract reports no significant difference in body-weight change between diet groups."
  source_supported_conclusion:
    - "This is a key original-study anchor for diet-composition comparisons."
    - "The study supports a low-carbohydrate/low-fiber diet branch, but only with study-design context preserved."
    - "It separates glycemic improvement from insulin-independence outcomes."
    - "The source supports a low-carbohydrate/low-fiber advantage for non-insulin-dependent outcome in this design, not a universal diet rule."
    - "Carbohydrate and fiber effects should not be isolated from each other without full-text support."
  llm_inference:
    - "This is a high-priority full-text target if the module needs diet effect-size tables, insulin-adjustment context, or remission-definition separation."
---

# Comparison of a low carbohydrate-low fiber diet and a moderate carbohydrate-high fiber diet in the management of feline diabetes mellitus

## One-Line Summary

Original diet-comparison study contrasting low-carbohydrate/low-fiber and moderate-carbohydrate/high-fiber approaches.

## Why It Matters For Feline Diabetes

- directly informs the diet architecture branch
- should be read before the module chooses a low-carbohydrate versus high-fiber framing

## Key Findings

- abstract-level extraction confirms a randomized 16-week diet comparison in 63 diabetic cats
- both diet groups improved serum glucose and fructosamine
- more cats in the low-carbohydrate/low-fiber group reverted to a non-insulin-dependent state by week 16
- body-weight changes did not significantly differ between diet groups in the abstract
- the source gives the strongest direct diet-comparison signal currently in the diabetes seed set
- the main endpoint tension is glycemic improvement in both groups versus greater non-insulin-dependence in the low-carbohydrate/low-fiber group

## Limits / Caveats

- extraction is abstract-weighted, not full-text
- do not isolate carbohydrate from fiber as the only causal variable
- do not treat non-insulin-dependent state as identical to a standard remission definition without full-text review
- do not treat the study as a universal diet prescription detached from insulin adjustment, canned-diet context, and 16-week duration
- remission claims should defer to [src-diabetes-007](src-diabetes-007.md)

## Diet-Comparison Logic

This source should control the direct diet-comparison branch, but only with its design preserved.

What can be promoted:

- 63 diabetic cats entered a randomized 16-week canned-diet comparison
- both diet groups improved serum glucose and fructosamine
- more low-carbohydrate/low-fiber cats reverted to a non-insulin-dependent state
- body-weight change did not significantly differ between groups in the abstract

What should be held:

- low-carbohydrate alone as the isolated causal factor
- high-fiber as universally inferior
- exact remission rates detached from remission-definition review
- broad diet prescription outside the study population and intervention context

## Relationship To Diet Architecture

This card should be read through:

- [diabetes diet architecture memo](../../system/indexes/diabetes-diet-architecture-memo.md)
- [src-diabetes-006](src-diabetes-006.md), broad diet overview
- [src-diabetes-016](src-diabetes-016.md), low-carbohydrate versus high-fiber review
- [src-diabetes-022](src-diabetes-022.md), high-protein / low-carbohydrate signal
- [src-diabetes-007](src-diabetes-007.md), remission boundary

The safe current diet architecture is not `low carbohydrate wins`; it is `diet variables, endpoint type, and evidence grade must stay separated`.

## Write-Back Implications

- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md) should separate serum glucose, fructosamine, non-insulin-dependence, and remission.
- [translation brief](../../topics/diabetes/translation-brief.md) should name this as the strongest diet-comparison study while preserving boundaries.
- [synthesis index](../../topics/diabetes/synthesis-index.md) should keep low-carbohydrate/low-fiber support inside the broader diet architecture.

## Full-Text Target If Needed

Extract insulin-adjustment rules, inclusion criteria, remission definitions, and exact diet composition before using this study for diet ranking.

## Open Follow-Up Questions

- what was the sample size and allocation method?
- what outcomes changed between diets?
- were insulin dose or remission rates reported?

## Linked Entities

- diseases: diabetes mellitus
- models:
- endpoints: glycemic control, remission
- mechanisms: diet composition
- regulations:
