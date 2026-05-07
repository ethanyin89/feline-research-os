---
id: topic-fip-endpoint
type: topic
topic: fip
species: feline
disease: FIP
question_type: endpoint
source_ids: [src-fip-002, src-fip-003, src-fip-006, src-fip-007, src-fip-010, src-fip-011, src-fip-013, src-fip-015, src-fip-016, src-fip-019, src-fip-022, src-fip-023, src-fip-024]
last_compiled_at: 2026-05-06
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline FIP Endpoint Handbook

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| FE1 | FIP endpoint logic should be layered support, not one-marker certainty. | B | src-fip-003, src-fip-006, src-fip-015 | diagnostic support frame, not final diagnosis |
| FE2 | Clinicopathologic pattern and disease form are the strongest current operational support endpoints. | B | src-fip-006, src-fip-015 | suspicion-building, not definitive proof |
| FE3 | Acute-phase, immunoglobulin, effusive immune context, and older serology belong in lower background support. | B | src-fip-002, src-fip-007, src-fip-011 | supportive context, not modern lead endpoints |
| FE4 | Mutation-related assays are useful only when utility and limitation are held together. | B | src-fip-010, src-fip-022 | bounded strengthening, not closure |
| FE5 | CSF viral detection is specialized neurologic/ocular support with strong positive value but weak broad rule-out value. | B | src-fip-023 | branch-specific support, not generic assay leadership |
| FE6 | Treatment response, remission, relapse, and survival are follow-up outcomes, not first-pass diagnostic endpoints. | C | src-fip-013, src-fip-016, src-fip-019, src-fip-024 | treatment-monitoring branch, not recognition order |

## Evidence-Depth Caveat

This page sits on a fully deep-extracted FIP source-card layer (24/24 papers). Key anchors: broad composite-support review (`src-fip-003`), clinicopathology series (`src-fip-006`, `src-fip-015`), acute-phase/immunoglobulin support (`src-fip-002`), effusive immune context (`src-fip-007`), historical serology (`src-fip-011`), mutation utility/limitation pair (`src-fip-022`, `src-fip-010`), CSF viral detection (`src-fip-023`), and treatment follow-up anchors (`src-fip-013`, `src-fip-016`, `src-fip-019`, `src-fip-024`). This is now an endpoint handbook rather than a routing page.

## Core Takeaway

The safest FIP endpoint architecture is ordered composite support: clinicopathology and disease form lead; lower laboratory and molecular channels strengthen but do not settle; CSF support belongs to the neurologic/ocular branch; treatment outcomes belong to follow-up rather than diagnosis.

## Endpoint Hierarchy

### Endpoint 1: Clinicopathologic Pattern And Disease Form

This is the lead operational endpoint layer for suspicion-building. It turns non-specific concern into a structured FIP workup and gives wet, dry, and neurologic form practical meaning.

**Key boundary:** raises suspicion but does not prove FIP alone.

**Lead sources:** `src-fip-003`, `src-fip-006`, `src-fip-015`

### Endpoint 2: Acute-Phase, Immunoglobulin, And Effusive Immune Context

Inflammatory laboratory context and effusive-form immunology are useful lower-tier support. They make the endpoint map richer than clinicopathology plus molecular testing, but they should not lead modern workup.

**Key boundary:** supportive background, not a first-line certainty marker.

**Lead sources:** `src-fip-002`, `src-fip-007`

### Endpoint 3: Historical Serology

Serology remains part of the endpoint history and exposure-linked support context. Its current role is background orientation rather than lead diagnostic authority.

**Key boundary:** historical support only; do not promote into modern endpoint leadership.

**Lead sources:** `src-fip-011`

### Endpoint 4: Mutation-Related Assays

Mutation-related testing is a meaningful support channel only when the utility paper and limitation paper are read together. It should strengthen an already suspicious case, not replace the recognition architecture.

