#!/usr/bin/env python3
"""
scripts/query.py — Agent query loop for the feline research OS vault.

Usage:
    python scripts/query.py "<question>" [--disease ckd|hcm|fip|ibd|diabetes] [--write-back] [--max-hops 3]

Dependencies:
    pip install anthropic openai

The agent routes your question through question-router.md, loads relevant topic
pages and source cards, then synthesizes a sourced answer with provenance tags:
  [quoted_fact: src-ckd-001]                   — direct quote from a loaded source card
  [source_supported_conclusion: src-ckd-001]   — inference supported by loaded evidence
  [llm_inference]                              — reasoning beyond loaded evidence

With --write-back, the answer is written to outputs/qa/ following the vault's
output schema (type: output, output_kind: qa).
"""

import argparse
import json
import re
import sys
import os
from datetime import date
from pathlib import Path
from typing import Callable, Optional

# Search integration — import vault_search for pre-synthesis context enrichment
try:
    from search import vault_search, format_results_for_llm
    SEARCH_AVAILABLE = True
except ImportError:
    try:
        from .search import vault_search, format_results_for_llm
        SEARCH_AVAILABLE = True
    except ImportError:
        SEARCH_AVAILABLE = False

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

VAULT_ROOT = Path(__file__).parent.parent
MODEL = "claude-opus-4-6"
OLLAMA_MODEL = "qwen2.5:14b"       # change to any model you have pulled
OLLAMA_BASE_URL = "http://localhost:11434/v1"
# Prefer a stable non-reasoning chat-completions model for ordinary user flows.
# Some OpenRouter GPT-5 responses can consume completion budget without emitting
# usable text in this app's JSON-first router/hop calls.
OPENROUTER_MODEL = os.environ.get("OPENROUTER_MODEL", "openai/gpt-4.1-mini")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_DAILY_BUDGET_ENV = "OPENROUTER_DAILY_BUDGET_USD"
OPENROUTER_MAX_DAILY_BUDGET_USD = 1.00
QUESTION_ROUTER_REL = "system/indexes/question-router.md"
ASK_THE_VAULT_REL = "system/indexes/ask-the-vault.md"
OUTPUTS_QA_REL = "outputs/qa"
CONTEXT_TOKEN_LIMIT = 80_000  # estimated; force synthesize above this
SYNTHESIS_MAX_TOKENS = 4096
OVERVIEW_COMPACT_TOPIC_CHAR_LIMIT = 3600
OVERVIEW_COMPACT_SOURCE_CHAR_LIMIT = 4200
OVERVIEW_MIN_SOURCE_CARDS = 4

# Vision integration — set to False to disable figure attachment entirely
VISION_INTEGRATION_ENABLED = True
VISION_FIGURE_CAP = 3        # max figures attached per synthesis call (3 PNGs ≈ 6–15k tokens)
VISION_MAX_FILE_BYTES = 2 * 1024 * 1024  # 2 MB — skip larger files with a warning

# ---------------------------------------------------------------------------
# Source weighting — combined score = evidence_level × verification_status
# ---------------------------------------------------------------------------

VERIFICATION_STATUS_WEIGHTS: dict[str, float] = {
    "audited": 1.0,
    "deep_extracted": 0.9,
    "source_checked": 0.7,
    "abstract_weighted": 0.4,
    "title_only": 0.1,
}

EVIDENCE_LEVEL_SCORES: dict[str, int] = {
    "guideline": 10,
    "regulation": 9,
    "review": 8,
    "original-study": 7,
    "guidance": 6,
    "case-series": 5,
    "case-report": 3,
    "commentary": 2,
}

# Weight tier labels for synthesis prompt
WEIGHT_TIER_LABELS: dict[str, tuple[float, float]] = {
    "high": (7.0, 10.0),      # guideline/regulation/review with deep extraction
    "medium": (4.0, 7.0),     # original-study or partial extraction
    "low": (0.0, 4.0),        # case reports or abstract-only
}

# External search integration (gated)
try:
    from external_search import (
        search_pubmed,
        search_crossref,
        ExternalSearchConfig,
        ExternalSearchResult,
        ExternalSearchResponse,
    )
    EXTERNAL_SEARCH_AVAILABLE = True
except ImportError:
    try:
        from .external_search import (
            search_pubmed,
            search_crossref,
            ExternalSearchConfig,
            ExternalSearchResult,
            ExternalSearchResponse,
        )
        EXTERNAL_SEARCH_AVAILABLE = True
    except ImportError:
        EXTERNAL_SEARCH_AVAILABLE = False

# Sparse result threshold for triggering external search
SPARSE_RESULT_THRESHOLD = 3


def is_local_search_sparse(
    search_results: list,
    loaded_source_ids: list[str],
    threshold: int = SPARSE_RESULT_THRESHOLD,
) -> bool:
    """
    Determine if local search results are too sparse to produce a good answer.

    Args:
        search_results: Results from vault_search
        loaded_source_ids: Source IDs already loaded
        threshold: Minimum number of useful results to avoid being sparse

    Returns:
        True if results are below threshold, suggesting external search may help
    """
    # Count results that actually loaded new source cards
    useful_count = len(loaded_source_ids)
    return useful_count < threshold


def build_external_search_trace(
    question: str,
    disease: str,
    max_results: int = 5,
) -> dict:
    """Search free literature APIs and return a research-trace entry."""
    external_query = (
        f"feline {disease} {question}"
        if disease and disease != "unknown"
        else f"feline cat {question}"
    )
    if not EXTERNAL_SEARCH_AVAILABLE:
        return {
            "step": "External search (PubMed/Crossref)",
            "detail": f"query={external_query}; results=0; status=unavailable",
            "items": [],
        }

    config = ExternalSearchConfig(allow_external=True, max_results=max_results)
    trace_items: list[dict] = []
    errors: list[str] = []
    total_results = 0

    for source, search_fn in (
        ("pubmed", search_pubmed),
        ("crossref", search_crossref),
    ):
        response = search_fn(external_query, config)
        if response.error:
            errors.append(f"{source}={response.error}")
            continue
        total_results += len(response.results)
        for result in response.results[:3]:
            trace_items.append({
                "source": source,
                "title": (
                    result.title[:60] + "..."
                    if len(result.title) > 60
                    else result.title
                ),
                "pmid": result.pmid,
                "doi": result.doi,
                "external": True,
            })

    status = "needs_intake" if trace_items else "no_results"
    detail = (
        f"query={external_query}; results={total_results}; status={status}"
    )
    if errors:
        detail += f"; errors={' | '.join(errors)}"
    return {
        "step": "External search (PubMed/Crossref)",
        "detail": detail,
        "items": trace_items,
    }


def compute_source_weight(evidence_level: str, verification_status: str) -> float:
    """Compute combined weight score for a source."""
    base = EVIDENCE_LEVEL_SCORES.get(evidence_level, 5)  # default to mid-range
    mult = VERIFICATION_STATUS_WEIGHTS.get(verification_status, 0.5)
    return base * mult


def get_weight_tier(score: float) -> str:
    """Return tier label (high/medium/low) for a weight score."""
    for tier, (low, high) in WEIGHT_TIER_LABELS.items():
        if low <= score < high or (tier == "high" and score >= high):
            return tier
    return "low"


# ---------------------------------------------------------------------------
# Backend helpers
# ---------------------------------------------------------------------------

def validate_openrouter_budget() -> float:
    """
    Project-side guardrail for live OpenRouter runs.

    This does not replace the OpenRouter dashboard limit. It forces the local
    project environment to acknowledge the intended daily cap before any API call.
    """
    raw = os.environ.get(OPENROUTER_DAILY_BUDGET_ENV, "").strip()
    if not raw:
        raise ValueError(
            f"{OPENROUTER_DAILY_BUDGET_ENV} not set. Set it to 1.00 or lower "
            "after setting the matching $1/day limit in the OpenRouter dashboard."
        )
    try:
        budget = float(raw)
    except ValueError as exc:
        raise ValueError(f"{OPENROUTER_DAILY_BUDGET_ENV} must be a number, got {raw!r}") from exc
    if budget <= 0:
        raise ValueError(f"{OPENROUTER_DAILY_BUDGET_ENV} must be greater than 0")
    if budget > OPENROUTER_MAX_DAILY_BUDGET_USD:
        raise ValueError(
            f"{OPENROUTER_DAILY_BUDGET_ENV}={budget:.2f} exceeds the project cap "
            f"of {OPENROUTER_MAX_DAILY_BUDGET_USD:.2f}"
        )
    return budget


def make_client(backend: str = "anthropic"):
    """
    Return a client for the selected backend.
      backend="anthropic"  — Anthropic SDK (requires ANTHROPIC_API_KEY)
      backend="ollama"     — OpenAI-compatible SDK pointing at local Ollama
      backend="openrouter" — OpenAI-compatible SDK pointing at OpenRouter
    Raises ImportError if the required package is not installed.
    """
    if backend in {"ollama", "openrouter"}:
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise ImportError("pip install openai") from exc
        if backend == "ollama":
            return OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not set")
        validate_openrouter_budget()
        return OpenAI(base_url=OPENROUTER_BASE_URL, api_key=api_key)
    else:
        try:
            import anthropic
        except ImportError as exc:
            raise ImportError("pip install anthropic") from exc
        return anthropic.Anthropic()


def _extract_text_from_message_content(content, backend_label: str) -> str:
    """Normalize SDK message content into plain text or raise a clear error."""
    if isinstance(content, str):
        text = content.strip()
        if text:
            return text
        raise ValueError(f"{backend_label} returned empty text content")

    if isinstance(content, list):
        text_parts: list[str] = []
        for block in content:
            if isinstance(block, dict):
                block_text = block.get("text")
            else:
                block_text = getattr(block, "text", None)
            if isinstance(block_text, str) and block_text.strip():
                text_parts.append(block_text.strip())
        if text_parts:
            return "\n".join(text_parts)

    raise ValueError(
        f"{backend_label} returned unsupported message content: "
        f"{type(content).__name__}"
    )


def _summarize_openai_choice(choice) -> str:
    """Return a safe, compact summary of an OpenAI-compatible choice/message shape."""
    finish_reason = getattr(choice, "finish_reason", None)
    message = getattr(choice, "message", None)
    if message is None:
        return f"finish_reason={finish_reason!r}, message=None"

    refusal = getattr(message, "refusal", None)
    tool_calls = getattr(message, "tool_calls", None) or []
    annotations = getattr(message, "annotations", None) or []
    audio = getattr(message, "audio", None)
    content = getattr(message, "content", None)

    refusal_present = bool(isinstance(refusal, str) and refusal.strip())
    content_type = type(content).__name__

    return (
        f"finish_reason={finish_reason!r}, "
        f"content_type={content_type}, "
        f"refusal_present={refusal_present}, "
        f"tool_calls={len(tool_calls)}, "
        f"annotations={len(annotations)}, "
        f"audio_present={audio is not None}"
    )


def _chat(client, model: str, system: str, messages: list[dict], max_tokens: int) -> str:
    """
    Unified chat call for both Anthropic and OpenAI-compatible clients.
    Anthropic: client.messages.create(system=..., messages=[...])
    Ollama/OpenRouter: client.chat.completions.create(messages=[{role:system,...},...])
    """
    if hasattr(client, "messages"):
        # Anthropic SDK
        resp = client.messages.create(
            model=model, max_tokens=max_tokens,
            system=system, messages=messages,
        )
        if not getattr(resp, "content", None):
            raise ValueError("Anthropic returned no content blocks")
        return _extract_text_from_message_content(resp.content[0].text, "Anthropic")
    else:
        # OpenAI-compatible (Ollama)
        all_messages = [{"role": "system", "content": system}] + messages
        resp = client.chat.completions.create(
            model=model, max_tokens=max_tokens,
            messages=all_messages,
        )
        choices = getattr(resp, "choices", None) or []
        if not choices:
            raise ValueError("OpenAI-compatible backend returned no choices")
        choice = choices[0]
        message = getattr(choice, "message", None)
        if message is None:
            raise ValueError(
                "OpenAI-compatible backend returned no message "
                f"({ _summarize_openai_choice(choice) })"
            )
        try:
            return _extract_text_from_message_content(
                getattr(message, "content", None),
                "OpenAI-compatible backend",
            )
        except ValueError as exc:
            raise ValueError(
                f"{exc} ({_summarize_openai_choice(choice)})"
            ) from exc


