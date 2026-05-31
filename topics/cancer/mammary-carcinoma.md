---
id: topic-cancer-mammary-carcinoma
type: topic
topic: cancer
species: feline
disease: cancer
question_type: branch
source_ids: [src-cancer-004, src-cancer-019, src-cancer-003, src-cancer-009, src-cancer-012, src-cancer-025, src-cancer-015]
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
| MC4 | Stage IV (metastatic) FMC has overall mean tumor-specific survival of 44 days | B | src-cancer-009 | largest metastatic cohort (n=73), retrospective |
| MC5 | Symptomatic vs asymptomatic at diagnosis: TSS 14 vs 128 days (P<0.001) | B | src-cancer-009 | major prognostic factor |
| MC6 | Pleural effusion predicts poor outcome (TSS 16 days vs without) | B | src-cancer-009 | major negative prognostic factor |
| MC7 | Metronomic chemo shows lower toxicity (20%) than MTD (66.7%) | B | src-cancer-009 | toxicity comparison, not survival comparison |
| MC8 | Tumor size is the most significant prognostic factor (P<0.0001) | B | src-cancer-012 | 100 cats, 1984 foundational study |
| MC9 | Age and breed are NOT prognostic factors | B | src-cancer-012 | 1984 study finding |
| MC10 | Surgery type affects disease-free interval but NOT survival time | B | src-cancer-012 | conservative vs radical comparison |
| MC11 | Validated prognostic parameters: tumor grading, lymph node/LV invasion | B | src-cancer-025 | 2015 systematic review |
| MC12 | Ki67, HER2, ER markers may provide therapeutic predictions but need standardization | B | src-cancer-025 | evidence quality concern |
| MC13 | Siamese breed has 2x risk (P<0.01) for mammary carcinoma | B | src-cancer-015 | 1981 North American study, 132 cats |
| MC14 | Malignant:benign ratio is 9:1 in feline mammary tumors | B | src-cancer-015 | foundational finding |
| MC15 | Feline mammary cancer appears estrogen-independent | B | src-cancer-015 | comparative oncology insight |

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

### Prognostic Factors (Abstract-Level)

Two abstract-level sources establish prognostic factor hierarchy:

**From `src-cancer-012` (1984 foundational study, n=100):**

| Factor | Prognostic Value | Evidence |
|--------|------------------|----------|
| Tumor size | **Most significant** (P<0.0001) | Small tumors (1-8 cm³) best prognosis |
| Age | NOT prognostic | ≤10 vs >10 years, no significance |
| Breed | NOT prognostic | no significance |
| Surgery type | Mixed | affects DFI (P<0.01) but NOT survival |

**From `src-cancer-025` (2015 systematic review):**

| Factor | Evidence Level | Status |
|--------|---------------|--------|
| Tumor grading | High reliability | Validated prognostic parameter |
| Lymph node invasion | High reliability | Validated prognostic parameter |
| Lymphovascular invasion | High reliability | Validated prognostic parameter |
| Tumor subtype | Promising | Needs standardized investigation |
| Tumor size | Promising | Needs standardized cutoffs |
| Staging | Promising | Needs standardized systems |
| Ki67, HER2, ER | May predict therapy | Needs consensus protocols |

**Key insight:** The field lacks standardization in methodology, weakening cross-study comparison.

### Metastatic Disease Outcomes (Abstract-Level)

`src-cancer-009` provides the largest published cohort of metastatic FMC (n=73, stage IV):

**Survival data:**

| Metric | Value | Context |
|--------|-------|---------|
| Overall mean TTP | 23 days | time to progression |
| Overall mean TSS | 44 days | tumor-specific survival |
| Symptomatic TSS | 14 days | cats with clinical signs at diagnosis |
| Asymptomatic TSS | 128 days | incidentally detected metastases |
| With pleural effusion | 16 days | major negative prognostic factor |

**Treatment modality comparison (abstract-level):**

| Treatment | n | Median TSS | Toxicity |
|-----------|---|------------|----------|
| MTD chemotherapy | 9 | 58 days | 66.7% |
| Metronomic chemotherapy | 15 | 75 days | 20% |
| Toceranib phosphate | 10 | 63 days | 30% |

**Boundary:** P=0.197 for treatment comparison — study was not powered to detect survival differences. Some cats survived >6 months despite overall poor prognosis.

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
