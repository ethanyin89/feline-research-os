---
id: system-fip-regulatory-jurisdiction-split-memo-20260417
type: system
topic: fip
species: feline
disease: FIP
question_type: regulatory
language: en
last_compiled_at: 2026-04-17
confidence: medium
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
source_ids:
  - src-reg-001
  - src-reg-002
  - src-reg-003
  - src-reg-004
  - src-reg-005
  - src-reg-006
  - src-reg-007
  - src-reg-008
  - src-reg-009
---

# FIP Regulatory Jurisdiction Split Memo, 2026-04-17

## Purpose

This memo fulfills the P1 minimum completion standard from the densification queue:

> 至少出现一张 jurisdiction-aware regulatory memo，不再只是 stop-sign page

It is the first jurisdiction-split analysis for FIP regulatory pathways. It does not yet constitute a submission-grade route memo. It converts the current `regulatory-brief.md` from a stop-sign page into the first structured, source-anchored jurisdiction analysis.

## What Makes FIP Regulatorily Distinct From CKD

FIP and CKD share the same regulatory source pack but the disease context is sharply different.

| Dimension | CKD | FIP |
|---|---|---|
| Disease course | Chronic, manageable | Rapidly fatal without treatment |
| Treatment goal | Slow progression | Cure or long-term remission |
| Product class | Renoprotective agents | Antivirals (GS-441524, GC376) |
| Unmet-need argument | Moderate | Strong |
| Placebo ethics | Feasible in early stage | Ethically difficult in advanced disease |

These differences change how the regulatory frameworks apply, even when the frameworks are the same.

## Jurisdiction Analysis

### China (src-reg-001, src-reg-002, src-reg-003)

**Regulatory anchor:** Ministry-level registration (兽药注册办法). All new veterinary drugs and imported veterinary drugs require formal registration. Post-registration, a separate product approval number (批准文号) is required before manufacture.

**FIP-specific reading:**

- The path bifurcates early on domestic vs imported product logic. `[source_supported_conclusion: src-reg-001, src-reg-003]`
- Registration requires completed clinical trials before formal submission. For FIP antivirals, clinical evidence already exists in the scientific literature, which could support an expedited dossier assembly. `[source_supported_conclusion: src-reg-001]`
- The two-step logic (registration + approval-number) means commercial manufacture readiness is a separate gate from regulatory clearance. `[source_supported_conclusion: src-reg-002]`
- China's companion animal regulatory channel is a formal path, not an informal shortcut. `[source_supported_conclusion: src-reg-001]`

**Provisional working frame:** `[llm_inference]`

Of the four jurisdictions covered here, China appears most structurally ready to process a first FIP antiviral dossier, given: (a) formal veterinary registration channel exists, (b) clinical evidence base in the literature is substantial, (c) unmet-need case is strong. Jurisdiction-specific implementing notices and companion animal dossier guidance have not yet been ingested and represent the next densification target for this branch.

**Open gaps:**

- No China companion animal efficacy package standard yet ingested
- Domestic vs imported product pathway distinction not yet mapped for FIP antiviral archetype
- Implementing notices beyond the three core regulations not yet covered

---

### USA (src-reg-004, src-reg-005, src-reg-006)

**Regulatory anchor:** FDA CVM full approval vs conditional approval fork (src-reg-004). Cats are a major species (src-reg-005), so conditional approval is not a default fallback.

**FIP-specific reading:**

- Full approval requires substantial evidence of effectiveness. `[quoted_fact: src-reg-004]`
- Conditional approval requires reasonable expectation of effectiveness plus a qualifying statutory basis. `[quoted_fact: src-reg-004, src-reg-005]`
- For major species (including cats), expanded conditional approval must rest on serious or life-threatening conditions or unmet health needs where effectiveness studies would be complex or particularly difficult. `[quoted_fact: src-reg-005]`
- FIP is a rapidly fatal disease in untreated cats. This is a stronger unmet-need and disease-seriousness case than most companion animal indications, and could plausibly support the conditional approval statutory basis — but eligibility must be tested explicitly. `[source_supported_conclusion: src-reg-004, src-reg-005]`
- If full approval is pursued, active-control study design may become relevant: withholding proven FIP treatment from a placebo group raises ethical issues, which is exactly the scenario where GFI #204 active-control logic becomes important. `[source_supported_conclusion: src-reg-006]`

**Provisional working frame:** `[llm_inference]`

The U.S. FIP pathway should be modeled as a conditional-approval eligibility test first. If FIP meets the major-species conditional approval threshold (serious/life-threatening + difficult studies), this is faster than full approval. If not, an active-controlled full-approval path is the fallback, with study ethics as a key design constraint.

**Open gaps:**

