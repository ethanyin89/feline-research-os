---
id: topic-fcv-endpoint-handbook
type: topic
topic: fcv
species: feline
disease: feline calicivirus infection
question_type: endpoints
source_ids: [src-fcv-003, src-fcv-005, src-fcv-010, src-fcv-011, src-fcv-012, src-fcv-013, src-fcv-017, src-fcv-018, src-fcv-022, src-fcv-024]
last_compiled_at: 2026-04-30
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline FCV Endpoint Handbook

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| FE1 | FCV endpoint language must separate neutralisation breadth, challenge protection, platform-vaccine design, shedding/carriage, and serologic resistance prediction | B | src-fcv-003, src-fcv-011, src-fcv-012, src-fcv-013, src-fcv-017, src-fcv-022 | endpoint-control frame, not final hierarchy |
| FE2 | Neutralising breadth, cellular cross-immunity, and regional strain fit are related but not interchangeable endpoint families | B | src-fcv-003, src-fcv-005, src-fcv-010, src-fcv-022 | not vaccine-product ranking |
| FE3 | Acute-disease mitigation, chronic-carrier prevention, and vaccine-failure investigation should not be written as one endpoint bucket | B | src-fcv-012, src-fcv-017, src-fcv-024 | not field-effectiveness claim |
| FE4 | Therapy endpoint exists but remains bounded: assay-stage, interferon-sensitivity, and in vivo CpG49 do not equal routine treatment | B | src-fcv-008, src-fcv-014, src-fcv-018 | not standard-of-care |

## Evidence-Depth Caveat

This page sits on a fully deep-extracted FCV source-card layer (24/24 papers). Endpoint anchors: neutralisation breadth (`src-fcv-003`), regional vaccine-fit (`src-fcv-005`), early field-fit stress testing (`src-fcv-010`), challenge protection (`src-fcv-011`), serology-resistance (`src-fcv-012`), replication-deficient platform (`src-fcv-013`), persistence control (`src-fcv-017`), in vivo therapy (`src-fcv-018`), interferon sensitivity (`src-fcv-008`), assay-stage discovery (`src-fcv-014`), cellular immunity (`src-fcv-022`), and vaccine-failure interpretation (`src-fcv-024`). This is now an endpoint handbook rather than a branch-separation page.

## Core Takeaway

FCV endpoint language stays separated between neutralisation breadth, challenge protection, acute clinical severity, viral shedding, carrier-state persistence, cellular immunity, and serologic resistance prediction. These are related but not interchangeable endpoint families.

## Endpoint Hierarchy

### Endpoint 1: Acute Clinical-Disease Reduction

Vaccination reduces disease burden. This is the most defensible vaccine benefit claim.

**Key boundary:** Disease reduction is not infection elimination.

**Lead sources:** `src-fcv-003`, `src-fcv-011`

### Endpoint 2: Heterologous Challenge Protection

Challenge studies show cross-protection against heterologous strains, but this protection is broader than complete.

**Key boundary:** Challenge protection in controlled settings is not the same as field control.

**Lead sources:** `src-fcv-011`

### Endpoint 3: Cross-Neutralisation Breadth

Neutralising antibodies show broad but incomplete coverage against field isolates. Laboratory-strain neutralization can look materially cleaner than field-isolate coverage.

**Key boundary:** Breadth should be written as `broad but incomplete`, not as closure.

**Lead sources:** `src-fcv-003`, `src-fcv-010`

### Endpoint 4: Cellular Cross-Immunity

Cellular immunity explains vaccine benefit beyond neutralising-antibody readouts. This branch helps explain why seronegative cats can still be protected.

**Key boundary:** Cellular immunity expands protection understanding without replacing humoral measures.

**Lead sources:** `src-fcv-022`

### Endpoint 5: Shedding and Chronic-Carrier Persistence

Acute-disease mitigation does not equal chronic-carrier control. Persistence and immune evasion maintain transmission pressure despite vaccination.

