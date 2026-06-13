# Researcher Answer Satisfaction Plan: CKD

Date: 2026-06-04
Branch: idea-chatacademia-research-workbench
Trigger: user compared `解释CKD` in free local mode and paid API mode, and neither answer felt satisfying enough.
Status: reviewed plan, not yet implemented

## Problem

The current answer work has improved routing, source loading, and no-API local surfaces. That is necessary, but it is not the same as answer quality.

For the query `解释CKD`, the product currently treats the prompt mostly as a broad explanation. A researcher may want something different:

1. a disease map,
2. the strongest evidence backbone,
3. the endpoint architecture,
4. the evidence-strength boundaries,
5. a way to verify claims,
6. a next research action.

If the answer does not expose those layers, it can be correct and still feel unsatisfying.

## Satisfaction Definition

A researcher is more likely to be satisfied when the answer helps them continue working.

Not just "understand CKD."

The answer should let them decide what to read next, what claims are defensible, what is weak, and where the vault's evidence actually sits.

## Target Answer Contract

For broad research prompts like `解释CKD`, `current understanding of feline CKD`, or `what should a researcher know about feline CKD`, the answer should follow this contract:

```text
1. Direct orientation
   What is CKD in one paragraph, but framed as a research object.

2. Researcher map
   Disease model, recognition/workup, endpoint architecture, treatment/translation, weak layers.

3. Evidence backbone
   Name the 3-5 source-card anchors and explain why each matters.

4. Key-Claim Traceability
   Table of 5-7 claims, evidence level, source IDs, and boundary.

5. What not to overclaim
   Explicitly separate consensus, plausible synthesis, and unresolved gaps.

6. Verification path
   Topic pages and source cards to open next.

7. Next research move
   A concrete action depending on user intent: mechanism, endpoint, treatment, early detection, or regulatory.
```

## Proposed Answer Shape

For `解释CKD`, return a layered answer, not one block of prose:

```markdown
## One-Paragraph Orientation

## Researcher Map
| Layer | Current best reading | Why it matters | Sources |

## Evidence Backbone
| Anchor | Role | What it supports | Boundary |

## Key-Claim Traceability
| ID | Claim | Level | Sources | Boundary |

## Endpoint Architecture
| Endpoint family | Use | Boundary |

## Weak Layers / Do Not Overstate

## Verification Path

## Next Research Moves
```

This is not longer for the sake of being longer. It is more structured because the researcher's job is structure.

## Source Backbone For CKD

Current strongest anchors from the existing vault:

| Anchor | Role | Why it matters |
|---|---|---|
| `src-ckd-004` | ISFM operational guideline | diagnosis, staging, workup, surveillance |
| `src-ckd-010` | histomorphometry correlation | connects markers to structural lesions |
| `src-ckd-011` | fibrosis mechanism frame | supports fibrosis-centered disease model |
| `src-ckd-013` | core outcome set | separates trial breadth from routine endpoint priority |
| `src-ckd-024` | biomarker review | keeps SDMA useful but bounded |

Compiled pages to reuse:

| Page | Role |
|---|---|
| `topics/ckd/synthesis-index.md` | best compiled overview |
| `topics/ckd/endpoint-handbook.md` | endpoint hierarchy and claim table |
| `topics/ckd/what-is-ckd.md` | ordinary-user explanation baseline |
| `topics/ckd/translation-brief.md` | treatment and translation boundaries |
| `topics/ckd/early-detection.md` | frontier early-detection and ML boundaries |

## CEO Review

### 0A. Premise Challenge

Original premise: improve the answer to `解释CKD`.

Better premise: build an answer contract that changes based on audience and job-to-be-done.

The same literal query can mean two different things:

| User | Real job |
|---|---|
| ordinary owner | understand disease and know when to see a vet |
| researcher | understand evidence architecture and what claims are defensible |

If the product cannot distinguish those jobs, free and paid modes will both feel wrong in different ways.

### 0B. Mode

Mode: SELECTIVE EXPANSION.

Hold scope to CKD answer quality, but add the minimum architecture needed so the pattern can later generalize across diseases.

### 0C. 10-Star Version

The 10-star version is not "the API writes a better paragraph."

The 10-star version is: Ask the Vault behaves like a research copilot that turns a broad disease prompt into a working evidence map with traceable claims.

For CKD, the answer would immediately show:

- fibrosis-centered disease model,
- operational endpoints,
- treatment-evidence boundary,
- weak layers,
- source-card anchors,
- next research branches.

### CEO Findings

