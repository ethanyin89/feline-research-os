---
id: karpathy-extraction-priority-queue
type: system
topic: content-pipeline
last_compiled_at: 2026-06-09
verification_status: compiled
decision_grade: no
status: active
---

# Karpathy Gap Closure: Extraction Priority Queue

## Key Finding

Of **334 abstract_weighted sources**, only **63 are branch-controlling** (cited in topic pages).
The other **271 are supporting** and can remain at abstract_weighted indefinitely.

This reduces the Karpathy extraction gap from 334 → 63 sources.

## Distribution

| Disease | Branch-Controlling | Supporting | Action |
|---------|-------------------|------------|--------|
| Cancer | 58 | 31 | **Priority** — controls 6 branch pages |
| FIP | 2 | 0 | Medium — src-fip-025, src-fip-027 |
| Diabetes | 2 | 84 | Low — most are supporting |
| Obesity | 1 | 79 | Low — most are supporting |
| CKD | 0 | 19 | None — all supporting |
| FCV | 0 | 79 | None — all supporting |

## Priority Queue (Top 20)

| Rank | Source | Citations | DOI Status | Topic Impact |
|------|--------|-----------|------------|--------------|
| 1 | src-cancer-095 | 12 | ✓ | oral-squamous-cell-carcinoma |
| 2 | src-cancer-047 | 12 | ✓ | injection-site-sarcoma |
| 3 | src-cancer-046 | 11 | ✓ | oral-squamous-cell-carcinoma |
| 4 | src-cancer-063 | 8 | ✓ | lymphoma |
| 5 | src-cancer-062 | 8 | ✓ | oral-squamous-cell-carcinoma |
| 6 | src-cancer-055 | 8 | ✓ | oral-squamous-cell-carcinoma |
| 7 | src-cancer-048 | 7 | ✗ | lymphoma |
| 8 | src-cancer-064 | 6 | ✓ | registry-and-prevalence |
| 9 | src-cancer-061 | 6 | ✓ | oral-squamous-cell-carcinoma |
| 10 | src-cancer-009 | 6 | ✓ | mammary-carcinoma |
| 11 | src-cancer-060 | 5 | ✗ | current-state-dashboard |
| 12 | src-cancer-056 | 5 | ✓ | current-state-dashboard |
| 13 | src-cancer-054 | 5 | ✓ | current-state-dashboard |
| 14 | src-cancer-052 | 5 | ✓ | current-state-dashboard |
| 15 | src-cancer-031 | 5 | ✗ | oral-squamous-cell-carcinoma |
| 16 | src-cancer-021 | 5 | ✓ | oral-squamous-cell-carcinoma |
| 17 | src-cancer-012 | 5 | ✗ | mammary-carcinoma |
| 18 | src-fip-025 | 3 | ✓ | fip/index |
| 19 | src-fip-027 | 2 | ✓ | fip/index |
| 20 | src-diabetes-118 | 2 | ✓ | diabetes topic |

## Full Priority List (63 sources)

