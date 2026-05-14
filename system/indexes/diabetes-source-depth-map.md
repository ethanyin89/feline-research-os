---
id: diabetes-source-depth-map
type: index
topic: system
question_type: navigation
language: bilingual
last_compiled_at: 2026-05-14
confidence: medium
verification_status: compiled
owner: codex
status: active
---

# Source Depth Map — Diabetes

## 用途 / How to Use

**为了快速找到该深挖哪些 Diabetes source card：** 先读 remission、SGLT2、obesity/diet、clinical overview、insulin protocol cards。
**为了在 context 有限时决定先读哪张：** Diabetes 24/24 paper source cards 已经都是 `full`；优先读 Tier 1，再读 Tier 2，最后读 Tier 3 edge-context rows。
**为了指导下一步 densification 工作：** 不再做普通 source-card thickening；只在会改变 treatment branch、monitoring gate、regulatory boundary、remission endpoint 时补 full-text 或 regulatory depth。

Depth definitions:

- **full**: source card explicitly says `extraction_depth: full`
- **partial**: source card explicitly says `extraction_depth: partial`
- **stub**: missing usable extraction body or source-card state

Verification-status overlay:

| verification_status | Count | Read |
|---|---:|---|
| deep_extracted | 24 | Diabetes still has a clean deep-extracted seed-corpus overlay. The remaining seed-corpus gap is branch-order compression, protocol comparison, and output-level clinical/regulatory precision. |
| abstract_weighted | 59 | The 2026-05-14 full source-check found Crossref abstracts for 59 diabetes extension cards; these cards can guide navigation and extraction priority, not topic-page claims. |
| title_only | 35 | The remaining diabetes extension cards lack Crossref abstract text or a resolvable DOI in this pass. They remain first-pass intake cards only. |

---

## Tier 1 — OUTPUT-CONTROLLING ANCHORS

| Source ID | Title (short) | Current Role | Words | Depth | Priority | Key Gap |
|---|---|---|---:|---|---|---|
| src-diabetes-007 | Diabetic remission systematic review | remission boundary | 745 | **full** | HIGH | full source-card depth exists and is now deep-extracted; stronger remission-rate tables still need tighter topic/output compression |
| src-diabetes-011 | SGLT2 inhibitor management | SGLT2 treatment / safety branch | 744 | **full** | HIGH | full source-card depth exists and label-control links added; full text needed for protocol comparison |
| src-diabetes-005 | Obese diabetic cat | obesity / body-condition sequencing | 793 | **full** | HIGH | full source-card depth exists for obesity/body-condition sequencing and is now deep-extracted; sequencing guidance still needs tighter output compression |
| src-diabetes-006 | Diet prevention and management | diet architecture overview | 705 | **full** | HIGH | full source-card depth exists for cross-stage diet architecture and is now deep-extracted; stronger stage-specific outputs still need compression |
| src-diabetes-014 | Feline diabetes clinical overview | clinical workup overview | 713 | **full** | HIGH | broad clinical overview now has full source-card depth and deep-extracted status for workup architecture; protocol-level compression still needs work |
| src-diabetes-024 | Glargine U300 treatment | insulin protocol branch | 711 | **full** | HIGH | insulin branch now has full source-card depth and deep-extracted status for IGla-U300 promise/boundary logic; protocol comparison still needs compression |

---

## Tier 2 — IMPORTANT BRANCH ANCHORS

| Source ID | Title (short) | Current Role | Words | Depth | Priority | Key Gap |
|---|---|---|---:|---|---|---|
| src-diabetes-001 | Pathogenesis review | pathogenesis spine | 701 | **full** | MEDIUM | full source-card depth exists and is now marked deep_extracted for mechanism spine |
| src-diabetes-013 | Hypersomatotropism / acromegaly / hyperadrenocorticism | endocrine-secondary boundary | 706 | **full** | MEDIUM | full source-card depth exists for secondary-endocrine gate and is now deep-extracted; routing compression still needs work |
| src-diabetes-020 | Hypersomatotropism-induced diabetes | endocrine-secondary detail | 712 | **full** | MEDIUM | full source-card depth exists for HST difficult-control branch and is now deep-extracted; stronger candidate-routing outputs still need compression |
| src-diabetes-010 | Diabetes and pancreatitis | pancreatitis comorbidity | 711 | **full** | MEDIUM | full source-card depth exists for pancreatitis/DKA complexity gate and is now deep-extracted; management detail still needs compression |
| src-diabetes-015 | Low-carb/low-fiber vs moderate-carb/high-fiber diets | diet comparison | 707 | **full** | MEDIUM | full source-card depth exists for diet-comparison branch and is now deep-extracted; comparison outputs still need tighter compression |
| src-diabetes-022 | High-protein diet management | diet/treatment study | 708 | **full** | MEDIUM | full source-card depth exists for high-protein/low-carbohydrate branch and is now deep-extracted; treatment comparison still needs compression |
| src-diabetes-009 | UK prevalence / risk factors | epidemiology / risk | 725 | **full** | MEDIUM | full source-card depth exists for UK risk map, denominator-bound |
| src-diabetes-012 | Australia frequency / breed predisposition | epidemiology / breed risk | 702 | **full** | MEDIUM | full source-card depth exists for Australian breed-risk anchor, denominator-bound |
| src-diabetes-004 | Neurological complications | neuropathy complication | 701 | **full** | MEDIUM | full source-card depth exists for clinical/electrophysiologic neuropathy branch |
| src-diabetes-018 | Endoneurial microvascular pathology | neuropathy pathology | 700 | **full** | MEDIUM | full source-card depth exists for microvascular neuropathy branch |

