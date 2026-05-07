# Deep Extraction Worksheet

Source: `src-hcm-001`  
Title: `The Feline Cardiomyopathies: 2. Hypertrophic cardiomyopathy`  
Method note: this worksheet is based on accessible abstract-level review framing and source-card-checked details, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The paper starts from disease prevalence and subclinical burden

- core_claim: HCM is the most common feline cardiomyopathy seen clinically and a meaningful fraction of cats may remain subclinical.
- implicit_premise: the HCM module has to be built for recognition before overt failure, not only around terminal disease.
- relation_to_previous: opening disease-framing problem.
- hard_details: the abstract states that HCM is the most common feline cardiomyopathy and may affect roughly up to 15% of domestic cats, mostly as subclinical disease.
- tension_or_surprise: common disease burden coexists with frequent diagnostic invisibility.

#### Unit 2: The review keeps recognition centered on structural assessment

- core_claim: biomarkers are supportive, but echocardiography leads practical diagnosis.
- implicit_premise: endpoint hierarchy should start with imaging-defined phenotype, not biomarker-first screening logic.
- relation_to_previous: moves from prevalence to operational recognition.
- hard_details: the abstract states that biomarkers should not be used on their own to diagnose HCM; severe HCM can usually be diagnosed by echocardiography.
- tension_or_surprise: even in a biomarker-rich era, the paper still protects echo from being displaced.

#### Unit 3: Mild-to-moderate hypertrophy remains an exclusion problem

- core_claim: borderline or moderate wall thickening cannot be flattened into a simple positive test result.
- implicit_premise: HCM recognition needs an explicit exclusion-zone branch.
- relation_to_previous: sharpens the recognition rule established in Unit 2.
- hard_details: the abstract states that mild to moderate wall thickening remains a diagnosis of exclusion.
- tension_or_surprise: this keeps uncertainty near the center of the HCM module rather than at the margins.

#### Unit 4: Clinical consequence is driven by filling dysfunction and atrial pressure

- core_claim: the dangerous downstream branch is not hypertrophy alone but the hemodynamic and atrial consequence layer.
- implicit_premise: mechanism and clinical-risk branches should connect through diastolic dysfunction and left-atrial burden.
- relation_to_previous: moves from diagnosis toward disease consequence.
- hard_details: the source card captures abstract-level framing that diastolic dysfunction and left-atrial consequences drive heart failure and arterial thromboembolism risk.
- tension_or_surprise: phenotype severity matters because of downstream loading and embolic consequence, not because hypertrophy is visually dramatic.

#### Unit 5: The review deliberately bounds treatment claims

- core_claim: current treatment does not reverse or slow the cardiomyopathic process.
- implicit_premise: translation should be modeled as management and consequence control, not disease reversal.
- relation_to_previous: converts disease consequence framing into treatment discipline.
- hard_details: the abstract states that no current treatment reverses or slows the underlying cardiomyopathic process.
- tension_or_surprise: strong review-level treatment pessimism is exactly what keeps the module from overpromising.

## Phase 1: Theme Reconstruction

## Theme: HCM should be modeled as a structural-phenotype-led disease

The strongest reusable contribution of this review is that feline HCM still has to be recognized through echocardiographic phenotype and exclusion logic. Biomarkers matter, but they do not replace structural definition.

### Hard Information

- HCM is the most common feline cardiomyopathy
- biomarkers should not be used alone for diagnosis
- severe disease is usually diagnosable by echocardiography
- mild to moderate wall thickening remains a diagnosis of exclusion

## Theme: The module needs a real exclusion-zone branch

This review does not let the reader pretend that every thickened ventricle is straightforward HCM. Borderline structural change sits in a diagnostic gray zone and must remain visible in the compiled architecture.

### Hard Information

- mild to moderate wall thickening remains a diagnosis of exclusion

## Theme: Translation should stay below phenotype recognition

The paper is useful because it keeps treatment language bounded. It does not support a reversal narrative and therefore helps protect the HCM module from treatment overcompression.

### Hard Information

- no current treatment reverses or slows the cardiomyopathic process

## Phase 2: Claim-Evidence Structure

### Recognition and Structure Key Points

**Claim 1**
- support: the abstract explicitly deprioritizes biomarker-only diagnosis
- details: biomarkers are supportive rather than standalone
- implicit_premise: endpoint hierarchy must keep imaging above blood-marker shortcuts

**Claim 2**
- support: the abstract states severe disease is usually diagnosable by echocardiography
- details: echo is the lead operational branch for confirmatory phenotype recognition
- implicit_premise: compiled HCM recognition should begin with structural phenotype

**Claim 3**
- support: the abstract states mild to moderate wall thickening remains a diagnosis of exclusion
- details: the disease map needs a bounded uncertainty zone
- implicit_premise: HCM cannot be reduced to one thickness threshold claim

### Translation-Boundary Key Points

**Claim 1**
- support: the abstract says no current treatment reverses or slows the cardiomyopathic process
- details: current intervention logic should be framed as consequence management
- implicit_premise: translation pages should not drift into disease-modifying overclaim

**Claim 2**
- support: the source is broad and modern, but only abstract-level extracted in this round
- details: it is safe for architectural write-back, not for fine-grained therapeutic ranking
- implicit_premise: treatment hierarchies still need later primary-study depth

## Phase 2.5: Write-Back Implications

### For `topics/hcm/risk-and-recognition.md`

- make the exclusion zone visible rather than hiding it behind a flat echo-positive story
- keep biomarker use supportive, not definitive

### For `topics/hcm/endpoint-handbook.md`

- rank echocardiography above biomarker-only logic
- keep screening markers below structural confirmation

### For `topics/hcm/translation-brief.md`

- explicitly state that management is not reversal of the core cardiomyopathic process

### For `topics/hcm/mechanism-overview.md`

- connect hypertrophy to diastolic dysfunction and atrial consequence rather than treating wall thickening as the whole disease

## Phase 3: Promotion Check

- source_card_updates:
  - keep this paper as the main broad HCM review anchor
  - preserve echo-led recognition and bounded treatment language
  - keep the exclusion-zone logic explicit
- topic_write_back_targets:
  - `topics/hcm/risk-and-recognition.md`
  - `topics/hcm/endpoint-handbook.md`
  - `topics/hcm/translation-brief.md`
  - `topics/hcm/mechanism-overview.md`
  - `topics/hcm/current-state-dashboard.md`
- not_safe_to_promote_yet:
  - any precise treatment ranking derived only from this review
  - any one-threshold simplification of mild-to-moderate hypertrophy
  - any biomarker-led diagnostic hierarchy that outranks structural confirmation
- conflicts_with_existing_vault:
  - none; this worksheet strengthens the current shell and makes its recognition hierarchy more defensible
