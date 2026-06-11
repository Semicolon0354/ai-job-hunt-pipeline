# Job Hunt Automation

Automated pipeline that searches Indeed for remote data analytics jobs, scores them, and generates a tailored resume and cover letter for each one — every weeknight at midnight.

---

## What It Does

Each night the pipeline runs three searches on Indeed, filters the results against hard rules, scores the survivors 0–100, and takes the top three. For each of those three jobs it generates a resume and cover letter customized to that specific posting using your profile and a local AI model. Everything lands in organized folders ready for you to review in the morning.

The system also learns. When you edit a generated document and save a final version, the next pipeline run picks up your changes, identifies the patterns, and updates its writing guides so future documents need fewer corrections.

---

## End-to-End Flow

```
Windows Task Scheduler (Mon–Fri, midnight)
  └── launch_pipeline.bat
        ├── Starts Ollama if not already running
        └── run_pipeline.py
              │
              ├── STEP 0 — Learn from edits (learn_from_edits.py)
              │     Scans applications/ for rough_draft + final pairs.
              │     If you edited a doc since the last run, Claude analyzes
              │     what changed and appends learned rules to the writing guides.
              │
              ├── STEP 1 — Job search (search_jobs.py)
              │     Claude Code CLI + Indeed MCP tools run 3 searches.
              │     Results are filtered, scored, and saved as .txt summaries
              │     in job_summaries/.
              │
              └── STEP 2 — Document generation (generate_resume_coverletter.py)
                    For each new .txt summary, a local Qwen model generates
                    a tailored resume and cover letter.
                    Both saved as *_rough_draft.docx in applications/{Company_date}/.
```

---

## Directory Structure

```
Claude_Code/
│
├── common/                          ← Shared across all projects
│   ├── profile.py                   ← YOUR PROFILE — single source of truth
│   │                                   Edit this to update your info everywhere.
│   │                                   (not committed — copy profile.example.py to get started)
│   └── write_like_user.md           ← Voice and tone guide for cover letters.
│                                       The feedback loop appends learned patterns here.
│                                       (not committed — copy write_like_user.example.md to get started)
│
└── personal/
    └── job_hunt/                    ← This project
        │
        ├── README.md                ← You are here
        │
        ├── config/
        │   ├── job_search_rules.md  ← Search queries, hard filters, scoring rubric,
        │   │                           output format. Edit to change what gets searched.
        │   └── resume_coverletter_guide.md
        │                            ← Tailoring rules for the LLM.
        │                               The feedback loop appends learned rules here.
        │                               (not committed — copy the .example version to get started)
        │
        ├── scripts/
        │   ├── run_pipeline.py      ← MAIN ENTRY POINT. Orchestrates all steps.
        │   ├── launch_pipeline.bat  ← Called by Task Scheduler. Starts Ollama,
        │   │                           then calls run_pipeline.py.
        │   ├── search_jobs.py       ← Runs Indeed searches via Claude + MCP.
        │   │                           Saves scored .txt summaries to job_summaries/.
        │   ├── generate_resume_coverletter.py
        │   │                        ← Generates resume + cover letter from a summary.
        │   │                           Uses Ollama/Qwen locally. Saves to applications/.
        │   ├── learn_from_edits.py  ← Compares rough draft vs. your edited final.
        │   │                           Updates writing guides with learned patterns.
        │   └── claude_utils.py      ← Shared helpers: find_claude_exe(), call_claude(),
        │                               extract_json(). Used by search_jobs and learn_from_edits.
        │
        ├── job_summaries/           ← Scored .txt job summaries awaiting processing.
        │                               Files here have been found but not yet converted
        │                               to documents. After docs are generated, the .txt
        │                               moves into the application folder.
        │
        ├── applications/            ← One subfolder per job application.
        │   └── Acme_Corp_2026-06-08/
        │       ├── summary_Acme_Corp_2026-06-08.txt
        │       │                    ← The scored summary (moved here from job_summaries/)
        │       ├── LastName_Resume_Acme_Corp_Data_Analyst_rough_draft.docx
        │       │                    ← LLM-generated resume. Ready to review.
        │       ├── LastName_Cover_Letter_Acme_Corp_Data_Analyst_rough_draft.docx
        │       │                    ← LLM-generated cover letter. Ready to review.
        │       └── .feedback_applied  ← Created after the feedback loop has analyzed
        │                                 this folder. Prevents reprocessing.
        │
        └── logs/
            ├── pipeline_YYYY-MM-DD.log  ← Full run log for each day.
            └── launcher.log             ← Task Scheduler launch events.
```

