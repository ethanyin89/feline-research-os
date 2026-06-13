---
id: src-cancer-069-deep-extraction-round1
type: system
source_id: src-cancer-069
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-069

**Source:** Spontaneous feline mammary intraepithelial lesions as a model for human estrogen receptor- and progesterone receptor-negative breast lesions
**Journal:** BMC Cancer (2010)
**DOI:** 10.1186/1471-2407-10-156
**PMID:** 20412586
**Evidence Level:** original-study (precursor lesion characterization)

## Phase 0: Context

**Access status:** Open access via BMC Cancer.

**Source scope:** 2010 study characterizing feline mammary intraepithelial lesions (IELs) in 203 specimens, demonstrating ER/PR-negative phenotype in precursor lesions.

**Key contribution:** Establishes that feline mammary precursor lesions are also hormone receptor-negative.

**Critical boundary:** Pathological characterization. Not clinical management.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| Specimens | 205 from 203 female cats |
| Focus | Mammary intraepithelial lesions (IELs) |
| Methods | Histopathology, IHC (ER, PR, HER2) |

### 1.2 IEL Prevalence and Categories

| Category | Full Name | % of IELs |
|----------|-----------|-----------|
| UH | Usual hyperplasia | 27% |
| ADH | Atypical ductal hyperplasia | 29% |
| DCIS | Ductal carcinoma in situ | 44% |

**IEL prevalence:** 28% (57/203) of feline mammary specimens.

### 1.3 Cancer Association

| IEL Type | Cancer Association |
|----------|-------------------|
| UH | 47% benign, 53% associated with benign lesions |
| ADH + DCIS (atypical) | 91% associated with mammary cancer |

**Key finding:** Atypical IELs strongly associated with malignancy.

### 1.4 Hormone Receptor Status

| Marker | Finding |
|--------|---------|
| ER in intermediate/high-grade DCIS | Negative |
| PR in intermediate/high-grade DCIS | Negative |
| ER/PR in associated tumors | Negative |
| HER2 overexpression | 27% of IELs |

**Key finding:** ER/PR negativity present from precursor stage.

## Phase 2: Theme Reconstruction

### Theme A: Precursor Lesion Pathway

IEL spectrum in cats:
- UH → ADH → DCIS → invasive carcinoma
- Parallels human breast cancer progression
- 91% of atypical IELs associated with cancer
- Establishes ductal origin model

### Theme B: Early Hormone Receptor Loss

ER/PR negativity is early:
- Present in intermediate/high-grade DCIS
- Maintained in associated invasive tumors
- Not acquired during invasion
- Supports TNBC-like phenotype from start

### Theme C: Comparative Oncology Value

Cat as ER/PR-negative model:
- Histologically similar to human IELs
- Same hormone receptor loss pattern
- Spontaneous (not induced) lesions
- Valuable for studying ER/PR-negative progression

### Theme D: HER2 Expression

HER2 in IELs:
- 27% show overexpression
- Present in precursor stage
- May define subset with different biology
- Requires further characterization

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC-PATH1 | IELs found in 28% of feline mammary specimens | A | n=203 |
| MC-PATH2 | 91% of atypical IELs (ADH/DCIS) associated with mammary cancer | A | n=57 |
| MC-PATH3 | Intermediate/high-grade DCIS is ER/PR-negative | A | IHC data |
| MC-PATH4 | HER2 overexpression present in 27% of IELs | A | precursor lesion |
| MC-MODEL3 | Feline IELs parallel human IEL spectrum histologically | B | comparative pathology |

**Section to update:** Pathogenesis / Precursor Lesions

**Boundary rules:**
- Pathological characterization only
- Not clinical screening recommendations
- Supports TNBC model
- Does not establish treatment implications

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] IELs found in 28% of feline mammary specimens
- [x] 91% of atypical IELs associated with cancer
- [x] ER/PR negativity present from DCIS stage
- [x] HER2 overexpression in 27% of IELs
- [x] Feline IELs histologically similar to human

### not_safe_to_promote_yet

- [ ] Clinical screening for IELs
- [ ] Treatment of IELs
- [ ] Prognosis based on IEL features
- [ ] HER2-targeted therapy implications

### open_questions

1. Should feline mammary tissue be screened for IELs?
2. Does IEL presence predict contralateral cancer?
3. What determines progression from ADH to DCIS?
4. Are HER2+ IELs a distinct subset?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 5 pathogenesis claims |
| Evidence level | original-study (n=203) |
| Key contribution | Feline IELs are ER/PR-negative like invasive tumors |
| Primary gap | Clinical implications |
| Topic page targets | mammary-carcinoma.md (pathogenesis) |
| Cross-reference | Supports TNBC prevalence data (src-cancer-022, 043) |
