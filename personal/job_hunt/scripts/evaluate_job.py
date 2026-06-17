#!/usr/bin/env python3
"""
evaluate_job.py — Score and summarize one specific job found outside the
nightly search (Indeed "good fit" recommendation, email alert, etc.).

Reuses the same rubric, profile, and .txt summary format as search_jobs.py
so the result flows into the existing job_summaries/ -> generate_resume_coverletter.py
pipeline like any nightly-search find. Unlike the nightly search, this always
saves a summary — the candidate already decided this job is worth a look, so
a low score or hard-filter hit becomes a flag in WATCH-OUTS, not a rejection.

Usage:
    python evaluate_job.py --url "https://www.indeed.com/viewjob?jk=abc123"
    python evaluate_job.py --file pasted_description.txt --source Email
    python evaluate_job.py --url "..." --dry-run
    python evaluate_job.py --url "..." --force      # bypass the already-seen check
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from claude_utils import find_claude_exe, call_claude, extract_json
from job_summary import previously_seen_jobs, safe_filename, format_summary

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

JOB_ID_RE = re.compile(r"[?&]jk=([a-zA-Z0-9]+)")


def extract_job_id(url: str) -> str | None:
    m = JOB_ID_RE.search(url)
    return m.group(1) if m else None


def already_seen(seen: list[dict], url: str = "", company: str = "", role: str = "") -> dict | None:
    for j in seen:
        if url and j.get("url") and j["url"] == url:
            return j
        if company and role and j.get("company") == company and j.get("role") == role:
            return j
    return None


# ── Prompt builder ─────────────────────────────────────────────────────────────

def build_evaluate_prompt(
    rules: str,
    profile: str,
    source: str,
    job_id: str | None = None,
    url: str = "",
    posting_text: str = "",
) -> str:
    today = date.today().isoformat()

    if posting_text:
        fetch_block = (
            "The full job posting text has already been provided below — do NOT "
            "search or fetch anything, just evaluate it.\n\n"
            "=== JOB POSTING ===\n"
            f"{posting_text}\n"
        )
    elif job_id:
        fetch_block = (
            f'Call get_job_details with job_id="{job_id}" to retrieve the full '
            "posting before evaluating it.\n"
        )
    else:
        fetch_block = (
            f"No job ID could be extracted from this URL: {url}\n"
            "Fetch the URL directly to retrieve the full posting before evaluating it.\n"
        )

    return f"""\
You are evaluating ONE specific job the candidate already found and chose to
look into (via {source}) — this is not a search task. Today is {today}.

=== SEARCH RULES AND SCORING RUBRIC ===
{rules}

=== CANDIDATE PROFILE ===
{profile}

=== JOB TO EVALUATE ===
{fetch_block}

=== INSTRUCTIONS ===

1. Get the full job posting content (see above).
2. Score it 0-100 using the rubric.
3. Check it against every hard filter, but do NOT discard or refuse the job
   based on score or hard-filter matches — the candidate has already decided
   this specific job is worth evaluating. Instead, call out any hard-filter
   hits (not fully remote, clearance required, etc.) and any low-score
   concerns explicitly and clearly in "watch_outs".
4. Always return exactly one job object, regardless of score.

=== REQUIRED OUTPUT FORMAT ===

Respond with ONLY a JSON object inside a ```json code block — no preamble,
no closing commentary:

```json
{{
  "company": "Exact Company Name",
  "title": "Exact Job Title",
  "location": "Remote",
  "salary": "$90,000 - $110,000",
  "score": 85,
  "url": "{url}",
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
  "watch_outs": "Any hard-filter hits or score concerns, clearly stated. 'None noted' if truly none.",
  "notes": "Mid-size SaaS company, ~500 employees. Fast-moving analytics team.",
  "full_posting": "Complete job description text, exactly as posted — do not summarize or truncate."
}}
```

Start now.
"""


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Score and summarize one specific job found outside the nightly search"
    )
    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument("--url", help="Indeed job URL (or any job URL)")
    source_group.add_argument("--file", help="Path to a .txt file containing the pasted job description")
    parser.add_argument("--source", default=None,
                        help="Source label for the summary (default: Indeed for --url, Email for --file)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the prompt without calling Claude")
    parser.add_argument("--model", default="claude-opus-4-8",
                        help="Claude model to use (default: claude-opus-4-8)")
    parser.add_argument("--verbose", action="store_true",
                        help="Print Claude's raw output before parsing")
    parser.add_argument("--force", action="store_true",
                        help="Process even if this URL/company+role was already seen")
    args = parser.parse_args()

    source = args.source or ("Indeed" if args.url else "Email")

    posting_text = ""
    job_id = None
    url = args.url or ""

    if args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"[ERROR] File not found: {file_path}")
            sys.exit(1)
        posting_text = file_path.read_text(encoding="utf-8", errors="replace")
    else:
        job_id = extract_job_id(url)

    rules   = (CONFIG_DIR / "job_search_rules.md").read_text(encoding="utf-8")
    profile = user.to_markdown()
    seen    = previously_seen_jobs()

    if url and not args.force:
        dup = already_seen(seen, url=url)
        if dup:
            print(f"[INFO] Already seen: {dup.get('company')} | {dup.get('role')}")
            print("Use --force to re-evaluate anyway.")
            return

    prompt = build_evaluate_prompt(
        rules, profile, source,
        job_id=job_id, url=url, posting_text=posting_text,
    )
    today = date.today().isoformat()

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

    print(f"Evaluating job via Claude ({args.model})...")

    try:
        claude_text = call_claude(prompt, claude_exe, args.model, timeout=300)
    except RuntimeError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

    if args.verbose:
        print("─── Raw Claude output ───────────────────────────────────")
        print(claude_text)
        print("─────────────────────────────────────────────────────────\n")

    try:
        job = extract_json(claude_text)
    except (ValueError, Exception) as e:
        print(f"[ERROR] Could not parse job data from Claude's response: {e}")
        print("\nTip: run with --verbose to see the raw output.")
        if not args.verbose:
            print("\nFirst 1000 chars of output:")
            print(claude_text[:1000])
        sys.exit(1)

    if isinstance(job, list):
        job = job[0] if job else {}

    job.setdefault("source", source)
    if url and not job.get("url"):
        job["url"] = url

    if not args.force:
        dup = already_seen(seen, url=job.get("url", ""), company=job.get("company", ""), role=job.get("title", ""))
        if dup:
            print(f"[INFO] Already seen: {dup.get('company')} | {dup.get('role')}")
            print("Use --force to save anyway.")
            return

    company_slug = safe_filename(job.get("company", "Unknown"))
    filename     = f"summary_{company_slug}_{today}.txt"
    filepath     = SUMMARIES_DIR / filename
    filepath.write_text(format_summary(job, today), encoding="utf-8")

    print(f"\nSaved: {filepath}")
    print(f"  {job.get('title')} @ {job.get('company')} — Score: {job.get('score')}/100")
    watch_outs = job.get("watch_outs", "")
    if watch_outs and watch_outs.strip().lower() not in ("none noted", "none", ""):
        print(f"  WATCH-OUTS: {watch_outs}")
    print(f"\nRun 'python run_pipeline.py --docs-only' to generate the resume and cover letter.")


if __name__ == "__main__":
    main()