# ---------------------------------------------------------------------------
# Pure helpers (unit-testable, no API calls)
# ---------------------------------------------------------------------------

def estimate_tokens(text: str) -> int:
    """Rough token estimate: 1 token ≈ 4 characters."""
    return len(text) // 4


def build_source_index(vault_root: Path) -> dict[str, Path]:
    """
    Scan raw/ recursively. For each .md file with a YAML frontmatter `id:` field,
    map that id to the file path. Returns {src_id: absolute_path}.
    """
    index: dict[str, Path] = {}
    raw_dir = vault_root / "raw"
    if not raw_dir.exists():
        return index
    for md_file in raw_dir.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if not content.startswith("---"):
            continue
        end = content.find("\n---", 3)
        if end == -1:
            continue
        for line in content[3:end].splitlines():
            if line.startswith("id:"):
                src_id = line.split(":", 1)[1].strip().strip("\"'")
                if src_id:
                    index[src_id] = md_file
                break
    return index


def build_source_titles(vault_root: Path) -> dict[str, str]:
    """
    Scan raw/ recursively. For each .md file with YAML frontmatter `id:` and `title:` fields,
    map the id to the title. Returns {src_id: title_string}.
    Used for rendering human-readable source references in the UI.
    """
    titles: dict[str, str] = {}
    raw_dir = vault_root / "raw"
    if not raw_dir.exists():
        return titles
    for md_file in raw_dir.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if not content.startswith("---"):
            continue
        end = content.find("\n---", 3)
        if end == -1:
            continue
        src_id = None
        title = None
        for line in content[3:end].splitlines():
            if line.startswith("id:"):
                src_id = line.split(":", 1)[1].strip().strip("\"'")
            elif line.startswith("title:"):
                title = line.split(":", 1)[1].strip().strip("\"'")
        if src_id and title:
            titles[src_id] = title
    return titles


def build_source_weights(vault_root: Path) -> dict[str, dict]:
    """
    Scan raw/ recursively. For each .md file with YAML frontmatter,
    extract id, evidence_level, and verification_status, then compute weight.
    Returns {src_id: {"score": float, "tier": str, "evidence_level": str, "verification_status": str}}.
    """
    weights: dict[str, dict] = {}
    raw_dir = vault_root / "raw"
    if not raw_dir.exists():
        return weights
    for md_file in raw_dir.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if not content.startswith("---"):
            continue
        end = content.find("\n---", 3)
        if end == -1:
            continue
        src_id = None
        evidence_level = "original-study"  # default
        verification_status = "source_checked"  # default
        for line in content[3:end].splitlines():
            if line.startswith("id:"):
                src_id = line.split(":", 1)[1].strip().strip("\"'")
            elif line.startswith("evidence_level:"):
                evidence_level = line.split(":", 1)[1].strip().strip("\"'")
            elif line.startswith("verification_status:"):
                verification_status = line.split(":", 1)[1].strip().strip("\"'")
        if src_id:
            score = compute_source_weight(evidence_level, verification_status)
            weights[src_id] = {
                "score": score,
                "tier": get_weight_tier(score),
                "evidence_level": evidence_level,
                "verification_status": verification_status,
            }
    return weights


def resolve_link(source_file: Path, link: str) -> Optional[Path]:
    """
    Resolve a relative markdown link from source_file's directory.
    Returns the resolved Path if it exists on disk, else None.
    Ignores http(s) links and anchor-only fragments.
    """
    if link.startswith(("http://", "https://")):
        return None
    link = link.split("#")[0].strip()
    if not link:
        return None
    resolved = (source_file.parent / link).resolve()
    return resolved if resolved.exists() else None


def parse_json_block(text) -> Optional[dict]:
    """
    Extract a JSON object from model output.
    Handles both raw JSON and markdown ```json ... ``` fences.
    """
    if not isinstance(text, str) or not text.strip():
        return None
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fenced:
        try:
            return json.loads(fenced.group(1))
        except json.JSONDecodeError:
            pass
    raw = re.search(r"\{[^{}]*\}", text, re.DOTALL)
    if raw:
        try:
            return json.loads(raw.group(0))
        except json.JSONDecodeError:
            pass
    return None


def parse_source_ids_from_answer(answer: str) -> list[str]:
    """Extract all source IDs cited via [quoted_fact: ...] or [source_supported_conclusion: ...]."""
    pattern = r"\[(?:quoted_fact|source_supported_conclusion):\s*([^\]]+)\]"
    ids: list[str] = []
    for match in re.findall(pattern, answer):
        ids.extend(s.strip() for s in re.split(r"[,;]", match))
    return sorted(set(ids))


def sanitize_provenance_tags(answer: str, allowed_source_ids: list[str]) -> str:
    """Drop or downgrade provenance tags that cite source IDs not loaded for this run."""
    allowed = {sid for sid in allowed_source_ids if sid.startswith("src-")}

    def informal_source_repl(match: re.Match) -> str:
        content = match.group(1)
        if re.match(r"(?:quoted_fact|source_supported_conclusion|llm_inference)\b", content):
            return match.group(0)
        ids = [sid for sid in re.findall(r"src-[a-z]+-\d{3}", content) if sid in allowed]
        if ids:
            return f"[source_supported_conclusion: {', '.join(sorted(set(ids)))}]"
        return match.group(0)

    answer = re.sub(r"\[([^\]]+)\]", informal_source_repl, answer)
    answer = re.sub(r"\[llm_inference[^\]]*\]", "[llm_inference]", answer)
    answer = re.sub(r"\[topic-[^\]]+\]", "[llm_inference]", answer)

    def repl(match: re.Match) -> str:
        tag_type = match.group(1)
        raw_ids = match.group(2)
        ids = [sid.strip() for sid in re.split(r"[,;]", raw_ids) if sid.strip()]
        valid_ids = [sid for sid in ids if sid in allowed]
        if not valid_ids:
            return "[llm_inference]"
        return f"[{tag_type}: {', '.join(valid_ids)}]"

    return re.sub(r"\[(quoted_fact|source_supported_conclusion):\s*([^\]]+)\]", repl, answer)


def parse_source_ids_from_frontmatter(content: str) -> list[str]:
    """
    Extract source_ids from YAML frontmatter.
    Supports both inline lists:
      source_ids: [src-ckd-001, src-ckd-002]
    and block lists:
      source_ids:
        - src-ckd-001
        - src-ckd-002
    """
    if not content.startswith("---"):
        return []
    end = content.find("\n---", 3)
    if end == -1:
        return []
    fm_text = content[3:end]

    ids: list[str] = []
    in_source_ids = False
    for line in fm_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("source_ids:"):
            remainder = stripped.split(":", 1)[1].strip()
            if remainder.startswith("[") and remainder.endswith("]"):
                inner = remainder[1:-1].strip()
                if not inner:
                    return []
                return [
                    item.strip().strip("\"'")
                    for item in inner.split(",")
                    if item.strip()
                ]
            in_source_ids = True
            continue
        if in_source_ids:
            if stripped.startswith("- "):
                ids.append(stripped[2:].strip().strip("\"'"))
            elif stripped and not stripped.startswith("#"):
                if not line.startswith("    ") and not line.startswith("\t"):
                    break
    return ids


def source_ids_from_topic_frontmatter(
    loaded_path_order: list[Path],
    frontmatter_source_ids: dict[Path, list[str]],
    already_loaded_source_ids: list[str],
    limit: int,
) -> list[str]:
    """Return ordered source IDs from loaded topic frontmatter, excluding already loaded cards."""
    seen = set(already_loaded_source_ids)
    selected: list[str] = []
    for path in loaded_path_order:
        for sid in frontmatter_source_ids.get(path, []):
            if not sid.startswith("src-") or sid in seen:
                continue
            selected.append(sid)
            seen.add(sid)
            if len(selected) >= limit:
                return selected
    return selected


def frontmatter_scalar(content: str, key: str) -> str:
    """Extract a single scalar value from YAML frontmatter without PyYAML."""
    if not content.startswith("---"):
        return ""
    end = content.find("\n---", 3)
    if end == -1:
        return ""
    for line in content[3:end].splitlines():
        if line.startswith(f"{key}:"):
            return line.split(":", 1)[1].strip().strip("\"'")
    return ""


def markdown_section(content: str, heading: str) -> str:
    """Return the body under an exact markdown heading until the next heading of equal/higher level."""
    pattern = rf"^{re.escape(heading)}\s*$"
    match = re.search(pattern, content, re.M)
    if not match:
        return ""
    level = len(heading) - len(heading.lstrip("#"))
    next_heading = re.search(rf"^#{{1,{level}}}\s+", content[match.end():], re.M)
    end = match.end() + next_heading.start() if next_heading else len(content)
    return content[match.end():end].strip()


def compact_source_card_context(src_id: str, rel: str, content: str, weight_info: str = "") -> str:
    """
    Compact source-card context for ordinary-user overview answers.

    Full source cards are useful for research asks, but broad reader prompts only
    need enough source material to keep provenance honest. Keep the title,
    evidence metadata, one-line summary, sourced facts, source-supported
    conclusions, and caveats.
    """
    metadata_lines = [
        f"id: {src_id}{weight_info}",
        f"title: {frontmatter_scalar(content, 'title')}",
        f"evidence_level: {frontmatter_scalar(content, 'evidence_level')}",
        f"verification_status: {frontmatter_scalar(content, 'verification_status')}",
        f"year: {frontmatter_scalar(content, 'year')}",
    ]
    sections = [
        ("One-Line Summary", markdown_section(content, "## One-Line Summary")),
        ("quoted_fact", markdown_section(content, "### quoted_fact")),
        ("source_supported_conclusion", markdown_section(content, "### source_supported_conclusion")),
        ("Limits / Caveats", markdown_section(content, "## Limits / Caveats")),
    ]
    parts = [
        f"--- {rel} ({src_id}{weight_info}; compact overview source) ---",
        "\n".join(line for line in metadata_lines if not line.endswith(": ")),
    ]
    for label, body in sections:
        if body:
            parts.append(f"## {label}\n{body}")
    compact = "\n\n".join(parts)
    if len(compact) > OVERVIEW_COMPACT_SOURCE_CHAR_LIMIT:
        compact = compact[:OVERVIEW_COMPACT_SOURCE_CHAR_LIMIT].rstrip() + "\n...[compact source clipped]"
    return compact


def compact_topic_page_context(rel: str, content: str) -> str:
    """Compact compiled topic pages for ordinary-user overview context."""
    page_id = frontmatter_scalar(content, "id")
    topic = frontmatter_scalar(content, "topic")
    question_type = frontmatter_scalar(content, "question_type")
    title_match = re.search(r"^#\s+(.+)$", content, re.M)
    title = title_match.group(1).strip() if title_match else rel
    preferred_headings = [
        "## One-Sentence State",
        "## Current Status",
        "## 1. Strongest Current Conclusions",
        "## Current Synthesis Spine",
        "## Current Working Hypothesis",
        "## Key-Claim Traceability",
        "## 4. Current Arguments We Can Defend",
        "## 5. Current Arguments We Should Not Overstate",
        "## Best First Compiled Questions",
    ]
    parts = [
        f"--- {rel} (compiled topic page; compact overview surface; not a source card) ---",
        f"id: {page_id}",
        f"topic: {topic}",
        f"question_type: {question_type}",
        f"title: {title}",
    ]
    for heading in preferred_headings:
        section = markdown_section(content, heading)
        if section:
            parts.append(f"{heading}\n{section}")
        compact = "\n\n".join(parts)
        if len(compact) >= OVERVIEW_COMPACT_TOPIC_CHAR_LIMIT:
            return compact[:OVERVIEW_COMPACT_TOPIC_CHAR_LIMIT].rstrip() + "\n...[compact topic clipped]"
    compact = "\n\n".join(parts)
    if len(compact) > OVERVIEW_COMPACT_TOPIC_CHAR_LIMIT:
        compact = compact[:OVERVIEW_COMPACT_TOPIC_CHAR_LIMIT].rstrip() + "\n...[compact topic clipped]"
    return compact


