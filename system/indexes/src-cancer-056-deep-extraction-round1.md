---
id: src-cancer-056-deep-extraction-round1
type: system
source_id: src-cancer-056
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-056

**Source:** Androgen receptor and FOXA1 coexpression define a "luminal-AR" subtype of feline mammary carcinomas, spontaneous models of breast cancer
**Journal:** BMC Cancer (2019)
**DOI:** 10.1186/s12885-019-6483-6
**PMID:** 31888566
**Evidence Level:** original-study (molecular subtyping, prognostic)

## Phase 0: Context

**Access status:** Open access via BMC (PMC6937649).

**Source scope:** 2019 retrospective cohort study of 180 FMCs evaluating AR/FOXA1 coexpression to define a luminal-AR-like subtype within triple-negative tumors.

**Key contribution:** Identifies feline equivalent of human luminal-AR TNBC with better prognosis.

**Critical boundary:** Prognostic marker study. Not treatment selection.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| Cohort | 180 female cats with FMC |
| Follow-up | 2 years post-mastectomy |
| Methods | Automated immunohistochemistry |
| Markers | AR, FOXA1, ER, PR, Ki-67, HER2, CK14 |

### 1.2 Subtype Distribution

| Subtype | Count | Percentage |
|---------|-------|------------|
| Luminal (ER+ and/or PR+) | 57 | 32% |
| Triple-negative (ER-/PR-/HER2-) | 123 | 68% |

### 1.3 Marker Positivity

| Marker | Positive Cases | Rate |
|--------|----------------|------|
| AR overexpression | 33/180 | 18% |
| FOXA1 ≥1% | 64/180 | 36% |

### 1.4 Prognostic Associations

| Marker | Outcome |
|--------|---------|
| AR overexpression | Longer DFS, OS, CSS |
| FOXA1 ≥1% | Longer DFS, OS, CSS |

**Key finding:** Both AR and FOXA1 positivity associated with better survival.

### 1.5 Luminal-AR-like Subtype

**Within triple-negative FMCs:**

| Subtype | Definition | n | Prognosis |
|---------|------------|---|-----------|
| Luminal-AR-like | AR+/FOXA1+/CK14- | 7 | Better CSS |
| Basal-like | AR+/FOXA1-/CK14+ | 46 | Worse CSS |

**Independent of:** Tumor size and nodal stage.

**Human parallel:** Luminal-AR TNBC.

## Phase 2: Theme Reconstruction

### Theme A: TNBC Heterogeneity

Not all TNBC is the same:
- Basal-like (CK14+): aggressive, poor prognosis
- Luminal-AR-like (AR+/FOXA1+): better outcomes
- Parallels human TNBC molecular subtypes

### Theme B: Prognostic Markers

AR and FOXA1 as prognostic markers:
- AR overexpression → better survival
- FOXA1 positivity → better survival
- Combined: identifies less aggressive subset

### Theme C: Comparative Oncology

Feline luminal-AR TNBC model:
- Parallels human luminal-AR subtype
- Spontaneous disease (not xenograft)
- May be useful for AR-targeted therapy research

### Theme D: Clinical Implications

Potential future directions:
- AR as therapeutic target in AR+ FMC
- FOXA1 in prognosis stratification
- Subtype-specific treatment approaches

**Boundary:** Research direction, not current treatment.

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC-SUB3 | AR overexpression (18%) is associated with better survival in FMC | A | n=180 |
| MC-SUB4 | FOXA1 positivity (36%) is associated with better survival in FMC | A | n=180 |
| MC-SUB5 | Luminal-AR-like subtype (AR+/FOXA1+/CK14-) has better prognosis than basal-like TNBC | A | within TNBC, n=7 vs 46 |
| MC-SUB6 | FMC shows molecular subtypes paralleling human breast cancer | B | comparative oncology |

**Section to update:** Molecular Subtypes / Prognostic Markers

**Boundary rules:**
- Prognostic marker evidence
- Same cohort as src-cancer-043 (Treg study)
- Not AR-targeted treatment validation
- Small luminal-AR subgroup (n=7)

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] AR overexpression associated with better FMC survival
- [x] FOXA1 positivity associated with better FMC survival
- [x] Within TNBC, AR+/FOXA1+/CK14- subset has better prognosis
- [x] Feline TNBC shows molecular heterogeneity like human TNBC

### not_safe_to_promote_yet

- [ ] AR-targeted therapy efficacy in FMC
- [ ] Treatment recommendations based on AR/FOXA1 status
- [ ] Prevalence of luminal-AR FMC (very small subset)
- [ ] Clinical utility of subtyping

### open_questions

1. Are AR-targeted therapies effective in AR+ FMC?
2. What is the optimal marker threshold for clinical use?
3. Does AR status predict response to hormonal therapy?
4. Is the luminal-AR subtype replicable in other cohorts?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 4 molecular subtyping/prognostic claims |
| Evidence level | original-study (prognostic, n=180) |
| Key contribution | Defined luminal-AR-like FMC subtype |
| Primary gap | Treatment implications |
| Topic page targets | mammary-carcinoma.md (subtypes) |
| Cross-reference | Same cohort as src-cancer-043 (Tregs) |
