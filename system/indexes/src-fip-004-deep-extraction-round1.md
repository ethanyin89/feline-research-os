# Deep Extraction Worksheet

Source: `src-fip-004`  
Title: `Feline infectious peritonitis: insights into feline coronavirus pathobiogenesis and epidemiology based on genetic analysis of the viral 3c gene`  
Method note: this worksheet is based on abstract-level genetic and epidemiologic details from PubMed and journal metadata, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The paper is a pathobiogenesis-refinement paper, not just another mutation paper

- core_claim: the study refines the mechanism branch by linking 3c gene status to gut replication competence and systemic FIPV behavior.
- implicit_premise: mechanism depth in FIP comes from functional branch logic, not just cataloguing mutations.
- relation_to_previous: opening architectural role.
- hard_details: the study analyzes the 3c gene in 27 FECV- and 28 FIPV-infected cats.
- tension_or_surprise: this is not mainly about diagnosis; it is about how different biological jobs may split across enteric and systemic phases.

#### Unit 2: Intact 3c is tied to enteric competence

- core_claim: functional 3c appears crucial for FECV replication in the gut.
- implicit_premise: gut-tropic enteric coronavirus background and systemic FIPV disease competence should not be treated as the same viral operating mode.
- relation_to_previous: sharpens functional separation.
- hard_details: the abstract states that functional 3c protein expression is crucial for FECV replication in the gut.
- tension_or_surprise: the key mechanistic distinction is not only virulence, but replication setting.

#### Unit 3: Systemic FIPV does not require intact 3c

- core_claim: 3c is dispensable for systemic FIPV replication.
- implicit_premise: systemic disease competence can emerge with a different functional profile than persistent gut competence.
- relation_to_previous: completes the split between enteric and systemic biology.
- hard_details: the abstract states that 3c was mutated in the majority of FIPVs but not in all, and that 3c is dispensable for systemic replication.
- tension_or_surprise: 3c mutation matters, but the paper explicitly blocks single-cause simplification.

#### Unit 4: The paper explains why outbreaks are uncommon

- core_claim: poor gut replication of 3c-inactivated viruses helps explain the rare incidence of FIP outbreaks.
- implicit_premise: epidemiology in FIP is partly constrained by the mismatch between systemic virulence and intestinal transmission competence.
- relation_to_previous: extends mechanism into epidemiology.
- hard_details: the abstract says 3c-inactivated viruses replicate not at all or only poorly in the gut, explaining rare FIP outbreaks.
- tension_or_surprise: the paper ties pathobiogenesis directly to outbreak rarity rather than leaving epidemiology as a separate branch.

#### Unit 5: Superinfection and intestinal-virus findings complicate any flat story

- core_claim: not all cats with FIP had intestinal FCoV, and when intestinal FCoV was found it had intact 3c and seemed to reflect FECV superinfection.
- implicit_premise: systemic FIPV and intestinal FCoV detection cannot be collapsed into one linear sequence.
- relation_to_previous: adds within-host and epidemiologic complexity.
- hard_details: most cats with FIP had no detectable intestinal FCoV; in those with intestinal FCoV, the virus had intact 3c.
- tension_or_surprise: the paper weakens any simple `one mutated virus everywhere` story.

## Phase 1: Theme Reconstruction

## Theme: 3c status helps split enteric background from systemic disease

This paper matters because it gives the mechanism branch a more functional split between FECV gut biology and systemic FIPV biology.

### Hard Information

- 27 FECV-infected cats
- 28 FIPV-infected cats
- intact 3c in all FECVs
- mutated 3c in the majority of FIPVs

## Theme: 3c mutation is important but not singular

The paper supports 3c as a serious mechanism signal while explicitly blocking single-cause overclaim.

### Hard Information

- 3c mutated in 71.4% of FIPVs
- not all FIPVs had 3c mutation
- mutation in 3c is not the single cause of FIP

## Theme: Outbreak rarity can be partly explained by gut incompetence of systemic viruses

This paper is valuable because it pushes the mechanism branch into epidemiology.

### Hard Information

- most cats with FIP had no detectable intestinal FCoV
- 3c-inactivated viruses replicate not at all or only poorly in the gut
- rare incidence of FIP outbreaks is explicitly discussed

## Phase 2: Claim-Evidence Structure

### Mechanism-Refinement Key Points

**Claim 1**
- support: functional 3c is crucial for gut replication in FECV
- details: enteric competence depends on intact 3c
- implicit_premise: background enteric coronavirus ecology needs its own mechanism layer

**Claim 2**
- support: 3c is dispensable for systemic FIPV replication
- details: systemic disease competence differs from gut persistence or transmissibility
- implicit_premise: FIP emergence should be modeled through branch shift rather than flat mutation language

**Claim 3**
- support: poor gut replication of 3c-inactivated viruses helps explain rare outbreaks
- details: the paper links pathobiogenesis to epidemiology
- implicit_premise: mechanism and outbreak pattern belong in the same explanatory branch

### Boundary-Setting Key Points

**Claim 1**
- support: not all FIPVs carried 3c mutation
- details: 3c is important but not sufficient as a total explanation
- implicit_premise: the vault should resist `one genetic answer` framing

**Claim 2**
- support: intestinal virus in FIP cats, when present, appeared intact-3c and likely due to FECV superinfection
- details: intestinal detection does not simply mirror systemic FIPV
- implicit_premise: sampling context and viral compartment matter

## Phase 2.5: Write-Back Implications

### For `topics/fip/mechanism-overview.md`

- sharpen the 3c branch from vague genetic refinement into `gut competence versus systemic competence`
- add outbreak-rarity logic as a mechanism consequence

### For `entities/mechanisms/mutation-origin.md`

- state more clearly that specific mechanism refinements like 3c do not collapse back into single-cause language

### For `topics/fip/synthesis-index.md`

- add a stabilizing rule that `gut competence and systemic competence are not the same thing`

## Phase 3: Promotion Check

- source_card_updates:
  - preserve functional split between gut and systemic replication
  - preserve 3c-importance-without-singularity language
  - preserve outbreak-rarity interpretation
- topic_write_back_targets:
  - `topics/fip/mechanism-overview.md`
  - `entities/mechanisms/mutation-origin.md`
  - `topics/fip/synthesis-index.md`
  - `topics/fip/current-state-dashboard.md`
  - `system/indexes/fip-source-index.md`
- not_safe_to_promote_yet:
  - any claim that 3c mutation alone explains FIP
  - any claim that this paper turns 3c into a definitive diagnostic marker
  - any collapse of intestinal and systemic viral findings into one simple trajectory
- conflicts_with_existing_vault:
  - none; this deepens the mechanism spine between classical mutation-origin and later spread-boundary papers
