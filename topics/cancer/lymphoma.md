---
id: topic-cancer-lymphoma
type: topic
topic: cancer
species: feline
disease: cancer
question_type: branch
source_ids: [src-cancer-004, src-cancer-008, src-cancer-063, src-cancer-065, src-cancer-068, src-cancer-048, src-cancer-075, src-cancer-029, src-cancer-018, src-cancer-026, src-cancer-042, src-cancer-044, src-cancer-060, src-cancer-084, src-cancer-086, src-cancer-102]
last_compiled_at: 2026-06-03
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline Lymphoma

## Key-Claim Traceability

| ID | Claim | Level | Source IDs | Boundary |
|---|---|---|---|---|
| LY1 | Lymphoma should be an early split-out cancer branch | B | src-cancer-004, src-cancer-008 | branch architecture, not prevalence ranking |
| LY2 | Lymphoma architecture should separate pathology/grade from anatomic topography | B | src-cancer-008 | classification frame, not treatment guidance |
| LY3 | Alimentary lymphoma deserves a future sub-branch; LGAL is the most prevalent subtype | B | src-cancer-004, src-cancer-008, src-cancer-063 | sub-branch signal with modern molecular context |
| LY4 | FeLV-associated lymphoma decreased after testing/vaccination, but overall lymphoma incidence increased due to intestinal lymphoma rise | B | src-cancer-065 | FeLV-shift context, 1983-2003 retrospective |
| LY5 | Lymphoma is the most common haematopoietic cancer in cats | B | src-cancer-068 | abstract-level claim, Australian population |
| LY6 | Male cats have increased lymphoma risk (OR 1.2) | B | src-cancer-068 | Australian population, abstract-level |
| LY7 | Median age at lymphoma diagnosis is 11.7 years | B | src-cancer-068 | Australian population, abstract-level |
| LY8 | Breed-specific anatomic presentation patterns exist | B | src-cancer-068 | Siamese, Burmilla, Australian mist, ragdoll, British shorthair noted |
| LY9 | JAK/STAT signaling pathway is implicated in feline alimentary lymphoma | B | src-cancer-063 | molecular context, homology with human GI T-cell lymphoma |
| LY10 | Siamese and Oriental breeds show high incidence of mediastinal lymphoma in young cats | B | src-cancer-065 | breed-specific pattern, UC Davis 21-year retrospective |
| LY11 | GI lymphoma presents as anorexia and weight loss ± vomiting/diarrhea in older cats | B | src-cancer-048 | clinical presentation |
| LY12 | Most GI lymphoma cats are FeLV-negative and FIV-negative | B | src-cancer-048 | post-FeLV era context |
| LY13 | Low-grade GI lymphoma may be more common than previously thought | B | src-cancer-048 | 2003 perspective |
| LY14 | Low-grade responds better to chemotherapy than high-grade | B | src-cancer-048 | treatment-relevant |
| LY15 | Initial response to chemotherapy is the most significant prognostic indicator | B | src-cancer-048 | strongest predictor |
| LY16 | FIV accounts for some non-FeLV lymphoma cases via distinct transformation mechanism | B | src-cancer-075 | 2014 review |
| LY17 | More viral aetiologies beyond FeLV/FIV may exist | B | src-cancer-075 | research direction |
| LY18 | Lymphosarcoma was most common tumor in cats in 1978 Tulsa Registry | B | src-cancer-029 | defined-population registry |
| LY19 | Feline lymphoma offers unique viral transformation research opportunities | B | src-cancer-018 | cytogenomics review, FeLV context |
| LY20 | Chromosomal aberrations in feline lymphomas studied as model system | B | src-cancer-018 | genomic microarray applications |
| LY21 | Early epidemiological study analyzed 221 lymphoma cases with matched controls | B | src-cancer-026 | 1972 environmental factors study |
| LY22 | FeLV confirmed infectious via seroepidemiological study of 2000+ cats | B | src-cancer-042 | 1976 foundational FeLV research |
| LY23 | Test-and-removal program controlled FeLV spread; 12% infection when FeLV+ remained | B | src-cancer-042 | eradication strategy basis |
| LY24 | Experimental FeLV susceptibility decreased with age after inoculation | B | src-cancer-044 | historical SPF-cat experimental infection |
| LY25 | FeLV-R predominantly induced thymic lymphosarcoma, while FeLV-KT caused fatal nonregenerative anemia without concurrent neoplasia | B | src-cancer-044 | strain-specific historical finding |
| LY26 | In a 1972-1976 Boston leukemia/lymphoma cohort, 67% of cases were FeLV virus-positive by fluorescent antibody testing | B | src-cancer-060 | historical cohort, not modern prevalence |
| LY27 | Virus-negative leukemia/lymphoma cases skewed older than virus-positive cases in that historical cohort | B | src-cancer-060 | age-at-diagnosis caveat |
| LY28 | Age-dependent FeLV susceptibility: kittens 71% viremic by 7mo (latent 3.4mo) vs adults 11% (latent 13mo) | B | src-cancer-084 | 1980 natural infection study |
| LY29 | FeLV-AB subgroup in 58% of lymphosarcoma cats vs 33% healthy carriers | B | src-cancer-086 | subgroup-disease association |
| LY30 | FeLV-C rare and found only in diseased cats, not healthy carriers | B | src-cancer-086 | FeLV-C pathogenicity signal |
| LY31 | Horizontal transmission requires viremic (gsa+) source: 85% infection from gsa+ vs 0% from gsa- cats | B | src-cancer-102 | 1977 experimental transmission |

