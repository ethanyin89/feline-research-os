---
id: src-cancer-093-deep-extraction-round1
type: system
topic: cancer
question_type: deep-extraction
source_ids: [src-cancer-093]
language: en
last_compiled_at: 2026-06-05
verification_status: deep_extracted
decision_grade: no
owner: claude
status: active
---

# Deep Extraction Worksheet

Source: `src-cancer-093`
Title: `Phosphoproteomic profiling of feline mammary carcinoma: Insights into tumor grading and potential therapeutic targets`
Method note: PLoS One open-access article. DOI `10.1371/journal.pone.0330520`. Full text accessed via journal website.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: First phosphoproteomic investigation in FMC

- core_claim: This is the first phosphoproteomic investigation of feline mammary carcinoma.
- implicit_premise: Phosphoproteomic data for FMC was previously absent; this source fills a research gap.
- relation_to_previous: Adds molecular-level data to complement existing FMC pathology sources (src-cancer-069, src-cancer-081).
- hard_details: 31 FMC samples (Grade 1: n=6, Grade 2: n=11, Grade 3: n=14) + 6 normal controls.
- tension_or_surprise: Small sample size limits statistical power; authors acknowledge this limitation.

#### Unit 2: 17 downregulated phosphoproteins identified as FMC markers

- core_claim: 17 phosphoproteins showed significant differential expression between FMC and normal tissue.
- implicit_premise: These proteins may serve as diagnostic biomarkers distinguishing malignant from normal tissue.
- relation_to_previous: Complements histopathological grading with molecular markers.
- hard_details: 11,942 total phosphoproteins analyzed; 17 significantly downregulated across all FMC grades.
- tension_or_surprise: No significant differences among tumor grades themselves — suggests early-stage biomarker potential rather than grading discrimination.

#### Unit 3: Five phosphoproteins interact with chemotherapy drugs and immune checkpoints

- core_claim: ABCC3, ACPP, PPP1CA, PRKAG3, RNASEL show interactions with therapeutic agents.
- implicit_premise: These proteins may predict drug sensitivity or immunotherapy response.
- relation_to_previous: Links to src-cancer-017 immunotherapy review and src-cancer-091 targeted therapies.
- hard_details: ABCC3 (multidrug resistance), ACPP (tumor suppressor), PPP1CA (growth promoter), PRKAG3 (Ki-67 association, p=0.03), RNASEL (tumor suppressor).
- tension_or_surprise: PRKAG3 shows statistically significant Ki-67 association — low PRKAG3 correlates with high Ki-67 (proliferation).

#### Unit 4: FMC molecular subtypes mirror human breast cancer classification

- core_claim: Five molecular subtypes identified using human breast cancer classification framework.
- implicit_premise: FMC can serve as a comparative oncology model for human breast cancer.
- relation_to_previous: Strengthens translational value noted in src-cancer-017 and src-cancer-091.
- hard_details: Luminal B/HER2- (35.5%), Luminal B/HER2+ (16.1%), HER2+ (12.9%), Triple-negative basal-like (19.4%), Triple-negative normal-like (16.1%).
- tension_or_surprise: High proportion of triple-negative subtypes (35.5% combined) — known to be aggressive with limited treatment options.

#### Unit 5: Immune checkpoint associations suggest immunotherapy potential

- core_claim: Identified phosphoproteins show indirect associations with CTLA-4 and PD-1.
- implicit_premise: Immunotherapy strategies from human oncology may be applicable to FMC.
- relation_to_previous: Connects to src-cancer-081 TIL/TAM data and src-cancer-017 immunotherapy review.
- hard_details: Indirect associations via protein-protein interaction networks; not direct binding studies.
- tension_or_surprise: Association is indirect — requires validation before clinical translation.

## Phase 1: Theme Reconstruction

## Theme: Phosphoproteomic profiling establishes molecular foundation for FMC biomarker research

This source is most useful because it provides the first systematic phosphoproteomic characterization of FMC, identifying 17 candidate biomarkers and 5 therapeutically relevant proteins.

### Hard Information

- First phosphoproteomic study in FMC
- 31 FMC samples + 6 normal controls
- 11,942 phosphoproteins analyzed
- 17 significantly downregulated phosphoproteins
- PRKAG3-Ki-67 association (p=0.03)
- Mills classification for histological grading

## Theme: FMC molecular subtypes enable human breast cancer comparison

The source supports FMC as a comparative oncology model by demonstrating parallel molecular subtyping to human breast cancer.

### Hard Information

- Five molecular subtypes identified
- Luminal B/HER2-negative most common (35.5%)
- Triple-negative subtypes: 35.5% combined
- Mean Ki-67 expression: 43.4%±15%
- Lymph node metastasis: 29% of cases

## Phase 2: Claim-Evidence Structure

### Biomarker Key Points

**Claim 1**
- support: 17 phosphoproteins significantly downregulated in FMC vs normal tissue.
- details: Includes ABCC3, ACPP, PPP1CA, PRKAG3, RNASEL as therapeutically relevant candidates.
- implicit_premise: Downregulation pattern suggests tumor-suppressor pathway involvement.

**Claim 2**
- support: PRKAG3 shows significant inverse correlation with Ki-67 (p=0.03).
- details: Low PRKAG3 expression associated with high Ki-67 (proliferation marker).
- implicit_premise: PRKAG3 may serve as prognostic biomarker for FMC aggressiveness.

### Therapeutic Target Key Points

**Claim 1**
- support: ABCC3 associated with multidrug resistance mechanisms.
- details: ABC transporter family involvement suggests chemotherapy resistance prediction.
- implicit_premise: ABCC3 expression may predict treatment response.

**Claim 2**
- support: Indirect CTLA-4 and PD-1 associations via protein networks.
- details: Suggests potential immunotherapy targets but requires validation.
- implicit_premise: Use with caveats — network associations, not direct binding.

## Phase 2.5: Write-Back Implications

### For `topics/cancer/mammary-carcinoma.md`

- Add phosphoproteomic biomarker section
- Include PRKAG3-Ki-67 association with p-value
- Document molecular subtype distribution
- Note first-study status with sample size caveat

### For `topics/cancer/synthesis-index.md`

- Add phosphoproteomic biomarker claim
- Link to therapeutic target identification

### For `raw/papers/src-cancer-093.md`

- Update status to `deep_extracted`
- Update extraction_depth to `full`
- Add specific biomarker proteins to evidence_policy

## Phase 3: Promotion Check

- source_card_updates:
  - promote `src-cancer-093` from `abstract_weighted` to `deep_extracted`
  - update extraction_depth from `abstract` to `full`
  - add specific phosphoprotein findings to evidence_policy
- topic_write_back_targets:
  - `topics/cancer/mammary-carcinoma.md` (biomarker section)
  - `topics/cancer/synthesis-index.md` (molecular marker claim)
- not_safe_to_promote_yet:
  - clinical diagnostic recommendations (small sample size)
  - treatment guidance based on biomarkers
  - prognosis prediction (no follow-up data)
  - grade discrimination claims (no inter-grade differences found)
- conflicts_with_existing_vault:
  - none detected; complements existing FMC molecular data
- new_entities_or_pages_justified:
  - future FMC molecular biomarker reference page
  - future phosphoproteomic methods documentation