def compute_confidence(answer: str) -> str:
    """
    Derive confidence from provenance tag distribution.
      high   — 0% llm_inference
      medium — 1–50% llm_inference
      low    — >50% llm_inference
    """
    llm_count = len(re.findall(r"\[llm_inference\]", answer))
    sourced_count = len(re.findall(r"\[(?:quoted_fact|source_supported_conclusion):[^\]]+\]", answer))
    total = llm_count + sourced_count
    if total == 0:
        return "low"
    ratio = llm_count / total
    if ratio == 0.0:
        return "high"
    if ratio <= 0.5:
        return "medium"
    return "low"


def build_slug(question: str) -> str:
    """Kebab-case slug from first 6 words of question (lowercase, alphanumeric only)."""
    words = re.sub(r"[^a-z0-9\s]", "", question.lower()).split()[:6]
    return "-".join(words)


def infer_disease_from_question(question: str) -> str:
    """Best-effort disease inference from common disease names and aliases.

    Uses flexible word boundaries that work with Chinese text adjacent to English.
    The pattern (?<![a-zA-Z]) and (?![a-zA-Z]) ensure we don't match partial words
    while still matching when Chinese characters are adjacent (e.g., "关于CKD的").
    """
    lowered = question.lower()
    # Use lookahead/lookbehind for flexible boundaries that work with CJK text
    # (?<![a-zA-Z]) = not preceded by letter, (?![a-zA-Z]) = not followed by letter
    disease_patterns = [
        ("ckd", [r"(?<![a-zA-Z])ckd(?![a-zA-Z])", r"chronic kidney disease", r"(?<![a-zA-Z])renal(?![a-zA-Z])", r"(?<![a-zA-Z])kidney(?![a-zA-Z])", r"(?<![a-zA-Z])sdma(?![a-zA-Z])", r"(?<![a-zA-Z])creatinine(?![a-zA-Z])", r"肾", r"慢性肾", r"肌酐"]),
        ("hcm", [r"(?<![a-zA-Z])hcm(?![a-zA-Z])", r"hypertrophic cardiomyopathy", r"(?<![a-zA-Z])cardiomyopathy(?![a-zA-Z])", r"心肌", r"肥厚型心肌"]),
        ("fip", [r"(?<![a-zA-Z])fip(?![a-zA-Z])", r"feline infectious peritonitis", r"传染性腹膜炎", r"猫传腹"]),
        ("ibd", [r"(?<![a-zA-Z])ibd(?![a-zA-Z])", r"inflammatory bowel disease", r"small-cell lymphoma", r"small cell lymphoma", r"炎症性肠病", r"肠病"]),
        ("diabetes", [r"(?<![a-zA-Z])diabetes(?![a-zA-Z])", r"diabetes mellitus", r"(?<![a-zA-Z])diabetic(?![a-zA-Z])", r"(?<![a-zA-Z])sglt2(?![a-zA-Z])", r"(?<![a-zA-Z])glargine(?![a-zA-Z])", r"糖尿病"]),
        ("fcv", [r"(?<![a-zA-Z])fcv(?![a-zA-Z])", r"feline calicivirus", r"(?<![a-zA-Z])calicivirus(?![a-zA-Z])", r"杯状病毒"]),
        ("obesity", [r"(?<![a-zA-Z])obesity(?![a-zA-Z])", r"(?<![a-zA-Z])obese(?![a-zA-Z])", r"weight loss", r"body condition", r"肥胖", r"超重", r"体况"]),
        ("cancer", [r"(?<![a-zA-Z])cancer(?![a-zA-Z])", r"(?<![a-zA-Z])tumou?r(?![a-zA-Z])", r"carcinoma", r"lymphoma", r"sarcoma", r"肿瘤", r"癌", r"淋巴瘤"]),
    ]
    for disease, patterns in disease_patterns:
        if any(re.search(pattern, lowered) for pattern in patterns):
            return disease
    return "unknown"


def prefers_chinese(question: str) -> bool:
    """Return True when the user question contains CJK characters."""
    return bool(re.search(r"[\u3400-\u9fff]", question))


def local_search_terms(question: str) -> list[str]:
    """Build a small deterministic search set for no-API vault lookup."""
    terms: list[str] = []

    def add(term: str) -> None:
        term = term.strip()
        if len(term) >= 2 and term not in terms:
            terms.append(term)

    add(question)
    for token in re.findall(r"[A-Za-z][A-Za-z0-9+/_-]{2,}", question):
        add(token)

    lowered = question.lower()
    domain_terms = [
        ("sirna", "siRNA"),
        ("肥胖", "肥胖"),
        ("药效", "药效"),
        ("疗效", "疗效"),
        ("评价", "评价"),
        ("猫", "猫"),
        ("feline", "feline"),
        ("obesity", "obesity"),
        ("obese", "obese"),
        ("body condition", "body condition"),
        ("weight loss", "weight loss"),
        ("cancer", "cancer"),
        ("肿瘤", "肿瘤"),
    ]
    for needle, term in domain_terms:
        if needle in lowered or needle in question:
            add(term)
    return terms[:8]


def aggregate_vault_search(
    question: str,
    vault_root: Path,
    scope: str = "all",
    limit: int = 8,
) -> tuple[list[dict], list[str]]:
    """Search whole query plus important terms, then merge ranked results."""
    if not SEARCH_AVAILABLE:
        return [], []
    terms = local_search_terms(question)
    merged: dict[str, dict] = {}
    for term in terms:
        for result in vault_search(term, vault_root, scope=scope, limit=limit):
            key = result["file"]
            if key not in merged:
                item = dict(result)
                item["matched_terms"] = []
                item["score"] = 0
                merged[key] = item
            merged[key]["score"] += int(result.get("matches", 0))
            if term not in merged[key]["matched_terms"]:
                merged[key]["matched_terms"].append(term)
            snippets = merged[key].setdefault("snippets", [])
            for snippet in result.get("snippets", []):
                if snippet not in snippets and len(snippets) < 3:
                    snippets.append(snippet)
    results = sorted(
        merged.values(),
        key=lambda r: (-int(r.get("score", 0)), r["file"]),
    )
    return results[:limit], terms


def source_card_disease_matches(path: Path, disease: str) -> bool:
    """Best-effort frontmatter disease filter for local search summaries."""
    if disease == "unknown":
        return True
    content = _read_file(path)
    if not content:
        return False
    fm_disease = frontmatter_scalar(content, "disease")
    fm_diseases = ""
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            for line in content[3:end].splitlines():
                if line.startswith("diseases:"):
                    fm_diseases = line.split(":", 1)[1]
                    break
    return disease in {fm_disease, fm_diseases} or disease in fm_diseases


def is_broad_explanation_question(question: str) -> bool:
    """Return True for broad ordinary-reader prompts that need a compact wiki answer."""
    lowered = question.lower().strip()
    broad_tokens = [
        "explain",
        "explanation",
        "what is",
        "overview",
        "tell me about",
        "current understanding",
        "researcher know",
        "researchers know",
        "介绍",
        "解释",
        "为什么",
        "是什么",
        "是什么病",
        "怎么理解",
        "能告诉我什么",
        "告诉我什么",
    ]
    compact = re.sub(r"\s+", "", lowered)
    compact_disease_tokens = {
        "ckd",
        "hcm",
        "fip",
        "ibd",
        "diabetes",
        "糖尿病",
        "慢性肾病",
        "肾病",
    }
    return any(token in lowered for token in broad_tokens) or compact in compact_disease_tokens


def heuristic_question_type(question: str) -> str:
    """Deterministic high-risk question typing guardrails before/after LLM routing."""
    lowered = question.lower()

    if any(token in lowered for token in ["verify whether", "verify ", "treated as a core", "settled fact", "anchor in this vault"]):
        return "claim_verification"
    if (
        "separated between recognition and endpoints" in lowered
        or (
            "recognition" in lowered
            and any(token in lowered for token in ["endpoint", "endpoints"])
        )
    ):
        return "recognition"
    if any(token in lowered for token in [
        "workup", "recognition", "boundary", "diagnostic", "diagnosis", "differentiate",
        "识别", "区分", "怎么识别", "怎么区分", "诊断", "鉴别",
    ]):
        return "recognition"
    if any(token in lowered for token in ["regulatory", "fda", "vmd", "ema", "jurisdiction", "china"]):
        return "regulatory"
    if any(token in lowered for token in ["compare ", "compare ckd", "versus", "vs ", " vs."]):
        return "synthesis"
    if any(token in lowered for token in ["maturity", "cross-disease", "cross disease"]):
        return "synthesis"
    
    # Heuristics for PK design
    if any(re.search(pat, lowered) for pat in [
        r"\bpk\b", r"\bpd\b", r"药代", r"药动",
        r"pharmacokinetic", r"采血", r"blood sampling",
        r"采样时间点", r"采样", r"时间点",
    ]):
        return "pk"
        
    # Heuristics for protocol design
    if any(re.search(pat, lowered) for pat in [
        r"方案", r"protocol", r"设计", r"design",
        r"how to design", r"怎么设计", r"研究方案",
        r"评分体系", r"如何构建", r"如何设定",
        r"约束", r"constraints",
    ]):
        return "protocol"

    if any(token in lowered for token in [
        "endpoint", "endpoints", "efficacy evaluation", "usable for", "outcome", "remission",
        "缓解", "为什么会缓解", "为什么缓解",
    ]):
        return "endpoints"
    if any(token in lowered for token in ["treatment", "therapy", "diet", "insulin", "glargine", "sglt2", "bexacat", "senvelgo"]):
        return "treatment"
    if any(token in lowered for token in ["mechanism", "机制", "pathway", "core mechanism", "mechanism spine", "主线"]):
        return "mechanism"
    if is_broad_explanation_question(question):
        return "overview"
    return "unknown"


def heuristic_files_for_route(question_type: str, disease: str) -> list[str]:
    """Return strong default answer surfaces for high-risk question types."""
    if question_type == "synthesis":
        return [
            "system/indexes/disease-module-maturity-ladder.md",
            "system/indexes/cross-disease-second-wave-narrow-owner-audit.md",
        ]
    if question_type == "protocol" and disease != "unknown":
        return [
            f"topics/{disease}/endpoint-handbook.md",
            f"topics/{disease}/translation-brief.md",
            f"topics/{disease}/model-map.md",
            f"topics/{disease}/model-summary.md",
        ]
    if question_type == "pk" and disease != "unknown":
        return [
            f"topics/{disease}/translation-brief.md",
            f"topics/{disease}/endpoint-handbook.md",
        ]
    if question_type == "claim_verification":
        files = ["system/indexes/verify-a-claim.md"]
        if disease != "unknown":
            files.append(f"topics/{disease}/current-state-dashboard.md")
        return files
    if disease == "unknown":
        return []

    if question_type == "overview":
        return [
            f"topics/{disease}/current-state-dashboard.md",
            f"topics/{disease}/synthesis-index.md",
        ]

    family_paths = {
        "mechanism": f"topics/{disease}/mechanism-overview.md",
        "recognition": f"topics/{disease}/risk-and-recognition.md",
        "endpoints": f"topics/{disease}/endpoint-handbook.md",
        "treatment": f"topics/{disease}/translation-brief.md",
        "regulatory": f"topics/{disease}/regulatory-brief.md",
    }
    path = family_paths.get(question_type)
    files = [path] if path else []

    # Fallback: when question_type is unknown but disease is known,
    # load default synthesis and dashboard pages for that disease
    if not files and disease != "unknown":
        files = [
            f"topics/{disease}/synthesis-index.md",
            f"topics/{disease}/current-state-dashboard.md",
            f"topics/{disease}/endpoint-handbook.md",
        ]
    if disease == "diabetes":
        diabetes_extra = {
            "mechanism": [
                "topics/diabetes/obesity-and-body-condition.md",
                "topics/diabetes/endocrine-secondary-diabetes.md",
                "topics/diabetes/pancreatitis-comorbidity.md",
            ],
            "recognition": [
                "topics/diabetes/diagnostic-monitoring-workup.md",
                "topics/diabetes/epidemiology-and-breed-risk.md",
                "topics/diabetes/endocrine-secondary-diabetes.md",
            ],
            "endpoints": [
                "topics/diabetes/remission-boundaries.md",
                "topics/diabetes/complications-neuropathy.md",
            ],
            "treatment": [
                "topics/diabetes/treatment-branch-map.md",
                "topics/diabetes/diet-architecture.md",
                "topics/diabetes/remission-boundaries.md",
                "topics/diabetes/sglt2-label-control.md",
            ],
            "regulatory": [
                "topics/diabetes/sglt2-label-control.md",
            ],
        }
        files.extend(diabetes_extra.get(question_type, []))
    return files


