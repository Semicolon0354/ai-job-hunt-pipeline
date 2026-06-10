# Resume and Cover Letter Guide

Instructions for generating a tailored resume and cover letter for Josh Humphreys.

Always use alongside:
- `common/profile.py` (via `profile.to_markdown()`) — factual background: contact, education, work history, skills, metrics
- `common/write_like_josh.md` — voice and tone for the cover letter

---

## Inputs

**Primary input:** A job summary `.txt` file

Extract from it:
- Company name and job title
- Must-have and nice-to-have requirements
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

## Tailoring Notes — Read Before Every Application

**Secret clearance:** Josh holds an active Secret clearance through the Army National Guard. Always mention for government, defense, or cleared-role postings. Do not mention for uncleared civilian roles.

**Remote / salary:** Fully remote preferred, full-time individual contributor, target $80K–$120K. Do not include in resume or cover letter — for screening only.

**Tableau vs. Power BI:** Power BI is Josh's primary BI tool. Josh has not used Tableau. Do NOT list Tableau as a skill or claim experience with it. If a job requires Tableau, acknowledge the gap and note that his Power BI expertise transfers directly — never list Tableau in the skills section or imply fluency.

**Healthcare domain expertise:** Josh has genuine, operationally grounded domain knowledge from EMS. Lead with this for any healthcare analytics role.

**Military framing:** Emphasize data work, leadership outcomes, and organizational impact for civilian employers. "Built analytics infrastructure for a 350-person organization" lands better than "supported Battalion readiness reporting."

**Career narrative:** Quantitative thinker (math degree) → discovered data in the field (EMS compliance reporting) → went back to school (M.S. Data Analytics) → now applying that training full-time (Knowledge Manager, targeting dedicated analytics roles).

**Current employment:** Josh is actively employed as Knowledge Manager at the Colorado Army National Guard. Frame as "currently in a data-adjacent role targeting a dedicated analytics position" — never as unemployed or seeking.

---

## Resume — Tailoring Rules

### Professional Summary
Write a 2–3 sentence summary targeted to this specific role:
- Match the job title language exactly
- Lead with the credential most relevant to this role
- Reference the specific domain if applicable (healthcare, defense, operations)
- Incorporate 2–3 ATS keywords naturally
- Do not reuse the same summary across applications
- Spell out the unit in full when referencing the current role: "Knowledge Manager for the 5th BN, 19th Special Forces Group, Colorado Army National Guard"

