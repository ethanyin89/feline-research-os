---
id: system-fip-neurologic-recognition-memo
type: system
topic: fip
last_compiled_at: 2026-04-09
owner: codex
status: active
language: en
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
---

# FIP Neurologic Recognition Memo

- Date: `2026-04-09`
- Scope: `src-fip-003`, `src-fip-015`, `src-fip-023`, `src-fip-024`

This memo exists to stop the FIP module from treating neurologic disease as either a rare footnote or just “more severe ordinary FIP.”

## Core Position

1. Neurologic FIP is a recognition branch shift, not just a severity modifier.
2. The neurologic branch starts at the recognition layer before it reaches specialized diagnostic support.
3. CSF-based support matters, but only after the case has already entered neurologic-branch logic.
4. Neurologic recognition and neurologic treatment complexity should remain adjacent but distinct layers.

## Current Neurologic Recognition Layers

### Layer 1: Neurologic Branch Trigger

This layer is mainly carried by:

- `src-fip-003`
- `src-fip-015`

What it means:

- neurologic involvement should immediately change how the case is read
- the case is no longer just ordinary wet/dry suspicion with extra severity
- disease-form recognition must widen into a separate branch

### Layer 2: Specialized Diagnostic Support

This layer is mainly carried by:

- `src-fip-023`

What it means:

- CSF RT-PCR can strongly support diagnosis in the neurologic/ocular branch
- negative CSF results do not erase FIP from the broader neurologic workup
- subgroup-specific utility should not be flattened into generic-workup claims

### Layer 3: High-Complexity Treatment Consequence

This layer is mainly carried by:

- `src-fip-024`

What it means:

- neurologic recognition is clinically important because treatment complexity changes downstream
- recognition and treatment are linked here, but should not be collapsed into one sentence

## Current Working Hierarchy

| Neurologic Branch | Current Position In Vault | Notes |
|---|---|---|
| Neurologic-sign branch trigger | leading recognition shift | changes the case category |
| CSF-based strengthening | bounded specialized support | useful after branch shift, not before |
| Neurologic treatment complexity | downstream consequence | adjacent to recognition, but not identical |

## What The Current Sources Actually Support

### Stronger Support

- neurologic disease should trigger a separate recognition branch
- CSF-based support has real value inside that branch
- subgroup logic matters more than one global test label
- neurologic recognition has downstream treatment consequences that justify its separate status

### Bounded Support

- neurologic recognition should not be reduced to CSF testing
- negative CSF support should not be used as a broad exclusion shortcut
- neurologic branch logic should not swallow the ordinary recognition architecture

## What This Branch Is Not Allowed To Become

- It is not allowed to become `neurologic signs = special PCR`.
- It is not allowed to become only a treatment-complexity story.
- It is not allowed to flatten neurologic recognition into ordinary FIP suspicion.
- It is not allowed to confuse branch shift with certainty.

## What The Vault Can Now Say More Clearly

1. Neurologic FIP should be recognized as a separate branch before specialized testing is chosen.
2. The correct sequence is `neurologic branch shift -> CNS-aware support`, not `CSF test creates the branch`.
3. CSF-based support is meaningful because the branch has already changed, not because it suddenly creates certainty.
4. Neurologic recognition matters partly because it changes downstream treatment complexity, but that does not make recognition and treatment the same layer.

## Best Reuse Targets

- [recognition architecture](../../topics/fip/recognition-architecture.md)
- [FIP diagnostic-workup memo](fip-diagnostic-workup-memo.md)
- [FIP endpoint-diagnostic bridge memo](fip-endpoint-diagnostic-bridge-memo.md)
- [current state dashboard](../../topics/fip/current-state-dashboard.md)
