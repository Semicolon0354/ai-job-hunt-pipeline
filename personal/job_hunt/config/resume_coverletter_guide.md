# Resume and Cover Letter Guide

Instructions for generating a tailored resume and cover letter for Josh Humphreys from a job summary .txt file.

Always use this guide alongside:
- `common\josh_profile.md` — complete work history, skills, education, bullet bank
- `common\write_like_josh.md` — voice and tone for the cover letter

---

## Inputs

**Primary input:** A job summary `.txt` file from `job_summaries\`

Extract from it:
- Company name and job title
- Must-have requirements
- Nice-to-have requirements
- ATS keywords (exact phrases from the job description)
- Watch-outs / gaps

---

## Output Files

Save both files to:
`C:\Users\jdhum\OneDrive\Claude_Code\personal\job_hunt\applications\{Company}_{YYYY-MM-DD}\`

- `Humphreys_Resume_{Company}_{Role}.docx`
- `Humphreys_Cover_Letter_{Company}_{Role}.docx`

Also move the source `.txt` summary into the same subfolder.

---

## Resume — Tailoring Rules

### Professional Summary
Write a 2–3 sentence summary targeted to this specific role:
- Match the job title language exactly (if they say "Data Analyst," use "Data Analyst")
- Lead with the credential most relevant to this role
- Reference the specific domain if applicable (healthcare, defense, operations)
- Incorporate 2–3 ATS keywords naturally
- Do not reuse the same summary across applications

### Core Competencies
Select 8–12 skills from Josh's profile that directly match job requirements. Use the job's own language where possible (e.g., "data pipeline development" not "ETL" if that's what they wrote).

### Experience — Tailoring Rules

**Knowledge Manager (CONG, Jul 2024–Present):** Always leads. Emphasize Power BI, Power Automate, SharePoint, data governance, stakeholder reporting, and training — depending on what the job values.

**Operations Supervisor (UCHealth EMS, Sep 2020–Oct 2023):** Emphasize Excel VBA automation, dashboard design, operational analytics, stakeholder reporting. Healthcare analytics roles get extra weight here.

**Special Forces Medical Sergeant (CONG, Jul 2019–Present):** Always include in main experience. Frame around leadership, resource management, cross-functional coordination, and risk-based decision-making. Downplay medical specifics for non-healthcare roles.

**Paramedic (UCHealth EMS, Oct 2014–Sep 2020):**
- Healthcare/clinical analytics roles → include in main Experience
- General data/BI/analytics roles → move to "Additional Experience" at the bottom

**Bullet count:**
- Every role in the main Experience section: exactly 4 bullets each — this applies to all roles listed there, not just the first one
- Every role in the Additional Experience section: exactly 2 bullets each

For each relevant bullet, work in 1–2 ATS keywords where they fit naturally. Don't keyword-stuff.

### Education
Always include both degrees:
- M.S. Data Analytics, Colorado State University Global Campus | Apr 2025
- B.S. Mathematics, University of Wyoming | Dec 2013

Tailor listed coursework to what the job values:
- ML/AI roles: Foundations of Artificial Intelligence, Principles of Machine Learning, Predictive Analytics
- BI/data warehouse roles: Data Warehousing in Enterprise Environments, Data Mining and Visualization, Enterprise Performance Management

### Skills Section
Group by category. Prioritize tools explicitly mentioned in the job description at the top of each category.

### Format
- Clean, single-column, ATS-friendly — no tables, text boxes, or graphics
- Font: Calibri, 10–11pt body, 12–14pt name
- Margins: 0.75–1 inch
- Section order: Summary → Core Competencies → Experience → Education → Skills
- Bold company names and job titles; dates right-aligned
- 1–2 pages

---

## Cover Letter — Structure

Apply `common\write_like_josh.md` in full. 4 paragraphs, approximately 300–400 words.

**Paragraph 1 — Opening: Why This Role, Why Now**
Don't open with "I am writing to express my interest." Open with what Josh is applying for and a specific, genuine reason this role appeals to him. Reference something concrete about the company or role. 1–3 sentences.

**Paragraph 2 — The Bridge: Background to This Role**
Connect Josh's background to this specific job. Lead with the most relevant experience. Explain the through-line: EMS → data analytics → Knowledge Manager at the National Guard → this role. Use "That is," or "Stated differently," at least once. Reference his M.S. in Data Analytics (completed April 2025) and B.S. in Mathematics. 3–5 sentences.

**Paragraph 3 — Proof: Specific, Relevant Work**
Name 2–3 concrete accomplishments directly relevant to this job's requirements. Use real numbers (50 ambulance crews, 350 soldiers, 5 partner agencies, 100+ administrators). Work in 2–3 ATS keywords naturally. 3–5 sentences.

**Paragraph 4 — Close: Direct and Confident**
Direct expression of interest and availability. No sycophancy. "I'd welcome the chance to discuss how my background fits your team's priorities." One sentence thank-you. Sign off: Joshua Humphreys.

### Cover Letter Format
- Standard business letter format
- Header: Joshua Humphreys | Loveland, CO 80538 | jdhumphreys01@gmail.com | (307) 241-0083 | LinkedIn | GitHub
- Date, RE: line, "Dear Hiring Manager,"
- 4 paragraphs, no more
- Margins: 1 inch
- Font: Calibri, 10.5pt

---

## Pre-Save Checklist

Before saving, verify:
- [ ] ATS keywords from the job description appear in both documents
- [ ] Professional summary is specific to this role (not a copy-paste)
- [ ] All numbers are accurate — do not invent metrics
- [ ] Cover letter is in Josh's voice (see write_like_josh.md)
- [ ] No passive voice in the cover letter
- [ ] No corporate filler ("leverage synergies," "results-driven," "passionate professional")
- [ ] Both files saved to the correct applications subfolder
- [ ] Filenames follow the convention

---
## Learned — 2026-06-10 (Crossroads_2026-06-09)
- Contact header is two lines: line 1 = phone | email | location; line 2 = LinkedIn | GitHub. Always include github.com/Semicolon0354 — do not omit the GitHub link.
- Do not include a Certifications section. Josh removes it; leave certifications off the resume unless he explicitly asks for them.
- List only tools Josh actually uses. Drop Tableau and Excel Power Pivot. Describe Power BI automation as "Power Query and DAX," not "SQL and Excel Power Pivot," and never invent a competency (e.g., "Revenue Cycle Management") that isn't in his profile.
- In Core Competencies, place programming languages (SQL, R, Python) last — after BI, domain, and analytics skills — not at the front.
- When naming the Knowledge Manager role in the summary, spell out the unit in full: "the Knowledge Manager for the 5th BN, 19th Special Forces Group, Colorado Army National Guard," not just "Colorado Army National Guard."
