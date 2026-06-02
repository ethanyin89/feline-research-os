---
id: cancer-abstract-extraction-sample-20260602
type: system
topic: content-pipeline
question_type: extraction-sample
language: bilingual
last_compiled_at: 2026-06-02
verification_status: source_checked
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# Cancer Abstract Extraction Sample, 2026-06-02

## Scope

Manual 5-card sample from the remaining `partial` feline cancer source cards. This is not a bulk promotion and does not add reader-facing topic claims.

## Method

1. Count current cancer extraction depths.
2. Take the next partial-card queue head with:
   `grep -l "extraction_depth: partial" raw/papers/src-cancer-*.md | head -10`
3. Search PubMed E-utilities by title.
4. Reject broad search results when the returned PMID title does not match the card.
5. Fetch the PubMed abstract only after title/PMID match is clear.
6. Upgrade source-card metadata and add abstract-level summary plus explicit boundary.
7. Run `python3 scripts/health.py`.

## Sample Results

| Source card | PMID | DOI | Result |
|---|---:|---|---|
| `src-cancer-057` | 22366263 | `10.1016/j.yexcr.2012.02.008` | Upgraded to abstract-weighted; FMC stem-like / tumor-initiating-cell model. |
| `src-cancer-058` | 22100245 | `10.1016/j.rvsc.2011.10.016` | Upgraded to abstract-weighted; in vitro myxoma-virus susceptibility signal. |
| `src-cancer-059` | 11896610 | `10.1038/sj.onc.1205221` | Upgraded to abstract-weighted; feline STK/RON comparative molecular evidence. |
| `src-cancer-067` | 25093734 | `10.1371/journal.pone.0104337` | Upgraded to abstract-weighted; preclinical GLV-5b451 oncolytic-vaccinia model evidence. |
| `src-cancer-070` | 10814873 | `10.1016/s0304-3835(00)00337-2` | Upgraded to abstract-weighted; p53 immunoreactivity across selected feline tumour types. |

## Counts After Sample

- `extraction_depth: abstract`: 61
- `extraction_depth: partial`: 35
- `extraction_depth: title_only`: 0

## Verification

`python3 scripts/health.py` exited 0 and wrote `system/health-checks/health-report-20260602.md`.

Health summary remained PASS for markdown links, query tests, ordinary-user vault eval, source IDs, schema fields, source refs, reader source IDs, and decision-grade gates. The existing thin-source usage WARN remains on cancer high-visibility pages and is not introduced by this sample.

## Boundary

These cards are abstract-weighted only. They can support source ownership, branch routing, and future extraction priority. They should not be used alone for diagnosis, treatment selection, prognosis, or client-facing recommendations.

Do not continue by broad PubMed title search alone. Several long-title searches can return plausible-looking but false broad matches. Always verify the fetched PubMed title before upgrading a card.
