---
id: src-cancer-012-deep-extraction-round1
type: system
source_id: src-cancer-012
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-012

**Source:** Prognostic factors for feline mammary tumors
**Journal:** Not specified (1984)
**DOI:** None available
**PMID:** 6746390
**Evidence Level:** original-study (retrospective)

## Phase 0: Context

**Access status:** Full abstract available in source card.

**Source scope:** Classic 1984 study of 100 cats with malignant mammary tumors establishing prognostic factors.

**Historical importance:** This is foundational work establishing tumor size as the primary prognostic factor for feline mammary tumors. Despite being 40 years old, the core finding remains widely cited.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Characteristics

| Parameter | Value |
|-----------|-------|
| Population | 100 cats with malignant mammary tumors |
| Staging system | WHO clinical staging |
| Design | Retrospective case review |
| Year | 1984 |
| Data collected | Age, breed, tumor size, surgery type, histology, DFI, survival, cause of death |

### 1.2 Significant Prognostic Factors

| Factor | Statistical Significance | Finding |
|--------|-------------------------|---------|
| Tumor size | P < 0.0001 | Most significant prognostic factor |
| Small tumors (1-8 cm³) | — | Best prognosis |

**Key insight:** Tumor size is overwhelmingly the most important prognostic factor, with very high statistical significance.

### 1.3 Non-Prognostic Factors

| Factor | Finding |
|--------|---------|
| Age (≤10 vs >10 years) | No prognostic value |
| Breed | No prognostic value |

**Key insight:** Neither age nor breed affects prognosis — tumor biology (size) matters most.

### 1.4 Surgery Type Effects

| Outcome | Surgery Effect | P-value |
|---------|---------------|---------|
| Disease-free interval | Significant difference | P < 0.01 |
| Survival time | No significant difference | — |

**Key insight:** Radical vs conservative surgery affects time to recurrence but not overall survival. This has implications for surgical planning.

## Phase 2: Theme Reconstruction

### Theme A: Tumor Size as Primary Prognostic Factor

The overwhelming significance of tumor size (P<0.0001) establishes early detection as the key to improving outcomes. Small tumors (1-8 cm³) have best prognosis.

**Clinical implication:** Regular mammary examination may enable earlier detection and better outcomes.

### Theme B: Surgery Type Dissociation

The finding that surgery type affects disease-free interval but not survival is important:
- Radical surgery may delay recurrence
- But ultimately does not change survival
- Quality-of-life considerations may favor conservative approaches

**Boundary:** This 1984 finding may not reflect current surgical techniques or adjuvant therapy options.

### Theme C: Age and Breed Not Prognostic

Contrary to possible assumptions:
- Older cats (>10 years) don't have worse prognosis
- No breed predisposition to worse outcomes

This focuses prognostic assessment on tumor characteristics, not patient demographics.

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC-PROG1 | Tumor size is the most significant prognostic factor for feline mammary tumors (P<0.0001) | B | 1984 foundational study, 100 cats |
| MC-PROG2 | Small mammary tumors (1-8 cm³) have best prognosis | B | size threshold from 1984 study |
| MC-PROG3 | Age and breed are not prognostic factors for feline mammary tumors | B | 1984 study finding |
| MC-PROG4 | Surgery type (conservative vs radical) affects disease-free interval (P<0.01) but not survival | B | surgical planning implication |

**Section to add/update:** Prognostic Factors

**Boundary rules:**
- Note 1984 study date
- Frame tumor size finding as foundational/widely cited
- Acknowledge surgical techniques may have evolved
- Do not use to recommend specific surgical approaches

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] Tumor size is most significant prognostic factor (P<0.0001)
- [x] Small tumors (1-8 cm³) have best prognosis
- [x] Age is not a prognostic factor
- [x] Breed is not a prognostic factor
- [x] Surgery type affects DFI but not survival

### not_safe_to_promote_yet

- [ ] Specific survival times by tumor size
- [ ] Current surgical recommendations
- [ ] Comparison with modern adjuvant therapies
- [ ] Molecular subtype effects (not studied in 1984)

### open_questions

1. Have more recent studies confirmed the tumor size finding?
2. What survival times correspond to different size categories?
3. How do modern surgical techniques compare?
4. Does adjuvant chemotherapy change the surgery type finding?
5. Do molecular subtypes (triple-negative) modify prognosis?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 4 prognostic factor claims |
| Evidence level | retrospective study (1984, 100 cats) |
| Key contribution | Established tumor size as primary prognostic factor |
| Primary gap | 40-year-old study, modern validation needed |
| Topic page targets | mammary-carcinoma.md (prognostic factors) |
| Historical value | High — foundational prognostic study |
