"""Strict adapters from approved Markdown shapes to presentation models."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from core.result_presentation import ResultPresentation, build_result_presentation
from core.source_metadata import (
    frontmatter_list,
    frontmatter_scalar,
    load_source_metadata,
)


PROVENANCE_RE = re.compile(
    r"\[(quoted_fact|source_supported_conclusion):\s*([^\]]+)\]"
    r"|\[(llm_inference)\]"
)


@dataclass
class RankedIntervention:
    name: str
    summary: str
    supported_use: str
    overclaim_boundary: str


@dataclass
class RankedTier:
    rank: int
    title: str
    interventions: list[RankedIntervention] = field(default_factory=list)


@dataclass
class RankedPresentation:
    base: ResultPresentation
    tiers: list[RankedTier]

    def validate(self) -> list[str]:
        errors = self.base.validate()
        expected = list(range(1, len(self.tiers) + 1))
        actual = [tier.rank for tier in self.tiers]
        if actual != expected:
            errors.append(f"Ranked tiers are not contiguous: {actual}")
        for tier in self.tiers:
            for intervention in tier.interventions:
                if not intervention.supported_use:
                    errors.append(f"{intervention.name}: missing supported use")
                if not intervention.overclaim_boundary:
                    errors.append(f"{intervention.name}: missing overclaim boundary")
        return errors


def _markdown_body(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    return text[end + 4:].lstrip() if end != -1 else text


def _section(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)",
        re.M | re.S,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def _strip_markdown_emphasis(text: str) -> str:
    return re.sub(r"\*\*(.*?)\*\*", r"\1", text).strip()


def _primary_language_content(text: str, language: str) -> str:
    blocks = [block.strip() for block in re.split(r"\n\s*\n", text) if block.strip()]
    if language == "zh":
        blocks = [block for block in blocks if re.search(r"[\u3400-\u9fff]", block)]
    return "\n\n".join(blocks)


def _extract_provenance(text: str) -> tuple[str, list[dict]]:
    claims = []
    citations = []

    def replace(match: re.Match) -> str:
        provenance = match.group(1) or match.group(3)
        source_ids = []
        if match.group(2):
            source_ids = [
                item.strip()
                for item in match.group(2).split(",")
                if item.strip()
            ]
        claims.append({"provenance": provenance, "source_ids": source_ids})
        for source_id in source_ids:
            citations.append({"source_ref": source_id, "provenance": provenance})
        return ""

    cleaned = PROVENANCE_RE.sub(replace, text)
    return re.sub(r"\n{3,}", "\n\n", cleaned).strip(), claims, citations


def _presentation_fields(text: str, expected_surface: str) -> dict[str, str]:
    surface = frontmatter_scalar(text, "presentation_surface")
    if surface != expected_surface:
        raise ValueError(
            f"Expected presentation_surface={expected_surface!r}, got {surface!r}"
        )
    fields = {
        "title": frontmatter_scalar(text, "presentation_title"),
        "subtitle": frontmatter_scalar(text, "presentation_subtitle"),
        "language": frontmatter_scalar(text, "presentation_language") or "zh",
        "lead_section": frontmatter_scalar(text, "presentation_lead_section"),
        "boundary_section": frontmatter_scalar(text, "presentation_boundary_section"),
        "topic": frontmatter_scalar(text, "topic") or "feline-research",
    }
    missing = [key for key, value in fields.items() if not value]
    if missing:
        raise ValueError(f"Missing presentation frontmatter: {', '.join(missing)}")
    return fields


def build_overview_presentation(path: Path, vault_root: Path) -> ResultPresentation:
    text = path.read_text(encoding="utf-8")
    fields = _presentation_fields(text, "overview")
    body = _markdown_body(text)
    source_ids = frontmatter_list(text, "source_ids")
    if not source_ids:
        raise ValueError("Overview presentation requires source_ids")

    lead_raw = _section(body, fields["lead_section"])
    boundary_raw = _section(body, fields["boundary_section"])
    if not lead_raw or not boundary_raw:
        raise ValueError("Overview lead or boundary section is missing")

    lead_clean, lead_claims, lead_citations = _extract_provenance(
        _primary_language_content(lead_raw, fields["language"])
    )
    boundary_clean, _, _ = _extract_provenance(
        _primary_language_content(boundary_raw, fields["language"])
    )

    configured_headings = frontmatter_list(text, "presentation_sections")
    sections = []
    claims = list(lead_claims)
    for heading in configured_headings:
        raw = _section(body, heading)
        if not raw:
            raise ValueError(f"Configured overview section is missing: {heading}")
        cleaned, section_claims, citations = _extract_provenance(
            _primary_language_content(raw, fields["language"])
        )
        claims.extend(section_claims)
        sections.append({
            "title": heading.split(" / ", 1)[0],
            "content": cleaned,
            "citations": citations,
        })

    sources = load_source_metadata(vault_root, source_ids)
    presentation = build_result_presentation(
        title=fields["title"],
        subtitle=fields["subtitle"],
        lead=lead_clean,
        sources=sources,
        claims=claims,
        sections=sections,
        boundary_notice=boundary_clean,
        topic=fields["topic"].upper(),
        surface_type="overview",
        language=fields["language"],
    )
    for citation in lead_citations:
        matching = next(
            (card for card in presentation.source_cards if card._internal_id == citation["source_ref"]),
            None,
        )
        if matching:
            from core.result_presentation import build_inline_citation

            presentation.inline_citations.append(
                build_inline_citation(matching, citation["provenance"])
            )
    return presentation


def _labeled_value(content: str, label: str) -> str:
    pattern = re.compile(
        rf"^{re.escape(label)}:\s*$\n(.*?)(?=^[A-Z][A-Za-z ]+:\s*$|\Z)",
        re.M | re.S,
    )
    match = pattern.search(content)
    if not match:
        return ""
    value = match.group(1).strip()
    value = re.sub(r"^\s*-\s*", "", value, flags=re.M)
    return _strip_markdown_emphasis(value)


def build_ranked_presentation(path: Path, vault_root: Path) -> RankedPresentation:
    text = path.read_text(encoding="utf-8")
    fields = _presentation_fields(text, "ranked")
    body = _markdown_body(text)
    source_ids = frontmatter_list(text, "source_ids")
    if not source_ids:
        raise ValueError("Ranked presentation requires source_ids")

    lead = _section(body, fields["lead_section"])
    boundary = _section(body, fields["boundary_section"])
    if not lead or not boundary:
        raise ValueError("Ranked lead or boundary section is missing")

    tier_matches = list(re.finditer(r"^## Tier ([1-4]):\s*(.+?)\s*$", body, re.M))
    if len(tier_matches) != 4:
        raise ValueError("Ranked presentation requires exactly four tiers")

    tiers = []
    for index, tier_match in enumerate(tier_matches):
        next_heading = re.search(r"^## (?!Tier )", body[tier_match.end():], re.M)
        next_non_tier_heading = (
            tier_match.end() + next_heading.start()
            if next_heading
            else len(body)
        )
        tier_end = (
            min(tier_matches[index + 1].start(), next_non_tier_heading)
            if index + 1 < len(tier_matches)
            else next_non_tier_heading
        )
        tier_body = body[tier_match.end():tier_end]
        intervention_matches = list(re.finditer(r"^### (.+?)\s*$", tier_body, re.M))
        interventions = []
        for item_index, item_match in enumerate(intervention_matches):
            item_end = (
                intervention_matches[item_index + 1].start()
                if item_index + 1 < len(intervention_matches)
                else len(tier_body)
            )
            item_body = tier_body[item_match.end():item_end].strip()
            supported_use = _labeled_value(item_body, "Supported use")
            boundary_text = _labeled_value(item_body, "Do not overclaim")
            summary = item_body.split("Supported use:", 1)[0].strip()
            summary = re.sub(r"^\s*-\s*", "", summary, flags=re.M)
            interventions.append(RankedIntervention(
                name=item_match.group(1).strip(),
                summary=summary,
                supported_use=supported_use,
                overclaim_boundary=boundary_text,
            ))
        tiers.append(RankedTier(
            rank=int(tier_match.group(1)),
            title=tier_match.group(2).strip(),
            interventions=interventions,
        ))

    sources = load_source_metadata(vault_root, source_ids)
    base = build_result_presentation(
        title=fields["title"],
        subtitle=fields["subtitle"],
        lead=lead,
        sources=sources,
        boundary_notice=boundary,
        topic=fields["topic"].upper(),
        surface_type="ranked",
        language=fields["language"],
        audience="professional",
    )
    return RankedPresentation(base=base, tiers=tiers)