def merge_routing_with_guardrails(question: str, disease_hint: Optional[str], routed: dict) -> dict:
    """
    Apply deterministic routing guardrails.
    Heuristic question types take precedence for high-risk asks; file lists are
    prefixed with strong default answer surfaces without discarding useful LLM picks.
    """
    routed = dict(routed or {})
    heuristic_disease = disease_hint or infer_disease_from_question(question)
    routed_disease = routed.get("disease") or "unknown"
    disease = disease_hint or (routed_disease if routed_disease != "unknown" else heuristic_disease)

    heuristic_qtype = heuristic_question_type(question)
    routed_qtype = routed.get("question_type") or "unknown"
    question_type = heuristic_qtype if heuristic_qtype != "unknown" else routed_qtype

    seeded = heuristic_files_for_route(question_type, disease)
    routed_files = routed.get("files_to_load") or []
    merged_files: list[str] = []
    for rel in seeded + routed_files:
        if rel and rel not in merged_files:
            merged_files.append(rel)

    reasoning = routed.get("reasoning", "").strip()
    if heuristic_qtype != "unknown":
        prefix = f"Guardrailed to {heuristic_qtype}"
        reasoning = f"{prefix}. {reasoning}".strip()

    return {
        "question_type": question_type or "unknown",
        "disease": disease or "unknown",
        "files_to_load": merged_files,
        "reasoning": reasoning or "Guardrailed route.",
    }


def _figure_type_from_filename(filename: str) -> Optional[str]:
    """
    Extract the figure_type segment from a filename following the naming convention:
    src-{disease}-{card_id}-{figure_type}-{description}.png
    Returns the 4th dash-separated segment (0-indexed: [3]), or None if not parseable.
    Examples:
      src-ckd-001-mechanism-schematic.png  → "mechanism"
      src-hcm-010-imaging-echo-lv.png      → "imaging"
      src-ckd-017-outcome-flowchart.png    → "outcome"
    """
    stem = Path(filename).stem  # strip .png
    parts = stem.split("-")
    if len(parts) >= 4 and parts[0] == "src":
        return parts[3]
    return None


def _parse_local_assets_from_frontmatter(content: str) -> list[str]:
    """
    Extract the local_assets list from YAML frontmatter without requiring PyYAML.
    Returns a list of vault-relative path strings, or [] if none / empty.
    """
    if not content.startswith("---"):
        return []
    end = content.find("\n---", 3)
    if end == -1:
        return []
    fm_text = content[3:end]

    assets: list[str] = []
    in_assets = False
    for line in fm_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("local_assets:"):
            if "[]" in stripped:
                return []
            in_assets = True
            continue
        if in_assets:
            if stripped.startswith("- "):
                assets.append(stripped[2:].strip())
            elif stripped and not stripped.startswith("#"):
                # Another YAML key at same or higher level — stop
                if not line.startswith("    ") and not line.startswith("\t"):
                    break
    return assets


def resolve_local_assets(
    source_ids: list[str],
    vault_root: Path,
    figure_type_hint: Optional[str] = None,
) -> list[dict]:
    """
    For each source_id, read its source card and parse links.local_assets.
    Returns only entries where:
      - the filename does NOT start with 'candidate-' (i.e. verified)
      - the file actually exists on disk
      - the file is under vault_root (path traversal guard)
      - the file is ≤ VISION_MAX_FILE_BYTES (size guard)

    When figure_type_hint is provided (e.g. "mechanism"), only assets whose
    figure_type matches OR whose figure_type is None (non-standard filename,
    type cannot be determined) are included. This prevents off-topic figures
    (e.g. imaging schematics on a mechanism question) from consuming synthesis
    tokens. Matching assets are sorted first within the filtered set.

    Each returned dict: {"source_id": str, "path": Path, "rel": str, "figure_type": Optional[str]}
    """
    assets: list[dict] = []
    papers_dir = vault_root / "raw" / "papers"
    for sid in source_ids:
        card_path = papers_dir / f"{sid}.md"
        if not card_path.exists():
            continue
        try:
            content = card_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for asset_rel in _parse_local_assets_from_frontmatter(content):
            asset_path = (vault_root / asset_rel).resolve()

            # Path traversal guard: asset must stay inside vault_root
            try:
                asset_path.relative_to(vault_root.resolve())
            except ValueError:
                print(f"[warn] Path traversal blocked: {asset_rel}", file=sys.stderr)
                continue

            if Path(asset_rel).name.startswith("candidate-"):
                continue  # not yet verified against article label

            if not asset_path.exists():
                continue

            # Size guard: skip files larger than VISION_MAX_FILE_BYTES
            try:
                file_size = asset_path.stat().st_size
            except OSError:
                continue
            if file_size > VISION_MAX_FILE_BYTES:
                print(
                    f"[warn] Figure skipped (too large: {file_size // 1024}KB > "
                    f"{VISION_MAX_FILE_BYTES // 1024}KB): {asset_rel}",
                    file=sys.stderr,
                )
                continue

            figure_type = _figure_type_from_filename(asset_path.name)
            assets.append({
                "source_id": sid,
                "path": asset_path,
                "rel": str(asset_path.relative_to(vault_root.resolve())),
                "figure_type": figure_type,
            })

    # Filter: when figure_type_hint is set, exclude figures whose type is known
    # and doesn't match. Figures with figure_type=None (non-standard filenames)
    # always pass through — we can't determine their type, so be permissive.
    if figure_type_hint:
        assets = [
            a for a in assets
            if a.get("figure_type") is None or a.get("figure_type") == figure_type_hint
        ]

    # Sort: matching figure_type first within the filtered set
    if figure_type_hint:
        assets.sort(key=lambda a: (0 if a.get("figure_type") == figure_type_hint else 1))

    return assets


def enrich_source_card_with_caption(
    source_id: str,
    asset_rel: str,
    caption: str,
    vault_root: Path,
) -> bool:
    """
    Write a figure_caption_ai entry back to the source card's YAML frontmatter.
    Appends under a top-level 'figure_captions_ai:' key (creates it if absent).
    Returns True if the card was updated, False on any error.

    This closes the self-annotation loop: when Claude describes a figure in synthesis,
    that description becomes durable vault content for future queries.
    """
    papers_dir = vault_root / "raw" / "papers"
    card_path = papers_dir / f"{source_id}.md"
    if not card_path.exists():
        return False
    try:
        original = card_path.read_text(encoding="utf-8")
    except OSError:
        return False

    if not original.startswith("---"):
        return False
    end = original.find("\n---", 3)
    if end == -1:
        return False

    fm_text = original[3:end]
    body = original[end + 4:]  # everything after closing ---

    # Sanitize caption for YAML inline string (no newlines, escape quotes)
    safe_caption = caption.replace("\n", " ").replace('"', '\\"')[:500]
    safe_rel = asset_rel.replace('"', '\\"')

    new_entry = f'  - file: "{safe_rel}"\n    caption: "{safe_caption}"'

    if "figure_captions_ai:" in fm_text:
        # Append under existing key
        fm_text = fm_text.rstrip() + "\n" + new_entry
    else:
        fm_text = fm_text.rstrip() + "\nfigure_captions_ai:\n" + new_entry

    updated = "---" + fm_text + "\n---" + body
    try:
        card_path.write_text(updated, encoding="utf-8")
        return True
    except OSError:
        return False


def validate_frontmatter(fm: dict) -> list[str]:
    """Return list of required keys that are missing or empty."""
    required = [
        "id", "type", "output_kind", "topic", "question",
        "question_type", "source_ids", "generated_at", "hops", "confidence",
    ]
    return [k for k in required if not fm.get(k) and fm.get(k) != 0]


def render_frontmatter(fm: dict) -> str:
    """Render a dict as YAML frontmatter without requiring PyYAML."""
    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, bool):
            lines.append(f"{k}: {str(v).lower()}")
        elif isinstance(v, list):
            if v:
                lines.append(f"{k}:")
                for item in v:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"{k}: []")
        elif isinstance(v, dict):
            lines.append(f"{k}:")
            for dk, dv in v.items():
                inner = dv if dv else "[]"
                lines.append(f"  {dk}: {inner}")
        elif isinstance(v, str) and any(c in v for c in ('"', ":", ",")):
            escaped = v.replace('"', '\\"')
            lines.append(f'{k}: "{escaped}"')
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# API calls
# ---------------------------------------------------------------------------

def router_call(
    client,
    question: str,
    disease_hint: Optional[str],
    vault_root: Path,
    model: str = MODEL,
) -> dict:
    """
    API Call 1 — Router.
    Returns: { question_type, disease, files_to_load: [...], reasoning }
    """
    router_text = _read_file(vault_root / QUESTION_ROUTER_REL)
    vault_text = _read_file(vault_root / ASK_THE_VAULT_REL)

    hint_line = f"\nThe user specified --disease: {disease_hint}." if disease_hint else ""

    system = f"""You are a routing agent for a feline disease knowledge vault.
The vault covers feline CKD, HCM, FIP, IBD, diabetes, FCV, obesity, and cancer.
Return ONLY a JSON object with these keys:
  question_type  — one of: overview, mechanism, recognition, endpoints, treatment, regulatory, synthesis, claim_verification
  disease        — one of: ckd, hcm, fip, ibd, diabetes, fcv, obesity, cancer, unknown
  files_to_load  — list of vault-relative paths, e.g. ["topics/ckd/mechanism-overview.md"]
  reasoning      — one sentence{hint_line}"""

    user = f"Question: {question}\n\n--- question-router.md ---\n{router_text}\n\n--- ask-the-vault.md ---\n{vault_text}"

    result = parse_json_block(_chat(client, model, system,
                                    [{"role": "user", "content": user}], 512))
    if not result:
        result = {"question_type": "unknown", "disease": disease_hint or "unknown",
                  "files_to_load": [], "reasoning": "Router could not parse."}
    return merge_routing_with_guardrails(question, disease_hint, result)


def hop_call(
    client,
    question: str,
    loaded_context: str,
    history: list[dict],
    hop_num: int,
    model: str = MODEL,
) -> dict:
    """
    API Call 2..N — Hop.
    Returns one of:
      { action: "load_more",    files: [...] }
      { action: "load_sources", source_ids: [...] }
      { action: "synthesize" }
    """
    system = """You are a research navigation agent for a feline disease knowledge vault.
Decide your next action. Return ONLY a JSON object — one of:

{ "action": "load_more",    "files": ["topics/ckd/endpoint-handbook.md"] }
  Use when: you need additional topic pages to answer the question.

{ "action": "load_sources", "source_ids": ["src-ckd-001", "src-ckd-003"] }
  Use when: you can identify specific source card IDs to load for citations.

{ "action": "synthesize" }
  Use when: you have enough evidence to write a sourced answer now.

Rules: prefer synthesize when you have ≥2 relevant source cards loaded.
Do not request files you have already seen."""

    messages = history + [{
        "role": "user",
        "content": f"Question: {question}\n\n--- Loaded context (before hop {hop_num}) ---\n{loaded_context}\n\nNext action?",
    }]

    result = parse_json_block(_chat(client, model, system, messages, 256))
    return result if result else {"action": "synthesize"}


