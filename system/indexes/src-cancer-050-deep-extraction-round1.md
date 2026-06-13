---
id: src-cancer-050-deep-extraction-round1
type: system
source_id: src-cancer-050
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-050

**Source:** Feline mammary carcinomas as a model for human breast cancer. II. Comparison of in vivo and in vitro adriamycin sensitivity
**Journal:** Anticancer Research (1989)
**PMID:** 2817785
**Evidence Level:** original-study (comparative oncology)

## Phase 0: Context

**Access status:** Abstract available from PubMed. Historical paper from 1989.

**Source scope:** Comparative oncology study validating FMC as a model for human breast cancer drug sensitivity testing using adriamycin (doxorubicin).

**Historical importance:** Early evidence for FMC as a comparative oncology model with clinical drug testing methodology.

**Critical boundary:** Historical (1989). Does not establish modern chemotherapy protocols.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| Drug | Adriamycin (doxorubicin) |
| In vitro method | 20 tumor islands tested at 0.25-2.00 µg/ml |
| In vivo method | Tumor left in situ after biopsy |
| In vivo dosing | 5 IV injections at 30 mg/m² |
| Goal | Compare in vitro sensitivity with in vivo response |

### 1.2 In Vitro Results

| Adriamycin Concentration | Metric | Value |
|--------------------------|--------|-------|
| 2.00 µg/ml | Sensitivity | 100% |
| 1.00 µg/ml | Specificity | 75% |

**Note:** Sensitivity = ability to detect responsive tumors; specificity = ability to correctly classify resistant tumors.

### 1.3 Acquired Resistance

| Finding | Detail |
|---------|--------|
| Observation | Tumors recurring after treatment showed acquired resistance |
| Method | In vitro testing of recurrent tumor tissue |
| Implication | Drug resistance develops with treatment failure |

**Clinical relevance:** Demonstrates that FMC, like human breast cancer, develops acquired chemoresistance.

## Phase 2: Theme Reconstruction

### Theme A: Comparative Oncology Validation

FMC as human breast cancer model:
- Similar adriamycin sensitivity patterns
- In vitro testing predicts in vivo response
- Acquired resistance parallels human disease
- Supports use of FMC in drug development

### Theme B: In Vitro Sensitivity Testing

Tumor island method:
- Feasible for drug sensitivity screening
- High sensitivity at optimal concentration
- Reasonable specificity
- Could guide clinical decisions (historical context)

**Boundary:** 1989 methodology; modern methods differ.

### Theme C: Acquired Drug Resistance

Resistance mechanisms relevant to both species:
- Recurrent tumors become resistant
- Supports multi-drug approaches
- Highlights treatment complexity

### Theme D: Adriamycin Historical Context

1989 adriamycin use:
- 30 mg/m² × 5 IV doses was the tested protocol
- Represents historical standard of care
- Modern protocols may differ

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC-MODEL2 | FMC shows in vitro/in vivo adriamycin sensitivity correlation | B | historical, 1989 |
| MC-RES2 | FMC develops acquired adriamycin resistance in recurrent tumors | B | historical observation |
| MC-COMP1 | FMC validated as comparative oncology model for drug testing | B | methodological |

**Section to update:** Historical Context / Chemotherapy Evidence

**Boundary rules:**
- Historical evidence (1989)
- Comparative oncology focus
- Not modern treatment guidance
- Methodology has evolved

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] FMC can model human breast cancer drug sensitivity
- [x] In vitro sensitivity correlates with in vivo response
- [x] Acquired resistance develops in recurrent FMC tumors
- [x] Historical doxorubicin protocols used 30 mg/m² dosing

### not_safe_to_promote_yet

- [ ] Modern doxorubicin protocols for FMC
- [ ] Expected response rates to doxorubicin
- [ ] Comparison with current standard of care
- [ ] Survival benefit from doxorubicin in FMC

### open_questions

1. What are current doxorubicin protocols for FMC?
2. How has in vitro sensitivity testing evolved?
3. What resistance mechanisms are now understood?
4. Is doxorubicin still used in FMC treatment?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 3 historical/methodological claims |
| Evidence level | original-study (comparative oncology) |
| Key contribution | Validated FMC as drug sensitivity model |
| Primary gap | Modern treatment protocols |
| Topic page targets | mammary-carcinoma.md (historical, chemotherapy) |
| Cross-reference | Related to src-cancer-049 (doxorubicin resistance) |
