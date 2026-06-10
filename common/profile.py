# ─────────────────────────────────────────────────────────────────────────────
# Josh Humphreys — Canonical Profile
# ─────────────────────────────────────────────────────────────────────────────
# Single source of truth for all scripts and LLM prompts across projects.
# Edit this file to update your information everywhere at once.
#
# Used by scripts:  import profile (after adding common/ to sys.path)
# Used by LLMs:     profile.to_markdown()  →  full markdown context block
# ─────────────────────────────────────────────────────────────────────────────

CONTACT = {
    "name":     "Joshua Humphreys",
    "pro_name": "Joshua Humphreys, M.S.",
    "location": "Loveland, CO",
    "email":    "jdhumphreys01@gmail.com",
    "work_email": "jhumphreys@ridgeline-data.com",
    "phone":    "(307) 241-0083",
    "work_phone": "(970) 305-5464",
    "linkedin": "linkedin.com/in/joshua-humphreys-a7687b223",
    "github":   "github.com/Semicolon0354",
}

# ── Education ─────────────────────────────────────────────────────────────────
EDUCATION = [
    {
        "degree":     "M.S. Data Analytics (AI/ML Specialization)",
        "school":     "Colorado State University Global Campus",
        "location":   "Aurora, CO",
        "date":       "April 2025",
        "coursework": [
            "Data Mining and Visualization",
            "Predictive Analytics",
            "Data Warehousing in Enterprise Environments",
            "Enterprise Performance Management",
            "Foundations of Artificial Intelligence",
            "Principles of Machine Learning",
            "Database Concepts",
            "Business Analytics",
            "Business Intelligence",
            "Foundations of Data Analytics",
        ],
    },
    {
        "degree":     "B.S. Mathematics",
        "school":     "University of Wyoming",
        "location":   "Laramie, WY",
        "date":       "December 2013",
        "coursework": [
            "Symbolic Logic",
            "Combinatorics",
            "Matrix Theory",
            "Numerical Analysis",
            "Mathematical Analysis",
        ],
    },
]

