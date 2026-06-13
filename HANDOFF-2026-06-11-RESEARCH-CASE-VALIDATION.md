# Handoff: Research Case Integrity Validation

**Date:** 2026-06-11  
**Status:** Persisted-case integrity gate implemented and verified

## Scope

This continuation followed the II-Commons handoff's next gate: validate the
durable Research Case workflow without adding more agent infrastructure or
inventing human review.

## Work Completed

Added `scripts/validate_research_cases.py`, a read-only corpus validator that
checks:

- case ID and filename agreement;
- current schema version;
- domain validation of the current projection;
- monotonic revision and event histories;
- unique operation IDs;
- revision snapshot SHA-256 hashes;
- current projection agreement with the latest revision;
- referenced legacy/evidence file containment, existence, and SHA-256;
- derived Frame, Criteria, Evidence, and Challenge states.

Integrated the validator into `scripts/health.py` as a hard health gate and
added persisted-corpus coverage to `scripts/test_research_cases.py`.

## Real Case Result

`case-ckd-phosphorus-control` passes integrity validation:

```text
frame=complete/current
criteria=blocked/current
evidence=not_started/current
challenge=not_started/current
```

This is the correct authority boundary. The case requires a named human reviewer
to define and freeze Criteria. No reviewer criteria or attestations were
fabricated.

## Verification

```text
python3 scripts/validate_research_cases.py  PASS (1/1 valid)
python3 scripts/test_research_cases.py      PASS (12 tests)
.venv/bin/python scripts/test_research_case_ui.py  PASS
python3 core/test_harness_loop.py           PASS
python3 scripts/benchmark_runner.py         PASS (20/20)
python3 scripts/test_query.py               PASS (111/111)
python3 -m py_compile ...                    PASS
git diff --check -- ...                     PASS
```

`python3 scripts/health.py --skip-slow` correctly remains nonzero because of
pre-existing source-card, compiled-reference, and ordinary-user answer-quality
failures. Its new `Research Case integrity` row passes with `1/1 valid`.

## Next Gate

The workflow cannot honestly advance the CKD case until a named human reviewer
defines and freezes decision criteria. Engineering can continue independently
by fixing the known aggregate health failures, but it should not bypass this
case gate.