- No FDA FIP-specific guidance ingested
- No assessment of FDA prior advisory committee precedent for antiviral FIP products
- Active-control feasibility under GFI #204 not yet mapped to FIP trial design

---

### EU (src-reg-007)

**Regulatory anchor:** EMA limited-market route under Article 23 of Regulation (EU) 2019/6 (src-reg-007). Provides reduced data requirements for products intended for veterinary limited markets.

**FIP-specific reading:**

- The EU branch should test limited-market eligibility early, because it may materially reduce the data package expected. `[source_supported_conclusion: src-reg-007]`
- The guideline became effective 20 September 2024. `[quoted_fact: src-reg-007]`
- A feline-only indication for an antiviral with limited commercial scale could plausibly fit limited-market logic, but eligibility must be checked explicitly rather than assumed. `[source_supported_conclusion: src-reg-007]`

**Provisional working frame:** `[llm_inference]`

EU strategy for a FIP antiviral should evaluate two branches in parallel: (1) whether the Article 23 limited-market route applies, and (2) standard route with orphan-medicine-adjacent framing. If limited-market eligibility holds, this may be the most evidence-efficient EU entry point. This has not yet been confirmed against EMA product-specific criteria.

**Open gaps:**

- No EMA FIP-specific precedent cases ingested
- Article 23 eligibility criteria not yet applied to FIP antiviral indication explicitly
- No EU efficacy package guidance for antiviral companion animal products ingested

---

### UK (src-reg-008, src-reg-009)

**Regulatory anchor:** VMD marketing authorisation guidance (src-reg-008) plus Annex 2 Section I dossier requirements (src-reg-009).

**FIP-specific reading:**

- The UK branch requires route-selection as an early decision, not a generic single pathway. Five MA routes exist. `[source_supported_conclusion: src-reg-008]`
- For initial UK planning, a GB-focused frame may be simpler than trying to solve all jurisdictional variants at once. `[source_supported_conclusion: src-reg-008]`
- Dossier structure must align with current veterinary medicinal knowledge and relevant quality, safety, and efficacy guidelines. `[quoted_fact: src-reg-009]`

**Provisional working frame:** `[llm_inference]`

The UK path for a FIP antiviral should start with GB national route selection. Post-Brexit, the UK is no longer covered by EMA procedures except for Northern Ireland under certain conditions. A GB-first frame isolates the simpler case. Dossier planning should use the internal FIP evidence base early, since Annex 2 alignment can in principle begin before a formal application is prepared.

**Open gaps:**

- UK-specific efficacy guidance for companion animal antivirals not yet ingested
- The five MA routes not yet mapped to FIP antiviral archetype
- Post-Brexit alignment between UK and EU dossier logic not yet examined

---

## Cross-Jurisdiction Summary

| Jurisdiction | Framework type | FIP-specific advantage | Key open gap |
|---|---|---|---|
| China | Two-step ministry registration | Formal companion animal channel; strong unmet-need case | Companion animal dossier implementing notices |
| USA | Full vs conditional approval fork | FIP disease seriousness may meet conditional-approval threshold | FDA FIP-specific precedent |
| EU | Standard + Article 23 limited-market option | Limited-market route may reduce data expectations | Article 23 eligibility not yet confirmed |
| UK | Route-selection + Annex 2 dossier | GB-first frame isolates simplest path | UK-specific antiviral efficacy guidance |

## Confidence Assessment

This memo is provisional at medium confidence. All source anchors are real regulatory texts. FIP-specific pathway conclusions are source_supported_conclusions where the regulatory logic is directly applied to FIP disease characteristics, and llm_inference where product-specific or precedent-specific judgments are involved. No submission-grade pathway decisions should be made from this memo alone.

## Minimum Completion Standard: Met

This memo fulfills the P1 densification queue requirement:
- ✓ At least one jurisdiction-aware regulatory memo exists
- ✓ No longer only a stop-sign page
- ✓ Four jurisdictions covered with source anchors
- ✓ FIP-disease-specific framing applied to each

## What This Memo Does Not Replace

- Submission-grade route memo
- Product-archetype analysis (GS-441524 vs GC376 specific regulatory handling)
- FDA advisory committee precedent analysis
- EMA Article 23 eligibility confirmation
- China companion animal implementing notice deep-read

## Next Densification Target for This Branch

1. China companion animal dossier implementing notices (most operationally actionable)
2. FDA conditional approval eligibility test for FIP (unmet-need framing)
3. EMA Article 23 eligibility check for feline antiviral indication

## Linked Pages

- [FIP regulatory brief](../../topics/fip/regulatory-brief.md) — parent page, now superseded from stop-sign to linked memo
- [regulatory source index](regulatory-source-index.md)
- [FIP treatment evidence memo](fip-treatment-evidence-memo.md)
