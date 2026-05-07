# Deep Extraction Worksheet

Source: `src-hcm-012`  
Title: `Influence of Clinical Aspects and Genetic Factors on Feline HCM Severity and Development`  
Method note: this worksheet is based on accessible abstract-level study framing and source-card-checked details, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The study treats genotype dosage as clinically meaningful

- core_claim: heterozygous and homozygous MYBPC3 p.A31P states are not equivalent in HCM severity.
- implicit_premise: the genetics branch should not stop at mutation presence/absence.
- relation_to_previous: opening genotype-severity rule.
- hard_details: the abstract studies heterozygosity and homozygosity for the p.A31P mutation in MYBPC3 and reports more severe disease in homozygous cats.
- tension_or_surprise: mutation dosage matters enough to change the severity story.

#### Unit 2: Homozygous status pushes disease earlier and harder

- core_claim: homozygous cats show moderate-to-severe HCM with higher penetrance and greater cardiac-death risk.
- implicit_premise: genotype branch and risk branch should connect directly.
- relation_to_previous: sharpens the genotype-dosage finding.
- hard_details: the abstract states that homozygous cats had moderate to severe HCM and significant risk of cardiac death, with higher penetrance than heterozygous cats.
- tension_or_surprise: this is stronger than a generic breed-predisposition statement.

#### Unit 3: Penetrance is age-dependent

- core_claim: HCM manifestation depends partly on age rather than existing uniformly across life.
- implicit_premise: recognition architecture should keep age-related penetrance visible.
- relation_to_previous: adds temporal structure to genotype-severity logic.
- hard_details: the abstract reports no disease in cats up to 1 year and highest detection among cats aged 7 years and older.
- tension_or_surprise: genetic risk is not the same as immediate detectable phenotype.

## Phase 1: Theme Reconstruction

## Theme: Genetics should be modeled as dosage-sensitive, not binary

This paper matters because it keeps the genotype branch from becoming simplistic. Mutation state influences severity, penetrance, and probably clinical timing.

### Hard Information

- MYBPC3 and MYH7 are named as primary feline HCM genes
- p.A31P MYBPC3 homozygosity is associated with more severe HCM
- penetrance differs between homozygous and heterozygous cats

## Theme: Risk and recognition need age-aware penetrance

The paper gives the HCM module a reason to keep age inside the recognition architecture rather than treating mutation-positive cats as temporally flat.

### Hard Information

- no disease in cats up to 1 year in the reported cohort
- highest percentage of diagnosed HCM in cats aged 7 years and older

## Phase 2: Claim-Evidence Structure

### Genotype-Phenotype Key Points

**Claim 1**
- support: the abstract directly compares homozygous and heterozygous states
- details: genotype dosage changes penetrance and severity
- implicit_premise: the genetics branch should be stratified

**Claim 2**
- support: homozygous cats show moderate-to-severe disease and higher cardiac-death risk
- details: genetics is tied to risk, not just susceptibility
- implicit_premise: risk and mechanism branches need a direct bridge

**Claim 3**
- support: age-related penetrance is described
- details: genotype-positive status does not imply immediate disease expression
- implicit_premise: recognition should remain time-aware

## Phase 2.5: Write-Back Implications

### For `topics/hcm/mechanism-overview.md`

- keep genotype pressure stratified rather than binary

### For `topics/hcm/risk-and-recognition.md`

- preserve age-related penetrance as a real recognition modifier

## Phase 3: Promotion Check

- source_card_updates:
  - preserve mutation-dosage and age-penetrance logic
  - keep genotype-severity visible
- topic_write_back_targets:
  - `topics/hcm/mechanism-overview.md`
  - `topics/hcm/risk-and-recognition.md`
  - `topics/hcm/current-state-dashboard.md`
- not_safe_to_promote_yet:
  - any broad claim that one mutation explains all feline HCM
  - any overgeneralization from this genotype pattern to all breeds and variants
- conflicts_with_existing_vault:
  - none; this worksheet sharpens the genetics branch materially
