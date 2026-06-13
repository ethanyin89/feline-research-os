#!/usr/bin/env python3
import re
from pathlib import Path
from collections import Counter, defaultdict
from datetime import date

VAULT_ROOT = Path(__file__).parent.parent.resolve()
DISEASES = ["ckd", "fip", "hcm", "ibd", "diabetes", "fcv", "obesity", "cancer"]

def parse_frontmatter(text: str) -> dict:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    fm_text = match.group(1)
    fm = {}
    for line in fm_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        if line.startswith(" ") or line.startswith("\t"):
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        if val.startswith("[") and val.endswith("]"):
            val = [x.strip() for x in val[1:-1].split(",") if x.strip()]
        fm[key] = val
    return fm

def scan_sources():
    sources = defaultdict(list)
    for disease in DISEASES:
        pattern = f"src-{disease}-*.md"
        cards = sorted((VAULT_ROOT / "raw" / "papers").glob(pattern))
        for card in cards:
            text = card.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            sources[disease].append({
                "id": fm.get("id", card.stem),
                "title": fm.get("title", "No Title"),
                "evidence_level": fm.get("evidence_level", "original-study"),
                "extraction_depth": fm.get("extraction_depth", "missing"),
                "verification_status": fm.get("verification_status", "missing"),
                "year": fm.get("year", ""),
                "status": fm.get("status", "")
            })
    return sources

