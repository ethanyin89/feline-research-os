# Handoff: Research Mode Presentation + Evidence Depth Queue

Date: 2026-06-19

## Classification

This task was handled as **排查 + 方案落地**.

The immediate failure was presentation-layer trust: the result page mixed English body text into a Chinese report, scrolled users away from the start of the report, exposed weak placeholder evidence as if it were ready, and rendered next-action cards as inert or poorly normalized UI.

## Changes Completed

### 0. Readability Follow-up

After browser review, the first presentation fix was still too hard to read:

- each paper was rendered inside a dense numbered-list paragraph
- Chinese fields were present, but they did not explain why the user should open the paper
- some entries used generic template language instead of extracted research signals

The paper entry format was changed again:

- each paper now renders as its own subsection
- fields are now:
  - `文献信息`
  - `链接`
  - `为什么值得读`
  - `关键发现`
  - `证据边界`
  - `临床相关性`
- reading hooks are generated from extracted summaries, supported conclusions, quoted facts, and theme-specific rules
- sample-size signals are localized, e.g. `12 只猫`, and stage labels such as `stage 4 cats` are not misread as sample size
- a regression caught and fixed one rule collision where a proteinuria paper was incorrectly described with a metabolomics/machine-learning hook

### 0.1 Link + Scroll Follow-up

Browser review exposed two remaining reader-path failures:

- some paper entries had no visible accessible link because the renderer only used DOI/PMID/PMCID and ignored `links.url`
- after research search, the page could still land near the lower part of the result instead of the start of the answer

Fixes:

- `SourceCard` now preserves `links.url`
- paper entries use locator priority:
  1. DOI
  2. PMID
  3. PMCID
  4. source URL
- the presentation regression now checks that the first recommended paper blocks contain `链接`
- result-page scrolling now uses the latest `#research-result-top` anchor and repeats scroll correction after render delays, so Streamlit chat input/history rendering does not pull the viewport down again

Browser QA for CKD confirmed:

- latest research anchor top was at the viewport top
- visible result began at the research contract/report start, not at the lower paper list
- recommended section had 15 visible `链接` fields
- previously linkless examples now render URLs, including OUP/JVIM article URLs

### 1. Chinese/English Report Contract

Research Mode now emits a bilingual deliverable with Chinese first and English second.

- `## 中文报告` appears before `## English report`.
- Chinese paper entries now use Chinese structured fields:
  - `为什么值得读`
  - `关键发现`
  - `证据边界`
  - `临床相关性`
- The output avoids the previous failure mode where only headings were Chinese while the paper summaries remained English.
- The English report is still preserved as a separate section for downstream use.

### 2. Evidence Readiness Filter

Reader-facing recommendations now exclude records that are not evidence-ready.

Excluded from main recommendation lists:

- `verification_status=title_only`
- metadata-only records without extracted facts, conclusions, or usable summaries
- first-pass triage / placeholder records

These are not hidden. They are moved into a separate depth queue.

### 3. Depth Extraction Queue

Added a persistent queue for important but not-yet-reader-ready records:

- `system/indexes/research-depth-queue.csv`
- `system/indexes/research-depth-queue.md`

Generated scope:

- 8 diseases
- 10 records per disease
- 80 queued records total

The queue includes the current verification state and reason, such as title-only, missing extracted claims, or first-pass triage content.

### 3.1 Depth Queue Sample Extraction

Started the depth-processing stage with a 5-source sample rather than a one-off manual patch.

New script:

- `scripts/depth_queue_extraction.py`

Sample generated:

- `system/indexes/depth-queue-extraction-sample-20260619.md`
- `system/indexes/src-ckd-128-depth-queue-extraction-round1.md`
- `system/indexes/src-hcm-169-depth-queue-extraction-round1.md`
- `system/indexes/src-fip-070-depth-queue-extraction-round1.md`
- `system/indexes/src-diabetes-035-depth-queue-extraction-round1.md`
- `system/indexes/src-obesity-039-depth-queue-extraction-round1.md`

Sample sources:

