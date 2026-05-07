---
id: topic-ckd-current-state-dashboard
type: topic
topic: ckd
species: feline
disease: CKD
question_type: overview
source_ids: [src-ckd-001, src-ckd-002, src-ckd-003, src-ckd-004, src-ckd-005, src-ckd-006, src-ckd-007, src-ckd-008, src-ckd-009, src-ckd-010, src-ckd-011, src-ckd-012, src-ckd-013, src-ckd-014, src-ckd-015, src-ckd-016, src-ckd-017, src-ckd-018, src-ckd-019, src-ckd-020, src-ckd-021, src-ckd-022, src-ckd-023, src-ckd-024]
last_compiled_at: 2026-04-11
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline CKD Current State Dashboard

## Quick Helpers

- if you want to trace a claim back down:
  [verify a claim](../../system/indexes/verify-a-claim.md)
- if you want to see real `promote / hold / partial promotion` examples:
  [promotion examples index](../../system/indexes/promotion-examples-index.md)

If you want to enter this vault by question rather than by file tree, start here:

- [ask the vault](../../system/indexes/ask-the-vault.md)

## Top Questions

If your real question is one of these, go straight there:

- `What is the strongest current CKD mechanism reading?`
  Open: [mechanism overview](mechanism-overview.md)
- `Which CKD endpoints are operational versus contextual?`
  Open: [endpoint handbook](endpoint-handbook.md)
- `How strong is the current CKD treatment branch?`
  Open: [translation brief](translation-brief.md)
- `How far can the current CKD regulatory reading go?`
  Open: [regulatory brief](regulatory-brief.md)
- `Which CKD claims should I verify back in the papers?`
  Open: [verify a claim](../../system/indexes/verify-a-claim.md)

## If This Page Exposes A Repeated Gap

Do not treat every question as a write-back candidate.

Promote it only if it keeps recurring and clearly improves structure, for example:

- a branch boundary is still blurry
- a `support` versus `lead` distinction is missing
- a better landing page is needed for the same recurring question

If you want the full operating logic, use:

- [query to write-back](../../system/indexes/query-to-writeback.md)

Use this page when you want the fastest possible answer to:

- what already exists
- what is solid
- what is still thin
- what to do next

## Current Status

### Usable Now

- CKD topic structure is in place
- CKD source corpus has expanded from 12 to 24 ingested papers
- core mechanism, endpoint, translation, and regulatory pages exist
- deep extraction workflow exists and now covers the full 24-paper CKD seed corpus
- bilingual derived outputs now exist
- first clean Chinese-facing outputs now exist
- health check has been run through round 3
- CKD is now mature enough to serve as the reusable disease-module template for future disease rollout

### Strongest Areas

- fibrosis-centered mechanism framing
- pathology-to-endpoint linkage
- endpoint shortlist and tiering
- trial-outcome logic
- first-pass treatment ranking
- recognition logic around older/high-risk cats
- route-level regulatory orientation
- archetype-versus-route comparison logic

### Still Weak

- intervention-by-intervention treatment ranking
- treatment primary-study density
- product-specific regulatory strategy
- final route recommendation beyond the current comparison layer
- Type 2 (controlled intervention) model coverage for drug-efficacy questions

## Page Status

