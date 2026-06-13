---
id: src-cancer-042-deep-extraction-round1
type: system
source_id: src-cancer-042
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-042

**Source:** Biology of feline leukemia virus in the natural environment
**Journal:** Cancer Research (1976)
**PMID:** 175919
**Evidence Level:** original-study (landmark epidemiology)

## Phase 0: Context

**Access status:** Abstract available from PubMed.

**Source scope:** Foundational 1976 study establishing FeLV epidemiology, test-and-removal control strategy, and cancer association in natural cat populations.

**Historical importance:** This is one of the earliest comprehensive FeLV control studies. Published in Cancer Research. Established the framework for FeLV eradication programs.

## Phase 1: Sequential Micro-Analysis

### 1.1 Historical Context

| Year | Event |
|------|-------|
| 1964 | FeLV discovered in cluster of cats with lymphosarcoma |
| 1976 | This study published — test-and-removal strategy validated |
| ~1985 | Commercial FeLV vaccine available |

### 1.2 Study Design

| Parameter | Value |
|-----------|-------|
| Cats tested | >2000 |
| Test method | Immunofluorescent test |
| Validation | 3 different test procedures |
| Study type | Seroepidemiological |

### 1.3 Test-and-Removal Program Results

| Household Group | Intervention | Outcome |
|-----------------|--------------|---------|
| 45 households | FeLV+ cats removed | Spread controlled |
| 25 households | FeLV+ cats remained | 12% of uninfected cats became infected |

**Key finding:** Test-and-removal is effective; leaving FeLV+ cats results in ongoing transmission (12% infection rate).

### 1.4 Control Strategy Elements

| Element | Status (1976) |
|---------|---------------|
| Testing | IFA available |
| Removal | Effective control |
| Vaccination | Experimental (attenuated FeLV) |
| Ultimate control | Awaited vaccine development |

### 1.5 Human Safety

| Finding | Evidence |
|---------|----------|
| FeLV infects humans | No evidence |
| Zoonotic risk | Not demonstrated |

## Phase 2: Theme Reconstruction

### Theme A: FeLV-Cancer Link Established

The clustering of lymphosarcoma cases led to FeLV discovery:
- Cancer clustering → infectious etiology hypothesis
- FeLV confirmed as lymphosarcoma cause
- Viral oncology foundation

### Theme B: Test-and-Removal Strategy

This study established the control paradigm:
1. Test all cats in household
2. Remove FeLV+ cats
3. Retest at intervals
4. Maintain negative status

This strategy became the standard until vaccination.

### Theme C: Household Transmission

12% infection rate when FeLV+ cats remain demonstrates:
- Close contact transmission
- Multi-cat household risk
- Need for segregation or removal

### Theme D: Vaccine Anticipation

The 1976 paper noted:
- Ultimate control awaits effective vaccine
- Experimental immunization underway
- Set stage for vaccine development (achieved ~1985)

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/lymphoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| LY-HIST2 | FeLV discovered in 1964 lymphosarcoma cluster | A | historical fact |
| LY-HIST3 | Test-and-removal controlled FeLV spread (1976 study) | B | historical context |
| LY-HIST4 | 12% infection rate when FeLV+ cats remained in household | A | 1976 data |
| LY-SAFE1 | No evidence FeLV infects humans (1976) | B | human safety |

**Section to update:** FeLV Etiology / Historical Context

**Boundary rules:**
- 1976 data — pre-vaccine era
- Historical foundation, not current protocol
- Modern FeLV testing and vaccination supersede test-and-removal

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] FeLV discovered 1964 in lymphosarcoma cluster
- [x] >2000 cats tested in seroepidemiological study
- [x] Test-and-removal controlled FeLV spread
- [x] 12% infection rate when FeLV+ cats remained
- [x] No evidence of human FeLV infection

### not_safe_to_promote_yet

- [ ] Current FeLV prevalence (1976 data outdated)
- [ ] Current testing protocols
- [ ] Vaccine recommendations
- [ ] Modern FeLV management

### open_questions

1. How did FeLV prevalence change after vaccine introduction?
2. What is current household transmission rate?
3. Is test-and-removal still used in any contexts?
4. What is current FeLV-associated lymphoma incidence?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 4 historical/epidemiological claims |
| Evidence level | original-study (1976, Cancer Research) |
| Key contribution | Established test-and-removal strategy; quantified transmission |
| Primary gap | Pre-vaccine era — modern data needed |
| Topic page targets | lymphoma.md (FeLV etiology, historical) |
| Cross-reference | Links to src-cancer-065 (FeLV-shift) |
