# Handoff: Intake Workflow Codification

**Date:** 2026-06-05
**Session:** Google Sheet intake workflow codification and CKD extension processing

## Summary

Following the rule "不允许做一次性工作" (no one-off work), this session codified the literature intake extraction workflow into reusable skills and processed remaining CKD extension sources.

## Completed Work

### 1. Codified Skills Created

| Skill | Path | Purpose |
|-------|------|---------|
| `/structured-abstract-extract` | `.claude/skills/structured-abstract-extract.md` | Abstract-level extraction from Crossref |
| `/doi-recovery` | `.claude/skills/doi-recovery.md` | Recover missing DOIs from URLs |

### 2. Scripts Created/Updated

| Script | Purpose |
|--------|---------|
| `scripts/doi_recovery.py` | Automatic DOI recovery (MDPI, PubMed, URL patterns) |

### 3. CKD Extension Processing

**Before this session:**
- 8 sources with structured abstracts (src-ckd-025, 026, 033, 034, 035, 043, 045, 046)
- 2 sources upgraded to source_checked (src-ckd-026, src-ckd-034)
- 18 sources at title_only

**After this session:**
- 14 sources with structured abstracts (+6 new)
- 6 new worksheets created:
  - `src-ckd-030-structured-abstract-round1.md` (Lactobacillus kidney protection)
  - `src-ckd-036-structured-abstract-round1.md` (Renal senescence, telomere)
  - `src-ckd-037-structured-abstract-round1.md` (Feline morbillivirus)
  - `src-ckd-038-structured-abstract-round1.md` (Polycystic kidney disease)
  - `src-ckd-041-structured-abstract-round1.md` (Inflammatory markers)
  - `src-ckd-048-structured-abstract-round1.md` (Health-related QOL)

### 4. DOI Recovery Results

| Source | Status | DOI |
|--------|--------|-----|
| src-ckd-030 | recovered (MDPI) | 10.3390/ani14040630 |
| src-ckd-036 | recovered (MDPI) | 10.3390/vetsci8120314 |
| src-ckd-037 | recovered (MDPI) | 10.3390/v12050501 |
| src-ckd-038 | recovered (MDPI) | 10.3390/vetsci8110269 |
| src-ckd-041 | recovered (MDPI) | 10.3390/ani13233674 |
| src-ckd-048 | recovered (PubMed) | 10.1177/1098612X251367535 |

### 5. Sources Still Needing Manual DOI Recovery

These 9 sources have URLs but DOIs couldn't be auto-recovered:

| Source | URL Pattern | Manual Action Needed |
|--------|-------------|---------------------|
| src-ckd-028 | academic.oup.com | Search Crossref by title |
| src-ckd-031 | academic.oup.com | Search Crossref by title |
| src-ckd-032 | pubmed (no DOI returned) | Check PubMed record |
| src-ckd-039 | sciencedirect.com | Extract from page/search |
| src-ckd-040 | sciencedirect.com | Extract from page/search |
| src-ckd-042 | academic.oup.com | Search Crossref by title |
| src-ckd-044 | sciencedirect.com | Extract from page/search |
| src-ckd-047 | sciencedirect.com | Extract from page/search |
| src-ckd-049 | sciencedirect.com | Extract from page/search |

## Current State Summary

| Disease | Total Sources | deep_extracted | source_checked | abstract_weighted | title_only |
|---------|---------------|----------------|----------------|-------------------|------------|
| CKD | 50 | 24 (seed) | 2 | 12 | 12 |
| Cancer | 102 | varies | varies | varies | many |
| FCV | 24 | 24 | 0 | 0 | 0 |

## Workflow Now Codified

```
Google Sheet → literature_sheet_intake.py → Intake Manifest
                                               ↓
                                    /doi-recovery (if DOIs missing)
                                               ↓
                                    /structured-abstract-extract
                                               ↓
                              abstract_weighted source cards
                                               ↓
                              /cancer-deep-extract or manual deep extraction
                                               ↓
                              source_checked or deep_extracted
```

## Session 2 Progress (continued same day)

### DOI Recovery Results (Manual Crossref Search)

| Source | DOI Recovered | Crossref Abstract |
|--------|---------------|-------------------|
| src-ckd-028 | 10.1111/jvim.15808 | ✓ worksheet created |
| src-ckd-031 | 10.1111/j.1939-1676.2007.tb03042.x | ✓ worksheet created |
| src-ckd-032 | NOT FOUND (JAVMA 2014) | N/A |
| src-ckd-039 | 10.1016/j.jcpa.2018.03.004 | no abstract in Crossref |
| src-ckd-040 | 10.1016/j.jcpa.2019.05.006 | no abstract in Crossref |
| src-ckd-042 | 10.1111/jvim.16363 | ✓ worksheet created |
| src-ckd-044 | 10.1016/j.tvjl.2019.105358 | no abstract in Crossref |
| src-ckd-047 | 10.1016/j.cvsm.2016.06.002 | no abstract in Crossref |
| src-ckd-049 | 10.1016/j.cvsm.2016.06.014 | no abstract in Crossref |

### Current CKD Extension Status After Session 2

| Status | Count | Source IDs |
|--------|-------|------------|
| source_checked | 2 | 026, 034 |
| abstract_weighted | 15 | 025, 028, 030, 031, 033, 035, 036, 037, 038, 041, 042, 043, 045, 046, 048 |
| title_only | 9 | 027, 029, 032, 039, 040, 044, 047, 049, 050 |

### Sources Still Needing Work

**No DOI found:**
- src-ckd-032: JAVMA 2014 "Chronic kidney disease in cats" (PMID 24783628) - search JAVMA directly

**Have DOI but no Crossref abstract (need alternative extraction):**
- src-ckd-027, 029, 050: Already had DOIs
- src-ckd-039, 040, 044, 047, 049: DOIs recovered this session

**Alternative abstract retrieval options:**
1. PubMed E-utilities efetch for abstract (TESTED - works)
   ```bash
   # Find PMID from DOI
   curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=DOI_HERE&retmode=json"
   # Fetch abstract
   curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=PMID_HERE&rettype=abstract&retmode=text"
   ```
2. Publisher page scraping
3. Manual entry from PDF

**Codification opportunity:** Add PubMed fallback to structured_abstract_extraction.py

## Next Session Priorities

1. **Alternative abstract retrieval** for 9 sources with DOIs but no Crossref abstracts
2. **src-ckd-032 DOI recovery** — search JAVMA directly or use PII
3. **Cancer module** — run same DOI recovery + structured abstract workflow
4. **Update source-depth-map.md** after batch completes

## Commands for Next Session

```bash
# Check current CKD status
grep "verification_status" raw/papers/src-ckd-0{25..50}.md | sort | uniq -c

# Manual DOI recovery for remaining sources
# Use Crossref search: https://api.crossref.org/works?query.title=YOUR+TITLE&rows=1

# Run structured abstract for recovered sources
python3 scripts/structured_abstract_extraction.py \
  --source-ids "src-ckd-028,src-ckd-031,..." \
  --write

# Check cancer sources needing processing
grep -l "verification_status: title_only" raw/papers/src-cancer-*.md | wc -l
```

## Files Modified This Session

| File | Change |
|------|--------|
| `.claude/skills/structured-abstract-extract.md` | Created |
| `.claude/skills/doi-recovery.md` | Created |
| `scripts/doi_recovery.py` | Created |
| `raw/papers/src-ckd-030.md` | DOI + status updated |
| `raw/papers/src-ckd-036.md` | DOI + status updated |
| `raw/papers/src-ckd-037.md` | DOI + status updated |
| `raw/papers/src-ckd-038.md` | DOI + status updated |
| `raw/papers/src-ckd-041.md` | DOI + status updated |
| `raw/papers/src-ckd-048.md` | DOI + status updated |
| `system/indexes/feline-ckd-extension-structured-abstract-batch2-*.md` | Created |
| `system/indexes/src-ckd-{030,036,037,038,041,048}-structured-abstract-round1.md` | Created |