**Starting points by role type** (always rewrite to match the job's language and ATS keywords):

*BI / Data Analyst:* "Data analytics and business intelligence professional with a Master's in Data Analytics (AI/ML specialization) and a background in mathematics. Skilled in building Power BI solutions, automating data workflows, and translating operational data into actionable insights for leadership. Currently serving as Knowledge Manager for the 5th BN, 19th Special Forces Group, Colorado Army National Guard, supporting data-driven decision-making for over 350 personnel."

*Healthcare Analytics:* "Data analytics professional with a Master's in Data Analytics and a decade of experience in healthcare operations — including frontline EMS and supervisory roles at UCHealth EMS. Experienced building compliance dashboards, automating regulatory reporting, and turning clinical and operational data into decisions that affect patient care and resource utilization."

*Data Science / ML:* "Data science professional with a Master's in Data Analytics (AI/ML specialization) and a Bachelor's in Mathematics. Skilled in predictive modeling, machine learning (scikit-learn, TensorFlow), and statistical analysis across Python, R, and SAS. Background in applying data science methods to real operational problems in healthcare and defense."

*Government / Defense:* "Data analytics and knowledge management professional with active service in the Colorado Army National Guard and a Master's in Data Analytics. Experienced building BI infrastructure and data governance programs from the ground up in policy-constrained, resource-limited environments. Holds active Secret clearance. Skilled in Power BI, Power Automate, and SharePoint."

### Core Competencies
Select 8–12 from Josh's competency pool that directly match job requirements. Use the job's own language where possible. Place programming languages (SQL, R, Python) last — after BI, domain, and analytics skills.

### Experience — Role Placement

**Professional Experience** (always present, in this order):
1. **Knowledge Manager**, 5th BN 19th SFG CONG (Jul 2024–Present) — always leads, never omit
2. **Operations Supervisor**, UCHealth EMS (Sep 2020–Oct 2023) — always in Professional Experience
3. **Special Forces Medical Sergeant**, 5th BN 19th SFG CONG (Jul 2019–Present) — always in Professional Experience

**Placement depends on job type:**
4. **Paramedic**, UCHealth EMS (Oct 2014–Sep 2020):
   - Healthcare / clinical analytics roles → Professional Experience
   - General data / BI / analytics roles → Additional Experience

### Experience — How to Write Bullets

Select the most relevant bullets from the profile for each role based on what the job values. You may make minor wording adjustments to incorporate 1–2 ATS keywords naturally — but the core accomplishment and message of each bullet must remain intact. Do not rewrite bullets from scratch. Do not invent accomplishments or metrics not present in the profile.

**Bullet count:**
- Every role in Professional Experience: exactly 4 bullets
- Every role in Additional Experience: exactly 2 bullets
- Bullet count never changes role placement. Do not move a role to a different section to meet a count. If a role has fewer profile bullets than needed, use all available ones.

**Per-role emphasis when selecting bullets:**
- *Knowledge Manager:* weight toward Power BI, Power Automate, SharePoint, data governance, stakeholder reporting, or training — depending on what this job values
- *Operations Supervisor:* weight toward Excel VBA automation, dashboard design, operational analytics, or stakeholder reporting; extra weight for healthcare roles
- *Special Forces Medical Sergeant:* select bullets around leadership, resource management, cross-functional coordination, and risk-based decision-making; avoid medical specifics for non-healthcare roles
- *Paramedic:* select bullets around patient care coordination, rapid decision-making, and multi-variable problem-solving

### Education
Always include both degrees:
- M.S. Data Analytics, Colorado State University Global Campus | Apr 2025
- B.S. Mathematics, University of Wyoming | Dec 2013

Select 3–5 coursework items from the profile's coursework list that are most relevant to this role. You may only use courses that appear verbatim in the profile — do not invent, rename, or paraphrase course titles.

Relevant courses by role type (all titles are exact — use as-is):
- ML/AI roles: Foundations of Artificial Intelligence, Principles of Machine Learning, Predictive Analytics
- BI / data warehouse roles: Data Warehousing in Enterprise Environments, Data Mining and Visualization, Enterprise Performance Management

### Skills Section
Group by category. Prioritize tools explicitly mentioned in the job description. Never include Tableau.

### Format
- Clean, single-column, ATS-friendly — no tables, text boxes, or graphics
- Font: Calibri, 10–11pt body, 12–14pt name
- Margins: 0.75–1 inch
- Section order: Summary → Core Competencies → Experience → Education → Skills
- Bold job titles and company names; dates right-aligned
- No certifications section
- 1–2 pages

---

## Cover Letter — Structure

Apply `common/write_like_josh.md` in full. 4 paragraphs, approximately 300–400 words.

**Paragraph 1 — Opening: Why This Role, Why Now**
Don't open with "I am writing to express my interest." Open with what Josh is applying for and a specific, genuine reason this role appeals to him. Reference something concrete about the company or role. 1–3 sentences.

**Paragraph 2 — The Bridge: Background to This Role**
Connect Josh's background to this specific job. Lead with the most relevant experience. Explain the through-line: EMS → data analytics → Knowledge Manager at the National Guard → this role. Use "That is," or "Stated differently," at least once. Reference his M.S. in Data Analytics (completed April 2025) and B.S. in Mathematics. 3–5 sentences.

**Paragraph 3 — Proof: Specific, Relevant Work**
Name 2–3 concrete accomplishments directly relevant to this job's requirements. Use real numbers from the verified metrics (50 ambulance crews, 350 soldiers, 5 partner agencies, 100+ administrators). Work in 2–3 ATS keywords naturally. 3–5 sentences.

**Paragraph 4 — Close: Direct and Confident**
Direct expression of interest and availability. No sycophancy. "I'd welcome the chance to discuss how my background fits your team's priorities." One sentence thank-you. Sign off: Joshua Humphreys.

### Cover Letter Format
- Standard business letter format
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
- [ ] Every Professional Experience role has exactly 4 bullets
- [ ] Every Additional Experience role has exactly 2 bullets
- [ ] Tableau is not listed anywhere
- [ ] No certifications section
- [ ] Cover letter is in Josh's voice (see write_like_josh.md)
- [ ] No passive voice in the cover letter
- [ ] No corporate filler ("leverage synergies," "results-driven," "passionate professional")
- [ ] Both files saved to the correct applications subfolder

---

## Learned — 2026-06-10 (Crossroads_2026-06-09)
- List only tools Josh actually uses. Describe Power BI automation as "Power Query and DAX" — never invent a competency (e.g., "Revenue Cycle Management") that isn't in his profile.
