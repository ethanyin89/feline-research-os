---
id: cancer-source-check-full-20260530
type: system
topic: content-pipeline
question_type: source-check-report
language: zh
last_compiled_at: 2026-05-30
verification_status: generated
decision_grade: no
owner: codex
status: active
---

# Feline Source Metadata Check, 2026-05-30

Source set: `feline cancer full source metadata check after first-pass bootstrap, 2026-05-30`

## Rule

This report is a repeatable second-pass source check. It does not make clinical claims.

- DOI metadata alone does not upgrade a card.
- Abstract availability can justify `abstract_weighted` only for navigation and extraction priority.
- Full-text or structured worksheet review is still required before `source_checked` or `deep_extracted`.

## Summary

- Cards checked: `102`
- Crossref metadata found: `41`
- Abstract available: `27`

## Check Table

| Source | Current | Recommended | DOI | Year | Container | Abstract | Error |
|---|---|---|---|---:|---|---|---|
| `src-cancer-001` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-002` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-003` | `abstract_weighted` | `abstract_weighted` | `10.1002/vms3.460` | 2021 | Veterinary Medicine and Science | `yes` |  |
| `src-cancer-004` | `abstract_weighted` | `abstract_weighted` | `10.21926/obm.genet.2102131` | 2021 | OBM Genetics | `yes` |  |
| `src-cancer-005` | `abstract_weighted` | `abstract_weighted` | `10.3390/vetsci2030111` | 2015 | Veterinary Sciences | `yes` |  |
| `src-cancer-006` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-007` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-008` | `abstract_weighted` | `abstract_weighted` | `10.1177/104063870001200401` | 2000 | Journal of Veterinary Diagnostic Investigation | `yes` |  |
| `src-cancer-009` | `abstract_weighted` | `abstract_weighted` | `10.1177/1098612x20964416` | 2021 | Journal of Feline Medicine and Surgery | `yes` |  |
| `src-cancer-010` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-011` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-012` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-013` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-014` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-015` | `title_only` | `title_only` | `10.1136/vr.108.22.476` | 1981 | Veterinary Record | `no` |  |
| `src-cancer-016` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-017` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-018` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-019` | `title_only` | `abstract_weighted` | `10.1186/1471-2407-13-403` | 2013 | BMC Cancer | `yes` |  |
| `src-cancer-020` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-021` | `title_only` | `abstract_weighted` | `10.1155/2013/502197` | 2013 | Pathology Research International | `yes` |  |
| `src-cancer-022` | `title_only` | `title_only` | `10.1186/s12917-014-0185-8` | 2014 | BMC Veterinary Research | `no` |  |
| `src-cancer-023` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-024` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-025` | `title_only` | `abstract_weighted` | `10.1177/0300985814528221` | 2015 | Veterinary Pathology | `yes` |  |
| `src-cancer-026` | `title_only` | `abstract_weighted` | `10.1002/ijc.2910100216` | 1972 | International Journal of Cancer | `yes` |  |
| `src-cancer-027` | `title_only` | `title_only` | `10.1007/bf00255902` | 1984 | Cancer Chemotherapy and Pharmacology | `no` |  |
| `src-cancer-028` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-029` | `title_only` | `abstract_weighted` | `10.1177/030098587801500602` | 1978 | Veterinary Pathology | `yes` |  |
| `src-cancer-030` | `title_only` | `title_only` | `10.1007/978-3-030-30734-9_9` | 2020 | Pets as Sentinels, Forecasters and Promoters of Human Health | `no` |  |
| `src-cancer-031` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-032` | `title_only` | `title_only` | `10.1186/s12885-018-4323-8` | 2018 | BMC Cancer | `no` |  |
| `src-cancer-033` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-034` | `title_only` | `abstract_weighted` | `10.1354/vp.08-vp-0161-d-fl` | 2009 | Veterinary Pathology | `yes` |  |
| `src-cancer-035` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-036` | `title_only` | `title_only` | `10.1371/journal.pone.0221776` | 2019 | PLOS ONE | `no` |  |
| `src-cancer-037` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-038` | `title_only` | `title_only` | `10.1007/s10616-015-9912-7` | 2016 | Cytotechnology | `no` |  |
| `src-cancer-039` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-040` | `title_only` | `abstract_weighted` | `10.1177/1098612x13483235` | 2013 | Journal of Feline Medicine and Surgery | `yes` |  |
| `src-cancer-041` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-042` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-043` | `title_only` | `abstract_weighted` | `10.1177/1010428319901052` | 2020 | Tumor Biology | `yes` |  |
| `src-cancer-044` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-045` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-046` | `title_only` | `abstract_weighted` | `10.1177/089875641503200104` | 2015 | Journal of Veterinary Dentistry | `yes` |  |
| `src-cancer-047` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-048` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-049` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-050` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-051` | `title_only` | `abstract_weighted` | `10.1111/j.1476-5829.2010.00244.x` | 2011 | Veterinary and Comparative Oncology | `yes` |  |
| `src-cancer-052` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-053` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-054` | `title_only` | `title_only` | `10.1186/bcr790` | 2004 | Breast Cancer Research | `no` |  |
| `src-cancer-055` | `title_only` | `title_only` | `10.1089/humc.2017.008` | 2017 | Human Gene Therapy Clinical Development | `no` |  |
| `src-cancer-056` | `title_only` | `abstract_weighted` | `10.1186/s12885-019-6483-6` | 2019 | BMC Cancer | `yes` |  |
| `src-cancer-057` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-058` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-059` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-060` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-061` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-062` | `title_only` | `abstract_weighted` | `10.1155/2014/675172` | 2014 | Veterinary Medicine International | `yes` |  |
| `src-cancer-063` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-064` | `title_only` | `title_only` | `10.1111/j.1748-5827.2010.00915.x` | 2010 | Journal of Small Animal Practice | `no` |  |
| `src-cancer-065` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-066` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-067` | `title_only` | `title_only` | `10.1371/journal.pone.0104337` | 2014 | PLoS ONE | `no` |  |
| `src-cancer-068` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-069` | `title_only` | `abstract_weighted` | `10.1186/1471-2407-10-156` | 2010 | BMC Cancer | `yes` |  |
| `src-cancer-070` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-071` | `title_only` | `abstract_weighted` | `10.1089/mab.2017.0046` | 2017 | Monoclonal Antibodies in Immunodiagnosis &amp; Immunotherapy | `yes` |  |
| `src-cancer-072` | `title_only` | `abstract_weighted` | `10.1089/omi.2022.0114` | 2022 | OMICS: A Journal of Integrative Biology | `yes` |  |
| `src-cancer-073` | `title_only` | `abstract_weighted` | `10.1111/vco.12967` | 2024 | Veterinary and Comparative Oncology | `yes` |  |
| `src-cancer-074` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-075` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-076` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-077` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-078` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-079` | `title_only` | `title_only` | `10.1007/bf00410693` | 1981 | Journal of Cancer Research and Clinical Oncology | `no` |  |
| `src-cancer-080` | `title_only` | `abstract_weighted` | `10.1111/vco.12551` | 2020 | Veterinary and Comparative Oncology | `yes` |  |
| `src-cancer-081` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-082` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-083` | `title_only` | `abstract_weighted` | `10.1016/j.jfms.2010.01.004` | 2010 | Journal of Feline Medicine and Surgery | `yes` |  |
| `src-cancer-084` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-085` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-086` | `title_only` | `abstract_weighted` | `10.1002/ijc.2910210314` | 1978 | International Journal of Cancer | `yes` |  |
| `src-cancer-087` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-088` | `title_only` | `title_only` | `10.1186/s12885-018-4650-9` | 2018 | BMC Cancer | `no` |  |
| `src-cancer-089` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-090` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-091` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-092` | `title_only` | `abstract_weighted` | `10.1186/s12917-021-03030-5` | 2021 | BMC Veterinary Research | `yes` |  |
| `src-cancer-093` | `title_only` | `abstract_weighted` | `10.1371/journal.pone.0330520` | 2025 | PLOS One | `yes` |  |
| `src-cancer-094` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-095` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-096` | `title_only` | `title_only` | `10.3109/07357909209024796` | 1992 | Cancer Investigation | `no` |  |
| `src-cancer-097` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-098` | `title_only` | `abstract_weighted` | `10.3390/vetsci8080164` | 2021 | Veterinary Sciences | `yes` |  |
| `src-cancer-099` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-100` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-101` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |
| `src-cancer-102` | `title_only` | `title_only` |  |  |  | `no` | no DOI in source card |

## Abstract Availability Notes

### `src-cancer-001`

- Metadata check failed: no DOI in source card

### `src-cancer-002`

- Metadata check failed: no DOI in source card

### `src-cancer-003`

- Crossref title: The role of COX expression in the prognostication of overall survival of canine and feline cancer: A systematic review
- Abstract lead for scope check only: Abstract Cyclooxygenase (COX) isoforms‐1 and ‐2 have been extensively investigated in cancer. Although COX‐2 is the isoform most studied and has been described in several malignan...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-004`

