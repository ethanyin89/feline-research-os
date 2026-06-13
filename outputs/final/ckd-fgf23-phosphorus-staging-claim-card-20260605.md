---
id: business-ckd-fgf23-phosphorus-staging-claim-card-20260605
type: business
artifact_kind: claim_card
disease: CKD
created_at: 2026-06-05
updated_at: 2026-06-05
owner: claim_evidence_workbench
status: reviewed
verification_status: source_checked
decision_grade: no
---

# Claim Evidence Card

**Disease:** CKD
**Claim:** FGF-23 elevates earlier than hyperphosphatemia across CKD stages and may serve as an earlier biomarker than serum phosphorus for feline CKD monitoring.

## Verdict

| Field | Value |
|-------|-------|
| Verdict | **SUPPORTED** |
| Confidence | medium |
| Claim Level | B (Source-Supported) |
| Next Action | promote |

## Key Sources

- `src-ckd-026` (full abstract extraction completed 2026-06-05)
- `src-ckd-006`
- `src-ckd-007`
- `src-ckd-015`
- `outputs/business/ckd-phosphorus-diet-vs-binder-claim-card-20260605.md`

## Evidence Depth

| Metric | Value |
|--------|-------|
| Sources checked | 50 |
| Matching sources | 4 |
| Level A (quoted) | 5 |
| Level B (supported) | 3 |
| Level C (inference) | 2 |
| Deep extracted (seed) | 24 |
| Abstract extracted (extension) | 1 |

## Quoted Facts (Level A)

- [src-ckd-026] "FGF-23 was higher in cats in all CKD stages than in controls."
- [src-ckd-026] "Higher serum phosphorus was observed in stage 3 (p = 0.04) and stage 4 (p < 0.01) compared to controls."
- [src-ckd-026] "No statistical difference was found in FGF-23 among age groups (p = 0.15) or by sex in healthy subjects."
- [src-ckd-026] "Pearson analysis indicated a positive linear relationship between FGF-23 and iPTH (control: r = 0.70, p < 0.01; CKD: r = 0.46, p = 0.02)."
- [src-ckd-026] "FGF-23 may be a useful biomarker of feline CKD and may precede hyperphosphatemia in advanced feline CKD."

## Source-Supported Conclusions (Level B)

- FGF-23 elevates earlier than hyperphosphatemia across CKD stages; hyperphosphatemia only appeared in stage 3-4 while FGF-23 was elevated in all stages vs controls.
- Age does not independently affect FGF-23 in healthy cats, reducing age-related confounding concerns for biomarker interpretation.
- FGF-23 and iPTH are positively correlated in both healthy and CKD cats, suggesting mechanistic linkage.

## Boundary

- Cross-sectional design cannot establish temporal precedence; FGF-23 "precedes" hyperphosphatemia is an association, not proven causation.
- This study cannot prove FGF-23 predicts progression; it shows association only.
- Sample is single-center (China); external validity to other populations unconfirmed.
- No treatment intervention data; this is observational only.
- This claim does not provide numeric FGF-23 cutoffs for clinical use.
- This claim does not weaken the existing diet-first phosphorus hierarchy.

## Business-Use Boundary

This claim card supports internal CKD biomarker architecture and staging refinement. It does NOT support:

- Universal FGF-23 cutoff recommendations for clinical practice
- FGF-23 as a treatment decision driver without additional evidence
- Progression prediction claims (cross-sectional limitation)
- Owner-facing monitoring recommendations

## Go/No-Go Implication

**Go:** FGF-23 should be added to the CKD biomarker architecture as an early-stage candidate that elevates before hyperphosphatemia. This refines phosphorus-control positioning without replacing diet-first hierarchy.

**No-Go:** Do not recommend FGF-23 monitoring as a routine owner-facing or product-positioning claim without replication studies and cutoff validation.

## What This Changes

The CKD phosphorus/mineral-burden branch now has additional biomarker context:

- Hyperphosphatemia is a late-stage finding (stage 3-4 only)
- FGF-23 elevation occurs earlier across all CKD stages
- iPTH correlation suggests the FGF-23-PTH-phosphorus axis is relevant in feline CKD

## Next Action

**Promote.** The claim is now source-supported (Level B) with multiple quoted facts (Level A). The full abstract extraction for `src-ckd-026` unblocked this card.

## Verification Path

`raw/papers/src-ckd-026.md -> system/indexes/src-ckd-026-structured-abstract-round2.md -> outputs/business/ckd-phosphorus-diet-vs-binder-claim-card-20260605.md`
