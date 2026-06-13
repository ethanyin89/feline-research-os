---
id: src-cancer-034-deep-extraction-round1
type: system
source_id: src-cancer-034
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-034

**Source:** Molecular Characterization of Feline COX-2 and Expression in Feline Mammary Carcinomas
**Journal:** Veterinary Pathology (2009)
**DOI:** 10.1354/vp.08-vp-0161-d-fl
**PMID:** 19176489
**Evidence Level:** original-study

## Phase 0: Context

**Access status:** Abstract available from PubMed. Journal access required for full-text.

**Source scope:** 2009 molecular characterization of feline COX-2 and expression analysis in 40 FMCs.

**Key contribution:** Establishes COX-2 expression prevalence (87%) in FMC — foundation for COX-2 inhibitor therapy rationale.

## Phase 1: Sequential Micro-Analysis

### 1.1 COX-2 Background

| Concept | Explanation |
|---------|-------------|
| COX-2 | Cyclooxygenase-2, inducible enzyme |
| Function | Rate-limiting enzyme in prostaglandin biosynthesis |
| Inflammation role | Upregulated in inflammatory conditions |
| Cancer role | Associated with tumorigenesis, angiogenesis, invasion |
| Therapeutic relevance | Target of NSAIDs (COX inhibitors) |

### 1.2 Molecular Characterization

| Finding | Value |
|---------|-------|
| Gene cloned | Feline COX-2 |
| Sequence determined | Primary structure |
| Species comparison | Confirms feline COX-2 as valid target |

### 1.3 Expression in FMC

| Parameter | Value |
|-----------|-------|
| Sample size | 40 feline mammary carcinomas |
| COX-2 positive | 35/40 (87%) |
| Detection method | Immunohistochemistry |
| Expression level | Strong in majority |

**Key finding:** 87% COX-2 expression rate is remarkably high and consistent with tumors that might respond to COX-2 inhibition.

### 1.4 Therapeutic Implications

| COX-2 Inhibitor | Status in Cats |
|-----------------|----------------|
| Meloxicam | Approved for cats (short-term) |
| Piroxicam | Used off-label in oncology |
| Celecoxib | Human drug, not veterinary approved |

**Rationale:** High COX-2 expression suggests these tumors might be susceptible to COX-2 inhibitor therapy, either alone or as adjuvant.

## Phase 2: Theme Reconstruction

### Theme A: COX-2 as Therapeutic Target

87% expression rate makes COX-2 a promising therapeutic target:
1. **Prevalence:** Majority of tumors express the target
2. **Drugs available:** NSAIDs already used in veterinary medicine
3. **Multi-modal potential:** Could combine with surgery/chemotherapy
4. **Anti-inflammatory benefit:** May reduce tumor-associated inflammation

### Theme B: Biomarker Potential

COX-2 expression could serve as:
- Predictive biomarker (predict response to COX inhibitors)
- Prognostic marker (if expression correlates with outcome)
- Patient selection criterion (for COX-2 inhibitor trials)

### Theme C: Evidence Gaps

Expression does not equal therapeutic response:
- No clinical trial data in this study
- No survival data by COX-2 status
- COX-2 inhibitor efficacy in FMC unproven
- Side effects of long-term COX-2 inhibition in cats (renal)

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC34 | 87% (35/40) of FMCs express COX-2 | A | single study, n=40 |
| MC35 | COX-2 is a potential therapeutic target in FMC | B | expression prevalence |
| MC36 | Feline COX-2 gene has been cloned and sequenced | A | molecular characterization |

**Section to update:** Molecular Markers / Therapeutic Targets

**Boundary rules:**
- Expression prevalence is validated
- Therapeutic efficacy NOT proven
- Do not recommend COX-2 inhibitors without clinical trial data
- Renal safety concerns for chronic NSAID use in cats

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] 87% of FMCs express COX-2
- [x] Feline COX-2 gene has been molecularly characterized
- [x] COX-2 is the rate-limiting enzyme in prostaglandin biosynthesis
- [x] COX-2 plays role in inflammation and tumorigenesis

### not_safe_to_promote_yet

- [ ] COX-2 inhibitor efficacy in FMC
- [ ] Specific COX-2 inhibitor recommendations
- [ ] Survival benefit from COX-2 inhibition
- [ ] Safety of long-term COX-2 inhibition in cats

### open_questions

1. Do COX-2 inhibitors improve FMC outcomes?
2. Does COX-2 expression correlate with prognosis?
3. Is COX-2 expression level (quantitative) clinically relevant?
4. What is the optimal COX-2 inhibitor for FMC (meloxicam vs piroxicam)?
5. Can COX-2 status guide therapy selection?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 3 molecular/expression claims |
| Evidence level | original-study (n=40) |
| Key contribution | 87% COX-2 expression establishes target prevalence |
| Primary gap | Clinical efficacy of COX-2 inhibitors |
| Topic page targets | mammary-carcinoma.md (molecular markers) |
| Therapeutic relevance | High — justifies COX-2 inhibitor investigation |
