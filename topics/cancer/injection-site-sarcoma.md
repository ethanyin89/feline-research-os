---
id: topic-cancer-fiss
type: topic
topic: cancer
species: feline
disease: cancer
question_type: branch
source_ids: [src-cancer-002, src-cancer-004, src-cancer-047]
last_compiled_at: 2026-05-30
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: not_checked
owner: codex
status: active
---

# Feline Injection Site Sarcoma (FISS)

## Key-Claim Traceability

| ID | Claim | Level | Source IDs | Boundary |
|---|---|---|---|---|
| FISS1 | FISS were first described in the early 1990s | B | src-cancer-047 | historical context |
| FISS2 | FISS pathogenesis has not been elucidated conclusively | B | src-cancer-047 | evidence gap acknowledgment |
| FISS3 | Chronic inflammatory reaction at injection site is hypothesized to trigger malignant transformation | B | src-cancer-047 | hypothesis, not proven mechanism |
| FISS4 | Alum-based adjuvants role is discussed but controversial | B | src-cancer-047 | controversy acknowledgment |
| FISS5 | Swiss registry showed marked fibrosarcoma decrease after non-adjuvanted FeLV vaccine (2007) | B | src-cancer-047 | Swiss registry, abstract-level |
| FISS6 | Non-adjuvanted vaccines might be safer for cats | B | src-cancer-047 | "might be" — not definitive recommendation |
| FISS7 | FISS occurrence estimated at 1-10 per 10,000 vaccinated cats | B | src-cancer-004 | range estimate, deep-extracted |
| FISS8 | Swiss registry 1965-2008 provides FISS time-trend context | B | src-cancer-002 | registry denominator anchor |

## Evidence-Depth Caveat

This page combines three deep-extracted sources (`src-cancer-002`, `src-cancer-004`, `src-cancer-047`). The Swiss registry provides time-trend evidence supporting adjuvant involvement. [Deep extraction worksheet](../../system/indexes/src-cancer-047-deep-extraction-round1.md).

## Core Takeaway

Feline injection site sarcomas are rare but serious tumors associated with vaccination sites. The Swiss data shows a decrease in fibrosarcomas after non-adjuvanted vaccine introduction, supporting but not proving the adjuvant hypothesis. Pathogenesis remains incompletely understood.

## Branch Architecture

### Historical Context

From `src-cancer-047` abstract:

- FISS first described in early 1990s
- Initially connected to rabies and FeLV vaccination
- Extensive research since then
- Pathogenesis not conclusively elucidated

### Proposed Mechanism

The current hypothesis involves chronic inflammatory reaction at injection sites triggering malignant transformation.

**Key components:**

- Injection site inflammation
- Possible role of alum-based adjuvants
- Genetic susceptibility factors (not well characterized)

**Boundary:** This is hypothesis, not proven mechanism. Do not present as established fact.

### Adjuvant Controversy

The role of alum-based adjuvants has been discussed but remains controversial.

`src-cancer-047` provides supportive evidence:

- Swiss Feline Cancer Registry data 2009-2014
- Marked decrease in fibrosarcoma incidence compared to earlier periods
- Drop occurred after non-adjuvanted FeLV vaccine introduced in Switzerland (2007)
- Authors conclude this "further supports the notion that alum-adjuvanted vaccines are involved in FISS genesis"

**Boundary:** "Supports" is not "proves." The temporal association is suggestive but does not establish causation.

### Incidence Estimates

From `src-cancer-004` (deep-extracted):

- FISS occurrence estimated at 1-10 per 10,000 vaccinated cats
- This is a range estimate, not precise incidence

From `src-cancer-002` (deep-extracted):

- Swiss registry provides longitudinal context
- Fibrosarcoma time-trends tracked from 1965-2008
- Registry denominator caveats apply

**Boundary:** Incidence estimates vary by study methodology and population. Do not cite as universal rates.

### Non-Adjuvanted Vaccines

`src-cancer-047` abstract states: "non-adjuvanted vaccines might be safer for cats"

**This is:**
- A reasonable inference from the time-trend data
- Consistent with the adjuvant hypothesis
- Not a controlled trial result

**Boundary:** This is not a definitive recommendation. Vaccine selection involves multiple factors beyond FISS risk.

## What The Module Can Say Safely

- FISS are rare tumors first described in the 1990s
- Pathogenesis involves chronic inflammation but is not fully understood
- Adjuvant involvement is supported by Swiss registry time-trend data
- Incidence is estimated at 1-10 per 10,000 vaccinated cats
- Fibrosarcoma incidence decreased after non-adjuvanted vaccine introduction in Switzerland

## What The Module Should Not Say Yet

- Do not make definitive vaccine recommendations
- Do not claim adjuvants definitively cause FISS
- Do not provide injection site guidelines from these sources
- Do not cite precise incidence rates without methodology caveats
- Do not recommend specific vaccine products
- Do not advise skipping vaccinations due to FISS risk

## Open Questions Requiring Additional Sources

1. What are current AAFP/AAHA injection site guidelines?
2. What is the FISS incidence in other countries/registries?
3. What specific non-adjuvanted vaccines are available?
4. What are treatment outcomes for FISS?
5. What are the histopathologic criteria for FISS vs other sarcomas?

## Current Role

Use this page as the FISS branch shell. The page provides historical context, adjuvant hypothesis framing, and Swiss registry evidence. Next gains require:

1. Full-text extraction of `src-cancer-047` for incidence numbers
2. Guideline sources for injection site recommendations
3. Treatment outcome sources before clinical guidance
