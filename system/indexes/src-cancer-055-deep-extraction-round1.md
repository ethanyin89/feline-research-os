---
id: src-cancer-055-deep-extraction-round1
type: system
source_id: src-cancer-055
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-055

**Source:** Therapeutic Targeting of Protein Kinase CK2 Gene Expression in Feline Oral Squamous Cell Carcinoma: A Naturally Occurring Large-Animal Model of Head and Neck Cancer
**Journal:** Human Gene Therapy Clinical Development (2017)
**DOI:** 10.1089/humc.2017.008
**PMID:** 28335614
**Evidence Level:** original-study (early-phase clinical trial)

## Phase 0: Context

**Access status:** Full-text available via PMC (PMC5510041).

**Source scope:** 2017 early-phase dose-escalation study testing anti-CK2 RNAi nanocapsule therapy in 9 cats with naturally occurring FOSCC.

**Key contribution:** First feline anti-CK2 gene therapy trial; establishes FOSCC as translational model for human HNSCC.

**Critical boundary:** Phase I-like safety study. Not efficacy-powered. Investigational only.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| Disease | Feline oral squamous cell carcinoma (FOSCC) |
| Enrolled | 9 cats |
| Design | 3+3 dose escalation |
| Treatments | 6 per cat |
| Primary endpoint | Safety |
| Secondary endpoints | Target inhibition, tumor response |

### 1.2 Intervention

| Component | Detail |
|-----------|--------|
| Drug | Anti-CK2 RNAi oligonucleotides |
| Targets | CK2α and CK2α' (CK2 alpha-prime) |
| Delivery | Tenfibgen-coated tumor-specific nanocapsule |
| Mechanism | RNA interference → CK2 gene silencing |

### 1.3 Safety Results

| Grade | Event | Frequency |
|-------|-------|-----------|
| 1-2 | Weight loss | Most common |
| 1-2 | Anorexia | Most common |
| 3-4 | Tissue necrosis (tumor response) | 1 cat |
| 3-4 | AST/CPK elevation (asymptomatic) | 1 cat |
| 3-4 | Hypokalemia (asymptomatic) | 1 cat |

**Safety conclusion:** Tolerable. No dose-limiting toxicities described as stopping trial.

### 1.4 Efficacy Signals

**Tumor response (n=9):**

| Response | Count |
|----------|-------|
| Progressive disease | 4 |
| Stable disease | 3 |
| Partial response | 1 |
| Not evaluable | 1 |

**Target modulation (n=6 evaluable biopsies):**

| Finding | Count |
|---------|-------|
| Reduced CK2 IHC score | 2 |
| Unchanged | 4 |

### 1.5 Limitations

| Limitation | Impact |
|------------|--------|
| Small sample | 9 cats only |
| Dose-finding design | Not efficacy-powered |
| Heterogeneous tumors | Natural disease variability |
| No control arm | Cannot attribute responses |

## Phase 2: Theme Reconstruction

### Theme A: CK2 as Therapeutic Target

Protein kinase CK2:
- Overexpressed in many cancers
- Promotes cell survival and proliferation
- Targetable by RNAi
- Relevant to both feline and human SCC

### Theme B: Gene Therapy Feasibility

Anti-CK2 RNAi nanocapsule:
- Deliverable to tumors
- Tolerable safety profile
- Some evidence of target inhibition
- Technical platform validated

### Theme C: FOSCC as Translational Model

Comparative oncology value:
- Naturally occurring disease (not xenograft)
- Similar to human HNSCC
- Large-animal model for drug development
- Spontaneous tumor microenvironment

### Theme D: Early-Phase Evidence Only

Cannot conclude:
- Efficacy compared to standard care
- Optimal dose/schedule
- Durability of responses
- Clinical benefit for cats

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/oral-squamous-cell-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| OSCC-EXP1 | Anti-CK2 RNAi nanocapsule therapy is under investigation for FOSCC | C | early-phase, n=9 |
| OSCC-EXP2 | CK2 targeting shows preliminary safety and some target modulation in FOSCC | C | investigational |
| OSCC-MODEL1 | FOSCC serves as a translational model for human HNSCC drug development | B | comparative oncology |

**Section to update:** Investigational Therapies / Comparative Oncology

**Boundary rules:**
- Investigational therapy only
- Not treatment recommendation
- Safety study, not efficacy trial
- Requires follow-up data

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] Anti-CK2 RNAi is under investigation for FOSCC
- [x] Early-phase data suggests tolerability
- [x] FOSCC is used as a translational model for human HNSCC
- [x] Some target modulation was observed

### not_safe_to_promote_yet

- [ ] Efficacy of anti-CK2 therapy in FOSCC
- [ ] Treatment recommendations
- [ ] Comparison to standard FOSCC treatments
- [ ] Clinical availability

### open_questions

1. Has a follow-up efficacy trial been conducted?
2. What is the optimal CK2 RNAi dosing regimen?
3. Are there human HNSCC trials using this platform?
4. Does CK2 expression predict response?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 3 investigational/model claims |
| Evidence level | original-study (early-phase, n=9) |
| Key contribution | First feline anti-CK2 gene therapy; translational model |
| Primary gap | Efficacy data |
| Topic page targets | oral-squamous-cell-carcinoma.md (experimental) |
| Cross-reference | Complements src-cancer-031 (OSCC biology) |
