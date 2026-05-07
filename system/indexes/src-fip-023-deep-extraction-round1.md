# Deep Extraction Worksheet

Source: `src-fip-023`  
Title: `Detection of feline coronavirus in cerebrospinal fluid for diagnosis of feline infectious peritonitis in cats with and without neurological signs`  
Method note: this worksheet is based on abstract-level diagnostic details already available from the journal and PubMed records, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: This is a neurologic-extension paper, not a general FIP workup paper

- core_claim: the paper evaluates CSF RT-PCR as a diagnostic tool for FIP in cats with and without neurologic and/or ocular signs.
- implicit_premise: CNS-directed testing belongs to a specialized workup layer rather than the ordinary suspicion layer.
- relation_to_previous: opening architectural placement.
- hard_details: the abstract explicitly frames CSF testing and includes cats with and without neurologic or ocular signs.
- tension_or_surprise: the paper is easy to overgeneralize because its specificity is strong.

#### Unit 2: Overall performance is not broad enough for generic workup leadership

- core_claim: the overall sensitivity is too limited for CSF RT-PCR to behave like a universal FIP rule-out or lead diagnostic test.
- implicit_premise: high-specificity specialized tests still require bounded placement when overall sensitivity is modest.
- relation_to_previous: moves from placement to performance boundary.
- hard_details: the abstract reports specificity of 100%, sensitivity of 42.1%, PPV of 100%, and NPV of 57.7%.
- tension_or_surprise: the strongest number is specificity, not broad-case sensitivity.

#### Unit 3: The branch becomes much stronger in neurologic or ocular disease

- core_claim: CSF RT-PCR becomes much more useful when the disease branch already includes neurologic and/or ocular involvement.
- implicit_premise: the test is best modeled as branch-sensitive rather than universally diagnostic.
- relation_to_previous: sharpens the subgroup logic.
- hard_details: the abstract reports sensitivity of 85.7% in cats with neurologic and/or ocular signs.
- tension_or_surprise: the same assay looks materially different once the workup shifts into the CNS branch.

#### Unit 4: This paper supports branch shift, not single-test certainty

- core_claim: the right lesson is that neurologic FIP needs its own extension logic, not that CSF PCR solves FIP diagnosis in general.
- implicit_premise: subgroup-sensitive utility should reorganize architecture, not flatten it.
- relation_to_previous: moves from diagnostic metrics to vault use.
- hard_details: the study is a prospective case-control design with 34 cats, including definitive histopathological FIP cases and non-FIP controls with similar signs.
- tension_or_surprise: the more impressive neurologic-branch sensitivity looks, the more important it becomes to keep the ordinary-workup boundary.

## Phase 1: Theme Reconstruction

## Theme: CSF viral detection is a specialized extension, not a first-line FIP endpoint

This paper gives the neurologic branch a serious diagnostic support tool, but only after the workup has already shifted into CNS-aware suspicion.

### Hard Information

- real-time RT-PCR on CSF
- specificity 100%
- overall sensitivity 42.1%

## Theme: Subgroup logic is the whole point of the paper

The paper matters because it shows that diagnostic value changes substantially once neurologic and/or ocular involvement enters the picture.

### Hard Information

- sensitivity 85.7% in cats with neurologic and/or ocular signs

## Theme: Positive support and universal readiness are different claims

This is a strong support paper for the neurologic branch, but it does not justify rewriting all of FIP workup around CSF testing.

### Hard Information

- PPV 100%
- NPV 57.7%
- case-control design with histopathologically confirmed FIP cases and clinically similar controls

## Phase 2: Claim-Evidence Structure

### Neurologic-Diagnostic Extension Key Points

**Claim 1**
- support: the paper directly studies CSF RT-PCR for FIP diagnosis
- details: this is a CNS-oriented diagnostic-support paper
- implicit_premise: neurologic workup needs a distinct extension layer

**Claim 2**
- support: specificity is 100% and PPV is 100% in the abstract
- details: a positive result can strongly strengthen the diagnosis in the right branch
- implicit_premise: this tool has real bounded utility

**Claim 3**
- support: sensitivity rises to 85.7% in cats with neurologic and/or ocular signs
- details: subgroup context changes the value of the assay
- implicit_premise: the branch should be modeled by context, not by one global test number

### Boundary-Setting Key Points

**Claim 1**
- support: overall sensitivity is 42.1% and NPV is 57.7%
- details: the assay is not broad enough for ordinary-workup leadership
- implicit_premise: negative CSF RT-PCR does not rule out FIP in general

**Claim 2**
- support: the study includes both neurologic/ocular and non-neurologic presentations
- details: the paper itself supports branch-sensitive interpretation
- implicit_premise: the vault should not generalize neurologic utility into generic FIP certainty

## Phase 2.5: Write-Back Implications

### For `topics/fip/endpoint-handbook.md`

- sharpen the `CSF viral detection` row with explicit high-specificity but branch-specific language
- reinforce that subgroup context matters more than one global label like `PCR`

### For `system/indexes/fip-diagnostic-workup-memo.md`

- add that CSF detection can be highly strengthening in neurologic/ocular workup but should not lead ordinary FIP workup

### For `system/indexes/fip-endpoint-diagnostic-bridge-memo.md`

- state more clearly that CNS-specific testing becomes valuable after suspicion has already shifted into the neurologic branch

## Phase 3: Promotion Check

- source_card_updates:
  - preserve subgroup-sensitive utility
  - preserve high-specificity but limited-overall-sensitivity language
  - preserve ordinary-workup boundary
- topic_write_back_targets:
  - `topics/fip/endpoint-handbook.md`
  - `system/indexes/fip-diagnostic-workup-memo.md`
  - `system/indexes/fip-endpoint-diagnostic-bridge-memo.md`
  - `topics/fip/current-state-dashboard.md`
  - `system/indexes/fip-source-index.md`
- not_safe_to_promote_yet:
  - any statement that CSF RT-PCR is a general FIP diagnostic shortcut
  - any statement that a negative CSF result broadly excludes FIP
  - any flattening of neurologic-branch utility into ordinary-workup certainty
- conflicts_with_existing_vault:
  - none; this sharpens the neurologic-extension branch already present in the module
