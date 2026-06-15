#!/usr/bin/env python3
"""
search_jobs.py — Automated Indeed job search.

Uses the Claude Code CLI (claude.exe) which has the Indeed MCP integration
configured. Claude runs the three searches, filters, and scores jobs. Python
handles file I/O and formats the .txt summary files.

Usage:
    python search_jobs.py           # Run full search (may take several minutes)
    python search_jobs.py --dry-run # Print the prompt without calling Claude
    python search_jobs.py --model claude-sonnet-4-6  # Use a different model
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from claude_utils import find_claude_exe, call_claude, extract_json

# Windows console defaults to cp1252; profile.py contains Unicode arrows.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ── Directory layout ───────────────────────────────────────────────────────────
SCRIPT_DIR      = Path(__file__).resolve().parent
JOB_HUNT_DIR    = SCRIPT_DIR.parent
CLAUDE_CODE_DIR = JOB_HUNT_DIR.parent.parent
COMMON_DIR      = CLAUDE_CODE_DIR / "common"
CONFIG_DIR      = JOB_HUNT_DIR / "config"
SUMMARIES_DIR   = JOB_HUNT_DIR / "job_summaries"

# ── Profile import ─────────────────────────────────────────────────────────────
sys.path.insert(0, str(COMMON_DIR))
import profile as user


# ── Helpers ────────────────────────────────────────────────────────────────────

def _parse_summary_file(path: Path) -> dict:
    """Extract company, role, and URL from a summary .txt file."""
    info = {"company": "", "role": "", "url": ""}
    try:
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            m = re.search(r"JOB SUMMARY - (.+?) \| (.+)", line, re.IGNORECASE)
            if m:
                info["company"] = m.group(1).strip()
                info["role"]    = m.group(2).strip()
            if line.upper().startswith("URL:"):
                info["url"] = line.split(":", 1)[1].strip()
    except OSError:
        pass
    return info


def previously_seen_jobs() -> list[dict]:
    """
    Return company/role/url for every job we've already saved — both summaries
    still pending in job_summaries/ AND jobs already converted to applications.
    Used to prevent the search from surfacing duplicates across runs.
    """
    seen: dict[str, dict] = {}   # keyed by URL (or company+role fallback)

    # Pending summaries
    if SUMMARIES_DIR.exists():
        for f in SUMMARIES_DIR.glob("summary_*.txt"):
            info = _parse_summary_file(f)
            key = info["url"] or f"{info['company']}|{info['role']}"
            if key:
                seen[key] = info

    # Processed summaries moved into applications subfolders
    apps_dir = JOB_HUNT_DIR / "applications"
    if apps_dir.exists():
        for f in apps_dir.rglob("summary_*.txt"):
            info = _parse_summary_file(f)
            key = info["url"] or f"{info['company']}|{info['role']}"
            if key:
                seen[key] = info

    return list(seen.values())


def safe_filename(text: str) -> str:
    """Strip characters that are illegal in Windows filenames."""
    return re.sub(r'[<>:"/\\|?*\s]+', "_", text).strip("_")


# ── Prompt builder ─────────────────────────────────────────────────────────────

def build_search_prompt(rules: str, profile: str, seen: list[dict]) -> str:
    today = date.today().isoformat()

    dup_block = ""
    if seen:
        lines = []
        for j in seen:
            parts = [j["company"]]
            if j["role"]:
                parts.append(j["role"])
            if j["url"]:
                parts.append(j["url"])
            lines.append("- " + " | ".join(parts))
        dup_block = (
            "\n## Already Seen — Skip These Completely\n"
            "Do not return any job that matches a company+role or URL below.\n"
            "This prevents duplicates across pipeline runs.\n"
            + "\n".join(lines)
            + "\n"
        )

    return f"""\
You are a job search agent. Today is {today}.

Use the Indeed search and job-details tools to find the best-matching remote
data analytics opportunities, then return the results as structured JSON.

=== SEARCH RULES AND SCORING RUBRIC ===
{rules}

=== CANDIDATE PROFILE ===
{profile}
{dup_block}
=== INSTRUCTIONS ===

1. Run ALL THREE searches defined in the rules (data analyst, BI analyst,
   analytics engineer — all remote US full-time).
2. Call get_job_details for every listing that looks promising.
3. Apply every hard filter. Discard anything that fails even one.
4. Score each remaining job 0-100 using the rubric.
5. Return the top 3 scoring jobs (minimum score 60 to qualify).
   If fewer than 3 qualify after filtering, return however many do.

=== REQUIRED OUTPUT FORMAT ===

