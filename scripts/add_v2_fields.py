#!/usr/bin/env python3
"""
scripts/add_v2_fields.py
Add V2 enhanced fields to source cards that don't have them.

Usage:
    python3 scripts/add_v2_fields.py --disease cancer --limit 5
    python3 scripts/add_v2_fields.py --disease hcm --dry-run
    python3 scripts/add_v2_fields.py --file raw/papers/src-hcm-042.md
    python3 scripts/add_v2_fields.py --disease fip --quality-gate  # Block F-grade extractions
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path
from typing import Optional

SCRIPTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

# Load .env if exists
env_file = PROJECT_ROOT / ".env"
if env_file.exists():
    for line in env_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())

# Budget guard - enforce $1/day limit per workspace rules
os.environ["OPENROUTER_DAILY_BUDGET_USD"] = os.environ.get("OPENROUTER_DAILY_BUDGET_USD") or "1.00"

# Verify budget is set
budget = float(os.environ.get("OPENROUTER_DAILY_BUDGET_USD", "1.00"))
if budget > 1.0:
    print(f"WARNING: Budget ${budget} exceeds $1/day limit. Capping to $1.00")
    os.environ["OPENROUTER_DAILY_BUDGET_USD"] = "1.00"

V2_FIELDS = ["study_design", "core_argument", "implicit_premise", "title_gap", "evidence_boundary"]

# Import quality gates (optional, for --quality-gate mode)
try:
    from v2_quality_gates import grade_v2_extraction, V2QualityReport
    QUALITY_GATES_AVAILABLE = True
except ImportError:
    QUALITY_GATES_AVAILABLE = False

def has_v2_fields(content: str) -> bool:
    """Check if a source card already has V2 fields."""
    return "core_argument:" in content and "evidence_boundary:" in content

def find_cards_without_v2(disease: str, limit: int = 10) -> list[Path]:
    """Find source cards that don't have V2 fields."""
    papers_dir = PROJECT_ROOT / "raw" / "papers"
    prefix = f"src-{disease}-"

    candidates = []
    for path in sorted(papers_dir.glob(f"{prefix}*.md")):
        if len(candidates) >= limit:
            break
        try:
            content = path.read_text(encoding="utf-8")
            if not has_v2_fields(content):
                candidates.append(path)
        except Exception:
            continue

    return candidates

def extract_existing_content(content: str) -> dict:
    """Extract existing fields from source card for context."""
    result = {}

    # Title
    title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    if title_match:
        result["title"] = title_match.group(1)

    # Year
    year_match = re.search(r'^year:\s*(\d{4})', content, re.MULTILINE)
    if year_match:
        result["year"] = year_match.group(1)

    # Evidence level
    level_match = re.search(r'^evidence_level:\s*(\S+)', content, re.MULTILINE)
    if level_match:
        result["evidence_level"] = level_match.group(1)

    # One-line summary
    summary_match = re.search(r'##\s*One-Line Summary\s*\n+(.+?)(?:\n\n|\n##|$)', content)
    if summary_match:
        result["one_line_summary"] = summary_match.group(1).strip()

    # Quoted facts
    facts = []
    fact_matches = re.findall(r'quoted_fact:\s*\n((?:\s+-\s*.+\n?)+)', content)
    for match in fact_matches:
        for line in match.strip().split('\n'):
            line = line.strip()
            if line.startswith('- '):
                facts.append(line[2:].strip().strip('"\''))
    result["quoted_facts"] = facts

    # Source supported conclusions
    conclusions = []
    concl_matches = re.findall(r'source_supported_conclusion:\s*\n((?:\s+-\s*.+\n?)+)', content)
    for match in concl_matches:
        for line in match.strip().split('\n'):
            line = line.strip()
            if line.startswith('- '):
                conclusions.append(line[2:].strip().strip('"\''))
    result["conclusions"] = conclusions

    # Abstract (if present in body)
    abstract_match = re.search(r'##\s*Abstract Summary\s*\n+(.+?)(?:\n\n##|\n##|$)', content, re.DOTALL)
    if abstract_match:
        result["abstract_section"] = abstract_match.group(1).strip()[:1000]

    return result

