---
id: system-ibd-treatment-hierarchy-feline-primary-memo-20260417
type: system
topic: ibd
species: feline
disease: IBD
question_type: treatment
language: en
last_compiled_at: 2026-04-17
confidence: medium
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
source_ids:
  - src-ibd-014
  - src-ibd-021
  - src-ibd-005
---

# IBD Treatment Hierarchy: Feline-Primary Framing Memo, 2026-04-17

## Purpose

This memo addresses the P2 gap from the densification queue:

> treatment hierarchy 的 stronger feline-primary framing

The existing treatment-evidence memos are accurate about what is uncertain. This memo adds the other half: what IS defensible, stated constructively, graded by feline-primary evidence quality. The goal is not to overclaim — it is to stop understating what the current source set actually supports.

## Core Shift From Prior Framing

| Prior framing | This memo's framing |
|---|---|
| "no stable final treatment ranking yet" | Here is the defensible ordering we can hold, labeled by confidence |
| "no strong idiopathic-IBD-specific drug efficacy hierarchy" | True. But a feline-primary functional ordering exists below that bar |
| Treatment branch = three tiers with weak language | Treatment branch = graduated confidence ladder with explicit anchors |

The prior framing was not wrong. It was incomplete — it named the ceiling without naming the floor.

## Feline-Primary Treatment Ladder

### Step 1: Dietary Intervention — Highest Feline-Primary Confidence

**Evidence source:** src-ibd-014

**What the evidence supports:**
- Hydrolysed protein dietary response is a real feline-primary signal
- Diet-first management is the most defensible early intervention anchor
- `diet-first chronic-enteropathy management` is a safe framing for step-one practical guidance

**Confidence grade:** medium-high (for feline-primary practical use)

**Why it leads:**
- src-ibd-014 is the only feline-primary treatment source with direct clinical anchoring
- The signal is clean even when labeled conservatively (chronic-enteropathy, not idiopathic-IBD-specific)
- Diet is also structurally safer for early management given the diagnostic boundary overlap with food-responsive disease

**Framing to hold:**
- `diet-first is step 1 in chronic enteropathy management for cats` `[source_supported_conclusion: src-ibd-014]`

**Framing to avoid:**
- "diet cures IBD" (overclaim)
- "diet is idiopathic-IBD-specific treatment" (wrong — it works across the exclusion workup spectrum)

---

### Step 2: Immunomodulatory / Medical Management — Real But Claim-Thin

**Evidence source:** src-ibd-021 (broad overview context)

**What the evidence supports:**
- Immunomodulatory strategies (corticosteroids as the most recognizable example) are part of the recognized feline IBD treatment architecture
- The broad overview places immunomodulation within the treatment map alongside diet
- This step is more medicine-like in shape and may eventually become the cleaner route-fit archetype

**Confidence grade:** low-to-medium (for feline-primary specific ranking)

**Why it stays here:**
- The current IBD vault does not contain a clean feline-primary efficacy hierarchy for specific immunomodulatory drugs
- src-ibd-021 provides overview context, not direct comparative feline efficacy data
- Broad overview material should not be promoted to feline-primary efficacy leader

**Framing to hold:**
- `immunomodulatory management is the recognized step 2 when dietary response is insufficient` `[source_supported_conclusion: src-ibd-021]`
- `specific drug ranking within this step should not be hardened beyond what feline-primary sources currently support` `[llm_inference]`

**Framing to avoid:**
- Specific preferred-drug hierarchy claims (prednisolone superiority over chlorambucil or vice versa) without feline-primary comparative evidence

---

### Step 3: Exploratory Branches — Acknowledged But Not Clinically Active

**Evidence source:** src-ibd-005 (mesenchymal stem cell), mechanism overview

**What the evidence supports:**
- Microbiota-directed strategies have real biologic rationale
- Feline-derived MSC work is a genuine translational branch
- These belong in the architecture as future-direction markers, not current clinical steps

**Confidence grade:** low (for current clinical hierarchy use)

**Framing to hold:**
- `exploratory branches belong in the treatment architecture, clearly below clinical steps 1 and 2` `[source_supported_conclusion: src-ibd-005]`
- `mouse-model benefit does not equal spontaneous feline enteropathy efficacy` `[quoted_fact: src-ibd-005]`

---

## Defensible Hierarchy Statement

The feline IBD treatment hierarchy that can be held now, at appropriate confidence:

```
Step 1: Dietary intervention (hydrolysed diet)
        — feline-primary anchor, medium-high confidence
        — safe for diet-first chronic-enteropathy management framing

Step 2: Immunomodulatory / medical management
        — real but claim-thin, low-to-medium feline-primary confidence
        — specific drug ranking not yet settled by feline-primary sources

Step 3 (exploratory): Microbiota-directed, stem-cell translational
        — real translational branches, not clinical management steps
        — named and bounded, not promoted
```

This ladder is not a final ranking. It is the most defensible current ordering from feline-primary sources.

## What Changes From Prior Treatment Memos

1. **The floor is now explicit.** Prior memos named the uncertainty ceiling (no final ranking). This memo names the defensible floor (what we CAN say at each step).

2. **Confidence is graduated, not binary.** Not "no ranking" vs "final ranking." Diet = medium-high, immunomodulatory = low-to-medium, exploratory = low.

3. **Feline-primary evidence is separated from cross-species extrapolation.** Each step now names which part of its claim is feline-primary vs context-derived.

4. **The step-1/step-2 division is made explicit.** Prior memos discussed tiers but did not name them as a sequential management ladder.

## What This Memo Does Not Change

- The diagnostic-boundary constraint still applies: treatment language should stay behind exclusion-first workup certainty
- The IBD/lymphoma boundary still matters: chlorambucil positioning requires that boundary to be explicit
- src-ibd-021 remains context-layer evidence, not a feline-primary efficacy authority
- Jurisdiction recommendation is not in scope

## Best Write-Back Targets

- [IBD treatment evidence memo](ibd-treatment-evidence-memo.md)
- [IBD treatment product archetype memo](ibd-treatment-product-archetype-memo.md)
- [translation brief](../../topics/ibd/translation-brief.md)
- [treatment evidence bilingual](../../topics/ibd/treatment-evidence-bilingual.md)
- [current state dashboard](../../topics/ibd/current-state-dashboard.md)
- [IBD recurring verification path](ibd-recurring-verification-path-20260417.md)

## Promotion Judgment

- repeated? `yes — treatment hierarchy questions recur`
- structurally clarifying? `yes — adds the defensible floor to existing ceiling language`
- evidence-safe enough for this layer? `yes — graduated confidence, feline-primary separation explicit`
- smallest durable home: `this memo + write-back to translation-brief + dashboard`

### Decision

- promote; supersedes the understated framing in prior treatment memos
