---
id: src-cancer-045-deep-extraction-round1
type: system
source_id: src-cancer-045
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-045

**Source:** Treatment of mammary cancer with focused ultrasound: A pilot study in canine and feline patients
**Journal:** Ultrasonics (2023)
**DOI:** 10.1016/j.ultras.2023.106974
**PMID:** 36917874
**Evidence Level:** original-study (pilot, feasibility)

## Phase 0: Context

**Access status:** Abstract available from PubMed. Full-text via ScienceDirect.

**Source scope:** 2023 pilot study assessing thermal focused ultrasound (FUS) feasibility for canine and feline mammary cancer ablation.

**Key contribution:** First veterinary FUS mammary cancer pilot; demonstrates technical feasibility.

**Critical boundary:** Feasibility-stage only. Not a treatment recommendation.

## Phase 1: Sequential Micro-Analysis

### 1.1 Technology

| Parameter | Value |
|-----------|-------|
| Technology | Focused ultrasound (FUS) |
| Frequency | 2 MHz |
| Transducer | Single-element, spherically focused |
| Positioning | Robotic integration |
| Mechanism | Thermal ablation → coagulative necrosis |

### 1.2 Study Design

| Parameter | Value |
|-----------|-------|
| Preclinical validation | Rabbit thigh model |
| Clinical subjects | 9 dogs and cats (mixed) |
| Tumor type | Superficial mammary cancer |
| Protocol | FUS ablation → immediate surgical resection |
| Selection | Specific safety criteria |

### 1.3 Results

| Outcome | Finding |
|---------|---------|
| Histopathology | Well-defined coagulative necrosis in all tumors |
| Off-target damage | None reported |
| Deep tumors | Not evaluated (superficial only) |

### 1.4 Limitations

| Limitation | Impact |
|------------|--------|
| Small sample | 9 total (dogs + cats) |
| Mixed species | Cannot separate feline-specific results |
| Immediate resection | No tumor-only ablation outcomes |
| Superficial only | Deep tumor feasibility unknown |
| No survival data | Efficacy not assessed |

## Phase 2: Theme Reconstruction

### Theme A: Technical Feasibility Demonstrated

FUS can produce targeted tumor necrosis:
- Coagulative necrosis achieved in all cases
- Robotic positioning enables precision
- No reported collateral damage
- Technology works in principle

### Theme B: Early-Stage Evidence

This is pilot/feasibility research:
- Does not replace surgery
- Combined FUS + resection (not FUS alone)
- No comparison group
- No long-term follow-up
- Cannot recommend clinically

### Theme C: Potential Future Role

If validated, FUS might offer:
- Non-invasive or minimally invasive ablation
- Inoperable tumor option
- Debulking before surgery
- Palliative application

**Boundary:** All speculative until larger trials completed.

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC-EXP3 | Focused ultrasound produces coagulative necrosis in FMC (pilot, n=9 mixed) | C | feasibility only |
| MC-EXP4 | Thermal FUS ablation is under investigation for mammary cancer | C | research direction |

**Section to update:** Experimental Therapies

**Boundary rules:**
- Feasibility evidence only
- Not a treatment recommendation
- Cannot separate feline from canine results
- No survival or standalone ablation data

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] FUS is being investigated for mammary cancer
- [x] Pilot demonstrated coagulative necrosis in treated tumors
- [x] No off-target damage reported in pilot

### not_safe_to_promote_yet

- [ ] FUS efficacy compared to surgery
- [ ] FUS as standalone treatment
- [ ] Long-term outcomes
- [ ] Feline-specific results
- [ ] Deep tumor ablation feasibility
- [ ] Clinical availability or recommendation

### open_questions

1. Can FUS ablate tumors without surgical resection?
2. What is FUS efficacy compared to surgery alone?
3. Is FUS suitable for deep-seated tumors?
4. What are feline-specific results?
5. When might FUS become clinically available?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 2 experimental/research claims |
| Evidence level | original-study (pilot, n=9) |
| Key contribution | First veterinary FUS mammary cancer pilot |
| Primary gap | Efficacy and standalone ablation data |
| Topic page targets | mammary-carcinoma.md (experimental therapies) |
| Clinical applicability | None — feasibility research only |