| Finding | Severity | Decision |
|---|---:|---|
| The current quality target is underspecified. "满意" is not a testable product requirement. | High | Define a researcher answer rubric before changing copy. |
| Broad prompts are overloaded. `解释CKD` can be ordinary-user or researcher intent. | High | Add audience/job interpretation to routing or answer mode. |
| Paid API should not mean "different random prose." | High | Paid mode should obey the same answer contract, with synthesis depth as the difference. |
| The vault's CKD content is strong enough to support a better answer now. | Medium | Reuse compiled pages and source cards, do not do new CKD content extraction. |

## Design Review

UI scope exists because answer shape is product design.

The screenshots show the user comparing two answer experiences. Even if the backend is correct, the visible answer must make the evidence structure legible.

### Design Completeness Score

Current plan before this document: 4/10.

Why: it has routing and citations, but not a clear visible answer grammar for researchers.

Target: 9/10.

### Information Architecture

The answer should not be one prose wall.

Use sections and tables where they map to researcher decisions:

```text
Answer
├── Orientation
├── Researcher Map
├── Evidence Backbone
├── Key-Claim Traceability
├── Endpoint Architecture
├── Weak Layers
├── Verification Path
└── Next Research Moves
```

### Interaction State Coverage

| State | Required behavior |
|---|---|
| Free local mode | deterministic CKD researcher answer, no API |
| Paid API mode | same answer contract, richer synthesis, no loss of traceability |
| Broad ambiguous prompt | show answer as "researcher overview" if user is in researcher mode or if query asks current understanding |
| Ordinary-user mode | keep plain explanation and vet boundary |
| Source missing | say what is absent, do not hallucinate a research conclusion |

### AI Slop Risk

Bad answer smells:

- "CKD is a common disease..." with no research map,
- long prose with citations but no claim boundaries,
- generic "consult a vet" ending for a researcher query,
- source IDs listed but not explained,
- API mode sounding more confident than the source layer supports.

### Design Decision

Add a visible "answer mode" concept:

| Mode | User-facing label | Answer contract |
|---|---|---|
| Plain explanation | What is this disease? | simple explanation |
| Research map | What do researchers know? | evidence architecture |
| Endpoint / treatment evidence | What should we measure or compare? | Key-Claim table |

For the immediate CKD fix, it is acceptable to infer `Research map` for researcher-like prompts, and keep `解释CKD` configurable later.

## Engineering Review

### Scope

Do not rewrite search, source cards, or paid API infrastructure.

Implement the smallest answer-contract layer that can be tested.

### Architecture

```text
User Query
  |
  v
infer disease
  |
  v
classify answer job
  |----------------------|
  | plain explanation    | -> what-is page / existing overview
  | researcher overview  | -> CKD research map builder
  | endpoint             | -> endpoint handbook surface
  | treatment evidence   | -> translation brief surface
  | retrieval fallback   | -> current local search
  |----------------------|
  |
  v
answer contract renderer
  |
  v
source trace gate
  |
  v
eval
```

### Files Likely To Change

| File | Change |
|---|---|
| `scripts/app.py` | add or replace CKD researcher overview builder, route researcher-style CKD prompts to it |
| `scripts/local_answer_surfaces.py` | add CKD researcher overview public helper if public HTTP should match Streamlit |
| `scripts/ordinary_user_vault_eval.py` | add satisfaction rubric cases for CKD researcher answer |
| `scripts/check_local_answer_surfaces.py` | add CKD researcher-map contract check |
| `system/indexes/researcher-answer-satisfaction-rubric.md` | new rubric artifact |

### Proposed New Function

```python
def build_ckd_researcher_overview(chinese: bool) -> tuple[str, list[str]]:
    """Return CKD as a research evidence map, not plain disease explanation."""
```

This function should draw from:

- `topics/ckd/synthesis-index.md`,
- `topics/ckd/endpoint-handbook.md`,
- `topics/ckd/translation-brief.md`,
- `topics/ckd/early-detection.md`.

### Routing Rule

Add researcher markers:

```python
RESEARCHER_MARKERS = [
    "研究者", "研究", "证据", "当前理解", "current understanding",
    "researcher know", "evidence map", "disease model",
]
```

For the exact Chinese prompt `解释CKD`, do not silently assume researcher forever.

Recommended staged behavior:

1. If user selects researcher mode, route `解释CKD` to researcher overview.
2. If no mode exists yet, keep ordinary explanation for `解释CKD`, but add a visible "For researcher map, ask: CKD研究者视角".
3. Add a follow-up chip or example: `CKD研究者视角`.

This is a taste decision. See final approval gate.

