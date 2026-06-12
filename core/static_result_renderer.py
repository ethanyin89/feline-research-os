"""Dependency-free deterministic HTML rendering for static result fixtures."""

from __future__ import annotations

import html
import re
from html.parser import HTMLParser

from core.result_presentation import ResultPresentation
from core.static_result_adapter import RankedPresentation


class _VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def visible_text(document: str) -> str:
    parser = _VisibleTextParser()
    parser.feed(document)
    return " ".join(parser.parts)


def validate_visible_html(document: str) -> list[str]:
    text = visible_text(document)
    forbidden = {
        "internal source ID": r"\bsrc-[a-z0-9-]+-\d+\b",
        "raw verification status": r"\b(?:deep_extracted|abstract_weighted|source_checked|title_only)\b",
        "raw provenance type": r"\b(?:quoted_fact|source_supported_conclusion|llm_inference)\b",
    }
    return [
        f"Rendered HTML contains {label}"
        for label, pattern in forbidden.items()
        if re.search(pattern, text, re.I)
    ]


def _inline_markdown(value: str) -> str:
    escaped = html.escape(value)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)


def _markdown_block(value: str) -> str:
    blocks = []
    lines = value.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue
        heading = re.match(r"^(#{3,6})\s+(.+)$", line)
        if heading:
            level = min(len(heading.group(1)), 4)
            blocks.append(f"<h{level}>{_inline_markdown(heading.group(2))}</h{level}>")
            index += 1
            continue
        if line.startswith("|") and index + 1 < len(lines) and re.match(r"^\|?[\s:|-]+\|?$", lines[index + 1].strip()):
            rows = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
                rows.append(cells)
                index += 1
            header = rows[0]
            body = rows[2:] if len(rows) > 1 else []
            table = ["<div class='table-wrap'><table><thead><tr>"]
            table.extend(f"<th>{_inline_markdown(cell)}</th>" for cell in header)
            table.append("</tr></thead><tbody>")
            for row in body:
                table.append("<tr>")
                table.extend(
                    f"<td data-label='{html.escape(header[cell_index] if cell_index < len(header) else '')}'>"
                    f"{_inline_markdown(cell)}</td>"
                    for cell_index, cell in enumerate(row)
                )
                table.append("</tr>")
            table.append("</tbody></table></div>")
            blocks.append("".join(table))
            continue
        if re.match(r"^(?:-|\d+\.)\s+", line):
            items = []
            ordered = bool(re.match(r"^\d+\.", line))
            while index < len(lines) and re.match(r"^(?:-|\d+\.)\s+", lines[index].strip()):
                item = re.sub(r"^(?:-|\d+\.)\s+", "", lines[index].strip())
                items.append(f"<li>{_inline_markdown(item)}</li>")
                index += 1
            tag = "ol" if ordered else "ul"
            blocks.append(f"<{tag}>{''.join(items)}</{tag}>")
            continue
        paragraph = [line]
        index += 1
        while index < len(lines) and lines[index].strip() and not lines[index].strip().startswith("|"):
            if re.match(r"^(?:-|\d+\.)\s+", lines[index].strip()):
                break
            paragraph.append(lines[index].strip())
            index += 1
        blocks.append(f"<p>{_inline_markdown(' '.join(paragraph))}</p>")
    return "".join(blocks)


def _source_cards(presentation: ResultPresentation) -> str:
    cards = []
    for card in presentation.source_cards:
        if card.has_valid_link():
            link = (
                f"<a href='{html.escape(card.canonical_url or '')}' "
                "target='_blank' rel='noopener'>"
                f"{html.escape(card.get_link_text())}</a>"
            )
        else:
            link = "<span>链接不可用</span>"
        year = f" · {card.publication_year}" if card.publication_year else ""
        metadata_bits = []
        if card.source_family_label:
            metadata_bits.append(f"家族：{html.escape(card.source_family_label)}")
        if card.species_label:
            metadata_bits.append(f"种属：{html.escape(card.species_label)}")
        if card.decision_grade_label:
            metadata_bits.append(f"决策：{html.escape(card.decision_grade_label)}")
        if card.safest_use:
            metadata_bits.append(f"最安全用途：{html.escape(card.safest_use)}")
        if not metadata_bits and card.publish_date:
            metadata_bits.append(f"发布日期：{html.escape(card.publish_date)}")
        metadata_line = ""
        if metadata_bits:
            metadata_line = (
                "<p class='source-meta'>"
                + " · ".join(metadata_bits)
                + "</p>"
            )
        cards.append(
            "<article class='source-card'>"
            f"<h3>{html.escape(card.title)}</h3>"
            f"<p>{html.escape(card.evidence_depth_label)} · "
            f"{html.escape(card.source_type_label)}{year} · {link}</p>"
            f"{metadata_line}"
            "</article>"
        )
    return "".join(cards)


