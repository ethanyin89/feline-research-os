---
id: system-fip-acute-phase-support-memo
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

# FIP Acute-Phase And Immunoglobulin Support Memo

- Date: `2026-04-09`
- Scope: `src-fip-002`, `src-fip-007`

This memo exists to stop the FIP module from treating inflammatory laboratory support as either irrelevant or definitive.

## Core Position

1. Acute phase proteins and immunoglobulin patterns belong in the FIP support architecture.
2. They are bounded supportive context, not lead diagnosis.
3. Their value is greatest after clinicopathologic suspicion is already real.
4. This branch helps prevent endpoint logic from collapsing into only clinicopathology plus mutation testing.

## Current Branch Role

This branch is mainly carried by:

- `src-fip-002`
- `src-fip-007`

What it means:

- laboratory inflammatory context can support suspicion
- comparison against coronavirus-exposed cats is more useful than a simplistic disease-versus-normal framing
- this branch should sit below clinicopathology and below disease-form recognition in operational priority
- older effusive-form immunology adds branch-specific background context without changing current support hierarchy

## Current Working Hierarchy

| Support Branch | Current Position In Vault | Notes |
|---|---|---|
| Clinicopathology / disease-form recognition | lead operational branch | starts and shapes suspicion |
| Mutation-based strengthening | bounded focused support | narrows after suspicion is real |
| Acute phase / immunoglobulin support | lower supportive context | enriches background laboratory reading |
| CSF-based neurologic support | specialized branch | only after neurologic branch shift |

## What The Current Source Actually Supports

### Stronger Support

- acute phase proteins and immunoglobulin patterns deserve explicit mention
- inflammatory/immunologic support is part of composite diagnosis
- exposure-aware comparison increases the architectural value of the branch
- older effusive-form immunology gives the support branch some disease-form specificity beneath the more modern comparative marker paper

### Bounded Support

- this branch should not lead workup
- this branch should not be promoted into definitive diagnosis
- the current vault still lacks full-text discriminative detail for marker-level ranking

## What This Branch Is Not Allowed To Become

- It is not allowed to disappear from the endpoint map.
- It is not allowed to become a one-marker certainty story.
- It is not allowed to outrun clinicopathology.
- It is not allowed to be mistaken for a replacement of mutation or neurologic-extension support.

## What The Vault Can Now Say More Clearly

1. FIP supportive laboratory markers matter, but they belong in the background-support layer.
2. Acute phase and immunoglobulin patterns strengthen composite diagnosis rather than define it.
3. The right framing is `supportive inflammatory context`, not `diagnostic shortcut`.
4. A richer endpoint architecture is more accurate than a clinicopathology-versus-mutation binary.

## Best Reuse Targets

- [endpoint handbook](../../topics/fip/endpoint-handbook.md)
- [FIP endpoint-diagnostic bridge memo](fip-endpoint-diagnostic-bridge-memo.md)
- [FIP diagnostic-workup memo](fip-diagnostic-workup-memo.md)
- [current state dashboard](../../topics/fip/current-state-dashboard.md)
