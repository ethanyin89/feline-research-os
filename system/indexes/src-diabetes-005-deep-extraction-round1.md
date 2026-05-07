# Deep Extraction Worksheet

Source: `src-diabetes-005`  
Title: `Feline comorbidities: Pathophysiology and management of the obese diabetic cat`  
Method note: this worksheet is based on Crossref abstract-level evidence and source-card metadata, not full section-by-section extraction of the complete article text.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The paper starts from obesity prevalence

- core_claim: overweight and obesity are common in domestic cats.
- implicit_premise: obesity is not an edge-case modifier for feline diabetes.
- relation_to_previous: opening population and risk frame.
- hard_details: abstract reports that up to 40% of the domestic feline population is overweight or obese.
- tension_or_surprise: a high-prevalence upstream condition can shape a large fraction of diabetes risk.

#### Unit 2: Obesity produces insulin resistance

- core_claim: feline obesity reduces insulin sensitivity through multiple mechanisms.
- implicit_premise: body condition belongs in the mechanism spine and endpoint plan.
- relation_to_previous: converts obesity prevalence into causal pressure.
- hard_details: abstract reports a decline in insulin sensitivity with each excess kilogram of body weight.
- tension_or_surprise: weight is not just a background risk marker; it affects insulin physiology.

#### Unit 3: Diabetes emerges when insulin resistance meets beta-cell dysfunction

- core_claim: obese insulin-resistant cats become diabetic when beta-cell dysfunction is also present.
- implicit_premise: obesity alone is not the whole disease explanation.
- relation_to_previous: aligns with the pathogenesis source's two-part mechanism spine.
- hard_details: abstract frames overt diabetes as a risk when insulin resistance coexists with beta-cell dysfunction.
- tension_or_surprise: this preserves beta-cell failure as the threshold event.

#### Unit 4: Management sequencing matters

- core_claim: diabetic control may need to precede caloric restriction in some obese diabetic cats.
- implicit_premise: weight management cannot be treated as a naive first action in every diabetic cat.
- relation_to_previous: moves from pathophysiology into treatment sequencing.
- hard_details: abstract notes that many obese diabetic cats have lost weight and muscle by presentation, so initial diabetic control may be needed before caloric restriction.
- tension_or_surprise: obesity history and presentation state can diverge.

## Phase 1: Theme Reconstruction

## Theme: Obesity is a mechanism branch, not just a risk label

This paper supports a direct link between obesity, insulin sensitivity, beta-cell strain, and overt diabetes risk.

### Hard Information

- overweight/obesity is common in domestic cats
- obesity reduces insulin sensitivity
- overt diabetes risk rises when insulin resistance coexists with beta-cell dysfunction

## Theme: Management must account for current body state

The review warns against mechanically applying weight loss before stabilizing the diabetic cat, especially when presentation already includes weight and muscle loss.

### Hard Information

- some degree of diabetic control may be attempted before caloric restriction
- diet composition and insulin therapy are both part of management

## Phase 2: Claim-Evidence Structure

### Obesity-Management Key Points

**Claim 1**
- support: abstract-level obesity prevalence and insulin-sensitivity statements
- details: obesity belongs in pathogenesis, recognition, and treatment pages
- implicit_premise: body condition is a causal and management variable

**Claim 2**
- support: abstract-level beta-cell dysfunction threshold framing
- details: obesity pressure needs beta-cell failure to become overt diabetes
- implicit_premise: this source aligns with `src-diabetes-001`

**Claim 3**
- support: abstract-level sequencing statement
- details: immediate caloric restriction is not always the first management move
- implicit_premise: treatment pages must preserve clinical sequencing

## Phase 2.5: Write-Back Implications

### For `topics/diabetes/mechanism-overview.md`

- place obesity upstream of insulin resistance and beta-cell stress

### For `topics/diabetes/risk-and-recognition.md`

- include body condition as a risk branch, not just a lifestyle note

### For `topics/diabetes/translation-brief.md`

- separate stabilization, diet composition, and weight-loss sequencing

## Phase 3: Promotion Check

- source_card_updates:
  - promote to obesity and management-sequencing anchor
  - preserve abstract-level diet and insulin co-management language
- topic_write_back_targets:
  - `topics/diabetes/mechanism-overview.md`
  - `topics/diabetes/risk-and-recognition.md`
  - `topics/diabetes/translation-brief.md`
  - `topics/diabetes/current-state-dashboard.md`
- not_safe_to_promote_yet:
  - exact calorie targets or diet percentages without full-text check
  - product-level diet recommendations
  - universal sequencing rules
- conflicts_with_existing_vault:
  - none; it strengthens the obesity and diet branches

