# Handoff: Current Worktree State

**Captured:** 2026-06-11 12:58 +0800  
**Branch:** `idea-chatacademia-research-workbench`  
**HEAD:** `803dcb7` (`feat(ckd): expand synthesis to 33 sources with biomarker and microbiome evidence`)  
**Purpose:** Authoritative restart point for the current dirty worktree

## Read This First

This file supersedes the completion claims in the other 2026-06-11 handoffs.
Those files remain useful as chronological session notes, but they do not describe
the current worktree accurately.

The repository is not in a clean, fully committed state:

- `180` tracked files have changes.
- `474` untracked top-level status entries exist.
- The tracked diff is approximately `5,307` insertions and `2,004` deletions
  across `180` files.
- Do not run cleanup, reset, checkout, or bulk deletion commands.
- Treat all existing changes as user/session work that must be preserved.

## Current Reality

### Committed baseline

Sixteen commits were made on 2026-06-11. The latest committed sequence deepened:

- FIP extraction and treatment surfaces
- diabetes mechanism and recognition surfaces
- FCV and obesity mechanism surfaces
- cancer synthesis
- CKD mechanism and synthesis

The current committed tip is `803dcb7`.

### Uncommitted work

The uncommitted work is much broader than the latest commits:

- `raw/`: 152 tracked changes and 175 untracked files
- `system/`: 10 tracked changes and 238 untracked files
- `scripts/`: 10 tracked changes and 19 untracked files
- `topics/`: 3 tracked changes and 9 untracked files
- `core/`: 8 untracked files
- new research-case, artifact-review, benchmark, intake, and business-output
  infrastructure
- many source-card normalizations and structured/deep extraction artifacts

Important uncommitted implementation areas include:

- `core/` research-case and verification primitives
- `scripts/research_cases.py`, `scripts/research_case_ui.py`, and related tests
- `scripts/artifact_review.py`, `scripts/benchmark_runner.py`, and
  `scripts/business_value_eval.py`
- `scripts/app.py`, `scripts/claim_evidence.py`, and
  `scripts/local_answer_surfaces.py`
- `system/research-cases/case-ckd-phosphorus-control.json`
- `outputs/business/` and `outputs/final/`

Do not assume these files form one reviewable commit. The next operator should
inventory and split them by feature before staging.

## Verified Checks

### Passing

```text
python3 scripts/test_query.py
111 passed | 0 failed
```

This is a local, no-paid-API test run.

The health report at
`system/health-checks/health-report-20260611.md` confirms:

- 603 strict disease paper cards
- 14 regulation cards
- no duplicate or missing source IDs
- no low-word paper cards
- compiled source references resolve
- reader page `source_ids` resolve
- candidate image gate passes

### Blocked or failing

Focused research-case pytest collection is not currently reproducible:

- system Python has `pytest` but not `streamlit`
- `.venv` has no `pytest`

No dependencies were installed during this handoff.

The 2026-06-11 health report is `needs_attention`, not clean. Known failures:

1. Two template links in `.claude/skills/` are reported as missing.
2. Ordinary-user vault evaluation has answer-quality failures.
3. `raw/papers/src-fip-049.md` is missing required schema fields.
4. `src-diabetes-118` and `src-obesity-085` use invalid
   `verification_status: quoted_fact_weighted`.
5. `src-fip-045` and `src-fip-049` lack DOI/URL proof.
6. `src-fip-049` has an empty machine-readable `evidence_policy`.
7. Diabetes-118 and obesity-085 violate the decision-grade gate.
8. Seven reader/high-visibility pages use thin sources, mainly cancer pages.

Use the health report as the exact issue list; do not rely on older handoff
statements such as "all checks pass" or "all work committed."

## Source Inventory Snapshot

From `system/health-checks/health-report-20260611.md`:

| Disease | Cards | Main verification-status distribution |
|---|---:|---|
| CKD | 85 | 28 deep, 54 abstract, 2 source-checked, 1 title-only |
| FIP | 49 | 26 deep, 22 abstract, 1 missing |
| HCM | 24 | 24 deep |
| IBD | 24 | 24 deep |
| Diabetes | 121 | 25 deep, 87 abstract, 8 title-only, 1 invalid status |
| FCV | 103 | 24 deep, 79 abstract |
| Obesity | 95 | 4 deep, 82 abstract, 1 source-checked, 7 title-only, 1 invalid status |
| Cancer | 102 | 29 deep, 69 abstract, 2 source-checked, 1 title-only, 1 publisher-verified |

These values use the current `verification_status` schema. They intentionally
do not repeat older handoff terminology such as `extracted` or `ingested`.

## Safe Next Actions

1. Preserve the worktree and inspect changes by feature boundary.
2. Fix the seven health-report issue groups before claiming production-ready.
3. Decide which Python environment owns test dependencies, then run the focused
   research-case tests without using a paid API.
4. Review the research-case implementation as a separate feature:
   `core/`, `scripts/research_case*`, schema, case JSON, and tests.
5. Review source-card/extraction changes separately from application changes.
6. Run `python3 scripts/health.py` after fixes and record the new report.
7. Stage and commit only after the work is divided into coherent units.

## Restart Commands

```bash
cd /Users/jiawei/Desktop/insclaude/feline-research-os
git status --short
git log -8 --oneline --decorate
python3 scripts/test_query.py
sed -n '1,240p' system/health-checks/health-report-20260611.md
```

Avoid a live OpenRouter or Anthropic run unless the task explicitly requires it
and the repository's budget/approval rules are satisfied.

