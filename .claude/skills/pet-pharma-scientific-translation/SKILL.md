---
name: pet-pharma-scientific-translation
description: >
  Translate and professionally edit English-Chinese scientific content in veterinary medicine,
  companion-animal health, pet pharmaceuticals, disease models, pharmacology, toxicology,
  diagnostics, biomarkers, and clinical research. Use for abstracts, full papers, methods,
  results, discussions, study reports, literature reviews, and technical R&D materials when
  terminology consistency, evidentiary strength, numerical fidelity, study-design accuracy,
  and natural professional Chinese expression matter. Do not use for popular-science rewriting,
  marketing copy, regulatory news, or general consumer content unless the user explicitly asks
  for a scientific-professional version.
---

# Pet Pharma Scientific Translation

## Purpose

Produce Chinese scientific text that is simultaneously:

1. faithful to the source;
2. natural to veterinary and biomedical professionals;
3. consistent in terminology;
4. calibrated to the strength of the evidence;
5. explicit about study design, sample, endpoints, results, and limitations;
6. free of literal-translation artifacts and unsupported interpretation.

The default target reader is a veterinary researcher, R&D scientist, clinical investigator,
technical product manager, or advanced veterinary professional.

## Core rule

Translate meaning first, then reconstruct the sentence in professional Chinese. Do not preserve
English word order when doing so makes the Chinese unnatural. Do not strengthen causality,
certainty, efficacy, safety, or clinical applicability beyond what the study design supports.

## Required workflow

### Step 1: Identify source type and translation boundary

Classify the input before translating:

- title / abstract;
- introduction / literature review;
- materials and methods;
- results;
- discussion / conclusion;
- figure or table legend;
- full paper;
- study report / technical report;
- literature synthesis.

Determine whether the user wants:

- faithful scientific translation;
- scientific editing of an existing translation;
- bilingual side-by-side output;
- terminology normalization;
- translation plus separate explanatory notes.

Unless requested otherwise, do not mix explanation into the translated body.

### Step 2: Build and lock a terminology sheet

Before translating a long document, extract and normalize:

- diseases and clinical states;
- anatomy and physiology;
- drugs, targets, pathways, genes, and proteins;
- assays, imaging methods, and laboratory methods;
- endpoints and statistical terms;
- study populations and animal models;
- abbreviations.

Use `references/glossary_seed.csv` as the starting glossary and extend it for the document.
For uncertain or current terms, verify against authoritative sources such as PubMed/PMC,
major veterinary journals, official drug labels, VICH/EMA/FDA CVM/USDA/MARA documents, or
recognized professional guidelines.

Never silently alternate between multiple Chinese renderings of the same technical term.

### Step 3: Preserve the evidence structure

For each claim, retain:

- subject and comparison group;
- study design;
- sample size;
- intervention or exposure;
- endpoint;
- direction and magnitude of effect;
- uncertainty or statistical qualification;
- time point;
- limitation or boundary condition.

Do not convert association into causation. Do not convert exploratory findings into validated
clinical conclusions. Do not convert model evidence into clinical efficacy.

Read `references/evidence-language-map.md` before translating Results, Discussion, or Conclusions.

### Step 4: Translate section by section

Apply section-specific rules from `references/source-type-rules.md`.

General rules:

- Preserve headings, paragraph order, citation markers, figure/table numbers, and footnotes.
- Preserve all numbers, signs, units, ranges, confidence intervals, and P values.
- Preserve species, breed, sex, age, disease stage, and sample-source distinctions.
- Preserve whether animals are client-owned, purpose-bred, experimentally induced, naturally
  affected, cadaveric/postmortem, or cell-derived.
- Distinguish in vitro, ex vivo, in vivo, animal-model, and clinical evidence.
- At first mention, normally use `中文全称（English full term, abbreviation）`; thereafter use the
  accepted abbreviation or Chinese short form consistently.
- Do not translate gene/protein symbols, drug codes, assay names, or registered product names
  unless an authoritative Chinese name exists.
- Use “实验用猫” rather than “实验猫” when referring to cats used for research in the Chinese
  laboratory-animal context.

