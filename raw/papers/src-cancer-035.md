---
id: src-cancer-035
type: source
title: "Immunohistochemical Detection of Proteins Associated with Multidrug Resistance to Anti-Cancer Drugs in Canine and Feline Primary Pulmonary Carcinoma"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
pmid: 20086324
year: 2010
doi: "10.1292/jvms.09-0519"
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, immunohistochemical, detection, proteins, associated, multidrug, resistance, anti-cancer]
links:
  doi: ""
  url: "https://www.jstage.jst.go.jp/article/jvms/72/5/72_09-0519/_article"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Immunohistochemical Detection of Proteins Associated with Multidrug Resistance to Anti-Cancer Drugs in Canine and Feline Primary Pulmonary Carcinoma."
    - "The intake sheet locator is: https://www.jstage.jst.go.jp/article/jvms/72/5/72_09-0519/_article."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
---

# Immunohistochemical Detection of Proteins Associated with Multidrug Resistance to Anti-Cancer Drugs in Canine and Feline Primary Pulmonary Carcinoma

## Evidence-Depth Caveat

This card has deep extraction based on the abstract. 2010 JVMS: feline pulmonary carcinomas (n=18) frequently express PGP, MRP, LRP; ~50% express MT. Inherent multidrug resistance explains poor chemotherapy response. [Deep extraction worksheet](../../system/indexes/src-cancer-035-deep-extraction-round1.md).

## Source Check, 2026-06-01

PubMed abstract fetched as a zero-cost extraction step.

- PMID: 20086324
- DOI: 10.1292/jvms.09-0519
- Journal: Journal of Veterinary Medical Science
- Year: 2010

## Abstract Summary

This study evaluated multidrug resistance (MDR) protein expression in canine (n=52) and feline (n=18) primary pulmonary carcinomas.

**Proteins evaluated:**
- P-glycoprotein (PGP)
- Multidrug resistance-related protein (MRP)
- Lung resistance-related protein (LRP)
- Metallothionein (MT)

**Expression findings:**

| Protein | Expression Pattern |
|---------|-------------------|
| PGP | Frequently expressed in all carcinoma types |
| MRP | Frequently expressed in all carcinoma types |
| LRP | Frequently expressed in all carcinoma types |
| MT | Expressed in ~50% of each carcinoma type |

**Key finding:**
- Overlapping expression detected in all positive cases
- Most pulmonary carcinomas show strong multidrug resistance

**Clinical implication:**
Difficult to treat canine and feline primary pulmonary carcinomas with anti-cancer drugs due to inherent MDR.

**Boundary:** This is observational data on MDR expression, not treatment guidance. Does not specify which chemotherapy agents are affected.

## One-Line Summary

Most feline pulmonary carcinomas express PGP, MRP, LRP (frequent) and MT (~50%), indicating strong inherent multidrug resistance.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Immunohistochemical Detection of Proteins Associated with Multidrug Resistance to Anti-Cancer Drugs in Canine and Feline Primary Pulmonary Carcinoma.
- The intake sheet locator is: https://www.jstage.jst.go.jp/article/jvms/72/5/72_09-0519/_article.

### source_supported_conclusion

- This is a first-pass source-card placeholder for triage and queue control.
- It should not support prevalence, diagnostic, treatment, management, or risk-ranking claims yet.

### llm_inference

- The title suggests a possible `cancer` role, but the actual claim-fit requires abstract or full-text review.

## Claim-Fit Judgment

Strongest safe use:

- intake ownership
- source queue placement
- deduplication and future extraction planning

Must not control yet:

- reader-facing medical advice
- numeric claims
- comparative ranking
- guideline-like recommendations
- mechanism closure

## Image Asset TODO

- figures to capture: unknown until source text is read
- why these matter: tables or figures should remain behind the candidate gate until labels are verified

## Open Follow-Up Questions

- What source family is confirmed by the abstract or article body?
- Which claims, if any, are reusable for the cancer module?
- Does this source deserve deep extraction, or should it remain queue context?
- Are there tables or figures that change the module structure?

## Linked Entities

- diseases: cancer
- models:
- endpoints:
- mechanisms:
- regulations:
