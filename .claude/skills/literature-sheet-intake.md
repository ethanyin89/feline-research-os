# /literature-sheet-intake

Google Sheet to source card creation workflow. Fetches literature references from Google Sheets, classifies them, and creates abstract-weighted source cards for new entries.

## Trigger

- `/literature-sheet-intake <disease>` — e.g., `/literature-sheet-intake fcv`
- `/literature-sheet-intake continue <disease>` — resume from last manifest progress
- `/literature-sheet-intake list` — show available sheet gids for each disease
- `/literature-sheet-intake status <disease>` — show intake manifest status

## Input

- `disease`: Disease code (ckd, cancer, diabetes, fcv, fip, hcm, ibd, obesity)

## Sheet Registry

| Disease | GID | Sheet Name | Notes |
|---------|-----|------------|-------|
| diabetes | 0 | Sheet1 (default) | Diabetes papers, split by "Feline Obesity" row |
| obesity | 0 | Sheet1 | Same sheet as diabetes, rows after "Feline Obesity" marker |
| ckd | 396361602 | CKD | CKD literature |
| hcm | 402159550 | HCM | HCM literature |
| fip | 639162275 | FIP | FIP literature |
| ibd | 763356244 | IBD | IBD literature |
| fcv | 799421167 | Feline calicivirus | FCV literature |
| cancer | 1048283205 | Feline cancer | Cancer literature |

Google Sheet base URL (main): `https://docs.google.com/spreadsheets/d/1Y-MSR39kW5F5J4OedcctdeHk0jhe1mbyvsK43Fcc7lk/export?format=csv&gid=`

## Workflow

### Step 0: Check Existing Progress

```bash
# Check for existing intake manifest
DISEASE="${1:-fcv}"
MANIFEST=$(ls -t system/indexes/feline-${DISEASE}-intake-manifest-*.md 2>/dev/null | head -1)
if [ -n "$MANIFEST" ]; then
  echo "Found existing manifest: $MANIFEST"
  grep "COMPLETED\|IN PROGRESS" "$MANIFEST" | tail -5
else
  echo "No existing manifest for $DISEASE"
fi
```

If manifest exists and shows incomplete batches, resume from last completed tier. Otherwise create new manifest.

### Step 1: Fetch Google Sheet

```bash
# Get GID for disease
case "$DISEASE" in
  diabetes|obesity) GID=0 ;;
  ckd) GID=396361602 ;;
  hcm) GID=402159550 ;;
  fip) GID=639162275 ;;
  ibd) GID=763356244 ;;
  fcv) GID=799421167 ;;
  cancer) GID=1048283205 ;;
  *) echo "Unknown GID for $DISEASE - check sheet registry"; exit 1 ;;
esac

# Export CSV
curl -sL "https://docs.google.com/spreadsheets/d/1Y-MSR39kW5F5J4OedcctdeHk0jhe1mbyvsK43Fcc7lk/export?format=csv&gid=$GID" -o /tmp/${DISEASE}-sheet.csv

# Preview
head -5 /tmp/${DISEASE}-sheet.csv
wc -l /tmp/${DISEASE}-sheet.csv
```

### Step 2: Generate Intake Manifest

```bash
python3 scripts/literature_sheet_intake.py \
  --csv /tmp/${DISEASE}-sheet.csv \
  --segment "$DISEASE" \
  --source-label "Google Sheet gid=$GID" \
  --manifest-id "feline-${DISEASE}-intake-manifest-$(date +%Y%m%d)" \
  --out "system/indexes/feline-${DISEASE}-intake-manifest-$(date +%Y%m%d).md"
```

Review manifest output:
- `existing`: Already in vault, skip
- `duplicate-in-sheet`: Same DOI appeared earlier, skip
- `new-{disease}`: Create source card
- `incomplete-locator`: Needs DOI recovery first

### Step 3: Prioritize New Entries

From manifest, classify new entries by priority:

**Tier 1 (HIGH): Clinical Impact**
- Virulent strains, outbreaks, treatment protocols
- Guidelines, consensus statements
- Novel therapeutics, vaccines

**Tier 2 (MEDIUM): Epidemiology/Diagnostics**
- Prevalence studies, geographic distribution
- Diagnostic test validation
- Molecular characterization

**Tier 3 (SUPPORTING): Mechanism/Basic Science**
- Receptor studies, pathogenesis
- In vitro studies
- Vaccine mechanism

Update manifest with tier assignments:

```markdown
## New Entry Priority Classification

### Tier 1: HIGH PRIORITY (Clinical Impact)
| # | Title | DOI | Topic |
|---|-------|-----|-------|
| {row} | {title} | {doi} | {topic} |

### Tier 2: MEDIUM PRIORITY (Epidemiology/Diagnostics)
...

### Tier 3: SUPPORTING (Mechanism/Basic Science)
...
```

### Step 4: Create Source Cards

For each new entry, create source card using this template:

```yaml
---
id: src-{disease}-{nnn}
type: source
title: "{title from sheet}"
source_kind: paper
species: feline
diseases: [{disease_uppercase}]
models: [{relevant models}]
endpoints: [{relevant endpoints}]
jurisdictions: [{geographic scope}]
evidence_level: original-study
year: {publication year}
status: extracted
extraction_depth: partial
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
tags: [{disease}, {topic tags}]
links:
  doi: "{doi}"
  url: "https://doi.org/{doi}"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "{key finding 1 from abstract}"
    - "{key finding 2}"
  source_supported_conclusion:
    - "{conclusion 1}"
    - "{conclusion 2}"
  llm_inference:
    - "{inference that requires full text}"
---

# {Short Title}

## Evidence-Depth Caveat

Abstract-weighted extraction. Full text needed for {specific missing info}.

## One-Line Summary

{One sentence summary of main finding}

## Why It Matters For Feline {Disease}

{2-3 sentences explaining significance}

## Key Findings

### quoted_fact

- {Finding 1}
- {Finding 2}
- {Finding 3}

### source_supported_conclusion

- {Conclusion 1}
- {Conclusion 2}

## Linked Entities

- diseases: {Disease}
- models: {models}
- endpoints: {endpoints}
- mechanisms: {mechanisms}
- regulations: {if applicable}
```

### Step 5: DOI Recovery & Year Metadata Extraction

If a card has a DOI or title-embedded date but is missing the `year` field:

```bash
# Dry run to preview year extractions
python3 scripts/extract_year_metadata.py

# Apply the year extractions to raw paper source cards
python3 scripts/extract_year_metadata.py --apply
```

If an entry has a URL but no DOI:
1. Search Crossref or PubMed for the title to recover the DOI.
2. Update the card frontmatter with the recovered DOI and year.

### Step 6: Metadata Check & Card Upgrade (Triage to abstract_weighted)

Check Crossref/PubMed API for the newly added source cards to fetch their metadata and abstracts, and automatically upgrade them to `abstract_weighted`:

```bash
# Run metadata check and automatically upgrade eligible cards with abstracts
python3 scripts/source_metadata_check.py --source-ids src-{disease}-NNN,src-{disease}-MMM --update-cards
```

### Step 7: Update Repository Indexes

Re-run index synchronization to compile the new cards into the global depth map and disease index:

```bash
python3 scripts/sync_indexes.py
```

### Step 8: Run Health Check

Verify vault integrity after all updates:

```bash
python3 scripts/health.py
```

Verify that:
- Link check: **PASS**
- Query tests: **PASS**
- Paper source cards count increased and matched
- No YAML format errors or metadata conflicts exist.

## Batch Processing

Process in batches of 5-10 sources per tier:
1. Complete Tier 1 first (highest clinical impact)
2. Then Tier 2 (epidemiology/diagnostics)
3. Finally Tier 3 (mechanism/supporting)

For each source:
1. Check if DOI exists → if not, run DOI recovery
2. WebFetch abstract if available
3. Create source card with evidence_policy
4. Update manifest progress

## Output Summary

Report after each batch:

| Item | Count |
|------|-------|
| Sources created | {N} |
| DOIs recovered | {M} |
| Skipped (no abstract) | {K} |
| Current total | {total} |

## Verify Run

```bash
# Count sources for disease
ls raw/papers/src-${DISEASE}-*.md | wc -l

# Check latest sources
ls -t raw/papers/src-${DISEASE}-*.md | head -5

# Verify health
python3 scripts/health.py 2>&1 | grep "Paper source cards"
```

## Sample Sessions (33+ FCV samples completed 2026-06-08)

### FCV Full Intake (103 sources total)

**Tier 1 (7 sources):**
- src-fcv-025: VS-FCV outbreak (10.2460/javma.2004.224.241)
- src-fcv-026: VS-FCV lethal outbreak (10.1136/vr.158.16.544)
- src-fcv-027: VS-FCV + antivirals Australia (10.3390/v13102040)
- src-fcv-028: mRNA vaccine (10.1016/j.vaccine.2025.01.106)
- src-fcv-029: Gingivostomatitis association (10.1016/j.jfms.2007.05.007)
- src-fcv-030: Next-gen vaccine challenges (10.1016/j.vetmic.2006.01.015)
- src-fcv-031: 3C-protease inhibitors (10.1128/jvi.03688-14)

**Tier 2 (13 sources):**
- src-fcv-032 through src-fcv-044: European epidemiology, shedding, receptor, diversity

**Tier 3-8 (56 sources):**
- src-fcv-045 through src-fcv-100: Supporting evidence, regional studies, vaccines, diagnostics

**Final batch (3 sources):**
- src-fcv-101: Australian seroprevalence
- src-fcv-102: Geographic vaccine specificity
- src-fcv-103: European wildcat surveillance

## Related Skills

- `/structured-abstract-extract` — upgrade title_only to abstract_weighted via Crossref
- `/cancer-deep-extract` — full text extraction for deep_extracted status
- `/doi-recovery` — recover missing DOIs
- `/source-check` — verify source metadata

## Automation Notes

For ongoing sheet monitoring:
1. Set up periodic fetch (weekly) to check for new entries
2. Compare row count vs manifest total
3. If new rows detected, classify and process

Cron setup (example):
```bash
# Weekly sheet check - add to crontab
0 9 * * 1 cd /path/to/repo && python3 scripts/literature_sheet_intake.py --csv <(curl -sL "URL") --segment fcv --out /tmp/fcv-check.md && diff system/indexes/feline-fcv-intake-manifest-*.md /tmp/fcv-check.md
```
