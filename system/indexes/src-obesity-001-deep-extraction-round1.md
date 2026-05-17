---
id: src-obesity-001-deep-extraction-round1
type: system
topic: obesity
question_type: deep-extraction
source_ids: [src-obesity-001]
language: en
last_compiled_at: 2026-05-17
verification_status: deep_extracted
decision_grade: no
owner: codex
status: active
---

# src-obesity-001 Deep Extraction, Round 1

## Source

- Source card: [src-obesity-001](../../raw/papers/src-obesity-001.md)
- Title: `Feline obesity - prevalence, risk factors, pathogenesis, associated conditions and assessment: a review`
- Official source: Journal article page extraction, 2026-05-17
- DOI: `10.17221/145/2015-VETMED`
- Journal: Veterinární medicína (Czech Academy of Agricultural Sciences)
- Volume: 61, Issue 6, Pages 295-307
- Year: 2016
- Authors: D. Tarkosova, M.M. Story, J.S. Rand, M. Svoboda
- License: CC BY-NC 4.0
- References: 91 citations
- Cited by: 40

## Evidence Boundary

This round uses the abstract and key findings from the journal article page. It is sufficient to promote this source from title-only to a comprehensive obesity shell anchor.

## Article Type

This is a **comprehensive review** covering prevalence, risk factors, pathogenesis, associated conditions, and assessment methods. One of the authors (J.S. Rand) is a recognized expert in feline diabetes and metabolism.

## Reusable Facts

### quoted_fact

- "Obesity is recognised as the most common multifactorial nutritional disorder of pet cats."
- Prevalence rates range from 11.5% to 63% of cats being overweight or obese across various countries.
- Risk factors include: "Breed, age, sex, reproductive status, the pet-owner relationship, owners' perceptions of their cats' body condition, type of diet, frequency of feeding, and environment."
- "An important aspect of preventing and managing obesity is the evaluation of body condition to determine ideal body weight and to formulate an appropriate weight loss plan."

### source_supported_conclusion

- Feline obesity is framed as the most common nutritional disorder in cats.
- Prevalence varies widely (11.5-63%) depending on population and geography.
- Risk factors span animal-intrinsic (breed, age, sex, reproductive status) and owner/environment factors.
- Assessment and body condition evaluation are essential for management.
- This source can anchor the broad obesity module architecture.

### llm_inference

- This source provides the broadest foundation for the obesity module shell.
- It can support the five-branch architecture: prevalence, risk factors, pathogenesis, associated conditions, assessment.
- J.S. Rand's involvement (known for feline diabetes work) strengthens the diabetes-obesity connection.

## Prevalence Data

| Finding | Range |
|---------|-------|
| Overweight/obese cats | 11.5% - 63% |
| Geographic variation | Yes, across various countries |
| Framing | Most common nutritional disorder |

## Risk Factors Identified

### Animal-Intrinsic Factors

| Factor | Category |
|--------|----------|
| Breed | Genetic |
| Age | Demographic |
| Sex | Demographic |
| Reproductive status | Physiological |

### Owner/Environment Factors

| Factor | Category |
|--------|----------|
| Pet-owner relationship | Behavioral |
| Owner perceptions of body condition | Behavioral |
| Type of diet | Nutritional |
| Frequency of feeding | Nutritional |
| Environment | Environmental |

## Associated Conditions

| Condition | Mechanism Type |
|-----------|---------------|
| Type 2 diabetes mellitus | Metabolic |
| Hepatic lipidosis | Metabolic |
| Lameness | Mechanical |
| Oral cavity disease | Mixed |
| Urinary tract disease | Mixed |
| Dermatological disease | Mixed |
| Neoplasia | Metabolic |

## Assessment Methods

- Body condition evaluation is emphasized as essential
- Purpose: determine ideal body weight
- Purpose: formulate appropriate weight loss plan
- Multiple established techniques discussed (specific methods need full-text verification)

## Use Boundaries

This source can now support:
- Obesity module shell architecture (5 branches)
- Prevalence range statements (with geographic caveat)
- Risk factor categories (intrinsic vs owner/environment)
- Associated condition visibility
- Assessment importance framing

This source must NOT yet support:
- Specific prevalence for a given country/population
- Risk factor ranking by effect size
- Body condition scoring thresholds (need full text)
- Treatment protocols
- Owner-facing weight-loss recommendations

## Open Questions

- What are the specific body condition assessment methods described?
- How does this review weight the different risk factors?
- What pathogenesis mechanisms are detailed?
- Are there specific populations with higher/lower prevalence?
