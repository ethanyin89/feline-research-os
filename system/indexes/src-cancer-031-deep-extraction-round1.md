---
id: src-cancer-031-deep-extraction-round1
type: system
source_id: src-cancer-031
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-031

**Source:** Feline SCCs of the Head and Neck Display Partial Epithelial-Mesenchymal Transition and Harbor Stem Cell-like Cancer Cells
**Journal:** Pathogens (2023, Open Access MDPI)
**DOI:** 10.3390/pathogens12111288
**PMID:** 38003753
**Evidence Level:** original-study

## Phase 0: Context

**Access status:** Open access. Abstract summary available in source card.

**Source scope:** 2023 molecular characterization of epithelial-mesenchymal transition (EMT) and cancer stem cell (CSC) properties in feline head and neck SCC.

**Key contribution:** Identifies partial EMT phenotype and CSC markers at invasive fronts — mechanistic basis for invasion and recurrence.

## Phase 1: Sequential Micro-Analysis

### 1.1 EMT Characterization

| Finding | Value |
|---------|-------|
| EMT type | Partial EMT (pEMT), not complete |
| Location | Tumor invasive fronts |
| Marker pattern | Co-expression of epithelial + mesenchymal markers |

**Key concept — EMT spectrum:**
- Complete EMT: cells lose epithelial markers, gain mesenchymal markers
- Partial EMT (pEMT): cells retain some epithelial markers while gaining mesenchymal features
- pEMT is associated with collective migration, metastasis, and worse prognosis

### 1.2 Cancer Stem Cell Markers

| Marker | Status | Location |
|--------|--------|----------|
| CD44 | + | Invasive fronts |
| CD271 | + | Invasive fronts |

**CSC implication:** CD44+/CD271+ cells at invasive fronts suggest:
- Cancer stem cell population drives invasion
- May explain recurrence despite apparent surgical clearance
- Potential therapeutic target

### 1.3 Comparative Oncology Alignment

| Feature | Feline HNSCC | Human HNSCC |
|---------|--------------|-------------|
| EMT phenotype | pEMT | pEMT |
| CD44 expression | At invasive front | At invasive front |
| CD271 (NGFR) | Expressed | Expressed in aggressive subtypes |
| Invasion pattern | Similar | Similar |

**Model validation:** Molecular similarities strengthen feline HNSCC as translational model.

## Phase 2: Theme Reconstruction

### Theme A: pEMT as Invasion Mechanism

Partial EMT explains key clinical features of feline OSCC:
1. **Local invasion:** pEMT cells invade while maintaining cohesion
2. **Bone involvement:** EMT facilitates tissue invasion
3. **Poor prognosis:** pEMT associated with treatment resistance
4. **Recurrence:** Stem-like cells survive therapy

### Theme B: Cancer Stem Cells in Oral SCC

The CD44+/CD271+ population may represent:
- Tumor-initiating cells
- Cells responsible for recurrence
- Therapy-resistant subpopulation
- Potential target for CSC-directed therapies

### Theme C: Therapeutic Implications

Understanding pEMT and CSC biology opens treatment avenues:
- EMT inhibitors (experimental)
- CD44-targeted therapy (under development in human oncology)
- CD271/NGFR targeting
- Combination approaches to eliminate CSC population

**Boundary:** These are research directions, not current treatment options.

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/oral-squamous-cell-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| OSCC20 | Feline HNSCC displays partial EMT (pEMT) at invasive fronts | A | 2023 molecular study |
| OSCC21 | CD44+ and CD271+ cancer stem cells identified at FOSCC invasive fronts | A | molecular characterization |
| OSCC22 | pEMT phenotype is shared between feline and human HNSCC | B | comparative oncology validation |
| OSCC23 | CSC population may drive invasion and recurrence in FOSCC | C | mechanistic hypothesis |

**Section to update:** Molecular Biology / Treatment Resistance

**Boundary rules:**
- pEMT and CSC findings are mechanistic, not clinical guidance
- Do not recommend CSC-targeted therapy (not available)
- Use for understanding invasion/recurrence biology

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] Feline HNSCC displays partial EMT (pEMT)
- [x] pEMT located at tumor invasive fronts
- [x] CD44+ cells identified at invasive fronts
- [x] CD271+ cells identified at invasive fronts
- [x] Feline HNSCC shares EMT features with human HNSCC

### not_safe_to_promote_yet

- [ ] EMT-targeting therapy recommendations
- [ ] CSC-targeting therapy recommendations
- [ ] Prognostic value of CD44/CD271 expression
- [ ] Quantified CSC prevalence

### open_questions

1. Does CD44/CD271 expression correlate with prognosis?
2. Can CSC-directed therapy improve FOSCC outcomes?
3. Are there EMT inhibitors applicable to feline cancer?
4. What other CSC markers are expressed in FOSCC?
5. Does surgical margin CSC status predict recurrence?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 4 molecular biology claims |
| Evidence level | original-study (2023, open access) |
| Key contribution | pEMT and CSC characterization at invasive fronts |
| Primary gap | Therapeutic application of findings |
| Topic page targets | oral-squamous-cell-carcinoma.md (molecular biology) |
| Comparative oncology value | High — validates FOSCC as HNSCC model at molecular level |
