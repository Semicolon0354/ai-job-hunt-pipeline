# ─────────────────────────────────────────────────────────────────────────────
# Josh Humphreys — Canonical Profile
# ─────────────────────────────────────────────────────────────────────────────
# Pure factual data about Josh's background, experience, and skills.
# No task-specific instructions — those live in the relevant skill/guide files.
#
# Used by scripts:  import profile (after adding common/ to sys.path)
# Used by LLMs:     profile.to_markdown()  →  full markdown context block
# ─────────────────────────────────────────────────────────────────────────────

CONTACT = {
    "name":       "Joshua Humphreys",
    "pro_name":   "Joshua Humphreys, M.S.",
    "location":   "Loveland, CO",
    "email":      "jdhumphreys01@gmail.com",
    "work_email": "jhumphreys@ridgeline-data.com",
    "phone":      "(307) 241-0083",
    "work_phone": "(970) 305-5464",
    "linkedin":   "linkedin.com/in/joshua-humphreys-a7687b223",
    "github":     "github.com/Semicolon0354",
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
# context: factual background on what the role entailed
# bullets: accomplishments and responsibilities — raw material for tailored resume bullets
EXPERIENCE = [
    {
        "company":  "5th Battalion, 19th Special Forces Group — Colorado Army National Guard",
        "title":    "Knowledge Manager",
        "location": "Watkins, CO",
        "dates":    "July 2024 – Present",
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
        "company":  "University of Colorado Health Emergency Medical Services (UCHealth EMS)",
        "title":    "Operations Supervisor",
        "location": "Windsor, CO",
        "dates":    "September 2020 – October 2023",
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
        "company":  "5th Battalion, 19th Special Forces Group — Colorado Army National Guard",
        "title":    "Special Forces Medical Sergeant",
        "location": "Watkins, CO",
        "dates":    "July 2019 – Present",
        "context": (
            "Special Forces qualified. Reserve component service running in parallel with civilian career."
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
        "company":  "University of Colorado Health Emergency Medical Services (UCHealth EMS)",
        "title":    "Paramedic",
        "location": "Windsor, CO",
        "dates":    "October 2014 – September 2020",
        "context": (
            "Front-line prehospital care provider with 6 years of direct patient care experience "
            "serving multiple counties in Northern Colorado."
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
CERTS = []

# ── Core Competencies Pool ────────────────────────────────────────────────────
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
# Do not invent metrics outside of these.
METRICS = {
    "soldiers_supported": "350+",
    "admins_trained":     "100+",
    "partner_agencies":   "5",
    "ambulance_crews":    "50+",
    "ems_years":          "9+",
    "ms_graduation":      "April 2025",
    "bs_graduation":      "December 2013",
    "clearance":          "Active Secret (Army National Guard)",
}


# ── Markdown renderer ─────────────────────────────────────────────────────────

def to_markdown() -> str:
    """Render the full profile as a clean markdown block for LLM prompts."""
    lines = [
        "# Josh Humphreys — Professional Profile",
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
    metric_labels = {
        "soldiers_supported": "soldiers supported through Power BI dashboards (National Guard)",
        "admins_trained":     "administrators trained in Microsoft 365 (National Guard)",
        "partner_agencies":   "partner agencies served by Excel VBA automated compliance reports (UCHealth EMS)",
        "ambulance_crews":    "ambulance crews supervised, coached, and monitored (UCHealth EMS)",
        "ems_years":          "years in prehospital emergency medicine",
        "ms_graduation":      "M.S. Data Analytics completed",
        "bs_graduation":      "B.S. Mathematics completed",
        "clearance":          "",
    }
    for key, val in METRICS.items():
        label = metric_labels.get(key, key.replace("_", " "))
        lines.append(f"- **{val}** {label}".rstrip())
    lines.append("")

    lines += ["---", "", "## Core Competencies", ""]
    lines.append(" | ".join(COMPETENCY_POOL))
    lines.append("")

    return "\n".join(lines)
