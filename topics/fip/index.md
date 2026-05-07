---
id: topic-fip-index
type: topic
topic: fip
species: feline
disease: FIP
question_type: overview
source_ids: [src-fip-001, src-fip-002, src-fip-003, src-fip-004, src-fip-005, src-fip-006, src-fip-007, src-fip-008, src-fip-009, src-fip-010, src-fip-011, src-fip-012, src-fip-013, src-fip-014, src-fip-015, src-fip-016, src-fip-017, src-fip-018, src-fip-019, src-fip-020, src-fip-021, src-fip-022, src-fip-023, src-fip-024]
last_compiled_at: 2026-04-10
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: unchecked
owner: codex
status: active
---

# Feline FIP Topic Index

## Question This Page Answers

What is the first-pass internal map of feline infectious peritonitis across pathobiogenesis, diagnosis, epidemiology, treatment, and regulatory layers?

## Topic Pages

- [navigation](./navigation.md)
- [current-state-dashboard](./current-state-dashboard.md)
- [current-state-dashboard-bilingual](./current-state-dashboard-bilingual.md)
- [mechanism-overview](./mechanism-overview.md)
- [endpoint-handbook](./endpoint-handbook.md)
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

- A first FIP seed corpus of `24` candidate sources has now been mapped into the vault.
- FIP is a strong second disease module because it naturally forces the system to handle mechanism, diagnosis, treatment, and epidemiology at the same time.
- The first-pass FIP map should treat `pathobiogenesis / mutation logic`, `risk factors`, `clinicopathology`, `diagnostic limits`, and `antiviral treatment` as separate branches.
- The current source spread supports separating pathobiogenesis, risk factors, clinicopathology, diagnostic limits, and antiviral treatment into distinct branches.
- The current treatment branch already includes GS-441524 and remdesivir-era material.
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
- treatment branch: `src-fip-013`, `src-fip-016`, `src-fip-017`, `src-fip-019`, `src-fip-024`

## Conflicts / Uncertainty

- Most of the current FIP map is no longer source-index level only, but final treatment, access, and route interpretation still lag behind the compiled disease spine.
- Diagnostic mutation logic is already likely to contain internal tension between `mutation-associated spread` and `mutation-based diagnosis limits`.
- Treatment-era optimism must be separated from decision-grade regulatory or access conclusions.

## Gaps

- no FIP entity layer yet
- no antiviral-treatment ranking memo yet
- no broad bilingual FIP page family yet beyond the current compiled core stack
- assay-specific discriminative detail is still thinner than the current boundary wording

## Next Sources To Read First

- `src-fip-003`
- `src-fip-009`
- `src-fip-016`
- `src-fip-019`
- `src-fip-024`
- `src-fip-005`
