---
id: src-cancer-060-deep-extraction-round1
type: system
source_id: src-cancer-060
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-060

**Source:** Comparison of virus-positive and virus-negative cases of feline leukemia and lymphoma
**Journal:** Cancer Research (1979)
**PMID:** 225010
**Evidence Level:** case-series (historical epidemiology)

## Phase 0: Context

**Access status:** Abstract available from PubMed.

**Source scope:** 1979 Boston-based case series comparing FeLV+ and FeLV- feline leukemia/lymphoma cases from 1972-1976.

**Historical importance:** Early documentation of FeLV-negative lymphoma and age-related differences.

**Critical boundary:** Historical (pre-vaccine, pre-test-and-removal era). Not modern prevalence.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| Total cases | 184 |
| Location | Boston |
| Time period | 1972-1976 |
| Disease mix | 58% lymphoma, 42% leukemia |
| Viral test | Fluorescent antibody test for FeLV |

### 1.2 FeLV Status

| Status | Percentage |
|--------|------------|
| Virus-positive | 67% |
| Virus-negative | 33% |

**Key finding:** One-third of lymphoma/leukemia cases were FeLV-negative.

### 1.3 Age at Diagnosis

| FeLV Status | Mean Age |
|-------------|----------|
| Virus-positive | 3.5 years |
| Virus-negative | 4.9 years |

**Older cats (>8 years):** 15/22 were FeLV-negative (68%).

**Pattern:** FeLV-negative lymphoma skews older.

### 1.4 Induction Period

| Metric | Value |
|--------|-------|
| Cats tracked | 19 (healthy FeLV+ at first test) |
| Mean induction period | 16.7 months |
| Range | 2-41 months |

**Finding:** Time from FeLV detection to cancer diagnosis.

### 1.5 Clinical/Epidemiological Comparison

| Aspect | Finding |
|--------|---------|
| Clinical presentation | Similar between groups |
| Epidemiological features | Similar except age |
| Main difference | Age at diagnosis |

## Phase 2: Theme Reconstruction

### Theme A: FeLV-Negative Lymphoma Exists

Not all lymphoma is FeLV-associated:
- 33% of cases were virus-negative
- Especially common in older cats
- Clinically similar presentation
- Different pathogenesis implied

### Theme B: Age-Related Differences

Two distinct populations:
- Young cats: predominantly FeLV-positive
- Older cats (>8 years): predominantly FeLV-negative
- Age at diagnosis is key differentiator

### Theme C: FeLV Induction Period

From FeLV positivity to cancer:
- Mean 16.7 months (range 2-41)
- Relatively long latent period
- Opportunity for intervention

### Theme D: Historical Context

1972-1976 era characteristics:
- Pre-FeLV vaccine
- Pre-test-and-removal programs
- Higher FeLV prevalence expected
- Baseline for later comparisons

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/lymphoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| LY-EPI3 | In pre-vaccine era, 67% of lymphoma/leukemia was FeLV+ and 33% FeLV- | B | Boston 1972-1976 |
| LY-EPI4 | FeLV-negative lymphoma cats are older at diagnosis than FeLV-positive | A | 4.9 vs 3.5 years |
| LY-EPI5 | Among cats >8 years with lymphoma, 68% were FeLV-negative | A | historical cohort |
| LY-PATH5 | Mean FeLV induction period (viremia to cancer) was 16.7 months | B | n=19 |

**Section to update:** Epidemiology / FeLV Association / Historical

**Boundary rules:**
- Historical data (1972-1976)
- Pre-vaccine, pre-test-and-removal
- Cannot extrapolate to modern prevalence
- Supports age-related FeLV association pattern

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] FeLV-negative lymphoma/leukemia exists
- [x] FeLV-negative cases skew older
- [x] FeLV induction period is ~17 months mean
- [x] Clinical presentation similar regardless of FeLV status

### not_safe_to_promote_yet

- [ ] Modern FeLV-associated lymphoma rates
- [ ] Current FeLV prevalence in lymphoma
- [ ] Treatment differences by FeLV status
- [ ] Prognosis comparisons

### open_questions

1. What is the current FeLV+ rate in lymphoma cases?
2. Has the age pattern persisted in modern era?
3. Are FeLV- lymphomas biologically different?
4. Does FeLV status affect treatment response?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 4 historical epidemiology claims |
| Evidence level | case-series (historical, n=184) |
| Key contribution | Documented FeLV-negative lymphoma and age pattern |
| Primary gap | Modern prevalence data |
| Topic page targets | lymphoma.md (epidemiology) |
| Cross-reference | Complements src-cancer-042, src-cancer-044 (FeLV biology) |
