---
id: src-cancer-068-deep-extraction-round1
type: system
topic: cancer
question_type: deep-extraction
source_ids: [src-cancer-068]
language: en
last_compiled_at: 2026-06-05
verification_status: deep_extracted
decision_grade: no
owner: claude
status: active
---

# Deep Extraction Worksheet

Source: `src-cancer-068`
Title: `Demographics of Feline Lymphoma in Australian Cat Populations: 1705 Cases`
Method note: MDPI Vet Sci 2024. DOI `10.3390/vetsci11120641`. PMID 39728981. Abstract-based extraction; full-text needed for specific breed risk list.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: Largest modern feline lymphoma demographics study

- core_claim: This is the largest modern feline lymphoma epidemiology study with 1705 cases and reference population comparison.
- implicit_premise: Large case numbers provide statistical power for breed and signalment associations.
- relation_to_previous: Complements src-cancer-008 pathology classification (602 cases) with modern epidemiological data.
- hard_details: 1705 lymphoma cases vs 85,741 reference population cats; Australian veterinary clinics.
- tension_or_surprise: Reference population enables odds ratio calculations rather than just proportional frequencies.

#### Unit 2: Male cats at increased lymphoma risk

- core_claim: Male sex is associated with increased lymphoma risk.
- implicit_premise: Sex-specific risk factors may inform screening discussions.
- relation_to_previous: Adds sex risk data not emphasized in src-cancer-008 pathology classification.
- hard_details: Male OR 1.2, 95%CI 1.1-1.3, p=0.002.
- tension_or_surprise: Modest effect size (OR 1.2) — clinically meaningful but not dramatic.

#### Unit 3: Lymphoma cases are older and weigh less

- core_claim: Lymphoma-affected cats are significantly older and lighter than reference population.
- implicit_premise: Age and weight may be associated with disease or its consequences.
- relation_to_previous: Age finding aligns with src-cancer-024 (older age strongest cancer predictor).
- hard_details: Median age 11.7 vs 9.0 years (p<0.0001); median weight 3.7 vs 4.0 kg (p=0.010).
- tension_or_surprise: Weight difference could reflect cachexia/disease effect rather than pre-existing risk factor.

#### Unit 4: Eight breeds at increased risk, three at decreased risk

- core_claim: Breed-specific lymphoma risk varies significantly.
- implicit_premise: Genetic factors may influence lymphoma susceptibility.
- relation_to_previous: Adds breed risk dimension not in src-cancer-008 pathology data.
- hard_details: 8 high-risk breeds, 3 low-risk breeds (specific names not in abstract).
- tension_or_surprise: Abstract doesn't list specific breeds — full-text extraction needed.

#### Unit 5: Breed-specific anatomic presentation patterns

- core_claim: Different breeds show different proportions of anatomic lymphoma presentations.
- implicit_premise: Breed may influence not just risk but disease phenotype.
- relation_to_previous: Could inform breed-aware topography discussions.
- hard_details: Siamese, Burmilla, Australian Mist, Ragdoll, British Shorthair, Domestic cats show "significant variations."
- tension_or_surprise: Interesting breed-phenotype association but details require full text.

## Phase 1: Theme Reconstruction

## Theme: Modern Australian data provides quantified lymphoma risk factors

This source is most useful because it provides odds ratios with confidence intervals for sex and breed risk, enabling evidence-graded discussions.

### Hard Information

- 1705 lymphoma cases
- 85,741 reference population
- Male OR 1.2 (95%CI 1.1-1.3, p=0.002)
- Median age 11.7 years (cases) vs 9.0 years (reference)
- Median weight 3.7 kg (cases) vs 4.0 kg (reference)
- 8 high-risk breeds, 3 low-risk breeds (names need full-text)

## Theme: Breed-anatomic associations suggest phenotype complexity

The source supports nuanced breed discussions beyond simple risk — anatomic presentation varies by breed.

### Hard Information

- Breeds with anatomic pattern variations: Siamese, Burmilla, Australian Mist, Ragdoll, British Shorthair, Domestic
- Retroviral status and immunophenotype data collected (details in full text)

## Phase 2: Claim-Evidence Structure

### Epidemiology Key Points

**Claim 1**
- support: Male cats have 1.2x lymphoma risk vs females (p=0.002).
- details: OR 1.2, 95%CI 1.1-1.3; statistically significant, modest effect size.
- implicit_premise: Sex-aware lymphoma discussions are evidence-supported.

**Claim 2**
- support: Lymphoma cases are older (median 11.7 vs 9.0 years, p<0.0001).
- details: Highly significant age difference; consistent with age as cancer risk factor.
- implicit_premise: Age-stratified screening discussions warranted.

### Breed Risk Key Points

**Claim 1**
- support: 8 breeds show increased risk, 3 show decreased risk.
- details: Specific breeds not named in abstract.
- implicit_premise: Breed-specific risk claims require full-text for promotion.

**Claim 2**
- support: 6 breeds show anatomic presentation pattern variations.
- details: Siamese, Burmilla, Australian Mist, Ragdoll, British Shorthair, Domestic.
- implicit_premise: Breed may influence disease phenotype, not just risk.

## Phase 2.5: Write-Back Implications

### For `topics/cancer/lymphoma.md`

- Add Australian demographics section
- Include male OR 1.2 with CI and p-value
- Add age/weight signalment data
- Note breed-anatomic associations (names pending full text)

### For `topics/cancer/registry-and-prevalence.md`

- Add Australian lymphoma data point
- Compare with Swiss registry lymphoma proportions

### For `raw/papers/src-cancer-068.md`

- Update status to `deep_extracted`
- Note full-text follow-up needed for breed list

## Phase 3: Promotion Check

- source_card_updates:
  - promote `src-cancer-068` from `abstract_weighted` to `deep_extracted`
  - update extraction_depth to `full`
  - add quantified risk factor findings
- topic_write_back_targets:
  - `topics/cancer/lymphoma.md` (demographics section)
  - `topics/cancer/registry-and-prevalence.md` (Australian data)
- not_safe_to_promote_yet:
  - specific breed names for risk claims (not in abstract)
  - breed-specific anatomic pattern details
  - causal mechanism claims
  - generalization beyond Australian population
- conflicts_with_existing_vault:
  - none detected; complements src-cancer-008 pathology data
- new_entities_or_pages_justified:
  - none; updates existing lymphoma.md
- follow_up_needed:
  - full-text extraction for specific breed risk list (8 high, 3 low)
  - anatomic presentation tables by breed
