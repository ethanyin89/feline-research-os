# Deep Extraction Worksheet

Source: `src-fcv-010`  
Title: `Neutralizing Feature of Commercially Available Feline Calicivirus (FCV) Vaccine Immune Sera against FCV Field Isolates`  
Method note: this worksheet is based on the J-STAGE abstract and limited open full-text sampling rather than a full section-by-section extraction of the complete paper.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: This paper is an early field-fit stress test, not a final vaccine answer

- core_claim: the study compares four commercial FCV vaccines by testing immune sera against both laboratory strains and field isolates.
- implicit_premise: vaccine-breadth language gets distorted if it only uses laboratory strains.
- relation_to_previous: opening role assignment.
- hard_details: the abstract explicitly reports four commercial vaccines, SPF cats, two immunizations, and neutralization testing against field isolates.
- tension_or_surprise: the paper matters because it operationalizes `variant problem` into actual failure-to-neutralize counts.

#### Unit 2: Laboratory-strain performance looks cleaner than field-isolate coverage

- core_claim: all vaccine sera neutralized laboratory strains relatively well, but field-isolate performance dropped substantially.
- implicit_premise: laboratory readouts can flatter vaccine breadth.
- relation_to_previous: sharpens the endpoint warning.
- hard_details: strains `F4`, `F9`, and `255` were neutralized relatively well, while many field isolates were not.
- tension_or_surprise: the strongest anti-overclaim message in the paper is the gap between lab strains and field isolates.

#### Unit 3: Product-level variability is real inside the same country dataset

- core_claim: the four vaccines did not perform equivalently against the 36 field isolates.
- implicit_premise: FCV breadth should not be written as one monolithic class property.
- relation_to_previous: adds internal differentiation.
- hard_details: vaccine A failed on `18-20` isolates, B on `19-22`, C on `22-25`, and D on `8-16`.
- tension_or_surprise: even in an old study, the spread across products is too large to ignore.

#### Unit 4: Some field isolates escaped everything in the dataset

- core_claim: a subset of isolates were not neutralized by any immune serum.
- implicit_premise: `partial coverage` is not just a small decrement from perfect breadth.
- relation_to_previous: sets the ceiling on vaccine-breadth rhetoric.
- hard_details: the full text reports `8` field isolates escaped all tested immune sera.
- tension_or_surprise: this is the sentence that stops soft wording from becoming misleading.

#### Unit 5: This source should anchor the historical field-fit warning beneath newer breadth papers

- core_claim: `src-fcv-010` should become the historical stress-test anchor in the FCV vaccine-breadth branch.
- implicit_premise: later, stronger breadth papers still benefit from an older paper that shows the problem in raw form.
- relation_to_previous: assigns durable module role.
- hard_details: this card pairs naturally with `src-fcv-003` for later breadth framing and `src-fcv-011` for challenge protection.
- tension_or_surprise: the right use is not `old data proves current failure`, but `field-fit instability has deep roots and should stay explicit`.

## Phase 1: Theme Reconstruction

## Theme: FCV breadth looks much weaker once field isolates replace laboratory strains

This paper upgrades the vaccine-breadth warning from a vague caveat into a concrete historical pattern. It supports saying that field-fit stress testing matters because laboratory-strain neutralization can materially overstate coverage.

### Hard Information

- four commercial vaccines tested
- laboratory strains `F4`, `F9`, and `255` neutralized relatively well
- many field isolates not neutralized

## Theme: Field-isolate coverage varies across products

The paper is useful not only because coverage was incomplete, but because incompleteness varied across the vaccines.

### Hard Information

- vaccine A failed on `18-20` field isolates
- vaccine B failed on `19-22`
- vaccine C failed on `22-25`
- vaccine D failed on `8-16`

## Theme: Some isolates escape the whole tested serum set

The ceiling of the paper is not `coverage was imperfect` but `some isolates escaped all tested sera`.

### Hard Information

- `8` field isolates not neutralized by any immune serum

## Phase 2: Claim-Evidence Structure

### Breadth-Boundary Key Points

**Claim 1**
- support: all immune sera neutralized laboratory strains relatively well, but field-isolate failure counts were much higher
- details: lab strains versus 36 field isolates
- implicit_premise: FCV breadth needs field-fit pressure tests, not just laboratory confirmation

**Claim 2**
- support: failure counts varied across vaccines A-D
- details: broad product spread in field-isolate non-neutralization
- implicit_premise: vaccine breadth should not be written as one flat class property

**Claim 3**
- support: eight field isolates were not neutralized by any immune serum
- details: universal escape inside this dataset
- implicit_premise: partial coverage can be structurally meaningful, not cosmetic

### Boundary-Setting Key Points

**Claim 1**
- support: this is a 1999 Japanese in vitro neutralization dataset
- details: country- and time-bounded historical field-fit signal
- implicit_premise: do not use this as present-day global performance truth

**Claim 2**
- support: neutralization failure counts are not clinical outcomes
- details: sera and isolates, not field disease endpoints
- implicit_premise: do not convert breadth gaps directly into clinical efficacy ranking

## Phase 2.5: Write-Back Implications

### For `topics/fcv/endpoint-handbook.md`

- this becomes a deep-extracted early stress-test anchor beneath the broader `breadth but incomplete` endpoint wording

### For `system/indexes/fcv-vaccine-persistence-boundary-memo.md`

- this source can now carry more of the `lab strains cleaner than field isolates` language directly

### For `topics/fcv/current-state-dashboard.md`

- the vaccine breadth row can now mention an older deep-extracted field-fit stress-test anchor, not only newer breadth and persistence anchors

### For `system/indexes/fcv-source-depth-map.md`

- `src-fcv-010` should move from partial/source_checked into full/deep_extracted

## Phase 3: Promotion Check

- source_card_updates:
  - preserve field-fit stress-test authority
  - preserve product-variability signal
  - preserve anti-current-performance and anti-clinical-overclaim boundaries
- topic_write_back_targets:
  - `topics/fcv/endpoint-handbook.md`
  - `system/indexes/fcv-vaccine-persistence-boundary-memo.md`
  - `topics/fcv/current-state-dashboard.md`
  - `system/indexes/fcv-source-depth-map.md`
- not_safe_to_promote_yet:
  - any current-market ranking claim
  - any global present-day vaccine-performance conclusion
  - any direct conversion from neutralization failure counts to clinical failure
- conflicts_with_existing_vault:
  - none; this worksheet gives the FCV branch a stronger early field-fit warning anchor