| Area | Main Page | State | Notes |
|---|---|---|---|
| Mechanism | [mechanism overview](mechanism-overview.md) | strong (handbook) | 2026-05-06 recompiled to handbook status with Key-Claim Traceability |
| Pathology bridge | [pathology correlations](pathology-correlations.md) | strong | one of the best current bridge pages |
| Endpoints | [endpoint handbook](endpoint-handbook.md) | strong (handbook) | 2026-05-06 recompiled to handbook status with Key-Claim Traceability |
| SDMA frontier | [CKD SDMA frontier memo](../../system/indexes/ckd-sdma-frontier-memo.md) | usable and improving | clarifies SDMA support logic versus metabolomic-panel frontier logic |
| Early detection | [early detection](early-detection.md) + [frontier branch memo](../../system/indexes/ckd-early-detection-frontier-branch-memo-20260417.md) | two named parallel branches | Branch A: serial surveillance (operational); Branch B: pre-clinical metabolomics/ML frontier (research-stage, distinct question) |
| Risk recognition | [risk and recognition](risk-and-recognition.md) | strong (handbook) | 2026-05-06 recompiled to handbook status with Key-Claim Traceability |
| Hypertension | [hypertension and comorbidity](hypertension-and-comorbidity.md) | usable and improving | implementation gap around SBP measurement is now explicit |
| Hypertension-proteinuria junction | [CKD hypertension-proteinuria junction memo](../../system/indexes/ckd-hypertension-proteinuria-junction-memo.md) | usable and improving | clarifies where hemodynamic management and proteinuria-oriented management overlap without collapsing into one claim |
| Translation | [translation brief](translation-brief.md) | usable and improving | trial-outcome logic, implementation-friction layer, and first-pass treatment ranking are now explicit |
| Disease-modification boundary | [CKD disease-modification boundary memo](../../system/indexes/ckd-disease-modification-boundary-memo.md) | usable | clarifies where management and progression-control language stop and true disease-modification overclaim begins |
| Proteinuria treatment evidence | [CKD proteinuria treatment evidence memo](../../system/indexes/ckd-proteinuria-treatment-evidence-memo.md) | usable and improving | clarifies proteinuria as endpoint, pathology signal, and bounded treatment branch |
| Phosphorus-control evidence | [CKD phosphorus-control evidence memo](../../system/indexes/ckd-phosphorus-control-evidence-memo.md) | usable and improving | separates renal-diet phosphorus logic, adjunct binder logic, and wider CKD-MBD burden logic |
| Mineral burden | [CKD mineral-burden memo](../../system/indexes/ckd-mineral-burden-memo.md) | usable and improving | lifts the branch above phosphorus alone and organizes PTH, calcium risk, and FGF23 into one CKD-MBD frame |
| Supportive care evidence | [CKD supportive-care evidence memo](../../system/indexes/ckd-supportive-care-evidence-memo.md) | usable and improving | separates potassium, anaemia, appetite-support, and subcutaneous-fluid branches instead of flattening them |
| Outcome architecture | [CKD outcome architecture memo](../../system/indexes/ckd-outcome-architecture-memo.md) | usable and improving | separates routine operational endpoints from broader treatment-trial outcome architecture |
| Treatment ranking | [CKD treatment ranking memo](../../system/indexes/ckd-treatment-ranking-memo.md) | usable | formalizes the current intervention hierarchy without overclaiming proof depth |
| Product archetypes | [CKD treatment product archetype memo](../../system/indexes/ckd-treatment-product-archetype-memo.md) | usable | converts intervention classes into first-pass asset types for later regulatory work |
| Archetype-versus-route comparison | [CKD archetype-route cleanliness memo](../../system/indexes/ckd-archetype-route-cleanliness-memo.md) | usable | shows why the strongest treatment archetype is not automatically the cleanest route archetype |
| Product-specific route memo | [CKD renal diet route memo](../../system/indexes/ckd-renal-diet-route-memo.md) | usable | first real jurisdiction-by-jurisdiction route test for one clean archetype |
| Product-specific route memo 2 | [CKD hemodynamic management route memo](../../system/indexes/ckd-hemodynamic-management-route-memo.md) | usable | shows where the current official-source pack becomes more useful for drug-like products |
| Product-specific route memo 3 | [CKD proteinuria-oriented renoprotective route memo](../../system/indexes/ckd-proteinuria-renoprotective-route-memo.md) | usable | shows where route-fit remains usable even as claim-fit becomes more fragile |
| Product-specific route memo 4 | [CKD phosphorus-control adjunct route memo](../../system/indexes/ckd-phosphorus-control-route-memo.md) | usable | shows where phosphorus endpoint strength is cleaner than product-category fit |
| Next route-memo priority | [CKD next route-memo priority memo](../../system/indexes/ckd-next-route-memo-priority-memo.md) | usable | shows why proteinuria is the best next borderline route stress test and why phosphorus should pause at route level |
| Traceability rollout | [sentence-level traceability standard](../../system/indexes/sentence-level-traceability-standard.md) | usable and expanding | key-claim-level traceability now exists on translation, regulatory, synthesis, and core strategy memos |
| Implementation realism | [implementation friction](implementation-friction.md) | usable | separates evidence logic from execution friction |
| Imaging realism | [imaging context](imaging-context.md) | usable | separates structural workup context from endpoint overclaim |
| Model | [model map](model-map.md) + [model taxonomy memo](../../system/indexes/ckd-model-taxonomy-memo-20260417.md) | taxonomy explicit | model types now separated by purpose; Type 2 (experimental intervention) remains the main gap |
| Regulatory | [regulatory brief](regulatory-brief.md) | usable | route-level, not product-specific |
| Global synthesis | [synthesis index](synthesis-index.md) | strong | best compiled overview in one language |
| Global synthesis bilingual | [synthesis index bilingual](synthesis-index-bilingual.md) | usable | good cross-language entry page |
| Trust audit | [CKD accuracy and verifiability audit](../../system/indexes/ckd-accuracy-and-verifiability-audit.md) | usable | states which layers are auditable, which remain working judgment only |
| Claim protocol | [claim audit protocol](../../system/indexes/claim-audit-protocol.md) | usable | defines what must be traced, downgraded, or blocked before reuse |
| Language QA | [language QA protocol](../../system/indexes/language-qa-protocol.md) | usable | defines which high-visibility pages need wording and bilingual-alignment checks |
| Language naming | [language filename alignment standard](../../system/indexes/language-filename-alignment-standard.md) | usable | defines how filename, frontmatter, and actual page language must align |
| Output language matrix | [CKD output language matrix](../../system/indexes/ckd-output-language-matrix.md) | usable | defines the current working-en, derived-en, zh, and bilingual output layers |
| Chinese outputs | [briefing zh](../../outputs/briefings/out-ckd-briefing-20260408-round1-zh.md) | usable | first clean Chinese-facing output layer now exists for briefing, dossier, and slides |
| Karpathy gap roadmap | [Karpathy framework gap roadmap](../../system/indexes/karpathy-framework-gap-roadmap.md) | usable | defines the remaining control-layer gaps to stay inside the LLM KB framework |

