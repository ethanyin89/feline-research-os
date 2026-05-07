---
id: topic-fip-recognition-architecture
type: topic
topic: fip
species: feline
disease: FIP
question_type: recognition
source_ids: [src-fip-002, src-fip-003, src-fip-005, src-fip-006, src-fip-008, src-fip-010, src-fip-011, src-fip-012, src-fip-015, src-fip-020, src-fip-022, src-fip-023]
last_compiled_at: 2026-04-23
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
language_qa_notes: "2026-04-23 checked for support-order and assay-placement drift; page remains a compiled architecture guide."
owner: codex
status: active
---

# Feline FIP Recognition Architecture

## Question This Page Answers

How should FIP recognition be structured before the module drifts into one-test thinking or one-case-form thinking?

## Core Position

Recognition in FIP should be modeled in three layers:

1. `who is at risk`
2. `what pattern raises suspicion`
3. `what additional branch is needed for neurologic complexity`

## Layer 1: Risk Context

This layer includes:

- multi-cat environment logic
- endemic coronavirus exposure context
- young-age signal
- patterned breed or population-structure signal
- male over-representation signal
- referral / hospital epidemiology context

This layer answers:

`who should make you worry earlier`

This layer should now be read more concretely:

- young age is one of the strongest current early-risk levers
- breed signal is patterned, not just `pedigree cats`
- sex signal matters, but should stay below age and ecology
- referral / hospital context can enrich burden without standing in for community prevalence

## Layer 2: Suspicion Pattern

This layer includes:

- clinicopathologic pattern recognition
- effusive versus non-effusive disease-form suspicion
- staged and form-aware description

This layer answers:

`what constellation looks like FIP enough to build composite support`

This layer should now be read more concretely:

- clinicopathology should lead the suspicion-pattern branch
- smaller practical case-pattern series and larger structured staging series can cooperate
- effusion is one of the cleanest early disease-form triggers inside suspicion-pattern recognition
- suspicion pattern comes before bounded molecular strengthening
- lower laboratory context belongs beneath this layer rather than beside it

## Layer 3: Neurologic Extension

This layer includes:

- neurologic-sign context
- CSF-based diagnostic extension
- separation from generic workup logic

This layer answers:

`when does the workup have to become a different branch`

This layer should now be read more concretely:

- neurologic signs should trigger branch shift before specialized support testing
- CSF-based support becomes meaningful after the branch has shifted
- neurologic complexity should not be flattened into ordinary suspicion plus one extra test
- the real control point is now clearer as a branch-boundary rule, not just as a reminder that CSF is specialized
- the current CSF evidence supports strong positive neurologic/ocular branch strengthening, but not broad negative exclusion or ordinary-workup leadership

## What This Architecture Prevents

- it prevents risk from being mistaken for diagnosis
- it prevents clinicopathology from being mistaken for certainty
- it prevents neurologic disease from being treated as just “more severe ordinary FIP”
- it prevents one assay from swallowing the recognition layer

## Assay Placement Boundary

This architecture should not be read as an assay-performance ranking.

The current recognition layer can place support channels more safely than it can rank them:

- acute-phase / immunoglobulin markers and older serology stay below suspicion pattern as background support
- mutation-related assays strengthen an already suspicious case, while carrying their limitation branch
- CSF viral detection belongs after neurologic / ocular branch shift and should not lead ordinary recognition

For numeric CSF boundaries and the reason non-CSF branches should not be forced into a leaderboard, use [endpoint handbook](endpoint-handbook.md) and [FIP assay-performance boundary memo](../../system/indexes/fip-assay-performance-boundary-memo.md).

## Best Linked Pages

- [risk and recognition](risk-and-recognition.md)
- [endpoint handbook](endpoint-handbook.md)
- [FIP risk epidemiology memo](../../system/indexes/fip-risk-epidemiology-memo.md)
- [FIP clinicopathology memo](../../system/indexes/fip-clinicopathology-memo.md)
- [FIP effusion recognition memo](../../system/indexes/fip-effusion-recognition-memo.md)
- [FIP neurologic recognition memo](../../system/indexes/fip-neurologic-recognition-memo.md)
- [FIP neurologic-workup branch-boundary memo](../../system/indexes/fip-neurologic-workup-branch-boundary-memo.md)
- [FIP diagnostic-workup memo](../../system/indexes/fip-diagnostic-workup-memo.md)
- [FIP support-order memo](../../system/indexes/fip-support-order-memo.md)
- [FIP assay-performance boundary memo](../../system/indexes/fip-assay-performance-boundary-memo.md)
- [FIP mutation-diagnostics boundary memo](../../system/indexes/fip-mutation-diagnostics-boundary-memo.md)
