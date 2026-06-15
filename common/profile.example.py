# ─────────────────────────────────────────────────────────────────────────────
# profile.example.py — Template for common/profile.py
# ─────────────────────────────────────────────────────────────────────────────
# Copy this file to common/profile.py and fill in your own information.
# profile.py is gitignored — it will never be committed.
#
# Used by scripts:  import profile  (after adding common/ to sys.path)
# Used by LLMs:     profile.to_markdown()  →  full markdown context block
# ─────────────────────────────────────────────────────────────────────────────

CONTACT = {
    "name":       "Your Full Name",
    "pro_name":   "Your Full Name, M.S.",        # professional display name
    "location":   "City, State",
    "email":      "your.email@gmail.com",
    "work_email": "you@yourcompany.com",          # optional — remove if not used
    "phone":      "(555) 000-0000",
    "work_phone": "(555) 000-0001",               # optional — remove if not used
    "linkedin":   "linkedin.com/in/your-profile",
    "github":     "github.com/YourUsername",
}

# ── Education ─────────────────────────────────────────────────────────────────
EDUCATION = [
    {
        "degree":     "M.S. Your Field (Specialization)",
        "school":     "University Name",
        "location":   "City, State",
        "date":       "Month Year",
        "coursework": [
            "Course Title 1",
            "Course Title 2",
            "Course Title 3",
            "Course Title 4",
            "Course Title 5",
            # The LLM selects 3-5 of these based on the job — list everything you took
        ],
    },
    {
        "degree":     "B.S. Your Undergraduate Field",
        "school":     "University Name",
        "location":   "City, State",
        "date":       "Month Year",
        "coursework": [
            "Course Title 1",
            "Course Title 2",
            "Course Title 3",
        ],
    },
]

# ── Work Experience ───────────────────────────────────────────────────────────
# context: factual background on what the role entailed
# bullets: accomplishments and responsibilities — raw material for tailored resume bullets
EXPERIENCE = [
    {
        "company":  "Your Most Recent Company",
        "title":    "Your Job Title",
        "location": "City, State",
        "dates":    "Month Year – Present",
        "context": (
            "Brief description of the role and its scope. What was the mandate? "
            "What environment were you operating in?"
        ),
        "bullets": [
            "Accomplishment or responsibility #1 — be specific, include metrics if real",
            "Accomplishment or responsibility #2",
            "Accomplishment or responsibility #3",
            "Accomplishment or responsibility #4",
            # Add as many as you have — the LLM selects the most relevant for each job
        ],
    },
    {
        "company":  "Previous Company",
        "title":    "Previous Job Title",
        "location": "City, State",
        "dates":    "Month Year – Month Year",
        "context": (
            "Brief description of the role."
        ),
        "bullets": [
            "Accomplishment or responsibility #1",
            "Accomplishment or responsibility #2",
            "Accomplishment or responsibility #3",
        ],
    },
]

# ── Technical Skills ──────────────────────────────────────────────────────────
SKILLS = {
    "Programming & Analytics": [
        "Python",
        "SQL",
        "R",
    ],
    "BI & Visualization": [
        "Power BI",
        "Excel (VBA, Pivot Tables)",
        "Dashboard Design",
    ],
    "Data Handling": [
        "ETL Pipeline Design",
        "Data Governance",
        "Database Management",
    ],
    # Add or remove categories to match your actual skill set
}

# ── Projects ─────────────────────────────────────────────────────────────────
# Optional. Include personal or academic projects that demonstrate technical depth
# not covered by work history — useful for AI/ML, automation, or data engineering roles.
# Leave as an empty list if you have none to include.
PROJECTS = [
    {
        "name":        "Your Project Name",
        "dates":       "2025 – Present",
        "type":        "personal",          # "personal", "academic project", "academic capstone"
        "tools":       ["Python", "pandas", "Some API"],
        "github":      "github.com/YourUsername/your-repo",   # optional — remove if no public repo
        "description": "One-sentence description of what this project does and why it matters.",
        "bullets": [
            "What you built and how — be specific about tools and scale",
            "What outcome or result the project produced",
        ],
        "ai_tool":    "Cursor AI",          # or "Claude Code", or omit if no AI tool used
        "ai_context": (
            "One sentence on how the AI tool was used — e.g., 'Developed with Cursor AI for "
            "scaffolding, API integration, and debugging.'"
        ),
    },
]

