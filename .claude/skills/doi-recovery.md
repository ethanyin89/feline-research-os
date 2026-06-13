# /doi-recovery

Recover DOIs from URLs for source cards missing DOI metadata.

## Trigger

- `/doi-recovery <source-id>` — recover DOI for single source
- `/doi-recovery batch --disease <disease>` — recover DOIs for all sources in a disease module
- `/doi-recovery list --disease <disease>` — show sources missing DOIs

## Supported URL Patterns

| Pattern | Method | Example |
|---------|--------|---------|
| MDPI | Pattern extraction | `https://www.mdpi.com/2076-2615/14/4/630` → `10.3390/ani14040630` |
| PubMed | NCBI API | `https://pubmed.ncbi.nlm.nih.gov/24783628/` → DOI via eutils |
| Direct DOI in URL | Regex extraction | URLs containing `doi.org/10.xxx` |

## URL Patterns Requiring Manual Recovery

- OUP academic.oup.com (JVIM, etc.)
- ScienceDirect with PII
- Springer link.springer.com
- Wiley onlinelibrary.wiley.com

For these, use the search fallback:
```bash
python3 -c "
import urllib.parse
title = 'YOUR TITLE HERE'
encoded = urllib.parse.quote(title[:50])
print(f'https://api.crossref.org/works?query.title={encoded}&rows=1')
"
```

## Workflow

### Step 1: Identify Sources Missing DOIs

```bash
python3 scripts/doi_recovery.py --disease ckd 2>&1 | grep "not_recovered\|NO_DOI"
```

### Step 2: Run Automatic Recovery

```bash
python3 scripts/doi_recovery.py --disease ckd --write
```

### Step 3: Manual Recovery for Remaining Sources

For sources that fail automatic recovery:
1. Search Crossref by title
2. Check the source URL directly for DOI metadata
3. Update source card manually

### Step 4: Run Structured Abstract Extraction

After DOIs are recovered:
```bash
python3 scripts/structured_abstract_extraction.py \
  --source-glob "raw/papers/src-ckd-*.md" \
  --status title_only \
  --write
```

## Output

| Item | Path |
|------|------|
| Script | `scripts/doi_recovery.py` |
| Updated source cards | `raw/papers/src-{disease}-{n}.md` |

## MDPI DOI Format

MDPI URLs follow this pattern:
- URL: `https://www.mdpi.com/{ISSN}/{volume}/{issue}/{article}`
- DOI: `10.3390/{journal_abbrev}{volume}{issue:02d}{article:04d}`

Journal abbreviations:
- `2076-2615` → `ani` (Animals)
- `2306-7381` → `vetsci` (Veterinary Sciences)
- `1999-4915` → `v` (Viruses)

## Related Skills

- `/structured-abstract-extract` — create abstract worksheets after DOI recovery
- `/cancer-deep-extract` — full-text deep extraction
