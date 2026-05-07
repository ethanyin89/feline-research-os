---
id: fip-source-depth-map
type: index
topic: system
question_type: navigation
language: bilingual
last_compiled_at: 2026-04-22
confidence: medium
verification_status: compiled
owner: codex
status: active
---

# Source Depth Map — FIP

## 用途 / How to Use

**为了快速找到该深挖哪些 FIP source card：** 先看 treatment / diagnostic / mechanism / risk 的 Tier 1 控制源。
**为了在 context 有限时决定先读哪张：** FIP 24/24 paper source cards 已经都是 `full`；优先读 Tier 1，再读 Tier 2，最后读 Tier 3 historical / context anchors。
**为了指导下一步 densification 工作：** 不再做普通 source-card thickening；只在会改变 assay ranking、diagnostic workup order、antiviral branch order、regulatory route test、或 outbreak/mechanism boundary 时补 full-text / official-source precision。

Depth definitions:

- **full**: source card explicitly says `extraction_depth: full`
- **partial**: source card explicitly says `extraction_depth: partial`
- **stub**: missing usable extraction body or source-card state

Verification-status overlay:

| verification_status | Count | Read |
|---|---:|---|
| deep_extracted | 24 | FIP is the cleanest non-CKD verification-status layer; remaining gaps are full-text table/detail, official-source, image/table, and output-specific precision, not abstract-led card depth. |

---

## Tier 1 — OUTPUT-CONTROLLING ANCHORS

| Source ID | Title (short) | Current Role | Words | Depth | Priority | Key Gap |
|---|---|---|---:|---|---|---|
| src-fip-003 | Broad FIP review | broad disease / diagnostic humility | 730 | **full** | HIGH | full source-card depth exists; still review-level and should not replace branch-specific evidence |
| src-fip-016 | GS-441524 natural disease | baseline antiviral efficacy / safety | 713 | **full** | HIGH | full source-card depth exists; severe neurologic/ocular boundaries still need label-specific handling |
| src-fip-019 | Remdesivir + GS case series | real-world treatment package | 730 | **full** | HIGH | full source-card depth exists; package logic should not be merged with single-agent baseline GS |
| src-fip-024 | Neurologic GS treatment | neurologic rescue / dose complexity | 764 | **full** | HIGH | full source-card depth exists; neurologic branch must stay separate from ordinary baseline treatment |
| src-fip-023 | CSF FCoV detection | neurologic diagnostic extension | 821 | **full** | HIGH | full source-card depth exists; CSF metrics need full-text table verification before visual reuse |
| src-fip-014 | Recombinant epizootic | recombinant outbreak / direct transmission | 778 | **full** | HIGH | full source-card depth exists; outbreak logic should widen, not replace, the default mechanism model |

---

## Tier 2 — IMPORTANT BRANCH ANCHORS

| Source ID | Title (short) | Current Role | Words | Depth | Priority | Key Gap |
|---|---|---|---:|---|---|---|
| src-fip-009 | Mutation from endemic FECV | classical mutation-origin spine | 705 | **full** | MEDIUM | full source-card depth exists; mechanism-first, not diagnostic certainty |
| src-fip-004 | 3c gene analysis | gut competence vs systemic competence | 736 | **full** | MEDIUM | full source-card depth exists; 3c signal should not become single-cause logic |
| src-fip-018 | Spike changes and systemic spread | spread-not-FIP boundary | 711 | **full** | MEDIUM | full source-card depth exists; sample/compartment details need full-text recovery |
| src-fip-022 | Spike mutation detection | positive mutation-diagnostics utility | 702 | **full** | MEDIUM | full source-card depth exists; performance/sample context still needs full text |
| src-fip-010 | Spike mutation limitations | mutation-diagnostics caution | 731 | **full** | MEDIUM | full source-card depth exists; exact limitation mechanism still needs full text |
| src-fip-015 | Taiwan clinicopathology/staging | structured disease-form recognition | 759 | **full** | MEDIUM | full source-card depth exists; staging table/image verification remains open |
| src-fip-006 | Sydney clinicopathology | practical recognition pattern | 708 | **full** | MEDIUM | full source-card depth exists; exact lab variable ranking still needs full text |
| src-fip-005 | Australian risk factors | signalment risk | 755 | **full** | MEDIUM | full source-card depth exists; population transferability remains bounded |
| src-fip-008 | Multi-cat endemic FECV risk | ecology-aware exposure risk | 707 | **full** | MEDIUM | full source-card depth exists; environment definitions need full-text recovery |
| src-fip-020 | VMTH epidemiology | referral-population enrichment | 720 | **full** | MEDIUM | full source-card depth exists; accession denominators must stay visible |
| src-fip-013 | GS remission follow-up | remission durability | 721 | **full** | MEDIUM | full source-card depth exists; selected-remission-cohort framing must stay attached |
| src-fip-017 | Experimental GS foundation | preclinical / PK / experimental rescue | 772 | **full** | MEDIUM | full source-card depth exists; do not collapse into natural-disease efficacy |

---

## Tier 3 — HISTORICAL / CONTEXT ANCHORS

| Source ID | Title (short) | Current Role | Words | Depth | Priority | Key Gap |
|---|---|---|---:|---|---|---|
| src-fip-001 | FIP / FCoV chapter | historical broad frame | 702 | **full** | LOW | full source-card depth exists; not current GS-era treatment authority |
| src-fip-002 | Acute phase / immunoglobulins | inflammatory laboratory support | 752 | **full** | LOW | full source-card depth exists; marker-specific discrimination still needs full text |
| src-fip-007 | Effusive immunologic phenomena | effusive immunopathology | 715 | **full** | LOW | full source-card depth exists; historical/form-specific, not general diagnostic leader |
| src-fip-011 | Naturally occurring FIP serology | historical serology support | 732 | **full** | LOW | full source-card depth exists; modern assay role remains bounded |
| src-fip-012 | Breed prevalence | breed-risk enrichment | 700 | **full** | LOW | full source-card depth exists; breed denominator and generalizability need review |
| src-fip-021 | Experimental morphogenesis | historical mechanism / virology | 721 | **full** | LOW | full source-card depth exists; keep as background sidebar unless mechanism history is needed |

---

## Coverage Summary

| Disease | Total Source Cards | full | partial | stub | verification_status read | Coverage |
|---|---:|---:|---:|---:|---|---|
| FIP | 24 | 24 | 0 | 0 | 24 deep_extracted | 100% full |

---

## Immediate Queue

No FIP source-card partials remain.

Completed on the 2026-04-22 FIP thickening pass:

1. Tier 1 output-controlling anchors: `src-fip-003`, `src-fip-014`, `src-fip-016`, `src-fip-019`, `src-fip-023`, `src-fip-024`
2. Tier 2 branch anchors: `src-fip-004`, `src-fip-005`, `src-fip-006`, `src-fip-008`, `src-fip-009`, `src-fip-010`, `src-fip-013`, `src-fip-015`, `src-fip-017`, `src-fip-018`, `src-fip-020`, `src-fip-022`
3. Tier 3 historical / context anchors: `src-fip-001`, `src-fip-002`, `src-fip-007`, `src-fip-011`, `src-fip-012`, `src-fip-021`

## Maintenance

Update this file after any future FIP full-text, regulatory, image, or output-driving source audit.
Because all FIP paper cards are already explicit `full`, future depth changes should record what changed in evidence quality, endpoint order, regulatory control, treatment branch hierarchy, or mechanism boundary.