# ── Work Experience ───────────────────────────────────────────────────────────
# placement: "main"        → always in main experience section
#            "conditional" → main for healthcare roles, additional for general roles
EXPERIENCE = [
    {
        "company":   "5th Battalion, 19th Special Forces Group — Colorado Army National Guard",
        "title":     "Knowledge Manager",
        "location":  "Watkins, CO",
        "dates":     "July 2024 – Present",
        "placement": "main",
        "context": (
            "Given a broad mandate to modernize the organization's data management and internal "
            "communications, Josh built the Battalion's Knowledge Management function from the "
            "ground up in a resource-constrained, policy-limited environment."
        ),
        "bullets": [
            "Built the Battalion's Knowledge Management function from the ground up, establishing "
            "data management processes, communication frameworks, and BI reporting infrastructure "
            "with minimal existing resources",
            "Built robust Power BI semantic models, reports, and dashboards to enhance performance "
            "monitoring and leadership engagement with over 350 soldiers",
            "Designed and implemented Power Automate workflows to integrate data from disconnected "
            "systems into SharePoint, improving cross-functional data accessibility and operational efficiency",
            "Developed and delivered Microsoft 365 training sessions for over 100 administrators, "
            "enhancing digital literacy and improving leadership engagement with organizational data",
            "Created sustainable data governance strategies within strict policy and resource constraints "
            "to streamline organizational processes",
            "Designed SharePoint-based information architecture to centralize and standardize access "
            "to organizational data and documentation",
            "Applied creative problem-solving to deliver analytics impact in a resource-limited "
            "environment with minimal legacy technical infrastructure",
        ],
    },
    {
        "company":   "University of Colorado Health Emergency Medical Services (UCHealth EMS)",
        "title":     "Operations Supervisor",
        "location":  "Windsor, CO",
        "dates":     "September 2020 – October 2023",
        "placement": "main",
        "context": (
            "Field supervisor for a large prehospital EMS operation serving multiple counties in "
            "Northern Colorado. Took on data and analytics responsibilities in addition to operational "
            "leadership — this is where Josh's data analytics career began."
        ),
        "bullets": [
            "Leveraged Excel VBA to automate individualized monthly compliance reports for 5 partner "
            "agencies, eliminating manual reporting and improving regulatory compliance accuracy and efficiency",
            "Compiled and visualized operational data for over 50 ambulance crews to optimize deployment "
            "strategies and enhance service delivery",
            "Designed interactive dashboards to enable leadership to monitor crew performance, identify "
            "trends, and make data-informed operational decisions",
            "Supervised and mentored over 50 ambulance crews, providing performance feedback, professional "
            "development guidance, and disciplinary oversight",
            "Coordinated logistical and operational support for ambulance crews, optimizing resource "
            "allocation and response readiness",
            "Built automated data workflows that reduced manual reporting burden and improved data "
            "reliability for compliance and performance tracking",
            "Partnered with leadership to translate operational data into actionable decisions about "
            "staffing, deployment, and agency partnerships",
        ],
    },
    {
        "company":   "5th Battalion, 19th Special Forces Group — Colorado Army National Guard",
        "title":     "Special Forces Medical Sergeant",
        "location":  "Watkins, CO",
        "dates":     "July 2019 – Present",
        "placement": "main",
        "context": (
            "Special Forces qualified. Reserve component service running in parallel with civilian "
            "career. Frame around leadership and data-relevant skills, not medical procedures "
            "(unless applying to clinical analytics roles)."
        ),
        "bullets": [
            "Advised senior leadership on resource allocation, risk management, and operational "
            "planning, ensuring effective utilization of personnel, equipment, and medical assets "
            "to support mission success",
            "Supervised, trained, and mentored medical personnel, non-medical teammates, and allied "
            "partners, enhancing team readiness and technical proficiency",
            "Managed mission-critical information and reporting in high-stakes, time-sensitive "
            "operational environments",
            "Applied data-driven risk assessment and resource planning to support mission execution "
            "and decision-making at the leadership level",
        ],
    },
    {
        "company":   "University of Colorado Health Emergency Medical Services (UCHealth EMS)",
        "title":     "Paramedic",
        "location":  "Windsor, CO",
        "dates":     "October 2014 – September 2020",
        "placement": "conditional",  # main for healthcare roles; additional for general analytics
        "context": (
            "Front-line prehospital care provider. 6 years of direct patient care experience. "
            "Include in main Experience for healthcare/clinical roles. "
            "Move to Additional Experience for general data/BI/analytics roles."
        ),
        "bullets": [
            "Coordinated the actions of responding crews to deliver prompt on-scene stabilization "
            "and comprehensive care to medical and trauma patients",
            "Articulated assessment findings and interventions clearly and concisely to receiving "
            "medical providers, contributing to continuity of patient care",
            "Managed complex, multi-variable emergency situations requiring rapid data synthesis, "
            "pattern recognition, and decisive action under pressure",
        ],
    },
]

# ── Technical Skills ──────────────────────────────────────────────────────────
SKILLS = {
    "Programming & Analytics": [
        "Python (pandas, NumPy, SciPy, scikit-learn, TensorFlow)",
        "R",
        "SAS",
        "SQL (PostgreSQL)",
        "Statistical Modeling",
        "Predictive Analytics",
    ],
    "Data Handling": [
        "Data Preprocessing & Cleaning",
        "ETL Pipeline Design",
        "Data Mining",
        "Database Management",
        "Data Governance",
    ],
    "BI & Visualization": [
        "Power BI (DAX, Power Query)",
        "Excel (VBA, Pivot Tables)",
        "Dashboard Design",
    ],
    "Automation & Collaboration": [
        "Power Automate",
        "SharePoint",
        "Microsoft 365",
        "Jupyter",
    ],
    "Machine Learning & AI": [
        "Supervised/Unsupervised Learning",
        "Neural Networks",
        "Regression Modeling",
        "Classification",
        "Feature Engineering",
    ],
}

# ── Certifications ────────────────────────────────────────────────────────────
# Currently none — add any relevant certifications here (e.g., Microsoft Certified: Data Analyst Associate)
CERTS = []

