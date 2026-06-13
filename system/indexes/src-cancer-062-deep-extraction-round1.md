---
id: src-cancer-062-deep-extraction-round1
type: system
source_id: src-cancer-062
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-062

**Source:** Pamidronate Disodium for Palliative Therapy of Feline Bone-Invasive Tumors
**Journal:** Veterinary Medicine International (2014)
**DOI:** 10.1155/2014/675172
**PMID:** 25013741
**Evidence Level:** original-study (pilot, n=8)

## Phase 0: Context

**Access status:** Open access via Hindawi (PMC4071848).

**Source scope:** 2014 pilot study assessing pamidronate feasibility for cats with bone-invasive tumors, including in vitro and clinical components.

**Key contribution:** First feasibility data for bisphosphonate use in feline bone-invasive cancer.

**Critical boundary:** Very small pilot (n=8), mixed concurrent treatments. Not treatment recommendation.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| In vitro | Antiproliferative effects in feline cancer cells |
| Clinical design | Retrospective pilot |
| Population | 8 cats with bone-invasive cancer |
| Intervention | IV pamidronate |
| Focus | Short-term toxicity and feasibility |

### 1.2 In Vitro Results

| Finding | Detail |
|---------|--------|
| Effect | Reduced proliferation in feline cancer cells |
| Implication | Biological activity demonstrated |

### 1.3 Clinical Outcomes

**Overall cohort (n=8):**

| Metric | Value |
|--------|-------|
| Median OS | 116.5 days |
| Median PFS | 55 days |

**OSCC subset:**

| Metric | Value |
|--------|-------|
| Median OS | 170 days |
| Median PFS | 71 days |

**Stable disease (n=3):**

| Metric | Value |
|--------|-------|
| Median PFI | 81 days |
| Context | 1 with chemo, 2 after prior therapy failure |

### 1.4 Dosing and Safety

| Parameter | Value |
|-----------|-------|
| Dose | 1-2 mg/kg IV |
| Interval | Every 21-28 days |
| Acute toxicity | None directly attributable to pamidronate |
| Azotemia | 3 cats (with concurrent NSAIDs) |

**Note:** Azotemia occurred with multiple modalities including NSAIDs, not clearly pamidronate-caused.

## Phase 2: Theme Reconstruction

### Theme A: Bisphosphonate Feasibility

Pamidronate in cats:
- Biologically active (in vitro)
- Tolerable at tested doses
- No acute toxicity from drug itself
- Feasible for multiple treatments

### Theme B: Palliative Context

Palliative bone care:
- May stabilize some patients
- Not curative intent
- Mixed concurrent treatments
- Supportive care option

### Theme C: OSCC-Specific Outcomes

OSCC with bone invasion:
- Median OS 170 days (better than cohort overall)
- Median PFS 71 days
- May represent favorable subset
- Very small numbers

### Theme D: Renal Monitoring

Azotemia risk:
- 3/8 cats developed azotemia
- Concurrent NSAID use
- Cannot isolate pamidronate contribution
- Renal monitoring advised

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/oral-squamous-cell-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| OSCC-PALL1 | Pamidronate is under investigation for bone-invasive OSCC | C | pilot, n=8 |
| OSCC-PALL2 | Pamidronate 1-2 mg/kg IV q21-28d appears tolerable in cats | C | feasibility |
| OSCC-SURV2 | Median OS 170 days reported in OSCC subset with pamidronate | C | pilot, mixed treatments |

**Section to update:** Palliative Care / Investigational Therapies

**Boundary rules:**
- Pilot study only (n=8)
- Mixed concurrent treatments
- Cannot attribute outcomes to pamidronate alone
- Not treatment recommendation

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] Pamidronate shows in vitro antiproliferative effects in feline cancer cells
- [x] IV pamidronate at 1-2 mg/kg q21-28d was tolerable in pilot
- [x] Bisphosphonates are being investigated for feline bone-invasive tumors

### not_safe_to_promote_yet

- [ ] Pamidronate efficacy for OSCC
- [ ] Treatment recommendations
- [ ] Survival benefit from pamidronate
- [ ] Safety without concurrent NSAID concern

### open_questions

1. Does pamidronate add benefit over supportive care alone?
2. What is the optimal dosing regimen?
3. Can pamidronate be safely combined with NSAIDs?
4. Is there a larger trial validating these findings?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 3 palliative/investigational claims |
| Evidence level | original-study (pilot, n=8) |
| Key contribution | First feline bisphosphonate feasibility data |
| Primary gap | Efficacy validation |
| Topic page targets | oral-squamous-cell-carcinoma.md (palliative) |
| Cross-reference | Related to bone-invasive cancer management |
