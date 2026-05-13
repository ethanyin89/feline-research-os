---
id: inbox-content-precision-promotion-batch-20260506
type: inbox
topic: content-pipeline
question_type: workflow
language: bilingual
last_compiled_at: 2026-05-06
verification_status: provisional
decision_grade: no
language_qa_status: light_checked
owner: codex
status: processed
---

# Content Precision Promotion Batch, 2026-05-06

## Classification

`方案 + 内容处理`

This batch follows:

- [content precision promotion workflow](../system/indexes/content-precision-promotion-workflow.md)

It does not directly edit canonical disease truth pages. It stages promotion decisions first.

## Candidates

| # | Disease | Object | Precision Type | Source Anchors | Decision | Target Surfaces |
|---|---|---|---|---|---|---|
| 1 | FIP | `fip-neurologic-workup-branch-boundary-memo.md` | workup | `src-fip-023`, `src-fip-003`, `src-fip-015` | `partial-promote / status-sync` | `risk-and-recognition`, `recognition-architecture`, dashboard |
| 2 | FIP | `fip-neurologic-rescue-boundary-memo.md` | treatment-order | `src-fip-024`, `src-fip-016`, `src-fip-019` | `partial-promote / status-sync` | `translation-brief`, dashboard, output claims |
| 3 | IBD | `ibd-best-overall-vs-route-cleaner-archetype-memo.md` | route-fit | `src-ibd-014`, `src-ibd-021`, product-archetype memo | `partial-promote / status-sync` | `regulatory-brief`, dashboard |
| 4 | FIP | `fip-antiviral-product-archetype-route-boundary-memo.md` | official-source | regulatory source pack + FIP treatment worksheets | `needs source access` | regulatory brief, route memos |
| 5 | FIP | non-CSF assay-performance gap | assay | `src-fip-023`, `src-fip-010`, `src-fip-022`, assay memo | `hold` | endpoint / recognition control layer |
| 6 | IBD | jurisdiction-specific route interpretation | official-source | `src-ibd-014`, `src-ibd-021`, regulatory page | `needs source access` | IBD regulatory brief |

## Decisions

### 1. FIP Neurologic Workup Branch Boundary

Source check:

- `src-fip-023` supports the key branch rule: CSF RT-PCR has strong positive branch-specific value, but overall sensitivity and NPV prevent generic rule-out or first-line use.
- The current extracted numbers are specificity `100%`, PPV `100%`, overall sensitivity `42.1%`, NPV `57.7%`, and neurologic/ocular sensitivity `85.7%`.
- `topics/fip/risk-and-recognition.md` already absorbs the rule: neurologic/ocular signs shift the case before CSF support becomes central.
- `topics/fip/current-state-dashboard.md` already lists the neurologic-workup boundary as a usable control owner.

Decision:

`partial-promote / status-sync`

What to promote:

- No new broad content needed.
- Future canonical edit should only tighten status wording if a target page drifts.
- The core rule is already present: CSF support is downstream of neurologic/ocular branch shift.

What not to say:

- Do not say CSF RT-PCR is the best general FIP diagnostic test.
- Do not use negative CSF support to broadly exclude FIP.
- Do not backflow CSF specificity into ordinary suspicion-building.

Write-back target:

- No immediate canonical edit required.
- Keep as a control layer for future recognition / endpoint edits.

### 2. FIP Neurologic Rescue Boundary

Source check:

- `src-fip-024` is neurologic-treatment specific, not a generic FIP treatment paper.
- It supports higher-dose / high-monitoring / relapse-sensitive branch framing.
- `src-fip-016` remains the baseline natural-disease treatment anchor and explicitly excludes severe neurologic and ocular cases.
- `src-fip-019` supports a real-world remdesivir-plus-GS package branch but does not replace neurologic-specific evidence.
- `topics/fip/translation-brief.md` already absorbs the boundary: neurologic rescue and package logic should not collapse into baseline GS efficacy.
- `topics/fip/current-state-dashboard.md` already lists the neurologic-rescue boundary as usable.

Decision:

`partial-promote / status-sync`

What to promote:

- Use the neurologic rescue memo as the default control layer for any output claim that tries to describe FIP antiviral outcomes.
- Future output review should check for accidental flattening of baseline GS, remdesivir package logic, and neurologic rescue.

What not to say:

- Do not use neurologic rescue as ordinary baseline treatment efficacy.
- Do not convert rescue success into whole-branch cure rate.
- Do not erase relapse, higher-dose, or monitoring burden.

Write-back target:

- No immediate canonical page edit required.
- Next output-specific review should inspect FIP briefing/dossier/slides for this flattening risk.

### 3. IBD Best-Overall Vs Route-Cleaner Archetype

Source check:

- `src-ibd-014` supports hydrolysed diet response as the cleanest current practical treatment anchor, with food-responsive / chronic-enteropathy overlap.
- `src-ibd-021` supports broader treatment-landscape framing but remains subordinate to feline-primary evidence.
- `ibd-treatment-product-archetype-memo.md` and `ibd-claim-fit-route-fit-boundary-memo.md` already separate claim-fit from route-fit.
- `topics/ibd/regulatory-brief.md` already says the regulatory branch is clearer as `best overall archetype` versus `future route-cleaner archetype`.
- `topics/ibd/current-state-dashboard.md` already lists the best-overall versus route-cleaner memo as usable.

