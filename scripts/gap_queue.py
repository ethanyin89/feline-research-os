#!/usr/bin/env python3
"""
scripts/gap_queue.py — Evidence Gap-to-Intake Queue for feline research OS.

Tracks evidence gaps identified during claim evaluation, with:
- Priority levels (P0, P1, P2)
- Suggested searches
- Status tracking (open, in_progress, resolved)
- Disease filtering

Usage:
    python scripts/gap_queue.py list
    python scripts/gap_queue.py list --disease ckd --priority P1
    python scripts/gap_queue.py add --disease ckd --description "Need phosphate binder RCT" --priority P1
    python scripts/gap_queue.py update GAP-C1 --status resolved
    python scripts/gap_queue.py scan  # Scan opportunity briefs for new gaps

Usage (imported):
    from gap_queue import GapQueue
    queue = GapQueue()
    gaps = queue.list_gaps(disease="ckd", priority="P1")
"""

import argparse
import json
import re
from dataclasses import dataclass, field, asdict
from datetime import date, datetime
from pathlib import Path
from typing import Optional

VAULT_ROOT = Path(__file__).parent.parent
GAP_QUEUE_FILE = VAULT_ROOT / "system" / "indexes" / "gap-to-intake-queue.json"


@dataclass
class GapItem:
    """Single evidence gap."""
    gap_id: str
    disease: str
    description: str
    impact: str
    priority: str  # P0, P1, P2
    suggested_search: str
    status: str  # open, in_progress, resolved
    created_at: str
    created_from: str  # artifact that exposed this gap
    resolved_at: Optional[str] = None
    resolved_by: Optional[str] = None
    notes: str = ""


class GapQueue:
    """Evidence gap tracking queue."""

    def __init__(self, queue_file: Path = GAP_QUEUE_FILE):
        self.queue_file = queue_file
        self.gaps: list[GapItem] = []
        self._load()

    def _load(self) -> None:
        """Load gaps from JSON file."""
        if self.queue_file.exists():
            try:
                data = json.loads(self.queue_file.read_text(encoding="utf-8"))
                self.gaps = [GapItem(**g) for g in data.get("gaps", [])]
            except (json.JSONDecodeError, TypeError):
                self.gaps = []
        else:
            self.gaps = []

    def _save(self) -> None:
        """Save gaps to JSON file."""
        self.queue_file.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "last_updated": datetime.now().isoformat(),
            "total_gaps": len(self.gaps),
            "open_gaps": sum(1 for g in self.gaps if g.status == "open"),
            "gaps": [asdict(g) for g in self.gaps],
        }
        self.queue_file.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def _generate_gap_id(self, disease: str) -> str:
        """Generate a unique gap ID."""
        disease_prefix = disease.upper()[:1]
        existing = [g for g in self.gaps if g.gap_id.startswith(f"GAP-{disease_prefix}")]
        next_num = len(existing) + 1
        return f"GAP-{disease_prefix}{next_num}"

    def add_gap(
        self,
        disease: str,
        description: str,
        impact: str = "",
        priority: str = "P2",
        suggested_search: str = "",
        created_from: str = "manual",
    ) -> GapItem:
        """Add a new gap to the queue."""
        gap_id = self._generate_gap_id(disease)

        # Check for duplicates
        for g in self.gaps:
            if g.disease.lower() == disease.lower() and g.description.lower() == description.lower():
                return g  # Return existing gap

        gap = GapItem(
            gap_id=gap_id,
            disease=disease.upper(),
            description=description,
            impact=impact or f"Weakens {disease.upper()} evidence backbone",
            priority=priority,
            suggested_search=suggested_search or f"Search for {disease} studies on: {description[:30]}",
            status="open",
            created_at=date.today().isoformat(),
            created_from=created_from,
        )
        self.gaps.append(gap)
        self._save()
        return gap

    def update_gap(
        self,
        gap_id: str,
        status: Optional[str] = None,
        priority: Optional[str] = None,
        notes: Optional[str] = None,
        resolved_by: Optional[str] = None,
    ) -> Optional[GapItem]:
        """Update an existing gap."""
        for gap in self.gaps:
            if gap.gap_id == gap_id:
                if status:
                    gap.status = status
                    if status == "resolved":
                        gap.resolved_at = date.today().isoformat()
                if priority:
                    gap.priority = priority
                if notes:
                    gap.notes = notes
                if resolved_by:
                    gap.resolved_by = resolved_by
                self._save()
                return gap
        return None

    def list_gaps(
        self,
        disease: Optional[str] = None,
        priority: Optional[str] = None,
        status: Optional[str] = None,
    ) -> list[GapItem]:
        """List gaps with optional filtering."""
        gaps = self.gaps

        if disease:
            gaps = [g for g in gaps if g.disease.lower() == disease.lower()]
        if priority:
            gaps = [g for g in gaps if g.priority == priority]
        if status:
            gaps = [g for g in gaps if g.status == status]

        # Sort by priority (P0 first) then by date
        priority_order = {"P0": 0, "P1": 1, "P2": 2}
        gaps.sort(key=lambda g: (priority_order.get(g.priority, 99), g.created_at))

        return gaps

    def get_gap(self, gap_id: str) -> Optional[GapItem]:
        """Get a specific gap by ID."""
        for gap in self.gaps:
            if gap.gap_id == gap_id:
                return gap
        return None

    def scan_opportunity_briefs(self) -> list[GapItem]:
        """Scan opportunity briefs for gaps and add to queue."""
        briefs_dir = VAULT_ROOT / "outputs" / "business"
        new_gaps = []

        if not briefs_dir.exists():
            return new_gaps

        for brief_path in briefs_dir.glob("*opportunity-brief*.md"):
            try:
                content = brief_path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue

            # Extract disease from filename or content
            disease_match = re.search(r'disease_branch:\s*(\w+)', content)
            if disease_match:
                disease = disease_match.group(1).upper()
            else:
                # Try to extract from filename
                name_parts = brief_path.stem.split("-")
                disease = name_parts[0].upper() if name_parts else "UNKNOWN"

            # Find Gap-to-Intake Queue table
            in_gap_table = False
            for line in content.splitlines():
                if "Gap-to-Intake Queue" in line or "Gap ID" in line:
                    in_gap_table = True
                    continue

                if in_gap_table and line.startswith("|"):
                    cells = [c.strip() for c in line.split("|")[1:-1]]
                    if len(cells) >= 4 and "---" not in line and cells[0].lower() != "gap id":
                        gap_id = cells[0]
                        description = cells[1].rstrip("...")
                        impact = cells[2].rstrip("...") if len(cells) > 2 else ""
                        priority = cells[3] if len(cells) > 3 else "P2"
                        suggested = cells[4].rstrip("...") if len(cells) > 4 else ""

                        # Add gap if not already exists
                        gap = self.add_gap(
                            disease=disease,
                            description=description,
                            impact=impact,
                            priority=priority,
                            suggested_search=suggested,
                            created_from=brief_path.name,
                        )
                        if gap.gap_id not in [g.gap_id for g in new_gaps]:
                            new_gaps.append(gap)

                elif in_gap_table and line.startswith("## "):
                    break

        return new_gaps

    def get_stats(self) -> dict:
        """Get queue statistics."""
        return {
            "total": len(self.gaps),
            "open": sum(1 for g in self.gaps if g.status == "open"),
            "in_progress": sum(1 for g in self.gaps if g.status == "in_progress"),
            "resolved": sum(1 for g in self.gaps if g.status == "resolved"),
            "by_priority": {
                "P0": sum(1 for g in self.gaps if g.priority == "P0" and g.status != "resolved"),
                "P1": sum(1 for g in self.gaps if g.priority == "P1" and g.status != "resolved"),
                "P2": sum(1 for g in self.gaps if g.priority == "P2" and g.status != "resolved"),
            },
            "by_disease": {},
        }