- Crossref title: Molecular Mechanisms of Feline Cancers
- Abstract lead for scope check only: Feline cancers have not been studied as extensively as canine cancers, though they may offer similar advantages, with cats being immunocompetent animals subject to similar conditi...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-005`

- Crossref title: Cats, Cancer and Comparative Oncology
- Abstract lead for scope check only: Naturally occurring tumors in dogs are well-established models for several human cancers. Domestic cats share many of the benefits of dogs as a model (spontaneous cancers developi...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-006`

- Metadata check failed: no DOI in source card

### `src-cancer-007`

- Metadata check failed: no DOI in source card

### `src-cancer-008`

- Crossref title: The Histologic Classification of 602 Cases of Feline Lymphoproliferative Disease using the National Cancer Institute Working Formulation
- Abstract lead for scope check only: Case information and histologic slides for 688 admissions of feline tissues from 12 veterinary institutions were assembled and reviewed to determine tissues obtained by biopsy or...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-009`

- Crossref title: Metastatic feline mammary cancer: prognostic factors, outcome and comparison of different treatment modalities – a retrospective multicentre study
- Abstract lead for scope check only: Objectives Although feline mammary carcinomas (FMCs) are highly metastatic, the literature and treatment options pertaining to advanced tumours are scarce. This study aimed to inv...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-010`

