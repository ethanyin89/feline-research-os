# Deep Extraction Worksheet

Source: `src-ckd-018`  
Title: `Early detection of feline chronic kidney disease via 3-hydroxykynurenine and machine learning`  
Method note: this worksheet is based on accessible full open-access article text, especially abstract, results, discussion, and methods framing.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The paper targets the exact unsolved early-detection problem

- core_claim: routine CKD tests are still too weak for early feline CKD detection, so the study tests whether metabolomic markers can identify disease earlier.
- implicit_premise: earlier recognition is clinically valuable if it can be done with sufficient predictive performance.
- relation_to_previous: opening problem statement.
- hard_details: advanced CKD is easier to diagnose; early CKD remains difficult with routine tests.
- tension_or_surprise: this paper is directly attacking the weakest current branch in the vault.

#### Unit 2: The study combines cross-sectional discovery with longitudinal validation

- core_claim: this is not only a one-time case-control comparison; it also tests prediction in an independent longitudinal population.
- implicit_premise: a biomarker story is stronger when it survives beyond baseline cross-sectional separation.
- relation_to_previous: moves from problem to design.
- hard_details: baseline population was 61 healthy cats and 63 CKD2 cats; longitudinal validation included 26 cats remaining healthy and 22 cats developing CKD2 within one year.
- tension_or_surprise: this makes the paper stronger than a pure discovery metabolomics paper, but still not equivalent to broad clinical validation.

#### Unit 3: 3-hydroxykynurenine is the best individual candidate, not the whole solution

- core_claim: S/U 3-hydroxykynurenine is the best individual biomarker candidate in the dataset.
- implicit_premise: a useful single biomarker can emerge from matrix-ratio thinking rather than serum-only thinking.
- relation_to_previous: moves from study design to individual-marker result.
- hard_details: S/U 3-hydroxykynurenine had AUC 0.844 and accuracy 0.804; it stayed stable in healthy cats and rose in cats later developing CKD2.
- tension_or_surprise: the most interesting individual biomarker here is not SDMA.

#### Unit 4: Multi-marker modelling outperforms any single marker

- core_claim: ML and multivariate approaches perform better than any single biomarker alone.
- implicit_premise: early CKD signal may be distributed across multiple metabolites and clinical parameters.
- relation_to_previous: expands from single-marker result to panel-level prediction.
- hard_details: linear SVM with metabolites and clinical parameters reached AUC 0.929 and accuracy 0.862 at T-6.
- tension_or_surprise: the title emphasizes one metabolite, but the operationally strongest story is actually panel-based.

#### Unit 5: The paper also weakens SDMA-as-shortcut thinking

- core_claim: SDMA matters, but it does not dominate the early-detection picture in this study.
- implicit_premise: current early-detection practice may overread SDMA as a lone solution.
- relation_to_previous: reframes the meaning of the model results against the current biomarker landscape.
- hard_details: SDMA ranked only 14th as an individual metabolite at T-6; poor sensitivity values were reported at T0, T-6, and T-12.
- tension_or_surprise: this is one of the clearest current vault sources against one-marker SDMA overpromotion.

#### Unit 6: The strongest result still sits inside a bounded disease-definition frame

- core_claim: the performance claims have real limits because only CKD2 cats were included and some earlier disease-state ambiguity remained.
- implicit_premise: predicting future CKD2 is not identical to solving the true earliest-disease detection problem.
- relation_to_previous: defines the ceiling of promotion.
- hard_details: only CKD2 cats were included; possible CKD1 cats at T-6 could have inflated performance; GFR and renal ultrasonography were absent.
- tension_or_surprise: this is promising, but still not a clinically finished screening solution.

## Phase 1: Theme Reconstruction

## Theme: The early-detection layer can now include a real metabolomic frontier

This paper is strong enough to force a structural update in the vault. Early detection is no longer only a story about serial creatinine, USG, proteinuria context, and optional SDMA support. It is now also a story about an emerging metabolomic frontier that may augment those tools.

### Hard Information

- baseline: 61 healthy, 63 CKD2
- longitudinal: 26 healthy, 22 future CKD2
- six-month earlier discrimination

## Theme: The best single marker and the best model are different things

The paper separates two claims that should not be collapsed. S/U 3-hydroxykynurenine is the best individual biomarker candidate in this dataset. But the strongest predictive performance comes from multi-marker models that combine metabolites and clinical parameters.

### Hard Information

