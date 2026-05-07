---
id: system-fip-diagnostic-workup-memo
type: system
topic: fip
last_compiled_at: 2026-04-21
owner: codex
status: active
language: en
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
---

# FIP Diagnostic-Workup Memo

- Date: `2026-04-09`
- Scope: `src-fip-003`, `src-fip-006`, `src-fip-010`, `src-fip-015`, `src-fip-022`, `src-fip-023`

This memo is here to stop the FIP module from drifting into one-test thinking.

It does four narrower things:

1. separate suspicion, support, and overclaim
2. clarify where clinicopathology belongs
3. bound mutation-based diagnostic logic
4. make neurologic-workup complexity explicit

## Core Position

1. FIP diagnosis in the current vault is best modeled as a composite-support problem, not a definitive single-test problem.
2. Clinicopathology is one of the most operationally useful branches in suspicion-building.
3. Mutation-testing belongs in the workup, but not as a clean certainty engine.
4. Neurologic FIP adds a second diagnostic layer rather than just a more severe version of the same workup.
5. Mechanism evidence should shape how the workup is interpreted, but should not outrank clinicopathologic suspicion.

## Why FIP Workup Needs Its Own Memo

The current module already has a strong treatment branch.
That creates a risk:

once treatment gets interesting, diagnosis can be rewritten too casually.

This memo exists to block that drift.

## Current Working Architecture

### Layer 1: Clinical Suspicion

This is where the workup starts:

- disease form suspicion
- clinicopathologic pattern recognition
- exposure and risk context

In the current vault, this layer is mainly carried by:

- `src-fip-003`
- `src-fip-006`
- `src-fip-015`

### Layer 2: Supportive Diagnostic Strengthening

This is where additional evidence accumulates:

- fluid / laboratory patterns
- mutation-related assays
- CNS-specific sample logic in neurologic disease

This layer is currently carried by:

- `src-fip-010`
- `src-fip-022`
- `src-fip-023`

### Layer 3: Overclaim Boundary

This is the part the module most needs to defend:

- mutation-origin does not equal mutation-test certainty
- one positive molecular signal does not automatically collapse the whole disease question
- neurologic workup is not interchangeable with general FIP workup
- mechanism-level elegance does not remove the need for composite-support diagnosis

## Current Diagnostic Branches

### Branch 1: Clinicopathology

What current sources support:

- clinicopathology is central to FIP recognition
- staged and form-aware disease description matters
- suspicion architecture should not begin with molecular assays alone
- the larger Taiwan case-series anchor strengthens staged disease-form recognition as a reusable operational layer

What the vault can say safely:

- clinicopathology is one of the strongest operational layers in the current FIP workup

What the vault should not say:

- do not pretend clinicopathology alone is definitive diagnosis

### Branch 2: Mutation-Based Diagnostic Logic

What current sources support:

- mutation-related testing is relevant to FIP workup
- later literature explicitly warns about limitations
- mutation-origin mechanism papers and mutation-based diagnosis papers are not the same type of evidence
- the limitation branch now has a real deep-extracted caution anchor rather than only a title-level placeholder
- utility (`src-fip-022`) and limitation (`src-fip-010`) must be read as a paired diagnostic-support branch, not as winner-take-all evidence

What the vault can say safely:

- mutation testing belongs in the workup as a bounded supportive branch
- mutation testing should strengthen an already suspicious case rather than lead the workup

What the vault should not say:

- do not write mutation testing as a universal certainty shortcut
- do not let mutation-origin papers substitute for mutation-diagnostic utility papers

### Branch 3: Neurologic FIP Diagnostic Extension

What current sources support:

- neurologic FIP can require CNS-specific diagnostic material
- CSF-based detection belongs to a distinct extension of the workup
- neurologic disease should be treated as a separate complexity layer
- CSF RT-PCR can strongly support diagnosis in the neurologic/ocular branch, but is too insensitive overall to lead ordinary FIP workup
- `src-fip-023` reports specificity `100%`, PPV `100%`, overall sensitivity `42.1%`, NPV `57.7%`, and neurologic/ocular subgroup sensitivity `85.7%`

What the vault can say safely:

- neurologic FIP adds a specialized diagnostic branch beyond general suspicion-building
- positive CSF viral detection can be highly strengthening in the neurologic branch
- negative CSF viral detection should not be used as broad FIP exclusion

What the vault should not say:

- do not treat neurologic diagnostic logic as interchangeable with ordinary FIP workup
- do not let neurologic-branch specificity be misread as broad negative-excluding power

## Current Working Hierarchy

| Workup Branch | Current Position In Vault | Notes |
|---|---|---|
| Clinicopathology and disease-form suspicion | strongest current operational branch | carried by case-series and broad-review logic |
| Composite-support diagnosis | core framing rule | reinforced by modern broad review |
| Mutation-based diagnostic logic | useful but overclaim-sensitive | must stay below certainty language |
| Neurologic / CSF extension | specialized high-complexity branch | separate from generic workup |

## What This Branch Is Not Allowed To Become

- It is not allowed to become a one-assay diagnosis story.
- It is not allowed to import mechanism-origin language directly into clinical certainty claims.
- It is not allowed to flatten neurologic FIP into standard suspicion logic.
- It is not allowed to let treatment availability weaken diagnostic discipline.

## What The Vault Can Now Say More Clearly

1. FIP workup is composite by structure, not because the field has simply failed to find the best one test.
2. Clinicopathology belongs near the center of operational suspicion-building.
3. Mutation-based assays are relevant but bounded.
4. Neurologic FIP should be treated as a workup extension branch with its own complexity.

## Best Reuse Targets

- [risk and recognition](../../topics/fip/risk-and-recognition.md)
- [FIP mechanism-diagnostic bridge memo](fip-mechanism-diagnostic-bridge-memo.md)
- [FIP neurologic recognition memo](fip-neurologic-recognition-memo.md)
- [translation brief](../../topics/fip/translation-brief.md)
- [current state dashboard](../../topics/fip/current-state-dashboard.md)
- [synthesis index](../../topics/fip/synthesis-index.md)