---

## The Feedback Loop

This is how the system learns your preferences over time.

**Step 1 — Review the rough draft**

After the pipeline runs, open `applications/{Company_date}/`. You'll find two `*_rough_draft.docx` files — the resume and cover letter the LLM generated.

**Step 2 — Create your edited version**

Edit the rough draft, then save a copy with `_rough_draft` removed from the filename. Both files now exist in the same folder — that's the trigger.

```
Before:  LastName_Cover_Letter_Acme_Corp_Data_Analyst_rough_draft.docx
After:   LastName_Cover_Letter_Acme_Corp_Data_Analyst.docx  ← your finished edits
```

Take as long as you need. A folder with only the rough draft (no final copy yet) is ignored by the pipeline entirely — it won't analyze or mark it. There's no deadline. The trigger is the presence of both files, not the passage of time.

One gotcha: if you create the final copy but haven't finished editing yet and the pipeline runs overnight, it will analyze whatever version you saved and lock the folder. If that happens, use `--reset` to re-open it (see Feedback loop controls below).

**Step 3 — Next pipeline run does the learning**

The pipeline's Step 0 (`learn_from_edits.py`) finds the pair, extracts the text from both versions, and measures how different they are. If the difference is significant (less than 92% similar), it sends both versions to Claude with the current writing guides and asks: *"What patterns in these edits should become permanent rules?"*

Claude returns specific, actionable rules — not company-specific tweaks, but patterns that should apply everywhere. Those rules get appended to:
- `common/write_like_user.md` — if the changes are about voice, tone, or phrasing
- `config/resume_coverletter_guide.md` — if they're about structure, content selection, or format

A `.feedback_applied` marker is written to the folder so it's analyzed exactly once, no matter how many pipeline runs follow.

**The goal:** Eventually you open the rough drafts and send them as-is.

---

## Dependencies

### Required software

| Dependency | Purpose | Notes |
|---|---|---|
| Python 3.x | Runs all scripts | `python` (must be on PATH, or set full path in `launch_pipeline.bat`) |
| python-docx | Reads/writes .docx files | `pip install python-docx` |
| requests | HTTP calls to Ollama | `pip install requests` |
| Ollama | Local LLM inference | Must be running when pipeline runs |
| Qwen 3.5 9B | Document generation model | `ollama pull qwen3.5:9b` |
| Claude Code (VSCode extension) | Indeed MCP integration | Provides job search tools |
| Windows Task Scheduler | Nightly automation | Built into Windows |

### Why two different AI models?

- **Claude (via Claude Code CLI)** — used for the job search. It has access to the Indeed MCP integration tools that can actually search and retrieve live job postings. Requires a Claude subscription.
- **Qwen via Ollama** — used for document generation. Runs entirely locally, no API cost, no data leaving your machine. Handles the writing-heavy tasks of tailoring bullets and drafting cover letters.

---

## Setup

### 1. Install Python packages

```powershell
pip install python-docx requests
```

### 2. Verify Ollama and the model

```powershell
ollama list   # should show qwen3.5:9b
```

If the model isn't there:
```powershell
ollama pull qwen3.5:9b
```

### 3. Verify the Claude Code extension is installed

