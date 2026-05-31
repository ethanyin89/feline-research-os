---
id: cancer-branch-control-candidates
type: system
topic: cancer
question_type: extraction-queue
language: bilingual
last_compiled_at: 2026-05-30
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# Cancer Branch Control Candidates

This page maps the 5 open synthesis questions from `synthesis-index.md` to candidate sources that could provide branch-control evidence.

## Open Synthesis Questions

From the synthesis index:

1. Which lymphoma source should control lymphoproliferative classification and FeLV/GI-shift claims?
2. Which oral SCC source should control clinical manifestations and local disease behavior?
3. Which sarcoma/FISS source should control injection-site versus spontaneous sarcoma boundaries?
4. Which FISS-specific source should verify injection-site sarcoma time-trend and causality boundaries?
5. Which treatment outcome sources are strong enough to move beyond workflow-level treatment modality descriptions?

## Candidate Mapping

### Q1: Lymphoma / FeLV / GI-Shift Control

| Source | Title | Current Status | Claim-Fit | Access |
|---|---|---|---|---|
| `src-cancer-008` | Histologic Classification of 602 Cases of Feline Lymphoproliferative Disease | **deep_extracted** (anchor) | pathology classification, grade, topography | ✅ extracted |
| `src-cancer-063` | Feline Alimentary Lymphomas: Established Concepts and Underexplored Molecular Landscape | **abstract_weighted** | alimentary lymphoma molecular, LGAL, JAK/STAT | ✅ PubMed abstract |
| `src-cancer-065` | Feline Lymphoma in the Post—Feline Leukemia Virus Era | **abstract_weighted** | FeLV decline, intestinal lymphoma rise, Siamese mediastinal | ✅ PubMed abstract |
| `src-cancer-068` | Demographics of Feline Lymphoma in Australian Cat Populations: 1705 Cases | **abstract_weighted** | modern demographics, breed risk, anatomic patterns | ✅ PubMed abstract |
| `src-cancer-048` | Feline gastrointestinal lymphoma | title_only | GI lymphoma specifics | ScienceDirect |
| `src-cancer-026` | Feline malignant lymphoma: Environmental factors (1972) | abstract_weighted | historical FeLV context | 1972 paper - historical only |

**Current answer**: `src-cancer-008` provides pathology classification. For FeLV/GI-shift claims, need modern source like `src-cancer-063` or `src-cancer-065`.

**Next extraction priority**: `src-cancer-063` now has abstract-level extraction (LGAL most prevalent, JAK/STAT pathway, IBD-lymphoma continuum). Full-text deep extraction recommended for molecular details.

---

### Q2: Oral SCC Clinical Manifestations

| Source | Title | Current Status | Claim-Fit | Access |
|---|---|---|---|---|
| `src-cancer-046` | Feline Oral Squamous Cell Carcinoma: Clinical Manifestations and Literature Review (2015) | abstract_weighted | clinical manifestations review | **full-text blocked** (SAGE paywall) |
| `src-cancer-095` | Feline Oral Squamous Cell Carcinoma: A Critical Review of Etiologic Factors | **abstract_weighted** | etiologic factors: papillomavirus, tobacco, diet | ✅ PubMed abstract |
| `src-cancer-021` | A Naturally Occurring Feline Model of Head and Neck SCC | abstract_weighted | comparative oncology model | **Cloudflare blocked** |
| `src-cancer-073` | Expression of mPGES1 and p16 in feline and human oral SCC | abstract_weighted | marker expression | comparative oncology angle |
| `src-cancer-080` | MCT1/MCT4 dual inhibitor in feline oral SCC | abstract_weighted | therapy mechanism | treatment target paper |
| `src-cancer-071` | Expression of Cat Podoplanin in Feline SCCs | abstract_weighted | marker development | biomarker paper |

**Current answer**: No deep-extracted oral SCC source yet. `src-cancer-046` is the ideal clinical review but full-text is blocked.