# ── Core Competencies Pool ────────────────────────────────────────────────────
# LLM picks 8–12 per application based on what the job description emphasizes.
COMPETENCY_POOL = [
    "Data Analytics",
    "Business Intelligence",
    "Power BI",
    "SQL",
    "Python",
    "ETL Pipeline Development",
    "Dashboard Design",
    "Predictive Modeling",
    "Statistical Analysis",
    "Data Governance",
    "Power Automate",
    "SharePoint Administration",
    "Stakeholder Reporting",
    "Statistical Analysis",
    "Cross-Functional Collaboration",
    "Project Management",
    "Personnel Management",
    "Training & Development",
    "Process Automation",
    "Knowledge Management",
    "Data Visualization",
    "Machine Learning",
    "Data Preprocessing",
    "Database Management",
    "Operational Analytics",
    "Healthcare Analytics",
]

# ── Verified Metrics ──────────────────────────────────────────────────────────
# Authoritative numbers to use in bullets and cover letters.
# Never invent metrics outside of these.
METRICS = {
    "soldiers_supported":     "350+",
    "admins_trained":         "100+",
    "partner_agencies":       "5",
    "ambulance_crews":        "50+",
    "ems_years":              "9+",
    "ms_graduation":          "April 2025",
    "bs_graduation":          "December 2013",
    "clearance":              "Active Secret (Army National Guard)",
}

# ── Tailoring Notes (LLM guidance) ───────────────────────────────────────────
TAILORING_NOTES = """\
**Secret clearance:** Josh holds an active Secret clearance through the Army National Guard. \
Always mention for government, defense, or cleared-role postings. \
Do not mention for uncleared civilian roles.

**Remote preference:** Fully remote, full-time individual contributor. \
Target salary $80K–$120K. \
Do not include in resume or cover letter — for screening only.

**Tableau vs. Power BI:** Power BI is Josh's primary BI tool. \
Josh has not used Tableau. Do NOT list Tableau as a skill he has or claim experience with it. \
If a job requires Tableau, acknowledge the gap and note that his Power BI expertise transfers directly — \
he is confident he can ramp on Tableau quickly. Never list Tableau in the skills section or imply fluency.

**Healthcare domain expertise:** Josh has genuine, operationally grounded domain knowledge \
from EMS. Lead with this for any healthcare analytics role.

**Military framing for civilian employers:** Emphasize data work, leadership outcomes, and \
organizational impact. "Built analytics infrastructure for a 350-person organization" lands \
better than "supported Battalion readiness reporting."

**Career narrative:** The through-line is: quantitative thinker (math degree) → discovered data \
in the field (EMS compliance reporting) → went back to school (M.S. Data Analytics) → now \
applying that training full-time (Knowledge Manager, targeting dedicated analytics roles).

**Current employment:** Josh is actively employed as Knowledge Manager at the Colorado Army \
National Guard. Do not frame as "unemployed and seeking" — frame as "currently in a \
data-adjacent role and targeting a dedicated analytics position."\
"""

# ── Professional Summary Templates ───────────────────────────────────────────
# Starting points only — always rewrite to match the specific job's language and ATS keywords.
SUMMARY_TEMPLATES = {
    "bi_analyst": (
        "Data analytics and business intelligence professional with a Master's in Data Analytics "
        "(AI/ML specialization) and a background in mathematics. Skilled in building Power BI "
        "solutions, automating data workflows, and translating operational data into actionable "
        "insights for leadership. Currently serving as Knowledge Manager for the Colorado Army "
        "National Guard, supporting data-driven decision-making for over 350 personnel."
    ),
    "healthcare_analytics": (
        "Data analytics professional with a Master's in Data Analytics and a decade of experience "
        "in healthcare operations — including frontline EMS and supervisory roles at UCHealth EMS. "
        "Experienced building compliance dashboards, automating regulatory reporting, and turning "
        "clinical and operational data into decisions that affect patient care and resource utilization."
    ),
    "data_science_ml": (
        "Data science professional with a Master's in Data Analytics (AI/ML specialization) and a "
        "Bachelor's in Mathematics. Skilled in predictive modeling, machine learning (scikit-learn, "
        "TensorFlow), and statistical analysis across Python, R, and SAS. Background in applying "
        "data science methods to real operational problems in healthcare and defense."
    ),
    "government_defense": (
        "Data analytics and knowledge management professional with active service in the Colorado "
        "Army National Guard and a Master's in Data Analytics. Experienced building BI infrastructure "
        "and data governance programs from the ground up in policy-constrained, resource-limited "
        "environments. Holds active Secret clearance. Skilled in Power BI, Power Automate, and SharePoint."
    ),
}