**Key boundary:** Disease reduction and carrier-state control must stay separated.

**Lead sources:** `src-fcv-017`

### Endpoint 6: Serologic Resistance Prediction

Serology can predict resistance in vaccinated cats, but this does not become a universal no-booster answer.

**Key boundary:** Titer-based prediction has limits that should not be overclaimed.

**Lead sources:** `src-fcv-012`

### Endpoint 7: Therapy Branch

FCV has a real therapy endpoint branch with assay-stage discovery (`src-fcv-014`), interferon-sensitivity caution (`src-fcv-008`), and first in vivo immunostimulatory therapy (`src-fcv-018`). However, this branch remains experimental.

**Key boundary:** In vivo CpG49 benefit does not equal routine treatment guidance.

**Lead sources:** `src-fcv-008`, `src-fcv-014`, `src-fcv-018`

### Endpoint 8: Platform-Vaccine Design

Replication-deficient vaccine platforms show promise for broader neutralising responses, but this remains research-stage rather than product-ranking evidence.

**Key boundary:** Platform innovation does not create current-market recommendation language.

**Lead sources:** `src-fcv-013`

### Regional Strain Fit

Vaccine fit varies by geography. Regional epidemiology affects endpoint interpretation.

**Key boundary:** Vaccine-fit thinking should be geography-aware rather than universal.

**Lead sources:** `src-fcv-005`, `src-fcv-024`

## Source-Layer Reality

| Source | Role | Status |
|---|---|---|
| src-fcv-003 | neutralisation breadth: broad but incomplete | deep_extracted |
| src-fcv-005 | regional epidemiology: vaccine-locality pressure | deep_extracted |
| src-fcv-008 | interferon-sensitivity: heterogeneous, strain-sensitive | deep_extracted |
| src-fcv-010 | early field-fit: laboratory vs field-isolate gap | deep_extracted |
| src-fcv-011 | challenge protection: high-signal benefit, below market ranking | deep_extracted |
| src-fcv-012 | serology-resistance: predictive but bounded | deep_extracted |
| src-fcv-013 | platform-vaccine: research-stage, not product ranking | deep_extracted |
| src-fcv-014 | assay-stage therapy: enzyme and cell-culture hits | deep_extracted |
| src-fcv-017 | persistence-control: acute vs chronic separation | deep_extracted |
| src-fcv-018 | in vivo therapy: CpG49, bounded benefit | deep_extracted |
| src-fcv-022 | cellular immunity: benefit beyond titre logic | deep_extracted |
| src-fcv-024 | vaccine-failure: molecular interpretation required | deep_extracted |

## Current Owner Memo

- [FCV vaccine-persistence boundary memo](../../system/indexes/fcv-vaccine-persistence-boundary-memo.md)

## Guardrail

Do not build a premature FCV numeric leaderboard across titres, challenge readouts, platform-vaccine findings, and carriage outcomes. The eight endpoint families are now stabilized, but the branch still needs denser field-effectiveness and label/regulatory evidence before it becomes a product-ranking surface.

## What The Module Can Say Safely

- neutralisation breadth is broad but incomplete
- challenge protection exceeds titre logic but does not equal field control
- cellular immunity explains protection beyond antibody measures
- acute-disease mitigation and chronic-carrier control are separate endpoints
- therapy exists as a real branch but remains experimental
- vaccine-failure cases need molecular interpretation

## What The Module Should Not Say Yet

- do not flatten endpoint families into one protection metric
- do not rank current-market products by these endpoints
- do not treat platform-vaccine findings as current recommendations
- do not write therapy as routine treatment guidance
- do not claim universal booster policy from serology data

## Current Role

Use this page as the FCV endpoint handbook. The source-card layer is complete at 24/24 deep-extracted papers. Next gains come from field-effectiveness and label/regulatory evidence to enable product-level discussion.
