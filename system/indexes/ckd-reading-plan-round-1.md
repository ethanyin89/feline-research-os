# CKD Reading Plan — Round 1

Purpose:

- get the first usable CKD topic map fast
- avoid reading 12 papers with equal effort
- extract the minimum evidence needed to compile the first topic pages

## Strategy

Round 1 only answers this:

1. what CKD is, mechanistically
2. how CKD is diagnosed / staged
3. what the current management baseline is
4. what the guideline says
5. what a strong primary-study anchor looks like

That is enough to build the first compiled topic pages.

Everything else can wait for Round 2.

## Priority Tiers

### Tier A: Read First

These five should be read first, in this order.

#### 1. src-ckd-004

**Title:** ISFM Consensus Guidelines on the Diagnosis and Management of Feline Chronic Kidney Disease

**Why first:**

- likely the most operationally important source in the corpus
- gives a stable baseline for diagnosis, staging, and management
- helps prevent the rest of the notes from drifting into unanchored summary

**What to extract:**

- explicit diagnostic recommendations
- staging logic
- management recommendations
- places where the guideline is evidence-backed vs consensus-heavy
- named endpoints or monitoring markers

**Primary write-back targets:**

- `topics/ckd/index.md`
- `topics/ckd/endpoint-handbook.md`
- `topics/ckd/regulatory-brief.md` only if practice guidance overlaps pathway discussion

#### 2. src-ckd-001

**Title:** Feline CKD: Pathophysiology and risk factors — what do we know?

**Why second:**

- strongest broad mechanism framing source in the current set
- should define the initial disease model before narrower mechanistic cards get created

**What to extract:**

- major pathophysiologic mechanisms
- strongest named risk factors
- which mechanisms seem feline-specific vs generic CKD framing
- candidate mechanism entities to create next

**Primary write-back targets:**

- `topics/ckd/mechanism-overview.md`
- `entities/mechanisms/*.md`

#### 3. src-ckd-002

**Title:** Feline CKD: Diagnosis, staging and screening – what is recommended?

**Why third:**

- most likely to define the first real endpoint shortlist
- complements the ISFM guideline with a tighter diagnostic lens

**What to extract:**

- recommended diagnostic markers
- screening recommendations
- staging criteria
- which markers are central vs auxiliary
- how the paper frames sensitivity / specificity / utility if discussed

**Primary write-back targets:**

- `topics/ckd/endpoint-handbook.md`
- `entities/endpoints/creatinine.md`
- `entities/endpoints/sdma.md`

#### 4. src-ckd-003

**Title:** Feline CKD: Current therapies – what is achievable?

**Why fourth:**

- establishes the treatment baseline
- gives the first translational map before diving into narrower therapy reviews

**What to extract:**

- major therapy categories
- claimed achievable outcomes
- which therapies appear standard-of-care vs exploratory
- what endpoints are actually used to judge benefit

**Primary write-back targets:**

- `topics/ckd/index.md`
- `topics/ckd/endpoint-handbook.md`
- future translation page if added later

#### 5. src-ckd-010

**Title:** Histomorphometry of Feline Chronic Kidney Disease and Correlation With Markers of Renal Dysfunction

**Why fifth:**

- strongest primary-study candidate in the seed set
- useful reality check against review-heavy synthesis
- bridges pathology and measurable dysfunction markers

**What to extract:**

- study design and sample type
- measured pathology features
- measured renal dysfunction markers
- strength and direction of correlations
- what this supports, and what it does not support

**Primary write-back targets:**

- `topics/ckd/mechanism-overview.md`
- `topics/ckd/endpoint-handbook.md`

### Tier B: Read Second

These matter, but only after Tier A has been extracted.

#### src-ckd-011

Renal fibrosis source. Good for deepening mechanism after the broad map exists.

#### src-ckd-007

Evidence-focused therapy review. Good for pressure-testing current treatment claims.

#### src-ckd-006

Hyperphosphatemia treatment source. Important once phosphorus becomes a tracked endpoint.

#### src-ckd-009

CKD-hypertension comorbidity. Useful for endpoint context and patient stratification.

#### src-ckd-012

Risk-factor case-control study. Good for checking whether review-level risk claims are well grounded.

### Tier C: Read Third

Useful, but not needed to compile the first usable wiki.

#### src-ckd-005

Future directions piece. Better after the current-state map is stable.

#### src-ckd-008

Prevention framing. Important later, but not needed for V1 baseline compilation.

## Extraction Template

For each Tier A paper, extract these fields before moving on:

1. one-sentence summary
2. 3-7 quoted facts
3. 2-5 source-supported conclusions
4. 1-3 explicit uncertainties
5. linked entities
6. write-back targets

If a paper cannot yield at least 3 quoted facts, note why. Do not force synthesis.

## First Compilation Target

After Tier A is done, compile only these pages:

- `topics/ckd/index.md`
- `topics/ckd/mechanism-overview.md`
- `topics/ckd/endpoint-handbook.md`

Do not try to fully compile every CKD page yet.

## Round 1 Exit Criteria

Round 1 is complete when:

- all 5 Tier A source cards have non-empty `quoted_fact`
- at least 3 of the 5 have non-empty `source_supported_conclusion`
- mechanism page has a first real outline
- endpoint page has a first real endpoint shortlist
- topic index no longer says “source ingest pending”

## What To Ignore For Now

- complete regulatory pathway comparison
- fully normalized model taxonomy
- comprehensive treatment evidence ranking
- broad prevention strategy synthesis

Those are Round 2 problems.