| Source | Citations | Disease | DOI |
|--------|-----------|---------|-----|
| src-cancer-095 | 12 | cancer | ✓ |
| src-cancer-047 | 12 | cancer | ✓ |
| src-cancer-046 | 11 | cancer | ✓ |
| src-cancer-063 | 8 | cancer | ✓ |
| src-cancer-062 | 8 | cancer | ✓ |
| src-cancer-055 | 8 | cancer | ✓ |
| src-cancer-048 | 7 | cancer | ✗ |
| src-cancer-064 | 6 | cancer | ✓ |
| src-cancer-061 | 6 | cancer | ✓ |
| src-cancer-009 | 6 | cancer | ✓ |
| src-cancer-060 | 5 | cancer | ✗ |
| src-cancer-056 | 5 | cancer | ✓ |
| src-cancer-054 | 5 | cancer | ✓ |
| src-cancer-052 | 5 | cancer | ✓ |
| src-cancer-031 | 5 | cancer | ✗ |
| src-cancer-021 | 5 | cancer | ✓ |
| src-cancer-012 | 5 | cancer | ✗ |
| src-cancer-090 | 4 | cancer | ✓ |
| src-cancer-088 | 4 | cancer | ✓ |
| src-cancer-086 | 4 | cancer | ✓ |
| src-cancer-080 | 4 | cancer | ✓ |
| src-cancer-075 | 4 | cancer | ✗ |
| src-cancer-074 | 4 | cancer | ✓ |
| src-cancer-071 | 4 | cancer | ✓ |
| src-cancer-065 | 4 | cancer | ✓ |
| src-cancer-049 | 4 | cancer | ✓ |
| src-cancer-044 | 4 | cancer | ✗ |
| src-cancer-043 | 4 | cancer | ✓ |
| src-cancer-032 | 4 | cancer | ✓ |
| src-cancer-028 | 4 | cancer | ✗ |
| src-cancer-025 | 4 | cancer | ✓ |
| src-cancer-015 | 4 | cancer | ✓ |
| src-cancer-013 | 4 | cancer | ✗ |
| src-cancer-007 | 4 | cancer | ✓ |
| src-fip-025 | 3 | fip | ✓ |
| src-cancer-102 | 3 | cancer | ✓ |
| src-cancer-101 | 3 | cancer | ✓ |
| src-cancer-084 | 3 | cancer | ✗ |
| src-cancer-081 | 3 | cancer | ✓ |
| src-cancer-073 | 3 | cancer | ✓ |
| src-cancer-050 | 3 | cancer | ✗ |
| src-cancer-045 | 3 | cancer | ✓ |
| src-cancer-042 | 3 | cancer | ✗ |
| src-cancer-036 | 3 | cancer | ✓ |
| src-cancer-034 | 3 | cancer | ✓ |
| src-cancer-022 | 3 | cancer | ✓ |
| src-cancer-020 | 3 | cancer | ✗ |
| src-cancer-018 | 3 | cancer | ✗ |
| src-cancer-017 | 3 | cancer | ✗ |
| src-cancer-016 | 3 | cancer | ✗ |
| src-fip-027 | 2 | fip | ✓ |
| src-diabetes-118 | 2 | diabetes | ✓ |
| src-cancer-100 | 2 | cancer | ✓ |
| src-cancer-091 | 2 | cancer | ✓ |
| src-cancer-069 | 2 | cancer | ✓ |
| src-cancer-041 | 2 | cancer | ✗ |
| src-cancer-038 | 2 | cancer | ✓ |
| src-cancer-029 | 2 | cancer | ✓ |
| src-cancer-026 | 2 | cancer | ✓ |
| src-obesity-085 | 1 | obesity | ✓ |
| src-diabetes-025 | 1 | diabetes | ✓ |
| src-cancer-005 | 1 | cancer | ✓ |
| src-cancer-001 | 1 | cancer | ✓ |

## Accessibility Analysis (Updated)

| Category | Count | Action |
|----------|-------|--------|
| **OPEN ACCESS** | 19 | **Can extract NOW** |
| Subscription | 16 | Need institutional access |
| Unknown publisher | 12 | Need to verify |
| No DOI | 16 | Need DOI recovery first |

### 19 Open Access Sources (Ready for Deep Extraction)

| Source | Citations | Publisher | Full-Text URL |
|--------|-----------|-----------|---------------|
| src-cancer-095 | 12 | MDPI Vet Sci | https://doi.org/10.3390/vetsci9100558 |
| src-cancer-063 | 8 | MDPI CIMB | https://doi.org/10.3390/cimb48020218 |
| src-cancer-062 | 8 | Hindawi | https://doi.org/10.1155/2014/675172 |
| src-cancer-061 | 6 | MDPI Biology | https://doi.org/10.3390/biology11010054 |
| src-cancer-056 | 5 | BMC Cancer | https://doi.org/10.1186/s12885-019-6483-6 |
| src-cancer-054 | 5 | Breast Cancer Res | https://doi.org/10.1186/bcr790 |
| src-cancer-021 | 5 | Hindawi | https://doi.org/10.1155/2013/502197 |
| src-cancer-088 | 4 | BMC Cancer | https://doi.org/10.1186/s12885-018-4650-9 |
| src-cancer-032 | 4 | BMC Cancer | https://doi.org/10.1186/s12885-018-4323-8 |
| src-cancer-101 | 3 | MDPI Cancers | https://doi.org/10.3390/cancers13061248 |
| src-cancer-081 | 3 | MDPI Cells | https://doi.org/10.3390/cells11162578 |
| src-cancer-036 | 3 | PLOS ONE | https://doi.org/10.1371/journal.pone.0221776 |
| src-cancer-022 | 3 | BMC Vet Res | https://doi.org/10.1186/s12917-014-0185-8 |
| src-cancer-100 | 2 | MDPI Animals | https://doi.org/10.3390/ani11082321 |
| src-cancer-091 | 2 | MDPI Vet Sci | https://doi.org/10.3390/vetsci8080164 |
| src-cancer-069 | 2 | BMC Cancer | https://doi.org/10.1186/1471-2407-10-156 |
| src-diabetes-025 | 1 | MDPI IJMS | https://doi.org/10.3390/ijms252313195 |
| src-cancer-005 | 1 | MDPI Vet Sci | https://doi.org/10.3390/vetsci2030111 |
| src-cancer-001 | 1 | MDPI Vet Sci | https://doi.org/10.3390/vetsci9100547 |

