---
id: src-cancer-035-deep-extraction-round1
type: system
source_id: src-cancer-035
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-035

**Source:** Immunohistochemical Detection of Proteins Associated with Multidrug Resistance to Anti-Cancer Drugs in Canine and Feline Primary Pulmonary Carcinoma
**Journal:** Journal of Veterinary Medical Science (2010)
**DOI:** 10.1292/jvms.09-0519
**PMID:** 20086324
**Evidence Level:** original-study

## Phase 0: Context

**Access status:** Abstract available from PubMed. J-STAGE open access.

**Source scope:** 2010 study of multidrug resistance protein expression in canine (n=52) and feline (n=18) primary pulmonary carcinomas.

**Key contribution:** Explains inherent chemotherapy resistance in pulmonary carcinoma through MDR protein expression.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Canine | Feline |
|-----------|--------|--------|
| Sample size | 52 | 18 |
| Tumor type | Primary pulmonary carcinoma | Primary pulmonary carcinoma |
| Method | Immunohistochemistry | Immunohistochemistry |

### 1.2 MDR Proteins Evaluated

| Protein | Full Name | Function |
|---------|-----------|----------|
| PGP | P-glycoprotein | Drug efflux pump (removes chemotherapy from cells) |
| MRP | Multidrug resistance-related protein | Drug efflux, detoxification |
| LRP | Lung resistance-related protein | Nucleocytoplasmic drug transport |
| MT | Metallothionein | Heavy metal binding, oxidative stress protection |

### 1.3 Expression Findings

| Protein | Feline Expression |
|---------|-------------------|
| PGP | Frequent |
| MRP | Frequent |
| LRP | Frequent |
| MT | ~50% |

**Key finding:** Overlapping expression of multiple MDR proteins in all positive cases indicates robust, multi-mechanism drug resistance.

### 1.4 Clinical Implications

| Finding | Implication |
|---------|-------------|
| High MDR expression | Poor response to standard chemotherapy expected |
| Multiple mechanisms | Single MDR inhibitor unlikely to overcome |
| Inherent resistance | Not acquired — present before treatment |

## Phase 2: Theme Reconstruction

### Theme A: Pulmonary Carcinoma as Drug-Resistant Cancer

This study explains why feline pulmonary carcinoma responds poorly to chemotherapy:
- Multiple efflux pumps (PGP, MRP) actively remove drugs
- LRP provides additional resistance mechanism
- Metallothionein protects against oxidative stress from drugs

### Theme B: Implications for Chemotherapy Selection

Understanding MDR profile suggests:
- Standard chemotherapy may be ineffective
- Surgery remains primary treatment modality
- MDR-overcoming strategies needed (if any)
- Palliation may be more realistic than cure

### Theme C: Cross-Cancer Relevance

MDR protein expression may affect other feline cancers:
- These proteins are not specific to pulmonary carcinoma
- May explain chemotherapy resistance in other tumor types
- Could guide biomarker testing before chemotherapy

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/index.md (general cancer section)

**Note:** Pulmonary carcinoma may not have its own topic page yet. Claims should go to general cancer discussion of chemotherapy resistance.

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| GC-MDR1 | Feline pulmonary carcinomas frequently express PGP, MRP, LRP MDR proteins | A | n=18 feline cases |
| GC-MDR2 | ~50% of feline pulmonary carcinomas express metallothionein | A | expression prevalence |
| GC-MDR3 | Inherent MDR expression may explain poor chemotherapy response in pulmonary carcinoma | B | mechanistic inference |

**Section to update:** Treatment Resistance / Chemotherapy Considerations

**Boundary rules:**
- Pulmonary carcinoma specific (n=18)
- Cannot generalize to all feline cancers
- Does not recommend specific treatment modifications

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] Feline pulmonary carcinomas frequently express PGP
- [x] Feline pulmonary carcinomas frequently express MRP
- [x] Feline pulmonary carcinomas frequently express LRP
- [x] ~50% express metallothionein
- [x] Overlapping MDR expression suggests robust drug resistance

### not_safe_to_promote_yet

- [ ] Specific chemotherapy agent recommendations
- [ ] MDR inhibitor therapy suggestions
- [ ] Prognostic value of MDR expression
- [ ] Treatment modification based on MDR status

### open_questions

1. Does MDR expression correlate with chemotherapy response in feline tumors?
2. Are MDR inhibitors (like verapamil) effective in veterinary oncology?
3. Do other feline cancers show similar MDR profiles?
4. Can MDR status guide treatment selection?
5. Is MDR expression prognostic in feline pulmonary carcinoma?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 3 chemotherapy resistance claims |
| Evidence level | original-study (n=18 feline) |
| Key contribution | MDR protein expression explains chemoresistance |
| Primary gap | Clinical response data by MDR status |
| Topic page targets | index.md (general cancer, chemotherapy resistance) |
| Cancer type | Pulmonary carcinoma (may need dedicated page) |
