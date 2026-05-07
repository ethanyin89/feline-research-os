---
id: hcm-source-depth-map
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

# Source Depth Map — HCM

## 用途 / How to Use

**为了快速找到该深挖哪些 HCM source card：** 所有 24 张 HCM paper source cards 已经是 explicit `full`；先读 Tier 1，再读 Tier 2。
**为了在 context 有限时决定先读哪张：** 不再按 `partial` 排队；按输出问题选择 genetics / treatment / biomarker / remodeling / boundary anchor。
**为了指导下一步 densification 工作：** 只在会改变 page-layer claim、branch order、或 full-text confirmation threshold 时继续补 HCM。

Load this when deciding which HCM source cards to deepen next under context limits.

Depth definitions:
- **full**: `status: extracted`, frontmatter `evidence_policy` contains reusable quoted facts and conclusions, words >= 700
- **partial**: `status: extracted` but evidence remains too shallow or words < 700
- **stub**: `status: ingested`, thin body, worksheet exists but source card still cannot safely support dense write-back on its own

Verification-status overlay:

| verification_status | Count | Read |
|---|---:|---|
| deep_extracted | 24 | HCM source-card depth is complete across the full paper-card layer; the remaining gap is output-specific comparison and implementation precision, not abstract-led card rescue. |
| source_checked | 0 | no HCM paper source cards remain source-checked only |

---

## Tier 1 — CRITICAL / OUTPUT-CONTROLLING ANCHORS

These cards create the largest HCM page-layer dependency. All are now explicit full source-card depth and deep-extracted, though stronger cross-context comparison still needs output-specific compression.

| Source ID | Title (short) | Current Role | Words | Depth | Priority | Key Gap |
|---|---|---|---|---|---|---|
| src-hcm-001 | Feline Cardiomyopathies 2: HCM | broad HCM review anchor | 799 | **full** | HIGH | broad review now densified and deep-extracted; stronger output-specific synthesis still needs compression |
| src-hcm-007 | Feline Cardiomyopathies 1: General concepts | outer cardiomyopathy frame | 721 | **full** | HIGH | broad framing is now source-backed at full depth and deep-extracted; stronger cross-cardiomyopathy compression is still useful |
| src-hcm-004 | Genetics of feline HCM | genotype anchor | 933 | **full** | HIGH | genetics branch now has abstract-backed phenotype/genotype analogy and variant-overclaim boundary |
| src-hcm-009 | Echo phenotype assessment | structural recognition anchor | 707 | **full** | HIGH | phenotype authority is now source-backed and deep-extracted; stronger output-facing comparison still needs compression |
| src-hcm-008 | Clinical-diagnostic and therapeutic advances | broad clinical and translation overview | 729 | **full** | HIGH | modern bridge review is now source-backed and deep-extracted; treatment/output hierarchy still needs tighter compression |

---

## Tier 2 — IMPORTANT (endpoint and treatment separators)

These cards are likely to matter next because they control biomarker compression, treatment skepticism, and phenotype boundary-setting.

