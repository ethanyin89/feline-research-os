---
id: topic-cancer-synthesis-index
type: topic
topic: cancer
species: feline
disease: cancer
question_type: synthesis
source_ids: [src-cancer-001, src-cancer-002, src-cancer-003, src-cancer-004, src-cancer-005, src-cancer-006, src-cancer-007, src-cancer-008, src-cancer-009, src-cancer-010, src-cancer-012, src-cancer-013, src-cancer-014, src-cancer-015, src-cancer-016, src-cancer-017, src-cancer-018, src-cancer-019, src-cancer-020, src-cancer-021, src-cancer-022, src-cancer-026, src-cancer-027, src-cancer-028, src-cancer-030, src-cancer-031, src-cancer-032, src-cancer-034, src-cancer-035, src-cancer-036, src-cancer-037, src-cancer-038, src-cancer-039, src-cancer-040, src-cancer-041, src-cancer-042, src-cancer-043, src-cancer-044, src-cancer-045, src-cancer-046, src-cancer-047, src-cancer-049, src-cancer-050, src-cancer-051, src-cancer-052, src-cancer-053, src-cancer-054, src-cancer-055, src-cancer-056, src-cancer-060, src-cancer-061, src-cancer-062, src-cancer-063, src-cancer-064, src-cancer-065, src-cancer-066, src-cancer-068, src-cancer-069, src-cancer-071, src-cancer-072, src-cancer-073, src-cancer-074, src-cancer-076, src-cancer-077, src-cancer-081, src-cancer-088, src-cancer-091, src-cancer-093, src-cancer-095, src-cancer-100, src-cancer-101]
last_compiled_at: 2026-06-11
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
language_qa_notes: "2026-06-11 expanded to 72 deep_extracted sources covering oncogenomics, lymphoma, mammary, oral SCC, FISS, and registry evidence."
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
| CS7 | TP53 mutations are documented across multiple feline cancer types (lymphoma, mammary, SCC, HSA, OSA) | A | src-cancer-001 | quoted_fact from 2022 oncogenomics review |
| CS8 | c-KIT mutations in exons 6, 8, 9 found in 60% of feline mast cell tumor cases | A | src-cancer-001 | quoted_fact; parallels canine MCT |
| CS9 | Low-grade GI lymphoma: 96% clinical response with chlorambucil + glucocorticoids, 2-3yr remission | A | src-cancer-001 | quoted_fact; treatment response rate |
| CS10 | High-grade GI lymphoma: only 30% clinical response | A | src-cancer-001 | quoted_fact; grade-dependent prognosis |
| CS11 | ~85% of feline mammary tumours are malignant | A | src-cancer-001 | quoted_fact from oncogenomics review |
| CS12 | Feline cancers have been understudied compared to canine/human cancers | B | src-cancer-001 | research gap framing |
| CS13 | High-quality reference genome (Felis_catus_9.0) enables comprehensive oncogenomic studies | B | src-cancer-001 | research infrastructure claim |

## Current Synthesis

The cancer synthesis has expanded from 6 to 72 deep-extracted sources. Key anchors:

**Genomic Foundation:**
- `src-cancer-001` (2022 oncogenomics review): TP53 mutations across cancer types, c-KIT in MCT (60%), BRCA1/2 in mammary, low-grade GI lymphoma response rates (96% vs 30%)

**Registry & Classification:**
- `src-cancer-002` supplies registry denominator discipline: tumor-frequency language must remain tied to Swiss pathology records and proportional calculations.
- `src-cancer-008` supplies the lymphoma pathology classification anchor (602 cases, NCI Working Formulation).

**Clinical Architecture:**
- `src-cancer-040` supplies the suspected-cancer workflow: presentation, diagnosis, staging, and conditional treatment planning.
- `src-cancer-004` supplies the molecular branch map: lymphoma, oral SCC, sarcoma/FISS, mammary carcinoma, and mast cell tumor.

**Branch-Specific Evidence:**
- `src-cancer-019` supplies the first mammary carcinoma / TNBC-like comparative oncology anchor.
- `src-cancer-003` supplies the first COX/prognosis-marker boundary.

**Evidence Strength:**
- 72 deep_extracted sources now available across all branches
- Mammary carcinoma: 55 claims from 34 sources
- Lymphoma: 31 claims from 16 sources (FeLV biology comprehensive)
- Oral SCC: 32 claims with immune/targeting updates

This is enough to build navigation, branch scaffolding, and genomic context. Treatment ranking and survival estimates remain gated.

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

Use this page as the cancer module shell. The 72-source compiled layer can define:

- Workflow architecture (presentation → diagnosis → staging → branch-specific treatment)
- Branch structure (mammary, lymphoma, oral SCC, FISS, MCT)
- Genomic context (TP53 mutations, c-KIT in MCT, BRCA1/2 in mammary)
- Registry discipline (denominator-labeled tumor frequency)
- Treatment response ranges (low-grade GI lymphoma: 96% response; high-grade: 30%)
- Prognostic markers (COX-2, Ki67, grade, lymph node status)

It cannot yet produce:
- Decision-grade treatment selection
- Owner-facing survival predictions
- Standardized biomarker testing recommendations

---

**Last compiled:** 2026-06-11
**Evidence base:** 72 deep_extracted sources
**Confidence:** Medium — comprehensive architecture with genomic foundation
**Decision Grade:** No — treatment selection and survival prediction remain gated
