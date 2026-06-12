"""
Evidence Card management.

Evidence Cards are structured knowledge units that:
- Track species boundaries (cat vs dog/human/mouse)
- Label evidence strength and use cases
- Enable targeted retrieval for research tasks
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Set

from .schemas import (
    EvidenceCard,
    EvidenceStrength,
    SourceType,
    SpeciesType,
    UseCase,
)


class EvidenceCardStore:
    """
    Evidence Card storage and retrieval.

    Extends the existing source card system by adding
    structured evidence metadata for research pipeline use.
    """

    def __init__(self, base_path: Path, source_cards_path: Optional[Path] = None):
        """
        Initialize evidence card store.

        Args:
            base_path: Directory for evidence card JSON storage
            source_cards_path: Optional path to existing source cards (raw/papers/)
        """
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

        self.source_cards_path = Path(source_cards_path) if source_cards_path else None

        # In-memory index for fast lookups
        self._index: Dict[str, EvidenceCard] = {}
        self._load_index()

    def _load_index(self) -> None:
        """Load all evidence cards into memory index."""
        for json_file in self.base_path.glob("*.json"):
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                card = EvidenceCard.from_dict(data)
                self._index[card.evidence_card_id] = card
            except (json.JSONDecodeError, KeyError):
                continue

    def save(self, card: EvidenceCard) -> Path:
        """
        Save an evidence card.

        Args:
            card: Evidence card to save

        Returns:
            Path to saved file
        """
        json_file = self.base_path / f"{card.evidence_card_id}.json"
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(card.to_dict(), f, indent=2, ensure_ascii=False)

        self._index[card.evidence_card_id] = card
        return json_file

    def get(self, card_id: str) -> Optional[EvidenceCard]:
        """
        Get evidence card by ID.

        Args:
            card_id: Evidence card ID

        Returns:
            EvidenceCard if found
        """
        return self._index.get(card_id)

    def search(
        self,
        disease: Optional[str] = None,
        species: Optional[SpeciesType] = None,
        use_cases: Optional[List[UseCase]] = None,
        min_strength: Optional[EvidenceStrength] = None,
        biomarkers: Optional[List[str]] = None,
        limit: int = 50,
    ) -> List[EvidenceCard]:
        """
        Search evidence cards with filters.

        Args:
            disease: Filter by disease
            species: Filter by species (default: cat only)
            use_cases: Filter by any matching use case
            min_strength: Minimum evidence strength
            biomarkers: Filter by any matching biomarker
            limit: Maximum results

        Returns:
            Matching evidence cards
        """
        # Define strength ordering for comparison
        strength_order = {
            EvidenceStrength.LOW: 0,
            EvidenceStrength.MEDIUM: 1,
            EvidenceStrength.HIGH: 2,
        }
        min_strength_value = strength_order.get(min_strength, 0) if min_strength else 0

        results = []
        for card in self._index.values():
            if len(results) >= limit:
                break

            # Apply filters
            if disease and card.disease.lower() != disease.lower():
                continue

            if species and card.species != species:
                continue

            if use_cases:
                if not any(uc in card.use_cases for uc in use_cases):
                    continue

            if min_strength:
                if strength_order.get(card.evidence_strength, 0) < min_strength_value:
                    continue

            if biomarkers:
                card_biomarkers_lower = [b.lower() for b in card.biomarkers]
                if not any(b.lower() in card_biomarkers_lower for b in biomarkers):
                    continue

            results.append(card)

        return results

    def search_for_task(
        self,
        disease: str,
        use_case: UseCase,
        cat_only: bool = True,
    ) -> List[EvidenceCard]:
        """
        Search for evidence relevant to a specific research task.

        Prioritizes cat-specific evidence and higher strength.

        Args:
            disease: Disease to search for
            use_case: Primary use case
            cat_only: Whether to restrict to cat evidence only

        Returns:
            Sorted list of relevant evidence cards
        """
        species_filter = SpeciesType.CAT if cat_only else None

        cards = self.search(
            disease=disease,
            species=species_filter,
            use_cases=[use_case],
        )

        # Sort by evidence strength (high first)
        strength_order = {
            EvidenceStrength.HIGH: 0,
            EvidenceStrength.MEDIUM: 1,
            EvidenceStrength.LOW: 2,
        }

        return sorted(cards, key=lambda c: strength_order.get(c.evidence_strength, 99))

    def create_from_source_card(
        self,
        source_id: str,
        use_cases: List[UseCase],
        key_finding: str,
        biomarkers: Optional[List[str]] = None,
        limitations: str = "",
        evidence_strength: EvidenceStrength = EvidenceStrength.MEDIUM,
    ) -> Optional[EvidenceCard]:
        """
        Create an evidence card from an existing source card.

        Reads metadata from the source card frontmatter and
        creates a structured evidence card.

        Args:
            source_id: Source card ID (e.g., "src-ckd-001")
            use_cases: Evidence use cases
            key_finding: Main finding from this source
            biomarkers: Relevant biomarkers
            limitations: Known limitations
            evidence_strength: Evidence quality level

        Returns:
            Created EvidenceCard, or None if source card not found
        """
        if not self.source_cards_path:
            return None

        # Find source card file
        source_file = self.source_cards_path / f"{source_id}.md"
        if not source_file.exists():
            return None

        # Parse source card frontmatter
        content = source_file.read_text(encoding="utf-8")
        frontmatter = self._parse_frontmatter(content)

        if not frontmatter:
            return None

        # Extract metadata
        title = frontmatter.get("title", source_id)
        species_str = frontmatter.get("species", "cat")
        diseases = frontmatter.get("diseases", [])
        disease = diseases[0] if diseases else ""

        # Map source_kind to SourceType
        source_kind = frontmatter.get("source_kind", "paper")
        source_type_map = {
            "paper": SourceType.PUBMED,
            "thesis": SourceType.THESIS,
            "guideline": SourceType.GUIDELINE,
            "review": SourceType.REVIEW,
        }
        source_type = source_type_map.get(source_kind, SourceType.PUBMED)

        # Map species
        species_map = {
            "feline": SpeciesType.CAT,
            "cat": SpeciesType.CAT,
            "canine": SpeciesType.DOG,
            "dog": SpeciesType.DOG,
            "human": SpeciesType.HUMAN,
            "mouse": SpeciesType.MOUSE,
        }
        species = species_map.get(species_str.lower(), SpeciesType.CAT)

        # Get DOI or other source ID
        links = frontmatter.get("links", {})
        doi = links.get("doi", "")
        external_id = doi if doi else source_id

        # Create evidence card
        card = EvidenceCard(
            evidence_card_id=EvidenceCard.generate_id(),
            title=title,
            source_type=source_type,
            source_id=external_id,
            species=species,
            disease=disease,
            study_type=frontmatter.get("evidence_level", "original-study"),
            biomarkers=biomarkers or [],
            use_cases=use_cases,
            key_finding=key_finding,
            limitations=limitations,
            evidence_strength=evidence_strength,
        )

        # Save the card
        self.save(card)
        return card

    def _parse_frontmatter(self, content: str) -> Optional[Dict]:
        """Parse YAML frontmatter from markdown content."""
        if not content.startswith("---"):
            return None

        # Find end of frontmatter
        end_match = content.find("---", 3)
        if end_match == -1:
            return None

        frontmatter_text = content[3:end_match].strip()

        # Simple YAML parsing (for common frontmatter fields)
        result = {}
        current_key = None
        current_list = None

        for line in frontmatter_text.split("\n"):
            line = line.rstrip()

            # Skip empty lines
            if not line.strip():
                continue

            # List item
            if line.strip().startswith("- "):
                if current_list is not None:
                    value = line.strip()[2:].strip().strip('"').strip("'")
                    current_list.append(value)
                continue

            # Key-value pair
            if ":" in line:
                # Check if this starts a new key
                indent = len(line) - len(line.lstrip())

                if indent == 0:
                    # Top-level key
                    parts = line.split(":", 1)
                    key = parts[0].strip()
                    value = parts[1].strip() if len(parts) > 1 else ""

                    # Remove quotes
                    value = value.strip('"').strip("'")

                    if value == "" or value == "[]":
                        # This might be a list
                        result[key] = []
                        current_key = key
                        current_list = result[key]
                    else:
                        result[key] = value
                        current_key = key
                        current_list = None
                else:
                    # Nested key (like links.doi)
                    if current_key and isinstance(result.get(current_key), dict):
                        pass  # Handle nested dict
                    elif current_key == "links" or (current_key is None and "links" in result):
                        # Nested under links
                        if "links" not in result:
                            result["links"] = {}
                        parts = line.strip().split(":", 1)
                        key = parts[0].strip()
                        value = parts[1].strip().strip('"').strip("'") if len(parts) > 1 else ""
                        result["links"][key] = value

        return result

    def get_species_distribution(self, disease: str) -> Dict[SpeciesType, int]:
        """
        Get distribution of evidence by species for a disease.

        Useful for understanding evidence gaps.

        Args:
            disease: Disease to analyze

        Returns:
            Count of evidence cards by species
        """
        distribution = {species: 0 for species in SpeciesType}

        for card in self._index.values():
            if card.disease.lower() == disease.lower():
                distribution[card.species] += 1

        return distribution

    def get_use_case_coverage(self, disease: str) -> Dict[UseCase, int]:
        """
        Get evidence coverage by use case for a disease.

        Helps identify gaps in evidence for specific purposes.

        Args:
            disease: Disease to analyze

        Returns:
            Count of evidence cards by use case
        """
        coverage = {uc: 0 for uc in UseCase}

        for card in self._index.values():
            if card.disease.lower() == disease.lower():
                for uc in card.use_cases:
                    coverage[uc] += 1

        return coverage

    def count(self) -> int:
        """Return total number of evidence cards."""
        return len(self._index)

    def list_diseases(self) -> Set[str]:
        """List all diseases with evidence cards."""
        return {card.disease for card in self._index.values() if card.disease}
