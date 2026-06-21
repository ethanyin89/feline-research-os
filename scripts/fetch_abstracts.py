#!/usr/bin/env python3
"""
scripts/fetch_abstracts.py
Fetches abstracts and metadata from PubMed/Crossref for placeholder papers
and saves them to scratch/fetched_abstracts.json without using any paid LLM APIs.
Includes strict DOI and title similarity validation checks to prevent mismatches.
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))
sys.path.insert(0, str(PROJECT_ROOT))

from external_search import search_pubmed, search_crossref, ExternalSearchConfig

def load_frontmatter(content: str) -> tuple[dict, str]:
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
                v = [item.strip().strip('"').strip("'") for item in v[1:-1].split(",") if item.strip()]
            metadata[k] = v
            
    return metadata, body

def find_placeholder_papers() -> list[tuple[Path, dict]]:
    papers_dir = PROJECT_ROOT / "raw" / "papers"
    placeholders = []
    
    for path in papers_dir.glob("src-*.md"):
        try:
            content = path.read_text(encoding="utf-8")
            metadata, _ = load_frontmatter(content)
            
            status = metadata.get("status", "ingested")
            v_status = metadata.get("verification_status", "title_only")
            
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
            
    # Sort them by ID for deterministic order
    placeholders.sort(key=lambda x: x[0].name)
    return placeholders

def clean_doi(d: str) -> str:
    if not d:
        return ""
    return re.sub(r"[^a-zA-Z0-9/.]", "", d).lower().strip()

def is_title_match(title1: str, title2: str) -> bool:
    if not title1 or not title2:
        return False
    t1 = re.sub(r"[^a-z0-9\s]", " ", title1.lower())
    t2 = re.sub(r"[^a-z0-9\s]", " ", title2.lower())
    words1 = set(t1.split())
    words2 = set(t2.split())
    if not words1 or not words2:
        return False
    stopwords = {"a", "an", "the", "in", "on", "of", "and", "or", "for", "with", "to", "at", "by", "from", "up", "about", "into", "over", "after"}
    w1_filtered = {w for w in words1 if w not in stopwords and len(w) > 2}
    w2_filtered = {w for w in words2 if w not in stopwords and len(w) > 2}
    if not w1_filtered:
        w1_filtered = words1
        w2_filtered = words2
    common_filtered = w1_filtered.intersection(w2_filtered)
    overlap = len(common_filtered) / len(w1_filtered)
    return overlap >= 0.70  # At least 70% of content words must match

def fetch_paper_abstract(title: str, doi: str) -> tuple[str, dict]:
    config = ExternalSearchConfig(allow_external=True, max_results=1)
    
    # 1. Search by DOI first (strict DOI verify)
    if doi:
        cleaned_target_doi = clean_doi(doi)
        print(f"  Searching DOI: {doi}...")
        for search_fn, name in [(search_crossref, "Crossref"), (search_pubmed, "PubMed")]:
            try:
                resp = search_fn(doi, config)
                if resp.results:
                    res = resp.results[0]
                    # Verify DOI matches exactly, or title is a solid match
                    doi_ok = clean_doi(res.doi) == cleaned_target_doi
                    title_ok = is_title_match(title, res.title)
                    if doi_ok or title_ok:
                        if res.abstract and len(res.abstract.strip()) > 50:
                            print(f"    Found validated abstract in {name} via DOI.")
                            return res.abstract, {
                                "journal": res.journal,
                                "year": res.year,
                                "authors": res.authors,
                                "doi": res.doi or doi,
                                "verified": True
                            }
            except Exception as e:
                print(f"    {name} DOI search error: {e}")

    # 2. Fallback to Title search
    clean_title = re.sub(r"[^a-zA-Z0-9\s]", " ", title)
    clean_title = re.sub(r"\s+", " ", clean_title).strip()
    print(f"  Searching Title on PubMed: {clean_title[:60]}...")
    try:
        resp = search_pubmed(clean_title, config)
        if resp.results:
            res = resp.results[0]
            if is_title_match(title, res.title):
                if res.abstract and len(res.abstract.strip()) > 50:
                    print(f"    Found validated abstract in PubMed via Title.")
                    return res.abstract, {
                        "journal": res.journal,
                        "year": res.year,
                        "authors": res.authors,
                        "doi": res.doi or doi,
                        "verified": True
                    }
            else:
                print(f"    Rejected title mismatch on PubMed: {res.title[:60]}...")
    except Exception as e:
        print(f"    PubMed Title search error: {e}")

    # 3. Fallback to Crossref Title search
    print(f"  Searching Title on Crossref: {clean_title[:60]}...")
    try:
        resp = search_crossref(clean_title, config)
        if resp.results:
            res = resp.results[0]
            if is_title_match(title, res.title):
                if res.abstract and len(res.abstract.strip()) > 50:
                    print(f"    Found validated abstract in Crossref via Title.")
                    return res.abstract, {
                        "journal": res.journal,
                        "year": res.year,
                        "authors": res.authors,
                        "doi": res.doi or doi,
                        "verified": True
                    }
            else:
                print(f"    Rejected title mismatch on Crossref: {res.title[:60]}...")
    except Exception as e:
        print(f"    Crossref Title search error: {e}")

    return "", {}

def extract_pmcid_from_text(text: str) -> str:
    if not text:
        return ""
    match = re.search(r'(PMC\d+)', text, re.I)
    if match:
        return match.group(1).upper()
    return ""

def extract_pmcid_from_meta(orig_meta: dict) -> str:
    # Check under links dict
    links = orig_meta.get("links")
    if isinstance(links, dict):
        for k in ["pmc", "pmcid", "pmc_id"]:
            val = links.get(k)
            if isinstance(val, str) and val:
                pmcid = extract_pmcid_from_text(val)
                if pmcid:
                    return pmcid
    # Check top-level frontmatter keys
    for k in ["pmc", "pmcid", "pmc_id"]:
        val = orig_meta.get(k)
        if isinstance(val, str) and val:
            pmcid = extract_pmcid_from_text(val)
            if pmcid:
                return pmcid
    return ""

def resolve_pmcid(doi: str, pmid: str) -> str:
    import urllib.request
    import urllib.parse
    target_id = doi or pmid
    if not target_id:
        return ""
    try:
        url = f"https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids={urllib.parse.quote(target_id)}&format=json&tool=feline-research-os&email=research@example.com"
        req = urllib.request.Request(url, headers={"User-Agent": "feline-research-os/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
        records = data.get("records", [])
        if records:
            return records[0].get("pmcid", "")
    except Exception as e:
        print(f"    PMC ID converter error for {target_id}: {e}")
    return ""

def download_pmc_figures(pmcid: str, card_id: str, disease: str) -> list[str]:
    import urllib.request
    if not pmcid:
        return []
    
    target_dir = PROJECT_ROOT / "raw" / "images" / disease
    target_dir.mkdir(parents=True, exist_ok=True)
    
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    
    print(f"  Scraping PMC figures from {url}...")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8")
    except Exception as e:
        print(f"    Failed to fetch PMC page {url}: {e}")
        return []
        
    blobs = re.findall(r"https://cdn\.ncbi\.nlm\.nih\.gov/pmc/blobs/[^\s\"<>]+", html)
    blobs = sorted(set(blobs))
    if not blobs:
        print("    No figure blobs found in PMC page.")
        return []
        
    local_assets = []
    for blob_url in blobs:
        filename = blob_url.split("/")[-1]
        ext_match = re.search(r'\.(jpg|jpeg|png|gif)$', filename, re.I)
        if not ext_match:
            continue
        ext = ext_match.group(1).lower()
        
        fig_num_match = re.search(r'-g(\d+)\.', filename, re.I)
        if fig_num_match:
            fig_num = int(fig_num_match.group(1))
            local_filename = f"{card_id}-fig{fig_num}.{ext}"
        else:
            local_filename = f"{card_id}-{filename}"
            
        dest_path = target_dir / local_filename
        rel_dest_path = f"raw/images/{disease}/{local_filename}"
        
        if dest_path.exists():
            print(f"    Asset already exists: {rel_dest_path}")
            local_assets.append(rel_dest_path)
            continue
            
        print(f"    Downloading {blob_url} -> {rel_dest_path}...")
        try:
            img_req = urllib.request.Request(blob_url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            with urllib.request.urlopen(img_req, timeout=15) as img_resp:
                img_data = img_resp.read()
            dest_path.write_bytes(img_data)
            local_assets.append(rel_dest_path)
        except Exception as e:
            print(f"      Failed to download {blob_url}: {e}")
            
    return local_assets

def main():
    parser = argparse.ArgumentParser(description="Fetch abstracts for placeholders.")
    parser.add_argument("--limit", type=int, default=5, help="Number of abstracts to fetch.")
    parser.add_argument("--output", type=str, default="scratch/fetched_abstracts.json", help="Output JSON file.")
    parser.add_argument("--cards", type=str, help="Comma-separated card IDs to fetch specifically (e.g. src-ckd-163,src-fip-235).")
    args = parser.parse_args()

    placeholders = find_placeholder_papers()
    if not placeholders:
        print("No placeholder papers found.")
        sys.exit(0)

    print(f"Found {len(placeholders)} placeholder cards in raw/papers/.")
    if args.cards:
        card_ids = [c.strip() for c in args.cards.split(",") if c.strip()]
        targets = []
        for cid in card_ids:
            found = False
            for path, orig_meta in placeholders:
                if (orig_meta.get("id") or path.stem) == cid:
                    targets.append((path, orig_meta))
                    found = True
                    break
            if not found:
                print(f"Warning: requested card ID {cid} not found as placeholder.")
    else:
        targets = placeholders[:args.limit]
    print(f"Fetching up to {len(targets)} abstracts...")

    output_path = PROJECT_ROOT / args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)

    results = []
    for path, orig_meta in targets:
        card_id = orig_meta.get("id") or path.stem
        title = orig_meta.get("title")
        doi = ""
        links = orig_meta.get("links")
        if isinstance(links, dict):
            doi = links.get("doi", "")
        elif isinstance(orig_meta.get("doi"), str):
            doi = orig_meta.get("doi")

        pmid = ""
        if orig_meta.get("pmid"):
            pmid = str(orig_meta.get("pmid"))

        print(f"\nProcessing {card_id}: {title[:60]}...")
        abstract, meta = fetch_paper_abstract(title, doi)
        if not abstract:
            print(f"  Failed to retrieve a validated abstract.")
            continue

        # Extract/resolve PMCID
        pmcid = extract_pmcid_from_meta(orig_meta)
        if not pmcid:
            print("  Attempting to resolve PMCID from DOI/PMID...")
            pmcid = resolve_pmcid(meta.get("doi") or doi, pmid)
        
        local_assets = []
        if pmcid:
            print(f"  Found PMCID: {pmcid}")
            parts = card_id.split("-")
            disease = parts[1] if len(parts) >= 2 else "unknown"
            local_assets = download_pmc_figures(pmcid, card_id, disease)
            # Add pmcid to links in metadata
            if "links" not in meta or not isinstance(meta["links"], dict):
                meta["links"] = {}
            meta["links"]["pmc"] = f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/"
            meta["links"]["pmcid"] = pmcid

        results.append({
            "card_id": card_id,
            "file_path": str(path.relative_to(PROJECT_ROOT)),
            "title": title,
            "doi": meta.get("doi") or doi,
            "abstract": abstract,
            "metadata": meta,
            "orig_metadata": orig_meta,
            "local_assets": local_assets
        })

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nSaved {len(results)} fetched abstracts to {args.output}")

if __name__ == "__main__":
    main()
