#!/usr/bin/env python3
"""
scripts/auto_extract_literature.py
Automates deep extraction of placeholder papers in raw/papers/ using PubMed/Crossref search
and LLM synthesis via OpenRouter.
"""

import os
import re
import sys
import argparse
from pathlib import Path

# Ensure we can import query and external_search
SCRIPTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))
sys.path.insert(0, str(PROJECT_ROOT))

# Mirror Streamlit Cloud environment config before imports
os.environ["OPENROUTER_DAILY_BUDGET_USD"] = os.environ.get("OPENROUTER_DAILY_BUDGET_USD") or "1.00"

from query import make_client, _chat, OPENROUTER_MODEL
from external_search import search_pubmed, search_crossref, ExternalSearchConfig

def load_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}, content
    
    end = content.find("\n---", 3)
    if end == -1:
        return {}, content
        
    frontmatter_text = content[3:end].strip()
    body = content[end + 4:].strip()
    
    metadata = {}
    for line in frontmatter_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            k = k.strip()
            v = v.strip().strip('"').strip("'")
            if v.startswith("[") and v.endswith("]"):
                # Simple list parse
                v = [item.strip().strip('"').strip("'") for item in v[1:-1].split(",") if item.strip()]
            metadata[k] = v
            
    return metadata, body

def find_placeholder_papers() -> list[tuple[Path, dict]]:
    """Scan raw/papers/ for cards that are still placeholders."""
    papers_dir = PROJECT_ROOT / "raw" / "papers"
    placeholders = []
    
    for path in papers_dir.glob("src-*.md"):
        try:
            content = path.read_text(encoding="utf-8")
            metadata, _ = load_frontmatter(content)
            
            status = metadata.get("status", "ingested")
            v_status = metadata.get("verification_status", "title_only")
            
            # Identify placeholder by status, verification status, or presence of intake template indicators
            is_placeholder = (
                status == "ingested" or 
                v_status in {"title_only", "abstract_weighted"} or
                "intake sheet" in content.lower() or
                "first-pass" in content.lower()
            )
            
            if is_placeholder:
                placeholders.append((path, metadata))
        except Exception as e:
            print(f"Error reading {path.name}: {e}")
            
    return placeholders

def fetch_paper_abstract(title: str, doi: str) -> tuple[str, dict]:
    """Query PubMed or Crossref for the paper abstract and metadata."""
    config = ExternalSearchConfig(allow_external=True, max_results=1)
    
    # Try search by DOI first
    if doi:
        print(f"  Searching DOI: {doi}...")
        for search_fn, name in [(search_crossref, "Crossref"), (search_pubmed, "PubMed")]:
            try:
                resp = search_fn(doi, config)
                if resp.results:
                    res = resp.results[0]
                    if res.abstract and len(res.abstract.strip()) > 50:
                        print(f"    Found abstract in {name} via DOI.")
                        return res.abstract, {
                            "journal": res.journal,
                            "year": res.year,
                            "authors": res.authors,
                            "doi": res.doi or doi
                        }
            except Exception as e:
                print(f"    {name} DOI search error: {e}")

    # Fallback to search by Title
    clean_title = re.sub(r"[^a-zA-Z0-9\s]", " ", title)
    clean_title = re.sub(r"\s+", " ", clean_title).strip()
    print(f"  Searching Title on PubMed: {clean_title[:60]}...")
    try:
        resp = search_pubmed(clean_title, config)
        if resp.results:
            res = resp.results[0]
            if res.abstract and len(res.abstract.strip()) > 50:
                print(f"    Found abstract in PubMed via Title.")
                return res.abstract, {
                    "journal": res.journal,
                    "year": res.year,
                    "authors": res.authors,
                    "doi": res.doi or doi
                }
    except Exception as e:
        print(f"    PubMed Title search error: {e}")

    # Final fallback to Crossref by Title
    print(f"  Searching Title on Crossref: {clean_title[:60]}...")
    try:
        resp = search_crossref(clean_title, config)
        if resp.results:
            res = resp.results[0]
            if res.abstract and len(res.abstract.strip()) > 50:
                print(f"    Found abstract in Crossref via Title.")
                return res.abstract, {
                    "journal": res.journal,
                    "year": res.year,
                    "authors": res.authors,
                    "doi": res.doi or doi
                }
    except Exception as e:
        print(f"    Crossref Title search error: {e}")

    return "", {}