## Evidence-Depth Caveat

This page combines two deep-extracted sources with two abstract-weighted sources. `src-cancer-004` and `src-cancer-008` provide branch architecture. `src-cancer-063` and `src-cancer-068` add modern molecular and demographic context at abstract level. Full-text deep extraction of the newer sources is recommended before treatment or prognosis claims.

## Core Takeaway

Feline lymphoma should not be one undifferentiated cancer paragraph. The current safe architecture has three axes:

- pathology / grade
- anatomic topography
- viral and historical context

Treatment and prognosis should remain gated until newer lymphoma-specific clinical sources are deep-extracted.

## Branch Architecture

### Pathology And Grade

`src-cancer-008` analyzed 602 feline lymphoproliferative disease cases using the National Cancer Institute Working Formulation.

Study-bound counts:

- low-grade: 69 cases
- intermediate-grade: 210 cases
- high-grade: 323 cases

**Boundary:** these are historical pathology-series counts, not modern prevalence or prognosis estimates.

### Topography

`src-cancer-008` supports separating histologic diagnosis from tumor topography. The study found correlations among diagnosis, topography, mitotic frequency, necrosis, sclerosis, and age.

**Current safe split candidates:**

- alimentary lymphoma
- mediastinal lymphoma
- multicentric lymphoma
- renal lymphoma
- cutaneous lymphoma

**Boundary:** site patterns should not become treatment recommendations without clinical outcome sources.

### Alimentary Lymphoma Signal

The pathology source gives alimentary lymphoma an early branch signal and suggests lower-grade / lower-mitotic patterns were more common in alimentary cases than in some other sites.

`src-cancer-063` (abstract-level) confirms that alimentary lymphoma has emerged as one of the most common feline malignancies. Low-grade alimentary lymphoma (LGAL) is identified as the most prevalent subtype.

**Molecular context (abstract-level):**

- JAK/STAT signaling pathway is implicated
- Substantial molecular homology with human gastrointestinal T-cell lymphoma
- Inflammatory-neoplastic continuum between chronic inflammatory enteropathies and lymphoma
- Molecular landscape remains poorly characterized; multi-omics studies are lacking

**Diagnostic ambiguity:** The review highlights diagnostic challenges distinguishing chronic inflammatory enteropathies from early lymphoma. This IBD-lymphoma continuum needs explicit handling in reader-facing content.

**Boundary:** do not infer that surgery, chemotherapy, or watchful waiting is appropriate from these sources. The JAK/STAT pathway mention is molecular context, not treatment recommendation.

### Modern Demographics (Deep-Extracted)

`src-cancer-068` provides Australian lymphoma demographics (1705 cases vs 85,741 reference population). [Deep extraction worksheet](../../system/indexes/src-cancer-068-deep-extraction-round1.md).

**Signalment findings:**

- Male cats at increased risk (OR 1.2, 95% CI: 1.1-1.3, p=0.002)
- Median age at diagnosis: 11.7 years (vs 9.0 years in reference)
- Lymphoma cases weighed less: median 3.7 kg vs 4.0 kg (p=0.010)

**Breed risk:**