- Metadata check failed: no DOI in source card

### `src-cancer-011`

- Metadata check failed: no DOI in source card

### `src-cancer-012`

- Metadata check failed: no DOI in source card

### `src-cancer-013`

- Metadata check failed: no DOI in source card

### `src-cancer-014`

- Metadata check failed: no DOI in source card

### `src-cancer-015`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-cancer-016`

- Metadata check failed: no DOI in source card

### `src-cancer-017`

- Metadata check failed: no DOI in source card

### `src-cancer-018`

- Metadata check failed: no DOI in source card

### `src-cancer-019`

- Crossref title: Feline mammary basal-like adenocarcinomas: a potential model for human triple-negative breast cancer (TNBC) with basal-like subtype
- Abstract lead for scope check only: Abstract Background Breast cancer is one of the leading causes of cancer deaths. Triple-negative breast cancer (TNBC), an immunophenotype defined by the absence of immunolabeling...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-020`

- Metadata check failed: no DOI in source card

### `src-cancer-021`

- Crossref title: A Naturally Occurring Feline Model of Head and Neck Squamous Cell Carcinoma
- Abstract lead for scope check only: Despite advances in understanding cancer at the molecular level, timely and effective translation to clinical application of novel therapeutics in human cancer patients is lacking...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-022`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-cancer-023`

- Metadata check failed: no DOI in source card

### `src-cancer-024`

- Metadata check failed: no DOI in source card

### `src-cancer-025`

- Crossref title: Prognostic Evaluation of Feline Mammary Carcinomas
- Abstract lead for scope check only: A large number of studies have investigated feline mammary tumors in an attempt to identify prognostic markers and generate comparative analyses with human breast cancer. Neverthe...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-026`

- Crossref title: Feline malignant lymphoma: Environmental factors and the occurrence of this viral cancer in cats
- Abstract lead for scope check only: Abstract Environmental data collected on 221 feline malignant lymphoma cases and age‐, sex‐ and breed‐matched controls were analyzed to find evidence which could prove or disprove...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-027`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-cancer-028`

- Metadata check failed: no DOI in source card

### `src-cancer-029`

- Crossref title: Frequency of Canine and Feline Tumors in a Defined Population
- Abstract lead for scope check only: The Tulsa Registry of Canine and Feline Neoplasms was the second animal tumor registry in the United States concerned with a defined population in a delimited geographic area. Onl...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-030`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-cancer-031`

- Metadata check failed: no DOI in source card

### `src-cancer-032`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-cancer-033`

- Metadata check failed: no DOI in source card

### `src-cancer-034`

