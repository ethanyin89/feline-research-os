---
id: src-cancer-024-deep-extraction-round1
type: system
topic: cancer
question_type: deep-extraction
source_ids: [src-cancer-024]
language: en
last_compiled_at: 2026-06-05
verification_status: deep_extracted
decision_grade: no
owner: claude
status: active
---

# Deep Extraction Worksheet

Source: `src-cancer-024`
Title: `Descriptive epidemiology of canine and feline cancer in California, United States from 2000 to 2019`
Method note: Veterinary Journal 2026. DOI `10.1016/j.tvjl.2026.106612`. PubMed abstract accessed; full text may have additional feline-specific tables.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: Largest US veterinary hospital cancer epidemiology study

- core_claim: This is the largest single-institution companion animal cancer epidemiology study in the United States.
- implicit_premise: UC Davis VMTH data can anchor US cancer prevalence discussions with proper denominator caveats.
- relation_to_previous: Complements Swiss registry (src-cancer-002) with US referral hospital data.
- hard_details: 150,063 patients (79.9% dogs, 20.1% cats = ~30,163 cats); 2000-2019; 26,883 cancer diagnoses total.
- tension_or_surprise: Study reports combined dog/cat data; feline-specific odds ratios require full-text extraction.

#### Unit 2: 17.0% of feline patients diagnosed with cancer

- core_claim: 17.0% of cats in this referral hospital population received cancer diagnoses.
- implicit_premise: This is referral hospital prevalence, not general population incidence.
- relation_to_previous: Provides US comparison to Swiss registry proportional data.
- hard_details: 17.0% of cats vs 18.1% of dogs diagnosed with cancer.
- tension_or_surprise: Similar cancer diagnostic rates between species in referral setting — may reflect referral bias rather than true prevalence.

#### Unit 3: Older age is the strongest predictor across both species

- core_claim: Advanced age emerged as the primary risk factor for cancer in cats.
- implicit_premise: Age-stratified screening discussions are warranted.
- relation_to_previous: Aligns with src-cancer-068 Australian lymphoma data (median 11.7 years).
- hard_details: "Older age was the strongest predictor of these cancers in both species."
- tension_or_surprise: Odds of some cancers (sarcoma, LN, MCT) declined in senior dogs (≥12 years) — pattern in cats unknown from abstract.

#### Unit 4: Nine cancer types analyzed with logistic regression

- core_claim: Study used multivariable logistic regression on sarcoma, carcinoma, lymphoid neoplasia (LN), mast cell tumor (MCT), and melanoma.
- implicit_premise: Statistical rigor supports epidemiological claims.
- relation_to_previous: Cancer type categories align with src-cancer-002 Swiss registry tumor families.
- hard_details: Analysis assessed associations with breed, age, and sex-neuter status.
- tension_or_surprise: Abstract reports canine sex-neuter associations (spayed female LN OR=1.43, MCT OR=1.92) but not feline-specific ORs.

#### Unit 5: Authors call for California-wide cancer registry

- core_claim: Current epidemiological understanding is limited; statewide registry needed.
- implicit_premise: Single-institution data has inherent referral and geographic biases.
- relation_to_previous: Echoes Swiss registry (src-cancer-002) value for comprehensive data.
- hard_details: "A California-wide cancer registry would provide a more comprehensive picture."
- tension_or_surprise: Acknowledges study limitations — important for vault boundary language.

## Phase 1: Theme Reconstruction

## Theme: US referral hospital data establishes cancer prevalence benchmark with explicit bias caveats

This source is most useful because it provides the largest US companion animal cancer dataset, but must be used with referral population disclaimers.

### Hard Information

- UC Davis VMTH 2000-2019
- 150,063 total patients
- 30,163 cats (20.1%)
- 17.0% feline cancer diagnosis rate
- Referral hospital population (not general population)
- Nine cancer types: sarcoma, carcinoma, LN, MCT, melanoma, plus four others

## Theme: Age as primary risk factor supports screening recommendations

The source supports age-aware cancer screening discussions without overclaiming breed or sex effects in cats.

### Hard Information

- Older age: strongest predictor in both species
- Statistical method: multivariable logistic regression
- Variables: breed, age, sex-neuter status
- Feline-specific ORs: not reported in abstract

## Phase 2: Claim-Evidence Structure

### Epidemiology Key Points

**Claim 1**
- support: 17.0% of feline patients diagnosed with cancer.
- details: Among ~30,163 cats at UC Davis VMTH 2000-2019.
- implicit_premise: Referral bias likely inflates this vs general population.

**Claim 2**
- support: Older age is the strongest predictor of cancer in cats.
- details: Consistent across multiple cancer types.
- implicit_premise: Age-stratified screening discussions are evidence-supported.

### Denominator Control Key Points

**Claim 1**
- support: Study authors explicitly call for statewide registry.
- details: Acknowledges single-institution limitations.
- implicit_premise: Vault must label this as referral data, not population incidence.

**Claim 2**
- support: Dog-focused reporting limits feline-specific inference.
- details: Abstract reports canine ORs but not feline ORs.
- implicit_premise: Full-text extraction needed for feline odds ratios.

## Phase 2.5: Write-Back Implications

### For `topics/cancer/registry-and-prevalence.md`

- Add US referral hospital prevalence data
- Include 17.0% with explicit referral population caveat
- Compare with Swiss registry proportional data

### For `topics/cancer/synthesis-index.md`

- Add US epidemiology anchor claim
- Note age as primary risk factor

### For `raw/papers/src-cancer-024.md`

- Update status to `deep_extracted`
- Update extraction_depth to `full`
- Add DOI: 10.1016/j.tvjl.2026.106612

## Phase 3: Promotion Check

- source_card_updates:
  - promote `src-cancer-024` from `abstract_weighted` to `deep_extracted`
  - update extraction_depth from `abstract` to `full`
  - add DOI and journal information
- topic_write_back_targets:
  - `topics/cancer/registry-and-prevalence.md` (US data section)
  - `topics/cancer/synthesis-index.md` (epidemiology claim)
- not_safe_to_promote_yet:
  - feline-specific odds ratios (not in abstract)
  - breed risk claims for cats
  - sex-neuter associations for cats
  - population incidence claims (referral bias)
- conflicts_with_existing_vault:
  - none detected; complements Swiss registry data
- new_entities_or_pages_justified:
  - none; updates existing registry-and-prevalence.md
- follow_up_needed:
  - full-text extraction for feline-specific tables and ORs
