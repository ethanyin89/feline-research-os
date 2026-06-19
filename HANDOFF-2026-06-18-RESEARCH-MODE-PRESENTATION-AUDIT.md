# HANDOFF: Research Mode Presentation Audit Note

Date: 2026-06-18
Branch: idea-chatacademia-research-workbench
Status: COMPLETE

## Summary

Continued the presentation-layer work after reviewing the deep research thought-path case study.

The change is intentionally small and focused: Research Mode now shows a concise **Research contract and audit note** at the top of its generated answer. This makes the output more trustworthy without exposing raw chain-of-thought.

## Why

The agent.ii.inc feline HCM case showed that detailed visible activity can create trust, but raw execution traces are not the right trust artifact. Users need to see:

- how their request was interpreted;
- what scope and source hierarchy were used;
- how "best papers" are ranked;
- whether "high-impact" is a strict metric or a softer higher-visibility proxy;
- what freshness boundary applies when PubMed or other external sources are used.

## Files Changed

- `scripts/research_mode.py`
- `scripts/app.py`

## What Changed

### 1. Added user-facing research contract section

New helper:

- `_build_research_contract_section(...)`

The section exposes:

- interpreted request;
- disease/topic boundary;
- standard conversion path;
- local source-card count;
- best-paper ranking formula;
- high-impact wording boundary;
- PubMed freshness/audit boundary.

### 2. Added scope label helper

New helper:

- `_research_scope_label(...)`

This keeps disease labels readable in English and Chinese.

### 3. Preserved audit boundary for "latest"

Research Mode now states that:

- PubMed augmentation helps freshness when available;
- external results need intake before becoming audited vault evidence;
- missing PubMed results are not proof that no newer paper exists;
- local-only output cannot claim live external database coverage.

### 4. Aligned UI source-card order with report ranking

`handle_research_query()` now returns `source_ids` from `rank_sources(cards, top_n=10)` instead of the first ten parsed source cards. This keeps the source cards closer to the order of the paper list shown in the answer.

### 5. Fixed ambiguous top-count wording

Changed wording from "Found 10 relevant sources" to "Showing the top 10 ranked local-vault sources" so users do not confuse the displayed top-N with the full local corpus count.

### 6. Rendered the contract as a UI panel

Added app-level splitting/rendering helpers:

- `split_research_contract(...)`
- `render_research_contract_panel(...)`

Research Mode still returns the complete text for CLI and saved-output compatibility, but Streamlit now separates the audit note from the literature-review body:

1. query classification / refinement;
2. research contract panel;
3. actual literature review;
4. evidence profile, source cards, loaded documents, and trace.

This avoids burying the report under a long preamble while still making the research boundary visible.

## Verification

Commands run:

```bash
python3 -m py_compile scripts/research_mode.py scripts/app.py scripts/query.py
python3 scripts/test_research_mode.py --verbose
python3 scripts/test_query.py
```

Results:

- `py_compile`: pass
- Research Mode health check: pass
- Query test suite: 113 passed, 0 failed

The warnings about a skipped large figure and path traversal are expected coverage checks from the existing test suite, not failures.

## Current Product State

Presentation layer now has three relevant pieces:

1. ordinary progress and answer sections;
2. source-card metadata, references, and cited-by expansion;
3. a visible Research Mode contract panel that is separate from the report body.

The next presentation-layer step should be a structured audit surface, not more free-form thought text. Candidate next work:

- turn the contract note into structured data returned from Research Mode;
- add a scope-change ledger for papers added/removed during recursive research;
- add acceptance checks for `latest`, `high-impact`, and CSV/report/source consistency.
