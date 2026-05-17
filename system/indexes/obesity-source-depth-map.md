---
id: obesity-source-depth-map
type: index
topic: obesity
question_type: navigation
language: bilingual
last_compiled_at: 2026-05-17
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# Source Depth Map — Obesity

## Use

Use this map to decide which obesity source cards need deep extraction before any obesity topic page becomes an answer surface.

## Depth Definitions

- `partial`: first-pass card exists, but article facts are not fully extracted.
- `title_only`: only title / DOI / bibliographic role has been verified.
- `abstract_weighted`: at least some accessible abstract text has been used, but not full-text extraction.
- `deep_extracted`: structured source worksheet and reusable card facts exist.

## Coverage Summary

| Disease | Source Cards | partial | full | title_only | abstract_weighted | deep_extracted |
|---|---:|---:|---:|---:|---:|---:|
| Obesity | 87 | 83 | 4 | 43 | 40 | 4 |

## Tier 1 — Bootstrap Anchors

| Source ID | Title Short | Current Role | Depth | Verification | Priority | Key Gap |
|---|---|---|---|---|---|---|
| src-obesity-001 | Feline obesity broad review | shell / assessment | full | deep_extracted | DONE | usable for 5-branch architecture, prevalence ranges (11.5-63%), risk factors, associated conditions; not specific rankings or body condition thresholds |
| src-obesity-004 | Domestic cat overweight/obesity risk and pathologies | risk / associated pathologies | full | deep_extracted | DONE | usable for risk-factor architecture (extrinsic/intrinsic) and associated-pathology visibility; not specific prevalence or ranking |
| src-obesity-005 | Target population and prevention | prevention | full | deep_extracted | DONE | usable for prevention architecture and target population (post-neuter kittens 5-12mo); not specific protocols |
| src-obesity-008 | Insulin sensitivity decreases with obesity | mechanism / diabetes bridge | full | deep_extracted | DONE | usable for bounded mechanism and diabetes-bridge placement; not screening or treatment advice |

## Tier 2 — Management Context

| Source ID | Title Short | Current Role | Depth | Verification | Priority | Key Gap |
|---|---|---|---|---|---|---|
| src-obesity-002 | Canine/feline obesity review | broad management context | partial | title_only | MEDIUM | split canine vs feline claims |
| src-obesity-003 | Canine/Feline obesity management | management | partial | title_only | MEDIUM | split species and evidence strength |
| src-obesity-006 | Management of obesity in cats | feline management | partial | title_only | MEDIUM | extract currentness and evidence basis |
| src-obesity-007 | Environment and behavior modification | behavior / environment branch | partial | title_only | MEDIUM | verify species scope and recommendation basis |
| src-obesity-080 | Weight loss diet / activity / microbiota | weight-loss study | partial | abstract_weighted | MEDIUM | needs methods/results extraction before diet or activity claims |

## Tier 1 Completion Status (2026-05-17)

All 4 Tier 1 sources deep-extracted. Architecture pages complete:

| Page | Sources | Status |
|------|---------|--------|
| mechanism-overview | 001, 004, 005, 008 | DONE + bilingual |
| risk-and-recognition | 001, 004, 005 | DONE + bilingual |
| prevention | 001, 005 | DONE + bilingual |
| diabetes-bridge | 001, 004, 008 | DONE + bilingual |

## Next Extraction Queue

For Tier 2 management/intervention context (if needed):

1. `src-obesity-080` — weight-loss diet / activity / microbiota study
2. `src-obesity-002` — broad management context
3. `src-obesity-003` — management review
4. `src-obesity-006` — feline management
5. `src-obesity-007` — environment/behavior modification

For assessment-methods page:
- Requires body condition scoring full-text extraction from Tier 1 sources or additional assessment-specific sources

The 2026-05-14 full structured abstract run created abstract-only worksheets for all 44 obesity `abstract_weighted` cards:

- report: [feline diabetes / obesity structured abstract full index](feline-diabetes-obesity-structured-abstract-full-20260514.md)
- 43 obesity cards remain `title_only` with no structured abstract worksheet

## Prioritized Extraction Queue (2026-05-17)

Based on scoring: reviews (+5), diabetes-bridge keywords (+3), year ≥2020 (+2), endpoints present (+1).

| Rank | Source ID | Year | Score | Flags |
|---:|---|---:|---:|---|
| 1 | src-obesity-004 | 2024 | 8 | REVIEW, RECENT |
| 2 | src-obesity-005 | 2024 | 8 | REVIEW, RECENT |
| 3 | src-obesity-008 | 2001 | 4 | DM-BRIDGE |
| 4 | src-obesity-081 | 2012 | 3 | DM-BRIDGE |
| 5 | src-obesity-046 | 2011 | 3 | DM-BRIDGE |
| 6 | src-obesity-079 | 2009 | 3 | DM-BRIDGE |
| 7 | src-obesity-069 | 1999 | 3 | DM-BRIDGE |
| 8 | src-obesity-030 | 2025 | 2 | RECENT |
| 9 | src-obesity-039 | 2025 | 2 | RECENT |
| 10 | src-obesity-050 | 2025 | 2 | RECENT |

## 2026-05-17 Manual Sample Result

The staged 5-sample promotion batch identified `src-obesity-008` as the only candidate safe for branch-placement promotion. A manual deep-extraction sample was completed before any durable automation or skill codification.

- sample completed: `src-obesity-008`
- result: partial promote for mechanism / diabetes-bridge placement only
- still blocked: public obesity guidance, risk ranking, prevention claims, screening thresholds, and weight-loss advice
- next manual samples before any recurring extraction skill: `src-obesity-004`, `src-obesity-005`, and `src-obesity-001` if source access is available

## Maintenance

Update this map after every obesity source-card ingest, source-check, or deep extraction. The 2026-05-13 full first-pass bootstrap created `src-obesity-009` through `src-obesity-087`; the 2026-05-14 full source-check leaves obesity at 44 `abstract_weighted` and 43 `title_only`, with no deep-extracted obesity source yet.

2026-05-17 update: Added year metadata to 32 source cards (31 from DOI patterns, 1 from Crossref lookup). 6 cards still missing year (no DOI available): src-obesity-018, 025, 029, 047, 077, 083. Year coverage now 81/87.

2026-05-17 update: Deep-extracted all 4 Tier 1 bootstrap anchors (`src-obesity-001`, `src-obesity-004`, `src-obesity-005`, `src-obesity-008`). Current obesity depth is 4 deep-extracted sources, 40 abstract-weighted sources, and 43 title-only sources. The obesity module can now support bounded architecture pages for the 5-branch shell, risk-factor architecture, prevention, and diabetes-bridge mechanism.
