---
id: src-cancer-072-deep-extraction-round1
type: system
source_id: src-cancer-072
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-072

**Source:** Satellite Noncoding RNAs (ncRNA) as Cancer Biomarkers? New Insights from FA-SAT ncRNA Molecular and Clinical Profiles in Feline Mammary Tumors
**Journal:** OMICS (2022)
**DOI:** 10.1089/omi.2022.0114
**PMID:** 36342778
**Evidence Level:** original-study (biomarker discovery)

## Phase 0: Context

**Access status:** Abstract available from PubMed.

**Source scope:** 2022 study evaluating FA-SAT satellite ncRNA as a potential biomarker in feline mammary tumors, correlating with clinicopathological parameters.

**Key contribution:** Novel ncRNA biomarker with multiple clinical correlations in FMC.

**Critical boundary:** Research-stage biomarker. Clinical utility not established.

## Phase 1: Sequential Micro-Analysis

### 1.1 Biomarker Background

| Parameter | Value |
|-----------|-------|
| Biomarker | FA-SAT satellite ncRNA |
| Location | Major satellite DNA of cat genome |
| Conservation | Also present in human genome |
| Molecules measured | FA-SAT DNA, long RNA, small RNA |

### 1.2 FA-SAT DNA Correlations

| Finding | Direction |
|---------|-----------|
| Lymphovascular invasion | Positive correlation |

### 1.3 FA-SAT Long RNA Correlations

| Parameter | Direction |
|-----------|-----------|
| Ki-67 index | Negative correlation |
| ER status | Positive correlation |
| ERBB2 RNA | Positive correlation |
| c-MYC RNA | Positive correlation |

**Note:** Lower Ki-67 with higher FA-SAT long RNA suggests association with less proliferative tumors.

### 1.4 FA-SAT Small RNA Correlations

| Parameter | Direction |
|-----------|-----------|
| Tumor size | Positive correlation |
| Skin ulceration | Positive correlation |

**Note:** Higher small RNA with worse clinical features.

## Phase 2: Theme Reconstruction

### Theme A: Novel ncRNA Biomarker

FA-SAT as potential marker:
- Multiple clinical correlations
- Different RNA species show different patterns
- May complement existing markers (ER, PR, HER2, Ki-67)
- Research direction for FMC molecular profiling

### Theme B: Complex Expression Patterns

Different FA-SAT forms have different associations:
- DNA: lymphovascular invasion
- Long RNA: ER+, lower Ki-67, ERBB2/c-MYC correlation
- Small RNA: larger tumors, ulceration

**Implication:** FA-SAT biology is complex; different forms may have different roles.

### Theme C: Comparative Oncology

Translational value:
- FA-SAT conserved in humans
- May enable human breast cancer research
- Cat as model for ncRNA biomarker development

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC-BIO1 | FA-SAT ncRNA is under investigation as a biomarker in FMC | C | research-stage |
| MC-BIO2 | FA-SAT DNA correlates with lymphovascular invasion | C | correlational |
| MC-BIO3 | FA-SAT long RNA correlates with ER status and ERBB2/c-MYC | C | correlational |

**Section to update:** Emerging Biomarkers / Research Directions

**Boundary rules:**
- Research-stage biomarker
- Correlational data only
- Clinical utility not established
- Not for clinical decision-making

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] FA-SAT ncRNA is being studied as a FMC biomarker
- [x] Multiple clinicopathological correlations observed
- [x] FA-SAT is conserved between cats and humans

### not_safe_to_promote_yet

- [ ] Clinical utility of FA-SAT testing
- [ ] Prognostic value validated
- [ ] Treatment selection based on FA-SAT
- [ ] Comparison with established markers

### open_questions

1. Does FA-SAT predict survival outcomes?
2. Can FA-SAT be measured in liquid biopsy?
3. What is the biological mechanism of FA-SAT in cancer?
4. Is FA-SAT validated in independent cohorts?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 3 emerging biomarker claims |
| Evidence level | original-study (biomarker discovery) |
| Key contribution | Novel ncRNA biomarker with clinical correlations |
| Primary gap | Clinical validation |
| Topic page targets | mammary-carcinoma.md (emerging biomarkers) |
| Cross-reference | Complements established markers (ER, Ki-67, HER2) |
