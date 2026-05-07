---
id: system-conflict-register
type: index
topic: system
question_type: conflict-map
language: bilingual
last_compiled_at: 2026-04-23
owner: codex
status: active
---

# Conflict Register

This page records source-to-source tensions that matter for compilation quality.

## Current Status

2026-04-11 initial pass covered `src-ckd-003`, `src-ckd-004`, `src-ckd-010` (reinforced vault direction, no direct contradictions requiring arbitration).

2026-04-18 CKD full pass: all 24 CKD deep-extraction files reviewed. 8 new tensions identified, 5 existing tensions confirmed. Total: 13 active tensions across 19 source cards.

2026-04-18 FIP / IBD state-sync pass: all 24 FIP and all 24 IBD round-1 worksheets reviewed for tracker write-back. No direct source-to-source contradictions requiring arbitration were identified. Current pressure in those modules is boundary discipline and overclaim control rather than conflict resolution.

2026-04-23 HCM / Diabetes boundary audit: all HCM and Diabetes source-card summaries plus current compiled owner pages were reviewed for source-to-source conflict pressure. No direct contradiction requiring reversal of a compiled disease spine was identified. Added HCM and Diabetes as active boundary-tension sections because both modules can be miscompiled if augmentation signals are treated as replacement authority or if treatment branches are flattened into rankings. Current register total: 22 active tensions across CKD, HCM, and Diabetes; FIP / IBD remain tracked as no-direct-conflict state-sync modules.

## Active Tension To Track

### CKD detection logic: practical core vs early-detection augmentation

- source_ids: `src-ckd-004`, `src-ckd-018`, `src-ckd-024`
- tension:
  `src-ckd-004` says SDMA cannot yet serve as a standalone screening test and keeps creatinine plus USG plus persistence as the practical core.
  Newer biomarker literature may improve earlier discrimination, but does not yet replace serial surveillance.
- current safe resolution:
  Keep `creatinine + USG + persistence + routine workup` as the operational backbone.
  Treat SDMA and newer biomarker-panel approaches as adjunctive early-detection support.

### CKD treatment logic: routine use vs strength of evidence

- source_ids: `src-ckd-003`, `src-ckd-007`, `src-ckd-014`
- tension:
  Common use of adjunct therapies can look stronger than the evidence base actually supports.
- current safe resolution:
  Keep renal diet and phosphorus control at the top of the treatment hierarchy.
  Label adjunct branches such as RAAS therapy, long-term fluids, and other supportive care with explicit evidence-strength caution.

### CKD phosphorus-control logic: diet-first hierarchy vs binder use in practice

- source_ids: `src-ckd-004`, `src-ckd-006`, `src-ckd-007`
- tension:
  Phosphate binders are operationally important, but the current feline evidence layer still supports diet more strongly than binder-first logic.
- current safe resolution:
  Keep phosphate-restricted diet above binder adjuncts.
  Present binders as clinically relevant when diet alone is insufficient, while preserving licensing and evidence-strength caution.

### CKD proteinuria logic: generic progression marker vs compartment-specific glomerular signal

- source_ids: `src-ckd-009`, `src-ckd-010`, `src-ckd-017`, `src-ckd-024`
- tension:
  Proteinuria appears both as a hemodynamic/progression marker in broader CKD and as a direct glomerular-disease signal in a narrower proteinuric subset.
- current safe resolution:
  Keep UPCR/proteinuria in the first-wave endpoint set, but preserve compartment-aware wording.
  Do not treat UPC magnitude alone as self-interpreting, and do not flatten all proteinuric cats into one CKD subtype story.

### CKD hypertension logic: older prevention framing vs later comorbidity/prognostic framing

- source_ids: `src-ckd-008`, `src-ckd-009`
- tension:
  The 2011 prevention-oriented review says hypertension is not a prognostic indicator in cats in its abstract framing, while the later dedicated comorbidity review gives hypertension a much stronger role in subgroup structure, target-organ-damage risk, and management importance.
- current safe resolution:
  Treat the older statement as date-bounded review framing rather than as a timeless rule.
  Keep SBP clinically important in current compilation, but avoid overstating it as a uniform standalone prognostic shortcut outside context.

## Tensions Added 2026-04-18 (Full 24-card Extraction Pass)

### Glomerular vs tubulointerstitial disease primacy

- source_ids: `src-ckd-016`, `src-ckd-017`, `src-ckd-022`, `src-ckd-010`
- tension:
  `src-ckd-016` frames feline CKD as tubulointerstitial-first with rare primary glomerulopathies. `src-ckd-017` reports 58% ICGN in proteinuric subset (74% of protein-losing nephropathy cats). `src-ckd-022` shows experimental ischemia eventually produces glomerulosclerosis. The question: is the vault building a tubulointerstitial-dominant synthesis, or does a clinically important proteinuric subpopulation need glomerular-first reasoning?
