#!/usr/bin/env python3
"""Preflight OpenRouter config without making a network/API call."""

from __future__ import annotations

import os
import sys
import tomllib
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SECRETS_PATH = PROJECT_ROOT / ".streamlit" / "secrets.toml"
MAX_DAILY_BUDGET_USD = 1.00


def load_streamlit_secrets() -> dict[str, str]:
    if not SECRETS_PATH.exists():
        return {}
    try:
        data = tomllib.loads(SECRETS_PATH.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        raise SystemExit(f"FAIL: {SECRETS_PATH} is not valid TOML: {exc}") from exc
    return {key: str(value).strip() for key, value in data.items() if str(value).strip()}


def get_config(key: str, secrets: dict[str, str]) -> tuple[str, str]:
    env_value = os.environ.get(key, "").strip()
    if env_value:
        return env_value, "env"
    secret_value = secrets.get(key, "").strip()
    if secret_value:
        return secret_value, "streamlit-secrets"
    return "", "missing"


def main() -> int:
    secrets = load_streamlit_secrets()
    checks: list[tuple[str, bool, str]] = []

    api_key, api_key_source = get_config("OPENROUTER_API_KEY", secrets)
    checks.append(("OPENROUTER_API_KEY", bool(api_key), api_key_source))

    raw_budget, budget_source = get_config("OPENROUTER_DAILY_BUDGET_USD", secrets)
    budget_ok = False
    budget_detail = budget_source
    if raw_budget:
        try:
            budget = float(raw_budget)
        except ValueError:
            budget_detail = f"{budget_source}: not a number"
        else:
            budget_ok = 0 < budget <= MAX_DAILY_BUDGET_USD
            budget_detail = f"{budget_source}: {budget:.2f}"
    checks.append(("OPENROUTER_DAILY_BUDGET_USD", budget_ok, budget_detail))

    model, model_source = get_config("OPENROUTER_MODEL", secrets)
    if not model:
        model = "openai/gpt-4.1-mini"
        model_source = "default"
    checks.append(("OPENROUTER_MODEL", True, f"{model_source}: {model}"))

    failed = False
    for name, ok, detail in checks:
        status = "PASS" if ok else "FAIL"
        print(f"{status}: {name} ({detail})")
        failed = failed or not ok

    if failed:
        print(
            "\nSet OPENROUTER_API_KEY and OPENROUTER_DAILY_BUDGET_USD=1.00 "
            "in the shell or Streamlit secrets, then restart the app.",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
