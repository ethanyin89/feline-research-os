---
id: topic-fip-index
type: topic
topic: fip
species: feline
disease: FIP
question_type: overview
source_ids: [src-fip-001, src-fip-002, src-fip-003, src-fip-004, src-fip-005, src-fip-006, src-fip-007, src-fip-008, src-fip-009, src-fip-010, src-fip-011, src-fip-012, src-fip-013, src-fip-014, src-fip-015, src-fip-016, src-fip-017, src-fip-018, src-fip-019, src-fip-020, src-fip-021, src-fip-022, src-fip-023, src-fip-024, src-fip-025, src-fip-026, src-fip-027, src-fip-028, src-fip-029, src-fip-030, src-fip-031, src-fip-032, src-fip-033, src-fip-034, src-fip-035, src-fip-036, src-fip-037, src-fip-038, src-fip-039, src-fip-040, src-fip-041, src-fip-042, src-fip-043, src-fip-044, src-fip-045, src-fip-046, src-fip-047, src-fip-048, src-fip-049]
last_compiled_at: 2026-06-11
confidence: high
verification_status: compiled
decision_grade: yes
language_qa_status: unchecked
owner: codex
status: active
---

# Feline FIP Topic Index

## Question This Page Answers

What is the first-pass internal map of feline infectious peritonitis across pathobiogenesis, diagnosis, epidemiology, treatment, and regulatory layers?

## 普通用户入口 / For Pet Owners

- [什么是FIP？/ What is FIP?](./what-is-fip.md) — 简单易懂的基础解释
- [FIP怎么识别？/ How to Recognize FIP](./fip-warning-signs.md) — 症状和警示信号

## Topic Pages

- [navigation](./navigation.md)
- [current-state-dashboard](./current-state-dashboard.md)
- [current-state-dashboard-bilingual](./current-state-dashboard-bilingual.md)
- [mechanism-overview](./mechanism-overview.md)
- [endpoint-handbook](./endpoint-handbook.md)
- [**treatment-overview**](./treatment-overview.md) — **NEW: Comprehensive treatment evidence (GS-441524/remdesivir era, ABCD guidelines, RCT)**
- [risk-and-recognition](./risk-and-recognition.md)
- [recognition-architecture](./recognition-architecture.md)
- [translation-brief](./translation-brief.md)
- [regulatory-brief](./regulatory-brief.md)
- [synthesis-index](./synthesis-index.md)
- [synthesis-index-bilingual](./synthesis-index-bilingual.md)
- [FIP support-order memo](../../system/indexes/fip-support-order-memo.md)
- [FIP assay-performance boundary memo](../../system/indexes/fip-assay-performance-boundary-memo.md)
- [FIP briefing round 1 working-en](../../outputs/briefings/out-fip-briefing-20260410-round1-working-en.md)
- [FIP dossier v1 working-en](../../outputs/dossiers/out-fip-dossier-20260410-v1-working-en.md)
- [FIP slides v1 working-en](../../outputs/slides/out-fip-slides-20260410-v1-working-en.md)

## Current Conclusions

### quoted_fact

- The current source set spans pathogenesis, epidemiology, clinicopathology, diagnostics, mutation logic, and antiviral treatment.

### source_supported_conclusion

- The FIP corpus now contains `28` sources including 2023-2024 molnupiravir evidence.
- FIP is a strong second disease module because it naturally forces the system to handle mechanism, diagnosis, treatment, and epidemiology at the same time.
- The first-pass FIP map should treat `pathobiogenesis / mutation logic`, `risk factors`, `clinicopathology`, `diagnostic limits`, and `antiviral treatment` as separate branches.
- The current source spread supports separating pathobiogenesis, risk factors, clinicopathology, diagnostic limits, and antiviral treatment into distinct branches.
- The current treatment branch includes GS-441524, remdesivir, and molnupiravir evidence.
- Molnupiravir is now validated as equivalent to GS-441524 (src-fip-028: 118 cats, p=0.326).
- The current treatment branch is likely stronger and more specific than the current regulatory branch.
- Endpoint and workup compression are now clearer as `support order + assay boundary`, not only broad diagnostic ambiguity.

### llm_inference

- FIP should become the first non-CKD disease where `diagnostic ambiguity` and `treatment transformation` are modeled together rather than separately.
- A good FIP compile will probably center on `systemic spread and macrophage tropism`, not on generic coronavirus background alone.

## Evidence Map

- broad review / chapter anchors: `src-fip-001`, `src-fip-003`
- pathobiogenesis / mutation branch: `src-fip-004`, `src-fip-009`, `src-fip-010`, `src-fip-018`
- risk-factor branch: `src-fip-005`, `src-fip-008`, `src-fip-012`, `src-fip-020`
- clinicopathology / staging branch: `src-fip-002`, `src-fip-006`, `src-fip-015`, `src-fip-023`
- treatment branch (GS-441524): `src-fip-013`, `src-fip-016`, `src-fip-017`, `src-fip-019`, `src-fip-024`
- treatment branch (molnupiravir): `src-fip-026`, `src-fip-027`, `src-fip-028`
- diagnostic innovation: `src-fip-025` (ML diagnosis)

## Conflicts / Uncertainty

- Most of the current FIP map is no longer source-index level only, but final treatment, access, and route interpretation still lag behind the compiled disease spine.
- Diagnostic mutation logic is already likely to contain internal tension between `mutation-associated spread` and `mutation-based diagnosis limits`.
- Treatment-era optimism must be separated from decision-grade regulatory or access conclusions.

## Gaps

- no FIP entity layer yet
- ~~no antiviral-treatment ranking memo yet~~ → molnupiravir validated as equivalent to GS-441524 (src-fip-028)
- no broad bilingual FIP page family yet beyond the current compiled core stack
- assay-specific discriminative detail is still thinner than the current boundary wording
- ML diagnostic tool (src-fip-025) not yet integrated into diagnostic guidance

## Next Sources To Read First

- `src-fip-003`
- `src-fip-009`
- `src-fip-016`
- `src-fip-019`
- `src-fip-024`
- `src-fip-005`
