---
id: system-fip-risk-epidemiology-memo
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

# FIP Risk Epidemiology Memo

- Date: `2026-04-09`
- Scope: `src-fip-005`, `src-fip-008`, `src-fip-012`, `src-fip-020`

This memo exists to stop the FIP module from using `risk` as one vague bucket.

## Core Position

1. FIP risk epidemiology is not flat.
2. The current vault already supports at least three different risk layers:
   - signalment risk
   - coronavirus ecology / multi-cat exposure risk
   - referral-population enrichment
3. Risk context should raise suspicion earlier, not settle diagnosis.
4. Institutional burden should not be confused with community prevalence.

## Current Risk Layers

### Layer 1: Signalment Risk

This layer is mainly carried by:

- `src-fip-005`
- `src-fip-012`

What it means:

- young age is one of the strongest practical early-risk signals
- breed signal is patterned, not just `purebred cats`
- sex signal exists, but should remain below age and ecology in interpretive weight

### Layer 2: Coronavirus Ecology / Multi-Cat Risk

This layer is mainly carried by:

- `src-fip-008`

What it means:

- endemic feline coronavirus exposure context matters
- multi-cat environments are not only demographic context, but biologic pressure context
- ecology-aware risk is different from generic population-risk language

### Layer 3: Referral / Institutional Enrichment

This layer is mainly carried by:

- `src-fip-020`

What it means:

- FIP is materially enriched in VMTH and diagnostic-laboratory settings
- referral burden and general-population prevalence are not the same thing
- institutional case flow changes how often FIP enters active workup

## Current Working Hierarchy

| Risk Layer | Current Position In Vault | Notes |
|---|---|---|
| Young-age and signalment risk | strongest practical early-risk layer | easiest reusable pretest-suspicion branch |
| Multi-cat / endemic coronavirus ecology | high-value contextual layer | sharpens exposure and background-pressure reasoning |
| Referral / institutional enrichment | important operational context | explains why FIP stays prominent in tertiary and diagnostic settings |
| Breed-prevalence literature | useful but thinner branch | should remain specific and population-bound |

## What The Current Sources Actually Support

### Stronger Support

- age should sit near the center of early FIP risk framing
- breed signal should be written specifically, not as a vague pedigree warning
- multi-cat endemic coronavirus context deserves its own ecology-aware branch
- referral and diagnostic-laboratory populations materially enrich FIP burden

### Bounded Support

- Australian signalment-risk findings should not be treated as universal
- referral-population burden should not be promoted into community prevalence
- risk signals should not be treated as diagnostic signals
- risk structure does not replace clinicopathologic recognition

## What This Branch Is Not Allowed To Become

- It is not allowed to become one sentence like `young purebred cats in multicat homes`.
- It is not allowed to confuse ecology with signalment.
- It is not allowed to confuse referral enrichment with baseline prevalence.
- It is not allowed to let risk context act as a diagnosis proxy.

## What The Vault Can Now Say More Clearly

1. FIP risk should be modeled as a layered pretest-suspicion architecture.
2. Signalment, ecology, and referral enrichment are different kinds of risk information.
3. Age is currently the cleanest practical risk lever in the module.
4. Risk context matters most when it makes the clinician worry earlier, not when it pretends to settle the case.

## Best Reuse Targets

- [risk and recognition](../../topics/fip/risk-and-recognition.md)
- [recognition architecture](../../topics/fip/recognition-architecture.md)
- [current state dashboard](../../topics/fip/current-state-dashboard.md)
- [synthesis index](../../topics/fip/synthesis-index.md)
