---
id: system-hcm-second-wave-owner-map-20260417
type: system
topic: hcm
species: feline
disease: HCM
question_type: densification
language: en
last_compiled_at: 2026-04-17
confidence: high
verification_status: compiled
decision_grade: stable
language_qa_status: light_checked
owner: codex
status: active
---

# HCM Second-Wave Owner Map, 2026-04-17

## Purpose

This page addresses the P3 densification gap:

> biomarker / AI / treatment branch 再压出一层更窄 owner

The prior HCM memos correctly describe the branch architecture. They all correctly end with "no final ranking yet." The gap is that none of them name the specific question that, when answered, declares the branch second-wave complete.

This page fixes that. For each of the three main thin branches (biomarker, AI, treatment), it names:
1. The single narrowest owner question
2. What already exists and can be held
3. What specific next piece would move the branch from "second-wave in progress" to "second-wave complete"
4. The source(s) that are the primary carrier of the gap

---

## Branch 1: Biomarker

**Existing memos:** `hcm-biomarker-use-case-memo.md`, `hcm-endpoint-separation-memo.md`

**What already holds:**
- Troponin I = injury/burden signal (src-hcm-006)
- NT-proBNP = severe-disease flag + bounded screening augmentation (src-hcm-010)
- Novel biomarkers = frontier stratification layer (src-hcm-017)
- Flat biomarker ranking is not safe

**The gap — stated precisely:**

The existing memo correctly separates use cases. What it cannot yet do:

> `In what clinical situation does NT-proBNP outperform troponin as a first-line screening augmentation tool, and where does troponin add more than NT-proBNP?`

That is the one question that would move this branch from "use-case separated" to "conditionally ranked." Right now the vault has use-case lanes but not conditional ranking logic.

**Narrowest owner question:**

`What is the conditional superiority case for NT-proBNP vs troponin across the mild / moderate / severe disease spectrum in feline HCM?`

**Source that carries the gap:** src-hcm-010 (NT-proBNP boundary scope), src-hcm-006 (troponin use-case detail). A second-pass read of both against the conditional-ranking question would likely extract the answer or confirm it is not yet in the source set.

**Second-wave complete when:**
- Conditional ranking logic exists (even if provisional) for NT-proBNP vs troponin by disease stage
- OR confirmed that the current source set does not support it (that is also a closed answer — it means the gap stays as a named open question, not an architectural uncertainty)

**Current state:** second-wave in progress

---

## Branch 2: AI Augmentation

**Existing memo:** `hcm-ai-augmentation-boundary-memo.md`

**What already holds:**
- AI is augmentation-class, not replacement-class (src-hcm-023)
- AI belongs below structural phenotype confirmation
- Augmentation-versus-replacement is the current governing boundary

**The gap — stated precisely:**

The AI boundary memo correctly says AI should stay in "bounded augmentation." What it cannot yet do:

> `What type of clinical workflow input makes AI most useful — screening triage, follow-up rate monitoring, or phenotype borderline adjudication?`

Without naming a specific workflow position, AI remains a "bounded augmentation" label without a slot in the actual workup sequence. The boundary is correct; the insertion point is still floating.

**Narrowest owner question:**

`Where in the feline HCM diagnostic workup sequence does AI augmentation add the most value — at initial screening, at severity monitoring, or at phenotype-borderline cases?`

**Source that carries the gap:** src-hcm-023 (AI augmentation depth). A focused re-read with the workflow-position question would likely extract the insertion point or confirm it is not resolved in the source.

**Second-wave complete when:**
- AI has a named insertion point in the workup sequence (even provisional: "most useful at screening-triage step" or "most useful at borderline-phenotype adjudication")
- OR confirmed that src-hcm-023 does not resolve this — making it a named open question in the AI boundary memo

**Current state:** second-wave in progress

---

## Branch 3: Treatment

**Existing memos:** `hcm-treatment-evidence-memo.md`, `hcm-treatment-branch-comparison-memo.md`

