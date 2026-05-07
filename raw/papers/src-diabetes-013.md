---
id: src-diabetes-013
type: source
title: "Hypersomatotropism, Acromegaly, and Hyperadrenocorticism and Feline Diabetes Mellitus"
source_kind: paper
species: feline
diseases: [diabetes mellitus, hypersomatotropism, acromegaly, hyperadrenocorticism]
models: []
endpoints: []
jurisdictions: []
evidence_level: review
year: 2013
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [diabetes, endocrine-comorbidity, hypersomatotropism, acromegaly, hyperadrenocorticism]
links:
  doi: "10.1016/j.cvsm.2012.12.004"
  url: "https://doi.org/10.1016/j.cvsm.2012.12.004"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "PubMed abstract says most diabetic cats fit a type-2-like assumption, but not all."
    - "PubMed abstract names hypersomatotropism, acromegaly, and hyperadrenocorticism as the focus."
    - "PubMed abstract says a significant proportion of diabetic cats have other specific types of diabetes."
    - "PubMed abstract says the article discusses relevance, presentation, diagnosis, and therapy."
  source_supported_conclusion:
    - "This source should anchor the endocrine-secondary diabetes branch."
    - "Type-2-like diabetes is the default frame, but secondary endocrine diabetes needs a branch-level gate."
    - "The source supports linking endocrine comorbidity across relevance, presentation, diagnosis, and therapy."
    - "This card should prevent the diabetes module from treating every case as primary type-2-like disease."
    - "Difficult control, high insulin requirement, non-remission, or unexpected treatment response should route to endocrine-secondary thinking."
  llm_inference:
    - "This is a high-priority full-text target if later outputs need screening triggers, prevalence estimates, or treatment algorithms."
---

# Hypersomatotropism, Acromegaly, and Hyperadrenocorticism and Feline Diabetes Mellitus

## One-Line Summary

Review anchor for endocrine disorders that can drive or complicate feline diabetes.

## Why It Matters For Feline Diabetes

- prevents the module from treating all feline diabetes as primary type-2-like disease
- likely important for insulin resistance, non-remission, and difficult-control branches

## Key Findings

- abstract-level extraction confirms this as an endocrine-secondary diabetes anchor
- abstract challenges a universal type-2-like assumption by noting that a meaningful subset of cats has other specific diabetes etiologies
- hypersomatotropism, acromegaly, and hyperadrenocorticism are the named endocrinopathy focus
- the source makes secondary endocrine disease cross-cutting: mechanism, recognition, diagnosis, and therapy all change
- its main value is a gate: default type-2-like framing is useful, but not universal

## Limits / Caveats

- extraction is abstract-weighted, not full-text
- diagnostic thresholds and management implications need extraction
- prevalence estimates and screening triggers need full-text review
- do not provide IGF-1, imaging, adrenal, or confirmatory testing algorithms from this card alone
- do not treat endocrine-secondary diabetes as either rare trivia or the universal baseline

## Endocrine-Secondary Gate Logic

This source controls the diabetes module's main mechanism overcompression risk.

What can be promoted:

- most feline diabetes can be started from a type-2-like frame
- a significant subset has specific secondary etiologies
- hypersomatotropism, acromegaly, and hyperadrenocorticism deserve named branches
- endocrine-secondary disease affects presentation, diagnosis, and therapy, not only mechanism

What should be held:

- prevalence estimates for each endocrinopathy
- exact screening thresholds
- confirmatory diagnostic sequence
- therapy recommendations
- claims that secondary endocrine disease explains all difficult diabetic cats

## Relationship To Newer HST Source

This card should be paired with [src-diabetes-020](src-diabetes-020.md), which adds newer hypersomatotropism-induced diabetes detail.

The safe hierarchy is:

- `src-diabetes-013` defines the broader secondary-endocrine branch
- `src-diabetes-020` sharpens the hypersomatotropism-induced diabetes subbranch
- [diabetes endocrine-secondary diabetes memo](../../system/indexes/diabetes-endocrine-secondary-diabetes-memo.md) remains the smallest durable owner

## Write-Back Implications

- [mechanism overview](../../topics/diabetes/mechanism-overview.md) should preserve type-2-like default framing while naming secondary endocrine disease.
- [risk and recognition](../../topics/diabetes/risk-and-recognition.md) should include a branch gate for non-primary diabetes suspicion.
- [translation brief](../../topics/diabetes/translation-brief.md) should avoid interpreting difficult control or non-remission without endocrine context.
- [synthesis index](../../topics/diabetes/synthesis-index.md) should keep the disease model mixed rather than remission-only or type-2-only.

## Full-Text Target If Needed

If later Diabetes outputs need a practical secondary-endocrine workup, the next read should extract:

- prevalence or enrichment estimates for each endocrinopathy
- screening triggers for difficult-control cats
- IGF1, imaging, adrenal, or confirmatory-test logic
- how therapy for the endocrine disorder changes glycemic control
- whether remission probability differs after secondary disease is identified
- whether the paper distinguishes screening in newly diagnosed cats from screening after poor control or unexpected insulin response

## Open Follow-Up Questions

- how common is hypersomatotropism among diabetic cats?
- what screening tests are recommended?
- how does endocrine disease alter remission probability?

## Linked Entities

- diseases: diabetes mellitus, hypersomatotropism, acromegaly, hyperadrenocorticism
- models:
- endpoints:
- mechanisms: growth hormone excess, cortisol excess, insulin resistance
- regulations:
