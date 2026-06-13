---
id: src-cancer-044-deep-extraction-round1
type: system
source_id: src-cancer-044
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-044

**Source:** Feline Leukemia Virus Infection: Age-Related Variation in Response of Cats to Experimental Infection
**Journal:** Journal of the National Cancer Institute (1976)
**DOI:** 10.1093/jnci/57.2.365
**PMID:** 187771
**Evidence Level:** original-study (experimental infection)

## Phase 0: Context

**Access status:** Abstract available from PubMed. Full-text via Oxford Academic.

**Source scope:** 1976 experimental infection study demonstrating age-related susceptibility to FeLV using 67 SPF cats.

**Historical importance:** Established the biological basis for age-dependent FeLV susceptibility. Foundation for kitten vaccination priority.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| Sample size | 67 specific-pathogen-free cats |
| Age groups | Newborn, 2 weeks, 1 month, 2 months, 4 months, 1 year |
| Route | Intraperitoneal inoculation |
| FeLV strains | Rickard (FeLV-R), Kawakami-Theilen (FeLV-KT) |

### 1.2 Age-Related Susceptibility

| Age at Inoculation | Persistent Viremia / Disease |
|--------------------|------------------------------|
| Newborn | 100% |
| 2 weeks to 2 months | 85% |
| 4 months or 1 year | 15% |

**Key finding:** Dramatic age-dependent susceptibility. Young kittens highly vulnerable; adult cats largely resistant.

### 1.3 Immune Response Patterns

| Outcome | Viremia Status | FOCMA Antibody | Virus-Neutralizing Ab |
|---------|----------------|----------------|----------------------|
| Susceptible (disease) | FeLV gsa+ by 4 weeks | Little or none | Little or none |
| Resistant (healthy) | FeLV gsa- | Persistent titers | Persistent titers |

**Key finding:** Resistance correlates with antibody production; susceptibility with antibody failure.

### 1.4 Strain-Specific Disease

| FeLV Strain | Primary Disease |
|-------------|-----------------|
| FeLV-R (Rickard) | Thymic lymphosarcoma |
| FeLV-KT (Kawakami-Theilen) | Fatal nonregenerative anemia (no neoplasia) |

**Key finding:** FeLV subgroups cause different diseases. Lymphoma is not the only FeLV outcome.

## Phase 2: Theme Reconstruction

### Theme A: Age-Dependent Immunity

The dramatic susceptibility gradient explains:
- Why kittens from FeLV+ households often become infected
- Why adult cats can resist infection
- Why early vaccination is critical
- Why maternal antibody protection matters

### Theme B: Immune Evasion vs Clearance

Two distinct outcomes:
1. **Susceptible:** Fails to mount immune response → persistent viremia → disease
2. **Resistant:** Mounts antibody response → clears virus → protection

This dichotomy persists in modern understanding.

### Theme C: FeLV Subgroup Pathogenesis

Different strains → different diseases:
- FeLV-A: Common, transmissible subgroup
- FeLV-B, C: Arise by recombination
- FeLV-R (experimental): Lymphosarcoma
- FeLV-KT (experimental): Anemia

**Modern relevance:** Explains spectrum of FeLV-associated diseases.

### Theme D: Vaccination Rationale

This study provides biological rationale for:
- Vaccinating kittens early
- Protecting before environmental exposure
- Understanding why adult cats may not need vaccination if testing negative

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/lymphoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| LY-PATH1 | Newborn kittens 100% susceptible to persistent FeLV infection | A | experimental, 1976 |
| LY-PATH2 | Cats 4 months or older only 15% susceptible to persistent FeLV | A | experimental, 1976 |
| LY-PATH3 | FeLV resistance correlates with FOCMA and neutralizing antibody production | A | immunological finding |
| LY-PATH4 | FeLV-R strain causes thymic lymphosarcoma; FeLV-KT causes anemia | A | strain specificity |

**Section to update:** FeLV Pathogenesis / Age-Related Susceptibility

**Boundary rules:**
- Experimental infection data (SPF cats, controlled exposure)
- Historical (1976) — modern vaccines and testing supersede
- Biological mechanism, not clinical recommendation

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] Newborn kittens 100% susceptible to persistent FeLV
- [x] 4-month or older cats only 15% susceptible
- [x] Susceptibility inversely correlates with age
- [x] Antibody response determines outcome
- [x] Different FeLV strains cause different diseases

### not_safe_to_promote_yet

- [ ] Modern vaccination recommendations
- [ ] Current FeLV prevalence
- [ ] Natural exposure vs experimental infection differences
- [ ] Treatment recommendations

### open_questions

1. Does modern FeLV vaccine provide age-independent protection?
2. How do natural exposure routes compare to IP inoculation?
3. What factors determine antibody response success?
4. Are there genetic predictors of FeLV resistance?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 4 pathogenesis claims |
| Evidence level | original-study (experimental infection, JNCI) |
| Key contribution | Quantified age-related FeLV susceptibility |
| Primary gap | Modern vaccination/testing context |
| Topic page targets | lymphoma.md (FeLV pathogenesis) |
| Cross-reference | Complements src-cancer-042 (FeLV epidemiology) |
