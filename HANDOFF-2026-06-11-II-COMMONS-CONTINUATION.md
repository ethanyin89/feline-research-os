# Handoff: II-Commons Research OS Continuation

**Date:** 2026-06-11  
**Status:** Search-depth execution contract completed and verified

## Scope

This continuation resumed the June 6 II-Commons / Research OS lane after reading
the authoritative dirty-worktree handoff. It deliberately changed only the
Research Record and Harness slice plus its documentation.

## Gap Closed

Before this continuation, `TaskEvaluator` assigned `quick`, `standard`, `deep`,
or `evidence_audit`, but no component checked whether the query pipeline actually
performed the promised retrieval work.

That meant a task could be labelled `deep` while using one retrieval pass, one
source family, and no counterevidence check.

## Implementation

Added `core/search_depth_controller.py`.

The controller checks:

- selected evidence count;
- observable retrieval rounds from Research trace;
- source-family plurality;
- gap reflection for Deep and Evidence Audit;
- counterevidence for Evidence Audit.

Integrated it into:

- `core/__init__.py`;
- `scripts/harness_loop.py`;
- `scripts/app.py`;
- `core/test_harness_loop.py`.

Explicit review terms such as `审查`, `验证`, `evidence audit`, and `verify` now
take precedence in `TaskEvaluator`, so an audit request is not misclassified as
ordinary endpoint or protocol work.

## Runtime Behavior

The controller does not make network calls and does not block the user-facing
answer.

When the assigned search-depth contract is not satisfied:

- the Research Record receives a `search_depth_contract` verification result;
- the record becomes `needs_human_review` or `failed` for a critical audit gap;
- exact missing requirements are returned in Harness metadata.

Loaded source IDs are used as actual selected evidence when available, rather
than relying only on citations emitted in the final prose.

## Verification

All checks were local and used no paid API:

```text
python3 core/test_harness_loop.py  PASS
python3 scripts/benchmark_runner.py  20/20
python3 scripts/test_query.py  111/111
python3 -m py_compile ...  PASS
git diff --check  PASS
```

A temporary-directory integration check also confirmed that a qualifying Deep
trace satisfies the contract and persists a Research Record.

## Remaining Boundary

The June 6 architecture MVP is now implemented. Remaining work is:

- validate repeated use with real research cases;
- improve trace classification if external PubMed/Crossref retrieval becomes
  part of the normal query path;
- convert source cards into Evidence Cards only for a measured retrieval need;
- keep YAML agent profiles deferred until role configuration solves a concrete
  problem.

Do not treat more agent infrastructure as the default next step. The
business-critical plan requires proving the durable human-reviewed workflow
before expanding orchestration.

## Worktree Safety

The repository remains heavily dirty. This continuation did not clean, reset,
stage, or revert unrelated changes. Review and commit this feature separately
from source-card, extraction, and Research Case work.