**Next extraction priority**: `src-cancer-095` now has abstract-level extraction (papillomavirus 16.2%, tobacco exposure 35.2%, canned food 4.7x risk). Full-text deep extraction recommended for study quality and forest plots.

---

### Q3 & Q4: FISS / Sarcoma Boundaries and Causality

| Source | Title | Current Status | Claim-Fit | Access |
|---|---|---|---|---|
| `src-cancer-047` | Feline Injection Site Sarcomas: Data from Switzerland 2009–2014 | **abstract_weighted** | FISS decrease after non-adjuvanted vaccine, adjuvant hypothesis | ✅ PubMed abstract |
| `src-cancer-002` | Swiss Feline Cancer Registry 1965–2008 | **deep_extracted** (anchor) | registry context, FISS hypothesis | ✅ extracted |
| `src-cancer-094` | A transmissible feline fibrosarcoma of viral origin | title_only | historical viral sarcoma | historical context |
| `src-cancer-004` | Molecular Mechanisms of Feline Cancers | **deep_extracted** (anchor) | FISS occurrence range (1-10/10,000) | ✅ extracted |

**Current answer**: `src-cancer-002` and `src-cancer-004` provide registry context and FISS occurrence range. For direct FISS epidemiology and time-trend verification, need `src-cancer-047`.

**Next extraction priority**: `src-cancer-047` if ScienceDirect access can be obtained.

---

### Q5: Treatment Outcome Sources

This is the least developed area. Candidate sources by branch:

**Mammary carcinoma treatment:**
- `src-cancer-009` (abstract_weighted) - metastatic mammary cancer outcomes
- `src-cancer-045` - focused ultrasound treatment pilot
- `src-cancer-083` - early detection, aggressive therapy

**Lymphoma treatment:**
- Need to identify from title_only corpus

**Oral SCC treatment:**
- `src-cancer-080` (abstract_weighted) - MCT1/MCT4 inhibitor
- `src-cancer-077` - BNCT of head/neck cancer

**Current answer**: No treatment outcome sources are deep-extracted yet. The synthesis correctly gates treatment guidance.

**Next extraction priority**: `src-cancer-009` for mammary carcinoma outcomes if branch-control is needed.

---

## Extraction Priority Queue

Based on this mapping, the next branch-control extractions should be:

| Priority | Source | Branch | Current Depth | Next Step | Access |
|---|---|---|---|---|---|
| 1 | `src-cancer-095` | oral SCC | **abstract_weighted** | full-text deep extraction | MDPI open access |
| 2 | `src-cancer-063` | lymphoma | **abstract_weighted** | full-text deep extraction | MDPI open access |
| 3 | `src-cancer-068` | lymphoma | **abstract_weighted** | full-text deep extraction | MDPI open access |
| 4 | `src-cancer-047` | FISS | title_only | needs abstract + full-text | ScienceDirect paywall |
| 5 | `src-cancer-009` | mammary | abstract_weighted | full-text if treatment needed | journal access unknown |

## Progress Update (2026-05-30)

The three MDPI priority sources were upgraded from `title_only` to `abstract_weighted` via PubMed E-utilities. Key findings from abstracts:

- **src-cancer-095**: FOSCC is most common oral neoplasia; papillomavirus 16.2%, tobacco 35.2%, canned food 4.7x, flea collars 5.3x risk factors identified (limited studies)
- **src-cancer-063**: LGAL most prevalent subtype; JAK/STAT pathway homology with human GI T-cell lymphoma; IBD-lymphoma continuum discussed
- **src-cancer-068**: 1705 cases vs 85,741 reference; male OR 1.2; median age 11.7 years; 8 breeds increased risk, 3 decreased; breed-specific anatomic patterns

## Current Boundary

- Deep-extract only sources that change branch structure or unlock gated synthesis.
- MDPI sources have abstract extraction complete; full-text deep extraction is next step.
- Treatment outcome sources remain lower priority until branch architecture is complete.