- Crossref title: Molecular Characterization of Feline COX-2 and Expression in Feline Mammary Carcinomas
- Abstract lead for scope check only: Cyclooxygenase-2 (COX-2), the rate-limiting enzyme in the biosynthesis of prostaglandins, plays an important role in inflammation and tumorigenesis. COX-2 primary structure has be...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-035`

- Metadata check failed: no DOI in source card

### `src-cancer-036`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-cancer-037`

- Metadata check failed: no DOI in source card

### `src-cancer-038`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-cancer-039`

- Metadata check failed: no DOI in source card

### `src-cancer-040`

- Crossref title: Cats with Cancer
- Abstract lead for scope check only: Practical relevance: Many cats develop cancer and may or may not present with an obvious mass lesion. As our feline patients are living longer and their owners are increasingly se...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-041`

- Metadata check failed: no DOI in source card

### `src-cancer-042`

- Metadata check failed: no DOI in source card

### `src-cancer-043`

- Crossref title: Identification of an immune-suppressed subtype of feline triple-negative basal-like invasive mammary carcinomas, spontaneous models of breast cancer
- Abstract lead for scope check only: Feline invasive mammary carcinomas are characterized by their high clinical aggressiveness, rare expression of hormone receptors, and pathological resemblance to human breast canc...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-044`

- Metadata check failed: no DOI in source card

### `src-cancer-045`

- Metadata check failed: no DOI in source card

### `src-cancer-046`

- Crossref title: Feline Oral Squamous Cell Carcinoma: Clinical Manifestations and Literature Review
- Abstract lead for scope check only: Squamous cell carcinoma (SCC) is the most commonly encountered malignant oral tumor in cats. The etiology of this locally invasive tumor is likely multifactorial. Several risk fac...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-047`

- Metadata check failed: no DOI in source card

### `src-cancer-048`

- Metadata check failed: no DOI in source card

### `src-cancer-049`

- Metadata check failed: no DOI in source card

### `src-cancer-050`

- Metadata check failed: no DOI in source card

### `src-cancer-051`

- Crossref title: Development of a questionnaire assessing health‐related quality‐of‐life in dogs and cats with cancer
- Abstract lead for scope check only: Health‐related quality‐of‐life (HRQoL) has been studied extensively in human medicine. There is currently no standard HRQoL evaluation for veterinary oncology patients. The aim of...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-052`

- Metadata check failed: no DOI in source card

### `src-cancer-053`

- Metadata check failed: no DOI in source card

### `src-cancer-054`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-cancer-055`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-cancer-056`

- Crossref title: Androgen receptor and FOXA1 coexpression define a “luminal-AR” subtype of feline mammary carcinomas, spontaneous models of breast cancer
- Abstract lead for scope check only: Abstract Background Invasive mammary carcinomas that spontaneously develop in female cats are associated with high mortality, and resemble the most aggressive human breast cancers...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-057`

- Metadata check failed: no DOI in source card

### `src-cancer-058`

- Metadata check failed: no DOI in source card

### `src-cancer-059`

- Metadata check failed: no DOI in source card

### `src-cancer-060`

- Metadata check failed: no DOI in source card

### `src-cancer-061`

- Metadata check failed: no DOI in source card

### `src-cancer-062`

- Crossref title: Pamidronate Disodium for Palliative Therapy of Feline Bone-Invasive Tumors
- Abstract lead for scope check only: This study sought to quantify in vitro antiproliferative effects of pamidronate in feline cancer cells and assess feasibility of use of pamidronate in cats by assessing short-term...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-063`

- Metadata check failed: no DOI in source card

### `src-cancer-064`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-cancer-065`

- Metadata check failed: no DOI in source card

### `src-cancer-066`

- Metadata check failed: no DOI in source card

### `src-cancer-067`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-cancer-068`

- Metadata check failed: no DOI in source card

### `src-cancer-069`

- Crossref title: Spontaneous feline mammary intraepithelial lesions as a model for human estrogen receptor- and progesterone receptor-negative breast lesions
- Abstract lead for scope check only: Abstract Background Breast cancer is the most frequently diagnosed cancer in women. Intraepithelial lesions (IELs), such as usual ductal hyperplasia (UH), atypical ductal hyperpla...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-070`

- Metadata check failed: no DOI in source card

### `src-cancer-071`

- Crossref title: Expression of Cat Podoplanin in Feline Squamous Cell Carcinomas
- Abstract lead for scope check only: Oral squamous cell carcinoma is an aggressive tumor in cats; however, molecular-targeted therapies against this tumor, including antibody therapy, have not been developed. Sensiti...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-072`

