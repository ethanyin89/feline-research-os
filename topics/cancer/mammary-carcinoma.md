---
id: topic-cancer-mammary-carcinoma
type: topic
topic: cancer
species: feline
disease: cancer
question_type: branch
source_ids: [src-cancer-004, src-cancer-019, src-cancer-003]
last_compiled_at: 2026-05-30
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: not_checked
owner: codex
status: active
---

# Feline Mammary Carcinoma

## Key-Claim Traceability

| ID | Claim | Level | Source IDs | Boundary |
|---|---|---|---|---|
| MC1 | Mammary carcinoma is an early branch in the feline cancer module because it appears in both molecular review and comparative oncology evidence | B | src-cancer-004, src-cancer-019 | branch priority, not prevalence ranking |
| MC2 | A TNBC-like / basal-like model sub-branch is supported by marker-defined evidence in one 24-case study | B | src-cancer-019 | study-bound, not universal phenotype frequency |
| MC3 | COX-2 can be carried as a feline mammary carcinoma prognosis-marker candidate with caveats | B | src-cancer-003 | marker caveat, not survival prediction or treatment guidance |

## Evidence-Depth Caveat

This page is a branch architecture page based on three deep-extracted sources. It can define branch structure and marker boundaries. It cannot yet provide treatment protocols, survival estimates, or owner-facing management advice.

## Core Takeaway

Feline mammary carcinoma should be a first split-out branch because it carries three distinct evidence roles:

- comparative oncology and human breast-cancer model relevance
- TNBC-like / basal-like marker phenotype evidence
- COX-2 prognosis-marker candidate evidence

These roles should remain separate. Model relevance is not treatment guidance, and biomarker signal is not a clinical decision rule.

## Branch Architecture

### Comparative Oncology Role

`src-cancer-004` and `src-cancer-019` support mammary carcinoma as a translationally important branch. The safe claim is that feline mammary carcinoma can be useful for comparative oncology framing, especially around hormone-independent and TNBC-like biology.

**Boundary:** do not translate human breast cancer therapies into feline recommendations from model similarity alone.

### TNBC-Like / Basal-Like Phenotype

`src-cancer-019` evaluated 24 feline mammary adenocarcinomas using ER, PR, HER2, CK5/6, and EGFR.

Study-bound findings:

- 14/24 tumors were triple negative.
- 11/14 triple-negative tumors were basal-like.
- 19/24 tumors were basal-like by CK5/6 and/or EGFR marker logic.

**Boundary:** keep these as one-study findings, not universal feline mammary carcinoma rates.

### BRCA Boundary

`src-cancer-019` did not find tumor-specific BRCA1/BRCA2 abnormalities in the amplified subset.

**Boundary:** this does not prove BRCA is irrelevant in cats; it prevents claiming that feline TNBC-like mammary carcinoma is BRCA-driven from this source.

### COX-2 Prognosis Marker Candidate

`src-cancer-003` supports COX-2 as a feline mammary carcinoma prognosis-marker candidate, but the evidence is limited and method-sensitive.

**Boundary:** do not turn COX-2 into a treatment selection rule or owner-facing survival prediction.

## What The Module Can Say Safely

- Mammary carcinoma deserves a dedicated cancer branch.
- TNBC-like / basal-like model evidence exists, but should be marker-defined and study-bound.
- BRCA translation from human TNBC should be handled cautiously.
- COX-2 is a candidate prognosis-marker layer for feline mammary carcinoma, with standardization caveats.

## What The Module Should Not Say Yet

- Do not rank treatments.
- Do not give survival ranges.
- Do not state universal TNBC-like prevalence.
- Do not claim BRCA-driven mechanism closure.
- Do not recommend COX inhibitors from COX marker evidence.

## Current Role

Use this page as the mammary carcinoma branch shell. Next gains require treatment outcome sources, registry/prevalence sources, and deeper extraction of dedicated mammary carcinoma prognosis reviews.