def synthesis_call(
    client,
    question: str,
    loaded_context: str,
    resolved_assets: Optional[list[dict]] = None,
    model: str = MODEL,
    answer_mode: str = "research",
    question_type: str = "unknown",
) -> tuple[str, list[dict]]:
    """
    Final synthesis call.
    Returns (answer_text, figures_used) where figures_used is a list of dicts:
      {"source_id": str, "file": str, "described_in_answer": bool}

    If resolved_assets are provided and the backend is Anthropic, attaches up to
    VISION_FIGURE_CAP image files as base64 blocks alongside the text context.
    Falls back gracefully to text-only for non-Anthropic backends or empty assets.
    """
    answer_language = "Chinese" if prefers_chinese(question) else "English"
    
    # Task-specific structure definition
    task_instructions = ""
    if question_type == "protocol":
        structure = """Structure:
1. Direct answer (one paragraph, lead with the conclusion)
2. Clinical Protocol (you MUST address all of the following sections and start each section with its exact level-2 markdown header):
   - ## 目的 / Purpose
   - ## 动物 / Animals
   - ## 入组与排除 / Enrollment
   - ## 分组 / Grouping
   - ## 给药干预 / Intervention
   - ## 终点指标 / Endpoints
   - ## 观察时间点 / Timepoints
   - ## 统计分析 / Statistics
   - ## 伦理与福利 / Ethics & Welfare
3. What we don't know yet (gaps or uncertainties in the evidence)"""
        task_instructions = """
Since the task type is protocol design, you MUST organize the core answer as a structured Clinical Protocol.
Ensure all of the following 9 sections are present and explicitly discussed, and you MUST use these exact headers:
- ## 目的 / Purpose
- ## 动物 / Animals
- ## 入组与排除 / Enrollment
- ## 分组 / Grouping
- ## 给药干预 / Intervention
- ## 终点指标 / Endpoints
- ## 观察时间点 / Timepoints
- ## 统计分析 / Statistics
- ## 伦理与福利 / Ethics & Welfare
Failing to include any of these sections with their exact headers will violate completeness checks and fail verification.
"""
    elif question_type == "endpoints":
        structure = """Structure:
1. Direct answer (one paragraph, lead with the conclusion)
2. Endpoint selection considerations:
   - 诊断与疗效评估的区别 / Diagnosis vs Efficacy
   - 主要与次要终点的划分 / Primary vs Secondary Endpoints
   - 猫种属特殊性证据 / Feline Species Evidence
   - 文献依据与出处 / Evidence Source
3. What we don't know yet (gaps or uncertainties in the evidence)"""
        task_instructions = """
Since the task type is endpoint selection, you MUST explicitly address:
- The distinction between diagnosis vs efficacy monitoring (诊断与疗效评估的区别)
- The primary vs secondary endpoints (主要与次要终点)
- Feline-specific evidence (猫种属证据)
- Literature source grounding (文献来源支持)
"""
    elif question_type == "pk":
        structure = """Structure:
1. Direct answer (one paragraph, lead with the conclusion)
2. PK Design elements:
   - 采血时点设计 / Sampling Times
   - 单次采血量限制 / Blood Volume Limitation
   - 样本量设计 / Sample Size
   - 生物分析方法 / Analytical Method
3. What we don't know yet (gaps or uncertainties in the evidence)"""
        task_instructions = """
Since the task type is PK design, you MUST address:
- Sampling times (采血时点)
- Blood volume constraints (单次采血量限制)
- Sample size (样本量)
- Analytical method (生物分析方法)
"""
    elif answer_mode == "overview":
        structure = """Structure:
1. Direct answer (2-4 short paragraphs, lead with the practical explanation)
2. What this means for a reader (plain-language interpretation, not veterinary advice)
3. Key evidence (3-5 bullets supporting the answer)
4. What we don't know yet (gaps or uncertainties in the evidence)"""
    else:
        structure = """Structure:
1. Direct answer (one paragraph, lead with the conclusion)
2. Key evidence (bulleted points supporting the answer)
3. What we don't know yet (gaps or uncertainties in the evidence)"""

    synthesis_tail_structure = """
Additionally, you MUST append three standardized sections at the very end of your response, using exact level-2 markdown headers:
## 研究者视角
(Synthesize key academic mechanisms, pathological characteristics, biomarker groups, and research context based on evidence.)
## 不能说过头的地方
(Clarify the boundaries of the evidence, specify extrapolation limits, state caution when applying case series to clinic, and note that this does not constitute professional veterinary advice.)
## 下一步
(Provide concrete next actions for further study or verification.)
"""

    translation_quality_control = """
Translation and Professional Terminology Rules:
- If answering in Chinese, you MUST use professional, natural, and standard veterinary and clinical trial terminology.
- Avoid mechanical, direct, or raw machine-translation styles.
- STRICTLY FORBIDDEN terms and their corrections:
  * NEVER use "无药性管理". Replace it with "非药物管理" (non-pharmacological management).
  * NEVER use "长期录下横灌运输转移" or similar nonsensical sentences. Translate it smoothly.
  * NEVER use "介阻极毒动物" or "前瞻瘦弱广泛筛". Use proper terms like "有毒物质/介导的疾病" or "前瞻性广泛筛查".
  * NEVER use "目标证据强烈的课题软性建议与限制". Use "高可信度证据的指南推荐与限制".
  * NEVER directly translate "RENAAL limits" out of context for cats. If mentioning human study limits, explain it clearly as cross-species extrapolation warning.
- Recommended professional terms:
  * non-pharmacological management -> 非药物管理
  * creatinine -> 肌酐
  * proteinuria -> 蛋白尿
  * clinical workflow -> 临床工作流
  * endpoint -> 终点指标
  * extrapolation -> （物种间）外推
  * prognosis -> 预后
  * retrospective study -> 回顾性研究
  * prospective study -> 前瞻性研究
  * biomarker -> 生物标记物
  * systolic blood pressure -> 收缩压
  * urine specific gravity (USG) -> 尿比重
"""

    system = f"""You are a research synthesis agent for a feline disease knowledge vault.
Write a sourced answer using only the loaded context.

{structure}

{synthesis_tail_structure}

{translation_quality_control}

{task_instructions}

Source weighting (each source card header shows weight tier):
- high (7-10): guidelines, regulations, reviews with deep extraction — prioritize these
- medium (4-7): original studies or partially extracted sources — use to support
- low (0-4): case reports, abstracts only — use cautiously, note limitations
When sources conflict, prefer higher-weighted sources. When citing low-weight sources,
acknowledge their evidence limitations (e.g., "based on a single case report" or
"from abstract-level evidence only").

Provenance tagging rules (apply to every factual claim):
  [quoted_fact: src-ckd-001]                     — direct quote or close paraphrase from a loaded source card
  [source_supported_conclusion: src-ckd-001]      — inference you draw from loaded evidence
  [llm_inference]                                — reasoning that goes beyond loaded evidence

CRITICAL: Every factual statement MUST end with a bracket-notation provenance tag.
Do NOT cite sources in prose style like "(src-hcm-001)" or "from src-hcm-001" — these
are invisible to provenance tracking. Always use the bracket format:
  [quoted_fact: src-hcm-001] or [source_supported_conclusion: src-hcm-001, src-hcm-009]
If you mention a source ID anywhere in the text, it MUST also appear inside a bracket tag.
An answer with zero bracket-tagged source IDs will fail acceptance checks.

Use the example IDs above only if those exact source cards appear in the loaded context.
Never output placeholder IDs such as src-id, src-id1, or src-id2.
Only source-card IDs beginning with `src-` may appear inside provenance tags.
Compiled topic pages are navigation/synthesis context, not source cards: never cite a
topic page with [quoted_fact: ...] or [source_supported_conclusion: ...].

Do NOT include a footer listing files loaded or source cards cited — the app handles source display.

Figure instructions (applies when images are provided):
- If figures are provided alongside the context, describe what each figure shows and
  integrate the visual evidence with your text synthesis.
- Cite the loaded source ID for each figure you reference, for example
  [quoted_fact: src-ckd-001] or [source_supported_conclusion: src-ckd-001].
- If a figure does not visibly support your answer, do not force a reference — state
  what it shows and note that it was not directly relevant to this question.
- Never describe figures that were not provided.

Critical constraints:
- Answer in {answer_language}. Match the user's language unless the user explicitly asks otherwise.
- Only cite source IDs that appear in the loaded context. Never invent IDs.
- If you cannot find a citation for a claim, tag it [llm_inference].
- Distinguish carefully between what the evidence says and what you are inferring.
- STRICTLY FOLLOW all Translation and Professional Terminology Rules. NEVER use forbidden terms like "无药性管理" or "长期录下横灌运输转移" under any circumstances."""

    use_vision = (
        VISION_INTEGRATION_ENABLED
        and resolved_assets
        and hasattr(client, "messages")  # Anthropic SDK only
    )

    if use_vision:
        import base64
        attached = resolved_assets[:VISION_FIGURE_CAP]
        content_blocks: list[dict] = [
            {"type": "text", "text": f"Question: {question}\n\n--- Loaded context ---\n{loaded_context}"}
        ]
        _EXT_TO_MEDIA_TYPE = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
            ".webp": "image/webp",
        }
        for asset in attached:
            suffix = asset["path"].suffix.lower()
            media_type = _EXT_TO_MEDIA_TYPE.get(suffix, "image/png")
            try:
                img_data = base64.b64encode(asset["path"].read_bytes()).decode()
            except OSError as e:
                print(f"[warn] Could not read figure {asset['rel']}: {e}", file=sys.stderr)
                continue
            content_blocks.append({
                "type": "image",
                "source": {"type": "base64", "media_type": media_type, "data": img_data},
            })

        print(f"[info] Vision: attaching {len(attached)} figure(s)", file=sys.stderr)
        resp = client.messages.create(
            model=model, max_tokens=SYNTHESIS_MAX_TOKENS,
            system=system,
            messages=[{"role": "user", "content": content_blocks}],
        )
        answer = resp.content[0].text

        # Mark which attached figures were actually referenced in the answer.
        # A figure is considered described if its source_id appears anywhere in
        # the answer text (i.e. in a provenance tag such as [quoted_fact: src-ckd-001]).
        figures_used = [
            {
                "source_id": a["source_id"],
                "file": a["rel"],
                "described_in_answer": a["source_id"] in answer,
            }
            for a in attached
        ]
        return answer, figures_used

    # Text-only path (Ollama, OpenRouter, or no assets on disk yet)
    answer = _chat(
        client, model, system,
        [{"role": "user", "content": f"Question: {question}\n\n--- Loaded context ---\n{loaded_context}"}],
        SYNTHESIS_MAX_TOKENS,
    )
    return answer, []


# ---------------------------------------------------------------------------
# File loading helpers
# ---------------------------------------------------------------------------

def _read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        print(f"[warn] Could not read {path}: {e}", file=sys.stderr)
        return ""


def _classify_page_family(rel: str) -> str:
    """Map a vault-relative path to a coarse answer-surface family label."""
    lowered = rel.lower()
    families = [
        ("mechanism-overview", "mechanism-overview"),
        ("endpoint-handbook", "endpoint-handbook"),
        ("risk-and-recognition", "risk-and-recognition"),
        ("translation-brief", "translation-brief"),
        ("regulatory-brief", "regulatory-brief"),
        ("synthesis-index", "synthesis-index"),
        ("current-state-dashboard", "current-state-dashboard"),
        ("verify-a-claim", "verify-a-claim"),
        ("disease-module-maturity-ladder", "disease-module-maturity-ladder"),
        ("src-reg-", "src-reg-source"),
    ]
    for needle, label in families:
        if needle in lowered:
            return label
    return "unknown"