**What already holds:**
- Branch 1: Bounded management anchor (src-hcm-008) — safest routine framing
- Branch 2: Selective targeted frontier (src-hcm-011, src-hcm-020)
- Branch 3: Older conventional therapy (src-hcm-014)
- Branch 4: Evidence skepticism (src-hcm-015) — embedded structural feature

**The gap — stated precisely:**

The treatment memos correctly name the skepticism anchor. What they cannot yet do:

> `At what stage in the disease progression (preclinical / compensated / overt heart failure) does evidence skepticism apply most strongly vs least strongly?`

Right now skepticism is correctly modeled as a structural feature of the whole branch. But it is applied uniformly. A more useful second-wave version would say: "skepticism is most load-bearing at stage X, least load-bearing at stage Y."

**Narrowest owner question:**

`How does treatment evidence quality vary across the feline HCM disease-stage spectrum — preclinical, compensated, overt CHF — and which stage carries the highest uncertainty?`

**Source that carries the gap:** src-hcm-015 (evidence skepticism scope), src-hcm-008 (bounded management range). A targeted re-read against the stage-specific skepticism question would likely identify where the evidence is most vs least settled.

**Second-wave complete when:**
- Stage-specific treatment confidence exists (even provisional: "evidence most uncertain at preclinical stage" or "management evidence strongest at overt CHF stage")
- OR confirmed that src-hcm-015 and src-hcm-008 do not support stage-stratification — making it a named open question in the treatment evidence memo

**Current state:** second-wave in progress

---

## What This Owner Map Changes

| Branch | Before this memo | After this memo |
|---|---|---|
| Biomarker | "no flat ranking safe" | Narrowest open question named: NT-proBNP vs troponin conditional ranking by stage |
| AI | "bounded augmentation" | Narrowest open question named: workflow insertion point (screening vs monitoring vs borderline) |
| Treatment | "evidence skepticism embedded" | Narrowest open question named: stage-specific skepticism weight (preclinical vs compensated vs CHF) |

**The gap was not architectural — it was that no one had named the floor.**

Each branch now has a single sentence that says: close this, and the branch moves from second-wave in progress to second-wave complete.

---

## Operator Rule For Each Branch

For each of the three branches, the next operator action is the same:

1. Do a targeted re-read of the primary source(s) listed against the narrowest owner question
2. Either extract the answer (even provisional), or confirm it is not in the source
3. If extracted: write a one-page provisional answer memo, update the branch memo, update the dashboard
4. If not in source: name the open question explicitly in the branch memo; that closes the gap by converting uncertainty to named ignorance

Named ignorance is closed. Unnamed ignorance is not.

---

## Branch Status Summary

| Branch | Primary carrier sources | Narrowest owner question | Status |
|---|---|---|---|
| Biomarker | src-hcm-006, src-hcm-010 | NT-proBNP vs troponin conditional ranking by disease stage | second-wave in progress |
| AI | src-hcm-023 | Workflow insertion point: screening vs monitoring vs borderline | second-wave in progress |
| Treatment | src-hcm-015, src-hcm-008 | Stage-specific skepticism weight: preclinical vs compensated vs CHF | second-wave in progress |

---

## What This Memo Does Not Replace

- [HCM biomarker use-case memo](hcm-biomarker-use-case-memo.md)
- [HCM AI augmentation boundary memo](hcm-ai-augmentation-boundary-memo.md)
- [HCM treatment evidence memo](hcm-treatment-evidence-memo.md)
- [HCM treatment-branch comparison memo](hcm-treatment-branch-comparison-memo.md)

Those memos remain the structural anchors. This memo adds the resolution layer on top.

---

## Linked Pages

- [HCM current state dashboard](../../topics/hcm/current-state-dashboard.md) — update "Still Thin" section to reflect named owner questions
- [feline foundation densification queue](feline-foundation-densification-queue-20260416.md) — P3 gate
