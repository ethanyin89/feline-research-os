---
id: system-fip-support-order-memo
type: system
topic: fip
last_compiled_at: 2026-04-21
owner: codex
status: active
language: en
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
---

# FIP Support-Order Memo

- Date: `2026-04-10`
- Scope: `src-fip-002`, `src-fip-003`, `src-fip-006`, `src-fip-007`, `src-fip-010`, `src-fip-011`, `src-fip-015`, `src-fip-022`, `src-fip-023`

This memo exists to stop the FIP endpoint and workup branch from drifting into `all support channels are useful, combine them somehow`.

That sentence is directionally fine.

It is not operational enough for this vault.

## Core Position

1. FIP support channels are not interchangeable.
2. The correct question is not only `which tests matter`.
3. The tighter question is `which support channel should lead, which should follow, and which only appears after a branch shift`.
4. The current vault supports a five-step order:
   - clinicopathologic and disease-form suspicion
   - bounded laboratory background support
   - mutation-related strengthening
   - neurologic / CSF branch extension when the case changes category
   - treatment-follow-up outcomes kept separate from first-pass diagnosis
5. The main error to block is `support flattening`, where serology, acute-phase markers, mutation assays, and CSF logic all get treated like parallel first-line evidence.

## Current Ordered Architecture

### Step 1: Clinicopathology And Disease Form Lead

This is the operational front door.

It is carried most strongly by:

- `src-fip-003`
- `src-fip-006`
- `src-fip-015`

What it does:

- turns vague concern into real FIP suspicion
- makes wet, dry, and neurologic form matter early
- justifies why stronger downstream support is worth pursuing

### Step 2: Acute-Phase, Immunoglobulin, And Older Serology Stay In Background Support

This layer is real, but it should not start the story.

It is carried mainly by:

- `src-fip-002`
- `src-fip-007`
- `src-fip-011`

What it does:

- enriches inflammatory and exposure-linked context
- keeps historical laboratory support visible without promoting it into modern workup leadership
- prevents endpoint logic from collapsing into only clinicopathology plus mutation testing

### Step 3: Mutation-Related Assays Strengthen But Do Not Close

This layer belongs after suspicion is already real.

It is carried mainly by:

- `src-fip-010`
- `src-fip-022`

What it does:

- narrows uncertainty after clinicopathologic suspicion
- adds bounded molecular support
- forces utility and limitation to be held together

### Step 4: CSF Logic Belongs To A Branch Shift

This layer only becomes relevant once the case has entered neurologic-branch logic.

It is carried mainly by:

- `src-fip-023`

What it does:

- changes the workup shape
- adds CNS-aware support
- creates subgroup-sensitive strengthening without broad exclusion power
- carries the current strongest extracted assay-style numbers: specificity `100%`, PPV `100%`, overall sensitivity `42.1%`, NPV `57.7%`, and neurologic/ocular sensitivity `85.7%`

### Step 5: Treatment-Follow-Up Outcomes Stay Separate

This step belongs after treatment begins.

It should not backflow into first-pass diagnostic leadership.

What it does:

- tracks response
- tracks remission
- tracks relapse
- tracks survival or downstream trajectory

## Current Working Hierarchy

| Support Channel | Current Position In Vault | Main Job |
|---|---|---|
| Clinicopathology / disease-form pattern | lead operational branch | starts and shapes suspicion |
| Acute-phase / immunoglobulin support | lower background-support branch | enriches inflammatory reading after suspicion is already real |
| Older serology | historical support context | keeps exposure-linked laboratory history visible without leading modern workup |
| Mutation-related assays | bounded strengthening branch | tightens support after suspicion, but does not settle certainty |
| CSF viral detection | neurologic-extension branch | applies after branch shift; strong positive support, weak broad rule-out value |
| Treatment response / remission / relapse | follow-up outcome branch | monitors treated disease, not first-pass diagnosis |

## What This Memo Clarifies That The Existing Pages Did Not

1. It is not enough to say `FIP diagnosis is composite`.
2. Composite support still needs a leader.
3. In the current vault, clinicopathology leads.
4. Acute-phase and serologic support fill the background layer rather than the lead layer.
5. Mutation support comes after suspicion, not before it.
6. CSF support belongs to a neurologic branch shift rather than to ordinary FIP workup.
7. Follow-up outcomes belong to treatment monitoring rather than diagnostic leadership.

## What This Branch Is Not Allowed To Become

- It is not allowed to become `everything helps equally`.
- It is not allowed to become `mutation testing first`.
- It is not allowed to let CSF specificity be misread as generic diagnostic leadership.
- It is not allowed to let response-to-treatment rewrite first-pass workup order.
- It is not allowed to erase lower laboratory context just because it is not first-line.

## What The Vault Can Now Say More Clearly

1. FIP support logic is layered and ordered, not merely multi-source.
2. The correct leading sequence is:
   `clinicopathology first -> bounded laboratory context -> mutation strengthening -> neurologic branch extension when needed`
3. Acute-phase and serology support matter most when they are prevented from pretending to be first triggers.
4. CSF support is strongest after the workup has already changed category.
5. Follow-up outcomes belong to treatment monitoring rather than diagnostic leadership.
6. Numeric assay detail currently supports sharpening the CSF branch more than the mutation or serology branches; keep those other branches as placement boundaries until deeper performance extraction exists.

## Best Reuse Targets

- [endpoint handbook](../../topics/fip/endpoint-handbook.md)
- [risk and recognition](../../topics/fip/risk-and-recognition.md)
- [FIP diagnostic-workup memo](fip-diagnostic-workup-memo.md)
- [FIP endpoint-diagnostic bridge memo](fip-endpoint-diagnostic-bridge-memo.md)
- [FIP acute-phase and immunoglobulin support memo](fip-acute-phase-support-memo.md)
- [FIP mutation-diagnostics boundary memo](fip-mutation-diagnostics-boundary-memo.md)
- [FIP neurologic recognition memo](fip-neurologic-recognition-memo.md)
- [current state dashboard](../../topics/fip/current-state-dashboard.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for support-order architecture; no, for one-test certainty or broad exclusion language`
- smallest durable home: `memo + topic update + control example`

### Reason

- what is repeating:
  FIP endpoint and workup questions keep recurring as `which test matters most` or `can these tests just be combined`
- what becomes clearer:
  the vault now has a stable order across clinicopathology, background laboratory support, mutation strengthening, neurologic branch shift, and downstream follow-up
- what is still too thin, if anything:
  assay-specific performance ranking and official-source route guidance remain too thin for stronger operational recommendation

### Decision

- promote