# ── Certifications ────────────────────────────────────────────────────────────
CERTS = [
    # "Certification Name — Issuing Organization — Year",
    # Leave empty list if none
]

# ── Core Competencies Pool ────────────────────────────────────────────────────
# The LLM selects 8-12 from this list based on what each job values.
COMPETENCY_POOL = [
    "Data Analytics",
    "Business Intelligence",
    "SQL",
    "Python",
    "Dashboard Design",
    "Stakeholder Reporting",
    "Data Governance",
    "Process Automation",
    # Add whatever accurately describes you
]

# ── Personal Interests ────────────────────────────────────────────────────────
# Included conditionally — only when the company's mission aligns with these interests.
# The LLM decides based on the resume_coverletter_guide.md rule.
INTERESTS = {
    "Your Activity": ["Specific discipline", "Specific discipline"],
    "Another Activity": ["Specific discipline"],
}

# ── Organizations ─────────────────────────────────────────────────────────────
# Included conditionally alongside Interests — always together or not at all.
ORGANIZATIONS = [
    "Organization Name",
    "Another Organization",
]

# ── Verified Metrics ──────────────────────────────────────────────────────────
# Real numbers only — the LLM is instructed not to invent metrics outside this dict.
METRICS = {
    "people_supported":   "350+",    # replace with your real numbers
    "people_trained":     "100+",
    "partner_agencies":   "5",
    "years_experience":   "9+",
    "degree_completed":   "Month Year",
}


# ── Markdown renderer ─────────────────────────────────────────────────────────

def to_markdown() -> str:
    """Render the full profile as a clean markdown block for LLM prompts."""
    lines = [
        "# Candidate Professional Profile",
        "",
        "Factual background data. Do not invent accomplishments, metrics, or skills not listed here.",
        "",
        "---",
        "",
        "## Contact",
        "",
    ]
    for key, val in CONTACT.items():
        lines.append(f"- **{key.replace('_', ' ').title()}**: {val}")
    lines.append("")

    lines += ["---", "", "## Education", ""]
    for edu in EDUCATION:
        lines.append(f"**{edu['degree']}** — {edu['school']} | {edu['location']} | **{edu['date']}**")
        lines.append(f"Relevant Coursework: {', '.join(edu['coursework'])}")
        lines.append("")

    lines += ["---", "", "## Work Experience", ""]
    for exp in EXPERIENCE:
        lines.append(f"### {exp['title']}")
        lines.append(f"**{exp['company']}** | {exp['location']} | {exp['dates']}")
        lines.append("")
        if exp.get("context"):
            lines.append(exp["context"])
            lines.append("")
        for b in exp["bullets"]:
            lines.append(f"- {b}")
        lines.append("")

    if PROJECTS:
        lines += ["---", "", "## Projects", ""]
        for proj in PROJECTS:
            ai_note = f" *(built with {proj['ai_tool']})*" if proj.get("ai_tool") else ""
            lines.append(f"### {proj['name']}{ai_note}")
            lines.append(f"**{proj['type'].title()}** | {proj['dates']} | Tools: {', '.join(proj['tools'])}")
            if proj.get("github"):
                lines.append(f"GitHub: {proj['github']}")
            lines.append("")
            lines.append(proj["description"])
            lines.append("")
            for b in proj["bullets"]:
                lines.append(f"- {b}")
            if proj.get("ai_context"):
                lines.append(f"\n*AI usage: {proj['ai_context']}*")
            lines.append("")

    lines += ["---", "", "## Technical Skills", ""]
    for category, items in SKILLS.items():
        lines.append(f"**{category}:** {', '.join(items)}")
    lines.append("")

    if CERTS:
        lines += ["---", "", "## Certifications", ""]
        for cert in CERTS:
            lines.append(f"- {cert}")
        lines.append("")

    lines += ["---", "", "## Verified Metrics", ""]
    for key, val in METRICS.items():
        label = key.replace("_", " ")
        lines.append(f"- **{val}** {label}")
    lines.append("")

    lines += ["---", "", "## Core Competencies", ""]
    lines.append(" | ".join(COMPETENCY_POOL))
    lines.append("")

    lines += ["---", "", "## Personal Interests", ""]
    for activity, disciplines in INTERESTS.items():
        lines.append(f"- **{activity}:** {', '.join(disciplines)}")
    lines.append("")

    lines += ["---", "", "## Organizations", ""]
    for org in ORGANIZATIONS:
        lines.append(f"- {org}")
    lines.append("")

    return "\n".join(lines)
