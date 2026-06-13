#!/usr/bin/env python3
"""Streamlit AppTest coverage for Research Case creation and reload."""

from __future__ import annotations

import tempfile
from pathlib import Path

from streamlit.testing.v1 import AppTest


SCRIPT = """
from pathlib import Path
import streamlit as st
from research_case_ui import render_research_cases

render_research_cases(Path({vault_root!r}))
"""


def _set_text_input(at: AppTest, label: str, value: str) -> None:
    next(item for item in at.text_input if item.label == label).set_value(value)


def _set_text_area(at: AppTest, label: str, value: str) -> None:
    next(item for item in at.text_area if item.label == label).set_value(value)


def test_create_and_reload_case() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "system").mkdir()
        at = AppTest.from_string(
            SCRIPT.format(vault_root=str(root)),
            default_timeout=20,
        )
        at.run()
        assert not at.exception

        _set_text_input(at, "Case ID", "case-ckd-phosphorus")
        _set_text_area(at, "Atomic research question", "Does phosphorus control merit further CKD research?")
        _set_text_area(at, "Scope", "Feline CKD evidence in the local vault")
        _set_text_area(at, "Alternatives, one per line", "advance evidence review\ndo not advance")
        _set_text_input(at, "Asset", "phosphorus-control program")
        _set_text_input(at, "Indication", "feline CKD")
        _set_text_input(at, "Jurisdiction", "research only")
        _set_text_input(at, "Owner", "Jiawei")
        _set_text_input(at, "Reviewer label", "Reviewer A")
        _set_text_input(at, "Deadline", "2026-06-30")
        next(button for button in at.button if button.label == "Create case").click()
        at.run()

        assert not at.exception, [exc.value for exc in at.exception]
        case_path = root / "system" / "research-cases" / "case-ckd-phosphorus.json"
        assert case_path.exists()
        assert next(item for item in at.selectbox if item.label == "Research Case").value == "case-ckd-phosphorus"
        assert [tab.label for tab in at.tabs] == ["Frame", "Criteria", "Evidence", "Challenge"]
        assert any("revision 1" in caption.value for caption in at.caption)
        assert any(
            "Recommend and Sign are intentionally outside this release." in caption.value
            for caption in at.caption
        )


if __name__ == "__main__":
    test_create_and_reload_case()
    print("PASS test_create_and_reload_case")