**Immediate opportunity:** Extracting these 19 sources closes **30%** of the branch-controlling gap.

## Implementation Plan

### Phase 1: Open Access Extraction (19 sources) — IN PROGRESS

These 19 sources have free full-text. Run `/cancer-deep-extract` for each:

**COMPLETED (3/19):**
- [x] src-cancer-095 — 12 citations, FOSCC etiology systematic review ✅ 2026-06-09
- [x] src-cancer-063 — 8 citations, alimentary lymphoma molecular landscape ✅ 2026-06-09
- [x] src-cancer-062 — 8 citations, pamidronate bone-invasive tumors ✅ 2026-06-09

**REMAINING (16/19):**
```bash
# Next priority (by citation count)
/cancer-deep-extract src-cancer-061  # 6 citations, translational oncology
/cancer-deep-extract src-cancer-056  # 5 citations, CK2 gene expression
/cancer-deep-extract src-cancer-054  # 5 citations, FMC model breast cancer
/cancer-deep-extract src-cancer-021  # 5 citations, FOSCC as HNSCC model
/cancer-deep-extract src-cancer-088  # 4 citations, FMC cell lines
/cancer-deep-extract src-cancer-032  # 4 citations, BB-Cl-Amidine PAD
```

### Phase 2: DOI Recovery (16 sources)

```bash
# Recover DOI via PubMed title search
python3 scripts/doi_recovery.py --source-ids "src-cancer-048,src-cancer-060,src-cancer-031,src-cancer-012,src-cancer-075,src-cancer-044,src-cancer-028,src-cancer-013,src-cancer-084,src-cancer-050,src-cancer-042,src-cancer-020,src-cancer-018,src-cancer-017,src-cancer-016,src-cancer-041"
```

### Phase 3: Unknown Publisher Check (12 sources)

Verify if these DOIs are open access:
- `10.1089/*` — Mary Ann Liebert (sometimes OA)
- `10.21873/*` — In Vivo (OA)
- `10.1038/*` — Nature (check specific article)
- `10.1002/*` — Wiley (usually subscription)

### Phase 4: Subscription Sources (16 sources)

These require institutional access or user-provided PDFs:
- Elsevier (10.1016/*)
- SAGE (10.1177/*)
- Wiley (10.1111/*)
- Springer (10.1007/*)

## Metrics

| Metric | Current | After Phase 1 | Target |
|--------|---------|---------------|--------|
| Branch-controlling at deep_extracted | **3/63 (5%)** | **19/63 (30%)** | 40/63 (63%) |
| Open access sources extracted | **3/19** | 19/19 | 19/19 |
| Cancer branches with deep control | 0/6 | 4/6 | 6/6 |
| Karpathy extraction alignment | 30% | **45%** | 60% |

### Session Progress (2026-06-09)

| Source | Citations | Status | Topic Impact |
|--------|-----------|--------|--------------|
| src-cancer-095 | 12 | ✅ deep_extracted | oral-squamous-cell-carcinoma etiology |
| src-cancer-063 | 8 | ✅ deep_extracted | lymphoma alimentary molecular |
| src-cancer-062 | 8 | ✅ deep_extracted | OSCC pamidronate palliative |

### Phase 1 Impact (19 open access sources)

If all 19 open access sources are deep-extracted:
- Branch-controlling gap closes from 63 → 44 (30% reduction)
- Cancer module gets 18 more deep-extracted sources (9 → 27)
- Mammary, OSCC, lymphoma branches gain deep control

## Not In Scope

The **271 supporting sources** (not cited in topic pages) remain at `abstract_weighted`.
This is acceptable per Karpathy principles — wiki quality matters more than uniform depth.
