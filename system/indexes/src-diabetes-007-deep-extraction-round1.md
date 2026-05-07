# Deep Extraction Worksheet

Source: `src-diabetes-007`  
Title: `Systematic review of feline diabetic remission: Separating fact from opinion`  
Method note: this worksheet is based on PubMed abstract-level evidence and source-card metadata, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The paper starts from remission being possible

- core_claim: diabetic remission is increasingly recognized as possible in cats.
- implicit_premise: remission must be represented in the module, but as an evidence-bounded endpoint.
- relation_to_previous: opening remission frame.
- hard_details: abstract states that remission is possible and that the review follows Cochrane Collaboration guidance.
- tension_or_surprise: the title explicitly separates fact from opinion, warning against overclaim.

#### Unit 2: The review grades evidence and bias

- core_claim: remission evidence is assessed through systematic methods and bias tools.
- implicit_premise: not all remission predictors or protocols should be weighted equally.
- relation_to_previous: establishes evidence-control method.
- hard_details: 22 studies were included; reviewers assigned levels of evidence using established tools.
- tension_or_surprise: the review is valuable because it judges evidence quality, not just remission frequency.

#### Unit 3: Evidence quality is only moderate to poor

- core_claim: current remission evidence has major design limitations.
- implicit_premise: compiled pages should avoid confident remission-rate comparisons.
- relation_to_previous: converts systematic review into caution.
- hard_details: common issues include lack of randomization/blinding, small sample sizes, missing diagnostic/remission criteria, and poor confounder control.
- tension_or_surprise: the strongest remission source is also the strongest reason to slow down.

#### Unit 4: No single factor predicts remission

- core_claim: remission has been documented across different insulin types and protocols; no single factor predicts it.
- implicit_premise: the treatment page should not turn one protocol, insulin, or diet into a universal remission rule.
- relation_to_previous: applies evidence-quality caution to clinical interpretation.
- hard_details: abstract says no single factor predicts remission and notes that carbohydrate reduction may be beneficial but needs more study.
- tension_or_surprise: remission optimism survives, but deterministic prediction does not.

## Phase 1: Theme Reconstruction

## Theme: Remission is real but overclaim-prone

The paper supports remission as a real clinical endpoint while warning that the evidence base is too weak for simple ranking claims.

### Hard Information

- 22 studies were included
- evidence quality was moderate to poor
- no single factor predicts remission
- remission has been documented with multiple insulin types and protocols

## Theme: Future research quality is part of the finding

This review is not just a clinical summary. It identifies why the field cannot yet support reliable meta-analysis or strong protocol comparisons.

### Hard Information

- frequent limitations include lack of randomization/blinding, small samples, missing remission criteria, and confounding

## Phase 2: Claim-Evidence Structure

### Remission-Boundary Key Points

**Claim 1**
- support: systematic review design and included-study count
- details: this source should be the remission boundary owner
- implicit_premise: lower-quality remission claims should defer to this review

**Claim 2**
- support: abstract-level evidence-quality judgment
- details: remission predictors and protocol comparisons are not settled
- implicit_premise: treatment pages need uncertainty markers

**Claim 3**
- support: abstract-level statement about no single predictor
- details: multiple insulin types and protocols have documented remission
- implicit_premise: avoid single-factor remission stories

## Phase 2.5: Write-Back Implications

### For `topics/diabetes/endpoint-handbook.md`

- define remission as a core endpoint but mark it evidence-fragile

### For `topics/diabetes/translation-brief.md`

- avoid ranking protocols by remission without deep extraction

### For `topics/diabetes/synthesis-index.md`

- add remission boundary memo as the first narrow-owner candidate

## Phase 3: Promotion Check

- source_card_updates:
  - promote to the remission boundary anchor
  - include bias and evidence-quality limitations
- topic_write_back_targets:
  - `topics/diabetes/endpoint-handbook.md`
  - `topics/diabetes/translation-brief.md`
  - `topics/diabetes/synthesis-index.md`
  - `topics/diabetes/current-state-dashboard.md`
- not_safe_to_promote_yet:
  - any precise remission-rate comparison
  - any claim that one diet or insulin type reliably predicts remission
  - any remission predictor not confirmed through full-text extraction
- conflicts_with_existing_vault:
  - it tightens the shell by preventing remission enthusiasm from becoming a protocol claim

