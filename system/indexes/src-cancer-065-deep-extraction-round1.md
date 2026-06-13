---
id: src-cancer-065-deep-extraction-round1
type: system
source_id: src-cancer-065
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-065

**Source:** Feline Lymphoma in the Post—Feline Leukemia Virus Era
**Journal:** Journal of Veterinary Internal Medicine (2005)
**DOI:** 10.1892/0891-6640(2005)19[329:flitpl]2.0.co;2
**PMID:** 15954547
**Evidence Level:** retrospective-study

## Phase 0: Context

**Access status:** PubMed abstract available. Full-text available at JVIM (Oxford Academic).

**Source scope:** 21-year retrospective survey at UC Davis VMTH (1983-2003) documenting the shift in feline lymphoma patterns after FeLV testing and vaccination programs.

**Historical importance:** This is the definitive source for the "FeLV-shift" — explaining why lymphoma remains common despite FeLV control.

## Phase 1: Sequential Micro-Analysis

### 1.1 Lymphoma as Primary Hematopoietic Cancer

| Claim | Quote | Boundary |
|-------|-------|----------|
| Most common hematopoietic neoplasm | "Lymphoma is the most common neoplasm of the hematopoietic system of cats" | Ranking claim |
| Highest species incidence | "The cat has the highest incidence for lymphoma of any species" | Comparative context |

### 1.2 FeLV-Shift Documentation

| Temporal Pattern | Detail |
|------------------|--------|
| Study period | 1983-2003 (21 years) |
| FeLV impact | "Significant decrease in the importance of FeLV-associated types of lymphoma" |
| Overall trend | "The incidence of lymphoma in cats actually increased from 1982 to 2003" |
| Key driver | "This increase was due largely to a rise in the incidence of intestinal lymphoma" |
| Secondary driver | "to a lesser degree, of atypical lymphoma" |

**Key insight:** FeLV vaccination success paradoxically coincided with overall lymphoma increase. The disease shifted from viral-associated to intestinal forms.

### 1.3 Breed-Specific Pattern

| Finding | Detail |
|---------|--------|
| Breed | Siamese and Oriental breeds |
| Anatomic form | Mediastinal lymphoma |
| Age | Young cats |
| Pattern | "High incidence" in this subgroup |

**Implication:** Siamese mediastinal lymphoma may have distinct etiology from intestinal lymphoma.

### 1.4 IBD-Lymphoma Association

| Claim | Quote | Boundary |
|-------|-------|----------|
| Association flagged | "Associations of intestinal lymphoma and inflammatory bowel disease and diet should be further considered" | Research direction, not established causation |

**Key boundary:** This is hypothesis-generating from the 2005 study, subsequently developed by later sources (src-cancer-063 in 2026).

## Phase 2: Theme Reconstruction

### Theme A: The FeLV Paradox

FeLV control (testing, elimination, vaccination from 1970s-1980s) successfully reduced FeLV-associated lymphoma, but overall feline lymphoma increased. This is the central finding that explains modern lymphoma epidemiology.

### Theme B: Anatomic Shift to Intestinal Forms

The rise in intestinal lymphoma as FeLV-associated forms declined suggests:
- Different etiologic factors for intestinal vs viral lymphoma
- Possible environmental/dietary influences
- IBD-lymphoma continuum worth investigating

### Theme C: Breed-Specific Biology

Siamese/Oriental mediastinal lymphoma in young cats represents a distinct pattern that persisted through the FeLV shift. This may indicate:
- Genetic susceptibility
- Different pathogenesis from intestinal forms
- Potential research model value

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/lymphoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| LY4 | FeLV-associated lymphoma decreased after testing/vaccination, but overall lymphoma incidence increased due to intestinal lymphoma rise | B | FeLV-shift context, 1983-2003 retrospective |
| LY10 | Siamese and Oriental breeds show high incidence of mediastinal lymphoma in young cats | B | breed-specific pattern, UC Davis 21-year retrospective |

**Section to add:** FeLV Context and the GI-Shift

**Key content:**
- Document the paradox: FeLV control + lymphoma increase
- Explain intestinal lymphoma as the driver
- Note Siamese mediastinal pattern
- Flag IBD-diet association for investigation (connect to src-cancer-063)

**Boundary rules:**
- Do not recommend diet changes based on association flag alone
- Do not claim FeLV vaccination caused intestinal lymphoma increase
- Keep IBD-lymphoma relationship as hypothesis requiring further sources

### Target: topics/cancer/synthesis-index.md

**Cross-reference:** Lymphoma FeLV-shift documentation with src-cancer-065 as primary retrospective source.

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] Lymphoma is most common hematopoietic neoplasm in cats
- [x] Cats have highest lymphoma incidence of any species
- [x] FeLV-associated lymphoma types decreased after testing/vaccination
- [x] Overall lymphoma incidence increased 1982-2003
- [x] Increase driven by intestinal lymphoma
- [x] Siamese/Oriental breeds show high mediastinal lymphoma in young cats

### not_safe_to_promote_yet

- [ ] Specific incidence rates (not in abstract)
- [ ] Diet recommendations
- [ ] IBD treatment guidance
- [ ] Causal mechanism for intestinal lymphoma increase
- [ ] Modern (post-2005) patterns

### open_questions

1. What are the numeric incidence rates per year?
2. What specific IBD-lymphoma hypotheses are proposed in full text?
3. How does 2005 UC Davis data compare to 2024 Australian data (src-cancer-068)?
4. Are there survival differences between anatomic forms?
5. What was the FeLV prevalence in the different time periods?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 6 primary claims |
| Evidence level | retrospective study (21 years, UC Davis) |
| Key contribution | FeLV-shift documentation, intestinal lymphoma rise |
| Primary gap | no numeric incidence data in abstract |
| Topic page targets | lymphoma.md (LY4, LY10 already present), synthesis-index.md |
| Historical value | Definitive FeLV-shift documentation |
