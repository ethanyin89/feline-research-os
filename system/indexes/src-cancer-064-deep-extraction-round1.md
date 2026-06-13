---
id: src-cancer-064-deep-extraction-round1
type: system
source_id: src-cancer-064
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-064

**Source:** Feline paediatric oncology: retrospective assessment of 233 tumours from cats up to one year (1993 to 2008)
**Journal:** Journal of Small Animal Practice (2010)
**DOI:** 10.1111/j.1748-5827.2010.00915.x
**PMID:** 20492453
**Evidence Level:** original-study (retrospective pathology)

## Phase 0: Context

**Access status:** Abstract available from PubMed.

**Source scope:** 2010 retrospective study of tumors in cats ≤12 months old from UK laboratory biopsies (1993-2008).

**Key contribution:** Only systematic pediatric feline oncology data available.

**Critical boundary:** Biopsy submission proportions, not population incidence.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| Age group | Cats ≤12 months old |
| Source | Idexx Laboratories, Wetherby, UK |
| Period | September 1993 to March 2008 |
| Submissions screened | 4196 |
| Neoplastic meeting criteria | 233 (6%) |

### 1.2 Tumor Category Distribution

| Category | n | % |
|----------|---|---|
| Hematopoietic | 73 | 31% |
| Malignant epithelial | 44 | 19% |
| Malignant mesenchymal | 38 | 16% |
| Benign epithelial | 37 | 16% |
| Benign mesenchymal | 30 | 13% |
| Miscellaneous | 11 | 5% |

### 1.3 Most Frequent Specific Tumors

| Tumor Type | n | % |
|------------|---|---|
| Lymphoma | 51 | 22% |
| Soft-tissue sarcoma | 34 | 15% |
| Mast cell tumor | 22 | 9% |
| Squamous cell carcinoma | 16 | 7% |

### 1.4 Additional Findings

| Finding | Value |
|---------|-------|
| Most common site | Skin and soft tissues (41%) |
| Malignant/malignant potential | 164/233 (70%) |

## Phase 2: Theme Reconstruction

### Theme A: Pediatric Cancer Differs

Young cats (≤12 months):
- Lymphoma is most common (22%)
- Hematopoietic cancers dominate (31%)
- Different pattern from adult cats
- High malignancy rate (70%)

### Theme B: Hematopoietic Dominance

In pediatric cats:
- Lymphoma leads at 22%
- Likely reflects FeLV susceptibility in young cats
- May include congenital/developmental tumors

### Theme C: Skin and Soft Tissue Location

Most common site:
- 41% in skin/soft tissues
- Soft-tissue sarcoma at 15%
- Mast cell tumor at 9%
- SCC at 7%

### Theme D: Referral/Submission Bias

Important caveats:
- UK laboratory submissions only
- Not population incidence
- Referral bias likely
- May over-represent submitted/diagnosed cases

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/registry-and-prevalence.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| REG-PED1 | In pediatric cats (≤12 months), lymphoma is the most common tumor (22%) | B | UK biopsies 1993-2008 |
| REG-PED2 | Hematopoietic tumors comprise 31% of pediatric feline neoplasms | B | biopsy submissions |
| REG-PED3 | 70% of pediatric feline tumors are malignant or have malignant potential | B | n=233 |
| REG-PED4 | Skin and soft tissues are the most common pediatric tumor site (41%) | B | biopsy submissions |

**Section to update:** Pediatric Oncology / Age-Related Patterns

**Boundary rules:**
- Biopsy submissions, not population incidence
- UK only
- May not generalize to other regions
- Pediatric-specific (≤12 months)

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] Lymphoma is the most common pediatric feline tumor
- [x] Hematopoietic tumors dominate in young cats
- [x] 70% of pediatric tumors are malignant
- [x] Skin/soft tissues are the most common site

### not_safe_to_promote_yet

- [ ] Population incidence of pediatric feline cancer
- [ ] Prognosis for pediatric tumors
- [ ] Treatment recommendations
- [ ] Regional variation outside UK

### open_questions

1. How do pediatric cancer patterns differ by region?
2. What is the FeLV association rate in pediatric lymphoma?
3. How does pediatric cancer prognosis compare to adults?
4. Are there congenital/developmental tumors included?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 4 pediatric epidemiology claims |
| Evidence level | original-study (retrospective pathology) |
| Key contribution | Only systematic pediatric feline oncology data |
| Primary gap | Population incidence |
| Topic page targets | registry-and-prevalence.md (pediatric) |
| Cross-reference | Complements FeLV age-related susceptibility data |