# ── Markdown renderer ─────────────────────────────────────────────────────────

def to_markdown() -> str:
    """
    Render the full profile as markdown suitable for pasting into LLM prompts.
    This is the equivalent of josh_profile.md — generated from the data above.
    """
    lines = [
        "# Josh Humphreys — Complete Profile Reference",
        "",
        "**Source of truth for all resume and cover letter generation.**",
        "Do not invent accomplishments, metrics, or skills not listed here.",
        "Always read this before drafting any resume section.",
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
        lines.append("")
        lines.append(f"Key Coursework: {', '.join(edu['coursework'])}")
        lines.append("")

    lines += ["---", "", "## Work Experience", ""]
    for exp in EXPERIENCE:
        tag = "← Current role, always leads" if "2024 – Present" in exp["dates"] and exp["placement"] == "main" else ""
        lines.append(f"### {exp['title']}")
        lines.append(f"**{exp['company']}** | {exp['location']}")
        header = f"**{exp['dates']}**"
        if tag:
            header += f"  {tag}"
        lines.append(header)
        lines.append("")
        if exp.get("context"):
            lines.append(f"**Context:** {exp['context']}")
            lines.append("")
        if exp["placement"] == "conditional":
            lines.append(
                "**Placement rule:** Healthcare/clinical roles → main Experience section. "
                "General data/BI/analytics roles → Additional Experience section."
            )
            lines.append("")
        max_b = 6 if exp["placement"] == "main" else 3
        min_b = 4 if exp["placement"] == "main" else 2
        lines.append(f"**Bullet bank — choose {min_b}–{max_b} most relevant per application:**")
        for b in exp["bullets"]:
            lines.append(f"- {b}")
        lines.append("")

    lines += ["---", "", "## Technical Skills — Full Inventory", ""]
    for category, items in SKILLS.items():
        lines.append(f"### {category}")
        for item in items:
            lines.append(f"- {item}")
        lines.append("")

    if CERTS:
        lines += ["---", "", "## Certifications", ""]
        for cert in CERTS:
            lines.append(f"- {cert}")
        lines.append("")

    lines += [
        "---",
        "",
        "## Core Competencies Pool",
        "Pick 8–12 per application based on what the job description emphasizes:",
        "",
        " | ".join(COMPETENCY_POOL),
        "",
    ]

    lines += ["---", "", "## Key Numbers & Accomplishments", "Use these in bullet points and cover letters — don't invent new metrics:", ""]
    labels = {
        "soldiers_supported": "soldiers supported through Power BI dashboards (National Guard)",
        "admins_trained":     "administrators trained in Microsoft 365 tools (National Guard)",
        "partner_agencies":   "partner agencies served by Excel VBA automated compliance reports (UCHealth EMS)",
        "ambulance_crews":    "ambulance crews supervised, coached, and monitored via dashboards (UCHealth EMS)",
        "ems_years":          "years in prehospital emergency medicine (paramedic through supervisor)",
        "ms_graduation":      "M.S. Data Analytics completed",
        "bs_graduation":      "B.S. Mathematics, University of Wyoming",
        "clearance":          "",
    }
    for key, val in METRICS.items():
        label = labels.get(key, key.replace("_", " "))
        if label:
            lines.append(f"- {val} {label}")
        else:
            lines.append(f"- {val}")
    lines.append("")

    lines += ["---", "", "## Tailoring Notes — Read Before Every Application", "", TAILORING_NOTES, ""]

    lines += [
        "---",
        "",
        "## Professional Summary Templates",
        "These are **starting points only** — always rewrite to match the specific job's language and ATS keywords.",
        "",
    ]
    role_labels = {
        "bi_analyst":          "BI / Data Analyst roles",
        "healthcare_analytics": "Healthcare Analytics roles",
        "data_science_ml":     "Data Science / ML roles",
        "government_defense":  "Government / Defense / Operations Analytics roles",
    }
    for key, text in SUMMARY_TEMPLATES.items():
        lines.append(f"**For {role_labels.get(key, key)} roles:**")
        lines.append(text)
        lines.append("")

    return "\n".join(lines)