def _render_loaded_paths_meta(loaded_paths: set[Path], vault_root: Path) -> str:
    """Serialize loaded vault-relative paths for stderr metadata."""
    rels: list[str] = []
    for path in sorted(loaded_paths):
        try:
            rels.append(str(path.relative_to(vault_root)))
        except ValueError:
            continue
    return ",".join(rels) if rels else "(none)"


# ---------------------------------------------------------------------------
# Write-back
# ---------------------------------------------------------------------------

def write_back(
    answer: str,
    question: str,
    disease: str,
    question_type: str,
    hops_used: int,
    files_loaded: list[Path],
    vault_root: Path,
    figures_used: Optional[list[dict]] = None,
) -> Path:
    """
    Write answer to outputs/qa/ with validated frontmatter.
    Aborts (raises ValueError) if required frontmatter keys are missing.
    """
    source_ids = parse_source_ids_from_answer(answer)
    confidence = compute_confidence(answer)

    slug = build_slug(question)
    today_str = date.today().isoformat()
    today_compact = today_str.replace("-", "")
    doc_id = f"qa-{disease}-{slug}-{today_compact}"

    files_loaded_rel = [str(p.relative_to(vault_root)) for p in files_loaded]

    fm = {
        "id": doc_id,
        "type": "output",
        "output_kind": "qa",
        "language": "en",
        "topic": disease,
        "question": question,
        "question_type": question_type,
        "source_ids": source_ids,
        "generated_at": today_str,
        "verification_status": "compiled",
        "decision_grade": "no",
        "language_qa_status": "not_applicable",
        "owner": "query-agent",
        "status": "draft",
        "hops": hops_used,
        "confidence": confidence,
        "write_back_reviewed": False,
        "files_loaded": files_loaded_rel,
        "evidence_policy": {
            "quoted_fact": [],
            "source_supported_conclusion": [],
            "llm_inference": [],
        },
    }

    if figures_used:
        fm["figures_used"] = figures_used

    missing = validate_frontmatter(fm)
    if missing:
        raise ValueError(f"Frontmatter validation failed — missing keys: {missing}")

    out_dir = vault_root / OUTPUTS_QA_REL
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{doc_id}.md"

    content = render_frontmatter(fm) + "\n\n" + f"# {question}\n\n" + answer
    out_path.write_text(content, encoding="utf-8")
    return out_path


# ---------------------------------------------------------------------------
# Inbox write-back (Karpathy write-back loop: outputs → inbox → human review → topics)
# ---------------------------------------------------------------------------

def write_to_inbox(
    answer: str,
    question: str,
    disease: str,
    question_type: str,
    vault_root: Path,
    figures_used: Optional[list[dict]] = None,
) -> Path:
    """
    Write a synthesis output to inbox/{disease}/ for human review.
    This feeds the write-back loop: Q&A outputs land here, get reviewed,
    and if approved, promote into topics/ or entities/.

    File naming: {date}-{question_type}-{slug}.md
    """
    slug = build_slug(question)
    today_str = date.today().isoformat()
    filename = f"{today_str}-{question_type}-{slug}.md"

    inbox_dir = vault_root / "inbox" / disease
    inbox_dir.mkdir(parents=True, exist_ok=True)
    out_path = inbox_dir / filename

    source_ids = parse_source_ids_from_answer(answer)
    confidence = compute_confidence(answer)

    escaped_question = question.replace('"', '\\"')
    header = f"""---
id: inbox-{disease}-{slug}-{today_str.replace('-', '')}
type: inbox
topic: {disease}
question: "{escaped_question}"
question_type: {question_type}
source_ids: [{', '.join(source_ids)}]
generated_at: {today_str}
confidence: {confidence}
review_status: pending
promoted_to: null
---

# {question}

"""
    content = header + answer
    out_path.write_text(content, encoding="utf-8")
    return out_path


