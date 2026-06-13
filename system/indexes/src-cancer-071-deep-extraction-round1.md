---
id: src-cancer-071-deep-extraction-round1
type: system
source_id: src-cancer-071
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-071

**Source:** Expression of Cat Podoplanin in Feline Squamous Cell Carcinomas
**Journal:** Monoclonal Antibodies in Immunodiagnosis and Immunotherapy (2017)
**DOI:** 10.1089/mab.2017.0046
**PMID:** 29090969
**Evidence Level:** original-study (biomarker characterization)

## Phase 0: Context

**Access status:** Abstract available from PubMed.

**Source scope:** 2017 study characterizing podoplanin expression in 40 feline SCCs across anatomic sites, with antibody development.

**Key contribution:** Establishes podoplanin as a highly expressed marker in feline SCC with therapeutic potential.

**Critical boundary:** Biomarker expression data. Therapeutic applications are investigational.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| Sample | 40 feline SCCs |
| Anatomic sites | Mouth floor (14), skin (13), ear (9), tongue (4) |
| Method | Immunohistochemistry with PMab-52 |
| Antibody | PMab-52 (anti-cat podoplanin monoclonal antibody) |

### 1.2 Podoplanin Expression

| Finding | Value |
|---------|-------|
| Overall positivity | 95% (38/40) |
| Strong membrane staining | 30% (12/40) |

**Key finding:** Near-universal podoplanin expression in feline SCC.

### 1.3 Mechanism

| Aspect | Detail |
|--------|--------|
| Target | Podoplanin (transmembrane glycoprotein) |
| Receptor | CLEC-2 (C-type lectin-like receptor 2) |
| Function | Activates platelet aggregation |
| Role in cancer | Involved in tumor metastasis |

### 1.4 Therapeutic Implications

| Development | Status |
|-------------|--------|
| PMab-52 antibody | Developed |
| Method | Cell-based immunization and screening (CBIS) |
| Application | Potential antibody therapy for podoplanin+ feline SCCs |

## Phase 2: Theme Reconstruction

### Theme A: Podoplanin as SCC Marker

Near-universal expression:
- 95% of feline SCCs are positive
- Across anatomic sites (oral, skin, ear)
- Reliable biomarker

### Theme B: Therapeutic Target

Podoplanin-targeting potential:
- Anti-podoplanin antibody developed (PMab-52)
- Targets metastasis mechanism
- Blocks CLEC-2-mediated platelet aggregation
- Investigational stage

### Theme C: Metastasis Mechanism

Podoplanin role:
- Binds CLEC-2 on platelets
- Activates platelet aggregation
- Facilitates tumor metastasis
- Blocking may reduce spread

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/oral-squamous-cell-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| OSCC-BIO1 | 95% of feline SCCs express podoplanin | A | n=40, IHC |
| OSCC-BIO2 | Podoplanin mediates CLEC-2-dependent platelet aggregation in metastasis | B | mechanism |
| OSCC-EXP3 | Anti-podoplanin antibody (PMab-52) is under development for feline SCC | C | investigational |

**Section to update:** Biomarkers / Investigational Therapies

**Boundary rules:**
- Biomarker expression confirmed
- Therapeutic application is investigational
- Not clinical treatment
- Sample includes oral and non-oral SCC sites

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] 95% of feline SCCs express podoplanin
- [x] 30% show strong membrane staining
- [x] Podoplanin involved in CLEC-2-mediated metastasis
- [x] PMab-52 antibody developed for potential targeting

### not_safe_to_promote_yet

- [ ] Clinical efficacy of anti-podoplanin therapy
- [ ] Treatment recommendations
- [ ] Comparison with other SCC markers
- [ ] Prognostic value of podoplanin expression level

### open_questions

1. Does podoplanin expression level predict metastasis?
2. Has PMab-52 shown in vivo efficacy?
3. Is there clinical trial data for anti-podoplanin therapy?
4. How does oral vs cutaneous SCC podoplanin expression compare?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 3 biomarker/investigational claims |
| Evidence level | original-study (biomarker, n=40) |
| Key contribution | Podoplanin nearly universal in feline SCC |
| Primary gap | Therapeutic validation |
| Topic page targets | oral-squamous-cell-carcinoma.md (biomarkers) |
| Cross-reference | Complements CK2 targeting (src-cancer-055) |
