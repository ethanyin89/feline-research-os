# HCM Source Index

## Seed Corpus

| ID | Title | Primary Layer | Evidence Level | Status |
|---|---|---|---|---|
| src-hcm-001 | The Feline Cardiomyopathies: 2. Hypertrophic cardiomyopathy | mechanism | review | deep-extracted round 1 |
| src-hcm-002 | Feline Hypertrophic Cardiomyopathy: An Update | mechanism | review | deep-extracted round 1 |
| src-hcm-003 | Feline Hypertrophic Cardiomyopathy: A Spontaneous Large Animal Model of Human HCM | model | review | deep-extracted round 1 |
| src-hcm-004 | Genetics of feline hypertrophic cardiomyopathy | mechanism | review | deep-extracted round 1 |
| src-hcm-005 | The Feline Cardiomyopathies: 3. Cardiomyopathies other than HCM | extension | review | deep-extracted round 1 |
| src-hcm-006 | Cardiac Troponin I in Feline Hypertrophic Cardiomyopathy | endpoint | original-study | deep-extracted round 1 |
| src-hcm-007 | The Feline Cardiomyopathies: 1. General concepts | review | review | deep-extracted round 1 |
| src-hcm-008 | Clinical-Diagnostic and Therapeutic Advances in Feline Hypertrophic Cardiomyopathy | translation | review | deep-extracted round 1 |
| src-hcm-009 | Echocardiographic Assessment of Spontaneously Occurring Feline Hypertrophic Cardiomyopathy: An Animal Model of Human Disease | endpoint | original-study | deep-extracted round 1 |
| src-hcm-010 | Investigation into the use of plasma NT-proBNP concentration to screen for feline hypertrophic cardiomyopathy | endpoint | original-study | deep-extracted round 1 |
| src-hcm-011 | A Small Molecule Inhibitor of Sarcomere Contractility Acutely Relieves Left Ventricular Outflow Tract Obstruction in Feline Hypertrophic Cardiomyopathy | translation | original-study | deep-extracted round 1 |
| src-hcm-012 | Influence of Clinical Aspects and Genetic Factors on Feline HCM Severity and Development | genetics | original-study | deep-extracted round 1 |
| src-hcm-013 | Diagnostic Value of Morphometry in Feline Hypertrophic Cardiomyopathy | diagnosis | original-study | deep-extracted round 1 |
| src-hcm-014 | The use of enalapril in the treatment of feline hypertrophic cardiomyopathy | translation | original-study | deep-extracted round 1 |
| src-hcm-015 | Is Treatment of Feline Hypertrophic Cardiomyopathy Based in Science or Faith?: A Survey of Cardiologists and a Literature Search | translation | review | deep-extracted round 1 |
| src-hcm-016 | Hypertrophic cardiomyopathy in man and cats | model | review | deep-extracted round 1 |
| src-hcm-017 | Evaluation of Potential Novel Biomarkers for Feline Hypertrophic Cardiomyopathy | frontier | original-study | deep-extracted round 1 |
| src-hcm-018 | Feline idiopathic cardiomyopathy: A retrospective study of 106 cats (1994-2001) | extension | case-series | deep-extracted round 1 |
| src-hcm-019 | Right ventricular involvement in feline hypertrophic cardiomyopathy | mechanism | original-study | deep-extracted round 1 |
| src-hcm-020 | Feline Hypertrophic Cardiomyopathy: The Consequence of Cardiomyocyte-Initiated and Macrophage-Driven Remodeling Processes? | mechanism | review | deep-extracted round 1 |
| src-hcm-021 | Feline Myocardial Disease: 1: Classification, Pathophysiology and Clinical Presentation | review | review | deep-extracted round 1 |
| src-hcm-022 | Exploration of Mediators Associated with Myocardial Remodelling in Feline Hypertrophic Cardiomyopathy | mechanism | original-study | deep-extracted round 1 |
| src-hcm-023 | Deep learning-based diagnosis of feline hypertrophic cardiomyopathy | diagnosis | original-study | deep-extracted round 1 |
| src-hcm-024 | Anatomopathological staging of feline hypertrophic cardiomyopathy through quantitative evaluation based on morphometric and histopathological data | diagnosis | original-study | deep-extracted round 1 |