### Step 5: Scientific Chinese editing

After the faithful draft, rewrite for professional Chinese:

- move the main subject and result forward;
- reduce stacked premodifiers;
- replace unnecessary passive constructions;
- split overlong English sentences when needed;
- combine fragmented short clauses when the logical relationship is clear;
- use explicit logical connectors only when present or strongly implied;
- avoid empty nominalization such as “进行了……的研究” when a direct verb is clearer;
- avoid promotional adjectives unless they are part of a quoted source.

The target should read as if originally written by a competent Chinese veterinary scientist,
not as translated English.

### Step 6: Independent bilingual QA

Run a second-pass review using `templates/qa-checklist.md`.

At minimum, verify:

- terminology consistency;
- number and unit fidelity;
- treatment/control direction;
- species and subgroup fidelity;
- evidence-strength calibration;
- causality and modality;
- clinical vs preclinical boundary;
- abbreviations and first mention;
- citations, figure/table numbering, and reference integrity;
- naturalness and absence of translationese.

For long files, optionally run:

```bash
python scripts/check_terms.py translated.md --glossary references/glossary_seed.csv
python scripts/check_numbers.py source.md translated.md
```

### Step 7: Deliver in a usable structure

Default output for a long scientific translation:

1. title and document metadata;
2. terminology sheet, only when useful;
3. translated body preserving source hierarchy;
4. translator notes, only for genuine ambiguity or terminology decisions;
5. QA summary listing unresolved uncertainties.

Do not expose internal chain-of-thought or low-level execution details. Show only decisions that
matter to the user's interpretation or later editing.

## Translation priorities

When priorities conflict, use this order:

1. factual fidelity;
2. evidentiary fidelity;
3. terminology consistency;
4. structural fidelity;
5. professional naturalness;
6. stylistic elegance.

Never sacrifice factual or evidentiary fidelity for smoother prose.

## Mandatory distinctions

Maintain these distinctions explicitly:

- association vs causation;
- statistical significance vs clinical relevance;
- efficacy vs effectiveness;
- safety signal vs established risk;
- exploratory vs validated biomarker;
- proof of concept vs clinical guidance;
- animal model vs client-owned clinical population;
- acute pharmacodynamic effect vs long-term outcome benefit;
- diagnosis vs screening vs risk stratification;
- absence of evidence vs evidence of absence.

## Preferred scientific register

Prefer:

- “研究显示……” when the design directly supports the observation;
- “结果提示……” for suggestive or exploratory evidence;
- “与……相关” for association;
- “支持……这一假设” for indirect mechanistic support;
- “尚不能据此判断……” when the design does not answer the clinical question;
- “其临床意义仍需在……中验证” for translational limits.

Avoid:

- “证实” unless evidence is genuinely definitive;
- “显著改善” when only a statistically significant surrogate changed;
- “可用于诊断/治疗” when the study only explored potential utility;
- “无效/不存在” when the study merely failed to detect a difference;
- marketing language such as “突破性、颠覆性、革命性、里程碑式” without explicit source support.

## Output modes

### Mode A: Faithful scientific translation

Use for papers, reports, and supplementary materials. Preserve all information and structure.
Do not summarize or interpret inside the translation.

### Mode B: Scientific polished translation

Preserve all substantive information while improving Chinese sentence architecture and field
usage. This is the default mode.

### Mode C: Translation plus scientific annotation

Provide the translation first, followed by clearly separated notes explaining terminology,
study design, evidence limits, or alternative renderings. Never insert annotations into the
translated body unless requested.

### Mode D: Existing translation audit

Compare source and target, then classify issues as:

- critical factual error;
- evidence-strength distortion;
- terminology error;
- omission/addition;
- structural mismatch;
- unnatural professional expression;
- formatting/citation issue.

## Refusal and uncertainty policy

If a term cannot be verified confidently:

1. preserve the English term;
2. provide the best provisional Chinese rendering;
3. mark it as a translator note;
4. state what source would resolve it.

Do not invent an established Chinese name.