| Source ID | Title (short) | Current Role | Words | Depth | Priority | Key Gap |
|---|---|---|---|---|---|---|
| src-hcm-006 | Cardiac Troponin I | biomarker use-case anchor | 742 | **full** | HIGH | troponin branch is now real, but broader biomarker ranking still thin |
| src-hcm-010 | NT-proBNP screening | screening-boundary anchor | 714 | **full** | HIGH | screening branch is now source-backed, but external generalizability remains bounded |
| src-hcm-015 | Science or faith? | treatment skepticism anchor | 726 | **full** | HIGH | evidence-skepticism branch is now source-backed at full depth and deep-extracted; implementation ranking remains open |
| src-hcm-014 | Enalapril treatment | older conventional-therapy anchor | 888 | **full** | HIGH | retrospective enalapril signal, CHF count, tolerability, and prospective-study caveat now captured |
| src-hcm-012 | Clinical aspects + genetic factors | genotype-severity bridge | 717 | **full** | MEDIUM | genotype-severity bridge is now real, but still mutation-context bounded |
| src-hcm-013 | Morphometry value | diagnosis boundary anchor | 720 | **full** | MEDIUM | macro-versus-micro morphometry boundary is now source-backed and deep-extracted; output-facing compression still helps |
| src-hcm-024 | Pathology staging | remodeled end-stage anchor | 711 | **full** | MEDIUM | end-stage remodeling depth is now source-backed, but still pathology-depth bounded |
| src-hcm-011 | Sarcomere inhibitor | targeted-frontier anchor | 891 | **full** | MEDIUM | MYK-461 five-cat acute LVOT proof-of-principle and conflict boundary now captured |
| src-hcm-021 | Myocardial disease classification | outer-frame anchor | 827 | **full** | MEDIUM | broader myocardial-disease classification, CHF/ATE, echo variability, and management controversy now captured |
| src-hcm-020 | Macrophage-driven remodeling | remodeling mechanism anchor | 725 | **full** | MEDIUM | remodeling branch is now source-backed and deep-extracted, but still not fully compressed for output-facing mechanism hierarchy |
| src-hcm-022 | Remodeling mediators | mediator-depth anchor | 856 | **full** | MEDIUM | lumican/LOX/TGF-beta2 mediator branch and tissue-mechanism boundary now captured |
| src-hcm-017 | Novel biomarkers | frontier-biomarker anchor | 844 | **full** | MEDIUM | IGFBP-2/WNT5A/IL-18 frontier marker signal and small-cohort validation boundary now captured |
| src-hcm-019 | RV involvement | phenotype-depth anchor | 784 | **full** | MEDIUM | RV hypertrophy cohort, reference-method split, and severity/CHF association now captured |
| src-hcm-016 | Human-cat comparative review | comparative-bridge anchor | 739 | **full** | MEDIUM | human-cat phenotype/pathology analogy and genetics-asymmetry boundary now captured |
| src-hcm-023 | Deep-learning diagnosis | AI-augmentation anchor | 801 | **full** | MEDIUM | VD-radiograph CNN dataset, performance signal, and screening-augmentation boundary now captured |
| src-hcm-018 | Idiopathic cardiomyopathy cohort | extension-boundary anchor | 782 | **full** | MEDIUM | 106-cat historical idiopathic-cardiomyopathy distribution and survival context now captured |
| src-hcm-002 | HCM update | historical-overview anchor | 861 | **full** | MEDIUM | older broad review now has full source-card depth and deep-extracted status for durable phenotype and review-scope framing |
| src-hcm-003 | Large-animal model review | model-bridge anchor | 935 | **full** | MEDIUM | spontaneous-model branch now has source-page-checked model value, breed/mutation context, and overclaim boundary |
| src-hcm-005 | Non-HCM cardiomyopathies review | boundary-extension anchor | 770 | **full** | MEDIUM | DCM/RCM/ARVC/LVNC/NCM boundary and echocardiographic confirmation logic now captured |

---

## Tier 3 — REMAINING STUBS

No remaining HCM cards are `stub` or `partial`. The remaining gap is not source-card depth; it is full-text confirmation only where an external output needs stronger clinical, regulatory, or numerical precision.

---

## Coverage Summary

| Disease | Total Source Cards | full | partial | stub | verification_status read | Coverage |
|---|---:|---:|---:|---:|---|---|
| HCM | 24 | 24 | 0 | 0 | 24 deep_extracted / 0 source_checked | 100% full |

---

## Immediate Queue

No HCM source-card partials remain.

Completed before this pass: `src-hcm-001`, `src-hcm-002`, `src-hcm-003`, `src-hcm-006`, `src-hcm-007`, `src-hcm-008`, `src-hcm-009`, `src-hcm-010`, `src-hcm-012`, `src-hcm-013`, `src-hcm-015`, `src-hcm-020`, `src-hcm-024`.

Completed in the 2026-04-22 HCM thickening pass: `src-hcm-004`, `src-hcm-005`, `src-hcm-011`, `src-hcm-014`, `src-hcm-016`, `src-hcm-017`, `src-hcm-018`, `src-hcm-019`, `src-hcm-021`, `src-hcm-022`, `src-hcm-023`.

## Maintenance

Update this file after future HCM full-text, output-driving, or regulatory/diagnostic precision passes.
Because all HCM paper cards are already explicit `full`, future changes should record evidence-quality or branch-order changes rather than another source-card thickening queue.