- CKD: `src-ckd-128`
- HCM: `src-hcm-169`
- FIP: `src-fip-070`
- diabetes: `src-diabetes-035`
- obesity: `src-obesity-039`

Boundary:

- worksheets use Crossref/PubMed abstract metadata only
- source cards were not modified
- topic pages were not modified
- outputs are review inputs for future source-card updates, not reader-facing clinical claims

### 4. Result Page Scroll Behavior

Research results now insert a `#research-result-top` marker and the app scrolls to the result start after rendering, rather than landing at the page bottom.

Browser QA for CKD showed:

- `scrollY: 0`
- report content visible from the top

### 5. Next Actions

Next actions now render as real Streamlit buttons instead of static cards.

Fixed:

- `深入了解ckd的机制` → `深入了解CKD的机制`
- button target becomes a user-facing query, e.g. `猫 CKD 病理生理机制`
- clicking the button queues a new search rather than acting as a dead visual card

### 6. Internal ID Leakage

Research output and page rendering were checked for internal source IDs.

Browser QA result:

- no `src-[disease]-NNN` leakage in the reader-facing result page

Internal IDs remain allowed in internal artifacts such as the depth queue.

## Files Changed

- `scripts/research_mode.py`
- `scripts/app.py`
- `core/result_presentation.py`
- `scripts/test_result_presentation.py`
- `scripts/check_research_mode_presentation.py`
- `scripts/build_research_depth_queue.py`
- `scripts/depth_queue_extraction.py`
- `system/indexes/research-depth-queue.csv`
- `system/indexes/research-depth-queue.md`
- `system/indexes/depth-queue-extraction-sample-20260619.md`
- `system/indexes/src-ckd-128-depth-queue-extraction-round1.md`
- `system/indexes/src-hcm-169-depth-queue-extraction-round1.md`
- `system/indexes/src-fip-070-depth-queue-extraction-round1.md`
- `system/indexes/src-diabetes-035-depth-queue-extraction-round1.md`
- `system/indexes/src-obesity-039-depth-queue-extraction-round1.md`

## Verification

Static checks:

- `python3 -m py_compile scripts/research_mode.py scripts/app.py core/result_presentation.py scripts/check_research_mode_presentation.py scripts/build_research_depth_queue.py`
- `python3 -m py_compile scripts/research_mode.py scripts/check_research_mode_presentation.py`
- `PYTHONPATH=. python3 scripts/test_result_presentation.py`
- `python3 scripts/check_research_mode_presentation.py`
- `python3 scripts/test_research_mode.py --verbose`
- `python3 scripts/test_query.py`
- `python3 -m py_compile scripts/research_mode.py scripts/app.py scripts/check_research_mode_presentation.py scripts/depth_queue_extraction.py`

Results:

- Research Mode sample check passed for CKD, HCM, FIP, diabetes, IBD, obesity.
- Query regression passed: 113/113.
- Depth queue sample extraction generated 5 worksheet files from Crossref/PubMed metadata.

Browser QA:

- test page: `http://localhost:8515/?qa=research-depth-fix-20260619-e`
- readability follow-up page: `http://localhost:8515/?qa=research-readable-cards-20260619`
- tested query: `search the latest papers about feline CKD, prioritize high-impact journals`
- checks passed:
  - Chinese report before English report
  - Chinese structured fields present
  - `为什么值得读`, `关键发现`, and `证据边界` present in paper entries
  - visible links present in first recommended paper blocks
  - depth extraction queue present
  - old placeholder warning absent
  - no internal `src-*` leakage
  - next-action label normalized to `CKD`
  - next-action click queues `猫 CKD 病理生理机制`
  - latest research result anchor stays at viewport top after render

## Remaining Work

The serious evidence-depth issue is not fully solved by presentation changes.

Current state:

- title-only and placeholder records are no longer promoted into recommendations
- they are queued for extraction

Next stage:

1. Pick 3-10 records from `system/indexes/research-depth-queue.md`.
2. Perform abstract/full-text extraction.
3. Add structured fields: methods, sample size, endpoint, findings, limitations, clinical relevance.
4. Re-run presentation checks.
5. Only after approval, solidify the repeated process into a skill/script pipeline.
