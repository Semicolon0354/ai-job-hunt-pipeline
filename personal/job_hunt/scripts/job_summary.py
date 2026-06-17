"""
job_summary.py — Shared helpers for formatting and tracking job summaries.

Imported by search_jobs.py (bulk nightly search) and evaluate_job.py
(one-off jobs found via Indeed recommendations, email, etc.).
"""

import re
from pathlib import Path

SCRIPT_DIR    = Path(__file__).resolve().parent
JOB_HUNT_DIR  = SCRIPT_DIR.parent
SUMMARIES_DIR = JOB_HUNT_DIR / "job_summaries"
APPS_DIR      = JOB_HUNT_DIR / "applications"


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
    if APPS_DIR.exists():
        for f in APPS_DIR.rglob("summary_*.txt"):
            info = _parse_summary_file(f)
            key = info["url"] or f"{info['company']}|{info['role']}"
            if key:
                seen[key] = info

    return list(seen.values())


def safe_filename(text: str) -> str:
    """Strip characters that are illegal in Windows filenames."""
    return re.sub(r'[<>:"/\\|?*\s]+', "_", text).strip("_")


_SUMMARY_TEMPLATE = """\
==========================================================
JOB SUMMARY - {company} | {title}
==========================================================
Date: {date}
Source: {source}
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
        source          = job.get("source", "Indeed"),
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
