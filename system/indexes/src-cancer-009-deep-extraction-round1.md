---
id: src-cancer-009-deep-extraction-round1
type: system
source_id: src-cancer-009
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-009

**Source:** Metastatic feline mammary cancer: prognostic factors, outcome and comparison of different treatment modalities – a retrospective multicentre study
**Journal:** Journal of Feline Medicine and Surgery (2021)
**DOI:** 10.1177/1098612x20964416
**PMID:** 33078692
**Evidence Level:** original-study (retrospective multicentre)

## Phase 0: Context

**Access status:** Full abstract available in source card. JFMS (subscription required for full text).

**Source scope:** Largest metastatic feline mammary carcinoma (FMC) cohort reported — 73 cats with stage IV disease, comparing treatment modalities.

**Clinical importance:** Provides prognosis data and treatment comparison for advanced FMC, filling a significant gap in the literature.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| Design | Retrospective multicentre |
| Population | 73 cats with stage IV FMC |
| Disease confirmation | Imaging (radiography, ultrasound, CT) + cytology/histopathology |
| Treatment groups | 3 chemotherapy arms + observation |
| Key claim | "highest number of patients with metastatic FMC assessed" |

### 1.2 Overall Prognosis (Stage IV)

| Metric | Value | Boundary |
|--------|-------|----------|
| Overall mean TTP | 23 days | time to progression |
| Overall mean TSS | 44 days | tumor-specific survival |

**Key insight:** Stage IV FMC has very poor prognosis with median survival well under 2 months.

### 1.3 Prognostic Factors

| Factor | Finding | P-value | Interpretation |
|--------|---------|---------|----------------|
| Clinical signs at diagnosis | 14 days vs 128 days | <0.001 | Major prognostic factor |
| Pleural effusion | 16 days vs without | <0.001 | Major negative factor |

**Key insight:** Asymptomatic cats with metastatic disease live 9x longer than symptomatic cats. Pleural effusion indicates very poor prognosis.

### 1.4 Treatment Comparison

| Group | n | Treatment | Median TSS | Toxicity |
|-------|---|-----------|------------|----------|
| 1 | 9 | Maximum tolerated dose (MTD) chemotherapy | 58 days | 66.7% |
| 2 | 15 | Metronomic chemotherapy | 75 days | 20% |
| 3 | 10 | Toceranib phosphate | 63 days | 30% |

**Statistical finding:** P = 0.197 — no significant difference between treatments.

**Key insight:** Metronomic chemotherapy showed longest median TSS (75 days) with lowest toxicity (20%), though comparison was not powered for statistical significance.

### 1.5 Outcome Variability

| Observation | Quote | Implication |
|-------------|-------|-------------|
| Some cats survived >6 months | "some cats survived >6 months" | Outliers exist despite poor overall prognosis |
| Treatment consideration | "adjuvant treatment may be an option to consider" | Not definitive recommendation |

## Phase 2: Theme Reconstruction

### Theme A: Stage IV FMC Has Very Poor Prognosis

Mean TSS of 44 days and TTP of 23 days confirm that metastatic FMC is an aggressive disease with limited survival. This aligns with the general characterization that feline mammary tumors are "usually malignant and aggressive."

### Theme B: Clinical Status as Major Prognostic Factor

The 9x difference in survival (14 days vs 128 days) between symptomatic and asymptomatic cats at diagnosis is the most striking finding. This suggests:
- Early detection of metastases matters
- Clinical symptoms indicate more advanced/aggressive disease
- Asymptomatic metastatic cats may benefit most from treatment

### Theme C: Treatment Modalities Show No Significant Difference

The comparison of three chemotherapy approaches showed no statistically significant difference in survival (P = 0.197). However:
- Metronomic chemotherapy had longest median TSS (75 days)
- Metronomic had lowest toxicity (20%)
- MTD had highest toxicity (66.7%)

This may favor metronomic chemotherapy for quality-of-life considerations, even without survival advantage proof.

### Theme D: Some Cats Outlive Prognosis

Despite very poor overall prognosis, some cats survived >6 months. This heterogeneity suggests:
- Individual factors affect outcome
- Treatment may benefit select patients
- Complete nihilism is not warranted

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC-META1 | Stage IV (metastatic) FMC has mean TSS of 44 days and TTP of 23 days | B | 73-cat retrospective, 2021 |
| MC-META2 | Symptomatic metastatic FMC cats have TSS of 14 days vs 128 days for asymptomatic (P<0.001) | B | major prognostic factor |
| MC-META3 | Pleural effusion indicates very poor prognosis in metastatic FMC (TSS 16 days) | B | negative prognostic indicator |
| MC-META4 | MTD chemotherapy, metronomic chemotherapy, and toceranib showed no significant difference in metastatic FMC survival | B | underpowered comparison, not treatment ranking |
| MC-META5 | Metronomic chemotherapy showed lowest toxicity (20%) vs MTD (66.7%) in metastatic FMC | B | quality-of-life consideration |

**Section to add:** Metastatic Disease Prognosis and Treatment

**Boundary rules:**
- Do not rank treatments as superior without powered comparison
- Frame as "options to consider" not "recommended treatments"
- Note retrospective, uncontrolled design
- Emphasize prognostic factors (symptoms, pleural effusion) as key findings

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] Stage IV FMC has poor prognosis (mean TSS 44 days)
- [x] Symptomatic vs asymptomatic is major prognostic factor (14 vs 128 days)
- [x] Pleural effusion indicates poor prognosis (16 days)
- [x] Three chemotherapy approaches showed no significant difference
- [x] Metronomic chemotherapy had lowest toxicity
- [x] Some cats survived >6 months despite overall poor prognosis
- [x] This is largest metastatic FMC cohort reported (73 cats)

### not_safe_to_promote_yet

- [ ] Treatment recommendations (not powered for comparison)
- [ ] Specific chemotherapy protocols
- [ ] Cost-benefit analysis
- [ ] Individual patient prognosis prediction

### open_questions

1. What factors predicted the >6 month survivors?
2. What imaging protocol is optimal for staging?
3. What is the optimal timing for chemotherapy initiation?
4. How do triple-negative tumors respond compared to other subtypes?
5. What supportive care protocols were used?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 7 prognosis and treatment claims |
| Evidence level | retrospective multicentre (2021, 73 cats) |
| Key contribution | Metastatic FMC prognosis data, prognostic factors, treatment comparison |
| Primary gap | Underpowered treatment comparison |
| Topic page targets | mammary-carcinoma.md (metastatic section) |
| Clinical value | High — fills gap on advanced disease |