Decision:

`partial-promote / status-sync`

What to promote:

- Keep both winner statements visible:
  - diet-first chronic-enteropathy management = best overall archetype now
  - broad medical-management = future route-cleaner candidate

What not to say:

- Do not say medicine-style management is evidence-superior now.
- Do not say diet-first is already the cleanest route-fit branch.
- Do not move into jurisdiction recommendation.

Write-back target:

- No immediate canonical edit required.
- Use as a control layer for future IBD regulatory or output edits.

### 4. FIP Antiviral Product-Archetype Route Boundary

Source check:

- Existing local regulatory source pack supports framework-level China / USA / EU / UK framing.
- FIP treatment worksheets support product-object separation:
  - baseline GS-441524 product
  - remdesivir plus GS package
  - neurologic / high-complexity branch
  - remission durability layer
- `topics/fip/regulatory-brief.md` already absorbs this structure and names the next live gaps.

Decision:

`needs source access`

What to promote:

- Nothing further until current official-source checks are done.

What not to say:

- Do not claim a current U.S. approved-record status without checking official FDA records dated to the current run.
- Do not claim office-stock nomination/list status without official-source confirmation.
- Do not claim EMA Article 23 eligibility from framework text alone.
- Do not recommend a first jurisdiction.

Write-back target:

- Stage a separate official-source batch for:
  - current Animal Drugs @ FDA / Green Book check for FIP antiviral entries
  - GS-441524 office-stock nomination / list-status check
  - EMA Article 23 eligibility screen for baseline GS-441524 FIP indication

### 5. FIP Non-CSF Assay-Performance Gap

Source check:

- `src-fip-023` has extractable CSF performance figures.
- `src-fip-010` and `src-fip-022` support mutation utility/limitation structure, but not a comparable cross-assay numeric performance table at the current extraction layer.
- `topics/fip/current-state-dashboard.md` already says non-CSF assay performance detail remains thin.

Decision:

`hold`

What to promote:

- Keep current assay boundary language.
- Promote no numeric leaderboard.

What not to say:

- Do not compare CSF, mutation assays, serology, and acute-phase markers as if all have comparable extracted sensitivity/specificity data.
- Do not write `molecular tests are best`.

Write-back target:

- None until full-text non-CSF assay performance extraction exists.

### 6. IBD Jurisdiction-Specific Route Interpretation

Source check:

- Current IBD regulatory branch is product-type-first only.
- `src-ibd-014` supports diet-first practical treatment framing but does not make jurisdiction logic safe.
- `src-ibd-021` supports broad treatment-landscape context but remains weaker than feline-primary anchors.
- `topics/ibd/regulatory-brief.md` explicitly says no jurisdiction-specific route analysis is ready yet.

Decision:

`needs source access`

What to promote:

- Nothing jurisdiction-specific.

What not to say:

- Do not recommend route or jurisdiction.
- Do not treat diet-first practical strength as regulatory readiness.
- Do not treat future medicine-style route cleanliness as current evidence superiority.

Write-back target:

- Future official-source regulatory source pack for IBD, only if route-level pressure becomes real.

## Batch Read

This batch did not find a need for immediate canonical disease-page edits.

The stronger finding is cleaner:

1. Several second-wave owners are already absorbed by target pages.
2. FIP and IBD regulatory branches should not move further without current official-source checks.
3. FIP assay ranking should stay held until non-CSF performance detail is comparable.
4. The next valuable content batch should be `official-source precision`, not another memo-writing pass.

## Health Check Read

Should this become a recurring check?

Not yet.

Reason: the promotion judgments here are still content-review decisions. The mechanical part that could become a health check later is narrower:

- flag when a dashboard says an owner is usable but the target topic page does not link it
- flag when a regulatory page has `next expansion targets` older than a threshold
- flag when a page contains route-recommendation language without official-source anchors

Do not cron automatic promotion.

## Approval Gate

Recommended next action after approval:

Run an official-source precision batch for FIP regulatory current status:

1. current Animal Drugs @ FDA / Green Book check for FIP antiviral entries
2. GS-441524 office-stock nomination / list-status check
3. EMA Article 23 eligibility screen for baseline GS-441524 FIP indication

## Processing Record

**Processed: 2026-05-07**

The recommended official-source precision batch has been completed:

| Item | Status | Result |
|------|--------|--------|
| FDA Animal Drugs / Green Book | ✅ Done (2026-05-06) | No FDA-approved FIP antivirals |
| GS-441524 office-stock | ✅ Done (2026-05-06) | Not authorized; patient-specific only |
| EMA Article 23 | ✅ Done (2026-05-07) | Cats are major species; FIP eligibility via "infrequent disease" criterion |
| China implementing notices | ✅ Done (2026-05-07) | No approved FIP antivirals; GS-441524 sales illegal |
| UK route mapping | ✅ Done (2026-05-07) | Legal since 2021 via Bova Specials UK |

All findings written to `topics/fip/regulatory-brief.md`.

This inbox file can be archived.

