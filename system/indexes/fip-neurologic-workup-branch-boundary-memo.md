---
id: system-fip-neurologic-workup-branch-boundary-memo
type: system
topic: fip
last_compiled_at: 2026-04-11
owner: codex
status: active
language: en
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
---

# FIP Neurologic Workup Branch Boundary Memo

- Date: `2026-04-11`
- Scope: `src-fip-003`, `src-fip-015`, `src-fip-023`

This memo exists to answer a narrower question than neurologic recognition alone:

`when does ordinary FIP workup stop being ordinary workup and become a neurologic / CSF branch?`

That question keeps recurring, and the current vault already has enough structure to answer it more cleanly than scattered sentences do.

## Core Takeaway

`the current FIP vault supports a hard boundary between ordinary suspicion-building workup and neurologic-extension workup: the branch should shift on neurologic-context recognition, and CSF support only becomes central after that shift`

## What This Memo Is Narrower Than

This memo is narrower than:

- [FIP neurologic recognition memo](fip-neurologic-recognition-memo.md)
- [FIP diagnostic-workup memo](fip-diagnostic-workup-memo.md)
- [FIP endpoint-diagnostic bridge memo](fip-endpoint-diagnostic-bridge-memo.md)

Those pages explain the larger recognition or workup architecture.

This page answers the tighter control question:

`what is the actual boundary that stops CSF logic from leaking backward into ordinary FIP workup?`

## Current Boundary

### Layer 1: Ordinary FIP Suspicion-Building Workup

- clinicopathology leads
- disease-form-aware suspicion stays visible
- background laboratory context and mutation-related strengthening stay bounded inside ordinary workup
- this is still the default branch for most FIP recognition

### Layer 2: Neurologic Branch Trigger

- the branch should change when neurologic context is real enough that the case is no longer just ordinary wet/dry suspicion
- this is a category shift, not just an intensity increase
- the trigger belongs to recognition logic first, not to assay availability

### Layer 3: CSF-Centered Specialized Support

- CSF viral detection becomes meaningful after the branch has already changed
- positive CSF support can be highly strengthening inside the neurologic branch
- negative CSF support does not erase FIP from the broader neurologic workup
- CSF specificity should not backflow into ordinary-workup leadership

## What The Module Can Already Say

- neurologic FIP should be modeled as a true workup branch shift
- ordinary suspicion-building and neurologic-extension workup should not be flattened into one continuum
- CSF support is strongest as branch-specific strengthening, not as a universal front-door assay
- the hard problem is branch timing, not whether CSF has any value

## What The Module Should Not Yet Say

- there is no safe claim that CSF is the best general FIP diagnostic test
- there is no safe claim that CSF logic should lead ordinary FIP workup
- there is no safe claim that neurologic complexity is just more severe ordinary FIP
- there is no safe claim that negative CSF support broadly excludes neurologic FIP

## Short Operational Read

| Workup Stage | Current role | What leads | What must not happen |
|---|---|---|---|
| Ordinary FIP suspicion | default composite workup | clinicopathology and disease-form suspicion | do not let CSF logic lead here |
| Neurologic branch shift | category change | neurologic-context recognition | do not confuse branch shift with certainty |
| Specialized neurologic support | bounded strengthening | CSF-based support inside narrowed branch | do not backflow CSF specificity into generic leadership |

## Best Write-Back Targets

- [risk and recognition](../../topics/fip/risk-and-recognition.md)
- [recognition architecture](../../topics/fip/recognition-architecture.md)
- [endpoint handbook](../../topics/fip/endpoint-handbook.md)
- [current state dashboard](../../topics/fip/current-state-dashboard.md)
- [risk and recognition bilingual](../../topics/fip/risk-and-recognition-bilingual.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for branch-boundary control; no, for CSF-led general workflow claims`
- smallest durable home: `memo + topic write-back + dashboard write-back`

### Reason

- what is repeating:
  neurologic FIP and CSF support keep being described correctly, but the actual workup boundary is still scattered across several pages
- what becomes clearer:
  branch shift is now the hard gate, and CSF value is downstream of that gate
- what is still too thin:
  routine implementation detail and stronger operational recommendation language

### Decision

- promote