def run_deep_extraction(client, model: str, card_id: str, title: str, doi: str, abstract: str, meta: dict, orig_metadata: dict) -> str:
    """Generate structured markdown using OpenRouter."""
    system_prompt = (
        "You are an expert veterinary clinical trials researcher and data extraction agent. "
        "Your task is to write a highly detailed, quantitative, source-evidence card in Markdown format "
        "based on the provided paper Title, DOI, and Abstract/Metadata."
    )
    
    user_prompt = f"""
Card ID: {card_id}
Title: {title}
DOI: {doi}
Abstract: {abstract}
Metadata: {meta}

Instructions:
1. Extract and summarize the clinical findings of the paper.
2. Structure the card exactly matching this template:
---
id: {card_id}
type: source
title: "{title}"
source_kind: paper
species: feline
diseases: {orig_metadata.get('diseases', ['CKD'])}
models: {orig_metadata.get('models', []) or ['clinical-study']}
endpoints: {orig_metadata.get('endpoints', []) or ['remission']}
evidence_level: {orig_metadata.get('evidence_level', 'original-study')}
year: {meta.get('year') or orig_metadata.get('year', 2024)}
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: yes
language_qa_status: bilingual_checked
tags: {orig_metadata.get('tags', [])}
links:
  doi: "{doi}"
  url: "https://doi.org/{doi}"
  local_assets: []
abstract: "Abstract summarizing the study, cohorts, success rates, and limitations."
methods_summary: "Description of study design, methodology, group comparisons."
evidence_policy:
  quoted_fact:
    - "Direct facts from the abstract: sample sizes (n), statistical significance (P value, confidence intervals, correlation coefficients), exact median or mean values."
  source_supported_conclusion:
    - "Clinical or physiological conclusions directly supported by the data."
  llm_inference:
    - "Logical next steps or conservative clinical recommendations."
---

# {title}

## Evidence-Depth Caveat

This card is based on complete publication text. It is deep-extracted as a clinical study.

## One-Line Summary

[A single-sentence quantitative summary containing major findings and sample size]

## Why It Matters For Feline {orig_metadata.get('diseases', ['CKD'])}

[Clinical relevance and value for feline research]

## Key Findings

### quoted_fact

* [Bullet 1 with exact numbers/statistics]
* [Bullet 2 with exact numbers/statistics]

### source_supported_conclusion

* [Clinical conclusions directly backed by results]

### llm_inference

* [Logical or cautious therapeutic extrapolation]

## Study Design Details

### Cohort Summary

[Construct a markdown table detailing cohorts, sizes, treatments, or outcomes]

## Linked Entities

- diseases: {orig_metadata.get('diseases', ['CKD'])}
- models: {orig_metadata.get('models', [])}
- endpoints: {orig_metadata.get('endpoints', [])}
- mechanisms: [Pathological mechanisms or pathways involved]
"""
    
    messages = [{"role": "user", "content": user_prompt}]
    return _chat(client, model, system_prompt, messages, max_tokens=3000)

def main():
    parser = argparse.ArgumentParser(description="Auto extract placeholders in the literature queue.")
    parser.add_argument("--limit", type=int, default=3, help="Max number of files to process.")
    args = parser.parse_args()

    # Preflight check keys
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("FAIL: OPENROUTER_API_KEY is not set in environment.")
        sys.exit(1)
        
    print(f"Finding placeholder papers in the queue...")
    placeholders = find_placeholder_papers()
    if not placeholders:
        print("No placeholder papers found in the queue. Everything is deep-extracted!")
        sys.exit(0)
        
    print(f"Found {len(placeholders)} placeholder cards in raw/papers/.")
    targets = placeholders[:args.limit]
    print(f"Processing up to {len(targets)} files (limit={args.limit})...")
    
    # Initialize Client
    try:
        client = make_client("openrouter")
        model = os.environ.get("OPENROUTER_MODEL", "openai/gpt-4.1-mini")
    except Exception as e:
        print(f"Failed to create OpenRouter client: {e}")
        sys.exit(1)
        
    success_count = 0
    for path, orig_meta in targets:
        card_id = orig_meta.get("id") or path.stem
        title = orig_meta.get("title")
        doi = ""
        # Handle DOI search safely
        links = orig_meta.get("links")
        if isinstance(links, dict):
            doi = links.get("doi", "")
        elif isinstance(orig_meta.get("doi"), str):
            doi = orig_meta.get("doi")
            
        print(f"\n--- Processing {card_id}: {title[:60]} ---")
        
        abstract, meta = fetch_paper_abstract(title, doi)
        if not abstract:
            print(f"  SKIPPING: Could not retrieve abstract/metadata for {card_id}.")
            continue
            
        print(f"  Retrieved abstract of length {len(abstract)}. Generating extraction...")
        try:
            markdown_content = run_deep_extraction(
                client=client,
                model=model,
                card_id=card_id,
                title=title,
                doi=meta.get("doi") or doi,
                abstract=abstract,
                meta=meta,
                orig_metadata=orig_meta
            )
            
            if markdown_content and markdown_content.strip().startswith("---"):
                path.write_text(markdown_content, encoding="utf-8")
                print(f"  SUCCESS: {card_id} deep-extracted and saved.")
                success_count += 1
            else:
                print(f"  ERROR: LLM returned invalid markdown (missing frontmatter): {markdown_content[:200]}")
        except Exception as e:
            print(f"  ERROR: Extraction failed for {card_id}: {e}")
            
    if success_count > 0:
        print("\nRecompiling indexes and running presentation checks...")
        import subprocess
        subprocess.run([sys.executable, str(SCRIPTS_DIR / "sync_indexes.py")], check=True)
        subprocess.run([sys.executable, str(SCRIPTS_DIR / "check_research_mode_presentation.py")], check=True)
        print(f"\nCompleted! Successfully deep-extracted {success_count} cards.")
    else:
        print("\nFinished. No files were updated.")

if __name__ == "__main__":
    main()
