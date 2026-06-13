---
id: src-cancer-005-deep-extraction-round1
type: system
source_id: src-cancer-005
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-005

**Source:** Cats, Cancer and Comparative Oncology
**Journal:** Veterinary Sciences (MDPI, Open Access) (2015)
**DOI:** 10.3390/vetsci2030111
**PMID:** 29061935
**Evidence Level:** review

## Phase 0: Context

**Access status:** Full abstract available in source card. Open access via MDPI.

**Source scope:** Comparative oncology review establishing cats as models for human cancer research, focusing on three specific tumor types.

**Cross-branch value:** Provides comparative oncology rationale for oral SCC, mammary carcinoma, and injection site sarcoma pages.

## Phase 1: Sequential Micro-Analysis

### 1.1 One Medicine Gap

| Claim | Quote | Boundary |
|-------|-------|----------|
| Canine models established | "Naturally occurring tumors in dogs are well-established models for several human cancers" | Context |
| Feline underutilization | "have not been utilized to the same degree in the One Medicine approach to cancer" | Research gap |
| Shared cat/dog model benefits | "spontaneous cancers developing in an immunocompetent animal sharing the same environment as humans" | Model rationale |
| Trial design advantages | "shorter lifespan allowing more rapid trial completion and data collection" | Methodological |
| Treatment-naïve populations | "lack of standard of care for many cancers allowing evaluation of therapies in treatment-naïve populations" | Trial design |

**Key insight:** Cats offer the same model benefits as dogs (spontaneous cancer, shared environment, immunocompetent) but remain underutilized.

### 1.2 Oral Squamous Cell Carcinoma Model

| Claim | Quote | Boundary |
|-------|-------|----------|
| Prevalence | "Feline oral squamous cell carcinoma is common" | General frequency |
| Model validity | "shares both clinical and molecular features with human head and neck cancer" | Comparative oncology |
| Research value | "attractive model for evaluating new therapies" | Trial potential |

**Implication:** Supports oral-squamous-cell-carcinoma.md comparative oncology section.

### 1.3 Mammary Tumor Phenotype

| Claim | Quote | Boundary |
|-------|-------|----------|
| Malignancy rate | "Feline mammary tumors are usually malignant and aggressive" | Clinical characterization |
| Triple-negative enrichment | "the 'triple-negative' phenotype being more common than in humans" | Key research finding |
| Research value | "offering an enriched population in which to examine potential targets and treatments" | Trial potential |

**Key insight:** The enriched triple-negative population makes cats particularly valuable for this aggressive breast cancer subtype research.

### 1.4 Injection Site Sarcoma Model

| Claim | Quote | Boundary |
|-------|-------|----------|
| Unique model | "although there is not an exact corollary in humans" | Limitation acknowledgment |
| Mechanism | "may be a model for inflammation-driven tumorigenesis" | Hypothesis |
| Research applications | "opportunities for studying variations in individual susceptibility as well as preventative and therapeutic strategies" | Research directions |

**Implication:** Connects to injection-site-sarcoma.md chronic inflammation hypothesis (aligned with src-cancer-047).

## Phase 2: Theme Reconstruction

### Theme A: Feline Comparative Oncology Opportunity

Cats share the benefits of dogs as cancer models but remain underutilized. This is a research opportunity, not a limitation. The same "shared environment, shorter lifespan, treatment-naïve" advantages that made canine oncology successful apply to cats.

### Theme B: Three Strategic Tumor Models

The review identifies three distinct feline cancers with specific human cancer parallels:

| Feline Cancer | Human Parallel | Special Value |
|---------------|----------------|---------------|
| Oral SCC | Head and neck cancer | Clinical + molecular similarity |
| Mammary tumors | Triple-negative breast cancer | Enriched phenotype for drug trials |
| Injection site sarcoma | Inflammation-driven cancer | Unique mechanistic model |

### Theme C: Triple-Negative Enrichment

The observation that triple-negative mammary tumors are more common in cats than humans is potentially significant. This creates an "enriched population" for research into this aggressive breast cancer subtype that is difficult to treat in humans.

**Boundary:** The review is from 2015. The triple-negative prevalence claim needs validation with more recent data.

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/oral-squamous-cell-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| OSCC-COMP1 | Feline oral SCC shares clinical and molecular features with human head and neck cancer | B | comparative oncology, 2015 review |
| OSCC-COMP2 | Feline oral SCC is an attractive model for evaluating new therapies | B | research context, not treatment |

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC-TN1 | Feline mammary tumors are usually malignant and aggressive | B | general characterization |
| MC-TN2 | Triple-negative phenotype is more common in feline mammary tumors than in human breast cancer | B | 2015 review claim, needs recent validation |
| MC-TN3 | Enriched triple-negative population offers research value for drug trials | B | research context, not treatment |

### Target: topics/cancer/injection-site-sarcoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| FISS-INF1 | FISS may be a model for inflammation-driven tumorigenesis | B | hypothesis, no human corollary |
| FISS-INF2 | Individual susceptibility variation in FISS is a research topic | B | open question |

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] Cats underutilized in comparative oncology vs dogs
- [x] Cats share model benefits: immunocompetent, shared environment, shorter lifespan, treatment-naïve
- [x] Oral SCC shares clinical and molecular features with human head/neck cancer
- [x] Feline mammary tumors usually malignant and aggressive
- [x] Triple-negative phenotype more common in cats than humans (2015 review)
- [x] FISS may model inflammation-driven tumorigenesis

### not_safe_to_promote_yet

- [ ] Specific molecular markers shared between feline and human cancers
- [ ] Triple-negative prevalence percentages
- [ ] Treatment recommendations based on comparative data
- [ ] Individual susceptibility genetic markers for FISS

### open_questions

1. What is the current (2020s) triple-negative prevalence in feline mammary tumors?
2. What specific molecular features are shared between feline oral SCC and human HNSCC?
3. What genetic factors influence individual FISS susceptibility?
4. Have any therapies been successfully tested using the feline oral SCC model?
5. What defines "triple-negative" in feline mammary tumors specifically?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 6 key comparative oncology claims |
| Evidence level | review (2015) |
| Key contribution | Three-model comparative oncology framework |
| Primary gap | Specific molecular details, recent prevalence data |
| Topic page targets | oral-squamous-cell-carcinoma.md, mammary-carcinoma.md, injection-site-sarcoma.md |
| Cross-branch value | High — provides comparative oncology rationale for 3 cancer types |
