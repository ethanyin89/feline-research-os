#!/usr/bin/env python3
"""
scripts/briefing_ui.py — Disease Briefing layer UI for the three-layer architecture.

Disease Briefing provides structured static knowledge pages:
- Loads pre-compiled briefing files from outputs/briefings/
- Renders with collapsible sections and table of contents
- Links to Research Workspace for dynamic research

This is Layer 2 of the three-layer architecture:
  Quick Start → Disease Briefing → Research Workspace
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Optional, NamedTuple
from dataclasses import dataclass, field


VAULT_ROOT = Path(__file__).parent.parent
BRIEFINGS_DIR = VAULT_ROOT / "outputs" / "briefings"


@dataclass
class BriefingFile:
    """Metadata about a briefing file."""
    path: Path
    disease: str
    language: str  # "zh" or "en"
    date: str
    title: str
    source_ids: list[str] = field(default_factory=list)


def list_available_briefings() -> dict[str, list[BriefingFile]]:
    """
    List all available briefing files grouped by disease.

    Returns:
        Dict mapping disease code to list of BriefingFile objects
    """
    result: dict[str, list[BriefingFile]] = {}

    if not BRIEFINGS_DIR.exists():
        return result

    # Pattern: out-{disease}-briefing-{date}-{round}-{lang}.md
    # Example: out-hcm-briefing-20260410-round1-zh.md
    pattern = re.compile(r"out-(\w+)-briefing-(\d+)-.*?-(\w+)\.md$")

    for file_path in BRIEFINGS_DIR.glob("out-*-briefing-*.md"):
        # Skip working files
        if "working" in file_path.name:
            continue

        match = pattern.match(file_path.name)
        if not match:
            continue

        disease = match.group(1).lower()
        date = match.group(2)
        language = match.group(3)

        # Parse title from file
        try:
            content = file_path.read_text(encoding="utf-8")
            title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
            title = title_match.group(1) if title_match else f"{disease.upper()} Briefing"

            # Parse source_ids from frontmatter
            source_ids = []
            fm_match = re.search(r"source_ids:\s*\[([^\]]+)\]", content)
            if fm_match:
                source_ids = [s.strip() for s in fm_match.group(1).split(",")]
        except Exception:
            title = f"{disease.upper()} Briefing"
            source_ids = []

        briefing = BriefingFile(
            path=file_path,
            disease=disease,
            language=language,
            date=date,
            title=title,
            source_ids=source_ids,
        )

        if disease not in result:
            result[disease] = []
        result[disease].append(briefing)

    # Sort each disease's briefings by date (newest first)
    for disease in result:
        result[disease].sort(key=lambda b: b.date, reverse=True)

    return result


def get_briefing(disease: str, language: str = "zh") -> Optional[BriefingFile]:
    """
    Get the latest briefing file for a disease.

    Args:
        disease: Disease code (hcm, ckd, fip, ibd, diabetes)
        language: "zh" for Chinese, "en" for English

    Returns:
        BriefingFile or None if not found
    """
    all_briefings = list_available_briefings()
    disease_briefings = all_briefings.get(disease.lower(), [])

    # Filter by language
    lang_briefings = [b for b in disease_briefings if b.language == language]

    if lang_briefings:
        return lang_briefings[0]  # Return newest

    # Fallback to other language if preferred not available
    if disease_briefings:
        return disease_briefings[0]

    return None


def parse_briefing_sections(content: str) -> list[tuple[str, str]]:
    """
    Parse briefing content into sections for collapsible rendering.

    Returns:
        List of (section_title, section_content) tuples
    """
    # Remove frontmatter
    if content.startswith("---"):
        end_idx = content.find("\n---", 3)
        if end_idx != -1:
            content = content[end_idx + 4:].strip()

    # Split by ## headers
    sections = []
    current_title = "Overview"
    current_content = []

    for line in content.split("\n"):
        if line.startswith("## "):
            # Save previous section
            if current_content:
                sections.append((current_title, "\n".join(current_content).strip()))
            current_title = line[3:].strip()
            current_content = []
        elif line.startswith("# "):
            # Skip top-level title
            continue
        else:
            current_content.append(line)

    # Save last section
    if current_content:
        sections.append((current_title, "\n".join(current_content).strip()))

    return sections


def sanitize_user_facing_markdown(text: str) -> str:
    """Remove raw local file names, .md file links, and paths from user-facing markdown.
    Also replace internal source IDs with external links if available."""
    import re
    from pathlib import Path
    
    # 0. Completely remove the "Derived from:" / "源自：" block
    text = re.sub(r"(?i)Derived from:\s*-\s*[^\n]+(?:\n|$)", "", text)
    text = re.sub(r"提取自：\s*-\s*[^\n]+(?:\n|$)", "", text)
    text = re.sub(r"源自：\s*-\s*[^\n]+(?:\n|$)", "", text)
    
    # 1. Clean markdown links pointing to local files (e.g., [file.md](file.md))
    def replace_md_link(match):
        label = match.group(1)
        url = match.group(2)
        if url.endswith(".md") or "/" in url or "\\" in url:
            stem = Path(url).stem
            if stem.startswith("src-"):
                return f"**{stem.upper()}**"
            
            # For general md links, format human-friendly title
            label_clean = label.replace(".md", "").replace("-zh", "").replace("-", " ")
            label_clean = " ".join(w.capitalize() for w in label_clean.split())
            acronyms = {"Hcm": "HCM", "Ckd": "CKD", "Fip": "FIP", "Ibd": "IBD", "Fcv": "FCV", "Working": "Working Draft", "En": "(English)", "Zh": "(Chinese)"}
            label_clean = " ".join(acronyms.get(w, w) for w in label_clean.split())
            return f"**{label_clean}**"
        return match.group(0)
    
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_md_link, text)
    
    # 2. Clean standalone md files or paths
    text = re.sub(r"\b\w+-\w+-briefing-\d+-[\w-]+\.md\b", "内部知识库简报", text)
    text = re.sub(r"\btopics/[\w/-]+\.md\b", lambda m: f"**{Path(m.group(0)).stem.replace('-', ' ').title()}**", text)
    text = re.sub(r"\braw/papers/[\w/-]+\.md\b", lambda m: f"**{Path(m.group(0)).stem.upper()}**", text)

    # 3. Replace source IDs with external links
    source_ids = list(set(re.findall(r"\bsrc-[a-z]+-\d{3}\b", text)))
    if source_ids:
        try:
            from core.source_metadata import load_source_metadata
            metadata_list = load_source_metadata(VAULT_ROOT, source_ids)
            id_to_meta = {m["id"]: m for m in metadata_list}
            
            def replace_src(match):
                sid = match.group(0)
                meta = id_to_meta.get(sid, {})
                title = meta.get("title") or sid.upper()
                if len(title) > 60:
                    title = title[:57] + "..."
                url = meta.get("url") or meta.get("doi")
                if url:
                    if not url.startswith("http"):
                        url = f"https://doi.org/{url}"
                    return f"[{title}]({url})"
                return f"**{title}**"
            
            text = re.sub(r"\bsrc-[a-z]+-\d{3}\b", replace_src, text)
        except Exception:
            pass

    return text


def render_briefing_page(briefing: BriefingFile, st_module) -> None:
    """
    Render a briefing file as a Streamlit page.

    Args:
        briefing: BriefingFile to render
        st_module: Streamlit module (passed to avoid circular imports)
    """
    st = st_module

    try:
        content = briefing.path.read_text(encoding="utf-8")
    except Exception as e:
        st.error(f"Failed to load briefing: {e}")
        return

    # Header
    st.title(briefing.title)
    st.caption(f"疾病：{briefing.disease.upper()} | 更新日期：{briefing.date}")

    # Parse sections
    sections = parse_briefing_sections(content)

    if not sections:
        st.warning("No content found in briefing file.")
        return

    # Render table of contents
    with st.expander("📑 目录", expanded=False):
        for title, _ in sections:
            st.markdown(f"- {title}")

    # Render sections as expanders
    for i, (title, section_content) in enumerate(sections):
        # First section expanded by default
        with st.expander(f"📄 {title}", expanded=True):
            st.markdown(sanitize_user_facing_markdown(section_content))

    # Render deep extraction source cards
    if briefing.source_ids:
        st.markdown("### 🔬 深度提炼文献卡片" if briefing.language == "zh" else "### 🔬 Deep Extraction Source Cards")
        from deep_extraction import has_deep_extraction
        
        # Build source titles map
        try:
            from query import build_source_titles
            source_titles = build_source_titles(VAULT_ROOT)
        except Exception:
            source_titles = {}

        cols = st.columns(2)
        for idx, sid in enumerate(briefing.source_ids):
            with cols[idx % 2]:
                title = source_titles.get(sid, sid)
                has_de = has_deep_extraction(sid)
                de_suffix = " (含深度提炼)" if has_de and briefing.language == "zh" else " (Deep extracted)" if has_de else ""
                
                if st.button(f"📄 {title}{de_suffix}", key=f"briefing-src-{sid}", use_container_width=True):
                    if has_de:
                        st.query_params["detail"] = sid
                        st.rerun()
                    else:
                        st.info(f"文献 {title} 暂无深度提炼内容。" if briefing.language == "zh" else f"Source {title} does not have deep extraction yet.")

    # Navigation to Research Workspace
    st.divider()
    st.markdown("**继续研究**")

    col1, col2 = st.columns(2)
    with col1:
        if st.button(
            f"🔬 启动 {briefing.disease.upper()} 研究工作台",
            key=f"briefing-to-workspace-{briefing.disease}",
            use_container_width=True
        ):
            # Queue a task-oriented research mode query
            disease_lower = briefing.disease.lower()
            research_queries = {
                "hcm": "构建 feline HCM 近三年证据地图",
                "ckd": "比较 CKD 诊断与分期指标的研究价值",
                "fip": "梳理 FIP 治疗研究的药效终点",
                "diabetes": "提炼猫糖尿病模型的关键评价指标",
                "ibd": "提炼猫炎症性肠病与小细胞淋巴瘤鉴别诊断的研究发现",
            }
            research_query = research_queries.get(disease_lower, f"提取 {briefing.disease.upper()} 最新机制与标志物研究")
            st.session_state.pending_question = research_query
            st.session_state.show_briefing = None
            st.rerun()

    with col2:
        if st.button(
            "← 返回主页",
            key=f"briefing-back-{briefing.disease}",
            use_container_width=True
        ):
            st.session_state.show_briefing = None
            st.rerun()


def get_available_diseases() -> list[str]:
    """Return list of diseases that have briefings available."""
    all_briefings = list_available_briefings()
    return list(all_briefings.keys())


# For testing
if __name__ == "__main__":
    print("Available briefings:")
    briefings = list_available_briefings()
    for disease, files in briefings.items():
        print(f"\n{disease.upper()}:")
        for bf in files:
            print(f"  - {bf.path.name} ({bf.language}, {bf.date})")
