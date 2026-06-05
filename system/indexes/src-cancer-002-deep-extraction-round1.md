---
id: src-cancer-002-deep-extraction-round1
type: system
topic: cancer
question_type: deep-extraction
source_ids: [src-cancer-002]
language: zh
last_compiled_at: 2026-05-30
verification_status: deep_extracted
decision_grade: no
owner: codex
status: active
---

# Deep Extraction Worksheet

Source: `src-cancer-002`  
Title: `Swiss Feline Cancer Registry 1965–2008: the Influence of Sex, Breed and Age on Tumour Types and Tumour Locations`  
Method note: ScienceDirect was the intake locator. The ETH Research Collection record confirmed open access, DOI `10.1016/j.jcpa.2016.01.008`, Journal of Comparative Pathology volume 154, pages 195-210, and a browser-readable PDF / dissertation copy. Local direct PDF fetch returned an HTML error shell, so the browser-readable ETH PDF text was used for this worksheet.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: This is a registry denominator source, not a population-incidence source

- core_claim: the study analyzes the Swiss Feline Cancer Registry across 1965-2008.
- implicit_premise: registry proportions must stay tied to the submission and pathology denominator.
- relation_to_previous: adds the first registry / prevalence control source after workflow, molecular, lymphoma, mammary, and COX anchors.
- hard_details: 51,322 feline patient records; 18,375 reported tumours.
- tension_or_surprise: the source is numerically strong, but the authors state that Switzerland lacked obligatory cat registration, so proportional calculations were used.

#### Unit 2: The study controls tumor-family and location branch priority

- core_claim: the source analyzes common tumour types and anatomical locations, not just "cancer" as one flat category.
- implicit_premise: cancer navigation should keep tumor type and anatomical site as separate axes.
- relation_to_previous: strengthens the branch-map logic from `src-cancer-004` with registry-scale pathology data.
- hard_details: the paper explicitly analyzes adenoma/adenocarcinoma, fibrosarcoma, lymphoma, squamous cell carcinoma, skin/subcutis, mammary gland, gastrointestinal tract, cardiorespiratory system, and oral cavity/pharynx.
- tension_or_surprise: registry prominence should drive extraction priority, but not clinical ranking.

#### Unit 3: Signalment variables are reusable only with caveats

- core_claim: age, sex/neuter status, breed, year, method of examination, and canton were modeled as variables.
- implicit_premise: signalment should be presented as registry-associated patterns, not owner-facing risk prediction.
- relation_to_previous: adds epidemiologic guardrails to branch pages that previously only had molecular or pathology anchors.
- hard_details: final models included age, sex/neuter status, breed, year, method of examination, and canton of origin.
- tension_or_surprise: breed findings can be statistically significant but still require replication before broad claims.

#### Unit 4: Fibrosarcoma time trends are important but not causal proof

- core_claim: fibrosarcoma relative frequency increased over the registry period, especially around the 1990s.
- implicit_premise: FISS needs a dedicated branch source before any causal language is promoted.
- relation_to_previous: points toward a future injection-site sarcoma branch after the molecular review already identified sarcoma/FISS as a branch.
- hard_details: the discussion reports fibrosarcoma frequency rising from 0% to around 10% before 1990, then approximately 20% in the 1990s and stable afterward.
- tension_or_surprise: the article links timing to injectable products and FeLV vaccine availability as a plausible explanation, but that is still not standalone causality.

#### Unit 5: Lymphoma time trends need FeLV-era separation

- core_claim: lymphoma frequency changed over time and should be interpreted with FeLV-era context.
- implicit_premise: lymphoma synthesis must distinguish historical FeLV-associated patterns from modern alimentary / immunophenotype framing.
- relation_to_previous: complements `src-cancer-008`, which already made lymphoma a pathology-first branch.
- hard_details: the discussion reports lymphoma as frequent up to 38% from the 1970s to early 1990s, decreasing to around 10% in the 1990s.
- tension_or_surprise: the paper suggests FeLV vaccine introduction as a possible explanation, but the cancer module needs FeLV-specific sources before causal synthesis.

