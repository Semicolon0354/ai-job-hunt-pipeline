#!/usr/bin/env python3
"""
learn_from_outcomes.py — Refine job search strategy from application outcomes.

Reads tracker.csv and identifies patterns in what was applied to, passed on,
or resulted in interviews. Proposes specific updates to job_search_rules.md
so future searches better match what actually works.

Runs as Step 0.5 in the full pipeline (after learn_from_edits, before search).
Skips silently if fewer than --min decided entries exist in the tracker.

Usage:
    python learn_from_outcomes.py              # Analyze and update rules if signal exists
    python learn_from_outcomes.py --dry-run    # Print decided entries without updating
    python learn_from_outcomes.py --verbose    # Print Claude's raw output
    python learn_from_outcomes.py --min 5      # Require 5 decided entries (default: 3)
"""

import argparse
import csv
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from claude_utils import find_claude_exe, call_claude, extract_json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR   = Path(__file__).resolve().parent
JOB_HUNT_DIR = SCRIPT_DIR.parent
CONFIG_DIR   = JOB_HUNT_DIR / "config"
APPS_DIR     = JOB_HUNT_DIR / "applications"

TRACKER_FILE = APPS_DIR / "tracker.csv"
RULES_FILE   = CONFIG_DIR / "job_search_rules.md"

PENDING_STATUS = "Pending"


def read_decided() -> list[dict]:
    """Return all tracker rows that have a user-set status (not Pending, not blank)."""
    if not TRACKER_FILE.exists():
        return []
    with TRACKER_FILE.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return [r for r in rows if r.get("Status", "").strip() not in ("", PENDING_STATUS)]


def build_prompt(decided: list[dict], current_rules: str) -> str:
    today = date.today().isoformat()

    status_counts = Counter(r["Status"] for r in decided)
    summary_line = ", ".join(f"{n} {s}" for s, n in status_counts.most_common())

    table_lines = []
    for r in decided:
        line = f"  - {r['Company']} | {r['Role']} | Score: {r['Score']} | {r['Status']}"
        if r.get("Notes", "").strip():
            line += f" | Notes: {r['Notes']}"
        table_lines.append(line)

    return f"""\
You are analyzing job application outcomes to refine a job search strategy.

Today: {today}
Decided applications ({summary_line}):
{chr(10).join(table_lines)}

=== CURRENT JOB SEARCH RULES ===
{current_rules}

=== INSTRUCTIONS ===

Study the patterns in these outcomes. Focus only on what would improve future searches.

CRITICAL: The Notes column is the ground truth for WHY a decision was made.
- A rule is only valid if the Notes column consistently and explicitly states the same reason across multiple entries.
- Never infer a filter rule from title or score correlation alone. If three Senior roles were passed on but the Notes say different things (wrong company, contract only, too niche), "Senior" is NOT the pattern — the individual Notes reasons are.
- Do not recommend filtering out a role type, seniority level, or industry unless the Notes repeatedly and explicitly name it as the reason.
- "Not Applying" with no Notes or vague Notes is not sufficient signal for a new rule.

With that constraint, look for:
- Employer types or industries the Notes explicitly and repeatedly flag (e.g. "faith-affiliated", "insurance", "staffing agency")
- Recurring gaps the Notes name (e.g. "requires Tableau", "contract only", "requires clearance")
- Score calibration issues: if the Notes reveal the rubric is rewarding things that don't convert, suggest reweighting
- Positive signals from Applied and Interviewing entries that could sharpen what to surface

Only surface insights NOT already captured in the current rules.
Be specific — "skip staffing agencies" beats "be more selective."

Respond with ONLY a JSON object in a ```json code block:

```json
{{
  "sufficient_signal": true,
  "summary": "One sentence: the main pattern in these outcomes",
  "rules_additions": ""
}}
```

Formatting rules for additions:
- Append under a dated heading:

  ---
  ## Learned from Outcomes — {today}
  - [specific, actionable rule]

- Maximum 5 rules. Quality over quantity.
- If there is no clear pattern yet, set "sufficient_signal": false and leave additions empty.
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Learn from job application outcomes")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print decided entries without updating rules")
    parser.add_argument("--model", default="claude-opus-4-8")
    parser.add_argument("--verbose", action="store_true",
                        help="Print Claude's raw output")
    parser.add_argument("--min", type=int, default=3, dest="min_entries",
                        help="Minimum decided entries required (default: 3)")
    args = parser.parse_args()

    decided = read_decided()

    if len(decided) < args.min_entries:
        print(f"Outcomes: {len(decided)} decided / {args.min_entries} required — skipping.")
        return

    print(f"Outcomes: {len(decided)} decided entries — analyzing patterns.")

    if args.dry_run:
        for r in decided:
            print(f"  {r['Status']:25} {r['Company']} | {r['Role']}")
        return

    try:
        claude_exe = find_claude_exe()
    except FileNotFoundError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

    current_rules = RULES_FILE.read_text(encoding="utf-8") if RULES_FILE.exists() else ""
    prompt = build_prompt(decided, current_rules)

    print("  → Calling Claude to identify patterns...")
    try:
        raw = call_claude(prompt, claude_exe, args.model)
    except RuntimeError as e:
        print(f"  [ERROR] Claude call failed: {e}")
        return

    if args.verbose:
        print("\n  --- Claude raw output ---")
        print(raw)
        print("  -------------------------\n")

    try:
        analysis = extract_json(raw)
    except (ValueError, json.JSONDecodeError) as e:
        print(f"  [ERROR] Could not parse Claude's response: {e}")
        return

    if not analysis.get("sufficient_signal", False):
        print("  → Claude: not enough signal yet — no rule updates.")
        return

    print(f"  Summary: {analysis.get('summary', '')}")

    additions = analysis.get("rules_additions", "").strip()
    if additions and RULES_FILE.exists():
        existing = RULES_FILE.read_text(encoding="utf-8")
        sep = "\n" if existing.endswith("\n") else "\n\n"
        RULES_FILE.write_text(existing + sep + additions + "\n", encoding="utf-8")
        print("  Updated: job_search_rules.md")
    else:
        print("  No additions needed.")


if __name__ == "__main__":
    main()
