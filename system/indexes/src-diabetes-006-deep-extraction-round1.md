# Deep Extraction Worksheet

Source: `src-diabetes-006`  
Title: `The Role of Diet in the Prevention and Management of Feline Diabetes`  
Method note: this worksheet is based on PubMed abstract-level evidence and source-card metadata, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The paper covers prevention and management

- core_claim: diet can affect both diabetes risk and diabetes treatment.
- implicit_premise: diet should be split into prevention, management, and remission-related questions.
- relation_to_previous: opening nutrition frame.
- hard_details: abstract says the review focuses on how diet may lower or increase diabetes risk and reviews diet in treatment.
- tension_or_surprise: diet is not one intervention; it acts across disease stages.

#### Unit 2: Evidence and physiology are both used

- core_claim: the review cites published studies where available but also uses clinical experience and physiologic principles where evidence is lacking.
- implicit_premise: diet guidance may mix direct evidence with expert interpretation.
- relation_to_previous: establishes evidence-quality boundary.
- hard_details: abstract explicitly distinguishes published-study evidence from areas where research evidence is lacking.
- tension_or_surprise: diet recommendations may be practical but not always trial-backed.

## Phase 1: Theme Reconstruction

## Theme: Diet is a cross-stage branch

This paper supports positioning diet across prevention and management, rather than only as a treatment add-on after diagnosis.

### Hard Information

- diet is discussed for lowering or increasing diabetes risk
- diet is discussed for treatment of diabetes

## Theme: Diet claims need evidence labels

The abstract itself warns that some guidance depends on clinical experience and physiology where research evidence is lacking. That makes it a useful boundary source, not only a diet-advocacy source.

### Hard Information

- published studies are cited where they exist
- clinical experience and physiologic principles are used where evidence is lacking

## Phase 2: Claim-Evidence Structure

### Diet Key Points

**Claim 1**
- support: abstract-level prevention and treatment scope
- details: diet belongs in risk, endpoint, and translation pages
- implicit_premise: prevention and management claims should be separated

**Claim 2**
- support: abstract-level evidence-boundary statement
- details: diet claims require careful labels
- implicit_premise: some recommendations may be source-supported but not trial-proven

## Phase 2.5: Write-Back Implications

### For `topics/diabetes/risk-and-recognition.md`

- include diet as prevention/risk pressure only with evidence-quality caveat

### For `topics/diabetes/endpoint-handbook.md`

- separate diet composition endpoints from remission endpoints

### For `topics/diabetes/translation-brief.md`

- distinguish direct published evidence from expert/physiology-based guidance

## Phase 3: Promotion Check

- source_card_updates:
  - promote to diet overview anchor
  - preserve evidence-boundary language
- topic_write_back_targets:
  - `topics/diabetes/risk-and-recognition.md`
  - `topics/diabetes/endpoint-handbook.md`
  - `topics/diabetes/translation-brief.md`
  - `topics/diabetes/synthesis-index.md`
- not_safe_to_promote_yet:
  - exact diet composition recommendations
  - product-level diet claims
  - strong prevention claims without study-level extraction
- conflicts_with_existing_vault:
  - none; it keeps diet important but evidence-labeled

