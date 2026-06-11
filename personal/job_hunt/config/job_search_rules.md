# Job Search Rules

Instructions for the daily automated job search. Searches Indeed for remote data analytics roles, scores candidates, and saves the top 3 as .txt summary files.

---

## Search Targets

Run these searches on Indeed (all remote, US, full-time):

1. "data analyst" remote
2. "business intelligence analyst" remote
3. "analytics engineer" remote

---

## Hard Filters — Skip Any Job That Matches These

- Not fully remote (on-site or hybrid = skip)
- Federal government employer or requires security clearance
- Defense contractor (Lockheed, Raytheon, SAIC, Leidos, Booz Allen, Northrop, General Dynamics, BAE, etc.)
- Obvious fake/fraudulent listing (unrealistic salary $400K+ for analyst, vague no-name company, staffing farms like SoftAppDesigns / CloudServiceTek / Hitapps / GlobalSoftSolution / Weboptimix / Teambuilderz / Alesig)
- Already processed in a prior run — check existing files in `job_summaries\` and skip any company+title combo already saved there

---

## Scoring Rubric (0–100)

| Category | Points |
|---|---|
| Role fit (title/level match) | 25 |
| Skills match (SQL, Python, BI tools, viz) | 25 |
| Remote confirmed | 20 |
| Compensation range ($75K+ preferred) | 15 |
| Company legitimacy & interest | 15 |

Pick the **top 3** scoring jobs after applying hard filters. Maximum 3 total per run.

---

## Output — Summary .txt Files

Save one file per job to:
`C:\Users\jdhum\OneDrive\Claude_Code\personal\job_hunt\job_summaries\`

**Filename format:** `summary_{Company}_{YYYY-MM-DD}.txt`
Example: `summary_Acme_Corp_2026-04-28.txt`

**File contents:**

```
==========================================================
JOB SUMMARY - {Company} | {Job Title}
==========================================================
Date: {YYYY-MM-DD}
Source: Indeed
Score: {XX}/100
URL: {apply link}

COMPENSATION
------------
{Salary range or "Not listed"}

WHY THIS IS A GOOD FIT
-----------------------
{2-3 sentences explaining why this matches Josh's background}

KEY REQUIREMENTS TO HIGHLIGHT IN APPLICATION
---------------------------------------------
- {keyword/skill from JD}
- {keyword/skill from JD}
- {keyword/skill from JD}
- {keyword/skill from JD}
- {keyword/skill from JD}

ATS KEYWORDS (include these in resume/cover letter)
----------------------------------------------------
{comma-separated list of 8-12 keywords pulled directly from the job description}

REQUIREMENTS SUMMARY
---------------------
Must-haves:
- {requirement}
- {requirement}
- {requirement}

Nice-to-haves:
- {requirement}
- {requirement}

WATCH-OUTS / GAPS
------------------
{Any mismatches between Josh's background and the JD}

NOTES
-----
{Anything else worth knowing — company size, industry, team context if mentioned}
==========================================================

FULL JOB POSTING
----------------
{Paste the complete job description text here, exactly as posted — do not summarize or truncate}
==========================================================
```

---

## Completion Report

After saving all 3 files, print a brief confirmation:

```
Done — {date}
Saved 3 job summaries:
1. {Title} @ {Company} — Score: {XX}/100
2. {Title} @ {Company} — Score: {XX}/100
3. {Title} @ {Company} — Score: {XX}/100

Top pick: {Company} — {one sentence why}
```

---

## What This Step Does NOT Do

- Does not draft resumes or cover letters
- Does not move or modify existing files
