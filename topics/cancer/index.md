---
id: topic-cancer-index
type: topic
topic: cancer
language: zh
last_compiled_at: 2026-05-30
verification_status: compiled
decision_grade: no
owner: codex
status: architecture-compiled
---

# Feline Cancer

## Current Role

This is the first architecture-compiled shell for the feline cancer literature queue added on 2026-05-30.

Do not treat this page as a compiled oncology guide yet. The current safe role is navigation:

- preserve the cancer source queue
- separate true feline oncology sources from acronym / model-organism false positives
- identify broad reviews, registry papers, lymphoma anchors, mammary carcinoma anchors, and comparative oncology sources
- keep reader-facing claims behind source-card and extraction gates

## Current Evidence State

| Layer | Status |
|---|---|
| Sheet intake | manifest generated |
| First-pass source cards | 102/102 accepted cancer rows created |
| Source index | active |
| Reading plan | active |
| Metadata / abstract check | 23/102 cards abstract-weighted; 6 deep-extracted |
| Structured abstract worksheets | 10-card sample complete |
| Deep extraction | `src-cancer-002`, `src-cancer-003`, `src-cancer-004`, `src-cancer-008`, `src-cancer-019`, and `src-cancer-040` sample complete |
| Topic synthesis | architecture compiled; treatment/prognosis still gated |

## Promoted Topic Branches

- [Synthesis index](synthesis-index.md)
- [Suspected cancer workflow](suspected-cancer-workflow.md)
- [Lymphoma](lymphoma.md)
- [Mammary carcinoma](mammary-carcinoma.md)
- [COX and prognosis marker caveats](cox-prognosis-markers.md)
- [Registry and prevalence](registry-and-prevalence.md)

## Near-Term Questions

- Use `src-cancer-002` as the first registry denominator anchor, but keep pathology-registry proportions below universal prevalence and causality claims.
- Use `src-cancer-004` as the first molecular branch-map anchor, but keep it below treatment-guideline authority.
- Use `src-cancer-008` as the first lymphoma pathology classification anchor, but keep treatment, prognosis, and modern immunophenotype claims gated.
- Use `src-cancer-019` as the first mammary carcinoma / TNBC-like model anchor, but keep its 24-case numbers study-bound.
- Use `src-cancer-003` as the first COX/prognosis-marker anchor, but keep it below treatment guidance and owner-facing survival prediction.
- Use `src-cancer-040` as the first suspected-cancer workflow anchor, but keep tumor-specific treatment claims behind branch sources.
- Which FISS-specific source should control injection-site sarcoma causality boundaries?
- Which rows are false positives because `feline` is an acronym, gene/protein name, vector system, or algorithm label rather than cat evidence?
- Should feline cancer be one broad module first, or split early into mammary carcinoma, lymphoma, oral SCC, injection-site sarcoma, and FeLV-associated neoplasia branches?

## Linked Indexes

- [Cancer source index](../../system/indexes/cancer-source-index.md)
- [Cancer reading plan round 1](../../system/indexes/cancer-reading-plan-round-1.md)
- [Cancer intake manifest](../../system/indexes/feline-cancer-intake-manifest-20260530.md)
