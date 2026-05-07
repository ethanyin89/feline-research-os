# Deep Extraction Worksheet

Source: `src-diabetes-014`  
Title: `Feline Diabetes mellitus`  
Method note: this worksheet is based on Crossref abstract-level evidence and source-card metadata, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The paper frames diabetes as common in feline practice

- core_claim: feline diabetes is a common endocrine disorder in clinical practice.
- implicit_premise: the module needs owner-facing clinical utility, not only mechanism depth.
- relation_to_previous: opening clinical scope.
- hard_details: abstract reports an approximate frequency of 1 in 200 cats.
- tension_or_surprise: this is common enough that a usable recognition and management map matters.

#### Unit 2: Most diabetic cats are framed as type-2-like

- core_claim: the majority of diabetic cats have type 2 diabetes mellitus.
- implicit_premise: insulin resistance plus declining insulin production is the default frame, but not the only frame.
- relation_to_previous: connects clinical frequency to disease type.
- hard_details: abstract describes the type-2-like mechanism as peripheral insulin resistance plus progressive reduction in insulin production.
- tension_or_surprise: this pairs cleanly with `src-diabetes-001`, but must be bounded against endocrine-secondary diabetes.

#### Unit 3: Diagnosis may be easy, management is not

- core_claim: diagnosis is usually straightforward, but management has multiple decision points.
- implicit_premise: endpoint and translation pages need decision structure, not only disease definition.
- relation_to_previous: moves from pathophysiology to practice friction.
- hard_details: abstract lists diet, insulin type, dose, monitoring method, monitoring intensity, and concomitant therapy as clinician decisions.
- tension_or_surprise: the hard part is not naming diabetes; it is running the protocol safely with patient and client constraints.

#### Unit 4: Complications and concurrent disease must stay in scope

- core_claim: the clinical frame includes ketoacidosis, diabetic complications, and concurrent diseases.
- implicit_premise: the module should not overfocus on uncomplicated remission candidates.
- relation_to_previous: adds rescue and complexity branches.
- hard_details: abstract flags diabetic ketoacidosis, complications, and multiple concurrent diseases.
- tension_or_surprise: remission is attainable in many newly diagnosed cats, but this does not erase high-risk subgroups.

## Phase 1: Theme Reconstruction

## Theme: Clinical diabetes is a decision-system problem

This paper's strongest reusable contribution is the decision map: diet, insulin, dose, monitoring, and concomitant disease all need to be coordinated.

### Hard Information

- diabetes is common in feline practice
- type-2-like disease predominates
- management includes diet, insulin, monitoring, and concurrent therapy decisions

## Theme: Remission is a goal, not a license to simplify

The abstract emphasizes remission as attainable in many newly diagnosed cats, but the same abstract also flags ketoacidosis, complications, and concurrent disease. The module needs both ideas at once.

### Hard Information

- remission is emphasized as an attainable management goal for many newly diagnosed cats
- diabetic ketoacidosis and complications remain clinically relevant

## Phase 2: Claim-Evidence Structure

### Clinical-Architecture Key Points

**Claim 1**
- support: abstract-level frequency and clinical-relevance framing
- details: diabetes deserves a full disease module rather than a narrow treatment memo
- implicit_premise: common endocrine disease needs recognition, endpoint, and treatment pages

**Claim 2**
- support: abstract-level type-2-like disease framing
- details: default mechanism is insulin resistance plus declining insulin production
- implicit_premise: secondary endocrine disease must be modeled as a branch, not the baseline

**Claim 3**
- support: abstract-level list of management decisions
- details: diet, insulin, dose, monitoring, and concurrent therapy all shape management
- implicit_premise: translation page should be structured by decisions and constraints

## Phase 2.5: Write-Back Implications

### For `topics/diabetes/current-state-dashboard.md`

- state that the module now has a broad clinical anchor
- preserve common-disease and management-complexity framing

### For `topics/diabetes/endpoint-handbook.md`

- include monitoring strategy as an endpoint-family problem

### For `topics/diabetes/translation-brief.md`

- structure treatment around diet, insulin, monitoring, complications, and concurrent disease

## Phase 3: Promotion Check

- source_card_updates:
  - promote to broad clinical overview anchor
  - add abstract-level facts on frequency, type-2-like framing, and management complexity
- topic_write_back_targets:
  - `topics/diabetes/current-state-dashboard.md`
  - `topics/diabetes/endpoint-handbook.md`
  - `topics/diabetes/translation-brief.md`
  - `topics/diabetes/synthesis-index.md`
- not_safe_to_promote_yet:
  - exact insulin or monitoring protocol ranking
  - precise remission rates
  - detailed dosing recommendations
- conflicts_with_existing_vault:
  - none; it reinforces the current mixed mechanism/clinical structure

