---
id: src-ckd-030-deep-extraction-round1
type: system
topic: ckd
question_type: deep-extraction
source_ids: [src-ckd-030]
language: zh
last_compiled_at: 2026-06-06
verification_status: deep_extracted
decision_grade: no
owner: codex
status: active
---

# src-ckd-030 Deep Extraction, Round 1

Source: `src-ckd-030`  
Access method: complete open publisher HTML  
Role: feasibility and mechanism-generating probiotic pilot, not treatment efficacy proof

## Phase 0: Sequential Micro-Analysis

### Unit 1: This is a single-arm pilot with severe attrition

- core_claim: cats with stage 2 or 3 CKD received Lactobacillus-mixture treats daily for eight weeks.
- hard_details: `12` cats enrolled; `6` completed; `6` dropped out; one completer had stage 2 and five had stage 3 CKD.
- design_boundary: no concurrent control group, no randomization, no blinding, and a `50%` dropout rate.

### Unit 2: The intervention is strain- and formulation-specific

- core_claim: the treats contained two selected strains, `Lacticaseibacillus paracasei MFM 18` and `Lactiplantibacillus plantarum MFM 30-3`.
- hard_details: approximately `2.79-3.93 x 10^8 CFU/cat/day`; cats retained their usual CKD treatment and diet.
- design_boundary: results cannot be generalized to probiotics, synbiotics, or commercial renal supplements as a class.

### Unit 3: Creatinine movement is suggestive, not confirmatory

- core_claim: creatinine shifted lower after eight weeks and decreased in all six completers.
- hard_details: reported `p = 0.06`; the authors emphasized 90% confidence intervals; one cat changed from stage 3 to stage 2.
- design_boundary: regression to the mean, hydration, concurrent care, diet, and ordinary biological variation cannot be separated from treatment effect.

### Unit 4: Uremic-toxin endpoints were not statistically significant

- core_claim: plasma TMAO, indoxyl sulfate, p-cresyl sulfate, and phenyl sulfate did not differ significantly after treatment.
- hard_details: all toxin comparisons reported `p > 0.05`; the authors interpreted 90% confidence intervals as a possible indoxyl-sulfate signal.
- design_boundary: this study does not demonstrate toxin lowering.

### Unit 5: Microbiome changes are exploratory

- core_claim: alpha diversity increased and several taxa or predicted pathways changed after treatment.
- hard_details: full-length 16S sequencing; PICRUSt-predicted metabolic functions; six paired completer samples.
- design_boundary: predicted microbial function is not direct functional measurement, and taxonomic change does not establish clinical benefit.

### Unit 6: Some signals cut against a simple benefit narrative

- core_claim: serum phosphate significantly increased after treatment.
- hard_details: phosphate was the biochemical parameter explicitly reported as significantly elevated.
- design_boundary: any future efficacy study must prespecify mineral monitoring and cannot summarize this pilot as uniformly kidney-protective.

### Unit 7: Quality-of-life observations are unblinded owner reports

- core_claim: four of six owners reported better appetite and all six reported improved or maintained activity.
- design_boundary: no validated blinded comparator was used, and cats whose treat palatability contributed to dropout were absent from completer outcomes.

### Unit 8: The authors acknowledge the need for a stronger trial

- core_claim: the paper identifies small sample size, single-group design, short duration, and uncontrolled diet or medication as limitations.
- design_boundary: the appropriate next step is a larger randomized placebo-controlled study, not clinical adoption.

## Phase 1: Theme Reconstruction

## Theme: Feasibility is the strongest safe conclusion

The study shows that paired kidney, toxin, microbiome, and owner-reported endpoints can be collected around an eight-week probiotic-treat intervention. It does not establish efficacy because only six cats completed and there was no control group.

## Theme: Mechanistic coherence is weaker than the title implies

The microbiome changed, but toxin concentrations were not significantly reduced. The intervention-to-microbiome-to-toxin-to-kidney chain therefore remains a hypothesis rather than a demonstrated mechanism.

## Theme: Attrition and phosphate movement are branch-control facts

Half the enrolled cats did not complete, including palatability-related dropout, and serum phosphate increased. These findings must remain visible whenever this source is discussed.

## Phase 2: Claim-Evidence Structure

### Feasibility

**Claim 1**
- support: six cats completed paired clinical, toxin, and microbiome measurements.
- safe use: inform future trial design and endpoint selection.
- unsafe use: claim treatment efficacy.

### Uremic-Toxin Intervention

**Claim 2**
- support: toxin assays were performed, but TMAO, IS, PCS, and PS changes were not statistically significant.
- safe use: classify this as an unconfirmed intervention hypothesis.
- unsafe use: say the treats lowered uremic toxins.

### Safety and Monitoring

**Claim 3**
- support: serum phosphate increased and half the enrolled cats dropped out.
- safe use: require mineral, adherence, and attrition monitoring in future trials.
- unsafe use: describe the intervention as broadly safe or well tolerated.

## Phase 3: Promotion Check

- source_card_updates:
  - replace title-led efficacy language with pilot design, attrition, nonsignificant toxin endpoints, and phosphate increase
  - mark full open-HTML review
- topic_write_back_targets:
  - none at reader-facing level
  - `system/indexes/ckd-uremic-toxin-microbiome-bridge-memo-20260606.md`
- not_safe_to_promote_yet:
  - probiotic efficacy
  - uremic-toxin reduction
  - CKD stage improvement
  - class-level probiotic or product recommendations
- conflicts_with_existing_vault:
  - title and simple-summary wording are materially stronger than the controlled evidence allows
- new_entities_or_pages_justified:
  - no treatment page; only a research-design boundary memo
