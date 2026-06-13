---
id: src-cancer-007-deep-extraction-round1
type: system
source_id: src-cancer-007
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-007

**Source:** Feline cancer prevalence in South Africa (1998-2005): contrasts with the rest of the world
**Journal:** Journal of Basic & Applied Sciences (2015)
**DOI:** 10.6000/1927-5129.2015.11.53
**PMID:** Not indexed
**Evidence Level:** original-study (hospital-based retrospective)

## Phase 0: Context

**Access status:** Publisher abstract available. Not PubMed indexed. Full text at SET Publisher.

**Source scope:** 7-year retrospective study (1998-2005) of feline cancer admissions at a South African hospital.

**Geographic value:** High-UV region data contrasting with Northern hemisphere lymphoma-dominant patterns. Supports UV exposure hypothesis for cutaneous SCC.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Characteristics

| Parameter | Value | Boundary |
|-----------|-------|----------|
| Study period | 1998-2005 | 7-year retrospective |
| Total feline admissions | 12,893 | single hospital |
| Cancer admissions | 100 | hospital-based, not population |
| Location | South Africa | high UV exposure region |
| Data source | hospital admissions | NOT population registry |

### 1.2 Cancer Distribution

| Tumor Type | Prevalence | Comparison |
|------------|------------|------------|
| SCC | 48% | Much higher than Northern hemisphere |
| Other tumors | 52% (distribution unknown) | Need full text |

**Key insight:** SCC at 48% dominates in South Africa, while lymphoma typically dominates in Northern hemisphere studies. This geographic contrast is significant.

### 1.3 Regional Context

| Factor | Relevance |
|--------|-----------|
| UV exposure | South Africa has high UV levels |
| Latitude | Southern hemisphere, closer to equator |
| Population | Potentially different breed composition |
| Environment | Different from UK/US/Australia study populations |

**Implication:** This supports the UV exposure hypothesis for cutaneous SCC prevalence.

### 1.4 Methodology Limitations

| Limitation | Impact |
|------------|--------|
| Hospital-based | Not population prevalence |
| 100 cases | Relatively small sample |
| Single institution | Limited generalizability |
| Not PubMed indexed | Lower visibility in literature |
| Admission bias | May not reflect true incidence |

## Phase 2: Theme Reconstruction

### Theme A: Geographic Variation in Cancer Prevalence

This source demonstrates that feline cancer prevalence varies significantly by geography:
- South Africa: SCC dominant (48%)
- Northern hemisphere: typically lymphoma dominant

This challenges any universal prevalence claims and supports region-specific epidemiology.

### Theme B: UV Exposure and SCC

The high SCC prevalence in South Africa (high UV region) supports the environmental UV hypothesis for cutaneous SCC:
- White or lightly pigmented cats at higher risk
- UV damage as carcinogen
- Geographic UV levels correlate with SCC prevalence

### Theme C: Denominator Discipline

This study uses hospital-admissions denominator, NOT population registry. This means:
- Cannot directly compare with pathology-registry studies
- Reflects what gets presented to veterinary care
- May miss mild/undiagnosed cases
- May over-represent severe/treatable cases

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/registry-and-prevalence.md (or topics/cancer/index.md)

**Claims to add:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| REG-GEO1 | Feline cancer prevalence varies by geographic region | B | epidemiology principle |
| REG-GEO2 | SCC was 48% of feline cancers in South Africa hospital study (1998-2005) | B | single hospital, 100 cases, not population |
| REG-GEO3 | South African SCC prevalence contrasts with lymphoma-dominant Northern hemisphere pattern | B | geographic comparison hypothesis |

### Target: topics/cancer/oral-squamous-cell-carcinoma.md (or cutaneous SCC section)

**Claims to add:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| SCC-GEO1 | High UV regions may have higher SCC prevalence in cats | B | hypothesis from geographic comparison |

**Boundary rules:**
- Always note hospital-based denominator
- Do not present as population prevalence
- Frame as "contrast" or "hypothesis" not "proof"
- Note small sample size (100 cases)

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] Feline cancer prevalence varies by geographic region
- [x] SCC was predominant tumor in South Africa study (48%)
- [x] This contrasts with Northern hemisphere lymphoma-dominant pattern
- [x] Geographic variation supports UV exposure hypothesis for SCC

### not_safe_to_promote_yet

- [ ] Specific tumor type breakdown beyond SCC (need full text)
- [ ] Population-level prevalence claims
- [ ] Breed-specific findings (if any)
- [ ] UV exposure mechanism confirmation

### open_questions

1. What were the other tumor types in the 52% non-SCC cases?
2. Was cutaneous SCC distinguished from oral SCC?
3. What breeds were represented?
4. Were white/lightly pigmented cats over-represented?
5. How does this compare to other high-UV regions (Australia)?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 4 geographic/epidemiologic claims |
| Evidence level | hospital-based retrospective (2015) |
| Key contribution | Geographic variation evidence, UV-SCC hypothesis support |
| Primary gap | Full tumor type breakdown, breed data |
| Topic page targets | registry-and-prevalence.md, oral-squamous-cell-carcinoma.md |
| Geographic value | High — unique Southern hemisphere data |
| Denominator caveat | Hospital-based, not population registry |