def _shell(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<style>
:root {{ color-scheme: dark; font-family: Geist, system-ui, sans-serif; }}
body {{ margin:0; background:#0f1117; color:#e8eaf0; line-height:1.7; }}
main {{ width:min(720px, calc(100% - 32px)); margin:0 auto; padding:40px 0 64px; }}
h1,h2,h3 {{ line-height:1.25; }}
.subtitle,.meta,.source-card p {{ color:#8b90a0; }}
.source-meta {{ color:#8b90a0; font-size:0.9em; margin-top:-4px; }}
.profile,.boundary,.source-card,.tier,.intervention {{ border:1px solid #2d3147; background:#1a1d27; border-radius:8px; padding:16px; margin:16px 0; }}
.tier {{ background:#151822; }}
.intervention {{ background:#1a1d27; }}
.supported {{ border-left:3px solid #16a34a; padding-left:12px; }}
.boundary-copy {{ border-left:3px solid #ca8a04; padding-left:12px; }}
.table-wrap {{ overflow-x:auto; }}
table {{ width:100%; border-collapse:collapse; min-width:520px; }}
th,td {{ border:1px solid #2d3147; padding:8px; text-align:left; vertical-align:top; }}
a {{ color:#e8eaf0; }}
@media (max-width:480px) {{
  main {{ width:min(100% - 24px, 720px); padding-top:24px; }}
  .profile,.boundary,.source-card,.tier,.intervention {{ padding:12px; }}
  table {{ min-width:0; }}
  thead {{ display:none; }}
  tbody,tr,td {{ display:block; width:auto; }}
  tr {{ border:1px solid #2d3147; margin:0 0 10px; }}
  td {{ border:0; border-bottom:1px solid #2d3147; padding-left:42%; position:relative; }}
  td:last-child {{ border-bottom:0; }}
  td::before {{
    content:attr(data-label);
    position:absolute;
    left:8px;
    width:36%;
    color:#8b90a0;
    font-weight:600;
  }}
}}
</style>
</head>
<body><main>{body}</main></body></html>"""


def render_overview(presentation: ResultPresentation) -> str:
    errors = presentation.validate()
    if errors:
        raise ValueError("; ".join(errors))
    sections = "".join(
        f"<section><h2>{html.escape(section.title)}</h2>{_markdown_block(section.content)}</section>"
        for section in presentation.sections
    )
    body = (
        f"<header><h1>{html.escape(presentation.context.title)}</h1>"
        f"<p class='subtitle'>{html.escape(presentation.context.subtitle)}</p></header>"
        f"<div class='profile'>{html.escape(presentation.evidence_profile.get_summary_text())}</div>"
        f"<section>{_markdown_block(presentation.lead)}</section>"
        f"{sections}"
        f"<section><h2>来源文献</h2>{_source_cards(presentation)}</section>"
        f"<section class='boundary'><h2>本页边界</h2>{_markdown_block(presentation.boundary_notice)}</section>"
    )
    document = _shell(presentation.context.title, body)
    errors = validate_visible_html(document)
    if errors:
        raise ValueError("; ".join(errors))
    return document


def render_ranked(presentation: RankedPresentation) -> str:
    errors = presentation.validate()
    if errors:
        raise ValueError("; ".join(errors))
    base = presentation.base
    tiers = []
    for tier in presentation.tiers:
        interventions = []
        for item in tier.interventions:
            interventions.append(
                "<article class='intervention'>"
                f"<h3>{html.escape(item.name)}</h3>"
                f"{_markdown_block(item.summary)}"
                f"<p class='supported'><strong>Supported use:</strong> {html.escape(item.supported_use)}</p>"
                f"<p class='boundary-copy'><strong>Do not overclaim:</strong> {html.escape(item.overclaim_boundary)}</p>"
                "</article>"
            )
        tiers.append(
            f"<section class='tier'><h2>Tier {tier.rank}: {html.escape(tier.title)}</h2>"
            f"{''.join(interventions)}</section>"
        )
    body = (
        f"<header><h1>{html.escape(base.context.title)}</h1>"
        f"<p class='subtitle'>{html.escape(base.context.subtitle)}</p></header>"
        f"<div class='profile'>{html.escape(base.evidence_profile.get_summary_text())}</div>"
        f"<section>{_markdown_block(base.lead)}</section>"
        f"{''.join(tiers)}"
        f"<section><h2>Sources</h2>{_source_cards(base)}</section>"
        f"<section class='boundary'><h2>Decision boundary</h2>{_markdown_block(base.boundary_notice)}</section>"
    )
    document = _shell(base.context.title, body)
    errors = validate_visible_html(document)
    if errors:
        raise ValueError("; ".join(errors))
    return document