Respond with ONLY a JSON array inside a ```json code block — no preamble,
no closing commentary. Each element represents one qualified job:

```json
[
  {{
    "company": "Exact Company Name",
    "title": "Exact Job Title",
    "location": "Remote",
    "salary": "$90,000 - $110,000",
    "score": 85,
    "url": "https://www.indeed.com/viewjob?jk=abc123",
    "why_good_fit": "2-3 sentence explanation of why this matches the candidate's background.",
    "key_requirements": [
      "SQL",
      "Power BI",
      "Python",
      "ETL pipeline design",
      "stakeholder reporting"
    ],
    "ats_keywords": "SQL, Python, Power BI, ETL, data pipeline, DAX, dashboard, KPIs, data warehouse",
    "must_haves": [
      "3+ years of data analytics experience",
      "Proficiency in SQL",
      "Experience with BI tools"
    ],
    "nice_to_haves": [
      "Experience with dbt",
      "Healthcare domain knowledge"
    ],
    "watch_outs": "Requires Tableau experience — candidate is stronger in Power BI.",
    "notes": "Mid-size SaaS company, ~500 employees. Fast-moving analytics team.",
    "full_posting": "Complete job description text, exactly as posted — do not summarize or truncate."
  }}
]
```

If no jobs qualify (all filtered out or scored below 60), return an empty array: []

Start searching now.
"""


# ── Output formatter ───────────────────────────────────────────────────────────

_SUMMARY_TEMPLATE = """\
==========================================================
JOB SUMMARY - {company} | {title}
==========================================================
Date: {date}
Source: Indeed
Score: {score}/100
URL: {url}

COMPENSATION
------------
{salary}

WHY THIS IS A GOOD FIT
-----------------------
{why_good_fit}

KEY REQUIREMENTS TO HIGHLIGHT IN APPLICATION
---------------------------------------------
{key_requirements}

ATS KEYWORDS (include these in resume/cover letter)
----------------------------------------------------
{ats_keywords}

REQUIREMENTS SUMMARY
---------------------
Must-haves:
{must_haves}

Nice-to-haves:
{nice_to_haves}

WATCH-OUTS / GAPS
------------------
{watch_outs}

NOTES
-----
{notes}
==========================================================

FULL JOB POSTING
----------------
{full_posting}
==========================================================
"""


def format_summary(job: dict, today: str) -> str:
    key_reqs = "\n".join(f"- {r}" for r in job.get("key_requirements", []))
    must     = "\n".join(f"- {r}" for r in job.get("must_haves", []))
    nice     = "\n".join(f"- {r}" for r in job.get("nice_to_haves", []))

    return _SUMMARY_TEMPLATE.format(
        company         = job.get("company", "Unknown"),
        title           = job.get("title", "Unknown"),
        date            = today,
        score           = job.get("score", "N/A"),
        url             = job.get("url", "Not provided"),
        salary          = job.get("salary", "Not listed"),
        why_good_fit    = job.get("why_good_fit", ""),
        key_requirements = key_reqs,
        ats_keywords    = job.get("ats_keywords", ""),
        must_haves      = must,
        nice_to_haves   = nice,
        watch_outs      = job.get("watch_outs", "None noted"),
        notes           = job.get("notes", ""),
        full_posting    = job.get("full_posting", "Not available"),
    )


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Search Indeed for remote data analytics jobs")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the prompt without calling Claude")
    parser.add_argument("--model", default="claude-opus-4-8",
                        help="Claude model to use (default: claude-opus-4-8)")
    parser.add_argument("--verbose", action="store_true",
                        help="Print Claude's raw output before parsing")
    args = parser.parse_args()

    rules   = (CONFIG_DIR / "job_search_rules.md").read_text(encoding="utf-8")
    profile = user.to_markdown()
    seen    = previously_seen_jobs()
    prompt  = build_search_prompt(rules, profile, seen)
    today   = date.today().isoformat()

    if args.dry_run:
        print("=" * 60)
        print("DRY RUN — Prompt that would be sent to Claude:")
        print("=" * 60)
        print(prompt)
        return

    try:
        claude_exe = find_claude_exe()
    except FileNotFoundError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

    SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Searching Indeed via Claude ({args.model})...")
    print("This may take several minutes while Claude runs the searches.\n")

    try:
        claude_text = call_claude(prompt, claude_exe, args.model, timeout=600)
    except RuntimeError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

    if args.verbose:
        print("─── Raw Claude output ───────────────────────────────────")
        print(claude_text)
        print("─────────────────────────────────────────────────────────\n")

    try:
        jobs = extract_json(claude_text)
    except (ValueError, Exception) as e:
        print(f"[ERROR] Could not parse job data from Claude's response: {e}")
        print("\nTip: run with --verbose to see the raw output.")
        if not args.verbose:
            print("\nFirst 1000 chars of output:")
            print(claude_text[:1000])
        sys.exit(1)

    if not jobs:
        print(f"[INFO] No jobs qualified after filtering and scoring on {today}.")
        print("Try again tomorrow — listings change daily.")
        return

    saved: list[tuple[dict, Path]] = []
    for job in jobs[:3]:
        company_slug = safe_filename(job.get("company", "Unknown"))
        filename     = f"summary_{company_slug}_{today}.txt"
        filepath     = SUMMARIES_DIR / filename
        content      = format_summary(job, today)
        filepath.write_text(content, encoding="utf-8")
        saved.append((job, filepath))

    # Completion report (matches job_search_rules.md format)
    print(f"Done — {today}")
    print(f"Saved {len(saved)} job summar{'y' if len(saved) == 1 else 'ies'}:")
    for i, (job, _) in enumerate(saved, 1):
        print(f"  {i}. {job.get('title')} @ {job.get('company')} — Score: {job.get('score')}/100")

    if saved:
        top = saved[0][0]
        first_sentence = top.get("why_good_fit", "").split(".")[0]
        print(f"\nTop pick: {top.get('company')} — {first_sentence}.")


if __name__ == "__main__":
    main()
