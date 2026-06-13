---
id: src-cancer-027-deep-extraction-round1
type: system
source_id: src-cancer-027
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-027

**Source:** Animal models for hormone-dependent human breast cancer. Relationship between steroid receptor profiles in canine and feline mammary tumors and survival rate
**Journal:** Cancer Chemother Pharmacol (1984)
**DOI:** 10.1007/BF00255902
**PMID:** 6690068
**Evidence Level:** original-study (comparative oncology)

## Phase 0: Context

**Access status:** Abstract extracted. PubMed record confirmed.

**Source scope:** 1984 comparative oncology study characterizing steroid receptor profiles in canine and feline mammary tumors with survival analysis.

**Historical importance:** Early foundation for receptor profiling in comparative mammary oncology. Establishes polyreceptive nature of companion animal mammary tumors.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| Species studied | Canine + Feline |
| Survival cohort | 45 bitches with mammary carcinoma |
| Receptors assessed | ER, PR, androgen, glucocorticoid, mineralocorticoid |
| Outcome | Survival rate by receptor status |

### 1.2 Receptor Profiles

| Receptor | Full Name | Canine | Feline |
|----------|-----------|--------|--------|
| ER | Estrogen receptor | Present | Present |
| PR | Progesterone receptor | Present | Present |
| AR | Androgen receptor | Present | Present |
| GR | Glucocorticoid receptor | Present | Present |
| MR | Mineralocorticoid receptor | Present | Present |

**Key finding:** Both canine and feline mammary tumors are "polyreceptive" — expressing multiple steroid receptor types.

### 1.3 Prognostic Finding (Canine)

| Group | Survival | Significance |
|-------|----------|--------------|
| Receptor-rich (ER and/or PR) | Higher | Statistically significant |
| Receptor-poor | Lower | Reference |

**Note:** This prognostic association is established for the 45-bitch canine cohort. Feline-specific survival data not reported in abstract.

### 1.4 Model Validation

| Criterion | Assessment |
|-----------|------------|
| Receptor biology shared | Yes (polyreceptive like human) |
| Prognostic relevance | Yes (receptor status → survival) |
| Model suitability | Canine validated; feline implied |

## Phase 2: Theme Reconstruction

### Theme A: Polyreceptive Nature of FMC

This study establishes that feline mammary tumors express multiple steroid receptors:
- Not just ER/PR (hormone receptors)
- Also androgen, glucocorticoid, mineralocorticoid
- This receptor diversity matches human breast cancer biology

**Implication:** Feline mammary tumors may respond to multiple hormone manipulation strategies, not just ER/PR-targeted therapy.

### Theme B: Receptor Status as Prognostic Factor

The canine data (45 bitches) shows receptor-rich tumors have better survival. This is:
- Consistent with human breast cancer (ER+ better than ER-)
- Foundation for receptor-based prognosis in companion animals
- Extrapolation to feline requires feline-specific data

### Theme C: Historical Foundation (1984)

This paper provides early evidence for:
- Comparative mammary oncology validity
- Receptor profiling feasibility in veterinary setting
- Hormone-dependent tumor biology across species

Modern understanding builds on this foundation (see src-cancer-022, src-cancer-013 for updated FMC receptor data).

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC27 | FMC can be polyreceptive (ER, PR, androgen, glucocorticoid, mineralocorticoid) | B | 1984 study, shared with canine |
| MC28 | Receptor-rich mammary tumors show better survival (canine data, 1984) | B | canine cohort, feline implied |
| MC-HIST2 | Receptor profiling in feline mammary tumors established by 1984 | C | historical context |

**Section to update:** Historical Context / Prognostic Factors

**Boundary rules:**
- Canine survival data cannot be directly applied to feline
- Modern receptor data (src-cancer-022, etc.) may supersede
- Historical context, not current clinical guidance

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] FMC can be polyreceptive (multiple steroid receptor types)
- [x] Receptor types include ER, PR, androgen, glucocorticoid, mineralocorticoid
- [x] Receptor-rich tumors show better survival (canine, 1984)
- [x] Historical foundation for receptor-based prognosis

### not_safe_to_promote_yet

- [ ] Feline-specific survival by receptor status (not in this study)
- [ ] Quantified receptor expression rates in feline
- [ ] Clinical treatment recommendations based on receptor status

### open_questions

1. What is feline-specific survival by receptor status?
2. How does this 1984 receptor data compare to modern IHC findings?
3. Are polyreceptive FMCs more or less common than monorecep tive?
4. Do androgen/glucocorticoid receptors have therapeutic relevance in FMC?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 3 (1 receptor biology, 1 prognosis, 1 historical) |
| Evidence level | original-study (1984, comparative) |
| Key contribution | Polyreceptive FMC characterization, receptor-survival link |
| Primary gap | Feline-specific survival data |
| Topic page targets | mammary-carcinoma.md (prognostic factors, historical) |
| Cross-reference | Compare with src-cancer-022 for modern phenotyping |