Open VS Code → Extensions → confirm `Claude Code` by Anthropic is installed and you're signed in. The Indeed integration must be connected under Settings → Integrations.

### 4. Verify the scheduled task exists

```powershell
schtasks /query /tn "Job Hunt Pipeline" /fo LIST
```

If missing, recreate it:
```powershell
$bat = "C:\path\to\Claude_Code\personal\job_hunt\scripts\launch_pipeline.bat"
schtasks /create /tn "Job Hunt Pipeline" /tr $bat /sc weekly /d MON,TUE,WED,THU,FRI /st 00:00 /f /it
```

Note: `/it` means the task only runs when you're logged in. It will run even with the screen locked.

---

## Running Manually

All commands should be run from the `job_hunt/` directory with UTF-8 encoding set:

```powershell
cd "C:\path\to\Claude_Code\personal\job_hunt"
$env:PYTHONIOENCODING = "utf-8"
```

### Full pipeline (search + generate + learn)

```powershell
python scripts\run_pipeline.py
```

### Individual steps

```powershell
# Search only — find jobs and save .txt summaries, skip document generation
python scripts\run_pipeline.py --search-only

# Docs only — generate documents for anything in job_summaries/, skip search
python scripts\run_pipeline.py --docs-only

# Learn only — run the feedback loop on any unanalyzed edit pairs
python scripts\learn_from_edits.py

# Preview the search prompt without calling Claude
python scripts\search_jobs.py --dry-run

# Preview what the feedback loop would analyze without making changes
python scripts\learn_from_edits.py --dry-run

# Generate docs for a specific summary file
python scripts\generate_resume_coverletter.py --summary job_summaries\summary_Acme_Corp_2026-06-08.txt
```

### Feedback loop controls

```powershell
# Re-analyze a folder (clears the .feedback_applied marker)
python scripts\learn_from_edits.py --reset Acme_Corp_2026-06-08

# See what Claude actually said during analysis
python scripts\learn_from_edits.py --verbose
```

---

## Configuration

### Changing what gets searched

Edit `config/job_search_rules.md`. This file controls:
- The three search queries run on Indeed
- Hard filters (job types, companies, and listing patterns to skip)
- The scoring rubric (what earns points toward the 0–100 score)
- The output format of the .txt summary files

### Updating your profile

Edit `common/profile.py`. This is the single source of truth for everything about you — contact info, work history, bullet bank, skills, certifications, and tailoring notes. All scripts read from this file. Change it here and the change flows everywhere automatically.

### Changing the cover letter voice

Edit `common/write_like_user.md`. This is the style guide the LLM follows when writing cover letters — sentence structure, what phrases to avoid, how paragraphs should be built. The feedback loop appends to the bottom of this file as it learns from your edits.

### Changing resume/cover letter structure

Edit `config/resume_coverletter_guide.md`. This covers which experience sections to include for which role types, how to handle the Paramedic role, what the cover letter paragraphs should do, and the pre-save checklist. The feedback loop also appends to this file.

### Using a different AI model for search

```powershell
python scripts\run_pipeline.py --search-model claude-sonnet-4-6
```

### Using a different Ollama model for documents

```powershell
python scripts\run_pipeline.py --docs-model llama3.1:8b
```

---

## Duplicate Prevention

The search script checks for duplicates across the full history — both summaries waiting in `job_summaries/` and jobs already converted to applications in `applications/`. Before running each search, it reads the company name, job title, and URL from every existing summary and passes that list to Claude with the instruction to skip matching results. This prevents the same job from surfacing on multiple runs.

---

## What This Pipeline Does NOT Do

- **Submit applications.** The Indeed MCP integration is read-only. You review and submit manually.
- **Edit your profile.py directly.** The feedback loop updates the text-based writing guides, not the Python profile file.
- **Guarantee document quality.** The rough drafts are a strong starting point, not a finished product. Review everything before sending.
