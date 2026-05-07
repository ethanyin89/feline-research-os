---
id: system-ibd-treatment-product-archetype-memo
type: system
topic: ibd
last_compiled_at: 2026-04-09
owner: codex
status: active
language: en
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
---

# IBD Treatment Product Archetype Memo

Date: 2026-04-09  
Scope: first-pass product-archetype framing for later IBD regulatory and route work

This memo does not make a jurisdiction recommendation.

It does something narrower:

- converts the current IBD treatment and extension branches into reusable product archetypes
- separates `claim-fit` from `route-fit`
- shows which archetypes are clean enough for later route analysis and which ones are still too biologically or diagnostically unstable

## Core Takeaway

`for IBD, product-type clarity must come before jurisdiction comparison`

The current IBD module is now strong enough to support product-archetype framing.

It is not yet strong enough to support indication-ready regulatory route recommendations.

## Why This Memo Exists Now

- the diagnostic and pathology branches are already more stable than the treatment branch
- the treatment branch is now tiered enough to stop being a flat list
- the module already contains several neighboring or extension diseases that make overbroad product claims risky
- regulatory work will stay weak unless product classes are separated first

## Current Archetype Set

### Archetype 1: Diet-First Chronic-Enteropathy Management

Best current anchors:

- [IBD early treatment anchor memo](ibd-early-treatment-anchor-memo.md)
- [IBD treatment evidence memo](ibd-treatment-evidence-memo.md)

Current meaning:

- this is the cleanest practical treatment archetype in the current IBD vault
- it is still partly an `IBD-plus-food-responsive-overlap` archetype rather than a pure idiopathic-IBD archetype
- it is the safest first bridge between clinical reality and later product thinking

Claim-fit:

- supportive management
- diet-first chronic-enteropathy control

Claim style to avoid:

- idiopathic-IBD-specific efficacy overclaim
- broad disease-modification framing

Current internal read:

- best current treatment archetype overall
- probably the first archetype to carry into later route-level thinking

### Archetype 2: Broad Immunomodulatory Or Medical Management

Best current anchors:

- [translation brief](../../topics/ibd/translation-brief.md)
- [IBD treatment evidence memo](ibd-treatment-evidence-memo.md)

Current meaning:

- this is a clinically recognizable branch
- the current vault does not yet contain a clean feline-primary efficacy hierarchy inside it
- it is closer to a medicine-style route question than the diet branch, but the evidence spine is less settled

Claim-fit:

- chronic-enteropathy symptom control
- inflammatory-burden management

Claim style to avoid:

- strong idiopathic-IBD-specific superiority hierarchy
- final preferred-drug logic

Current internal read:

- route-fit may later be easier than for diet
- claim-fit is currently weaker than the diet archetype

### Archetype 3: Microbiota-Directed Adjunct

Best current anchors:

- [mechanism overview](../../topics/ibd/mechanism-overview.md)
- [IBD support and frontier marker memo](ibd-support-and-frontier-marker-memo.md)

Current meaning:

- the biologic rationale is real
- the current module still carries this mostly as mechanism and boundary pressure rather than as direct treatment proof
- this archetype is conceptually important but operationally unstable

Claim-fit:

- adjunctive microbiota support
- mechanism-informed supportive positioning

Claim style to avoid:

- routine-ready disease-control positioning
- biomarker-driven efficacy certainty

Current internal read:

- too unstable for early route memo work
- useful as a future translational branch, not as a first regulatory stress test

### Archetype 4: Regenerative / Stem-Cell Translational Product

Best current anchors:

- [src-ibd-005 deep extraction round 1](src-ibd-005-deep-extraction-round1.md)
- [IBD treatment evidence memo](ibd-treatment-evidence-memo.md)

Current meaning:

- this is a real translational branch
- it is anchored by mouse-model benefit, not spontaneous feline enteropathy efficacy
- it is the clearest example of `mechanistic excitement > routine readiness`

Claim-fit:

- exploratory translational potential
- regenerative mechanism branch

Claim style to avoid:

- clinical management guidance
- efficacy-forward feline product framing

Current internal read:

- not suitable for current route work
- belongs in long-horizon translational strategy only

### Archetype 5: Diagnostic Or Stratification Assay

Best current anchors:

- [endpoint handbook](../../topics/ibd/endpoint-handbook.md)
- [IBD support and frontier marker memo](ibd-support-and-frontier-marker-memo.md)
- [IBD tissue-marker boundary memo](ibd-tissue-marker-boundary-memo.md)

Current meaning:

- the IBD module contains several candidate assay-style branches
- none of them currently justify one-marker workup leadership
- this branch matters strategically because it could later split into support-marker and frontier-marker product logic

Claim-fit:

- support-marker or stratification positioning
- non-lead diagnostic support

Claim style to avoid:

- definitive diagnostic assay
- stand-alone disease-class discrimination

Current internal read:

- strategically relevant, but still too unstable for early product-route compression

## Archetype Comparison Table

| Archetype | Current Evidence Strength | Claim-Fit Clarity | Likely Future Route-Fit | Current Best Internal Read |
|---|---|---|---|---|
| diet-first chronic-enteropathy management | high | medium-to-high | medium | best first practical archetype |
| broad immunomodulatory or medical management | medium | medium | medium-to-high | route-fit may later exceed claim-fit |
| microbiota-directed adjunct | low-to-medium | low | low-to-medium | biologically interesting, operationally unstable |
| regenerative / stem-cell translational product | low | low | low | not ready for route work |
| diagnostic or stratification assay | low-to-medium | low | low-to-medium | strategically important, but not yet lead-workup safe |

## What This Memo Changes

This memo makes one point explicit:

`the first IBD regulatory question is not which jurisdiction is easiest; it is which product class is coherent enough to survive route analysis`

That means:

- the diet branch is still the cleanest first archetype
- the medicine-style branch may later become a better route-fit test than the diet branch
- microbiota, regenerative, and assay branches are still too unstable to carry early route work

## Best Current Internal Read

### What we can say now

- the current IBD module is strong enough to sort treatment and adjacent branches into product archetypes
- diet-first management is the cleanest present archetype
- medicine-style management may later become the cleanest route-fit archetype
- several conceptually attractive branches are still too thin for route work

### What we should not say now

- do not claim that any jurisdiction is already the best first IBD route
- do not assume a medicine-like product is automatically the best strategy just because route logic may later be cleaner
- do not let treatment or assay product thinking outrun the exclusion-first workup architecture

## What To Do Next

The next regulatory step should probably be one of these:

- a first `diet-first chronic-enteropathy route memo`, if the goal is to start from the cleanest treatment archetype
- a first `medical-management route memo`, if the goal is to test where route-fit may be cleaner than claim-fit

Both should wait until an official-source regulatory pack exists for IBD.

## Best Reuse Targets

- [regulatory brief](../../topics/ibd/regulatory-brief.md)
- [IBD treatment evidence memo](ibd-treatment-evidence-memo.md)
- [translation brief](../../topics/ibd/translation-brief.md)
- [current state dashboard](../../topics/ibd/current-state-dashboard.md)