- 8 breeds identified with increased potential risk
- 3 breeds identified with decreased risk
- Specific breeds not extractable from abstract; full-text needed

**Anatomic presentation patterns:**

- Significant breed variations in anatomical presentations
- Breeds noted: Siamese, Burmilla, Australian mist, ragdoll, British shorthair, domestic cats

**Boundary:** These findings are from Australian population with potentially restricted genetic pool. Breed risk claims need population boundary caveats.

### GI Lymphoma Clinical Context (Abstract-Level)

`src-cancer-048` (2003 clinical review) provides foundational GI lymphoma guidance:

**Presentation:**

- Common cause of anorexia and weight loss in older cats
- With or without vomiting or diarrhea
- Most cats are FeLV-negative and FIV-negative

**Grade and prognosis:**

- Low-grade GI lymphoma may be more common than previously thought (2003)
- Low-grade responds better to chemotherapy than high-grade
- Most significant prognostic indicator: initial response to chemotherapy
- Cats surviving initial induction generally achieve long-term remission
- Molecular markers and immunophenotyping had not identified useful prognostic indicators as of 2003

**Boundary:** This is a 2003 review. Molecular marker statements may be outdated; `src-cancer-063` provides 2026 molecular context.

### FeLV Context and the GI-Shift

`src-cancer-065` (abstract-level) provides the definitive FeLV-shift documentation from a 21-year UC Davis retrospective (1983-2003):

**Key historical pattern:**

- Mass FeLV testing, elimination/quarantine programs (1970s) and vaccination (1980s) reduced FeLV infection
- FeLV-associated lymphoma types significantly decreased
- But overall lymphoma incidence INCREASED from 1982 to 2003
- The increase was driven by intestinal lymphoma rise
- Atypical lymphoma also increased to a lesser degree

This explains why lymphoma remains common despite FeLV control: the disease shifted from viral-associated to alimentary forms.

**Breed-specific pattern:**

- Siamese and Oriental breeds show high mediastinal lymphoma incidence in young cats
- This pattern persisted through the post-FeLV era

**IBD connection:**

The 2005 study flagged IBD and diet associations for further investigation. This aligns with `src-cancer-063`'s discussion of the inflammatory-neoplastic continuum.

**Boundary:** The FeLV-shift is documented historically. Modern FeLV risk guidance needs separate, current sources. Diet recommendations are not supported by these abstracts.

### Age-Dependent FeLV Susceptibility (Abstract-Level)

`src-cancer-044` (1976 JNCI) experimentally inoculated 67 specific-pathogen-free cats at different ages with Rickard or Kawakami-Theilen FeLV strains.

**Persistent viremia / FeLV-related disease by age:**

| Age at inoculation | Abstract-Reported Outcome |
|--------------------|---------------------------|
| Newborn | 100% |
| 2 weeks to 2 months | 85% |
| 4 months or 1 year | 15% |

**Immune-response pattern:**

- Cats susceptible to FeLV leukemogenesis became persistently FeLV gsa-positive by 4 weeks post-inoculation and produced little or no FOCMA or virus-neutralizing antibody.
- Cats resisting FeLV leukemogenesis developed persistent FOCMA and virus-neutralizing titers and did not become FeLV gsa-positive.

**Strain-specific outcome:**

- FeLV-R induced predominantly thymic lymphosarcoma.
- FeLV-KT caused fatal nonregenerative anemia without concurrent neoplasia.

**Boundary:** This is historical experimental-infection evidence. It should contextualize FeLV biology, not act as modern vaccination, testing, or exposure-management guidance.

### Virus-Positive vs Virus-Negative Historical Cohort (Abstract-Level)

`src-cancer-060` compared 184 feline leukemia and lymphoma cases diagnosed in Boston from 1972 through 1976.

Study-bound findings:

- 58% of cases were lymphoma and 42% were leukemia.
- 67% of cats had positive fluorescent antibody tests for circulating FeLV; 33% were virus-negative.
- Virus-positive and virus-negative cases were clinically and epidemiologically similar except for age at diagnosis.
- Virus-negative cats were older on average at diagnosis (4.9 years) than virus-positive cats (3.5 years).
- Among 22 cases diagnosed after age 8 years, 15 were virus-negative.

**Boundary:** This is a historical leukemia/lymphoma cohort from one setting. It is useful for FeLV-era interpretation, not contemporary lymphoma prevalence or owner-facing FeLV risk estimates.

