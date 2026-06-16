# /enrich-source-metadata

Fetch citation count and impact factor for source cards from external APIs.

## When to Use

- After adding a new source card with DOI
- Batch enrichment of existing source cards
- Before generating researcher-facing outputs where IF/citations matter

## Inputs

- `source_path`: Path to source card markdown file (e.g., `raw/papers/src-ckd-004.md`)
- `batch`: Optional, enrich all source cards in a directory

## External APIs

### Semantic Scholar (citation count)
- Endpoint: `https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}`
- Fields: `citationCount,year,venue,abstract`
- Rate limit: 100/5min free, higher with API key
- Fallback: title search if no DOI

### Journal IF Lookup
- Local file: `system/indexes/journal-impact-factors.json`
- Maps journal name → IF/SJR/h-index

## Steps

### Step 1: Read source card frontmatter

```bash
SOURCE_PATH="${1:-raw/papers/src-ckd-004.md}"
head -100 "$SOURCE_PATH" | grep -E "^(doi|title|journal|year):"
```

Extract DOI and journal name from frontmatter.

### Step 2: Fetch citation count from Semantic Scholar

```bash
DOI=$(grep "doi:" "$SOURCE_PATH" | sed 's/.*doi: *"\?\([^"]*\)"\?/\1/' | tr -d ' ')
if [ -n "$DOI" ] && [ "$DOI" != '""' ]; then
  RESPONSE=$(curl -s "https://api.semanticscholar.org/graph/v1/paper/DOI:$DOI?fields=citationCount,year,venue")
  CITATIONS=$(echo "$RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('citationCount',''))" 2>/dev/null)
  VENUE=$(echo "$RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('venue',''))" 2>/dev/null)
  echo "Citations: $CITATIONS"
  echo "Venue: $VENUE"
else
  echo "No DOI found, skipping Semantic Scholar lookup"
fi
```

### Step 3: Look up Impact Factor

```bash
JOURNAL=$(grep -i "journal:" "$SOURCE_PATH" | head -1 | sed 's/.*journal: *"\?\([^"]*\)"\?/\1/' | tr '[:upper:]' '[:lower:]')
IF_FILE="system/indexes/journal-impact-factors.json"
if [ -f "$IF_FILE" ] && [ -n "$JOURNAL" ]; then
  IF=$(python3 -c "import json; d=json.load(open('$IF_FILE')); j=d.get('journals',{}).get('$JOURNAL',{}); print(j.get('if',''))" 2>/dev/null)
  echo "Impact Factor: $IF"
fi
```

### Step 4: Update frontmatter (if values found)

Use the Edit tool to add fields to frontmatter:

```yaml
citation_count: 161
impact_factor: 1.8
metadata_enriched: 2026-06-16
```

**Location**: After `verification_status:` line, before `tags:` line.

### Step 5: Report result

Output:
```
Enriched: src-ckd-004
  - citation_count: 161
  - impact_factor: 1.8
  - venue_verified: Journal of Feline Medicine and Surgery
```

## Batch Mode

For batch enrichment of all source cards:

```bash
for f in raw/papers/src-*.md; do
  echo "Processing: $f"
  # Run steps 1-4 for each file
  sleep 1  # Rate limiting
done
```

## Caching Rules

1. **Don't re-fetch** if `metadata_enriched` date is < 30 days old
2. **Force refresh** with `--force` flag
3. **Store raw API response** in `system/cache/semantic-scholar/` for debugging

## Error Handling

| Error | Action |
|-------|--------|
| 429 Rate Limit | Wait 60s, retry once |
| No DOI | Try title search OR mark as `needs_manual_lookup` |
| API timeout | Log and continue to next file |
| Journal not in IF table | Leave IF blank, add journal to table later |

## Example Run

```bash
# Single file
/enrich-source-metadata raw/papers/src-ckd-004.md

# Batch (with rate limiting)
/enrich-source-metadata --batch raw/papers/

# Force refresh
/enrich-source-metadata --force raw/papers/src-ckd-004.md
```

## Output Fields Added

| Field | Source | Example |
|-------|--------|---------|
| `citation_count` | Semantic Scholar | 161 |
| `impact_factor` | Local lookup | 1.8 |
| `sjr` | Local lookup | 0.62 |
| `metadata_enriched` | Timestamp | 2026-06-16 |

## Maintenance

- **Journal IF table**: Update quarterly from Scimago
- **API key**: Apply at https://www.semanticscholar.org/product/api for higher limits
- **New journals**: Add to `journal-impact-factors.json` as encountered
