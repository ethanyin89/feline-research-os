---
id: feline-fip-intake-manifest-20260608
type: intake-manifest
topic: fip
species: feline
last_compiled_at: 2026-06-08
verification_status: compiled
decision_grade: no
language_qa_status: not_applicable
owner: codex
status: active
---

# FIP Literature Sheet Intake Manifest

**Source:** Google Sheet gid=639162275
**Date:** 2026-06-08
**Estimated rows:** ~150+

## Existing Coverage

The vault has 24 FIP source cards (src-fip-001 through src-fip-024), all at `deep_extracted` status.

### Core Topics Already Covered

| Topic | Sources | Status |
|-------|---------|--------|
| GS-441524 treatment | src-fip-016, src-fip-017, src-fip-013, src-fip-024 | deep_extracted |
| Remdesivir combination | src-fip-019 | deep_extracted |
| Pathogenesis/mutation | src-fip-009, src-fip-004, src-fip-018 | deep_extracted |
| Diagnosis methods | src-fip-010, src-fip-022, src-fip-023 | deep_extracted |
| Epidemiology | src-fip-005, src-fip-008, src-fip-020 | deep_extracted |
| Clinical staging | src-fip-006, src-fip-015 | deep_extracted |

## Sheet Cross-Reference Summary

| Classification | Count | Notes |
|---------------|-------|-------|
| Already in vault | ~120 | Matches existing src-fip-* titles/DOIs |
| New 2024 candidates | 4 | See below |
| Duplicates/variants | ~20 | Same study, different links |
| Out-of-scope | ~6 | Non-feline, generic coronavirus |

## New 2024 Candidates (Not in Vault) — DOIs Recovered

| # | Title | Journal | Year | DOI | Priority |
|---|-------|---------|------|-----|----------|
| 1 | Assessing the feasibility of applying machine learning to diagnosing non-effusive FIP | Sci Rep | 2024 | 10.1038/s41598-024-52577-4 | HIGH |
| 2 | Molnupiravir treatment of 18 cats with FIP: A case series | JVIM | 2023 | 10.1111/jvim.16832 | HIGH |
| 3 | Open label clinical trial of molnupiravir as first-line treatment for effusive FIP | JVIM | 2024 | 10.1111/jvim.17187 | HIGH |
| 4 | GS-441524 and molnupiravir are similarly effective for treatment of cats with FIP | Front Vet Sci | 2024 | 10.3389/fvets.2024.1422408 | HIGH |

**Intake Status:** COMPLETED — 4 source cards created (src-fip-025 through src-fip-028)

## Action Required

1. **DOI Recovery** for new candidates - need full citation to verify uniqueness
2. **Full text access** check before creating source cards
3. **Classification** of any remaining unmatched entries

## Intake Decision

The FIP module is already well-covered (24 deep_extracted sources). The 4 new 2024 candidates represent:
- **Molnupiravir** — new antiviral option (alternative to GS-441524)
- **Machine learning diagnosis** — emerging diagnostic technology
- **Proteomics** — biomarker research

**Recommendation:** Intake the 2-3 molnupiravir and ML diagnosis papers when full text becomes available. These extend the treatment and diagnosis branches without requiring restructure.

## Intake Summary

| Source ID | Title | Status |
|-----------|-------|--------|
| src-fip-025 | ML diagnosis for non-effusive FIP | abstract_weighted |
| src-fip-026 | Molnupiravir 18 cats case series | **deep_extracted** |
| src-fip-027 | Molnupiravir clinical trial (effusive) | abstract_weighted |
| src-fip-028 | GS-441524 vs molnupiravir comparison | **deep_extracted** |

**Deep extraction worksheets created:**
- `system/indexes/src-fip-026-deep-extraction-round1.md`
- `system/indexes/src-fip-028-deep-extraction-round1.md`

## Next Steps

| Item | Action | Priority |
|------|--------|----------|
| src-fip-025, src-fip-027 | Upgrade to deep_extracted when full text available | MEDIUM |
| FIP treatment page | Update to include molnupiravir as alternative | HIGH |
| FIP diagnosis page | Consider ML diagnostic tool mention | LOW |

**Completed:**
- src-fip-026: Deep extracted (molnupiravir case series)
- src-fip-028: Deep extracted (GS-441524 vs molnupiravir comparison)