def sync_ckd_index(ckd_sources):
    path = VAULT_ROOT / "system" / "indexes" / "ckd-source-index.md"
    
    seed_sources = []
    extension_sources = []
    
    for s in ckd_sources:
        match = re.search(r"src-ckd-(\d+)", s["id"])
        if match:
            num = int(match.group(1))
            if num <= 24:
                seed_sources.append(s)
            else:
                extension_sources.append(s)
        else:
            extension_sources.append(s)
            
    today_str = date.today().isoformat()
    
    lines = [
        "# CKD Source Index",
        "",
        "## Seed Corpus",
        "",
        "| ID | Title | Primary Layer | Evidence Level | Status |",
        "|---|---|---|---|---|",
    ]
    
    seed_info = {
        "src-ckd-001": ("mechanism", "review", "deep-extracted round 1"),
        "src-ckd-002": ("endpoint", "review", "deep-extracted round 1"),
        "src-ckd-003": ("translation", "review", "deep-extracted round 1"),
        "src-ckd-004": ("regulatory", "guideline", "deep-extracted round 1"),
        "src-ckd-005": ("translation", "review", "deep-extracted round 1"),
        "src-ckd-006": ("translation", "review", "deep-extracted round 1"),
        "src-ckd-007": ("translation", "review", "deep-extracted round 1"),
        "src-ckd-008": ("translation", "review", "deep-extracted round 1"),
        "src-ckd-009": ("translation", "review", "deep-extracted round 1"),
        "src-ckd-010": ("mechanism", "original-study", "deep-extracted round 1"),
        "src-ckd-011": ("mechanism", "review", "deep-extracted round 1"),
        "src-ckd-012": ("mechanism", "original-study", "deep-extracted round 1"),
        "src-ckd-013": ("translation", "review", "deep-extracted round 1"),
        "src-ckd-014": ("translation", "original-study", "deep-extracted round 1"),
        "src-ckd-015": ("mechanism", "review", "deep-extracted round 1"),
        "src-ckd-016": ("mechanism", "review", "deep-extracted round 1"),
        "src-ckd-017": ("mechanism", "original-study", "deep-extracted round 1"),
        "src-ckd-018": ("endpoint", "original-study", "deep-extracted round 1"),
        "src-ckd-019": ("translation", "review", "deep-extracted round 1"),
        "src-ckd-020": ("model", "review", "deep-extracted round 1"),
        "src-ckd-021": ("mechanism", "review", "deep-extracted round 1"),
        "src-ckd-022": ("model", "original-study", "deep-extracted round 1"),
        "src-ckd-023": ("mechanism", "original-study", "deep-extracted round 1"),
        "src-ckd-024": ("endpoint", "review", "deep-extracted round 1"),
    }
    
    for s in seed_sources:
        info = seed_info.get(s["id"], ("mechanism", "original-study", "deep-extracted round 1"))
        lines.append(f"| {s['id']} | {s['title']} | {info[0]} | {info[1]} | {info[2]} |")
        
    lines.extend([
        "",
        f"## Extension Intake Queue, Updated {today_str}",
        "",
        "These source cards came from the user-provided `feline CKD` Google Sheet. They are source-ownership and triage material only until abstract extraction, source worksheet review, or full-text extraction is complete.",
        "",
        "| ID | Title | Evidence Level | Extraction Depth | Verification Status | Year |",
        "|---|---|---|---|---|---|",
    ])
    
    for s in extension_sources:
        title_esc = s['title'].replace("|", "\\|")
        lines.append(f"| {s['id']} | {title_esc} | {s['evidence_level']} | {s['extraction_depth']} | {s['verification_status']} | {s['year']} |")
        
    lines.extend([
        "",
        "Blocked sheet row:",
        "",
        "- row 51, `The nutritional management of feline chronic kidney disease`, has no locator and must not become a source card until URL, DOI, PubMed ID, or another durable locator is recovered.",
        "",
        "Structured abstract follow-up:",
        "",
        "- `system/indexes/feline-ckd-extension-structured-abstract-20260605.md`",
        "- `system/indexes/feline-ckd-extension-pubmed-fallback-20260606.md`",
        "- `system/indexes/feline-ckd-extension-structured-abstract-pubmed-20260606.md`",
        "- `system/indexes/feline-ckd-extension-claim-fit-queue-20260605.md`",
        f"- Round-1 structured abstract worksheets exist for {len([x for x in extension_sources if x['verification_status'] == 'abstract_weighted'])} extension cards.",
        "- **Full abstract extraction (round 2) completed 2026-06-05 for `src-ckd-026` and `src-ckd-034`**; these now have `source_checked` status and promoted claim cards.",
        "- **Full-text deep extraction completed 2026-06-06 for `src-ckd-027` and `src-ckd-029`**. These control metabolomics branch mapping and a guarded phosphate-supplement evidence boundary, respectively.",
        "- **Full-text deep extraction completed 2026-06-06 for `src-ckd-030`**. It controls probiotic-pilot and microbiome-intervention limits, not efficacy guidance.",
        "- **Full-text deep extraction completed 2026-06-06 for `src-ckd-050`**. It anchors the primary feline renal fibroblast model and direct in-vitro TGF-beta evidence.",
        "- Cross-source boundary memo: `system/indexes/ckd-uremic-toxin-microbiome-bridge-memo-20260606.md`.",
        "",
        "## Notes",
        "",
        "- `deep-extracted round 1` means a first worksheet now exists in `system/indexes/`",
        "- `abstract_weighted` extension rows can guide extraction priority only; they are not decision-grade evidence.",
        "- `src-ckd-032` remains `title_only` because PMID `24783628` has no PubMed abstract and no DOI was recovered.",
        "- `src-ckd-047` has an open-manuscript repository lead but direct access was blocked by a Cloudflare challenge; keep it `abstract_weighted`.",
        "- `src-ckd-049` remains `abstract_weighted` because only abstract text was available.",
        "",
        "## Current Status Note",
        "",
        "The CKD seed source corpus is fully processed across the original 24-source seed list.",
        "",
        f"That means CKD is no longer split between deep-read and source-card-only layers inside the seed corpus. CKD also has {len(extension_sources)} extension intake cards ({seed_sources[0]['id']} through {extension_sources[-1]['id'] if extension_sources else ''}) from the Google Sheet; four now have selective full-text deep extraction.",
        "",
        "The next gains should come from:",
        "",
        "- denser write-back into topic pages",
        "- narrower control compression",
        "- selective new-source ingest beyond the current 24-source seed boundary",
    ])
    
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Synced {path.name}")

