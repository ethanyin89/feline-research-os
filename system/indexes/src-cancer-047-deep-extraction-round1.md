---
id: src-cancer-047-deep-extraction-round1
type: system
source_id: src-cancer-047
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-047

**Source:** Feline Injection Site Sarcomas: Data from Switzerland 2009–2014
**Journal:** Journal of Comparative Pathology (2018)
**DOI:** 10.1016/j.jcpa.2018.06.008
**PMID:** 30213367
**Evidence Level:** original-study (registry)

## Phase 0: Context

**Access status:** PubMed abstract available. Full-text paywalled (ScienceDirect).

**Source scope:** Swiss Feline Cancer Registry study covering 2009-2014, analyzing FISS incidence trends after non-adjuvanted FeLV vaccine introduction in 2007.

**Registry continuity:** This study continues the Swiss Feline Cancer Registry data from src-cancer-002 (1965-2008), providing longitudinal perspective.

## Phase 1: Sequential Micro-Analysis

### 1.1 Historical Context

| Claim | Quote | Boundary |
|-------|-------|----------|
| FISS discovery | "Feline injection site sarcomas (FISS) were first described in the early 1990s" | Historical context |
| Pathogenesis unclear | "Despite extensive research, the pathogenesis of these tumours has not been elucidated conclusively" | Knowledge gap acknowledgment |

### 1.2 Hypothesized Mechanism

| Mechanism Element | Evidence Level |
|-------------------|---------------|
| Chronic inflammatory reaction at injection site | Hypothesized ("assumed") |
| Triggers malignant transformation | Hypothesized |
| Alum-based adjuvants role | "Discussed, but controversial" |

**Key boundary:** The mechanism is hypothesized, not proven. Use conditional language.

### 1.3 Time-Trend Evidence

| Finding | Detail |
|---------|--------|
| Incidence change | "Marked decrease of the incidence of fibrosarcomas" |
| Comparison period | 2009-2014 vs previous observation period |
| Temporal association | Drop occurred after non-adjuvanted FeLV vaccine introduced in 2007 |
| Implication | "Supports the notion that alum-adjuvanted vaccines are involved in the genesis of FISS" |

**Key insight:** This is associational evidence — temporal correlation with vaccine change — not causal proof.

### 1.4 Non-Adjuvanted Vaccine Impact

| Finding | Boundary |
|---------|----------|
| Non-adjuvanted FeLV vaccine introduced in Switzerland in 2007 | Specific intervention identified |
| "Non-adjuvanted vaccines might be safer for cats" | Conditional recommendation ("might be") |

## Phase 2: Theme Reconstruction

### Theme A: FISS as Iatrogenic Cancer

FISS represents a cancer type associated with medical intervention (vaccination). This creates a unique branch in the cancer module requiring careful framing around:
- Benefits of vaccination vs FISS risk
- Adjuvant vs non-adjuvanted vaccine considerations
- Individual risk vs population benefit

### Theme B: Registry Time-Trend Evidence

The Swiss registry provides longitudinal data spanning:
- src-cancer-002: 1965-2008 (fibrosarcoma trends)
- src-cancer-047: 2009-2014 (post-non-adjuvanted vaccine)

This continuity enables before/after comparison not available in many other datasets.

### Theme C: Adjuvant Hypothesis Support

The study supports but does not prove adjuvant involvement:
- "Supports" — not "proves"
- "Might be safer" — not "is safer"
- Mechanism still "not elucidated conclusively"

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/injection-site-sarcoma.md (if exists) or topics/cancer/index.md

**Claims to add:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| FISS1 | FISS first described in early 1990s | A | historical fact |
| FISS2 | Pathogenesis not conclusively elucidated despite extensive research | B | current knowledge state |
| FISS3 | Chronic inflammatory reaction at injection site hypothesized as trigger | B | mechanism hypothesis |
| FISS4 | Alum-based adjuvants role discussed but controversial | B | controversy acknowledgment |
| FISS5 | Swiss registry showed marked fibrosarcoma decrease 2009-2014 after non-adjuvanted FeLV vaccine introduction (2007) | B | temporal association, Swiss population |
| FISS6 | Time-trend data supports adjuvant involvement hypothesis | B | "supports" not "proves" |

**Boundary rules to add:**
- Do not recommend specific vaccine brands or types to owners
- Frame as population-level evidence, not individual risk assessment
- Acknowledge vaccination benefits outweigh FISS risk for most cats
- Do not claim adjuvants definitively cause FISS

### Target: topics/cancer/synthesis-index.md

**Cross-reference:** Add FISS as distinct cancer branch with src-cancer-047 + src-cancer-002 as registry evidence.

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] FISS first described in early 1990s (historical fact)
- [x] Pathogenesis not conclusively elucidated (evidence gap)
- [x] Chronic inflammation hypothesis exists (with uncertainty framing)
- [x] Swiss registry showed fibrosarcoma decrease after non-adjuvanted vaccine (temporal association)

### not_safe_to_promote_yet

- [ ] Specific incidence numbers (not in abstract)
- [ ] Non-adjuvanted vaccine recommendation (policy-level, not individual advice)
- [ ] Specific vaccine brand recommendations
- [ ] Owner-facing injection site guidance (needs additional sources)
- [ ] Treatment or prognosis claims

### open_questions

1. What are the actual incidence numbers (fibrosarcomas per 100,000 cats)?
2. What specific non-adjuvanted FeLV vaccine was introduced?
3. Were other variables controlled (vaccination rates, reporting changes)?
4. How does Swiss data compare to US/UK FISS trends?
5. What are current AAHA/AAFP FISS prevention guidelines?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 6 primary claims |
| Evidence level | registry study (2018) |
| Key contribution | time-trend evidence supporting adjuvant hypothesis |
| Primary gap | mechanism not proven, incidence numbers not in abstract |
| Topic page targets | injection-site-sarcoma.md (create or update), synthesis-index.md |
| Registry continuity | Extends src-cancer-002 (1965-2008) through 2014 |
