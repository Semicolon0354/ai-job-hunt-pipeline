"""
claude_utils.py — Shared utilities for calling the Claude Code CLI.

Imported by search_jobs.py and learn_from_edits.py.
"""

import json
import os
import re
import subprocess
from pathlib import Path

JOB_HUNT_DIR = Path(__file__).resolve().parent.parent


def find_claude_exe() -> Path:
    """Locate the claude.exe bundled with the Claude Code VSCode extension."""
    ext_base = Path.home() / ".vscode" / "extensions"
    if not ext_base.exists():
        raise FileNotFoundError(
            f"VSCode extensions directory not found at {ext_base}.\n"
            "Make sure Claude Code is installed as a VSCode extension."
        )
    for candidate in sorted(ext_base.glob("anthropic.claude-code-*"), reverse=True):
        exe = candidate / "resources" / "native-binary" / "claude.exe"
        if exe.exists():
            return exe
    raise FileNotFoundError(
        "claude.exe not found inside any anthropic.claude-code-* extension.\n"
        "Reinstall the Claude Code extension or add 'claude' to your PATH."
    )


def call_claude(
    prompt: str,
    claude_exe: Path,
    model: str = "claude-opus-4-8",
    timeout: int = 300,
) -> str:
    """Run claude.exe in print mode and return the text result."""
    result = subprocess.run(
        [str(claude_exe), "-p", "--output-format", "json", "--model", model],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=str(JOB_HUNT_DIR),
        timeout=timeout,
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
    )
    if result.returncode != 0:
        raise RuntimeError(f"Claude exited {result.returncode}: {result.stderr[:500]}")
    try:
        return json.loads(result.stdout).get("result", result.stdout)
    except json.JSONDecodeError:
        return result.stdout


def extract_json(text: str):
    """
    Extract the first JSON value (array or object) from Claude's output.
    Handles ```json ... ``` fenced blocks and bare JSON.
    """
    fence = re.search(r"```(?:json)?\s*(\[.*?\])\s*```", text, re.DOTALL)
    if fence:
        return json.loads(fence.group(1))
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fence:
        return json.loads(fence.group(1))
    bare = re.search(r"\[.*\]", text, re.DOTALL)
    if bare:
        return json.loads(bare.group(0))
    bare = re.search(r"\{.*\}", text, re.DOTALL)
    if bare:
        return json.loads(bare.group(0))
    raise ValueError("No JSON found in Claude's output.")
