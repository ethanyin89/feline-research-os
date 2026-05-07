---
id: ibd-source-depth-map
type: index
topic: system
question_type: navigation
language: bilingual
last_compiled_at: 2026-04-24
confidence: medium
verification_status: compiled
owner: codex
status: active
---

# Source Depth Map — IBD

## 用途 / How to Use

**为了快速找到该深挖哪些 IBD source card：** 先读 exclusion / lymphoma-boundary / activity-index / biopsy-site / fibrosis / diet anchors。
**为了在 context 有限时决定先读哪张：** IBD 24/24 paper source cards 现在都是 `full`；优先读 Tier 1，再读 Tier 2，最后读 Tier 3 extension/context rows。
**为了指导下一步 densification 工作：** 普通 source-card thickening 已完成。`src-ibd-009` 已恢复 abstract/methods/metrics-level source detail，并已同步为 `deep_extracted`，但仍不是 decision-grade；后续只在会改变 workup sequence、lymphoma-boundary ranking、treatment claim-fit、regulatory route-fit、或 image/table verification 时补 full-text / official-source precision。

Depth definitions:

- **full**: source card explicitly says `extraction_depth: full`
- **partial**: source card explicitly says `extraction_depth: partial`
- **stub**: missing usable extraction body or source-card state

Verification-status overlay:

| verification_status | Count | Read |
|---|---:|---|
| deep_extracted | 24 | The entire IBD paper-card layer is now deep-extracted, so strong workup, lymphoma-boundary, marker-hierarchy, and treatment-boundary claims no longer depend on a small anchor subset. |
| source_checked | 0 | no IBD paper source cards remain source-checked only |

---

## Tier 1 — OUTPUT-CONTROLLING ANCHORS

| Source ID | Title (short) | Current Role | Words | Depth | Priority | Key Gap |
|---|---|---|---:|---|---|---|
| src-ibd-003 | Feline IBD review | exclusion-first architecture | 826 | **full** | HIGH | full source-card depth exists; full text needed for older treatment/biopsy nuance |
| src-ibd-004 | FCEAI activity index | disease activity / response tracking | 838 | **full** | HIGH | full source-card depth exists; component table and scoring details need verification |
| src-ibd-015 | Duodenal and ileal biopsies | biopsy-site lymphoma boundary | 832 | **full** | HIGH | full source-card depth exists; site-specific table/image verification remains high value |
| src-ibd-010 | Muscularis propria ultrasound | imaging pressure toward lymphoma | 720 | **full** | HIGH | full source-card depth exists; ultrasound thresholds need full-text recovery |
| src-ibd-001 | Mucosal microbiota and lymphoma | microbiota-boundary bridge | 703 | **full** | HIGH | full source-card depth exists; full text needed for sampling/location detail |
| src-ibd-022 | Intestinal fibrosis | chronicity / remodeling burden | 794 | **full** | HIGH | full source-card depth exists; fibrosis-method table/image verification remains high value |

---

## Tier 2 — IMPORTANT BRANCH ANCHORS

| Source ID | Title (short) | Current Role | Words | Depth | Priority | Key Gap |
|---|---|---|---:|---|---|---|
| src-ibd-016 | Bcl-2 marker | lymphoma-leaning tissue marker | 779 | **full** | MEDIUM | full source-card depth exists; threshold and independent-value details need full text |
| src-ibd-019 | Fecal metabolomics | frontier class-separation marker | 713 | **full** | MEDIUM | full source-card depth exists; validation and marker stability remain open |
| src-ibd-014 | Hydrolysate diet | diet-first treatment anchor | 753 | **full** | MEDIUM | full source-card depth exists; mixed IBD/FRE frame must stay visible |
| src-ibd-012 | Idiopathic IBD IHC | IBD-side immunopathology | 751 | **full** | MEDIUM | full source-card depth exists; small cohort limits operational authority |
| src-ibd-007 | MDR1 / COX2 mRNA | shared molecular disturbance | 708 | **full** | MEDIUM | full source-card depth exists; not a class separator |
| src-ibd-011 | COX-2 immunoexpression | shared epithelial response marker | 706 | **full** | MEDIUM | full source-card depth exists; scoring details may refine explanation only |
| src-ibd-013 | Vitamin D | shared serum burden marker | 705 | **full** | MEDIUM | full source-card depth exists; burden vs prognosis remains open |
| src-ibd-017 | Fecal S100A12 | noninvasive disease-vs-health support | 700 | **full** | MEDIUM | full source-card depth exists; no IBD-vs-lymphoma separation |
| src-ibd-006 | FISH microbiota | older microbiota mechanism | 701 | **full** | MEDIUM | full source-card depth exists; Desulfovibrio direction and sampling detail need full text |

