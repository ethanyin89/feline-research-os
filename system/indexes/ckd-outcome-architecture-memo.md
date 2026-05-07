---
id: system-ckd-outcome-architecture-memo
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

# CKD Outcome Architecture Memo

- Date: `2026-04-09`
- Scope: `src-ckd-013`, `src-ckd-003`, `src-ckd-004`, `src-ckd-006`, `src-ckd-009`, `src-ckd-010`

This memo exists to separate two questions that are easy to collapse:

1. what should be monitored in routine feline CKD workup and follow-up
2. what should be captured in a feline CKD treatment-trial outcome architecture

In the current vault, those are related but not identical problems.

## Core Position

1. Routine operational endpoints should stay relatively compact.
2. Trial-grade treatment evaluation should be broader than the routine endpoint shortlist.
3. A strong CKD outcome architecture has to include both disease-course and patient-level burden.
4. The current vault is now strong enough to distinguish `routine endpoint logic` from `trial-outcome logic` without pretending they are the same layer.

## Key-Claim Traceability

| Claim ID | Key Claim | Claim Level | Supporting Source IDs | Notes |
|---|---|---|---|---|
| OA1 | Routine feline CKD workup should center on a compact operational endpoint shortlist rather than a maximal marker set | B | src-ckd-004, src-ckd-006, src-ckd-009, src-ckd-010 | compiled endpoint-layer judgment |
| OA2 | Feline CKD treatment trials should include broader outcomes than laboratory and hemodynamic markers alone | B | src-ckd-013 | direct trial-design signal |
| OA3 | Quality of life, food intake, progression, survival time, and cause of death belong in trial-outcome logic even when they are not first-wave routine endpoints | B | src-ckd-013, src-ckd-003 | consensus plus treatment-context support |
| OA4 | Supportive-care branches matter partly because they affect burden and stability outcomes that sit more naturally in a broad treatment-outcome frame | B | src-ckd-003, ckd-supportive-care-evidence-memo | compiled cross-layer judgment |
| OA5 | Operational endpoints and trial outcomes should be linked, but not collapsed into one list | B | src-ckd-013, src-ckd-004 | the central architecture boundary |
| OA6 | The core outcome set defines minimum breadth, not a universal outcome-priority order across all intervention classes | B | src-ckd-013 | important boundary against overreading the consensus paper |
| OA7 | Pathology-linked endpoints should not be treated as one flat severity scale because different markers map to different structural-consequence patterns | B | src-ckd-010 | endpoint consequence mapping, not just endpoint importance |
| OA8 | Frontier early-detection signal should not be confused with routine endpoint readiness | B | src-ckd-018 | strongest support is for panel augmentation, not workflow replacement |

## Layer 1: Routine Operational Endpoints

This is the layer for:

- diagnosis
- staging
- follow-up
- practical treatment monitoring

Current operational core:

- creatinine
- USG
- UPCR / proteinuria
- systolic blood pressure
- phosphorus
- SDMA

Why this layer stays compact:

- it has to work in real clinical workflow
- it should privilege interpretability and repeated usability
- it should not become a maximal research list

## Layer 2: Context And Burden Endpoints

This layer matters when the question is no longer only “is CKD present and how severe is it?”

This includes:

- potassium
- anaemia
- PTH
- calcium / hypercalcaemia context
- FGF23
- appetite and GI burden

Why this layer matters:

- it sharpens interpretation
- it changes treatment context
- it captures complication burden

Why it should not be flattened into Layer 1:

- many of these variables are clinically important without being default first-wave endpoints

## Layer 3: Trial-Outcome Architecture

This is where `src-ckd-013` matters most.

The current vault can now say clearly that treatment trials should not rely only on:

- chemistry
- urinalysis
- blood pressure

They should also cover:

- quality of life
- food intake
- progression
- survival time
- cause of death

This is broader by design.

That is not a weakness.
It is the point of a treatment-trial outcome architecture.

What `src-ckd-013` does not do:

- it does not say every intervention class should weight every outcome equally
- it does not replace the compact operational shortlist used in routine workflow
- it does not itself rank the most decisive outcome for every treatment class

## Why The Distinction Matters

If the vault collapses routine endpoints and trial outcomes into one list, two errors appear:

- routine care starts to look unrealistically maximal
- treatment-trial design starts to look too narrow and lab-centered

The current architecture should instead be read as:

- `routine endpoints` for practical CKD workflow
- `context endpoints` for burden, mechanism, and treatment interpretation
- `trial outcomes` for broader efficacy and patient-level consequence

## What The Current Sources Actually Support

### Stronger Support

- routine endpoint logic should stay compact
- trial outcomes should be broader than lab markers alone
- quality-of-life and food-intake signals belong in treatment-evaluation thinking
- progression and survival belong in the same trial-design frame
- endpoint movement can carry different structural meanings rather than one generic “worse kidney” signal

### Bounded Support

- the core outcome set does not mean every intervention requires every outcome at identical priority
- not every context endpoint belongs in every trial
- not every routine endpoint is equally decisive for every intervention class
- minimum architecture and intervention-specific priority should remain separated
- frontier outcome signal and routine-readiness signal should remain separated

## Current Working Architecture

| Layer | Main Purpose | Best Current Examples | Main Risk If Misused |
|---|---|---|---|
| Routine endpoints | diagnosis, staging, monitoring | creatinine, USG, UPCR, SBP, phosphorus, SDMA | becoming too narrow for treatment evaluation |
| Context endpoints | burden, mechanism, treatment interpretation | potassium, anaemia, PTH, calcium, FGF23 | being either ignored or wrongly promoted into default routine status |
| Trial outcomes | efficacy, patient-level consequence, disease-course evaluation | QoL, food intake, progression, survival time, cause of death | being reduced to lab-only readouts |

## What This Branch Is Not Allowed To Become

- It is not allowed to become “the routine endpoint list is the trial-outcome list.”
- It is not allowed to treat quality of life and food intake as soft optional extras in every treatment study.
- It is not allowed to turn every context endpoint into a mandatory first-wave operational marker.
- It is not allowed to pretend broad trial architecture makes everyday clinic workflow equally broad.

## What The Vault Can Now Say More Clearly

1. Routine endpoint architecture and trial-outcome architecture are different layers.
2. Both layers matter, and both should remain visible.
3. Supportive-care branches become easier to understand once broader burden outcomes are kept in view.
4. `src-ckd-013` is best read as defining minimum breadth, not exact per-intervention priority.
5. `src-ckd-010` helps explain why endpoint movement should be read as multi-axis structural consequence, not one flat severity ladder.
6. `src-ckd-018` helps explain why an early-detection frontier signal is not the same thing as a routine-ready endpoint package.
7. The current vault no longer has to carry this distinction only through scattered paragraphs in endpoint and translation pages.

## Best Reuse Targets

- [translation brief](../../topics/ckd/translation-brief.md)
- [endpoint handbook](../../topics/ckd/endpoint-handbook.md)
- [CKD supportive-care evidence memo](ckd-supportive-care-evidence-memo.md)
- [current state dashboard](../../topics/ckd/current-state-dashboard.md)
