# IBD Source Index

## Seed Corpus

| ID | Title | Primary Layer | Evidence Level | Status |
|---|---|---|---|---|
| src-ibd-001 | Relationship of the mucosal microbiota to gastrointestinal inflammation and small cell intestinal lymphoma in cats | mechanism | original-study | deep-extracted |
| src-ibd-002 | Feline Epitheliotropic Intestinal Malignant Lymphoma: 10 Cases (1997-2000) | boundary | case-series | deep-extracted |
| src-ibd-003 | Feline inflammatory bowel disease | mechanism | review | deep-extracted |
| src-ibd-004 | A Clinical Index for Disease Activity in Cats with Chronic Enteropathy | endpoint | original-study | deep-extracted |
| src-ibd-005 | Prostaglandin E2 secreted from feline adipose tissue-derived mesenchymal stem cells alleviate DSS-induced colitis by increasing regulatory T cells in mice | translation | original-study | deep-extracted |
| src-ibd-006 | Molecular characterisation of the gut microflora of healthy and inflammatory bowel disease cats using fluorescence in situ hybridisation with special reference to Desulfovibrio spp. | mechanism | original-study | deep-extracted |
| src-ibd-007 | Pilot study: duodenal MDR1 and COX2 gene expression in cats with inflammatory bowel disease and low-grade alimentary lymphoma | boundary | original-study | deep-extracted |
| src-ibd-008 | Impact of Changes in Gastrointestinal Microbiota in Canine and Feline Digestive Diseases | mechanism | review | deep-extracted |
| src-ibd-009 | Identifying free-text features to improve automated classification of structured histopathology reports for feline small intestinal disease | diagnosis | original-study | deep-extracted |
| src-ibd-010 | Ultrasonographic Evaluation of the Muscularis Propria in Cats with Diffuse Small Intestinal Lymphoma or Inflammatory Bowel Disease | diagnosis | original-study | deep-extracted |
| src-ibd-011 | Cyclooxygenase-2 immunoexpression in intestinal epithelium and lamina propria of cats with inflammatory bowel disease and low grade alimentary lymphoma | boundary | original-study | deep-extracted |
| src-ibd-012 | Immunohistochemical Findings in Idiopathic Inflammatory Bowel Disease in Nine Cats | diagnosis | original-study | deep-extracted |
| src-ibd-013 | Cats with Inflammatory Bowel Disease and Intestinal Small Cell Lymphoma Have Low Serum Concentrations of 25-Hydroxyvitamin D | endpoint | original-study | deep-extracted |
| src-ibd-014 | Efficacy of a commercial hydrolysate diet in eight cats suffering from inflammatory bowel disease or adverse reaction to food | translation | original-study | deep-extracted |
| src-ibd-015 | Utility of Endoscopic Biopsies of the Duodenum and Ileum for Diagnosis of Inflammatory Bowel Disease and Small Cell Lymphoma in Cats | diagnosis | original-study | deep-extracted |
| src-ibd-016 | Expression of the Bcl-2 apoptotic marker in cats diagnosed with inflammatory bowel disease and gastrointestinal lymphoma | boundary | original-study | deep-extracted |
| src-ibd-017 | Fecal S100A12 concentrations in cats with chronic enteropathies | endpoint | original-study | deep-extracted |
| src-ibd-018 | Feline Gastrointestinal Eosinophilic Sclerosing Fibroplasia-Extracellular Matrix Proteins and TGF-beta1 Immunoexpression | extension | original-study | deep-extracted |
| src-ibd-019 | Untargeted metabolomic analysis in cats with naturally occurring inflammatory bowel disease and alimentary small cell lymphoma | frontier | original-study | deep-extracted |
| src-ibd-020 | Granulomatous colitis: more than a canine disease? A case of Escherichia coli-associated granulomatous colitis in an adult cat | extension | case-report | deep-extracted |
| src-ibd-021 | A Comprehensive Exploration of Therapeutic Strategies in Inflammatory Bowel Diseases: Insights from Human and Animal Studies | translation | review | deep-extracted |
| src-ibd-022 | Characterization of intestinal fibrosis in cats with chronic inflammatory enteropathy | mechanism | original-study | deep-extracted |
| src-ibd-023 | Feline cholangitis: A necropsy study of 44 cats (1986-2008) | extension | case-series | deep-extracted |
| src-ibd-024 | Feline chronische Enteropathien - ein stetiger Begleiter in der Kleintierpraxis | review | review | deep-extracted |

## First-Pass Reading Priorities

### Tier A

- `src-ibd-003`
- `src-ibd-004`
- `src-ibd-015`
- `src-ibd-001`
- `src-ibd-022`
- `src-ibd-010`

### Tier B

- `src-ibd-013`
- `src-ibd-017`
- `src-ibd-019`
- `src-ibd-006`
- `src-ibd-007`
- `src-ibd-011`
- `src-ibd-014`
- `src-ibd-024`

## Notes

- `ingested` means a first source card already exists in `raw/papers/`
- `deep-extracted` means a round-1 extraction worksheet now exists in `system/indexes/`
- deep extraction now covers the full 24-source seed corpus; the listed source cards should be read as a complete round-1 worksheet set, not as a partial startup batch
- the highest-value early compression problem is the `IBD versus small-cell lymphoma` boundary

## Current Status Note

The IBD source-card layer is now complete across the current 24-source seed corpus, deep extraction covers the full seed set, and all 24 paper cards are explicit `extraction_depth: full`.

That means the next gains should come from:

- full-text / image-table / regulatory precision where output or branch order requires it
- denser write-back into topic pages
- tighter diagnostic-boundary compression
- better endpoint and treatment separation

For card-level depth detail, use:

- [IBD source depth map](ibd-source-depth-map.md)
