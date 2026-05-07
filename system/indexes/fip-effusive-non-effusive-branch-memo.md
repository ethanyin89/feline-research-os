---
id: system-fip-effusive-non-effusive-branch-memo
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

# FIP Effusive-Non-Effusive Branch Memo

- Date: `2026-04-09`
- Scope: `src-fip-003`, `src-fip-006`, `src-fip-015`, `src-fip-023`

This memo exists to stop the FIP module from flattening disease form into either `wet vs dry` shorthand or generic severity language.

## Core Position

1. Effusive and non-effusive FIP should be treated as branch-defining presentation patterns, not as cosmetic labels.
2. Disease form belongs first to recognition and workup architecture, not first to one linear severity ladder.
3. Effusion can accelerate suspicion, but should not be mistaken for diagnostic finality.
4. Non-effusive and neurologic disease mainly matter because they change the workup pathway and supportive evidence mix.

## Why This Memo Matters

The current module already has:

- clinicopathology anchors
- effusion recognition logic
- neurologic recognition logic
- composite-support diagnostic framing

What was still missing was a clean rule for how disease form should sit between them.

## Current Branch Architecture

### Branch 1: Effusive Front-Door Recognition

This branch is where:

- abdominal or thoracic fluid can sharply increase suspicion
- recognition may become faster and more front-loaded
- fluid-associated pattern recognition becomes operationally central

This branch is mainly carried by:

- `src-fip-006`
- `src-fip-015`

### Branch 2: Non-Effusive / Dry-Form Complexity

This branch is where:

- suspicion becomes less visually obvious
- clinicopathology and staged pattern recognition matter more
- workup can drift into broader ambiguity if disease form is not modeled explicitly

This branch is mainly carried by:

- `src-fip-003`
- `src-fip-015`

### Branch 3: Neurologic Extension

This is not just `more severe dry form`.

It is where:

- recognition becomes branch-shifted
- CNS-aware support enters the workup
- CSF-based strengthening can become relevant

This branch is mainly carried by:

- `src-fip-023`

## What The Current Sources Actually Support

### Stronger Reading

- disease form is operationally important in FIP
- clinicopathology and staging work should be read through form-aware recognition
- effusive presentation can function as a front-door suspicion trigger
- non-effusive and neurologic forms explain why FIP cannot be modeled as an easy fluid-disease story

### Bounded Reading

- wet versus dry should not be treated as a complete mechanistic taxonomy
- effusive presentation should not be treated as diagnostic proof
- non-effusive presentation should not be reduced to “same disease, just later”
- neurologic form should not be collapsed into ordinary non-effusive disease

## Current Working Hierarchy

| Disease-Form Branch | Current Position In Vault | Notes |
|---|---|---|
| Effusive front-door suspicion | fast recognition branch | raises suspicion early but does not settle diagnosis |
| Non-effusive clinicopathology-led recognition | ambiguity-heavy branch | depends more on structured pattern recognition |
| Neurologic extension | specialized branch shift | changes both recognition and support strategy |

## What This Branch Is Not Allowed To Become

- It is not allowed to become a wet-versus-dry slogan with no workup consequence.
- It is not allowed to treat effusion as proof of FIP.
- It is not allowed to erase the added complexity of non-effusive and neurologic disease.
- It is not allowed to substitute disease form for full diagnostic architecture.

## What The Vault Can Now Say More Clearly

1. Disease form in FIP changes how recognition starts and how support is layered.
2. Effusive FIP is best treated as a suspicion accelerator, not a certainty engine.
3. Non-effusive FIP is where clinicopathology and staged recognition become especially important.
4. Neurologic disease is best modeled as a branch extension beyond the basic wet-versus-dry split.

## Best Reuse Targets

- [risk and recognition](../../topics/fip/risk-and-recognition.md)
- [recognition architecture](../../topics/fip/recognition-architecture.md)
- [FIP effusion recognition memo](fip-effusion-recognition-memo.md)
- [FIP neurologic recognition memo](fip-neurologic-recognition-memo.md)
- [FIP diagnostic-workup memo](fip-diagnostic-workup-memo.md)
