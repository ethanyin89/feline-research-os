---
id: src-cancer-014-deep-extraction-round1
type: system
source_id: src-cancer-014
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-014

**Source:** Clinical Use of Molecular Biomarkers in Canine and Feline Oncology: Current and Future
**Journal:** Veterinary Sciences (MDPI, Open Access) (2024)
**DOI:** 10.3390/vetsci11050199
**PMID:** 38787171
**Evidence Level:** review

## Phase 0: Context

**Access status:** Open access via MDPI. Full abstract in source card.

**Source scope:** Comprehensive 2024 review on clinical use of molecular biomarkers in veterinary oncology, covering both dogs and cats.

**Framework value:** Provides a classification system for biomarker utility (diagnostic, prognostic, predictive, screening) applicable across cancer types.

## Phase 1: Sequential Micro-Analysis

### 1.1 Biomarker Classification Framework

| Biomarker Class | Clinical Utility |
|-----------------|------------------|
| Diagnostic | Identify cancer type/subtype |
| Prognostic | Predict disease outcome |
| Predictive | Predict response to specific therapy |
| Screening | Early detection in asymptomatic patients |

**Key insight:** This four-class framework helps organize molecular biomarker evidence across cancer types.

### 1.2 Biomarker Types

| Type | Description |
|------|-------------|
| Somatic | Acquired mutations in tumor cells |
| Germline | Inherited predisposition variants |

| Source | Method |
|--------|--------|
| Tissues | Biopsy, surgical samples |
| Body fluids | Liquid biopsy (blood, urine, etc.) |

### 1.3 Field Status (2024)

| Aspect | Assessment |
|--------|------------|
| Adoption level | "gaining traction as part of standard practice" |
| Trajectory | "molecular biomarkers will become mainstay" |
| Current state | Available tests for dogs and cats in clinical settings |
| Challenge | "bench to bedside" translation barriers |

**Key insight:** Precision oncology is transitioning from research to clinical practice in veterinary medicine.

### 1.4 Translation Challenges

| Challenge | Description |
|-----------|-------------|
| Discovery to adoption | Gap between finding biomarker and clinical use |
| Clinician adoption | Veterinarians need to integrate genomics |
| Infrastructure | Testing availability and cost |
| Evidence base | Clinical validation for each biomarker |

## Phase 2: Theme Reconstruction

### Theme A: Precision Medicine Framework

This review establishes a precision medicine framework for veterinary oncology analogous to human cancer care:
- Molecular profiling of tumors
- Biomarker-guided treatment selection
- Individualized prognosis assessment

### Theme B: Biomarker Utility Classification

The four-class system (diagnostic/prognostic/predictive/screening) provides a framework for evaluating any molecular biomarker:
- **Diagnostic:** What cancer is this?
- **Prognostic:** How will it behave?
- **Predictive:** Will treatment X work?
- **Screening:** Is there cancer present?

### Theme C: Current vs Future

The review distinguishes:
- **Currently available:** Tests in clinical use for dogs/cats
- **Emerging:** Promising biomarkers not yet in routine practice
- **Future:** Anticipated trajectory toward mainstay use

**Boundary:** Specific biomarkers per cancer type require full-text extraction.

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/index.md (Molecular Testing section)

**Claims to add:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| BIO1 | Molecular biomarkers in veterinary oncology are classified as diagnostic, prognostic, predictive, or screening | B | framework from 2024 review |
| BIO2 | Biomarkers can be somatic (tumor-acquired) or germline (inherited) | B | molecular genetics context |
| BIO3 | Biomarkers can be detected from tissues or body fluids (liquid biopsy) | B | testing modality |
| BIO4 | Precision oncology is "gaining traction" in veterinary practice (2024) | B | field status assessment |

**Section to add:** Molecular Biomarkers and Precision Oncology

**Boundary rules:**
- This provides framework, not specific biomarker recommendations
- Full-text needed for specific biomarker-cancer type mappings
- Do not recommend specific genetic tests without additional sources
- Frame as emerging field with translation challenges

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] Biomarker classification framework (diagnostic/prognostic/predictive/screening)
- [x] Somatic vs germline distinction
- [x] Tissue vs liquid biopsy sources
- [x] Field is "gaining traction" in standard practice (2024)
- [x] Translation challenges exist (bench to bedside)

### not_safe_to_promote_yet

- [ ] Specific biomarkers for feline cancers
- [ ] Testing recommendations
- [ ] Cost/availability information
- [ ] Clinical validation data for specific biomarkers

### open_questions

1. What specific biomarkers are available for feline lymphoma?
2. What biomarkers are available for feline mammary carcinoma?
3. What is the cost and availability of veterinary molecular testing?
4. Which labs offer feline cancer genomic profiling?
5. What is the clinical validation level for each available test?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 4 framework-level claims |
| Evidence level | review (2024, MDPI open access) |
| Key contribution | Biomarker classification framework, field status |
| Primary gap | Specific biomarker-cancer mappings |
| Topic page targets | cancer/index.md (molecular testing section) |
| Framework value | High — organizes biomarker evidence |
