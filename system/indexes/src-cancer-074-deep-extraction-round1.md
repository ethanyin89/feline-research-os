---
id: src-cancer-074-deep-extraction-round1
type: system
source_id: src-cancer-074
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-074

**Source:** Investigation of immune cell markers in feline oral squamous cell carcinoma
**Journal:** Veterinary Immunology and Immunopathology (2018)
**DOI:** 10.1016/j.vetimm.2018.06.011
**PMID:** 30078599
**Evidence Level:** original-study (immunopathology)

## Phase 0: Context

**Access status:** Abstract available from PubMed.

**Source scope:** 2018 study characterizing immune cell infiltrates in FOSCC using IHC (n=12) and flow cytometry for circulating Tregs (n=9).

**Key contribution:** First comprehensive immune cell profiling of FOSCC tumor microenvironment; supports comparative oncology with human HNSCC.

**Critical boundary:** Small sample sizes. Prognostic correlations not detected.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Cohort | N | Analysis |
|--------|---|----------|
| IHC cohort | 12 | Tissue markers: CD3, CD79a, CD20, FoxP3, COX-2 |
| Flow cytometry cohort | 9 | Circulating CD4+FoxP3+ T cells |
| Histology | — | 75% conventional SCC (50% well-diff, 50% mod-diff) |

### 1.2 Tumor-Infiltrating Lymphocytes (TILs)

| Marker | Prevalence | Location |
|--------|------------|----------|
| CD3+ (T cells) | 92% (11/12) | Epithelium + stroma |
| FoxP3+ (Tregs) | 57% (7/12) | Epithelium + stroma |
| CD79a/CD20+ (B cells) | Present | Stroma only |

**Context:** High T cell infiltration but majority are not Tregs (92% vs 57%). B cells restricted to stroma.

### 1.3 Regulatory T Cells (Tregs)

| Finding | Detail |
|---------|--------|
| Tissue Tregs | FoxP3+ in 57% of tumors, both compartments |
| Circulating Tregs | CD4+FoxP3+ elevated vs healthy controls |
| Statistical significance | P=0.045 |

**Implication:** Both local and systemic Treg enrichment suggests immunosuppressive tumor microenvironment.

### 1.4 COX-2 Expression

| Finding | Detail |
|---------|--------|
| Prevalence | 75% positive |
| Intensity | Weak staining |
| Location | Epithelium + stroma |

**Note:** Weaker COX-2 expression than some previous reports; may reflect antibody or scoring differences.

## Phase 2: Theme Reconstruction

### Theme A: Immunosuppressive Microenvironment

FOSCC immune profile:
- High T cell infiltration (92%)
- Significant Treg component (57%)
- Systemic Treg elevation
- Suggests immune evasion mechanism

**Clinical implication:** Treg depletion or checkpoint inhibition may be therapeutic strategies.

### Theme B: Comparative Oncology Support

FOSCC parallels human HNSCC:
- T cell infiltration patterns similar
- Treg enrichment observed in both
- COX-2 expression in both
- Supports FOSCC as immunotherapy model

### Theme C: Inflammation Role

COX-2 in FOSCC:
- 75% positive confirms inflammation involvement
- Lower intensity than some reports
- Complements mPGES1 findings (src-cancer-073)
- Potential COX-2 inhibitor target

### Theme D: Translational Immunotherapy

Immunotherapy implications:
- Treg depletion strategies
- Anti-PD-1/PD-L1 checkpoint inhibitors
- COX-2 inhibitors as adjunct
- FOSCC as preclinical model for human HNSCC immunotherapy

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/oral-squamous-cell-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| OSCC-IMM1 | 92% of FOSCC show CD3+ T cell infiltrates | A | n=12 |
| OSCC-IMM2 | 57% of FOSCC have FoxP3+ Treg infiltrates | A | n=12 |
| OSCC-IMM3 | Circulating Tregs elevated in FOSCC patients vs controls | A | n=9, P=0.045 |
| OSCC-IMM4 | COX-2 positive in 75% of FOSCC (weak intensity) | A | n=12 |
| OSCC-COMP4 | FOSCC immune profile parallels human HNSCC | B | comparative oncology |

**Section to update:** Tumor Microenvironment / Immunology

**Boundary rules:**
- Small sample sizes limit generalizability
- Prognostic value not established
- Immunotherapy response not tested
- Not treatment guidance

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] 92% CD3+ T cell infiltration rate
- [x] 57% FoxP3+ Treg infiltration rate
- [x] Elevated circulating Tregs vs controls (P=0.045)
- [x] COX-2 positive in 75% (weak)
- [x] FOSCC shares immune features with HNSCC

### not_safe_to_promote_yet

- [ ] Prognostic value of immune infiltrates
- [ ] Immunotherapy response predictions
- [ ] Optimal Treg depletion strategy
- [ ] PD-1/PD-L1 expression (not measured)

### open_questions

1. Does Treg infiltration predict survival?
2. What is PD-1/PD-L1 expression in FOSCC?
3. Can checkpoint inhibitors benefit FOSCC patients?
4. Is Treg depletion feasible in veterinary oncology?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 5 immunology claims |
| Evidence level | original-study (n=12 IHC, n=9 flow) |
| Key contribution | First comprehensive FOSCC immune profiling |
| Primary gap | Prognostic and therapeutic validation |
| Topic page targets | oral-squamous-cell-carcinoma.md (tumor microenvironment) |
| Cross-reference | Complements src-cancer-073 (mPGES1/inflammation), src-cancer-043 (Tregs in mammary) |
