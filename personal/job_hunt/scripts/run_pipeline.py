#!/usr/bin/env python3
"""
run_pipeline.py — Job hunt pipeline orchestrator.

Scheduled to run Mon-Fri at midnight via Windows Task Scheduler.
Chains: search_jobs.py → generate_resume_coverletter.py (for each new summary).

After the pipeline runs:
  - job_summaries/                  contains any NEW summaries still awaiting doc generation
  - applications/{Company_date}/    contains resume.docx, cover_letter.docx, and the summary .txt

Usage:
    python run_pipeline.py               # Full pipeline (search + docs)
    python run_pipeline.py --search-only # Job search only; skip document generation
    python run_pipeline.py --docs-only   # Generate docs for everything in job_summaries/
"""

import argparse
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR    = Path(__file__).resolve().parent
JOB_HUNT_DIR  = SCRIPT_DIR.parent
SUMMARIES_DIR = JOB_HUNT_DIR / "job_summaries"
LOGS_DIR      = JOB_HUNT_DIR / "logs"

SEARCH_SCRIPT  = SCRIPT_DIR / "search_jobs.py"
DOCS_SCRIPT    = SCRIPT_DIR / "generate_resume_coverletter.py"
LEARN_SCRIPT   = SCRIPT_DIR / "learn_from_edits.py"
PYTHON         = sys.executable  # same interpreter that launched this script


# ── Logging ────────────────────────────────────────────────────────────────────

def log(msg: str, logfile=None) -> None:
    ts   = datetime.now().strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    if logfile:
        logfile.write(line + "\n")
        logfile.flush()


# ── File helpers ───────────────────────────────────────────────────────────────

def pending_summaries() -> list[Path]:
    """All .txt summaries currently in job_summaries/ (not yet converted to applications)."""
    SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)
    return sorted(SUMMARIES_DIR.glob("summary_*.txt"))


# ── Subprocess runner ──────────────────────────────────────────────────────────

def run_step(
    cmd: list[str],
    label: str,
    logfile=None,
    timeout: int = 900,
) -> bool:
    log(f"--- {label} ---", logfile)
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=str(JOB_HUNT_DIR),
        timeout=timeout,
        env=env,
    )
    for line in (result.stdout or "").splitlines():
        log(f"  {line}", logfile)
    if result.returncode != 0:
        log(f"  [FAILED] exit code {result.returncode}", logfile)
        for line in (result.stderr or "").splitlines():
            log(f"  STDERR: {line}", logfile)
        return False
    return True


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Job hunt pipeline: search then generate docs")
    parser.add_argument(
        "--search-only", action="store_true",
        help="Run job search only; skip document generation",
    )
    parser.add_argument(
        "--docs-only", action="store_true",
        help="Generate docs for existing summaries in job_summaries/; skip search",
    )
    parser.add_argument(
        "--search-model", default="claude-opus-4-8",
        help="Claude model for the job search (default: claude-opus-4-8)",
    )
    parser.add_argument(
        "--docs-model", default="qwen3.5:9b",
        help="Ollama model for document generation (default: qwen3.5:9b)",
    )
    args = parser.parse_args()

    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    today    = datetime.now().strftime("%Y-%m-%d")
    log_path = LOGS_DIR / f"pipeline_{today}.log"

    with log_path.open("a", encoding="utf-8") as logfile:
        started = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log(f"========== Pipeline started: {started} ==========", logfile)
        log(f"Mode: {'docs-only' if args.docs_only else 'search-only' if args.search_only else 'full'}", logfile)

        # ── Step 0: Learn from any edits Josh made since the last run ──────────
        if not args.docs_only and not args.search_only:
            run_step(
                [PYTHON, str(LEARN_SCRIPT)],
                "Learn from edits (feedback loop)",
                logfile,
                timeout=300,
            )
            # Non-fatal: if learning fails, continue with search + generation

        # ── Step 1: Job search ─────────────────────────────────────────────────
        new_summaries: list[Path] = []

        if not args.docs_only:
            before = set(pending_summaries())

            ok = run_step(
                [PYTHON, str(SEARCH_SCRIPT), "--model", args.search_model],
                "Job search (Indeed via Claude)",
                logfile,
                timeout=900,
            )
            if not ok:
                log("Job search failed — aborting.", logfile)
                sys.exit(1)

            after = set(pending_summaries())
            new_summaries = sorted(after - before)
            log(f"New summaries from this run: {len(new_summaries)}", logfile)
            for p in new_summaries:
                log(f"  + {p.name}", logfile)
        else:
            # --docs-only: process everything currently in job_summaries/
            new_summaries = pending_summaries()
            log(f"--docs-only: {len(new_summaries)} summary/summaries to process.", logfile)
            for p in new_summaries:
                log(f"  ~ {p.name}", logfile)

        if args.search_only:
            log("--search-only: skipping document generation.", logfile)
            log("========== Pipeline complete ==========", logfile)
            return

        # ── Step 2: Generate resume + cover letter for each new summary ─────────
        if not new_summaries:
            log("No summaries to process — nothing to generate.", logfile)
            log("========== Pipeline complete ==========", logfile)
            return

        results: list[tuple[str, bool]] = []
        for summary_path in new_summaries:
            ok = run_step(
                [
                    PYTHON, str(DOCS_SCRIPT),
                    "--summary", str(summary_path),
                    "--model", args.docs_model,
                ],
                f"Generate docs: {summary_path.name}",
                logfile,
                timeout=600,
            )
            results.append((summary_path.name, ok))

        log("", logfile)
        log("========== Results ==========", logfile)
        for name, ok in results:
            status = "OK    " if ok else "FAILED"
            log(f"  [{status}] {name}", logfile)

        failed = sum(1 for _, ok in results if not ok)
        if failed:
            log(f"WARNING: {failed} generation(s) failed. Summary file(s) NOT moved.", logfile)

    print(f"\nLog: {log_path}")


if __name__ == "__main__":
    main()