- current safe resolution:
  Keep tubulointerstitial-fibrosis-first as the backbone for general feline CKD. Explicitly carve out a glomerular-disease branch for proteinuric cats with high UPC and protein-losing nephropathy features. Do not let the majority-population framing silently absorb the proteinuric subset.

### Phosphate restriction benefit vs hypercalcaemia risk

- source_ids: `src-ckd-004`, `src-ckd-006`, `src-ckd-003`, `src-ckd-015`
- tension:
  Three sources treat phosphate-restricted renal diet as the strongest first-line CKD intervention with survival data. `src-ckd-015` introduces a complication: dietary phosphate restriction may contribute to hypercalcaemia in some CKD cats, with increased total hypercalcaemia risk and potential nephrocalcinosis links. The dominant first-line recommendation carries a documented risk on a different mineral axis.
- current safe resolution:
  Preserve phosphate-restricted diet as primary first-line (survival benefit evidence is stronger). Add bounded caution: dietary phosphate restriction should be accompanied by calcium monitoring, particularly in cats at higher hypercalcaemia risk. Not a reversal, but synthesis pages should not present it as consequence-free.

### FGF23 timing: early marker vs conflicted clinical role

- source_ids: `src-ckd-015`, `src-ckd-024`
- tension:
  `src-ckd-015` reports FGF23 increases before azotaemic CKD, framing it as an early mineral signal. `src-ckd-024` groups it with emerging markers not yet suitable for routine use. `src-ckd-015` itself notes conflicting evidence for FGF23 and α-Klotho in calcium homeostasis. Is FGF23's early rise a useful leading indicator, or a biologically interesting but clinically unresolved signal?
- current safe resolution:
  Do not promote FGF23 into first-wave endpoint shortlist. Acknowledge it reinforces the argument that CKD-MBD starts before overt hyperphosphataemia. Preserve explicit boundary that clinical interpretation remains conflicted and not actionable in routine feline practice.

### RAAS activation: experimental model vs natural disease

- source_ids: `src-ckd-009`, `src-ckd-021`
- tension:
  `src-ckd-009` frames CKD-hypertension relationship as bidirectional with RAAS-targeting drugs (telmisartan) given clinical weight. `src-ckd-021` reports that while RAAS activation is clear in induced feline CKD models (renin, aldosterone, angiotensin all rise after ischemia), naturally occurring normotensive azotaemic CKD cats did not show clearly elevated RAAS biomarkers vs controls. Treatment rationale implicitly assumes RAAS overactivation that the natural-disease data does not consistently support.
- current safe resolution:
  Keep telmisartan and amlodipine as clinically relevant antihypertensives with empirical blood-pressure-lowering rationale. Do not assert that spontaneous feline CKD has consistently elevated circulating RAAS biomarkers. Distinguish: the drug works on blood pressure, but its mechanism in natural feline CKD may differ from the induced-model RAAS-activation story.

### Protein restriction survival benefit vs sarcopenia risk

- source_ids: `src-ckd-003`, `src-ckd-004`, `src-ckd-005`, `src-ckd-019`
- tension:
  Multiple sources frame protein-restricted renal diets as having the strongest survival evidence. `src-ckd-019` lists sarcopenia as a recognized sign in both hyperthyroid and CKD older cats. `src-ckd-016` lists progressive muscle wasting. `src-ckd-014` reports 36.9% of cats on renal diets had intake below 75% of daily requirements. Protein restriction in aged sarcopenic cats could worsen muscle mass loss, a concern well-documented in human CKD but largely absent from the feline survival-trial framing.
- current safe resolution:
  Renal diet remains strongest first-line recommendation. Synthesis pages should note protein restriction carries a potential interaction with sarcopenia risk in aging or hyperthyroid-concurrent cats. Monitoring body condition score and muscle mass is not optional. Do not import human CKD protein-restriction controversy wholesale, but do not pretend the issue is settled either.

### Benazepril ACEI caution vs telmisartan ARB endorsement