## Workflow Status

### Ingest Workflow

- first-pass ingest: complete for the current 24-source seed corpus
- source-card structure: complete for the current 24-source seed corpus
- verification-status frontmatter is now clean for the CKD paper-card layer: `24/24` cards are marked `deep_extracted`; decision-grade reuse still follows the CKD trust audit and claim protocol
- topic write-back: working

### Deep Extraction Workflow

- deep extraction: complete for the current 24-source seed corpus
- prompt: [deep extraction prompt v1](../../system/prompts/deep-extraction-prompt-v1.md)
- workflow page: [deep extraction workflow](../../system/indexes/deep-extraction-workflow.md)
- examples:
  - [src-ckd-004](../../system/indexes/src-ckd-004-deep-extraction-round1.md)
  - [src-ckd-010](../../system/indexes/src-ckd-010-deep-extraction-round1.md)
  - [src-ckd-011](../../system/indexes/src-ckd-011-deep-extraction-round1.md)
  - [src-ckd-024](../../system/indexes/src-ckd-024-deep-extraction-round1.md)
  - [src-ckd-013](../../system/indexes/src-ckd-013-deep-extraction-round1.md)
  - [src-ckd-022](../../system/indexes/src-ckd-022-deep-extraction-round1.md)
  - [src-ckd-017](../../system/indexes/src-ckd-017-deep-extraction-round1.md)
  - [src-ckd-016](../../system/indexes/src-ckd-016-deep-extraction-round1.md)
  - [src-ckd-018](../../system/indexes/src-ckd-018-deep-extraction-round1.md)
  - [src-ckd-015](../../system/indexes/src-ckd-015-deep-extraction-round1.md)
  - [src-ckd-019](../../system/indexes/src-ckd-019-deep-extraction-round1.md)
  - [src-ckd-020](../../system/indexes/src-ckd-020-deep-extraction-round1.md)
  - [src-ckd-021](../../system/indexes/src-ckd-021-deep-extraction-round1.md)
  - [src-ckd-023](../../system/indexes/src-ckd-023-deep-extraction-round1.md)
  - [src-ckd-014](../../system/indexes/src-ckd-014-deep-extraction-round1.md)
  - [src-ckd-001](../../system/indexes/src-ckd-001-deep-extraction-round1.md)
  - [src-ckd-002](../../system/indexes/src-ckd-002-deep-extraction-round1.md)
  - [src-ckd-003](../../system/indexes/src-ckd-003-deep-extraction-round1.md)
  - [src-ckd-005](../../system/indexes/src-ckd-005-deep-extraction-round1.md)
  - [src-ckd-006](../../system/indexes/src-ckd-006-deep-extraction-round1.md)
  - [src-ckd-007](../../system/indexes/src-ckd-007-deep-extraction-round1.md)
  - [src-ckd-008](../../system/indexes/src-ckd-008-deep-extraction-round1.md)
  - [src-ckd-009](../../system/indexes/src-ckd-009-deep-extraction-round1.md)
  - [src-ckd-012](../../system/indexes/src-ckd-012-deep-extraction-round1.md)

