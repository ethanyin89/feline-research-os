---
id: cancer-fulltext-availability-sample-5-20260530
type: system
topic: cancer
question_type: fulltext-availability-check
language: zh
last_compiled_at: 2026-05-30
verification_status: manual-sample
decision_grade: no
owner: codex
status: active
---

# Cancer Full-Text Availability Sample 5, 2026-05-30

Source set: registry / prevalence continuation sample.

## Rule

This is a 2-card continuation inside the already approved 3-10 source deep-extraction sample flow. It records access leads and blockers before promotion. It does not bulk-promote cards.

## Candidates

| Source | Role | DOI | Access result | Decision |
|---|---|---|---|---|
| `src-cancer-002` | Swiss registry / epidemiology | `10.1016/j.jcpa.2016.01.008` | ETH Research Collection record and browser-readable PDF text available | deep-extract as registry denominator anchor |
| `src-cancer-007` | South Africa hospital-admissions prevalence comparator | `10.6000/1927-5129.2015.11.53` | publisher page and abstract readable; direct PDF download returned verification / 404 during local probing | keep abstract-weighted and full-text blocked |

## Access Notes

### `src-cancer-002`

- ETH Research Collection record confirmed open-access status, Journal of Comparative Pathology volume 154, pages 195-210, and DOI.
- Browser-readable PDF text exposed the article body and was sufficient for a round-1 worksheet.
- Local direct fetch saved an HTML error shell, so local file download should not be treated as the verified extraction route.

### `src-cancer-007`

- SET Publisher article page lists title, author, journal, DOI, keywords, and abstract.
- The publisher abstract reports a hospital-admissions denominator and SCC-heavy tumor mix, which is enough to prioritize the source.
- Direct PDF retrieval was not verified in this environment; do not promote beyond abstract-weighted status until full text is readable.

## Outcome

- `src-cancer-002` promoted to `deep_extracted`.
- `src-cancer-007` upgraded from title-only to abstract-weighted / full-text blocked.
- Registry and prevalence synthesis may use `src-cancer-002` as the controlling denominator caveat, with `src-cancer-007` listed only as a blocked comparator lead.