### Beyond FeLV: Other Viral Causes (Abstract-Level)

`src-cancer-075` (2014 review) explains why lymphoma prevalence remains high despite FeLV vaccination success:

**Key points:**

- FeLV vaccination has reduced FeLV prevalence globally
- FeLV-related cancers have decreased accordingly
- BUT: feline lymphoma prevalence remains high despite this
- FIV (feline immunodeficiency virus) accounts for some non-FeLV cases
- FIV transformation mechanism is distinct from FeLV, incompletely understood
- More viral aetiologies may be waiting to be discovered

**Implication:** The "GI-shift" (increased alimentary lymphoma despite FeLV decline) may involve multiple factors including FIV and possibly unknown viruses, not just dietary or environmental causes.

**Boundary:** FIV-associated lymphoma mechanisms remain incompletely characterized as of 2014.

### FeLV Subgroups And Disease Association (Abstract-Level)

`src-cancer-086` (1978 Int J Cancer) compared FeLV subgroup distribution between lymphosarcoma cats and healthy carriers:

**Subgroup frequencies:**

| Population | FeLV-A only | FeLV-AB | FeLV-C present |
|------------|-------------|---------|----------------|
| Lymphosarcoma cats | 42% | 58% | Rare |
| Healthy carriers | 67% | 33% | Not found |

**Key finding:** FeLV-AB subgroup is more common in lymphosarcoma cats than healthy carriers. FeLV-C appears only in diseased cats.

**Boundary:** This supports subgroup-pathogenicity research but does not inform FeLV testing interpretation for owners.

### FeLV Horizontal Transmission Requirements (Abstract-Level)

`src-cancer-102` (1977 J Natl Cancer Inst) experimentally demonstrated FeLV transmission conditions:

**Protocol:**
- 37 SPF cats inoculated with Rickard strain FeLV
- Each inoculated cat shared cage with control SPF cat for 40 weeks

**Results:**

| Source cat status | Contact infection rate |
|-------------------|------------------------|
| gsa-positive (viremic) | 85% (17/20) |
| gsa-negative (non-viremic) | 0% (0/17) |

**Key finding:** Horizontal FeLV transmission requires viremic source cat; non-viremic antibody-positive cats do not transmit.

**Boundary:** This is foundational experimental evidence. It supports FeLV testing rationale but does not replace modern test-and-isolate protocols.

### Age-Dependent FeLV Susceptibility (Abstract-Level)

`src-cancer-084` (1980 Leukemia Research) followed natural FeLV infection in a multi-cat household:

**Age-stratified outcomes:**

| Age group | Viremia rate | Latent period |
|-----------|--------------|---------------|
| Kittens | 71% by 7 months | 3.4 months |
| Adults | 11% | 13 months |

**Key finding:** Kittens are markedly more susceptible to persistent FeLV infection than adults.

**Boundary:** This informs vaccination timing rationale but does not provide modern vaccination schedules.

## What The Module Can Say Safely

- Lymphoma deserves an early cancer branch.
- Lymphoma is the most common haematopoietic cancer in cats.
- Pathology/grade and topography should be separated.
- Alimentary lymphoma is a high-priority sub-branch; LGAL is most prevalent.
- Male cats and older cats show increased lymphoma risk.
- Breed-specific patterns exist for anatomic presentation.
- JAK/STAT pathway involvement provides comparative oncology context.
- FeLV context matters, but historical sources have major missingness.

## What The Module Should Not Say Yet

- Do not rank lymphoma treatments.
- Do not provide survival ranges.
- Do not make modern FeLV risk claims.
- Do not claim modern immunophenotype classification is resolved.
- Do not recommend surgery for alimentary lymphoma from these sources.
- Do not name specific high-risk breeds until full-text extraction confirms the list.
- Do not recommend JAK/STAT-targeted therapy from abstract-level molecular context.
- Do not conflate IBD with lymphoma; maintain diagnostic uncertainty framing.

## Current Role

Use this page as the lymphoma branch shell. The page now includes abstract-level modern demographics and molecular context. Next gains require:

1. Full-text deep extraction of `src-cancer-063` for molecular details
2. Full-text deep extraction of `src-cancer-068` for breed-specific risk tables
3. Modern clinical sources for treatment and prognosis guidance
