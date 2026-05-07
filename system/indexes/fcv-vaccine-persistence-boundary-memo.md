---
id: system-fcv-vaccine-persistence-boundary-memo
type: system
topic: fcv
last_compiled_at: 2026-04-24
owner: codex
status: active
language: en
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
---

# FCV Vaccine-Persistence Boundary Memo

- Date: `2026-04-24`
- Scope: `src-fcv-003`, `src-fcv-010`, `src-fcv-011`, `src-fcv-012`, `src-fcv-017`, `src-fcv-022`, `src-fcv-024`

This memo exists to stop the FCV vaccine branch from collapsing into one vague claim like:

`vaccines work, but variants are a problem`

That sentence is directionally true and structurally weak.

## Core Takeaway

`the current FCV vaccine branch supports disease mitigation, heterologous protection, and broad but incomplete immune coverage; it does not support sterilizing-immunity, complete field coverage, or chronic-carrier control`

## Current Vaccine-Persistence Layers

### Layer 1: Broad But Incomplete Neutralisation Breadth

This layer is mainly carried by:

- `src-fcv-003`
- `src-fcv-010`
- `src-fcv-024`

Current meaning:

- currently used vaccine strains can show broad cross-neutralisation against field isolates
- broad is not complete
- sequence diversity and field drift remain relevant to interpretation
- `src-fcv-003` is now deep-extracted and can directly carry the `breadth but not closure` language
- `src-fcv-010` is now deep-extracted and can directly carry the `laboratory strains cleaner than field isolates` warning

Boundary:

- in-vitro breadth is not equal to field sterilizing immunity
- geography and time can change isolate fit

### Layer 2: Challenge Protection

This layer is mainly carried by:

- `src-fcv-011`
- `src-fcv-013`

Current meaning:

- some vaccine or vaccine-strain studies support meaningful challenge protection
- challenge-protection logic belongs above simple titre rhetoric
- avirulent/broadly neutralising strain work is useful as a controlled proof branch
- `src-fcv-011` is now deep-extracted and can directly carry the challenge-protection branch
- `src-fcv-013` is now deep-extracted and adds a replication-deficient platform-vaccine branch, but remains experimental rather than current-market guidance

Boundary:

- challenge studies do not automatically equal current-market superiority
- protection in controlled settings is not a whole-population field-control answer

### Layer 3: Cellular-Immunity Augmentation

This layer is mainly carried by:

- `src-fcv-022`

Current meaning:

- vaccine benefit can exceed humoral cross-neutralisation alone
- cellular immunity is a real explanatory branch for FCV vaccine performance
- one deep-extracted cellular-immunity anchor now supports this layer directly

Boundary:

- this is not a replacement for breadth or challenge endpoints
- experimental immune readouts do not create a simple owner-facing vaccine rank

### Layer 3.5: Platform-Vaccine Design

This layer is mainly carried by:

- `src-fcv-013`

Current meaning:

- replication-deficient platform work can generate neutralising-antibody and homologous challenge signals
- combining genetically distant VP1 constructs can broaden neutralising responses
- platform design is now a real FCV vaccine research branch

Boundary:

- experimental platform findings are not current-market recommendation language
- neutralisation breadth and challenge reduction are not the same as field effectiveness or label authority

### Layer 4: Serology-Resistance Prediction

This layer is mainly carried by:

- `src-fcv-012`

Current meaning:

- antibody testing can support resistance-prediction logic in vaccinated cats
- serology belongs to endpoint interpretation, not to whole-program vaccination policy
- `src-fcv-012` is now deep-extracted and can directly carry the `predictive in vaccinated cats, but not policy absolutism` language

Boundary:

- antibody positivity is not the same as universal long-term protection
- this does not justify a generalized no-booster claim

### Layer 5: Persistence / Chronic Carrier Control

This layer is mainly carried by:

- `src-fcv-017`

Current meaning:

- prior infection or vaccination can reduce acute disease while failing to prevent chronic carriage
- persistence is a central FCV control problem, not an edge case

Boundary:

- vaccine success should not be written as carrier-state elimination
- persistence cannot be explained away as vaccine failure alone

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| FVP1 | FCV vaccines have broad but incomplete cross-neutralisation coverage against field isolates | B | src-fcv-003, src-fcv-010, src-fcv-024 | not field sterilizing-immunity claim |
| FVP2 | Challenge-protection and cellular-immunity branches support real vaccine benefit beyond simple titre language | B | src-fcv-011, src-fcv-013, src-fcv-022 | not current-market superiority claim |
| FVP3 | Serologic resistance-prediction is a bounded endpoint branch, not a stand-alone vaccination-policy answer | B | src-fcv-012 | not no-booster policy claim |
| FVP4 | Acute-disease mitigation and chronic-carrier prevention must stay separated in FCV vaccine language | B | src-fcv-017, src-fcv-022 | not carrier-state-control claim |

## What The Module Can Say Safely

- vaccination is a core FCV disease-control tool
- vaccine benefit should be written as disease-mitigation and partial cross-protection, not infection elimination
- one deep-extracted breadth anchor now supports `broad but incomplete` cross-neutralisation wording directly
- one deep-extracted early field-fit stress-test anchor now supports the warning that field-isolate coverage can look much weaker than laboratory readouts
- one deep-extracted challenge anchor now supports `challenge benefit above titre rhetoric` wording directly
- one deep-extracted replication-deficient platform anchor now supports `active vaccine design branch, not current-market recommendation` wording
- one deep-extracted cellular-immunity anchor now supports the claim that vaccine benefit can exceed titre logic
- neutralisation breadth, challenge protection, cellular immunity, serology, and persistence belong to different endpoint families
- one deep-extracted serology anchor now supports bounded resistance-prediction language directly
- chronic carriage is the main branch that prevents overclaim in FCV vaccine prose

## What The Module Should Not Say Yet

- do not write a flat FCV vaccine leaderboard
- do not claim universal coverage against current field diversity
- do not equate antibody positivity with complete durable protection
- do not treat reduced acute disease as proof of carrier-state suppression
- do not turn experimental challenge results into current-label or current-market conclusions
- do not turn platform-vaccine findings into product availability or approval claims

## Best Reuse Targets

- [endpoint handbook](../../topics/fcv/endpoint-handbook.md)
- [translation brief](../../topics/fcv/translation-brief.md)
- [regulatory brief](../../topics/fcv/regulatory-brief.md)
- [current state dashboard](../../topics/fcv/current-state-dashboard.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for boundary architecture; no, for final vaccine ranking`
- smallest durable home: `memo + endpoint write-back + translation write-back`

### Decision

- promote
