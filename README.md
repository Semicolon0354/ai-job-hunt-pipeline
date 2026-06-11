# AI Job Hunt Pipeline

An automated job search and application pipeline that runs nightly on Windows, searches Indeed for remote data analytics roles, scores the results, and generates a tailored resume and cover letter for each qualifying job — all while it learns your writing preferences over time.

---

## What It Does

Each night (Mon–Thu, 1am):

1. **Search** — Claude Code uses the Indeed MCP integration to run three searches (data analyst, BI analyst, analytics engineer — all remote US full-time). Results are filtered against hard rules, scored 0–100, and the top 3 are saved as structured `.txt` summaries.

2. **Generate** — For each new summary, a local Qwen 3.5 9B model (via Ollama) reads your profile and the job posting, then produces a tailored resume and cover letter. Both are saved as `*_rough_draft.docx` files ready to review in the morning.

3. **Learn** — When you edit a rough draft and save a final version, the next pipeline run detects the pair, sends both versions to Claude, and extracts reusable writing patterns. Those patterns get appended to your voice guide and tailoring rules — so future drafts need progressively less editing.

---

## Architecture

```
Windows Task Scheduler
  └── launch_pipeline.bat
        └── run_pipeline.py (orchestrator)
              ├── learn_from_edits.py   ← feedback loop (Step 0)
              ├── search_jobs.py        ← Claude + Indeed MCP (Step 1)
              └── generate_resume_coverletter.py  ← Ollama/Qwen (Step 2)

common/
  ├── profile.py           ← your profile: contact, work history, skills, metrics
  └── write_like_user.md   ← your voice: how the LLM writes cover letters for you

personal/job_hunt/config/
  ├── job_search_rules.md          ← search queries, filters, scoring rubric
  └── resume_coverletter_guide.md  ← resume structure, tailoring rules, cover letter format
```

### Why two AI models?

| Model | Role | Why |
|---|---|---|
| Claude (via Claude Code CLI) | Job search | Has access to the Indeed MCP integration — can actually search and retrieve live postings |
| Qwen 3.5 9B via Ollama | Document generation | Runs entirely locally — no API cost, no data leaving your machine; handles the writing-heavy generation task |

---

## Key Design Decisions

**Profile as pure data** — `profile.py` contains only facts about the candidate: contact info, work history, bullet bank, skills, education, interests, metrics. Zero instructions. This prevents the LLM from confusing "who I am" with "what to do with that information."

**Separation of concerns** — tailoring logic lives in `resume_coverletter_guide.md`. Voice and tone live in `write_like_user.md`. The profile and the guides are independent; you can update either without touching the other.

**Feedback loop** — `learn_from_edits.py` computes text similarity between rough draft and final. Below a threshold (92%), it calls Claude to identify patterns in the edits and appends actionable rules to the appropriate guide. This is the mechanism that makes the system improve over time without manual rule-writing.

**Structured JSON generation** — the document generator asks the LLM for a structured JSON object (not prose), then builds the `.docx` using `python-docx`. This keeps formatting deterministic and separates content generation from layout.

**Duplicate prevention** — before each search, the pipeline reads all existing summaries (pending and processed) and passes that list to Claude with an instruction to skip matching results. The same job never surfaces twice.

---

## Setup

See [personal/job_hunt/README.md](personal/job_hunt/README.md) for full setup instructions, dependency list, and usage examples.

Quick start:

```powershell
# 1. Install Python dependencies
pip install python-docx requests

# 2. Pull the Ollama model
ollama pull qwen3.5:9b

# 3. Copy and fill in your personal files (these are gitignored — never committed)
copy common\profile.example.py common\profile.py
copy common\write_like_user.example.md common\write_like_user.md
copy personal\job_hunt\config\resume_coverletter_guide.example.md personal\job_hunt\config\resume_coverletter_guide.md

# 4. Edit each file with your own information

# 5. Run manually to verify
cd personal\job_hunt
python scripts\run_pipeline.py --search-only
```

---

## What's Not in This Repo

Three files are gitignored because they contain personal information:

| File | What it is | What to use instead |
|---|---|---|
| `common/profile.py` | Your contact info, work history, skills | `common/profile.example.py` |
| `common/write_like_user.md` | Your voice and writing style guide | `common/write_like_user.example.md` |
| `personal/job_hunt/config/resume_coverletter_guide.md` | Your tailoring rules with role-specific placement logic | Build from the example in the detailed README |

---

## Dependencies

| Dependency | Purpose |
|---|---|
| Python 3.x | Runs all scripts |
| python-docx | Reads/writes `.docx` files |
| requests | HTTP calls to Ollama |
| Ollama | Local LLM inference |
| Qwen 3.5 9B | Document generation model (`ollama pull qwen3.5:9b`) |
| Claude Code (VSCode extension) | Indeed MCP integration for job search |
| Windows Task Scheduler | Nightly automation |