def generate_v2_fields_prompt(existing: dict) -> str:
    """Generate the prompt for V2 field extraction."""
    context_parts = []

    if existing.get("title"):
        context_parts.append(f"Title: {existing['title']}")
    if existing.get("year"):
        context_parts.append(f"Year: {existing['year']}")
    if existing.get("evidence_level"):
        context_parts.append(f"Evidence level: {existing['evidence_level']}")
    if existing.get("one_line_summary"):
        context_parts.append(f"One-line summary: {existing['one_line_summary']}")
    if existing.get("quoted_facts"):
        context_parts.append(f"Quoted facts:\n" + "\n".join(f"- {f}" for f in existing['quoted_facts'][:5]))
    if existing.get("conclusions"):
        context_parts.append(f"Conclusions:\n" + "\n".join(f"- {c}" for c in existing['conclusions'][:3]))
    if existing.get("abstract_section"):
        context_parts.append(f"Abstract section:\n{existing['abstract_section']}")

    context = "\n\n".join(context_parts)

    prompt = f"""Based on this feline veterinary research paper, generate V2 enhanced fields in Chinese.

{context}

Generate these fields (all in Chinese except tension_with which can be empty):

1. study_design: Brief description of research method and cohort
   Format: "研究类型，样本描述，主要方法"
   Example: "回顾性横断面研究，91 只猫按 ACVIM 分期，采用常规及斑点追踪超声心动图"

2. core_argument: The paper's central thesis in one complete sentence
   Must be a specific claim, not a topic description
   Wrong: "这篇论文是关于猫 HCM 的"
   Right: "轻中度左心室肥厚在猫中无法仅靠超声心动图诊断，仍是排除性诊断"

3. implicit_premise: What must be true for the core argument to hold?
   Usually an unstated methodological or theoretical assumption

4. title_gap: Why this paper is worth reading beyond what the title suggests
   Must create specific intellectual tension or curiosity
   Format: "标题说X，但真正发现是Y——..."

5. evidence_boundary: What questions does this paper explicitly NOT answer?
   Must be specific, not generic like "需要更多研究"

6. unexpected_finding: (optional) Any surprising or counter-intuitive result

IMPORTANT: If this is NOT actually a feline study (e.g., "Feline sarcoma-related protein" is a protein name, not species), start study_design with "**误收录警告**：" and explain.

Return ONLY valid YAML with these fields, no markdown code blocks:
study_design: "..."
core_argument: "..."
implicit_premise: "..."
title_gap: "..."
evidence_boundary: "..."
unexpected_finding: "..."
"""
    return prompt

