---
id: system-ibd-recurring-verification-path-20260417
type: system
topic: ibd
species: feline
disease: IBD
question_type: verification
language: en
last_compiled_at: 2026-04-17
confidence: high
verification_status: compiled
decision_grade: stable
language_qa_status: light_checked
owner: codex
status: active
---

# IBD Recurring Verification Path, 2026-04-17

## Purpose

This page is the stable answer to the P2 densification gap:

> recurring verification path 变成稳定页

It is IBD-specific. The general `verify-a-claim.md` handles cross-disease claim lookup logic. This page handles the recurring IBD-specific verification questions that keep arriving in the system.

Use this page when you have an IBD claim and want to know: **where does it live, how strong is it, and where do you go to check it?**

---

## IBD-Specific Verification Pitfalls

These are the mistakes that recur specifically in IBD verification. Know them before you start.

### Pitfall 1: Conflating diagnosis with treatment

IBD claims split across two very different evidence layers: recognition/diagnosis and treatment. A strong claim in one does not strengthen the other.

Test: Is this a claim about what IBD IS (diagnostic/pathology layer), or about what WORKS (treatment layer)?

- Diagnostic claims: go to `mechanism-overview`, `idiopathic-pathology-memo`, `diagnostic-workup-memo`
- Treatment claims: go to `treatment-evidence-memo`, `treatment-hierarchy-feline-primary-memo`, `translation-brief`

### Pitfall 2: Conflating feline-primary with cross-species extrapolation

The IBD module contains both feline-primary studies and human/mouse overview material. These are not equivalent.

Test: Is the source a direct feline study or a cross-species review?

- src-ibd-014 = feline-primary (diet)
- src-ibd-021 = broad therapeutic overview (cross-species context)
- src-ibd-005 = mouse-model MSC work (translational only)

### Pitfall 3: Treating treatment hierarchy as flat

The current IBD treatment branch is NOT a flat list. It is a graduated ladder:
- Step 1 (diet): feline-primary, medium-high confidence
- Step 2 (immunomodulation): real but claim-thin, low-to-medium confidence  
- Step 3 (exploratory): architectural only, not clinical

Test: Is the claim treating all treatment options as equivalent? If so, it needs to be re-tiered.

### Pitfall 4: Crossing the IBD/lymphoma boundary

Some treatment logic (especially chlorambucil) lives at the boundary between IBD and small-cell lymphoma. A claim that is correct for one may be wrong for the other.

Test: Does this claim cross or ignore the IBD/lymphoma boundary?

- If yes: go to `ibd-lymphoma-boundary-memo` before concluding

### Pitfall 5: Outrunning the exclusion-first architecture

IBD diagnosis requires exclusion of other causes first. Treatment claims should not assume definitive IBD diagnosis in situations where the exclusion workup is incomplete.

Test: Is this claim assuming clean IBD diagnosis? Is that assumption warranted?

---

## Standard IBD Verification Route

### For any IBD claim, use this path in order:

**1. Locate the claim's layer**

| Claim type | First stop |
|---|---|
| Diagnostic / recognition | `mechanism-overview.md`, `recognition-architecture.md` |
| Pathology / histology | `idiopathic-pathology-memo.md`, `tissue-marker-boundary-memo.md` |
| Treatment (practical) | `treatment-evidence-memo.md`, `treatment-hierarchy-feline-primary-memo-20260417.md` |
| Treatment (translational) | `translation-brief.md`, `treatment-branch-comparison-memo.md` |
| Regulatory | `regulatory-brief.md`, `ibd-treatment-product-archetype-memo.md` |
| Endpoint / biomarker | `endpoint-handbook.md`, `support-and-frontier-marker-memo.md` |
| Boundary (IBD vs lymphoma) | `ibd-lymphoma-boundary-memo.md` |

**2. Check the source index**

- [IBD source index](ibd-source-index.md) — find the exact source card the claim is supposed to rest on

**3. Check the source card**

Source cards are in `raw/papers/`. Each has explicit `quoted_fact`, `source_supported_conclusion`, and `llm_inference` sections. Verify which category the original claim belongs to.

**4. Go to raw paper only if needed**

Raw papers are in `raw/papers/`. Only descend here if the source card is ambiguous or if you are verifying a direct quotation.

---

## Recurring Question Templates

These are the questions that keep appearing in IBD verification. Use them as starting probes.

**"Is this treatment claim feline-primary?"**
→ Check src-ibd-014 (diet, feline-primary), src-ibd-021 (overview, cross-species), src-ibd-005 (MSC, mouse only)
→ If it does not trace to src-ibd-014 or a similarly direct feline study, label it as context-layer or llm_inference

**"How strong is the diet-first recommendation?"**
→ Go to [treatment-hierarchy-feline-primary-memo-20260417.md](ibd-treatment-hierarchy-feline-primary-memo-20260417.md)
→ Step 1, medium-high confidence, feline-primary anchor via src-ibd-014
→ Conservative framing: "diet-first chronic-enteropathy management" not "IBD cure"

**"Can I say prednisolone is the preferred drug for feline IBD?"**
→ No — specific immunomodulatory drug ranking is not yet settled by feline-primary sources
→ Correct framing: "immunomodulatory management is step 2 when dietary response is insufficient" `[source_supported_conclusion: src-ibd-021]`

**"Is this claim about treatment or about diagnosis?"**
→ Use the Pitfall 1 test above
→ Strong diagnostic evidence does not strengthen treatment claims

**"Does this claim belong in the IBD module or the lymphoma module?"**
→ Go to [ibd-lymphoma-boundary-memo.md](ibd-lymphoma-boundary-memo.md) first
→ If the claim is about chlorambucil or small-cell intestinal lymphoma, the boundary must be explicit

**"Has this treatment been shown to work in cats specifically?"**
→ Go to source index, check disease-specific tags
→ Only src-ibd-014 has clean feline-primary treatment evidence in the current vault

---

## Quick Reference: IBD Verification Hierarchy

```
Topic pages (start here)
  ├─ mechanism-overview.md
  ├─ recognition-architecture.md
  ├─ translation-brief.md
  └─ current-state-dashboard.md

System memos (next level)
  ├─ treatment-hierarchy-feline-primary-memo-20260417.md ← NEW, use for treatment claims
  ├─ treatment-evidence-memo.md
  ├─ treatment-branch-comparison-memo.md
  ├─ treatment-product-archetype-memo.md
  ├─ diagnostic-workup-memo.md
  ├─ idiopathic-pathology-memo.md
  ├─ tissue-marker-boundary-memo.md
  ├─ ibd-lymphoma-boundary-memo.md
  └─ support-and-frontier-marker-memo.md

Source index
  └─ ibd-source-index.md

Source cards (raw/papers/)
  ├─ src-ibd-014.md  ← feline-primary diet treatment
  ├─ src-ibd-021.md  ← broad therapeutic overview
  └─ src-ibd-005.md  ← MSC translational (mouse)

Raw papers (raw/) — last resort
```

---

## What This Page Does Not Replace

- [verify-a-claim.md](verify-a-claim.md) — cross-disease claim lookup methodology
- [IBD source index](ibd-source-index.md) — full source list
- Individual source cards and deep extraction pages

---

## When To Use This Page vs verify-a-claim.md

| Situation | Use |
|---|---|
| Need the general claim-layer framework | verify-a-claim.md |
| Need IBD-specific pitfall checks | this page |
| Need the IBD treatment ladder | this page → treatment-hierarchy-feline-primary-memo |
| Need to check a specific source | ibd-source-index.md → source card |
| Need the IBD/lymphoma boundary call | ibd-lymphoma-boundary-memo.md |