def _extract_frontmatter_block(text: str) -> tuple[dict[str, object], str]:
    """Parse the small YAML subset used by vault QA and inbox files."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text

    frontmatter: dict[str, object] = {}
    lines = text[3:end].splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.startswith((" ", "\t")) or ":" not in line:
            i += 1
            continue

        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()

        if raw_value == "":
            items: list[str] = []
            j = i + 1
            while j < len(lines) and lines[j].lstrip().startswith("- "):
                items.append(lines[j].lstrip()[2:].strip().strip("\"'"))
                j += 1
            frontmatter[key] = items
            i = j
            continue

        if raw_value.startswith("[") and raw_value.endswith("]"):
            inner = raw_value[1:-1].strip()
            frontmatter[key] = [
                item.strip().strip("\"'")
                for item in inner.split(",")
                if item.strip()
            ]
        else:
            frontmatter[key] = raw_value.strip("\"'")
        i += 1

    return frontmatter, text[end + 4 :].lstrip()


def list_saved_answers(
    vault_root: Path,
    limit: int = 5,
    disease: Optional[str] = None,
) -> list[dict[str, object]]:
    """
    Return recent saved reader answers from outputs/qa/ and inbox/{disease}/.

    The rejected inbox subtree is intentionally ignored; it contains abandoned
    migration artifacts, not reader-facing answers.
    """
    candidates: list[tuple[str, Path, str]] = []

    qa_dir = vault_root / OUTPUTS_QA_REL
    if qa_dir.exists():
        candidates.extend(("saved", path, "outputs/qa") for path in qa_dir.glob("*.md"))

    inbox_dir = vault_root / "inbox"
    if inbox_dir.exists():
        for child in inbox_dir.iterdir():
            if not child.is_dir() or child.name == "rejected":
                continue
            candidates.extend(("inbox", path, f"inbox/{child.name}") for path in child.glob("*.md"))

    answers: list[dict[str, object]] = []
    for state, path, collection in candidates:
        try:
            text = path.read_text(encoding="utf-8")
            mtime = path.stat().st_mtime
        except (OSError, UnicodeDecodeError):
            continue

        frontmatter, body = _extract_frontmatter_block(text)
        topic = str(frontmatter.get("topic") or "unknown")
        if disease and topic != disease:
            continue

        question = str(frontmatter.get("question") or "")
        if not question:
            heading = re.search(r"^#\s+(.+)$", body, re.M)
            question = heading.group(1).strip() if heading else path.stem

        source_ids = frontmatter.get("source_ids") or []
        if not isinstance(source_ids, list):
            source_ids = []

        answer_text = re.sub(r"^#\s+.+\n+", "", body, count=1).strip()
        answers.append({
            "question": question,
            "topic": topic,
            "question_type": str(frontmatter.get("question_type") or "unknown"),
            "confidence": str(frontmatter.get("confidence") or "unknown"),
            "source_ids": source_ids,
            "generated_at": str(frontmatter.get("generated_at") or ""),
            "review_status": str(frontmatter.get("review_status") or state),
            "state": state,
            "collection": collection,
            "file": str(path.relative_to(vault_root)),
            "answer_preview": answer_text[:700],
            "_mtime": mtime,
        })

    answers.sort(key=lambda item: (str(item["generated_at"]), float(item["_mtime"])), reverse=True)
    for item in answers:
        item.pop("_mtime", None)
    return answers[:limit]


# ---------------------------------------------------------------------------
# Shared query engine (DRY core used by main() and app.py)
# ---------------------------------------------------------------------------

class NoSourceCardsLoadedError(RuntimeError):
    """Raised when routing/search fails to load any source cards for synthesis."""


def run_local_query_core(
    question: str,
    vault_root: Path,
    source_index: dict[str, Path],
    source_weights: Optional[dict[str, dict]] = None,
    disease_hint: Optional[str] = None,
    preferred_source_ids: Optional[list[str]] = None,
    search_limit: int = 8,
    on_status: Optional[Callable[[str], None]] = None,
) -> dict:
    """No-API vault lookup for simple inquiries and evidence-gap checks."""
    def _status(msg: str) -> None:
        if on_status:
            on_status(msg)

    chinese = prefers_chinese(question)
    disease = disease_hint or infer_disease_from_question(question)
    question_type = heuristic_question_type(question)
    if question_type == "unknown":
        question_type = "local_search"

    research_trace: list[dict] = []

    def add_trace(step: str, detail: str, items: Optional[list[dict]] = None) -> None:
        entry = {"step": step, "detail": detail}
        if items is not None:
            entry["items"] = items
        research_trace.append(entry)

    add_trace("Interpreted query", f"disease={disease}; question_type={question_type}; engine=local")

    _status("Searching local vault...")
    disease_search_terms = {
        "obesity": "obesity body condition weight loss",
        "cancer": "cancer tumor carcinoma lymphoma sarcoma",
        "diabetes": "diabetes diabetic glucose insulin",
        "fcv": "FCV calicivirus",
    }
    search_question = question
    if disease in disease_search_terms and disease_search_terms[disease] not in question.lower():
        search_question = f"{question} {disease_search_terms[disease]}"
    raw_results, raw_terms = aggregate_vault_search(search_question, vault_root, scope="raw", limit=search_limit)
    topic_results, topic_terms = aggregate_vault_search(search_question, vault_root, scope="topics", limit=search_limit)
    terms = []
    for term in raw_terms + topic_terms:
        if term not in terms:
            terms.append(term)
    results = (raw_results[: max(4, search_limit // 2)] + topic_results[: max(4, search_limit // 2)])[:search_limit]
    add_trace(
        "Searched vault",
        f"terms={', '.join(terms) if terms else question}; results={len(results)}; api_calls=0",
        [
            {
                "file": r["file"],
                "id": r.get("id") or "",
                "matches": r.get("score", r.get("matches", 0)),
                "terms": ", ".join(r.get("matched_terms", [])),
            }
            for r in results[:search_limit]
        ],
    )

    loaded_paths: set[Path] = set()
    loaded_source_ids: list[str] = []
    selected_results: list[dict] = []

    def include_result(result: dict) -> None:
        rel = result["file"]
        path = (vault_root / rel).resolve()
        try:
            path.relative_to(vault_root.resolve())
        except ValueError:
            return
        if not path.exists():
            return
        loaded_paths.add(path)
        sid = result.get("id") or ""
        if sid.startswith("src-") and sid not in loaded_source_ids:
            loaded_source_ids.append(sid)
        if result not in selected_results:
            selected_results.append(result)

    for result in results:
        sid = result.get("id") or ""
        if sid.startswith("src-"):
            path = source_index.get(sid)
            if path and (disease == "unknown" or source_card_disease_matches(path, disease)):
                include_result(result)
        elif len(selected_results) < 3:
            include_result(result)
        if len(selected_results) >= 6:
            break

    if preferred_source_ids:
        preferred_items: list[dict] = []
        for sid in preferred_source_ids:
            path = source_index.get(sid)
            loaded = False
            if path and path.exists():
                loaded_paths.add(path)
                if sid not in loaded_source_ids:
                    loaded_source_ids.append(sid)
                loaded = True
            preferred_items.append({"source_id": sid, "loaded": loaded})
        add_trace(
            "Applied selected source",
            f"{sum(1 for item in preferred_items if item['loaded'])}/{len(preferred_items)} preferred sources loaded",
            preferred_items,
        )

    add_trace(
        "Loaded evidence",
        f"source_cards={len(loaded_source_ids)}; files={len(loaded_paths)}; api_calls=0",
        [{"source_id": sid} for sid in loaded_source_ids[:12]],
    )

    lower_question = question.lower()
    exact_needles = [term for term in terms if term.lower() in {"sirna", "rnai"}]
    disease_specific_hits = [
        sid for sid in loaded_source_ids
        if sid in source_index and (disease == "unknown" or source_card_disease_matches(source_index[sid], disease))
    ]
    has_direct_rare_term_hit = False
    for result in selected_results:
        snippets_text = " ".join(result.get("snippets", []))
        if any(needle.lower() in snippets_text.lower() or needle.lower() in str(result.get("title", "")).lower() for needle in exact_needles):
            has_direct_rare_term_hit = True
            break

    cited = ", ".join(disease_specific_hits[:3])
    if not cited and loaded_source_ids:
        cited = ", ".join(loaded_source_ids[:3])

    if chinese:
        if exact_needles and disease != "unknown" and not has_direct_rare_term_hit:
            direct = (
                f"本地库里目前没有找到“{question}”的直接证据；尤其没有找到同时支持 `{disease}` 与 "
                f"`{', '.join(exact_needles)}` 的 source card。这个结果没有调用 API。"
            )
        elif disease_specific_hits:
            direct = f"本地库找到了可读证据入口，但这是检索结果，不是 API 综合回答。这个结果没有调用 API。"
        else:
            direct = "本地库没有找到足够匹配的 source card。这个结果没有调用 API。"

        evidence_lines = []
        for result in selected_results[:5]:
            sid = result.get("id") or result["file"]
            title = result.get("title") or result["file"]
            terms_hit = ", ".join(result.get("matched_terms", []))
            evidence_lines.append(f"- `{sid}` — {title}；命中词：{terms_hit or 'n/a'}")
        if not evidence_lines:
            evidence_lines.append("- 没有本地命中。")

        cited_tag = " [llm_inference]" if exact_needles and not has_direct_rare_term_hit else (f" [source_supported_conclusion: {cited}]" if cited else " [llm_inference]")
        answer = (
            f"{direct}{cited_tag}\n\n"
            "## 本地命中\n"
            + "\n".join(evidence_lines)
            + "\n\n## 和 Google 搜索的差别\n"
            "- 这里先查的是本项目已经入库、带 source card / topic page 的材料；不会把未入库网页当证据。\n"
            "- 免费检索模式只告诉你“库里有什么/没有什么”，不会花 OpenRouter 或 Anthropic token。\n"
            "- 如果要做跨文献发现或生成研究判断，再切到 API synthesis；那时应把 Research trace 当作花费是否值得的审计依据。\n\n"
            "## 下一步\n"
            "如果目标是评估一个新方向，先补一轮 PubMed/DOI source intake；在没有 siRNA-feline-obesity 证据卡前，不应生成药效结论。"
        )
    else:
        if exact_needles and disease != "unknown" and not has_direct_rare_term_hit:
            direct = (
                f"The local vault does not currently contain direct evidence for `{question}`, "
                f"especially no source card that connects `{disease}` with `{', '.join(exact_needles)}`. No API call was made."
            )
        elif disease_specific_hits:
            direct = "The local vault found relevant evidence entry points. This is retrieval, not API synthesis. No API call was made."
        else:
            direct = "The local vault did not find enough matching source-card evidence. No API call was made."

        evidence_lines = []
        for result in selected_results[:5]:
            sid = result.get("id") or result["file"]
            title = result.get("title") or result["file"]
            terms_hit = ", ".join(result.get("matched_terms", []))
            evidence_lines.append(f"- `{sid}` — {title}; matched terms: {terms_hit or 'n/a'}")
        if not evidence_lines:
            evidence_lines.append("- No local hits.")

        cited_tag = " [llm_inference]" if exact_needles and not has_direct_rare_term_hit else (f" [source_supported_conclusion: {cited}]" if cited else " [llm_inference]")
        answer = (
            f"{direct}{cited_tag}\n\n"
            "## Local hits\n"
            + "\n".join(evidence_lines)
            + "\n\n## Difference from Google search\n"
            "- This searches only vault materials that already have source cards or topic pages.\n"
            "- Free retrieval tells you what is or is not in the vault without spending API tokens.\n"
            "- Use API synthesis only when you need a cross-source judgment and can inspect the Research trace.\n\n"
            "## Next step\n"
            "If this is a new research direction, run PubMed/DOI intake first; do not generate efficacy conclusions before source cards exist."
        )

    answer = sanitize_provenance_tags(answer, loaded_source_ids)
    add_trace("Returned local answer", f"mode=free_retrieval; api_calls=0; results={len(selected_results)}")

    return {
        "answer": answer,
        "figures_used": [],
        "disease": disease,
        "question_type": question_type,
        "answer_mode": "local_search",
        "hops_used": 0,
        "loaded_paths": loaded_paths,
        "loaded_source_ids": loaded_source_ids,
        "first_family_loaded": "local-search",
        "research_trace": research_trace,
        "est_tokens": 0,
    }


def run_query_core(
    client,
    question: str,
    vault_root: Path,
    source_index: dict[str, Path],
    source_weights: Optional[dict[str, dict]] = None,
    disease_hint: Optional[str] = None,
    preferred_source_ids: Optional[list[str]] = None,
    max_hops: int = 3,
    model: str = MODEL,
    on_status: Optional[Callable[[str], None]] = None,
    allow_external_search: bool = False,
) -> dict:
    """
    Route, hop, and synthesize a research question.
    Returns a result dict:
      {
        "answer": str,
        "figures_used": list[dict],
        "disease": str,
        "question_type": str,
        "hops_used": int,
        "loaded_paths": set[Path],
        "est_tokens": int,
      }
    on_status(msg: str) is called for progress updates (optional).
    Raises SystemExit only on disease routing failure for non-synthesis questions.
    """
    def _status(msg: str) -> None:
        if on_status:
            on_status(msg)

    loaded_paths: set[Path] = set()
    loaded_path_order: list[Path] = []
    context_parts: list[str] = []
    frontmatter_source_ids: dict[Path, list[str]] = {}
    first_family_loaded: Optional[str] = None
    research_trace: list[dict] = []

    def add_trace(step: str, detail: str, items: Optional[list[dict]] = None) -> None:
        """Record an auditable retrieval/synthesis step for the UI."""
        entry = {"step": step, "detail": detail}
        if items is not None:
            entry["items"] = items
        research_trace.append(entry)

    def resolve_vault_path(rel: str) -> Optional[Path]:
        direct = (vault_root / rel).resolve()
        try:
            direct.relative_to(vault_root.resolve())
        except ValueError:
            direct = None
        else:
            if direct.exists():
                return direct

        candidates: list[Path] = []
        for base in loaded_path_order:
            resolved = resolve_link(base, rel)
            if not resolved:
                continue
            try:
                resolved.relative_to(vault_root.resolve())
            except ValueError:
                continue
            if resolved not in candidates:
                candidates.append(resolved)
        if candidates:
            return candidates[0]
        return None

    def try_load_path(rel: str) -> bool:
        nonlocal first_family_loaded
        p = resolve_vault_path(rel)
        if p is None:
            print(f"[warn] Not found, skipping: {rel}", file=sys.stderr)
            return False
        if p in loaded_paths:
            return False
        text = _read_file(p)
        if text:
            try:
                rel_from_root = str(p.relative_to(vault_root))
            except ValueError:
                rel_from_root = rel
            if question_type == "overview" and rel_from_root.startswith("topics/"):
                context_parts.append(compact_topic_page_context(rel_from_root, text))
            else:
                context_parts.append(f"--- {rel_from_root} ---\n{text}")
            loaded_paths.add(p)
            loaded_path_order.append(p)
            frontmatter_source_ids[p] = parse_source_ids_from_frontmatter(text)
            family = _classify_page_family(rel_from_root)
            if first_family_loaded is None and family != "unknown":
                first_family_loaded = family
            return True
        return False

    def try_load_source(src_id: str) -> bool:
        if src_id not in source_index:
            print(f"[warn] Source card not found: {src_id}", file=sys.stderr)
            return False
        p = source_index[src_id]
        if p in loaded_paths:
            return False
        text = _read_file(p)
        if text:
            rel = str(p.relative_to(vault_root))
            # Include weight tier if available
            weight_info = ""
            if source_weights and src_id in source_weights:
                w = source_weights[src_id]
                weight_info = f" | weight: {w['tier']} ({w['score']:.1f})"
            if question_type == "overview":
                context_parts.append(compact_source_card_context(src_id, rel, text, weight_info))
            else:
                context_parts.append(f"--- {rel} ({src_id}{weight_info}) ---\n{text}")
            loaded_paths.add(p)
            return True
        return False

    # Route
    _status("Routing question...")
    routing = router_call(client, question, disease_hint, vault_root, model=model)

    disease = disease_hint or routing.get("disease", "unknown")
    question_type = routing.get("question_type", "unknown")
    initial_files = routing.get("files_to_load", [])
    add_trace(
        "Interpreted query",
        f"disease={disease}; question_type={question_type}; initial_files={len(initial_files)}",
        [{"file": str(f)} for f in initial_files[:8]],
    )

    # Cross-disease queries (synthesis question_type) are allowed with unknown disease
    if disease == "unknown" and question_type != "synthesis":
        print(
            "\nCould not determine disease from question.\n"
            "Please specify with: --disease [ckd|hcm|fip|ibd|diabetes]\n"
            "Or use a cross-disease synthesis question.",
            file=sys.stderr,
        )
        raise SystemExit(1)

    initial_loaded: list[dict] = []
    for f in initial_files:
        loaded = try_load_path(f)
        initial_loaded.append({"file": str(f), "loaded": loaded})
        if loaded:
            print(f"[info] Loaded: {f}", file=sys.stderr)
    if initial_loaded:
        add_trace("Loaded routed files", f"{sum(1 for item in initial_loaded if item['loaded'])}/{len(initial_loaded)} files loaded", initial_loaded)

    # Search pre-heat: use full-text search to find relevant source cards
    # that the router might have missed. Only loads source cards (not topic pages)
    # to avoid polluting context with redundant wiki text.
    if SEARCH_AVAILABLE:
        _status("Searching vault...")
        search_scope = "raw" if disease != "unknown" else "all"
        search_limit = 3 if question_type == "overview" else 5
        search_results = vault_search(question, vault_root, scope=search_scope, limit=search_limit)
        search_trace_items: list[dict] = []
        for sr in search_results:
            loaded_by_search = False
            if sr["id"] and sr["id"].startswith("src-") and sr["id"] in source_index:
                if try_load_source(sr["id"]):
                    loaded_by_search = True
                    print(f"[info] Search pre-loaded: {sr['id']} ({sr['matches']} matches)", file=sys.stderr)
            search_trace_items.append({
                "file": sr["file"],
                "id": sr.get("id") or "",
                "matches": sr["matches"],
                "loaded": loaded_by_search,
            })
        add_trace(
            "Searched vault",
            f"scope={search_scope}; limit={search_limit}; results={len(search_results)}",
            search_trace_items,
        )

        # Check if local search is sparse and external search is allowed
        loaded_source_ids_after_search = [
            sid for sid, src_path in source_index.items() if src_path in loaded_paths
        ]
        if (
            allow_external_search
            and EXTERNAL_SEARCH_AVAILABLE
            and is_local_search_sparse(search_results, loaded_source_ids_after_search)
        ):
            _status("Local results sparse, searching PubMed/Crossref...")
            external_trace = build_external_search_trace(question, disease)
            add_trace(
                external_trace["step"],
                external_trace["detail"],
                external_trace["items"],
            )

    if preferred_source_ids:
        preferred_trace_items: list[dict] = []
        for sid in preferred_source_ids:
            loaded = sid in source_index and try_load_source(sid)
            preferred_trace_items.append({"source_id": sid, "loaded": loaded})
            if loaded:
                print(f"[info] User-preferred source pre-loaded: {sid}", file=sys.stderr)
        add_trace(
            "Applied selected source",
            f"{sum(1 for item in preferred_trace_items if item['loaded'])}/{len(preferred_trace_items)} preferred sources loaded",
            preferred_trace_items,
        )

    if question_type == "overview":
        loaded_source_ids_now = [
            sid for sid, src_path in source_index.items() if src_path in loaded_paths
        ]
        needed = max(0, OVERVIEW_MIN_SOURCE_CARDS - len(loaded_source_ids_now))
        if needed:
            preload_ids = source_ids_from_topic_frontmatter(
                loaded_path_order,
                frontmatter_source_ids,
                loaded_source_ids_now,
                needed,
            )
            preload_trace_items: list[dict] = []
            for sid in preload_ids:
                loaded = sid in source_index and try_load_source(sid)
                preload_trace_items.append({"source_id": sid, "loaded": loaded})
                if loaded:
                    print(f"[info] Overview baseline loaded source: {sid}", file=sys.stderr)
            if preload_trace_items:
                add_trace(
                    "Loaded overview baseline evidence",
                    (
                        f"target={OVERVIEW_MIN_SOURCE_CARDS}; "
                        f"already={len(loaded_source_ids_now)}; "
                        f"added={sum(1 for item in preload_trace_items if item['loaded'])}"
                    ),
                    preload_trace_items,
                )

    # Hop loop
    history: list[dict] = []
    hops_used = 0

    for hop in range(max_hops):
        loaded_context = "\n\n".join(context_parts)
        est_tokens = estimate_tokens(loaded_context)

        if est_tokens > CONTEXT_TOKEN_LIMIT:
            print(f"[info] Context limit (~{est_tokens} tokens), forcing synthesize", file=sys.stderr)
            break

        _status(f"Hop {hop + 1}/{max_hops} (~{est_tokens} tokens loaded)...")
        print(f"[info] Hop {hop + 1}/{max_hops} (~{est_tokens} tokens loaded)...", file=sys.stderr)
        action = hop_call(client, question, loaded_context, history, hop + 1, model=model)
        history.append({"role": "assistant", "content": json.dumps(action)})
        hops_used = hop + 1

        act = action.get("action")
        add_trace(
            f"Agent hop {hop + 1}",
            f"action={act}; est_tokens={est_tokens}",
            [
                {"file": str(f)} for f in action.get("files", [])[:8]
            ] + [
                {"source_id": str(sid)} for sid in action.get("source_ids", [])[:8]
            ],
        )
        if act == "synthesize":
            print("[info] Agent ready to synthesize", file=sys.stderr)
            break
        elif act == "load_more":
            for f in action.get("files", []):
                if try_load_path(f):
                    print(f"[info] Loaded: {f}", file=sys.stderr)
        elif act == "load_sources":
            for sid in action.get("source_ids", []):
                if try_load_source(sid):
                    print(f"[info] Loaded source: {sid}", file=sys.stderr)
        else:
            print(f"[warn] Unknown action '{act}', forcing synthesize", file=sys.stderr)
            break

    # Resolve figures from loaded source cards
    loaded_source_ids: list[str] = [
        sid for sid, src_path in source_index.items() if src_path in loaded_paths
    ]

    if not loaded_source_ids:
        fallback_ids: list[str] = []
        for path in loaded_path_order:
            for sid in frontmatter_source_ids.get(path, []):
                if sid not in fallback_ids:
                    fallback_ids.append(sid)
        fallback_cap = 4 if question_type == "overview" else 10
        if fallback_ids:
            print(
                f"[info] Fallback source preload from compiled pages: {fallback_ids[:fallback_cap]}",
                file=sys.stderr,
            )
            add_trace(
                "Fallback source preload",
                f"found={len(fallback_ids)}; cap={fallback_cap}",
                [{"source_id": sid} for sid in fallback_ids[:fallback_cap]],
            )
        for sid in fallback_ids[:fallback_cap]:
            if try_load_source(sid):
                print(f"[info] Fallback loaded source: {sid}", file=sys.stderr)

        loaded_source_ids = [
            sid for sid, src_path in source_index.items() if src_path in loaded_paths
        ]

    if not loaded_source_ids:
        raise NoSourceCardsLoadedError(
            "No source cards matched the routed context for this question."
        )
    add_trace(
        "Loaded evidence",
        f"source_cards={len(loaded_source_ids)}; files={len(loaded_paths)}",
        [{"source_id": sid} for sid in loaded_source_ids[:12]],
    )

    # Map question_type to preferred figure_type for relevance-sorted retrieval.
    # Note: figures with figure_type not in any value here (e.g. "pathology")
    # will be excluded when a hint is active. If a figure_type should be visible
    # for a question_type, add it here or use None (no filtering).
    _QTYPE_TO_FIGURE_TYPE: dict[str, Optional[str]] = {
        "mechanism": "mechanism",
        "endpoints": "outcome",
        "recognition": "imaging",
        "treatment": "outcome",
        "regulatory": "outcome",
        "synthesis": None,  # cross-disease synthesis: no filtering, show all figures
    }
    figure_type_hint = _QTYPE_TO_FIGURE_TYPE.get(question_type)

    resolved_assets: list[dict] = []
    if VISION_INTEGRATION_ENABLED and loaded_source_ids and question_type != "overview":
        resolved_assets = resolve_local_assets(
            loaded_source_ids, vault_root, figure_type_hint=figure_type_hint
        )
        if resolved_assets:
            print(
                f"[info] Vision: {len(resolved_assets)} verified figure(s) available from "
                f"{sorted(set(a['source_id'] for a in resolved_assets))}",
                file=sys.stderr,
            )
        else:
            print("[info] Vision: no verified figures on disk yet (extract PDFs to enable)", file=sys.stderr)
        add_trace(
            "Checked verified figures",
            f"available={len(resolved_assets)}; enabled={VISION_INTEGRATION_ENABLED}",
            [
                {"source_id": a.get("source_id", ""), "file": a.get("file", "")}
                for a in resolved_assets[:VISION_FIGURE_CAP]
            ],
        )

    # Synthesize
    loaded_context = "\n\n".join(context_parts)
    n_files = len(loaded_paths)
    est_tokens = estimate_tokens(loaded_context)
    _status(f"Synthesizing ({n_files} files, ~{est_tokens} tokens)...")
    print(f"[info] Synthesizing ({n_files} files, ~{est_tokens} tokens)...", file=sys.stderr)

    answer_mode = "overview" if question_type == "overview" else "research"
    add_trace(
        "Synthesized answer",
        f"mode={answer_mode}; files={n_files}; est_tokens={est_tokens}",
    )
    answer, figures_used = synthesis_call(
        client, question, loaded_context,
        resolved_assets=resolved_assets,
        model=model,
        answer_mode=answer_mode,
        question_type=question_type,
    )
    answer = sanitize_provenance_tags(answer, loaded_source_ids)

    return {
        "answer": answer,
        "figures_used": figures_used,
        "disease": disease,
        "question_type": question_type,
        "answer_mode": answer_mode,
        "hops_used": hops_used,
        "loaded_paths": loaded_paths,
        "loaded_source_ids": loaded_source_ids,
        "first_family_loaded": first_family_loaded or "unknown",
        "research_trace": research_trace,
        "est_tokens": est_tokens,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Query the feline research OS vault via an agent loop.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("question", help="Your research question")
    parser.add_argument("--disease", choices=["ckd", "hcm", "fip", "ibd", "diabetes"],
                        help="Specify disease to narrow routing")
    parser.add_argument("--write-back", action="store_true",
                        help="Write answer to outputs/qa/ after synthesis")
    parser.add_argument("--save-to-inbox", action="store_true",
                        help="Save answer to inbox/{disease}/ for human review (write-back loop)")
    parser.add_argument("--max-hops", type=int, default=3,
                        help="Maximum navigation hops before forced synthesis (default: 3)")
    parser.add_argument("--backend", choices=["anthropic", "ollama", "openrouter"], default="anthropic",
                        help="LLM backend: 'anthropic', 'ollama' (local), or 'openrouter'")
    parser.add_argument("--ollama-model", default=OLLAMA_MODEL,
                        help=f"Ollama model name (default: {OLLAMA_MODEL})")
    parser.add_argument("--openrouter-model", default=OPENROUTER_MODEL,
                        help=f"OpenRouter model name (default: {OPENROUTER_MODEL})")
    args = parser.parse_args()

    try:
        client = make_client(args.backend)
    except (ImportError, ValueError) as e:
        print(f"Missing dependency or config: {e}", file=sys.stderr)
        sys.exit(1)
    if args.backend == "ollama":
        active_model = args.ollama_model
    elif args.backend == "openrouter":
        active_model = args.openrouter_model
    else:
        active_model = MODEL
    print(f"[info] Backend: {args.backend}  model: {active_model}", file=sys.stderr)

    # Build source index (decision 1A: scan raw/ recursively)
    source_index = build_source_index(VAULT_ROOT)
    source_weights = build_source_weights(VAULT_ROOT)
    print(f"[info] Source index: {len(source_index)} cards indexed", file=sys.stderr)
    print(f"[info] Source weights: {len(source_weights)} cards weighted", file=sys.stderr)

    # Run query (routing → hops → synthesis via shared engine)
    print("[info] Routing...", file=sys.stderr)
    try:
        result = run_query_core(
            client, args.question, VAULT_ROOT, source_index,
            source_weights=source_weights,
            disease_hint=args.disease,
            max_hops=args.max_hops,
            model=active_model,
        )
    except NoSourceCardsLoadedError as e:
        print(f"[error] {e}", file=sys.stderr)
        print(
            "No source cards matched your question. Try rephrasing or pass --disease "
            "[ckd|hcm|fip|ibd|diabetes].",
            file=sys.stderr,
        )
        sys.exit(1)
    answer = result["answer"]
    figures_used = result["figures_used"]
    disease = result["disease"]
    question_type = result["question_type"]
    hops_used = result["hops_used"]
    loaded_paths = result["loaded_paths"]
    first_family_loaded = result.get("first_family_loaded", "unknown")

    print(f"[meta] ROUTER_QTYPE={question_type}", file=sys.stderr)
    print(f"[meta] ROUTER_DISEASE={disease}", file=sys.stderr)
    print(f"[meta] FIRST_FAMILY={first_family_loaded}", file=sys.stderr)
    print(f"[meta] LOADED_PATHS={_render_loaded_paths_meta(loaded_paths, VAULT_ROOT)}", file=sys.stderr)

    print("\n" + answer + "\n")

    # --- Figure footer + caption write-back ---
    described = [f for f in figures_used if f.get("described_in_answer")]
    if described:
        print("FIGURES REFERENCED IN ANSWER:")
        for fig in described:
            print(f"  [{fig['source_id']}] {fig['file']}")
            # Caption write-back waits for synthesis_call() to return per-figure
            # caption text; until then, figures are cited without inventing captions.
            caption = fig.get("caption", "")
            if caption:
                ok = enrich_source_card_with_caption(
                    fig["source_id"], fig["file"], caption, VAULT_ROOT
                )
                if ok:
                    print(f"  [caption written] {fig['source_id']}", file=sys.stderr)
        print()

    # --- Write-back (opt-in) ---
    if args.write_back:
        try:
            out_path = write_back(
                answer=answer,
                question=args.question,
                disease=disease,
                question_type=question_type,
                hops_used=hops_used,
                files_loaded=list(loaded_paths),
                vault_root=VAULT_ROOT,
                figures_used=figures_used if figures_used else None,
            )
            rel = out_path.relative_to(VAULT_ROOT)
            print(f"[written] {rel}", file=sys.stderr)
        except ValueError as e:
            print(f"[error] Write-back aborted: {e}", file=sys.stderr)
            sys.exit(1)

    # --- Inbox write-back (opt-in, feeds the human review loop) ---
    if args.save_to_inbox:
        inbox_path = write_to_inbox(
            answer=answer,
            question=args.question,
            disease=disease,
            question_type=question_type,
            vault_root=VAULT_ROOT,
            figures_used=figures_used if figures_used else None,
        )
        rel = inbox_path.relative_to(VAULT_ROOT)
        print(f"[inbox] {rel}", file=sys.stderr)


if __name__ == "__main__":
    main()
