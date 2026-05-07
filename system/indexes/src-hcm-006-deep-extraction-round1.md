# Deep Extraction Worksheet

Source: `src-hcm-006`  
Title: `Cardiac Troponin I in Feline Hypertrophic Cardiomyopathy`  
Method note: this worksheet is based on accessible abstract-level study framing and source-card-checked details, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The study is about myocardial injury signal, not primary phenotype definition

- core_claim: cTnI is being evaluated as a marker of myocardial damage in cats with HCM.
- implicit_premise: biomarker interpretation should be tied to injury burden rather than confused with structural disease definition.
- relation_to_previous: opening biomarker-use-case rule.
- hard_details: the abstract frames cTnI as a sensitive and specific means of detecting myocardial damage.
- tension_or_surprise: the paper starts from damage biology, not from screening convenience.

#### Unit 2: The marker separates moderate-to-severe HCM from normal cats

- core_claim: cTnI is substantially elevated in moderate-to-severe HCM compared with healthy controls.
- implicit_premise: this biomarker has operational value, but likely in more advanced disease states.
- relation_to_previous: moves from assay rationale to discriminative performance.
- hard_details: the abstract reports 33 control cats and 20 cats with moderate to severe HCM, with 85% sensitivity and 97% specificity for differentiating diseased from normal cats.
- tension_or_surprise: useful discrimination does not automatically make it a universal screen.

#### Unit 3: Correlation with structure is limited

- core_claim: cTnI does not map cleanly onto all structural severity measures.
- implicit_premise: the marker should not be treated as a structural surrogate.
- relation_to_previous: constrains the value suggested in Unit 2.
- hard_details: the abstract reports only weak correlation with left-ventricular free-wall thickness and no clear correlation with some other indices.
- tension_or_surprise: strong group separation coexists with imperfect structural correlation.

#### Unit 4: Heart failure status pushes the marker higher

- core_claim: cTnI is higher in cats with active congestive heart failure.
- implicit_premise: the marker may be more useful for burden or consequence stratification than for early recognition.
- relation_to_previous: turns biomarker signal into use-case ranking.
- hard_details: the abstract states cats with congestive heart failure at sampling had significantly higher cTnI than other HCM cats.
- tension_or_surprise: the biomarker seems strongest when disease is already clinically consequential.

## Phase 1: Theme Reconstruction

## Theme: Troponin belongs to the injury/severity branch, not the phenotype-definition branch

This study is valuable because it gives the HCM module a strong blood-marker signal without justifying biomarker-first diagnosis. It is better read as an injury-burden marker than as a replacement for echo.

### Hard Information

- significantly higher cTnI in HCM cats than normal cats
- 85% sensitivity and 97% specificity for moderate-to-severe HCM versus normal cats
- only weak correlation with some structural measures

## Theme: Troponin signal strengthens with active clinical burden

The heart-failure result suggests that cTnI becomes more informative as disease consequence intensifies.

### Hard Information

- higher cTnI in cats with active congestive heart failure

## Phase 2: Claim-Evidence Structure

### Biomarker-Use-Case Key Points

**Claim 1**
- support: the abstract demonstrates strong separation of moderate-to-severe HCM from normal controls
- details: cTnI has real endpoint value
- implicit_premise: biomarker branches should remain visible in the HCM module

**Claim 2**
- support: structural correlations are weak or incomplete
- details: cTnI should not be promoted to phenotype-definition authority
- implicit_premise: echo and morphometry remain above troponin in the hierarchy

**Claim 3**
- support: the marker is higher in active heart failure
- details: cTnI is likely useful for consequence and severity interpretation
- implicit_premise: endpoint architecture should distinguish diagnosis from burden stratification

## Phase 2.5: Write-Back Implications

### For `topics/hcm/endpoint-handbook.md`

- place cTnI under biomarker and severity-linked interpretation
- keep it below structural confirmation

### For `topics/hcm/risk-and-recognition.md`

- avoid using troponin as a standalone recognition shortcut

## Phase 3: Promotion Check

- source_card_updates:
  - preserve cTnI as a real but bounded biomarker signal
  - keep its stronger tie to advanced burden visible
- topic_write_back_targets:
  - `topics/hcm/endpoint-handbook.md`
  - `topics/hcm/risk-and-recognition.md`
  - `topics/hcm/current-state-dashboard.md`
- not_safe_to_promote_yet:
  - any claim that cTnI is a sufficient screen for all HCM
  - any claim that cTnI can replace imaging or morphometry
- conflicts_with_existing_vault:
  - none; this worksheet sharpens biomarker ranking
