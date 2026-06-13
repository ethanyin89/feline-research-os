---
id: src-cancer-049-deep-extraction-round1
type: system
source_id: src-cancer-049
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-049

**Source:** TiHo-0906: a new feline mammary cancer cell line with molecular, morphological, and immunocytological characteristics of epithelial to mesenchymal transition
**Journal:** Scientific Reports (2018)
**DOI:** 10.1038/s41598-018-31682-1
**PMID:** 30185896
**Evidence Level:** original-study (cell line characterization)

## Phase 0: Context

**Access status:** Open access via Nature Scientific Reports.

**Source scope:** 2018 cell line establishment study characterizing TiHo-0906, a feline mammary cancer cell line with EMT features.

**Key contribution:** Provides a validated research model for EMT-type feline mammary carcinoma with human metaplastic breast cancer parallels.

**Critical boundary:** In vitro cell line data only. Not clinical evidence.

## Phase 1: Sequential Micro-Analysis

### 1.1 Cell Line Origin

| Parameter | Value |
|-----------|-------|
| Cell line name | TiHoCMglAdcar0906 (TiHo-0906) |
| Source tumor | Feline mammary carcinoma |
| Tumor characteristics | Anaplastic, malignant spindle cells |
| Human counterpart | Metaplastic breast carcinoma, spindle-cell subtype |

### 1.2 Molecular Characterization

| Marker | Finding |
|--------|---------|
| HMGA2 | High expression |
| CD44 | High expression |
| Phenotype | Mixed epithelial/mesenchymal |

**EMT signature:** HMGA2 and CD44 are established EMT markers; high expression confirms EMT-like state.

### 1.3 Copy Number Variations

CNVs affected regions containing these cancer-associated genes:

| Gene | Pathway/Function |
|------|------------------|
| AKT1 | PI3K/AKT signaling (survival, proliferation) |
| GATA3 | Luminal differentiation (loss → poor prognosis) |
| CCND2 | Cell cycle (cyclin D2) |
| CDK4 | Cell cycle (G1/S transition) |
| ZEB1 | EMT transcription factor |
| KRAS | RAS/MAPK signaling |
| HMGA2 | EMT, stemness |
| ESRP1 | Epithelial splicing |
| MTDH | Metastasis, AKT activation |
| YWHAZ | 14-3-3 protein (signaling scaffold) |
| MYC | Oncogenic transcription factor |

**Pattern:** CNV landscape overlaps with human metaplastic breast cancer.

### 1.4 Functional Properties

| Property | Finding |
|----------|---------|
| Growth | Stable during subculturing |
| Migration | Stable during subculturing |
| Doxorubicin IC50 (low passage) | 99.97 nM |
| Doxorubicin IC50 (high passage) | 41.22 nM |
| Resistance ratio | Low-passage 2× more resistant |

**Drug resistance note:** Early-passage cells more resistant may reflect EMT-associated chemoresistance; high-passage cells may lose EMT features.

## Phase 2: Theme Reconstruction

### Theme A: EMT Model Validation

TiHo-0906 captures EMT phenotype:
- Morphology: spindle-cell (mesenchymal)
- Markers: HMGA2+, CD44+ (EMT markers)
- CNVs: ZEB1, ESRP1 regions affected
- Behavior: migratory, chemoresistant

**Value:** Enables study of EMT mechanisms and drug resistance in feline context.

### Theme B: Comparative Oncology

Parallels to human metaplastic breast cancer:
- Spindle-cell morphology
- EMT gene signature
- Overlapping CNV patterns
- Both are aggressive, treatment-resistant subtypes

**Value:** FMC as spontaneous model for human MPBC research.

### Theme C: Chemoresistance Mechanism

Doxorubicin resistance in low-passage cells suggests:
- EMT-associated drug resistance
- Passage number affects drug sensitivity
- Early-passage may better reflect primary tumor biology

**Boundary:** In vitro only; clinical translation not established.

### Theme D: Research Tool Availability

TiHo-0906 provides:
- Validated cell line for FMC research
- EMT model for drug screening
- Comparative oncology tool
- Stable growth/migration characteristics

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC-MODEL1 | TiHo-0906 is a validated EMT-type FMC cell line | C | in vitro model |
| MC-EMT1 | EMT-type FMC shows high HMGA2 and CD44 expression | C | cell line data |
| MC-RES1 | EMT-type FMC cells show doxorubicin resistance | C | in vitro, passage-dependent |

**Section to update:** Research Models / Molecular Subtypes

**Boundary rules:**
- Cell line evidence only
- Cannot predict clinical treatment response
- Cannot establish patient-level prognosis
- Useful for mechanism/drug screening research

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] TiHo-0906 is an available FMC cell line with EMT features
- [x] EMT markers (HMGA2, CD44) are expressed in this model
- [x] CNV patterns overlap with human metaplastic breast cancer
- [x] Doxorubicin resistance observed in early-passage cells

### not_safe_to_promote_yet

- [ ] Clinical relevance of EMT markers in patient tumors
- [ ] Doxorubicin resistance prediction in clinical cases
- [ ] Treatment recommendations based on EMT status
- [ ] Prognosis based on HMGA2/CD44 expression

### open_questions

1. Does in vivo chemoresistance correlate with EMT markers?
2. Can EMT status predict clinical doxorubicin response?
3. Are other FMC cell lines available for comparison?
4. What passage number best represents clinical biology?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 3 research model claims |
| Evidence level | original-study (cell line characterization) |
| Key contribution | Validated EMT-type FMC cell line |
| Primary gap | Clinical translation |
| Topic page targets | mammary-carcinoma.md (research models) |
| Cross-reference | Complements src-cancer-031 (EMT/CSC in OSCC) |