- S/U 3-hydroxykynurenine AUC 0.844, accuracy 0.804
- linear SVM with metabolites and clinical parameters AUC 0.929, accuracy 0.862

## Theme: The paper strengthens innovation, but not routine readiness

The study is more robust than a simple case-control paper because it includes an independent longitudinal cohort. Even so, it does not justify a routine workflow rewrite because sample size is limited, CKD1 is not directly characterized, and the assay pathway remains metabolomics-heavy.

### Hard Information

- only CKD2 included
- possible CKD1 at T-6
- no GFR
- no renal ultrasonography

## Theme: SDMA should be re-positioned as one ingredient, not the answer

This study does not make SDMA irrelevant, but it clearly argues against treating SDMA as the dominant single early-detection solution. In this dataset, SDMA contributed inside models more than it succeeded alone.

### Hard Information

- SDMA 14th at T-6 as individual predictor
- poor individual SDMA sensitivity values

## Theme: Frontier signal and routine readiness are different claims

This paper is strongest when it is used to support a frontier-outcome claim:

- earlier discrimination may improve if multi-marker panel logic becomes real

It is much weaker if used to support a routine-workflow claim:

- machine-learning metabolomic screening is ready for practice

### Hard Information

- the longitudinal validation cohort was still modest in size
- only CKD2 cats were included
- no GFR or ultrasonography was used to adjudicate possible earlier CKD1 cases
- the workflow remained metabolomics-heavy rather than clinic-light

## Phase 2: Claim-Evidence Structure

### Early-Detection Innovation Key Points

**Claim 1**
- support: the study identified earlier discrimination up to six months before traditional diagnosis
- details: longitudinal validation population was independent from the baseline discovery/training set
- implicit_premise: this is stronger than pure discovery-stage signal hunting

**Claim 2**
- support: S/U 3-hydroxykynurenine was the strongest individual biomarker candidate
- details: AUC 0.844 and accuracy 0.804
- implicit_premise: matrix-ratio biomarkers may outperform familiar single serum analytes

**Claim 3**
- support: SVM-based modelling with metabolites and clinical parameters outperformed individual biomarkers
- details: AUC 0.929 and accuracy 0.862
- implicit_premise: early CKD detection may require panel logic rather than one-marker replacement logic

### Boundary-Setting Key Points

**Claim 1**
- support: only CKD2 cats were included and some T-6 cats may already have had CKD1
- details: no GFR or ultrasonography for deeper earliest-stage adjudication
- implicit_premise: performance may overestimate true de novo earliest-disease screening utility

**Claim 2**
- support: SDMA performed modestly as an individual predictor in this dataset
- details: ranked 14th at T-6; poor sensitivity values reported
- implicit_premise: routine early-detection workflows should not be flattened into SDMA-only logic

**Claim 3**
- support: the strongest story in this paper is panel augmentation of early-detection architecture, not routine replacement of serial surveillance
- details: the best single marker and the best overall model were different
- implicit_premise: frontier outcome signal should remain bounded until workflow readiness and broader validation improve

## Phase 2.5: Write-Back Implications

### For `early-detection.md`

- keep serial surveillance as the practical backbone
- add that the frontier signal is outcome-architecture widening, not routine workflow replacement

### For `sdma-positioning.md`

- keep SDMA relevant
- sharpen the point that SDMA is one ingredient inside a broader frontier and not the dominant single answer in this study

### For `ckd-outcome-architecture-memo.md`

- use this paper to distinguish `frontier outcome signal` from `routine endpoint readiness`

## Phase 3: Promotion Check

- source_card_updates:
  - add real cohort and performance numbers
  - separate single-biomarker and multi-marker claims
  - add CKD2-only and no-GFR limits
  - add frontier-signal-versus-routine-readiness boundary
- topic_write_back_targets:
  - `topics/ckd/early-detection.md`
  - `topics/ckd/synthesis-index.md`
  - `topics/ckd/endpoint-handbook.md`
  - `topics/ckd/sdma-positioning.md`
  - `system/indexes/ckd-outcome-architecture-memo.md`
- not_safe_to_promote_yet:
  - any claim that machine learning is ready to replace serial surveillance
  - any claim that 3-hydroxykynurenine is already a routine clinical screening assay
  - any claim that this paper solves CKD1 detection
  - any claim that frontier outcome signal alone proves routine endpoint readiness
- conflicts_with_existing_vault:
  - none; this paper complicates but does not overturn the serial-surveillance frame