- Crossref title: Satellite Noncoding RNAs (ncRNA) as Cancer Biomarkers? New Insights from                     <i>FA-SAT</i>                     ncRNA Molecular and Clinical Profiles in Feline Mammary Tumors
- Abstract lead for scope check only: Satellite noncoding RNAs (ncRNAs) are a new frontier of cancer biology research and biomarkers. While the knowledge on ncRNAs in human cancers is still limited, studies in other s...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-073`

- Crossref title: Expression of <scp>mPGES1</scp> and p16 in feline and human oral squamous cell carcinoma: A comparative oncology approach
- Abstract lead for scope check only: Abstract Comparative cancer studies help us determine if discoveries in one species apply to another. Feline and human oral squamous cell carcinoma (FOSCC and HOSCC) are invasive...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-074`

- Metadata check failed: no DOI in source card

### `src-cancer-075`

- Metadata check failed: no DOI in source card

### `src-cancer-076`

- Metadata check failed: no DOI in source card

### `src-cancer-077`

- Metadata check failed: no DOI in source card

### `src-cancer-078`

- Metadata check failed: no DOI in source card

### `src-cancer-079`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-cancer-080`

- Crossref title: A novel MCT1 and MCT4 dual inhibitor reduces mitochondrial metabolism and inhibits tumour growth of feline oral squamous cell carcinoma
- Abstract lead for scope check only: Abstract Monocarboxylate transporters (MCTs) support tumour growth by regulating the transport of metabolites in the tumour microenvironment. High MCT1 or MCT4 expression is corre...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-081`

- Metadata check failed: no DOI in source card

### `src-cancer-082`

- Metadata check failed: no DOI in source card

### `src-cancer-083`

- Crossref title: Early Detection, Aggressive Therapy
- Abstract lead for scope check only: Aims This article reviews the incidence, etiology, diagnosis, treatment and prognosis of mammary tumors in cats. Practical relevance Approximately 80% of feline mammary masses are...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-084`

- Metadata check failed: no DOI in source card

### `src-cancer-085`

- Metadata check failed: no DOI in source card

### `src-cancer-086`

- Crossref title: The frequency of occurrence of feline leukaemia virus subgroups in cats
- Abstract lead for scope check only: Abstract Feline leukaemia viruses (FeLV) were isolated from cats in Glasgow and New York with lympho‐sarcoma and from apparently healthy carrier cats. The subgroup composition of...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-087`

- Metadata check failed: no DOI in source card

### `src-cancer-088`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-cancer-089`

- Metadata check failed: no DOI in source card

### `src-cancer-090`

- Metadata check failed: no DOI in source card

### `src-cancer-091`

- Metadata check failed: no DOI in source card

### `src-cancer-092`

- Crossref title: Feline thymidine kinase 1: molecular characterization and evaluation of its serum form as a diagnostic biomarker
- Abstract lead for scope check only: Abstract Background Thymidine kinase 1 (TK1) catalyzes the initial phosphorylation of thymidine in the salvage pathway synthesis of dTTP, an essential building block of DNA. TK1 i...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-093`

- Crossref title: Phosphoproteomic profiling of feline mammary carcinoma: Insights into tumor grading and potential therapeutic targets
- Abstract lead for scope check only: Feline mammary carcinoma (FMC) is the most prevalent reproductive tumor in queens and is characterized by aggressive metastatic progression and short survival. Protein phosphoryla...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-094`

- Metadata check failed: no DOI in source card

### `src-cancer-095`

- Metadata check failed: no DOI in source card

### `src-cancer-096`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-cancer-097`

- Metadata check failed: no DOI in source card

### `src-cancer-098`

- Crossref title: Emerging Biomarkers and Targeted Therapies in Feline Mammary Carcinoma
- Abstract lead for scope check only: Feline mammary carcinoma (FMC) is a common aggressive malignancy with a low survival rate that lacks viable therapeutic options beyond mastectomy. Recently, increasing efforts hav...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-cancer-099`

- Metadata check failed: no DOI in source card

### `src-cancer-100`

- Metadata check failed: no DOI in source card

### `src-cancer-101`

- Metadata check failed: no DOI in source card

### `src-cancer-102`

- Metadata check failed: no DOI in source card
