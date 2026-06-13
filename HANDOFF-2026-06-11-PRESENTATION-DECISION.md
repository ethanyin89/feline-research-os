# Handoff: Presentation Logic Decision Lock-In

**Date:** 2026-06-11  
**Branch:** `idea-chatacademia-research-workbench`  
**Context:** `/autoplan` review for presentation logic

---

## Current Decision

The user chose **A** after the CEO review gate.

That locks in the following direction:

- Do **not** ship a global answer-level `high | medium | low` trust badge as V1.
- Reframe presentation around **claim / evidence / boundary / gap / decision implication**.
- Treat `confidence` as an **evidence profile**, not a universal answer quality score.
- Keep the pilot narrow and prove the semantics before turning it into a reusable skill.

This is the key outcome of the review: the old trust badge only reflected provenance-tag ratios, not actual evidence quality.

---

## What Changed

The plan file was updated to reflect the new direction:

- `PLAN-page-rendering-improvements.md`

The plan now centers on:

- `ResultPresentation.evidence_profile`
- `SourceDisplay`
- three surface modes:
  - Overview / What-Is
  - Ranked Evidence / Decision Support
  - Ask the Vault response

It also explicitly records:

- the CEO premise challenge
- the user choice of A
- the rejection of answer-level trust badges as a V1 surface

---

## What the Next Session Should Do

1. Start from `PLAN-page-rendering-improvements.md`.
2. Decide whether the first pilot surface should be:
   - Ask the Vault, or
   - a more defensible decision-support surface first
3. Implement only the narrow evidence-profile presentation flow.
4. Verify the surface with a small set of samples before considering skillification.
5. Do not reintroduce a global `high | medium | low` trust badge unless there is a real graded-evidence model behind it.

---

## Files to Read First

- [`PLAN-page-rendering-improvements.md`](PLAN-page-rendering-improvements.md)
- [`HANDOFF-2026-06-11-PRESENTATION-LAYER.md`](HANDOFF-2026-06-11-PRESENTATION-LAYER.md)
- [`HANDOFF-2026-06-11-PRESENTATION-SAMPLES.md`](HANDOFF-2026-06-11-PRESENTATION-SAMPLES.md)

---

## Notes for Handoff Continuity

- The project is currently about **presentation logic**, not visual restyling.
- The defensible unit is the evidence chain, not a single answer-level score.
- The reusable skill should come **after** the pilot works, not before.