def format_gap_list(gaps: list[GapItem], verbose: bool = False) -> str:
    """Format a list of gaps for display."""
    if not gaps:
        return "No gaps found."

    lines = [
        "",
        f"{'='*70}",
        f"  EVIDENCE GAP QUEUE ({len(gaps)} items)",
        f"{'='*70}",
        "",
    ]

    current_priority = None
    for gap in gaps:
        if gap.priority != current_priority:
            current_priority = gap.priority
            lines.append(f"### Priority {current_priority}")
            lines.append("")

        status_icon = {"open": "[ ]", "in_progress": "[~]", "resolved": "[x]"}.get(gap.status, "[ ]")
        lines.append(f"{status_icon} {gap.gap_id} | {gap.disease} | {gap.description[:50]}...")

        if verbose:
            lines.append(f"    Impact: {gap.impact[:60]}...")
            lines.append(f"    Search: {gap.suggested_search[:60]}...")
            lines.append(f"    From: {gap.created_from} | Created: {gap.created_at}")
            if gap.notes:
                lines.append(f"    Notes: {gap.notes}")
            lines.append("")

    return "\n".join(lines)


def format_gap_markdown(gaps: list[GapItem]) -> str:
    """Format gaps as markdown table."""
    lines = [
        "# Evidence Gap-to-Intake Queue",
        "",
        f"**Last updated:** {date.today().isoformat()}",
        f"**Total gaps:** {len(gaps)}",
        f"**Open:** {sum(1 for g in gaps if g.status == 'open')}",
        "",
        "## Queue",
        "",
        "| Gap ID | Disease | Priority | Description | Status | Suggested Search |",
        "|--------|---------|----------|-------------|--------|------------------|",
    ]

    for gap in gaps:
        lines.append(f"| {gap.gap_id} | {gap.disease} | {gap.priority} | {gap.description[:40]}... | {gap.status} | {gap.suggested_search[:30]}... |")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Manage evidence gap-to-intake queue.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # list command
    list_parser = subparsers.add_parser("list", help="List gaps")
    list_parser.add_argument("--disease", "-d", help="Filter by disease")
    list_parser.add_argument("--priority", "-p", choices=["P0", "P1", "P2"], help="Filter by priority")
    list_parser.add_argument("--status", "-s", choices=["open", "in_progress", "resolved"], help="Filter by status")
    list_parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed info")
    list_parser.add_argument("--markdown", "-m", action="store_true", help="Output as markdown")

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new gap")
    add_parser.add_argument("--disease", "-d", required=True, help="Disease code")
    add_parser.add_argument("--description", required=True, help="Gap description")
    add_parser.add_argument("--impact", help="Impact if gap not filled")
    add_parser.add_argument("--priority", "-p", choices=["P0", "P1", "P2"], default="P2", help="Priority level")
    add_parser.add_argument("--search", help="Suggested search terms")

    # update command
    update_parser = subparsers.add_parser("update", help="Update a gap")
    update_parser.add_argument("gap_id", help="Gap ID to update")
    update_parser.add_argument("--status", "-s", choices=["open", "in_progress", "resolved"], help="New status")
    update_parser.add_argument("--priority", "-p", choices=["P0", "P1", "P2"], help="New priority")
    update_parser.add_argument("--notes", "-n", help="Add notes")
    update_parser.add_argument("--resolved-by", help="Source that resolved this gap")

    # scan command
    scan_parser = subparsers.add_parser("scan", help="Scan opportunity briefs for gaps")

    # stats command
    stats_parser = subparsers.add_parser("stats", help="Show queue statistics")

    # search command - trigger external search for a gap
    search_parser = subparsers.add_parser("search", help="Search external sources for a gap")
    search_parser.add_argument("gap_id", help="Gap ID to search for")
    search_parser.add_argument("--source", "-s", choices=["pubmed", "crossref", "both"], default="both", help="Search source")
    search_parser.add_argument("--max-results", "-n", type=int, default=5, help="Max results per source")
    search_parser.add_argument("--generate-stubs", "-g", action="store_true", help="Generate intake stubs")

    args = parser.parse_args()
    queue = GapQueue()

    if args.command == "list":
        gaps = queue.list_gaps(
            disease=args.disease,
            priority=args.priority,
            status=args.status,
        )
        if args.markdown:
            print(format_gap_markdown(gaps))
        else:
            print(format_gap_list(gaps, verbose=args.verbose))

    elif args.command == "add":
        gap = queue.add_gap(
            disease=args.disease,
            description=args.description,
            impact=args.impact or "",
            priority=args.priority,
            suggested_search=args.search or "",
            created_from="manual",
        )
        print(f"Added: {gap.gap_id} | {gap.disease} | {gap.description[:50]}...")

    elif args.command == "update":
        gap = queue.update_gap(
            args.gap_id,
            status=args.status,
            priority=args.priority,
            notes=args.notes,
            resolved_by=args.resolved_by,
        )
        if gap:
            print(f"Updated: {gap.gap_id} | status={gap.status} | priority={gap.priority}")
        else:
            print(f"Gap not found: {args.gap_id}")

    elif args.command == "scan":
        new_gaps = queue.scan_opportunity_briefs()
        print(f"Scanned opportunity briefs. Found {len(new_gaps)} gaps.")
        for gap in new_gaps:
            print(f"  {gap.gap_id} | {gap.disease} | {gap.description[:40]}...")

    elif args.command == "stats":
        stats = queue.get_stats()
        print(f"""
Gap Queue Statistics
====================
Total gaps: {stats['total']}
Open: {stats['open']}
In progress: {stats['in_progress']}
Resolved: {stats['resolved']}

By Priority (open/in-progress):
  P0 (critical): {stats['by_priority']['P0']}
  P1 (high): {stats['by_priority']['P1']}
  P2 (normal): {stats['by_priority']['P2']}
""")

    elif args.command == "search":
        gap = queue.get_gap(args.gap_id)
        if not gap:
            print(f"Gap not found: {args.gap_id}")
            return

        # Import external search module
        from external_search import (
            search_pubmed,
            search_crossref,
            ExternalSearchConfig,
            format_search_results_markdown,
            generate_intake_stubs,
        )

        config = ExternalSearchConfig(allow_external=True, max_results=args.max_results)
        search_query = gap.suggested_search or f"feline {gap.disease.lower()} {gap.description}"

        print(f"Searching for gap: {gap.gap_id}")
        print(f"Query: {search_query}")
        print()

        all_results = []

        if args.source in ("pubmed", "both"):
            response = search_pubmed(search_query, config)
            print(format_search_results_markdown(response))
            all_results.extend(response.results)

        if args.source in ("crossref", "both"):
            response = search_crossref(search_query, config)
            print(format_search_results_markdown(response))
            all_results.extend(response.results)

        if args.generate_stubs and all_results:
            stub_paths = generate_intake_stubs(all_results, gap.disease.lower())
            print(f"\n## Generated {len(stub_paths)} intake stubs")
            for path in stub_paths:
                print(f"- {path.relative_to(VAULT_ROOT)}")

            # Update gap status to in_progress
            queue.update_gap(
                args.gap_id,
                status="in_progress",
                notes=f"External search run on {date.today().isoformat()}. {len(stub_paths)} stubs generated.",
            )
            print(f"\nGap {gap.gap_id} status updated to in_progress.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