def sync_global_depth_map(sources_by_disease):
    path = VAULT_ROOT / "system" / "indexes" / "source-depth-map.md"
    today_str = date.today().isoformat()
    total_papers = sum(len(lst) for lst in sources_by_disease.values())
    
    snapshot_rows = []
    coverage_rows = []
    year_rows = []
    
    for disease in DISEASES:
        sources = sources_by_disease[disease]
        total = len(sources)
        
        depths = Counter(s["extraction_depth"] for s in sources)
        exp_full = depths.get("full", 0) + depths.get("abstract_full", 0) + depths.get("deep", 0)
        exp_partial = depths.get("partial", 0)
        missing_depth = depths.get("missing", 0) + depths.get("abstract", 0)
        
        verifs = Counter(s["verification_status"] for s in sources)
        
        status_reality = ", ".join(f"{count} {status}" for status, count in sorted(verifs.items()))
        
        if disease == "ckd":
            worksheets = "24 seed worksheets plus 31 extension worksheets (25 structured round 1 + 2 abstract round 2 + 4 full-text deep extractions)"
            current_read = "Seed corpus remains mature; full-text extension depth now covers metabolomics, guarded phosphorus intervention, probiotic-pilot boundaries, and a feline fibroblast/TGF-beta model"
        elif disease == "fip":
            worksheets = "24"
            current_read = "Separate FIP depth map exists; all source cards now explicit full depth"
        elif disease == "hcm":
            worksheets = "24"
            current_read = "Separate HCM depth map exists; all source cards now explicit full depth and deep-extracted"
        elif disease == "ibd":
            worksheets = "24"
            current_read = "Separate IBD depth map exists; all source cards are explicit full and deep-extracted"
        elif disease == "diabetes":
            worksheets = "24 seed worksheets plus extension structured-abstract worksheets where available"
            current_read = "Seed corpus is full; extension corpus is navigation/source-check material only, not compiled decision-grade evidence"
        elif disease == "fcv":
            worksheets = "24"
            current_read = "Separate FCV depth map exists; core source-card layer is full, but image assets and output-level branches remain thinner"
        elif disease == "obesity":
            worksheets = "44 structured-abstract worksheets, 43 title-only cards, 4 deep extraction worksheets"
            current_read = "All 4 Tier 1 priority cards deep-extracted (001, 004, 005, 008); 5-branch architecture complete with 4 pages + 4 bilingual versions"
        elif disease == "cancer":
            worksheets = "29 structured-abstract worksheets, 43 deep extraction worksheets"
            current_read = "Core oncology branches outlined; most high-visibility cancer sources Triaged and verified"
        else:
            worksheets = "TBD"
            current_read = "No custom notes"
            
        snapshot_rows.append(
            f"| {disease.upper()} | {total} | `{status_reality}` | {exp_full} | {exp_partial} | {missing_depth} | {worksheets} | `{status_reality}` | {current_read} |"
        )
        
        coverage_rows.append(
            f"| {disease.upper()} | {total} | {exp_full} | {exp_partial} | {missing_depth} | {depths.get('stub', 0)} | {current_read} |"
        )
        
        with_year = sum(1 for s in sources if s["year"])
        year_rows.append(
            f"| {disease.upper()} | {with_year}/{total} ({int(with_year/total*100) if total > 0 else 0}%) | Complete |"
        )
        
    content = path.read_text(encoding="utf-8")
    
    content = re.sub(r"last_compiled_at:\s*\d{4}-\d{2}-\d{2}", f"last_compiled_at: {today_str}", content)
    
    content = re.sub(
        r"The vault now has `\d+` strict disease paper source cards",
        f"The vault now has `{total_papers}` strict disease paper source cards",
        content
    )
    
    content = re.sub(
        r"\d{4}-\d{2}-\d{2} reality sync:",
        f"{today_str} reality sync:",
        content
    )
    
    snapshot_table_pattern = r"(## \d{4}-\d{2}-\d{2} Cross-Disease Snapshot\n\n\| Disease \| Source cards \|.*?)(?=\n\n## Default Next Moves|\n\n---)"
    new_snapshot_table = (
        f"## {today_str} Cross-Disease Snapshot\n\n"
        "| Disease | Source cards | Status reality | Explicit full | Explicit partial | Missing depth field | Worksheets | Verification-status overlay | Current read |\n"
        "|---|---|---|---|---|---|---|---|---|\n"
        + "\n".join(snapshot_rows)
    )
    content = re.sub(snapshot_table_pattern, new_snapshot_table, content, flags=re.DOTALL)
    
    coverage_table_pattern = r"(## Coverage Summary\n\n.*?\| Disease \| Total Source Cards \|.*?)(?=\n\n---)"
    new_coverage_table = (
        "## Coverage Summary\n\n"
        "This summary uses explicit `extraction_depth` fields only. It intentionally does not treat missing fields as `stub`; missing fields are schema debt that must be resolved against the completed worksheets.\n\n"
        "| Disease | Total Source Cards | explicit full | explicit partial | missing depth | stub | Coverage read |\n"
        "|---|---|---|---|---|---|---|\n"
        + "\n".join(coverage_rows)
    )
    content = re.sub(coverage_table_pattern, new_coverage_table, content, flags=re.DOTALL)
    
    year_table_pattern = r"(## Year Metadata Coverage.*?\n\n\| Disease \| Year Coverage \|.*?)(?=\n\nYear metadata enables)"
    new_year_table = (
        "## Year Metadata Coverage\n\n"
        "| Disease | Year Coverage | Notes |\n"
        "|---|---|---|\n"
        + "\n".join(year_rows)
    )
    content = re.sub(year_table_pattern, new_year_table, content, flags=re.DOTALL)
    
    path.write_text(content, encoding="utf-8")
    print(f"Synced {path.name}")

def main():
    sources = scan_sources()
    sync_ckd_index(sources["ckd"])
    sync_global_depth_map(sources)

if __name__ == "__main__":
    main()
