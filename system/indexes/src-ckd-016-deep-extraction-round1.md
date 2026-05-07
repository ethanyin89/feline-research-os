# Deep Extraction Worksheet

Source: `src-ckd-016`  
Title: `Chronic Kidney Disease in Aged Cats: Clinical Features, Morphology, and Proposed Pathogeneses`  
Method note: this worksheet is based on accessible abstract and visible review framing, not full section-by-section extraction of the entire paper.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The disease is framed as a geriatric feline condition

- core_claim: feline CKD is primarily a disease of aged cats, and this age relationship is part of the basic disease frame rather than a side observation.
- implicit_premise: age-related biology matters to both recognition and pathogenesis.
- relation_to_previous: opening disease frame.
- hard_details: most affected cats are geriatric, older than 12 years of age.
- tension_or_surprise: this is stronger than a generic “older cats are at risk” statement.

#### Unit 2: The lesion pattern is mainly tubulointerstitial and fibrotic

- core_claim: the typical pathology of feline CKD centers on interstitial inflammation, tubular atrophy, fibrosis, and secondary glomerulosclerosis.
- implicit_premise: lesion-centered reading is more accurate than symptom-first reading.
- relation_to_previous: moves from demographic framing to lesion identity.
- hard_details: interstitial inflammation, tubular atrophy, fibrosis, secondary glomerulosclerosis.
- tension_or_surprise: the review explicitly contrasts cats with people and dogs by noting that marked primary glomerulopathies are rare in cats.

#### Unit 3: Initiation and progression are not the same problem

- core_claim: the factors implicated in initiation are broader than those implicated in progression.
- implicit_premise: one of the reasons CKD becomes confusing is that people mix causal-initiation and progression variables together.
- relation_to_previous: deepens the disease story beyond morphology.
- hard_details: initiation factors include aging, ischemia, comorbid conditions, phosphorus overload, and routine vaccinations; progression factors include dietary phosphorus intake, magnitude of proteinuria, and anemia.
- tension_or_surprise: this split is operationally useful because it matches how the vault already treats phosphorus, proteinuria, and anemia as downstream bridge variables.

#### Unit 4: Ischemia and hypoxia are plausible upstream branches

- core_claim: ischemia and renal hypoxia deserve serious consideration as contributors to feline CKD initiation and progression.
- implicit_premise: episodic vascular compromise may help explain why fibrosis emerges so often in aged feline kidneys.
- relation_to_previous: links the review's pathogenesis framing to lesion interpretation.
- hard_details: experimental renal ischemia produces morphologic changes similar to spontaneous CKD; renal hypoxia may play a role in initiation and progression.
- tension_or_surprise: this aligns unusually well with the new experimental ischemia-model paper.

## Phase 1: Theme Reconstruction

## Theme: Aged-cat CKD is mostly a fibrosis-centered tubulointerstitial disease

This paper reinforces a major vault conclusion: feline CKD in aged cats is not best framed as a heavily proteinuric primary glomerular disease. It is mainly a tubulointerstitial disease with fibrosis as a central lesion and glomerulosclerosis often secondary.

### Hard Information

- geriatric >12 years
- interstitial inflammation
- tubular atrophy
- fibrosis
- secondary glomerulosclerosis

## Theme: Pathogenesis should be separated into upstream contributors and downstream progression drivers

One of the most useful features of this review is that it separates possible initiators from factors that influence progression after disease is established. This maps well onto the vault's structure because it keeps aging and ischemia in the upstream story while phosphorus, proteinuria, and anemia sit lower in the progression story.

### Hard Information

- initiation: aging, ischemia, comorbid conditions, phosphorus overload, routine vaccinations
- progression: dietary phosphorus intake, magnitude of proteinuria, anemia

## Phase 2: Claim-Evidence Structure

### Mechanism-Pathogenesis Key Points

**Claim 1**
- support: the review says typical feline CKD histology is interstitial inflammation, tubular atrophy, fibrosis, and secondary glomerulosclerosis
- details: primary glomerulopathies with marked proteinuria are rare in cats
- implicit_premise: spontaneous feline CKD should not be framed as a glomerular-first disease by default

**Claim 2**
- support: the review identifies aging and ischemia/hypoxia as plausible contributors to initiation, while phosphorus intake, proteinuria, and anemia relate to progression
- details: factors are split explicitly
- implicit_premise: separating initiation and progression improves disease reasoning

## Phase 3: Promotion Check

- source_card_updates:
  - add aged-cat and morphology details
  - add initiation-versus-progression distinction
  - add ischemia/hypoxia bridge wording
- topic_write_back_targets:
  - `topics/ckd/mechanism-overview.md`
  - `topics/ckd/pathology-correlations.md`
  - `topics/ckd/early-detection.md`
- not_safe_to_promote_yet:
  - any claim that routine vaccination is a settled causal driver
  - any claim that ischemia/hypoxia fully explains spontaneous feline CKD
- conflicts_with_existing_vault:
  - none; this review mainly strengthens and organizes existing CKD framing
