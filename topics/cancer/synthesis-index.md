---
id: topic-cancer-synthesis-index
type: topic
topic: cancer
species: feline
disease: cancer
question_type: synthesis
source_ids: [src-cancer-002, src-cancer-003, src-cancer-004, src-cancer-008, src-cancer-019, src-cancer-040]
last_compiled_at: 2026-05-30
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: not_checked
owner: codex
status: active
---

# Feline Cancer Synthesis Index

## Key-Claim Traceability

| ID | Claim | Level | Source IDs | Boundary |
|---|---|---|---|---|
| CS1 | The cancer module should start with clinical workflow: presentation, diagnosis, staging, then branch-specific treatment discussion | B | src-cancer-040 | workflow architecture, not tumor-specific advice |
| CS2 | Feline cancer should split early by tumor family rather than stay as one flat oncology page | B | src-cancer-004, src-cancer-008, src-cancer-040 | branch architecture, not complete taxonomy |
| CS3 | Mammary carcinoma deserves an early branch because it has comparative oncology and TNBC-like / basal-like model evidence | B | src-cancer-004, src-cancer-019 | model boundary, not treatment or prognosis rule |
| CS4 | COX markers belong in a prognosis-marker caveat layer, with feline reuse limited mainly to mammary carcinoma COX-2 and oral SCC COX-1 pattern | B | src-cancer-003 | marker caveat, not survival prediction or treatment recommendation |
| CS5 | Lymphoma should be split by pathology/grade and topography before treatment or prognosis synthesis | B | src-cancer-004, src-cancer-008 | classification boundary, not treatment guidance |
| CS6 | Registry and prevalence claims must be denominator-labeled before numeric tumor-frequency language is reused | B | src-cancer-002 | pathology registry proportions, not universal prevalence |

## Current Synthesis

The first cancer synthesis pass is now architecture-level only. Six deep-extracted sources define the safe shell:

- `src-cancer-002` supplies registry denominator discipline: tumor-frequency language must remain tied to Swiss pathology records and proportional calculations.
- `src-cancer-040` supplies the suspected-cancer workflow: presentation, diagnosis, staging, and conditional treatment planning.
- `src-cancer-004` supplies the molecular branch map: lymphoma, oral SCC, sarcoma/FISS, mammary carcinoma, and mast cell tumor.
- `src-cancer-008` supplies the lymphoma pathology classification anchor.
- `src-cancer-019` supplies the first mammary carcinoma / TNBC-like comparative oncology anchor.
- `src-cancer-003` supplies the first COX/prognosis-marker boundary.

This is enough to build navigation and branch scaffolding. It is not enough to rank treatments, state survival ranges, or give owner-facing tumor-specific management advice.

## Promoted Topic Branches

- [suspected cancer workflow](suspected-cancer-workflow.md)
- [lymphoma branch](lymphoma.md)
- [mammary carcinoma branch](mammary-carcinoma.md)
- [oral squamous cell carcinoma branch](oral-squamous-cell-carcinoma.md)
- [injection site sarcoma (FISS) branch](injection-site-sarcoma.md)
- [COX and prognosis marker caveats](cox-prognosis-markers.md)
- [registry and prevalence](registry-and-prevalence.md)

## Next Synthesis Questions

1. Which lymphoma source should control lymphoproliferative classification and FeLV/GI-shift claims?
2. Which oral SCC source should control clinical manifestations and local disease behavior?
3. Which sarcoma/FISS source should control injection-site versus spontaneous sarcoma boundaries?
4. Which FISS-specific source should verify injection-site sarcoma time-trend and causality boundaries?
5. Which treatment outcome sources are strong enough to move beyond workflow-level treatment modality descriptions?

See [branch-control candidates](../../system/indexes/cancer-branch-control-candidates.md) for the candidate source mapping and extraction priority queue.

## Current Verdict

Use this page as the cancer module shell. The current compiled layer can define workflow, branch architecture, mammary model boundaries, and COX marker caveats. It cannot yet produce decision-grade treatment, diagnosis, prognosis, or biomarker guidance.
