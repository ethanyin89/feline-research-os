---
id: system-fip-assay-performance-boundary-memo
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

# FIP Assay-Performance Boundary Memo

- Date: `2026-04-10`
- Scope: `src-fip-002`, `src-fip-007`, `src-fip-010`, `src-fip-011`, `src-fip-022`, `src-fip-023`

This memo exists to stop the FIP endpoint branch from sounding more precise than the current source pack actually is.

Right now the vault already knows the order of use.

What is still easy to blur is the performance boundary between the main assay-style branches.

## Core Position

1. The current FIP vault does not support a clean ranking like `best assay -> second-best assay -> third-best assay`.
2. It does support a boundary map.
3. That boundary map is currently tighter than any numeric-seeming assay leaderboard.
4. The most reusable current read is:
   - acute-phase and immunoglobulin markers are real but background-level
   - older serology is historically useful but too overclaim-sensitive for modern leadership
   - mutation-related assays are meaningful but must carry their limitation branch with them
   - CSF viral detection has the sharpest subgroup-specific strengthening, but only after neurologic branch shift
5. The current vault is stronger at saying `where each assay fits` than `which assay wins`.

## Current Assay Boundary Map

### Acute-Phase And Immunoglobulin Markers

Current role:

- bounded inflammatory support
- exposure-aware background context
- supportive rather than decisive

Current safe reading:

- this branch belongs in composite support
- it enriches the case after suspicion is already real
- it should not be promoted into a front-door diagnostic trigger

### Older Serology

Current role:

- historical laboratory context
- exposure-linked support background

Current safe reading:

- older serology helps explain why laboratory support remained interesting in FIP
- it does not deserve modern first-wave authority inside the current vault

### Mutation-Related Assays

Current role:

- bounded strengthening after suspicion
- context-sensitive molecular support

Current safe reading:

- mutation-related assays can matter diagnostically
- their utility and their limitation are inseparable
- this branch is stronger than serology for current workup relevance
- this branch is still too fragile for certainty language

### CSF Viral Detection

Current role:

- specialized neurologic-extension support
- subgroup-sensitive strengthening

Current safe reading:

- a positive CSF signal can be highly strengthening in the neurologic and/or ocular branch
- this does not make CSF the leader of ordinary FIP workup
- overall sensitivity remains too limited for generic exclusion or generic first-wave authority
- the current abstract-level figures are: specificity `100%`, PPV `100%`, overall sensitivity `42.1%`, NPV `57.7%`, and neurologic/ocular sensitivity `85.7%`

## Current Working Hierarchy

| Assay / Marker Branch | Current Position In Vault | Strongest Safe Claim | Main Boundary |
|---|---|---|---|
| Acute-phase / immunoglobulin markers | background support | real supportive inflammatory context exists | not a lead trigger |
| Older serology | historical context | exposure-linked support remains part of the history | too overclaim-sensitive for modern leadership |
| Mutation-related assays | bounded strengthening | meaningful supportive value after suspicion is real | utility and limitation must stay together |
| CSF viral detection | specialized branch support | can strongly strengthen the neurologic/ocular branch, especially when positive | not generic-workup authority; limited overall sensitivity and NPV prevent broad exclusion use |

## What The Current Vault Can Say Safely

1. Serology is the weakest current operational assay-style branch.
2. Acute-phase and immunoglobulin support is more reusable than serology, but still background-level.
3. Mutation-related assays are more clinically actionable than background laboratory support, but still bounded.
4. CSF viral detection has the sharpest subgroup-specific strengthening signal, but only inside the neurologic branch.
5. None of these branches outranks clinicopathology as the operational front door.
6. `src-fip-023` is currently the only assay-style branch with enough extracted numeric performance detail to quote; do not invent comparable numeric rankings for mutation assays, serology, or acute-phase markers from the current extraction layer.

## What The Current Vault Should Not Pretend To Know

- It should not pretend to have a clean sensitivity/specificity ranking table across these branches.
- It should not act as if mutation testing has solved diagnostic closure.
- It should not act as if CSF specificity makes CSF the best general assay.
- It should not demote clinicopathology just because some assay branches sound more technical.
- It should not collapse assay placement into one sentence like `molecular tests are best`.

## What This Memo Adds

1. The support-order memo answers `what comes first`.
2. This memo answers `what each assay branch is actually allowed to claim`.
3. Together they let the vault say more than `composite diagnosis` without pretending to have a final assay leaderboard.

## Best Reuse Targets

- [endpoint handbook](../../topics/fip/endpoint-handbook.md)
- [risk and recognition](../../topics/fip/risk-and-recognition.md)
- [FIP support-order memo](fip-support-order-memo.md)
- [FIP diagnostic-workup memo](fip-diagnostic-workup-memo.md)
- [FIP mutation-diagnostics boundary memo](fip-mutation-diagnostics-boundary-memo.md)
- [FIP acute-phase and immunoglobulin support memo](fip-acute-phase-support-memo.md)
- [current state dashboard](../../topics/fip/current-state-dashboard.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for assay-placement boundary; no, for numeric ranking or final assay-performance claims`
- smallest durable home: `memo + endpoint topic update + dashboard update`

### Reason

- what is repeating:
  FIP marker questions keep recurring as if the vault should already know a clean assay leaderboard
- what becomes clearer:
  the current system can now distinguish background support, bounded strengthening, and subgroup-specific specialized support without faking a final ranking table
- what is still too thin, if anything:
  assay-level full-text discriminative detail remains too thin for stronger comparative performance language

### Decision

- promote
