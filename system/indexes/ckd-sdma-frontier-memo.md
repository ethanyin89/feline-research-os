---
id: system-ckd-sdma-frontier-memo
type: system
topic: ckd
last_compiled_at: 2026-04-09
owner: codex
status: active
language: en
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
---

# CKD SDMA Frontier Memo

Date: 2026-04-09  
Scope: `src-ckd-004`, `src-ckd-018`, `src-ckd-024`

This memo compresses the current SDMA and early-detection frontier into one bounded positioning page.

## What This Memo Is For

This page is not trying to settle the final rank order of feline CKD biomarkers.

It does something narrower and more useful:

- clarify what SDMA now contributes in the current vault
- separate SDMA-support logic from SDMA-overclaim logic
- place metabolomic and machine-learning innovation in the right frontier bucket
- keep serial surveillance as the current operational backbone

This page is an English working memo.  
It is not a bilingual summary and it is not a decision-grade diagnostic recommendation.

## Core Position

The current vault now supports three statements at the same time:

1. SDMA matters.
2. SDMA is not the whole early-detection answer.
3. The strongest innovation signal beyond SDMA currently comes from metabolomic-panel logic, not from a single routine-ready replacement marker.

## Key-Claim Traceability

| Claim ID | Key Claim | Claim Level | Supporting Source IDs | Notes |
|---|---|---|---|---|
| S1 | SDMA belongs in the current endpoint map as an adjunctive support marker for earlier recognition and staging | B | src-ckd-004, src-ckd-024 | guideline plus biomarker-review support |
| S2 | SDMA should currently sit below serial creatinine interpretation plus USG, not above them | B | src-ckd-004, src-ckd-024 | current practical core still dominates |
| S3 | The strongest single innovation signal in the metabolomics study was S/U 3-hydroxykynurenine, not SDMA | B | src-ckd-018 | AUC 0.844, accuracy 0.804 |
| S4 | The strongest predictive story in `src-ckd-018` is panel-based modelling, not single-marker replacement | B | src-ckd-018 | linear SVM AUC 0.929, accuracy 0.862 at T-6 |
| S5 | `src-ckd-018` weakens any strong SDMA-as-shortcut story | B | src-ckd-018 | SDMA ranked 14th at T-6, poor individual sensitivity |
| S6 | Current frontier promise should be written as panel augmentation of serial surveillance, not routine workflow replacement | B | src-ckd-004, src-ckd-018, src-ckd-024 | cross-source bounded synthesis |

## What SDMA Now Clearly Is

### Current best position

- an adjunctive biomarker
- a support marker for earlier recognition and staging
- especially useful when muscle loss may distort creatinine interpretation
- a useful antidote to a creatinine-only mindset

### What moved this forward

- `src-ckd-004` gave the strongest current guideline wording:
  - SDMA appears more sensitive than creatinine for early CKD detection
  - SDMA is not currently recommended as a single screening test
  - SDMA may support diagnosis or staging, especially with marked muscle loss
- `src-ckd-024` reinforced SDMA as a meaningful GFR-related biomarker, while preserving specificity caution

Net effect:

- the current vault no longer needs to hedge on whether SDMA matters at all
- the unresolved question is now weighting, not relevance

## What SDMA Is Not

- not a creatinine replacement
- not a USG replacement
- not a one-test screening shortcut
- not the strongest individual innovation signal in the newest frontier paper
- not a solved marker-positioning branch in routine feline workflows

## What `src-ckd-018` Changed

### 1. It created a real early-detection frontier branch

This paper is stronger than a simple discovery metabolomics paper because it combines baseline separation with independent longitudinal validation.

Important details:

- baseline population: 61 healthy cats, 63 CKD2 cats
- longitudinal population: 26 cats remaining healthy, 22 cats developing CKD2 within one year
- discrimination claimed up to six months before traditional CKD2 diagnosis

### 2. It separated single-marker and panel logic

The paper should not be summarized as “a better SDMA paper.”

It actually says two different things:

- the best individual candidate in this dataset was S/U 3-hydroxykynurenine
- the strongest predictive performance came from multivariate modelling combining metabolites and clinical parameters

Important details:

- S/U 3-hydroxykynurenine: AUC 0.844, accuracy 0.804
- linear SVM plus metabolites and clinical parameters at T-6: AUC 0.929, accuracy 0.862

### 3. It made SDMA-overpromotion harder to defend

This is one of the strongest current vault sources against flattening the early-detection problem into SDMA alone.

Important details:

- SDMA ranked only 14th as an individual metabolite at T-6
- poor individual SDMA sensitivity values were reported

Net effect:

- SDMA remains relevant
- SDMA-alone overpromotion becomes less defensible

## Why This Frontier Still Stays Bounded

### Main limits

- only CKD2 cats were included
- some T-6 cats may already have had CKD1
- no GFR
- no renal ultrasonography
- metabolomics-heavy assay path
- limited sample size relative to routine-clinic deployment ambitions

### What this means

- this paper strengthens innovation logic
- it does not justify a routine workflow rewrite
- it does not solve true earliest-stage adjudication
- it does not justify machine-learning-as-clinic-program language

## Current Working Hierarchy

| Branch | Current Role In Vault | Why |
|---|---|---|
| Serial surveillance in older/high-risk cats | operational backbone | strongest practical support in current corpus |
| Creatinine trend plus USG | practical core | still central for routine interpretation |
| SDMA | adjunctive support marker | relevant, but bounded and not standalone |
| Proteinuria / UPCR context | contextual support | adds clinically meaningful renal abnormality framing |
| Blood pressure context | comorbidity and progression support | part of recognition and management context |
| Single metabolomic marker | frontier innovation signal | promising, but not routine-ready |
| Multi-marker ML panel | strongest innovation frontier | augmentation logic stronger than replacement logic |

## What The Vault Can Now Say More Clearly

1. SDMA is no longer a speculative side branch in this vault.
2. SDMA still belongs inside a serial and multi-marker interpretation frame.
3. The best current early-detection frontier signal is panel-based, not one-marker-based.
4. The newest frontier paper strengthens innovation and weakens shortcut rhetoric at the same time.
5. The right contrast is now:
   `serial surveillance backbone + adjunctive SDMA + future panel augmentation`
   not
   `old markers replaced by one better test`

## What We Should Not Overstate

- that SDMA is the best single early CKD marker in routine practice
- that machine-learning performance in `src-ckd-018` is already clinic-ready
- that metabolomic performance in CKD2 prediction solves CKD1 or true earliest-disease detection
- that the vault now has enough evidence to produce a final biomarker ranking

## Best Reuse Targets

- [sdma positioning](../../topics/ckd/sdma-positioning.md)
- [early detection](../../topics/ckd/early-detection.md)
- [endpoint handbook](../../topics/ckd/endpoint-handbook.md)
- [synthesis index](../../topics/ckd/synthesis-index.md)
- [SDMA entity card](../../entities/endpoints/sdma.md)