## Phase 1: Theme Reconstruction

## Theme: Registry data gives the cancer module a denominator discipline

This source is most useful because it prevents tumor-frequency language from floating free of denominator. It makes the module state whether a number comes from pathology submissions, hospital admissions, a registry, or a clinical trial.

### Hard Information

- Swiss Feline Cancer Registry
- 1965-2008
- 51,322 feline patient records
- 18,375 tumours
- no obligatory Swiss cat registration; proportional calculations used
- ICD-O-3 coding was used for tumour topography and morphology

## Theme: Tumor type and anatomic location are separate navigation axes

The source supports early navigation around both tumor family and site. It should not force one taxonomy; it should keep branch pages honest about which axis a claim uses.

### Hard Information

- analyzed tumor types: adenoma/adenocarcinoma, fibrosarcoma, lymphoma, squamous cell carcinoma
- analyzed locations: skin/subcutis, mammary gland, gastrointestinal tract, cardiorespiratory system, oral cavity/pharynx
- variables: age, sex/neuter status, breed, year, method of examination, canton

## Phase 2: Claim-Evidence Structure

### Registry / Prevalence Key Points

**Claim 1**
- support: the paper states the registry includes 51,322 feline patient records and 18,375 tumours.
- details: the dataset spans 1965-2008 and is based on pathology records.
- implicit_premise: prevalence pages need denominator labels before numeric claims.

**Claim 2**
- support: the paper says proportional calculations were used because obligatory cat registration was absent.
- details: this blocks population-incidence wording unless paired with a population denominator source.
- implicit_premise: "common in this registry" is not the same as "common in all cats."

### Branch-Control Key Points

**Claim 1**
- support: the paper evaluates common tumor types and anatomical locations with signalment variables.
- details: tumor family and anatomic site should both appear in the module architecture.
- implicit_premise: registry scale can prioritize extraction order.

**Claim 2**
- support: the paper discusses fibrosarcoma and lymphoma time trends.
- details: both require branch-specific corroboration before causal language.
- implicit_premise: use registry trends to ask better questions, not to close mechanisms.

## Phase 2.5: Write-Back Implications

### For `topics/cancer/registry-and-prevalence.md`

- create a registry / prevalence page.
- distinguish registry proportions, hospital admissions, and population incidence.
- mark Swiss registry findings as high-value branch prioritization, not universal prevalence.

### For `topics/cancer/synthesis-index.md`

- add a registry denominator claim.
- connect registry evidence to tumor-family branch prioritization.

### For `system/indexes/cancer-source-index.md`

- `src-cancer-002` should be marked as a deep-extracted registry / epidemiology anchor.

## Phase 3: Promotion Check

- source_card_updates:
  - promote `src-cancer-002` from `title_only` to `deep_extracted`
  - add DOI and Swiss jurisdiction
  - capture denominator, tumor-family, location, signalment, and time-trend boundaries
- topic_write_back_targets:
  - `topics/cancer/registry-and-prevalence.md`
  - `topics/cancer/synthesis-index.md`
  - `topics/cancer/index.md`
  - `topics/cancer/current-state-dashboard.md`
  - `topics/cancer/navigation.md`
  - `system/indexes/cancer-source-index.md`
  - `system/indexes/cancer-source-depth-map.md`
- not_safe_to_promote_yet:
  - universal feline cancer prevalence
  - vaccine causality
  - treatment ranking
  - owner-facing risk prediction
  - survival or prognosis claims
- conflicts_with_existing_vault:
  - none detected; this source adds the first registry denominator anchor
- new_entities_or_pages_justified:
  - registry and prevalence branch page
  - future FISS / sarcoma page
  - future FeLV-era lymphoma boundary page