---

## Tier 3 — CONTEXT / EDGE ANCHORS

| Source ID | Title (short) | Current Role | Words | Depth | Priority | Key Gap |
|---|---|---|---:|---|---|---|
| src-diabetes-002 | Pathogenesis review | older/parallel mechanism | 710 | **full** | LOW | full source-card depth exists for historical pathogenesis lineage and is now deep-extracted |
| src-diabetes-003 | Feline type-2 model | comparative model | 703 | **full** | LOW | full source-card depth exists for model-value boundary and is now deep-extracted |
| src-diabetes-008 | Alpha-glucosidase + low-carb diet | adjunct treatment | 700 | **full** | LOW | full source-card depth exists for adjunct/diet attribution boundary and is now deep-extracted |
| src-diabetes-016 | Low carbohydrate vs high fiber | diet framing | 704 | **full** | LOW | full source-card depth exists for diet-debate boundary and is now deep-extracted |
| src-diabetes-017 | New approaches | frontier treatment | 700 | **full** | LOW | full source-card depth exists for pre-SGLT2 frontier branch and is now deep-extracted |
| src-diabetes-019 | Special about feline diabetes | mechanism context | 700 | **full** | LOW | full source-card depth exists for species-specific boundary and is now deep-extracted |
| src-diabetes-021 | Diabetes mellitus in cats | clinical overview | 700 | **full** | LOW | full source-card depth exists for older clinical overview bridge and is now deep-extracted |
| src-diabetes-023 | Comparative occurrence / pancreatic disease | epidemiology / pancreatitis context | 720 | **full** | LOW | full source-card depth exists for cross-species context boundary and is now deep-extracted |

---

## Coverage Summary

| Disease | Total Source Cards | full | partial | stub | verification_status read | Coverage |
|---|---:|---:|---:|---:|---|---|
| Diabetes seed corpus | 24 | 24 | 0 | 0 | 24 deep_extracted | 100% full |
| Diabetes extension corpus | 94 | 0 | 94 | 0 | 59 abstract_weighted, 35 title_only | full source-check complete; 0% decision-grade |

---

## Immediate Queue

No Diabetes seed-corpus source-card partials remain. The extension corpus has 94 partial cards; 59 have Crossref abstract scope checks and 35 remain title-only queue objects. None of the extension cards are compiled evidence yet.

2026-05-13 source-check sample:

- upgraded to `abstract_weighted`: `src-diabetes-035`, `src-diabetes-050`, `src-diabetes-087`, `src-diabetes-091`
- remained `title_only` because Crossref had no abstract: `src-diabetes-046`
- report: [feline diabetes / obesity source-check sample](feline-diabetes-obesity-source-check-sample-20260513.md)

2026-05-14 full source-check:

- checked all 94 diabetes extension cards plus all 87 obesity cards
- diabetes extension result: 59 `abstract_weighted`, 35 `title_only`
- report: [feline diabetes / obesity full source-check](feline-diabetes-obesity-source-check-full-20260514.md)

2026-05-14 structured abstract sample:

- worksheets created for `src-diabetes-035`, `src-diabetes-050`, `src-diabetes-087`, and `src-diabetes-091`
- report: [feline diabetes / obesity structured abstract sample](feline-diabetes-obesity-structured-abstract-sample-20260514.md)
- cards remain `abstract_weighted`; no topic-page claims were promoted

2026-05-14 full structured abstract run:

- all 59 diabetes extension `abstract_weighted` cards now have abstract-only worksheets
- report: [feline diabetes / obesity structured abstract full index](feline-diabetes-obesity-structured-abstract-full-20260514.md)
- 35 diabetes extension cards remain `title_only` with no structured abstract worksheet

Completed on the 2026-04-21 Diabetes thickening pass:

1. Tier 1 output-controlling anchors: `src-diabetes-005`, `src-diabetes-006`, `src-diabetes-007`, `src-diabetes-011`, `src-diabetes-014`, `src-diabetes-024`
2. Tier 2 branch anchors: `src-diabetes-001`, `src-diabetes-004`, `src-diabetes-009`, `src-diabetes-010`, `src-diabetes-012`, `src-diabetes-013`, `src-diabetes-015`, `src-diabetes-018`, `src-diabetes-020`, `src-diabetes-022`
3. Tier 3 context / edge anchors: `src-diabetes-002`, `src-diabetes-003`, `src-diabetes-008`, `src-diabetes-016`, `src-diabetes-017`, `src-diabetes-019`, `src-diabetes-021`, `src-diabetes-023`

## Maintenance

Update this file after any future Diabetes source-check, full-text, regulatory, or output-driving source audit.
Because the seed Diabetes paper cards are already explicit `full`, future depth changes should record what changed in evidence quality, endpoint order, regulatory control, or claim boundary.
