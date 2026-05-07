---
id: system-fip-endpoint-diagnostic-bridge-memo
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

# FIP Endpoint-Diagnostic Bridge Memo

- Date: `2026-04-09`
- Scope: `src-fip-002`, `src-fip-003`, `src-fip-006`, `src-fip-010`, `src-fip-011`, `src-fip-015`, `src-fip-022`, `src-fip-023`

This memo exists to answer a narrower question than the endpoint handbook or the diagnostic-workup memo:

`how do the main endpoint channels actually cooperate when FIP workup moves from suspicion to stronger support?`

## Core Position

1. In FIP, endpoint logic is not separate from diagnostic logic.
2. The current vault supports a bridge architecture with three layers:
   - clinicopathologic suspicion
   - bounded molecular strengthening
   - specialized neurologic extension
3. The error to avoid is not only `single-marker certainty`.
4. The second error is `marker flattening`, where all support channels are treated as interchangeable.
5. CSF viral detection becomes useful after the branch shift, not before it.

## Layered Bridge Architecture

### Layer 1: Clinicopathologic Suspicion Builds The Case

This is the operational front door.

It is where the workup becomes serious enough to justify stronger downstream testing.

In the current vault, this layer is strongest because:

- it is carried by direct case-series work
- it is form-aware
- it is central to real suspicion-building

This layer answers:

`is this disease pattern FIP-like enough that the workup should intensify?`

### Layer 2: Molecular / Mutation Support Tightens But Does Not Close

This layer is where mutation-related assays live.

Its role is not to replace the first layer.
Its role is to narrow uncertainty after suspicion is already real.

This layer answers:

`given that the pattern is already suspicious, does mutation-related evidence strengthen the case?`

### Layer 3: Neurologic Extension Changes The Workup Shape

This is not just “more support.”

It is a different workup branch.

Once neurologic disease is in play, the module needs:

- CNS-specific logic
- CSF-based support
- separation from ordinary suspicion pathways

This branch should now be read more tightly:

- a positive CSF signal can be highly strengthening in the neurologic branch
- a negative CSF signal does not erase FIP from the broader workup
- subgroup-sensitive utility is not the same thing as generic-workup leadership
- `src-fip-023` reports specificity `100%` and PPV `100%`, but overall sensitivity `42.1%` and NPV `57.7%`; the neurologic/ocular subgroup sensitivity rises to `85.7%`

This layer answers:

`when does the workup stop being ordinary FIP suspicion and become a neurologic branch?`

## What This Means Practically

The current vault supports the following workup sequence:

1. recognize disease-form and clinicopathologic pattern
2. use mutation-related assays as bounded strengthening, not as the first trigger
3. branch into CSF / neurologic extension when CNS complexity is present

That sequence is more useful than a generic sentence like:

`combine tests`

because it says which layer should lead.

## Current Working Hierarchy

| Bridge Layer | Current Position In Vault | Function |
|---|---|---|
| Clinicopathologic pattern | leading operational layer | starts and shapes suspicion |
| Mutation-related support | secondary strengthening layer | narrows but does not settle |
| CSF / neurologic support | specialized extension layer | changes the branch, not just the confidence |
| Acute phase / immunoglobulin support | lower supportive context | background support, not first trigger |
| Serology | historical background context | explains why older laboratory support did not resolve the workup alone |

## What The Vault Can Now Say More Clearly

1. FIP workup should be led by clinicopathologic suspicion, not by mutation testing.
2. Mutation assays matter most after the case is already suspicious.
3. Neurologic workup is a branch shift, not just an intensity increase.
4. Endpoint channels in FIP have different jobs, and the order of use matters.
5. Older serology is most useful as historical boundary context, not as current workup leadership.
6. The CSF branch has strong positive support after branch shift, but weak enough broad negative support that it cannot become a generic rule-out gate.

## Best Reuse Targets

- [endpoint handbook](../../topics/fip/endpoint-handbook.md)
- [FIP acute-phase and immunoglobulin support memo](fip-acute-phase-support-memo.md)
- [FIP diagnostic-workup memo](fip-diagnostic-workup-memo.md)
- [FIP mutation-diagnostics boundary memo](fip-mutation-diagnostics-boundary-memo.md)
- [recognition architecture](../../topics/fip/recognition-architecture.md)
