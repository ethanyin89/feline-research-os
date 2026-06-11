---
id: topic-cancer-current-state-dashboard
type: topic
topic: cancer
source_ids: [src-cancer-001, src-cancer-002, src-cancer-003, src-cancer-004, src-cancer-008, src-cancer-019, src-cancer-040]
language: zh
last_compiled_at: 2026-06-11
verification_status: compiled
decision_grade: no
confidence: medium
language_qa_status: light_checked
language_qa_notes: "2026-06-11 refreshed; 72 deep_extracted sources confirmed."
owner: codex
status: architecture-compiled
---

# Feline Cancer Current State Dashboard

## Status

| Area | State | Note |
|---|---|---|
| Intake | **complete** | 102 source cards created |
| Deep extraction | **72 sources complete** | 72/102 deep_extracted (71%); 30 ingested (subscription-blocked) |
| Oncogenomics | **src-cancer-001 integrated** | TP53 mutations, c-KIT in MCT (60%), BRCA1/2, low/high-grade lymphoma response |
| Mammary carcinoma | **55 claims / 34 sources** | TNBC model, prognostic markers, comparative oncology |
| Lymphoma | **31 claims / 16 sources** | FeLV biology, GI shift, grade-dependent response |
| Oral SCC | **32 claims** | Immune/targeting updated |
| Synthesis-index | **13 claims / 72 sources** | Genomic foundation + branch architecture |
| Reader-facing synthesis | architecture compiled | 8 branch pages (workflow, mammary, lymphoma, oral SCC, FISS, COX, registry, index) |
| Treatment/prognosis | **gated** | Decision-grade guidance requires additional clinical outcome sources |
| Confidence | **MEDIUM** | Comprehensive architecture; treatment selection remains gated |

## Compiled Architecture Pages

- [Synthesis index](synthesis-index.md)
- [Suspected cancer workflow](suspected-cancer-workflow.md)
- [Lymphoma](lymphoma.md) — 31 claims, FeLV transmission/subgroups/susceptibility added 2026-06-03
- [Mammary carcinoma](mammary-carcinoma.md) — 55 claims, AKT/CXCR4/TIL-TAM/nanomedicine added 2026-06-03
- [Oral squamous cell carcinoma](oral-squamous-cell-carcinoma.md) — 32 claims, podoplanin/immune/MCT inhibitor added 2026-06-03
- [Injection site sarcoma (FISS)](injection-site-sarcoma.md) — adjuvant hypothesis branch
- [COX and prognosis marker caveats](cox-prognosis-markers.md)
- [Registry and prevalence](registry-and-prevalence.md)

## Strongest Early Candidate Branches

- broad feline oncology / oncogenomics reviews
- suspected-cancer clinical workflow
- cancer registry and prevalence papers
- mammary carcinoma comparative oncology
- mammary carcinoma / TNBC-like basal phenotype model
- COX / prognosis-marker caveats
- lymphoma and lymphoproliferative disease
- oral squamous cell carcinoma
- FeLV-associated neoplasia

## Do Not Do Yet

- do not rank treatments
- do not state prognosis ranges as reusable claims
- do not promote comparative oncology model papers into clinical guidance
- do not ingest rows where `feline` is only an acronym or non-cat label