### Test Coverage

Add eval cases:

| Query | Expected surface | Must contain |
|---|---|---|
| `CKD研究者视角` | `ckd_researcher_overview` | `Evidence Backbone`, `Key-Claim Traceability`, `src-ckd-004`, `src-ckd-010`, `Weak Layers` |
| `current understanding of feline CKD` | `ckd_researcher_overview` | `fibrosis`, `endpoint`, `renal diet`, `SDMA`, `Do Not Overstate` |
| `解释CKD` in ordinary mode | `ckd_overview` | simple answer, symptoms, diagnosis, management |
| `解释CKD` in researcher mode | `ckd_researcher_overview` | researcher map, evidence backbone, verification path |

### Coverage Diagram

```text
CKD prompt
├── plain owner intent
│   ├── Chinese -> ckd_overview
│   └── English -> ckd_overview
├── researcher intent
│   ├── Chinese -> ckd_researcher_overview
│   └── English -> ckd_researcher_overview
├── endpoint intent
│   └── ckd_endpoint / endpoint handbook
├── treatment evidence intent
│   └── ckd_treatment_evidence / translation brief
└── unknown intent
    └── local retrieval fallback with evidence-gap wording
```

### Failure Modes Registry

| Failure | Impact | Mitigation |
|---|---|---|
| Researcher answer becomes too long and unreadable | user bounces before seeing value | use fixed sections and compact tables |
| Answer cites source IDs not loaded | trust break | source trace gate must require cited IDs loaded |
| Paid mode ignores contract | paid feels worse than free | API synthesis prompt must include answer contract |
| `解释CKD` routed incorrectly for owners | ordinary user gets too technical | add explicit answer mode or follow-up chips |
| Research answer overstates treatment evidence | scientific trust loss | include "what not to overclaim" section |
| Builder duplicates source truth manually | stale claims | prefer compiled topic pages and source IDs |

## Decision Audit Trail

| # | Phase | Decision | Classification | Principle | Rationale | Rejected |
|---|---|---|---|---|---|---|
| 1 | CEO | Define researcher satisfaction rubric before editing answers | Mechanical | Explicit over clever | "满意" must become testable | prompt-only rewrite |
| 2 | CEO | Treat answer quality as job-to-be-done, not mode/free-vs-paid | Mechanical | Pragmatic | free and paid should share contract | compare prose length |
| 3 | Design | Use sectioned research map answer grammar | Mechanical | Completeness | researcher needs navigation and traceability | one prose answer |
| 4 | Eng | Add CKD researcher overview builder and evals | Mechanical | Bias toward action | small blast radius, testable | full query rewrite |
| 5 | Product | Whether exact `解释CKD` should default to researcher map | Taste | User sovereignty | screenshots suggest user expects researcher-grade answer, but owners may not | silent permanent reroute |

## Final Approval Gate

### Recommended Plan

Implement CKD researcher answer quality as a first-class answer contract.

Do this in three cuts:

1. Write `system/indexes/researcher-answer-satisfaction-rubric.md`.
2. Add `ckd_researcher_overview` builder and local/public helper.
3. Add evals for ordinary vs researcher CKD prompts.

### Taste Decision For User

Should `解释CKD` default to researcher-map output?

Recommendation: not globally yet.

Better first version:

- keep `解释CKD` as ordinary explanation unless a researcher mode is selected,
- add `CKD研究者视角` / `current understanding of feline CKD` as researcher examples,
- if your real target user is researchers only, then make researcher-map the default later.

### Completion Summary

| Review | Status | Findings |
|---|---|---|
| CEO Review | PASS_WITH_SCOPE_CHANGE | answer quality must be defined as researcher job completion |
| Design Review | PASS_WITH_REQUIREMENTS | answer needs visible information architecture, not prose mass |
| Eng Review | PASS_WITH_TEST_PLAN | implementation is small if added as builder + evals |

## GSTACK REVIEW REPORT

| Review | Trigger | Why | Runs | Status | Findings |
|--------|---------|-----|------|--------|----------|
| CEO Review | `/plan-ceo-review` via `/autoplan` | Scope & strategy | 1 | PASS_WITH_SCOPE_CHANGE | define satisfaction rubric, split ordinary vs researcher jobs |
| Design Review | `/plan-design-review` via `/autoplan` | Answer UX | 1 | PASS_WITH_REQUIREMENTS | sectioned answer grammar required |
| Eng Review | `/plan-eng-review` via `/autoplan` | Architecture & tests | 1 | PASS_WITH_TEST_PLAN | add builder, route, evals, source trace gate |

