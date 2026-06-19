#!/usr/bin/env python3
"""Check Research Mode presentation quality across multiple feline diseases.

This is a local regression guard for the researcher-facing search path:

- Chinese output should show the Chinese report before the English report.
- Chinese structured fields should not contain English sentence bodies.
- User-facing output must not expose internal source IDs such as src-ckd-001.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from research_mode import handle_research_query  # noqa: E402


SAMPLE_QUERIES = [
    "search the latest papers about feline CKD, prioritize high-impact journals",
    "search the latest papers about feline HCM, prioritize high-impact journals",
    "search the latest papers about feline FIP, prioritize high-impact journals",
    "search the latest papers about feline diabetes, prioritize high-impact journals",
    "search the latest papers about feline IBD, prioritize high-impact journals",
    "search the latest papers about feline obesity, prioritize high-impact journals",
]

STRUCTURED_PREFIXES = (
    "**为什么值得读：**",
    "**关键发现：**",
    "**证据边界：**",
    "**临床相关性：**",
)

ENGLISH_SENTENCE_FRAGMENTS = (
    " the ",
    " and ",
    " with ",
    " for ",
    " that ",
    " this ",
    " study ",
    " abstract ",
    " endpoint ",
    " trial ",
)


def chinese_section(output: str) -> str:
    start = output.find("## 中文报告")
    end = output.find("## English report")
    if start == -1:
        return ""
    if end == -1 or end < start:
        return output[start:]
    return output[start:end]


def has_english_sentence_body(line: str) -> bool:
    normalized = f" {line.lower()} "
    if not any(fragment in normalized for fragment in ENGLISH_SENTENCE_FRAGMENTS):
        return False
    ascii_letters = len(re.findall(r"[A-Za-z]", line))
    cjk_chars = len(re.findall(r"[\u3400-\u9fff]", line))
    return ascii_letters > max(12, cjk_chars)


def first_recommended_blocks(zh: str, limit: int = 5) -> list[str]:
    start = zh.find("## 推荐优先阅读的文献")
    if start == -1:
        return []
    end = zh.find("## 临床与治疗研究", start)
    section = zh[start:end if end != -1 else len(zh)]
    parts = re.split(r"\n###\s+\d+\.\s+", section)
    return [part.strip() for part in parts[1:limit + 1] if part.strip()]


def check_query(query: str) -> list[str]:
    output, _ = handle_research_query(query, chinese=True, include_external=False)
    errors: list[str] = []

    if re.search(r"src-[a-z]+-\d{3}", output):
        errors.append("internal source ID leaked")
    if "部分仅为标题占位符" in output:
        errors.append("weak title-only wording still present")

    zh_idx = output.find("## 中文报告")
    en_idx = output.find("## English report")
    if zh_idx == -1:
        errors.append("missing Chinese report")
    if en_idx == -1:
        errors.append("missing English report")
    if zh_idx != -1 and en_idx != -1 and zh_idx > en_idx:
        errors.append("English report appears before Chinese report")

    zh = chinese_section(output)
    if not zh:
        errors.append("could not extract Chinese report section")
        return errors
    if "深度提取队列" not in zh:
        errors.append("missing explicit depth extraction queue")

    structured_lines = [
        line.strip()
        for line in zh.splitlines()
        if line.strip().startswith(STRUCTURED_PREFIXES)
    ]
    if not structured_lines:
        errors.append("no structured Chinese research fields found")

    bad_lines = [line for line in structured_lines if has_english_sentence_body(line)]
    if bad_lines:
        errors.append(f"English sentence body in Chinese fields: {bad_lines[0][:140]}")

    blocks = first_recommended_blocks(zh)
    if not blocks:
        errors.append("no recommended paper blocks found")
    missing_link_blocks = [block for block in blocks[:3] if "**链接：**" not in block]
    if missing_link_blocks:
        errors.append(f"recommended paper missing accessible link: {missing_link_blocks[0].splitlines()[0][:120]}")

    return errors


def main() -> int:
    failed = False
    print("=== Research Mode Presentation Check ===")
    for query in SAMPLE_QUERIES:
        errors = check_query(query)
        label = query.replace("search the latest papers about feline ", "").split(",", 1)[0]
        if errors:
            failed = True
            print(f"FAIL {label}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {label}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