## First-Pass Reading Priorities

### Tier A

- `src-hcm-001`
- `src-hcm-007`
- `src-hcm-004`
- `src-hcm-009`
- `src-hcm-008`
- `src-hcm-020`

### Tier B

- `src-hcm-006`
- `src-hcm-010`
- `src-hcm-012`
- `src-hcm-013`
- `src-hcm-015`
- `src-hcm-024`

## Notes

- `ingested` means a first source card now exists in `raw/papers/`
- `deep-extracted round 1` means a first worksheet now exists in `system/indexes/`
- all 24 HCM paper source cards are now explicit `extraction_depth: full` as of the 2026-04-22 source-depth pass
- the highest-value early compression problem is likely `phenotype recognition versus biomarker and genetics overcompression`

## Current Status Note

The first-pass HCM source-card layer is built across the current 24-source seed corpus, HCM deep extraction covers the full seed set, and the source-card depth layer is now 24/24 explicit full.

The next control layer now exists as:

- [HCM source depth map](hcm-source-depth-map.md)

That means the next gains should come from:

- full-text/output-specific precision where a real answer surface needs stronger support
- tighter phenotype-recognition and treatment-boundary compression
- better separation of genetics, biomarkers, and remodeling
- sharper separation of targeted therapy, conventional therapy, frontier biomarkers, and AI augmentation

## First-Wave Deep Extraction Outputs

- [src-hcm-001 deep extraction round 1](src-hcm-001-deep-extraction-round1.md)
- [src-hcm-007 deep extraction round 1](src-hcm-007-deep-extraction-round1.md)
- [src-hcm-004 deep extraction round 1](src-hcm-004-deep-extraction-round1.md)
- [src-hcm-009 deep extraction round 1](src-hcm-009-deep-extraction-round1.md)
- [src-hcm-008 deep extraction round 1](src-hcm-008-deep-extraction-round1.md)
- [src-hcm-020 deep extraction round 1](src-hcm-020-deep-extraction-round1.md)
- [src-hcm-006 deep extraction round 1](src-hcm-006-deep-extraction-round1.md)
- [src-hcm-010 deep extraction round 1](src-hcm-010-deep-extraction-round1.md)
- [src-hcm-012 deep extraction round 1](src-hcm-012-deep-extraction-round1.md)
- [src-hcm-013 deep extraction round 1](src-hcm-013-deep-extraction-round1.md)
- [src-hcm-015 deep extraction round 1](src-hcm-015-deep-extraction-round1.md)
- [src-hcm-024 deep extraction round 1](src-hcm-024-deep-extraction-round1.md)
- [src-hcm-011 deep extraction round 1](src-hcm-011-deep-extraction-round1.md)
- [src-hcm-014 deep extraction round 1](src-hcm-014-deep-extraction-round1.md)
- [src-hcm-017 deep extraction round 1](src-hcm-017-deep-extraction-round1.md)
- [src-hcm-023 deep extraction round 1](src-hcm-023-deep-extraction-round1.md)
- [src-hcm-019 deep extraction round 1](src-hcm-019-deep-extraction-round1.md)
- [src-hcm-021 deep extraction round 1](src-hcm-021-deep-extraction-round1.md)
- [src-hcm-022 deep extraction round 1](src-hcm-022-deep-extraction-round1.md)
- [src-hcm-002 deep extraction round 1](src-hcm-002-deep-extraction-round1.md)
- [src-hcm-003 deep extraction round 1](src-hcm-003-deep-extraction-round1.md)
- [src-hcm-005 deep extraction round 1](src-hcm-005-deep-extraction-round1.md)
- [src-hcm-016 deep extraction round 1](src-hcm-016-deep-extraction-round1.md)
- [src-hcm-018 deep extraction round 1](src-hcm-018-deep-extraction-round1.md)
