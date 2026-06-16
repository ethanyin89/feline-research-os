# Metadata Enrichment Sample Run

Date: 2026-06-16
Purpose: Validate Semantic Scholar API before skillifying

## API Tested

**Semantic Scholar Graph API v1**
- Endpoint: `https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}`
- Fields: `title,citationCount,year,venue,abstract`
- Auth: None (free tier)
- Rate limit: ~100 requests/5 min (free tier)

## Sample Results

| source_id | DOI | API Success | Citations | Year | Venue Match |
|-----------|-----|-------------|-----------|------|-------------|
| src-ckd-004 | 10.1177/1098612X16631234 | ✓ | 161 | 2016 | ✓ Journal of Feline Medicine and Surgery |
| src-ckd-010 | 10.1177/0300985812453176 | ✓ | 155 | 2013 | ✓ Veterinary Pathology |
| src-ckd-011 | 10.1016/j.tvjl.2014.10.009 | ✓ | 87 | 2015 | ✓ The Veterinary Journal |
| src-ckd-024 | 10.1111/jvim.16377 | ✓ | 49 | 2022 | ✓ Journal of Veterinary Internal Medicine |
| src-ckd-013 | (no DOI) | — | — | — | needs title search |

## Findings

### What Works
1. DOI lookup is reliable and fast (~200ms)
2. Citation count is accurate and up-to-date
3. Year and venue match our frontmatter
4. Returns paperId for future reference

### Limitations
1. **Rate limit**: Free tier gets 429 quickly with batch requests
2. **Abstract**: Some publishers block it (returned null for src-ckd-004)
3. **No DOI fallback**: Title search exists but is less reliable + rate limited
4. **No Impact Factor**: Semantic Scholar doesn't provide IF

## Recommendations for Skill

1. **Get API key**: Apply at https://www.semanticscholar.org/product/api#api-key-form
2. **Cache results**: Store in source card frontmatter, don't re-fetch
3. **Rate limiting**: Max 1 request/second, batch with delays
4. **Fallback chain**: DOI → PMID → title search → manual
5. **IF source**: Use separate Scimago lookup table (CSV)

## Impact Factor Strategy

Semantic Scholar doesn't provide IF. Options:
1. **Scimago Journal Rankings**: Free CSV download, map journal name → SJR
2. **Manual lookup table**: Create `system/indexes/journal-impact-factors.json`
3. **Skip IF for now**: Focus on citation count first (more useful anyway)

**Recommendation**: Create local journal IF lookup table for top 20 veterinary journals.

## Next Steps

1. ✓ Sample run complete (4/5 DOIs successful)
2. → Create skill file with rate limiting + caching
3. → Create journal IF lookup table
4. → Update schema fields
