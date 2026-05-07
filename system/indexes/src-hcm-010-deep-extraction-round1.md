# Deep Extraction Worksheet

Source: `src-hcm-010`  
Title: `Investigation into the use of plasma NT-proBNP concentration to screen for feline hypertrophic cardiomyopathy`  
Method note: this worksheet is based on accessible abstract-level study framing and source-card-checked details, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The paper asks a screening question, not a full diagnostic one

- core_claim: NT-proBNP is being evaluated specifically as a screening tool for subclinical HCM.
- implicit_premise: this study belongs in a screening-augmentation branch, not in a definitive diagnosis branch.
- relation_to_previous: opening use-case framing.
- hard_details: the abstract explicitly states the objective was to evaluate NT-proBNP as a screening tool for cats with subclinical HCM.
- tension_or_surprise: the paper's own question is narrower than general diagnostic authority.

#### Unit 2: Severe disease produces a usable signal

- core_claim: NT-proBNP meaningfully identifies severe HCM in the studied population.
- implicit_premise: biomarker value increases as phenotype burden increases.
- relation_to_previous: moves from study aim to positive result.
- hard_details: the abstract reports significant elevation in severe HCM and that values above 44 pmol/L accurately predicted severe HCM.
- tension_or_surprise: the test is not useless; it is just narrower than a universal screen.

#### Unit 3: Moderate and equivocal disease remain a failure zone

- core_claim: NT-proBNP does not adequately identify moderate or equivocal HCM in this cohort.
- implicit_premise: the biomarker cannot replace structural workup for earlier or borderline disease.
- relation_to_previous: sharply limits the positive result from Unit 2.
- hard_details: the abstract states NT-proBNP was not increased in cats with moderate or equivocal HCM compared with normal cats.
- tension_or_surprise: a screening paper becomes a boundary paper against overclaim.

#### Unit 4: The conclusion is narrower than many biomarker summaries imply

- core_claim: the test cannot be used to screen for mild-to-moderate HCM in the studied colony.
- implicit_premise: compiled endpoint pages should explicitly separate severe-disease flagging from early screening competence.
- relation_to_previous: converts the negative result into an architectural rule.
- hard_details: the abstract concludes that the test cannot be used to screen cats for the presence of mild to moderate HCM.
- tension_or_surprise: the most reusable value of the paper is probably its limitation.

## Phase 1: Theme Reconstruction

## Theme: NT-proBNP is a severe-disease flag, not a universal screen

This study is useful because it gives the HCM module a clean boundary. NT-proBNP may identify severe disease, but it does not justify biomarker-led screening for mild or equivocal HCM.

### Hard Information

- significant elevation in severe HCM
- threshold above 44 pmol/L predicted severe HCM
- no increase in moderate or equivocal HCM versus normal cats

## Theme: Screening and diagnosis must remain separate branches

The paper helps prevent the endpoint architecture from collapsing screening augmentation into diagnostic authority.

### Hard Information

- the study objective is screening
- the study conclusion rejects use for mild-to-moderate screening in the evaluated colony

## Phase 2: Claim-Evidence Structure

### Biomarker-Screening Key Points

**Claim 1**
- support: the abstract shows strong performance in severe HCM
- details: NT-proBNP can flag heavier phenotype burden
- implicit_premise: severe disease detection and mild-disease screening are different problems

**Claim 2**
- support: the abstract shows failure in moderate and equivocal disease
- details: the biomarker should not be promoted into general HCM screening authority
- implicit_premise: structural phenotype assessment remains indispensable

**Claim 3**
- support: the cohort came from Maine Coon and Maine Coon crossbred colony cats with genotype context
- details: generalizability should remain bounded
- implicit_premise: external routine-use conclusions should stay conservative

## Phase 2.5: Write-Back Implications

### For `topics/hcm/endpoint-handbook.md`

- place NT-proBNP in screening augmentation and severe-disease flagging
- explicitly note failure in mild-to-moderate screening

### For `topics/hcm/risk-and-recognition.md`

- keep biomarker use secondary to structural workup for equivocal disease

## Phase 3: Promotion Check

- source_card_updates:
  - preserve the severe-versus-mild boundary
  - keep the screening use case narrower than diagnosis
- topic_write_back_targets:
  - `topics/hcm/endpoint-handbook.md`
  - `topics/hcm/risk-and-recognition.md`
  - `topics/hcm/current-state-dashboard.md`
- not_safe_to_promote_yet:
  - any claim that NT-proBNP is a reliable general screen for early HCM
  - any claim that this colony study fully defines routine clinical practice outside similar populations
- conflicts_with_existing_vault:
  - none; this worksheet sharply improves endpoint-boundary discipline
