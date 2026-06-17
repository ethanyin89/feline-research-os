# Skill: Deep Extract Source Cards

Invoke: `/deep-extract [source-id]` or `/deep-extract --batch`

## Purpose

Deep-extract source cards from `abstract_weighted` or `title_only` to `deep_extracted` status by fetching full text or abstracts from open-access sources (MDPI, PMC, PLOS, BMC).

## Single Source Extraction

```bash
/deep-extract src-cancer-031
```

### Steps

1. **Read current source card**
   ```
   Read raw/papers/{source-id}.md
   ```

2. **Get PMID if missing**
   ```
   WebFetch https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:{doi}&format=json
   → Extract PMID
   ```

3. **Fetch abstract/content**
   ```
   WebFetch https://pubmed.ncbi.nlm.nih.gov/{pmid}/
   → Extract: study design, key findings, statistics, verbatim quotes
   ```

   For PMC full text:
   ```
   WebFetch https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/
   ```

4. **Update frontmatter**
   - `status: deep_extracted`
   - `extraction_depth: full`
   - `verification_status: deep_extracted`
   - Add `pmid`, `doi` if missing
   - Update `evidence_policy.quoted_fact` with verbatim quotes
   - Update `evidence_policy.source_supported_conclusion` with findings
   - Update `evidence_policy.llm_inference` with caveats

5. **Update body**
   - Evidence-Depth Caveat (first section)
   - Source Check table (PMID, DOI, journal, year)
   - Key findings tables
   - One-Line Summary
   - Claim-Fit Judgment
   - Deep Extraction Metadata
   - Linked Entities

6. **Commit**
   ```bash
   git add raw/papers/{source-id}.md
   git commit -m "feat: deep-extract {source-id} ({brief description})"
   ```

## Batch Extraction

```bash
/deep-extract --batch
```

### Steps

1. **Find open-access sources needing extraction**
   ```bash
   # Find sources with MDPI/PMC/PLOS DOIs still at abstract_weighted
   for f in raw/papers/src-*.md; do
     if grep -q "verification_status: abstract_weighted" "$f"; then
       doi=$(grep "^doi:" "$f")
       if echo "$doi" | grep -qE "10\.3390|plos|bmc|hindawi|frontiers"; then
         echo "$(basename $f .md): $doi"
       fi
     fi
   done
   ```

2. **Prioritize by branch-control (topic page citations)**
   ```bash
   for src in {source-list}; do
     count=$(grep -r "$src" topics/ | wc -l)
     echo "$src: $count citations"
   done | sort -t: -k2 -rn
   ```

3. **Extract top 3-5 sources per session**

4. **Commit as batch**
   ```bash
   git add raw/papers/src-*.md
   git commit -m "feat: deep-extract N sources ({modules})"
   ```

## Quality Checks

Before marking `deep_extracted`:

- [ ] `quoted_fact` contains verbatim text from source
- [ ] `source_supported_conclusion` is factual, not interpretive
- [ ] `llm_inference` clearly labeled as inference with caveats
- [ ] One-Line Summary under 150 characters
- [ ] Claim-Fit Judgment has all four categories
- [ ] Deep Extraction Metadata includes date and source

## Open-Access Detection

| DOI Pattern | Publisher | Access |
|-------------|-----------|--------|
| `10.3390/*` | MDPI | Open |
| `10.1371/*` | PLOS | Open |
| `10.1186/*` | BMC | Open |
| `10.1155/*` | Hindawi | Open |
| `10.3389/*` | Frontiers | Open |
| `PMC*` | PubMed Central | Open |

## Evidence Policy Rules

### quoted_fact
- Exact text from source
- Include page/section if available
- Use quotation marks

### source_supported_conclusion
- Direct findings from the source
- No interpretation beyond what's stated
- Include sample sizes, statistics

### llm_inference
- Clearly labeled as inference
- Include uncertainty markers
- Note limitations

## Commit Message Format

```
feat: deep-extract {source-id} ({brief finding})

- Key finding 1
- Key finding 2
- N topic page citations

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

## Sample Extraction Output

```yaml
evidence_policy:
  quoted_fact:
    - "All cats recovered with dramatic improvement of clinical and laboratory parameters."
    - "Oral treatment was highly effective without causing serious adverse effects."
  source_supported_conclusion:
    - "100% survival (18/18 cats) with oral GS-441524."
    - "Two-tier dosing: 10 mg/kg (neurological) vs 5 mg/kg (other)."
    - "84-day treatment duration."
  llm_inference:
    - "Oral formulation provides practical alternative to injectable."
    - "100% cure rate is exceptional but n=18 is modest sample size."
```

## When NOT to Deep Extract

- Source is behind paywall (no open access)
- Source is a duplicate of existing card
- Source has no relevance to current disease modules
- Source is title-only with no abstract available
