# CKD Reading Plan — Round 2

Purpose:

- use the 12 newly ingested CKD sources to densify the thinnest layers
- avoid reading all new papers with equal effort
- choose papers that are most likely to change the compiled map

## Strategy

Round 2 is not trying to rebuild the whole CKD topic.

It is targeting the specific weak spots that still limit the vault:

1. SDMA and biomarker positioning
2. treatment-trial outcome logic
3. explicit experimental-model evidence
4. proteinuria / pathology bridge strengthening
5. older-cat morphology / pathogenesis densification

## Priority Tiers

### Tier A: Read First

Status: completed on 2026-04-08.

These five should be read first, in this order.

#### 1. src-ckd-024

**Title:** Renal biomarkers in cats: A review of the current status in chronic kidney disease

**Why first:**

- likely the best new source for the current weak point around SDMA positioning
- directly relevant to endpoint-handbook, early-detection, and sdma-positioning
- may reduce one of the most repeated uncertainty statements in the vault

**What to extract:**

- how the review positions SDMA relative to creatinine and USG
- which biomarkers are practical versus investigational
- whether the review supports ranking markers by use case
- what remains unresolved even in the review

**Primary write-back targets:**

- `topics/ckd/sdma-positioning.md`
- `topics/ckd/endpoint-handbook.md`
- `topics/ckd/early-detection.md`
- `entities/endpoints/sdma.md`

#### 2. src-ckd-013

**Title:** What outcomes should be measured in feline chronic kidney disease treatment trials? Establishing a core outcome set for research

**Why second:**

- likely the strongest new source for trial-grade endpoint selection
- directly useful for moving from general endpoint discussion to treatment-trial logic
- may materially improve translation-brief and future efficacy-evaluation outputs

**What to extract:**

- proposed core outcomes
- how outcomes are grouped or prioritized
- whether owner-centered and biochemical outcomes are separated
- whether the paper implies a trial-design hierarchy

**Primary write-back targets:**

- `topics/ckd/translation-brief.md`
- `topics/ckd/endpoint-handbook.md`
- future trial-design page if justified

#### 3. src-ckd-022

**Title:** Chronic Renal Changes After a Single Ischemic Event in an Experimental Model of Feline Chronic Kidney Disease

**Why third:**

- model layer is still one of the thinnest areas in the vault
- this may be the strongest explicit experimental-model source currently available
- likely the highest-leverage paper for testing whether the model map should change materially

**What to extract:**

- model design
- lesion and time-course pattern
- which readouts were measured
- how well the model resembles naturally occurring feline CKD
- where translational relevance breaks down

**Primary write-back targets:**

- `topics/ckd/model-map.md`
- `topics/ckd/model-summary.md`
- `topics/ckd/synthesis-index.md`

#### 4. src-ckd-017

**Title:** Clinicopathologic and pathologic characteristics of feline proteinuric kidney disease

**Why fourth:**

- proteinuria is already a major bridge variable in the vault
- this source likely strengthens that branch with additional primary-study grounding
- may improve both pathology-correlations and endpoint-handbook

**What to extract:**

- what lesions correlate with proteinuria
- how proteinuric kidney disease is characterized clinicopathologically
- whether findings refine UPCR/proteinuria interpretation
- what the study supports, and what it does not generalize

**Primary write-back targets:**

- `topics/ckd/pathology-correlations.md`
- `topics/ckd/endpoint-handbook.md`
- `entities/endpoints/upcr.md`

#### 5. src-ckd-016

**Title:** Chronic Kidney Disease in Aged Cats: Clinical Features, Morphology, and Proposed Pathogeneses

**Why fifth:**

- likely useful for connecting older-cat surveillance with morphology and proposed pathogeneses
- may strengthen the current disease framing without simply repeating fibrosis
- could help the aged-cat natural-history side of CKD feel less thin

**What to extract:**

- clinical features in aged cats
- key morphological findings
- which pathogeneses are proposed versus strongly supported
- how the paper frames age, structure, and progression

**Primary write-back targets:**

- `topics/ckd/mechanism-overview.md`
- `topics/ckd/pathology-correlations.md`
- `topics/ckd/early-detection.md`

### Tier B: Read Second

These matter, but only after Tier A has been extracted.

#### src-ckd-018

Newer early-detection biomarker plus machine-learning paper. High-interest, but likely needs cautious reading before promotion.

#### src-ckd-015

Mineral and bone disorder review. Good for deepening the phosphorus/PTH/calcium branch after the endpoint core is stabilized.

#### src-ckd-019

Hyperthyroidism comorbidity review. Likely useful for interpretation realism, but not a first-wave map changer.

#### src-ckd-021

Aldosterone / mineralocorticoid-receptor target framing. Mechanistically interesting, but probably second-generation expansion.

#### src-ckd-023

Telomere / senescence paper. Useful for mechanism richness, but not yet obviously map-changing for V1.

### Tier C: Read Third

Useful, but not needed to change the compiled state immediately.

#### src-ckd-014

Practice-pattern questionnaire. Good contextual source, but weaker for backbone claims.

#### src-ckd-020

Ultrasound review. Useful for workup completeness, but not currently as valuable as biomarker, model, or pathology densification.

## Round 2 Exit Criteria

Round 2 is complete when:

- at least 3 Tier A source cards have real `quoted_fact`
- at least 2 Tier A papers produce meaningful topic write-back
- SDMA uncertainty is reduced in one compiled page
- model layer is strengthened by at least one real experimental-model source
- translation layer gets at least one trial-outcome-oriented update

Current status:

- all 5 Tier A source cards now have real `quoted_fact`
- all 5 Tier A papers produced topic write-back
- SDMA uncertainty was reduced in `sdma-positioning.md` and `endpoint-handbook.md`
- model layer now includes one explicit ischemic experimental anchor via `src-ckd-022`
- translation layer now includes trial-outcome architecture via `src-ckd-013`

See:

- [CKD Round 2 Tier A synthesis memo](ckd-round-2-tier-a-synthesis-memo.md)

## Best Next Step After Tier A

- read `src-ckd-018` next
- keep the same bounded approach
- do not promote machine-learning novelty faster than source support allows

## Do Not Do In Round 2

- do not try to read all 12 new papers deeply
- do not create a new topic page for every interesting branch
- do not over-promote machine-learning or biomarker novelty without careful limits
