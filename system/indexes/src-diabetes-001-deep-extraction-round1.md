# Deep Extraction Worksheet

Source: `src-diabetes-001`  
Title: `Pathogenesis of Feline Diabetes`  
Method note: this worksheet is based on PubMed abstract-level evidence and source-card metadata, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The paper starts from inadequate insulin secretion

- core_claim: feline diabetes is framed around inadequate insulin secretion.
- implicit_premise: beta-cell failure has to stay visible even when insulin resistance is the most obvious upstream pressure.
- relation_to_previous: opening mechanism frame.
- hard_details: PubMed abstract states that diabetes mellitus results from inadequate insulin secretion.
- tension_or_surprise: a module built only around insulin resistance would miss the final failure point.

#### Unit 2: Reduced insulin sensitivity raises secretory demand

- core_claim: cats often develop diabetes in settings that reduce insulin sensitivity and increase insulin demand.
- implicit_premise: upstream insulin-resistance states belong in the causal spine, not only in risk pages.
- relation_to_previous: links beta-cell insufficiency to predisposing conditions.
- hard_details: the abstract names obesity, acromegaly, and pancreatitis as common predisposing causes.
- tension_or_surprise: pancreatitis and acromegaly are not peripheral comorbidities; they may change disease type and management logic.

#### Unit 3: Beta-cell failure mechanisms remain incompletely understood

- core_claim: the mechanisms preventing adequate beta-cell insulin secretion are not fully settled.
- implicit_premise: the module should preserve uncertainty instead of pretending there is a single causal path.
- relation_to_previous: narrows from clinical predisposition to cellular injury.
- hard_details: the abstract lists inflammatory mediators, reactive oxygen species, toxic intracellular protein oligomers, and glucotoxicity as possible contributors.
- tension_or_surprise: the review gives a candidate mechanism cluster, not a finished causal chain.

## Phase 1: Theme Reconstruction

## Theme: Feline diabetes needs a two-part mechanism spine

The strongest reusable contribution is the separation of insulin-resistance pressure from inadequate insulin secretion. Obesity, acromegaly, and pancreatitis increase the demand side; beta-cell failure determines whether that pressure becomes overt diabetes.

### Hard Information

- inadequate insulin secretion is central
- reduced insulin sensitivity increases insulin-secretory demand
- obesity, acromegaly, and pancreatitis are named predisposing causes

## Theme: Mechanism uncertainty should stay visible

The paper does not reduce beta-cell failure to one cause. It lists multiple possible injury mechanisms, which makes this a guardrail against overconfident mechanism pages.

### Hard Information

- possible beta-cell stressors include inflammatory mediators, oxidative stress, toxic protein oligomers, and high-glucose toxicity

## Phase 2: Claim-Evidence Structure

### Mechanism Key Points

**Claim 1**
- support: abstract-level statement that diabetes results from inadequate insulin secretion
- details: source supports beta-cell failure as an essential disease endpoint
- implicit_premise: insulin resistance alone is insufficient as a complete disease explanation

**Claim 2**
- support: abstract-level naming of obesity, acromegaly, and pancreatitis
- details: these should be represented as causal pressure branches
- implicit_premise: comorbidity pages and mechanism pages should share a common architecture

**Claim 3**
- support: abstract-level list of candidate beta-cell injury mechanisms
- details: the review points to multiple possible mechanisms rather than one settled cause
- implicit_premise: compiled pages should preserve uncertainty until fuller extraction

## Phase 2.5: Write-Back Implications

### For `topics/diabetes/mechanism-overview.md`

- make the core spine `insulin resistance pressure -> beta-cell failure -> overt diabetes`
- keep obesity, acromegaly, and pancreatitis in mechanism view

### For `topics/diabetes/risk-and-recognition.md`

- treat acromegaly and pancreatitis as disease-shaping risk/comorbidity branches

### For `topics/diabetes/synthesis-index.md`

- frame diabetes as mixed metabolic-endocrine disease, not a single pathway

## Phase 3: Promotion Check

- source_card_updates:
  - promote this to a Tier A mechanism anchor
  - thicken evidence policy with abstract-level beta-cell and insulin-resistance facts
- topic_write_back_targets:
  - `topics/diabetes/mechanism-overview.md`
  - `topics/diabetes/risk-and-recognition.md`
  - `topics/diabetes/synthesis-index.md`
- not_safe_to_promote_yet:
  - precise causal weighting among beta-cell injury mechanisms
  - treatment consequences of each predisposing cause
  - any full-text-only mechanism detail not present in the abstract
- conflicts_with_existing_vault:
  - none; this worksheet strengthens the current diabetes shell