def call_llm(prompt: str) -> Optional[str]:
    """Call OpenRouter to generate V2 fields."""
    try:
        from query import make_client, _chat, OPENROUTER_MODEL

        # Explicitly use openrouter backend
        client = make_client("openrouter")
        if not client:
            print("  ERROR: No API client available")
            return None

        system_prompt = "You are a veterinary research assistant. Generate structured V2 fields for feline research papers."

        response = _chat(
            client,
            OPENROUTER_MODEL,
            system_prompt,
            [{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        # _chat returns the content string directly
        return response if response else None
    except Exception as e:
        print(f"  ERROR: LLM call failed: {e}")
        return None

def parse_v2_response(response: str) -> dict:
    """Parse LLM response into V2 fields dict."""
    fields = {}

    # Clean up response
    response = response.strip()
    if response.startswith("```"):
        response = re.sub(r'^```\w*\n?', '', response)
        response = re.sub(r'\n?```$', '', response)

    for field in V2_FIELDS + ["unexpected_finding"]:
        pattern = rf'{field}:\s*["\']?(.+?)["\']?\s*(?:\n|$)'
        match = re.search(pattern, response, re.MULTILINE)
        if match:
            value = match.group(1).strip().strip('"\'')
            if value and value.lower() not in ("null", "none", "n/a", ""):
                fields[field] = value

    return fields

def insert_v2_fields(content: str, fields: dict) -> str:
    """Insert V2 fields into source card content."""
    # Find the end of evidence_policy section (before ---)
    # We need to insert after llm_inference entries

    # Find llm_inference section end
    llm_match = re.search(r'(llm_inference:\s*\n(?:\s+-\s*.+\n?)*)', content)
    if not llm_match:
        print("  WARNING: Could not find llm_inference section")
        return content

    insert_pos = llm_match.end()

    # Build V2 fields YAML
    v2_yaml_parts = ["  # V2 enhanced fields"]
    for field in V2_FIELDS + ["unexpected_finding"]:
        if field in fields:
            v2_yaml_parts.append(f'  {field}: "{fields[field]}"')

    v2_yaml = "\n".join(v2_yaml_parts) + "\n"

    # Insert
    new_content = content[:insert_pos] + v2_yaml + content[insert_pos:]
    return new_content

def run_quality_gate(fields: dict, existing_facts: list[str]) -> tuple[bool, str, V2QualityReport | None]:
    """
    Run quality gate on extracted V2 fields.

    Returns:
        (should_proceed, message, report)
        - should_proceed: True if extraction passes quality gate
        - message: Human-readable message
        - report: Full quality report
    """
    if not QUALITY_GATES_AVAILABLE:
        return True, "Quality gates not available", None

    # Include quoted_fact for hard_data scoring
    gate_input = fields.copy()
    gate_input["quoted_fact"] = existing_facts

    report = grade_v2_extraction(gate_input)

    if report.overall_grade == "F":
        return False, f"BLOCKED: Grade F (score {report.total_score}/12)", report
    elif report.overall_grade == "C":
        issues = "; ".join(report.issues[:2]) if report.issues else "low quality"
        return True, f"WARNING: Grade C - needs_review ({issues})", report
    else:
        return True, f"PASS: Grade {report.overall_grade} (score {report.total_score}/12)", report


def process_card(path: Path, dry_run: bool = False, quality_gate: bool = False) -> bool:
    """Process a single source card to add V2 fields."""
    print(f"\nProcessing: {path.name}")

    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  ERROR: Could not read file: {e}")
        return False

    if has_v2_fields(content):
        print("  SKIP: Already has V2 fields")
        return False

    # Extract existing content for context
    existing = extract_existing_content(content)
    if not existing.get("title"):
        print("  ERROR: Could not extract title")
        return False

    print(f"  Title: {existing.get('title', 'Unknown')[:60]}...")

    # Generate prompt
    prompt = generate_v2_fields_prompt(existing)

    if dry_run:
        print("  DRY RUN: Would call LLM to generate V2 fields")
        print(f"  Context: {len(existing.get('quoted_facts', []))} facts, {len(existing.get('conclusions', []))} conclusions")
        return True

    # Call LLM
    print("  Calling LLM...")
    response = call_llm(prompt)
    if not response:
        print("  ERROR: No response from LLM")
        return False

    # Parse response
    fields = parse_v2_response(response)
    if not fields.get("core_argument") or not fields.get("evidence_boundary"):
        print(f"  ERROR: Missing required fields. Got: {list(fields.keys())}")
        return False

    print(f"  Generated {len(fields)} V2 fields")

    # Quality gate check
    if quality_gate:
        should_proceed, message, report = run_quality_gate(
            fields, existing.get("quoted_facts", [])
        )
        print(f"  Quality Gate: {message}")

        if not should_proceed:
            print("  BLOCKED: Extraction did not meet quality standards")
            if report and report.recommendations:
                print("  Recommendations:")
                for rec in report.recommendations:
                    print(f"    - {rec}")
            return False

        # Add needs_review flag for C-grade extractions
        if report and report.overall_grade == "C":
            fields["needs_review"] = "true"

    # Insert fields
    new_content = insert_v2_fields(content, fields)

    # Verify insertion
    if not has_v2_fields(new_content):
        print("  ERROR: V2 fields not properly inserted")
        return False

    # Write back
    try:
        path.write_text(new_content, encoding="utf-8")
        grade_info = ""
        if quality_gate and QUALITY_GATES_AVAILABLE:
            _, _, report = run_quality_gate(fields, existing.get("quoted_facts", []))
            if report:
                grade_info = f" [Grade: {report.overall_grade}]"
        print(f"  SUCCESS: V2 fields added{grade_info}")
        return True
    except Exception as e:
        print(f"  ERROR: Could not write file: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Add V2 enhanced fields to source cards")
    parser.add_argument("--disease", type=str, help="Disease to process (e.g., hcm, ckd, cancer)")
    parser.add_argument("--file", type=str, help="Specific file to process")
    parser.add_argument("--limit", type=int, default=5, help="Max cards to process (default: 5)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without making changes")
    parser.add_argument("--quality-gate", action="store_true",
                        help="Enable quality gate: block F-grade extractions, mark C-grade with needs_review")

    args = parser.parse_args()

    if args.quality_gate and not QUALITY_GATES_AVAILABLE:
        print("WARNING: Quality gates requested but v2_quality_gates.py not available")

    if args.file:
        path = Path(args.file)
        if not path.is_absolute():
            path = PROJECT_ROOT / path
        if not path.exists():
            print(f"ERROR: File not found: {path}")
            return 1

        success = process_card(path, dry_run=args.dry_run, quality_gate=args.quality_gate)
        return 0 if success else 1

    if not args.disease:
        print("ERROR: Must specify --disease or --file")
        return 1

    # Find cards without V2 fields
    cards = find_cards_without_v2(args.disease, limit=args.limit)

    if not cards:
        print(f"No cards without V2 fields found for {args.disease}")
        return 0

    print(f"Found {len(cards)} cards without V2 fields for {args.disease}")
    if args.quality_gate:
        print("Quality gate ENABLED: F-grade extractions will be blocked")

    success_count = 0
    blocked_count = 0
    for card in cards:
        result = process_card(card, dry_run=args.dry_run, quality_gate=args.quality_gate)
        if result:
            success_count += 1
        elif args.quality_gate:
            # Count blocked separately from other failures
            blocked_count += 1

    print(f"\n{'=' * 50}")
    if args.quality_gate:
        print(f"Processed: {len(cards)} | Success: {success_count} | Blocked: {blocked_count} | Other failures: {len(cards) - success_count - blocked_count}")
    else:
        print(f"Processed: {len(cards)} | Success: {success_count} | Failed: {len(cards) - success_count}")

    return 0 if success_count == len(cards) else 1

if __name__ == "__main__":
    sys.exit(main())