- source_ids: `src-ckd-003`, `src-ckd-007`, `src-ckd-009`, `src-ckd-014`
- tension:
  `src-ckd-003` establishes benazepril improved appetite but not survival in proteinuric CKD cats. `src-ckd-007` grades RAAS interventions cautiously. `src-ckd-009` names telmisartan (an ARB, pharmacologically distinct from benazepril's ACE inhibition) as a current antihypertensive option. `src-ckd-014` reports 59.9% ACEI usage in Portuguese practice. The vault risks conflating two distinct RAAS drug classes with different evidence bases.
- current safe resolution:
  Split RAAS treatment into two distinct branches. Benazepril/ACEI: survival benefit not demonstrated, appetite benefit present, evidence caution applies. Telmisartan/ARB: different mechanism (AT1 blockade vs ACE inhibition), endorsed in guidelines, but equivalent survival evidence has not been applied. Do not allow benazepril's negative finding to absorb telmisartan, and do not allow telmisartan's guideline presence to rehabilitate benazepril.

### Early detection: biomarker-centric vs owner-observation recognition gap

- source_ids: `src-ckd-012`, `src-ckd-002`, `src-ckd-005`, `src-ckd-018`
- tension:
  `src-ckd-012` establishes that owners noticed polydipsia/polyuria before CKD diagnosis. `src-ckd-005` frames late diagnosis as the main strategic bottleneck. `src-ckd-002` and `src-ckd-018` frame the early-detection problem in biomarker terms (creatinine insensitivity, SDMA validation, metabolomics). The vault's early-detection architecture is biomarker-centric and may undersell the recognition gap at the owner/veterinary interface.
- current safe resolution:
  Preserve biomarker-development narrative as the technical frontier. Add an explicit owner-recognition layer: PU/PD observed by owners before diagnosis is documented and represents an actionable low-tech recognition prompt. The two framings address different parts of the same problem (owner-side signal vs laboratory-side sensitivity) and should not be collapsed into one "detection is hard" paragraph.

### Aging: epidemiological risk factor vs cellular senescence mechanism

- source_ids: `src-ckd-023`, `src-ckd-001`, `src-ckd-016`, `src-ckd-011`
- tension:
  `src-ckd-001`, `src-ckd-016`, `src-ckd-011` treat aging as contextual background. `src-ckd-023` provides direct feline tissue evidence: CKD kidneys show telomere shortening in renal tubular cells and increased senescence-associated β-galactosidase staining, kidney-specific (absent in liver/skin). Aging in feline CKD is not just an epidemiological risk factor, there is tissue-level mechanistic evidence of cellular senescence.
- current safe resolution:
  Keep fibrosis as primary mechanism backbone (multiple convergent sources). Add cellular senescence as second-tier mechanism enrichment: kidney-specific, direct feline tissue support, opens senolytic hypothesis not yet validated. Mechanism overview should distinguish aging as epidemiological risk (cats >12y) from aging as cellular biology (telomere shortening, senescence enrichment in CKD tissue).

## Tensions Added 2026-04-23 (HCM Boundary Audit)

### HCM recognition: structure-first confirmation vs biomarker / AI augmentation

- source_ids: `src-hcm-001`, `src-hcm-006`, `src-hcm-007`, `src-hcm-009`, `src-hcm-010`, `src-hcm-013`, `src-hcm-017`, `src-hcm-023`, `src-hcm-024`
- tension:
  The HCM corpus contains real biomarker and AI augmentation signals, including troponin I, NT-proBNP, novel biomarkers, and radiograph-based deep learning. The same corpus repeatedly keeps structural phenotype, echocardiography, morphometry, and anatomopathology as the safer confirmation layer. The risk is compiling every support signal into a replacement diagnostic shortcut.
- current safe resolution:
  Keep structural phenotype confirmation first. Use biomarkers and AI as support, screening, severity, or stratification branches. Do not let troponin, NT-proBNP, frontier markers, or AI replace echo-led or morphometry-led phenotype authority in compiled pages.

### HCM model value: human-HCM analogy vs feline clinical equivalence

- source_ids: `src-hcm-003`, `src-hcm-004`, `src-hcm-016`, `src-hcm-011`, `src-hcm-014`, `src-hcm-015`
- tension:
  The corpus supports feline HCM as a useful spontaneous model with human-HCM genotype and phenotype similarities, especially in Maine Coon / Ragdoll mutation contexts. But treatment evidence remains overclaim-sensitive, and model similarity does not automatically import human treatment hierarchy, endpoint hierarchy, or regulatory assumptions into feline practice.
- current safe resolution:
  Preserve model value for mechanism, phenotype, mutation-context, and targeted-frontier reasoning. Do not compile model similarity as clinical equivalence. Keep treatment hierarchy and routine-use claims behind feline-specific outcome and full-text evidence.

### HCM treatment: targeted frontier signal vs evidence-skepticism control

- source_ids: `src-hcm-008`, `src-hcm-011`, `src-hcm-014`, `src-hcm-015`, `src-hcm-020`
- tension:
  MYK-461 and remodeling papers make the treatment branch more than supportive care, while the enalapril and treatment-survey / literature-search layer keeps routine HCM treatment evidence thin and scenario-dependent. The risk is promoting acute physiologic improvement or historical treatment use into a final intervention ranking.
- current safe resolution:
  Keep HCM treatment as branch comparison: bounded management, selective targeted frontier, older conventional therapy, and evidence skepticism. Do not rank interventions until full-text and output-specific evidence support final ordering.

### HCM disease boundary: HCM dominance vs broader myocardial disease map

- source_ids: `src-hcm-001`, `src-hcm-002`, `src-hcm-005`, `src-hcm-007`, `src-hcm-018`, `src-hcm-021`
- tension:
  HCM is repeatedly described as the most common feline cardiomyopathy, but the corpus also keeps non-HCM cardiomyopathies and broader myocardial disease visible. HCM dominance can erase DCM, RCM, ARVC, LVNC, UCM, and nonspecific cardiomyopathy boundaries if compiled as "feline cardiomyopathy equals HCM."
- current safe resolution:
  Let HCM lead the disease module, but preserve cardiomyopathy-boundary routing. Use HCM as the dominant branch, not as a synonym for all feline myocardial disease.

## Tensions Added 2026-04-23 (Diabetes Boundary Audit)

### Diabetes disease model: type-2-like default vs secondary endocrine / pancreatitis branches

- source_ids: `src-diabetes-001`, `src-diabetes-002`, `src-diabetes-003`, `src-diabetes-010`, `src-diabetes-013`, `src-diabetes-014`, `src-diabetes-020`, `src-diabetes-021`
- tension:
  Several sources frame feline diabetes as type-2-like, with insulin resistance, obesity, residual insulin secretion, and beta-cell decline. Other sources keep hypersomatotropism, acromegaly, hyperadrenocorticism, and pancreatitis visible as branch-changing comorbid or secondary drivers. The risk is flattening the module into a single type-2-like story.
- current safe resolution:
  Compile feline diabetes as a mixed metabolic / endocrine syndrome. Use type-2-like disease as the default frame, but route difficult control, high insulin needs, pancreatitis / DKA complexity, and endocrine signs into secondary branch checks.

### Diabetes remission / diet optimism vs evidence-quality boundary

- source_ids: `src-diabetes-006`, `src-diabetes-007`, `src-diabetes-015`, `src-diabetes-016`, `src-diabetes-022`, `src-diabetes-024`
- tension:
  Diet and insulin studies create real remission or insulin-requirement signals, including low-carbohydrate / low-fiber diet and glargine U300 branches. The systematic-review boundary says evidence quality is moderate to poor and no single factor predicts remission. The risk is compiling study signals into a universal remission protocol.
- current safe resolution:
  Keep remission as a visible endpoint and control branch. Do not rank diets, insulin protocols, or remission predictors without full-text design checks and definition alignment.

### Diabetes treatment route: SGLT2 approval / oral route vs safety and candidate gates

- source_ids: `src-diabetes-011`, `src-diabetes-024`, `src-reg-010`, `src-reg-011`, `src-reg-012`, `src-reg-013`
- tension:
  SGLT2 inhibitors are now a real U.S. FDA-regulated feline treatment branch, and oral route can look operationally attractive. The same source layer keeps residual beta-cell function, insulin-naive / uncomplicated-disease selection, ketone monitoring, contraindications, and euglycemic DKA risk ahead of convenience.
- current safe resolution:
  Treat SGLT2 as a candidate-gated regulatory / treatment branch, not a route-convenience winner. Do not rank Bexacat, Senvelgo, insulin, or oral route against each other without product-label and full-text comparator control.

### Diabetes obesity: risk-factor logic vs current presentation-state sequencing

- source_ids: `src-diabetes-001`, `src-diabetes-005`, `src-diabetes-006`, `src-diabetes-014`, `src-diabetes-021`
- tension:
  Obesity is a major insulin-resistance and risk branch, but diabetic cats may present after weight and muscle loss, and glycemic stabilization may need to precede caloric restriction in some cases. The risk is compiling obesity into a simple "all diabetic cats need immediate weight loss" instruction.
- current safe resolution:
  Keep obesity upstream in mechanism and recognition. Separate historical overweight / insulin resistance from current body condition, muscle state, stabilization needs, and diet composition decisions.

### Diabetes breed risk: Burmese signal vs population-specific denominator

- source_ids: `src-diabetes-009`, `src-diabetes-012`
- tension:
  UK insured-population and Australian datasets both support Burmese predisposition signals, but the denominators, geography, time windows, and population structures differ. The risk is converting breed association into a universal prevalence or mechanism claim.
- current safe resolution:
  Preserve Burmese as a recurring risk signal. Keep prevalence and risk-magnitude language tied to study population, geography, and denominator. Do not infer a universal mechanism from the current compiled epidemiology layer alone.
