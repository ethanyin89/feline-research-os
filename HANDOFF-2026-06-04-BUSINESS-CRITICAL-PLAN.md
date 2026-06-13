# Handoff: Business-Critical Feline Research OS Plan

Date: 2026-06-04
Branch: `idea-chatacademia-research-workbench`
Status: planning handoff after CKD answer-quality dissatisfaction and repo-level business-value reframing

## Trigger

The user compared the same question, `解释CKD`, across free/local and paid/API modes. The content was still not satisfying.

The important clarification was broader than CKD:

> The project should truly help push the business forward, not become a nice-to-have.

So the current next task is not just "make the CKD answer prettier." It is to align `feline-research-os` around business-critical decision artifacts.

## What Changed This Session

### 1. Local answer surfaces were implemented

The public test app now has deterministic, no-API answer surfaces for common evidence queries.

Relevant files:

- `scripts/local_answer_surfaces.py`
- `scripts/public_test_app.py`
- `scripts/check_local_answer_surfaces.py`
- `scripts/check_public_test_page.sh`

Coverage verified for:

- FIP recognition
- FIP endpoint
- FIP treatment evidence
- FIP what-is
- CKD endpoint
- CKD treatment evidence
- HCM endpoint
- IBD endpoint
- diabetes endpoint
- FCV treatment evidence

This matters because the app can now answer common ordinary-user and researcher-adjacent questions without spending API money.

### 2. Query architecture handoff was updated

Read this if continuing the implementation line:

- [HANDOFF-2026-06-04-QUERY-ARCHITECTURE.md](HANDOFF-2026-06-04-QUERY-ARCHITECTURE.md)

That handoff contains the concrete implementation details behind the local surfaces and public-test verification.

### 3. CKD answer satisfaction plan was written

Read:

- [PLAN-researcher-answer-satisfaction-ckd.md](PLAN-researcher-answer-satisfaction-ckd.md)

Core conclusion:

Answer quality is not just better retrieval, more citations, or a paid model. For a researcher, satisfaction requires an answer contract:

- orientation,
- researcher map,
- evidence backbone,
- Key-Claim Traceability,
- explicit overclaim boundaries,
- verification path,
- next research move.

For `解释CKD`, the unresolved product decision is whether the default should be:

- ordinary owner explanation, or
- researcher evidence map.

Do not silently choose one forever. Make this an explicit product-mode decision.

### 4. Business-critical product plan was written

Read:

- [PLAN-business-critical-feline-research-os.md](PLAN-business-critical-feline-research-os.md)

Core conclusion:

`feline-research-os` should become a claim-traceable feline evidence decision workbench, not a generic AI vet, generic academic search engine, prettier vault, or chat UI.

The business-critical path is:

```text
question -> evidence map -> decision artifact -> business action
```

The first strong wedge should be `Claim Evidence Workbench`.

## Key Decisions

1. `Ask the Vault` is useful, but it is not the main monetization wedge.
2. Ordinary-user answers are trust and distribution infrastructure.
3. Business value comes from `Decide` and `Verify` workflows.
4. The repo already has enough truth infrastructure to generate real decision artifacts.
5. The next product layer should expose claim support, evidence gaps, and next actions.
6. A paid API answer should obey the same answer contract as local mode; it should not be random better-sounding prose.

## Recommended Next Task

Build the first `Claim Evidence Workbench` slice.

Minimum useful behavior:

```text
Input:
  A claim, for example:
  "Feline CKD progression can be monitored primarily with SDMA."

Output:
  verdict: supported / partially supported / unsupported / absent
  evidence backbone: source IDs + compiled pages
  boundary: what the claim can and cannot say
  missing evidence: what would make the claim stronger
  next action: promote, revise, kill, or search/extract more sources
```

Suggested implementation files:

- `scripts/claim_evidence.py`
- `scripts/business_value_eval.py`
- integrate a minimal UI path in `scripts/app.py` or the current public-test app after the backend is stable

Suggested first diseases:

- CKD
- FIP
- diabetes
- cancer only if the current dirty cancer extraction work is coherent enough

## Immediate P0 Checklist

1. Create `system/indexes/business-critical-product-rubric.md`.
2. Define the required artifact contract for:
   - claim evidence card,
   - opportunity brief,
   - endpoint decision memo,
   - gap-to-intake queue item.
3. Implement `scripts/claim_evidence.py` for one disease first, preferably CKD.
4. Add deterministic tests in `scripts/business_value_eval.py`.
5. Only then expose it in UI.

## P1 Follow-Up

If continuing the CKD answer-quality line, implement `ckd_researcher_overview`.

That should use the contract in [PLAN-researcher-answer-satisfaction-ckd.md](PLAN-researcher-answer-satisfaction-ckd.md), not just rewrite prose.

## Verification Already Run

```bash
python3 -m py_compile scripts/local_answer_surfaces.py scripts/check_local_answer_surfaces.py scripts/public_test_app.py
python3 scripts/check_local_answer_surfaces.py
python3 scripts/public_test_app.py --host 127.0.0.1 --port 8510
bash scripts/check_public_test_page.sh http://127.0.0.1:8510
```

The local surface checks passed. The temporary local server used for verification was stopped.

## Worktree Warning

The worktree is dirty and contains many unrelated existing modifications and untracked files, especially cancer source-card work and system index files.

Do not revert unrelated changes.

Files most relevant to this session are untracked or newly modified:

- `HANDOFF-2026-06-04-QUERY-ARCHITECTURE.md`
- `PLAN-researcher-answer-satisfaction-ckd.md`
- `PLAN-business-critical-feline-research-os.md`
- `scripts/local_answer_surfaces.py`
- `scripts/check_local_answer_surfaces.py`
- `scripts/public_test_app.py`
- `scripts/check_public_test_page.sh`
- `topics/ckd/what-is-ckd.md`
- `topics/fip/fip-warning-signs.md`
- `topics/fip/what-is-fip.md`
- `topics/obesity/what-is-obesity.md`

## Do Not Do Next

- Do not build a generic pet chatbot.
- Do not build an agent menu.
- Do not spend the next session only polishing `解释CKD` unless the user explicitly chooses that branch.
- Do not treat more citations as equivalent to a more useful answer.
- Do not make paid mode the quality strategy; make the artifact contract the strategy.

## One Line

Make `feline-research-os` produce decision artifacts that change what the business does next.