### Bilingual Workflow

- policy: [bilingual content policy](../../system/prompts/bilingual-content-policy.md)
- rules: [bilingual output rules](../../system/prompts/bilingual-output-rules.md)
- output matrix: [CKD output language matrix](../../system/indexes/ckd-output-language-matrix.md)
- current best examples:
  - [core paper synthesis memo bilingual](../../system/indexes/core-paper-synthesis-memo-ckd-round1-bilingual.md)
  - [synthesis index bilingual](synthesis-index-bilingual.md)
  - [dossier en](../../outputs/dossiers/out-ckd-dossier-20260408-v1-en.md)
  - [dossier zh](../../outputs/dossiers/out-ckd-dossier-20260408-v1-zh.md)

## Quality Status

- latest quality report: [health check round 3](../../system/health-checks/health-check-report-20260408-round3.md)
- current main bottleneck:
  - uneven evidence density across layers
  - especially treatment primary-study density, model taxonomy, and newer early-detection literature
- control-layer note:
  - verification status and key-claim traceability now exist on the main compiled pages
  - language QA is now a separate required gate for high-visibility pages

## Recommended Next Moves

### Highest Value

1. begin the next disease shells, using CKD as the default reusable module for `FIP / IBD / HCM`
2. keep CKD open for incremental source additions rather than waiting for a fictional fully-finished state
3. continue denser CKD write-back under the outcome architecture when new high-value papers arrive
4. use `src-ckd-003` and `src-ckd-014` to sharpen supportive-care and implementation-burden outcomes when CKD densification resumes

### Round 2 Tier A Cluster: Completed

- [src-ckd-024 biomarker review](../../raw/papers/src-ckd-024.md)
- [src-ckd-013 core outcome set](../../raw/papers/src-ckd-013.md)
- [src-ckd-022 experimental model](../../raw/papers/src-ckd-022.md)
- [src-ckd-017 proteinuric kidney disease](../../raw/papers/src-ckd-017.md)
- [src-ckd-016 aged-cat morphology and pathogeneses](../../raw/papers/src-ckd-016.md)

See:

- [CKD reading plan round 2](../../system/indexes/ckd-reading-plan-round-2.md)
- [CKD Round 2 Tier A synthesis memo](../../system/indexes/ckd-round-2-tier-a-synthesis-memo.md)
- [CKD Round 2 late-cluster synthesis memo](../../system/indexes/ckd-round-2-late-cluster-synthesis-memo.md)

### Current Light-Source Cleanup: Completed

- [src-ckd-020 ultrasonography review](../../raw/papers/src-ckd-020.md)
- [src-ckd-014 Portugal practice-pattern study](../../raw/papers/src-ckd-014.md)

### Do Not Do Yet

- do not translate raw source cards by default
- do not overbuild new structure before adding more source depth
- do not make submission-grade regulatory claims from the current corpus

## One-Sentence State

This CKD vault is now a real working research system with a completed second Tier A densification cluster, a formal first-pass treatment ranking, a first-pass product-archetype layer, four product-specific route memos, and an explicit next-route priority layer, and its next gains will come from carefully chosen evidence additions rather than more framework.

## New Densification Note

- [CKD outcome primary-study densification memo](../../system/indexes/ckd-outcome-primary-study-densification-memo.md)
- [CKD completion and multi-disease rollout memo](../../system/indexes/ckd-completion-and-multi-disease-rollout-memo.md)
