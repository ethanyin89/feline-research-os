# Deep Extraction Worksheet

Source: `src-fcv-014`  
Title: `Potential Therapeutic Agents for Feline Calicivirus Infection`  
Method note: this worksheet is based on the open-access MDPI article abstract and accessible result/discussion text, not a full section-by-section extraction of the complete article PDF.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: This paper is a discovery-infrastructure paper, not a treatment-answer paper

- core_claim: the study tests 15 compounds against FCV using both protein-based and cell-culture assays.
- implicit_premise: the FCV therapy branch needs a screening and assay layer before any in vivo or clinical language becomes coherent.
- relation_to_previous: opening branch placement.
- hard_details: the abstract explicitly reports `15` compounds and both protein and cell-culture assays.
- tension_or_surprise: the paper matters more for structure than for any one candidate.

#### Unit 2: Enzyme inhibition and cell-culture inhibition are different endpoint families

- core_claim: hits against the FCV polymerase or protease do not automatically translate into antiviral effect in infected cells.
- implicit_premise: assay-stage therapy reading should preserve endpoint separation rather than celebrate every low IC50.
- relation_to_previous: sharpens the method value.
- hard_details: quercetagetin and PPNDS inhibited polymerase, and GC376 inhibited protease, but the abstract states those compounds did not show antiviral effects in cell culture.
- tension_or_surprise: the most impressive enzyme numbers are not the final winners of the paper.

#### Unit 3: The strongest cell-culture leads are nitazoxanide and 2CMC

- core_claim: the practical center of gravity of the paper is the identification of two compounds with low-micromolar cell-culture activity.
- implicit_premise: assay-stage FCV translation should weight replication inhibition in infected cells above isolated enzyme hits.
- relation_to_previous: explains which signals actually rise above the screening floor.
- hard_details: nitazoxanide had an `EC50` of `0.6 uM` and `2'-C-methylcytidine` had an `EC50` of `2.5 uM`.
- tension_or_surprise: the broad-screening paper still ends up with a narrow shortlist.

#### Unit 4: Nitazoxanide and 2CMC are still bounded by preclinical limits

- core_claim: promising cell-culture activity does not make either compound a practice-grade FCV treatment recommendation.
- implicit_premise: discovery-stage potency and veterinary utility are different claim families.
- relation_to_previous: sets the translation ceiling.
- hard_details: the paper stays in vitro, while later discussion notes therapeutic-index and tolerability questions remain live.
- tension_or_surprise: the paper sounds like a shortlist, but the correct use is still screening-stage hierarchy only.

#### Unit 5: This source should own the assay-stage subsection of the FCV therapy branch

- core_claim: `src-fcv-014` should become the default source for the sentence `FCV therapy has a structured assay-stage discovery layer`.
- implicit_premise: the therapy branch becomes misleading if it jumps from supportive care directly to CpG49-style in vivo optimism.
- relation_to_previous: assigns durable module role.
- hard_details: this paper pairs naturally with `src-fcv-008` above it as treatment-heterogeneity caution and `src-fcv-018` above both as the first in vivo branch anchor.
- tension_or_surprise: its safest role is not `candidate winner`, but `assay-stage architecture owner`.

## Phase 1: Theme Reconstruction

## Theme: FCV therapy now has a defined discovery-infrastructure layer

This paper upgrades FCV therapy from vague speculation into a real assay-stage branch. It supports saying that the module has a systematic drug-discovery layer beneath later translation.

### Hard Information

- `15` compounds tested
- protein-based assays and cell-culture assays both used
- direct screening against protease, polymerase, and replication phenotypes

## Theme: The branch needs endpoint separation inside preclinical work

The paper is strongest when it teaches the module to separate enzyme inhibition from infected-cell antiviral effect.

### Hard Information

- quercetagetin and PPNDS inhibited polymerase
- GC376 inhibited protease
- those enzyme hits did not translate into cell-culture antiviral effect in the abstract

## Theme: Only a narrow subset of screened compounds rise to real cell-culture lead status

The source narrows the discovery field. Nitazoxanide and 2CMC become the main cell-culture leads rather than one large undifferentiated list of compounds.

### Hard Information

- nitazoxanide `EC50` `0.6 uM`
- `2'-C-methylcytidine` `EC50` `2.5 uM`

## Phase 2: Claim-Evidence Structure

### Therapy-Discovery Key Points

**Claim 1**
- support: the paper reports `15` compounds across antiviral classes tested using protein and cell-culture assays
- details: screening architecture rather than one-off compound claim
- implicit_premise: FCV therapy discovery is now an explicit branch in the module

**Claim 2**
- support: quercetagetin and PPNDS inhibited polymerase, and GC376 inhibited protease, but these did not show cell-culture antiviral effect in the preserved abstract
- details: enzyme-hit versus replication-hit separation
- implicit_premise: low IC50 values do not settle translational relevance

**Claim 3**
- support: nitazoxanide and 2CMC showed low-micromolar inhibition in cell culture
- details: `0.6 uM` and `2.5 uM` `EC50` values
- implicit_premise: a small subset of compounds deserve higher downstream attention

### Boundary-Setting Key Points

**Claim 1**
- support: all key results remain in vitro
- details: enzyme and cell-culture evidence only
- implicit_premise: do not promote the paper into veterinary treatment guidance

**Claim 2**
- support: later discussion raises therapeutic-index and tolerability concerns around nitazoxanide
- details: promising potency is not enough for routine use claims
- implicit_premise: assay-stage leads remain bounded until stronger translational evidence exists

## Phase 2.5: Write-Back Implications

### For `topics/fcv/translation-brief.md`

- this becomes the deep-extracted assay-stage therapy anchor beneath `src-fcv-008` and `src-fcv-018`

### For `topics/fcv/current-state-dashboard.md`

- the therapy row can now be described as a three-layer branch: assay-stage discovery, strain-sensitive caution, and first in vivo signal

### For `system/indexes/fcv-source-depth-map.md`

- `src-fcv-014` should move from partial/source_checked into full/deep_extracted

### For `system/indexes/fcv-source-index.md`

- the source should no longer be described as first-pass ingest

## Phase 3: Promotion Check

- source_card_updates:
  - preserve assay-stage therapy architecture
  - preserve enzyme-hit versus cell-culture-hit separation
  - preserve anti-clinical-overclaim boundary
- topic_write_back_targets:
  - `topics/fcv/translation-brief.md`
  - `topics/fcv/current-state-dashboard.md`
  - `system/indexes/fcv-source-depth-map.md`
  - `system/indexes/fcv-source-index.md`
- not_safe_to_promote_yet:
  - any owner-facing treatment recommendation
  - any claim that nitazoxanide or 2CMC are established feline FCV therapies
  - any flattening of enzyme hits and cell-culture hits into one equivalent shortlist
- conflicts_with_existing_vault:
  - none; this worksheet gives the FCV therapy branch its missing assay-stage control layer
