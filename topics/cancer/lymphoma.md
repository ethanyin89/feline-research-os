---
id: topic-cancer-lymphoma
type: topic
topic: cancer
species: feline
disease: cancer
question_type: branch
source_ids: [src-cancer-004, src-cancer-008, src-cancer-063, src-cancer-065, src-cancer-068]
last_compiled_at: 2026-05-30
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: not_checked
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

### Modern Demographics (Abstract-Level)

`src-cancer-068` provides Australian lymphoma demographics (1705 cases vs 85,741 reference population):

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