---

## Tier 3 — EXTENSION / CONTEXT ANCHORS

| Source ID | Title (short) | Current Role | Words | Depth | Priority | Key Gap |
|---|---|---|---:|---|---|---|
| src-ibd-002 | Epitheliotropic intestinal lymphoma | lymphoma-side historical anchor | 709 | **full** | LOW | full source-card depth exists; phenotype details need full text |
| src-ibd-005 | Feline MSCs in mouse colitis | exploratory translational treatment | 700 | **full** | LOW | full source-card depth exists; not feline clinical efficacy |
| src-ibd-008 | Canine/feline microbiota review | cross-species dysbiosis context | 702 | **full** | LOW | full source-card depth exists; feline-specific sections need review |
| src-ibd-009 | Histopathology report classification | pathology workflow / informatics | 1151 | **full** | LOW | deep-extracted methods/metrics recovered; keep below biopsy, imaging, and pathology interpretation anchors |
| src-ibd-018 | Eosinophilic sclerosing fibroplasia | remodeling extension | 701 | **full** | LOW | full source-card depth exists; keep extension-only until stronger overlap evidence |
| src-ibd-020 | E. coli granulomatous colitis | organism-linked differential | 705 | **full** | LOW | full source-card depth exists; one-case awareness source |
| src-ibd-021 | Broad therapeutic strategies | treatment landscape context | 700 | **full** | LOW | full source-card depth exists; do not rank feline therapies from this review |
| src-ibd-023 | Cholangitis necropsy | hepatobiliary extension / comorbidity | 702 | **full** | LOW | full source-card depth exists; triaditis/comorbidity modeling remains future work |
| src-ibd-024 | Chronic enteropathy practice review | practice framing / terminology | 714 | **full** | LOW | full source-card depth exists; title-led, best for orientation until full text |

---

## Coverage Summary

| Disease | Total Source Cards | full | partial | stub | verification_status read | Coverage |
|---|---:|---:|---:|---:|---|---|
| IBD | 24 | 24 | 0 | 0 | 24 deep_extracted / 0 source_checked | 100% explicit full; src-ibd-009 remains non-decision-grade workflow support |

---

## Immediate Queue

No IBD source-card partial remains.

- `src-ibd-009`: deep-extracted pathology-report workflow source; methods, label set, and classifier metrics are now recovered. It can support report-structure and pathology-language normalization claims, but not decision-grade diagnosis.

Completed on the 2026-04-22 IBD thickening pass:

1. Tier 1 output-controlling anchors: `src-ibd-001`, `src-ibd-003`, `src-ibd-004`, `src-ibd-010`, `src-ibd-015`, `src-ibd-022`
2. Tier 2 branch anchors: `src-ibd-006`, `src-ibd-007`, `src-ibd-011`, `src-ibd-012`, `src-ibd-013`, `src-ibd-014`, `src-ibd-016`, `src-ibd-017`, `src-ibd-019`
3. Tier 3 extension / context anchors completed, including the 2026-04-23 `src-ibd-009` workflow-source upgrade and 2026-04-28 deep-extracted status reconciliation.

## Maintenance

Update this file after any future IBD full-text, regulatory, image/table, or output-driving source audit.
Because all IBD paper cards are already explicit `full`, future depth changes should record what changed in evidence quality, workup order, treatment claim-fit, route-fit, or extension-boundary handling.