**Key boundary:** bounded diagnostic strengthening, not mutation-test closure.

**Lead sources:** `src-fip-010`, `src-fip-022`

### Endpoint 5: CSF Viral Detection In Neurologic/Ocular Branch

CSF RT-PCR has the strongest extracted assay-style numbers in this endpoint layer: specificity `100%`, PPV `100%`, overall sensitivity `42.1%`, NPV `57.7%`, and neurologic/ocular subgroup sensitivity `85.7%`.

**Key boundary:** positive support is strongest after neurologic/ocular branch shift; limited overall sensitivity and NPV block broad rule-out use.

**Lead sources:** `src-fip-023`

### Endpoint 6: Treatment Follow-Up Outcomes

Response, remission, relapse, viral-load follow-up, survival, and neurologic monitoring belong to a treatment-outcome branch. They are important endpoints, but they should not rewrite first-pass diagnosis.

**Key boundary:** treatment monitoring, not initial recognition.

**Lead sources:** `src-fip-013`, `src-fip-016`, `src-fip-019`, `src-fip-024`

## Source-Layer Reality

| Source | Role | Status |
|---|---|---|
| src-fip-002 | acute-phase and immunoglobulin support | deep_extracted |
| src-fip-003 | broad composite-support diagnostic frame | deep_extracted |
| src-fip-006 | Sydney clinicopathology support endpoint | deep_extracted |
| src-fip-007 | effusive immunopathology context | deep_extracted |
| src-fip-010 | mutation-diagnostic limitation anchor | deep_extracted |
| src-fip-011 | historical serology support | deep_extracted |
| src-fip-013 | remission durability and follow-up anchor | deep_extracted |
| src-fip-015 | Taiwan clinicopathology and disease staging | deep_extracted |
| src-fip-016 | baseline GS natural-disease treatment outcomes | deep_extracted |
| src-fip-019 | remdesivir-plus-GS package outcomes | deep_extracted |
| src-fip-022 | mutation-diagnostic utility anchor | deep_extracted |
| src-fip-023 | CSF viral detection performance boundary | deep_extracted |
| src-fip-024 | neurologic treatment monitoring and relapse-sensitive branch | deep_extracted |

## Current Owner Memo

- [FIP support-order memo](../../system/indexes/fip-support-order-memo.md)
- [FIP assay-performance boundary memo](../../system/indexes/fip-assay-performance-boundary-memo.md)
- [FIP endpoint-diagnostic bridge memo](../../system/indexes/fip-endpoint-diagnostic-bridge-memo.md)
- [FIP acute-phase and immunoglobulin support memo](../../system/indexes/fip-acute-phase-support-memo.md)
- [FIP neurologic-workup branch-boundary memo](../../system/indexes/fip-neurologic-workup-branch-boundary-memo.md)

## Guardrail

Do not make this page an assay leaderboard. The current source layer supports endpoint placement and a CSF branch boundary more strongly than it supports a comparable sensitivity/specificity ranking across mutation assays, serology, acute-phase markers, and CSF.

## What The Module Can Say Safely

- FIP endpoint logic is composite and ordered
- clinicopathology and disease form lead suspicion support
- lower inflammatory and serologic markers are background support
- mutation assays strengthen but do not close the case
- CSF viral detection is strongest as neurologic/ocular branch-specific positive support
- treatment outcomes should be tracked separately from first-pass diagnostic endpoints

## What The Module Should Not Say Yet

- do not rank non-CSF assays numerically against CSF without comparable extracted performance detail
- do not treat mutation testing as diagnostic closure
- do not treat negative CSF RT-PCR as broad FIP exclusion
- do not let treatment response become the recognition endpoint

## Current Role

Use this page as the FIP endpoint handbook. The source-card layer is complete at 24/24 deep-extracted papers. Next gains come from non-CSF full-text assay-performance extraction and output-specific outcome architecture where treatment claims need tighter endpoint separation.
