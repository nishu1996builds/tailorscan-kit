#!/usr/bin/env python3
"""Builds The Job Search Kit (the paid product) into kit/dist/. Requires python-docx, openpyxl, reportlab."""
import shutil
import zipfile
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Inches
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

import content as C
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont("DejaVu", str(__import__("pathlib").Path(__file__).resolve().parent / "fonts" / "DejaVuSans.ttf")))

HERE = Path(__file__).resolve().parent
OUT = HERE / "dist" / "The-Job-Search-Kit"
GREY = RGBColor(0x6B, 0x70, 0x78)
ACCENT_HEX = "1F6F5C"

# ---------------------------------------------------------------- Word helpers

def base_doc(font="Calibri", size=10.5, margins=0.7):
    d = Document()
    for s in d.sections:
        s.top_margin = s.bottom_margin = Inches(margins)
        s.left_margin = s.right_margin = Inches(margins)
    st = d.styles["Normal"]
    st.font.name = font
    st.element.rPr.rFonts.set(qn("w:eastAsia"), font)
    st.font.size = Pt(size)
    st.paragraph_format.space_after = Pt(2)
    st.paragraph_format.line_spacing = 1.08
    return d


def bottom_border(p, color="999999"):
    pPr = p._p.get_or_add_pPr()
    b = OxmlElement("w:pBdr")
    el = OxmlElement("w:bottom")
    for k, v in (("w:val", "single"), ("w:sz", "6"), ("w:space", "1"), ("w:color", color)):
        el.set(qn(k), v)
    b.append(el)
    pPr.append(b)


def para(d, text="", bold=False, italic=False, size=None, color=None, align=None, after=None, before=None):
    p = d.add_paragraph()
    if text:
        r = p.add_run(text)
        r.bold, r.italic = bold, italic
        if size:
            r.font.size = Pt(size)
        if color:
            r.font.color.rgb = color
    if align:
        p.alignment = align
    if after is not None:
        p.paragraph_format.space_after = Pt(after)
    if before is not None:
        p.paragraph_format.space_before = Pt(before)
    return p


def tip(d, text):
    return para(d, "Tip: " + text, italic=True, size=8.5, color=GREY, after=4)


def bullet(d, text):
    p = d.add_paragraph(style="List Bullet")
    p.add_run(text)
    p.paragraph_format.space_after = Pt(1)
    return p


# ---------------------------------------------------------------- resume templates

RESUME_DATA = {
    "name": "ALEX MORGAN",
    "contact": "Denver, CO  |  alex.morgan@email.com  |  (555) 555-0100  |  linkedin.com/in/alexmorgan",
    "headline": "Senior Marketing Analyst | Lifecycle, Experimentation, and Marketing Analytics",
    "summary": "Marketing analyst with 7 years turning customer data into revenue for B2C subscription brands. Built the experimentation program at Northwind that drove $2.1M in incremental revenue, and own SQL, Looker, and Braze end to end. Known for translating analysis into decisions that executives act on.",
    "jobs": [
        ("Senior Marketing Analyst", "Northwind Subscriptions", "Denver, CO", "Mar 2022 to Present", [
            "Built and ran a 60-test A/B testing program across email, push, and web, generating $2.1M in incremental annual revenue.",
            "Designed SQL churn models and Looker dashboards adopted by 5 teams, cutting weekly reporting time from 10 hours to 1.",
            "Partnered with Product to rebuild onboarding journeys in Braze, lifting Day-30 retention 14% across 900K new users.",
            "Mentored 2 junior analysts and set the team's analysis review standards.",
        ]),
        ("Marketing Analyst", "Bluepeak Retail", "Boulder, CO", "Jun 2019 to Feb 2022", [
            "Owned attribution reporting for a $6M paid media budget, reallocating 18% of spend to channels with 2x higher ROAS.",
            "Automated 12 recurring Excel reports with Python and SQL, saving 25 hours a month.",
            "Segmented a 1.4M-customer base by purchase behavior, informing a loyalty relaunch that raised repeat purchase rate 9%.",
        ]),
    ],
    "skills": [
        ("Analytics", "SQL, Python (pandas), Excel, A/B Testing, Cohort Analysis, Attribution, Forecasting"),
        ("Tools", "Looker, Tableau, Braze, Amplitude, Google Analytics 4, Segment, Snowflake, dbt"),
        ("Marketing", "Lifecycle Marketing, Segmentation, Personalization, Email Marketing, Paid Media"),
    ],
    "education": ("Bachelor of Science, Economics", "University of Colorado Boulder", "2019"),
    "certs": "Google Analytics Certification  |  Braze Certified Marketer",
}

STYLES = {
    "Classic": dict(font="Georgia", size=10.5, name_size=20, head_size=11, head_color=RGBColor(0x1A, 0x1A, 0x1A), center=True, caps=True),
    "Modern": dict(font="Calibri", size=10.5, name_size=24, head_size=11.5, head_color=RGBColor(0x1F, 0x6F, 0x5C), center=False, caps=True),
    "Senior": dict(font="Arial", size=10, name_size=18, head_size=10.5, head_color=RGBColor(0x22, 0x2B, 0x45), center=False, caps=True),
}


def build_resume(style_name):
    st = STYLES[style_name]
    R = RESUME_DATA
    d = base_doc(st["font"], st["size"])
    align = WD_ALIGN_PARAGRAPH.CENTER if st["center"] else None
    para(d, R["name"], bold=True, size=st["name_size"], align=align, after=0)
    para(d, R["contact"], size=9.5, align=align, after=2)
    if style_name != "Classic":
        para(d, R["headline"], bold=True, size=11, color=st["head_color"], align=align, after=2)

    def heading(t):
        p = para(d, t.upper() if st["caps"] else t, bold=True, size=st["head_size"], color=st["head_color"], before=8, after=3)
        bottom_border(p, ACCENT_HEX if style_name == "Modern" else "888888")

    heading("Summary")
    para(d, R["summary"], after=2)
    tip(d, "2 to 4 sentences. Open with the target job title from the posting, then your two strongest proof points. Delete every 'Tip' line before sending.")
    if style_name == "Senior":
        heading("Selected Results")
        for b in ["$2.1M incremental revenue from an experimentation program built from zero.",
                  "14% lift in Day-30 retention across 900K users through a lifecycle rebuild.",
                  "18% of a $6M media budget reallocated to 2x-ROAS channels."]:
            bullet(d, b)
        tip(d, "For senior roles, 3 headline results above the fold help recruiters see scope in 5 seconds.")
    heading("Experience")
    for i, (title, co, loc, dates, bullets) in enumerate(R["jobs"]):
        p = para(d, after=0, before=4 if i else 0)
        r = p.add_run(title)
        r.bold = True
        p.add_run(f"  |  {co}, {loc}")
        p2 = para(d, dates, italic=True, size=9.5, color=GREY, after=2)
        for b in bullets:
            bullet(d, b)
        if i == 0:
            tip(d, "Strong verb + what you did and with which tool + measurable result. Put the bullets that prove the posting's must-haves first.")
    heading("Skills")
    for k, v in R["skills"]:
        p = para(d, after=1)
        p.add_run(k + ": ").bold = True
        p.add_run(v)
    tip(d, "Use the posting's exact spelling for each tool. Plain comma-separated text only: no rating bars, icons, or tables.")
    heading("Education")
    deg, school, yr = R["education"]
    p = para(d, after=1)
    p.add_run(deg).bold = True
    p.add_run(f", {school}, {yr}")
    heading("Certifications")
    para(d, R["certs"])
    d.core_properties.title = f"Resume template ({style_name})"
    d.core_properties.author = "The Job Search Kit"
    return d


def build_cover_letter():
    d = base_doc("Calibri", 11, 1.0)
    para(d, "ALEX MORGAN", bold=True, size=16, after=0)
    para(d, "Denver, CO  |  alex.morgan@email.com  |  (555) 555-0100  |  linkedin.com/in/alexmorgan", size=9.5, after=12)
    para(d, "{Date}", after=8)
    para(d, "Dear {Hiring manager name, or 'Hiring Team'},", after=8)
    tip(d, "Pick ONE opening below and delete the other two.")
    para(d, "Opening A (direct): I'm applying for the {Role} role at {Company}. In my current role at {Company}, I {headline result that maps to the posting's top requirement}, and I'd like to do the same for your team.", after=6)
    para(d, "Opening B (company hook): {Specific thing the company did recently} caught my attention, because {why it connects to your work}. That's why the {Role} role stood out to me.", after=6)
    para(d, "Opening C (referral): {Referrer name}, who works on your {team}, suggested I reach out about the {Role} role. We worked together on {project}, where I {result}.", after=10)
    para(d, "Body paragraph 1: Match their top requirement. The posting emphasizes {requirement 1}. At {Company}, I {specific action} which {measurable result}. {One sentence on how that translates to their situation}.", after=8)
    para(d, "Body paragraph 2: Match their second and third requirements. I also bring {requirement 2} and {requirement 3}. For example, {short proof point with a number}.", after=8)
    para(d, "Close: I'd welcome the chance to discuss how I could help {Company} {specific goal from the posting}. Thank you for your time and consideration.", after=12)
    para(d, "Sincerely,", after=0)
    para(d, "Alex Morgan", after=12)
    tip(d, "Keep it under 300 words. A cover letter that mirrors three posting requirements with three proof points beats a long story every time.")
    return d


def build_scripts():
    d = base_doc("Calibri", 11, 0.9)
    para(d, "Outreach and Follow-up Scripts", bold=True, size=20, after=4)
    para(d, "Copy, replace everything in {braces}, and personalize at least one line. Specific beats long.", italic=True, color=GREY, after=10)
    for title, body in C.SCRIPTS:
        p = para(d, title, bold=True, size=13, before=10, after=4)
        bottom_border(p, ACCENT_HEX)
        for line in body.split("\n"):
            para(d, line, after=2)
    para(d, "Timing rules", bold=True, size=13, before=14, after=4)
    for t in ["Referral asks: before you apply, or the same day.", "Follow-up after applying: 7 to 10 days later, once.",
              "Thank-you notes: within 24 hours of each interview, one per interviewer.", "Post-interview check-in: 1 business day after the date they gave you, or 7 days if none.",
              "Stop after two follow-ups with no reply. Move on and log it as Ghosted in your tracker."]:
        bullet(d, t)
    return d


def build_screening():
    d = base_doc("Calibri", 11, 0.9)
    para(d, "Screening Question Answer Frameworks", bold=True, size=20, after=4)
    para(d, "25 questions you will see on application forms and recruiter screens. Each has a structure to follow and an example to adapt. Write your own version once and reuse it.", italic=True, color=GREY, after=10)
    for i, (q, how, ex) in enumerate(C.SCREENING, 1):
        p = para(d, f"{i}. {q}", bold=True, size=12.5, before=10, after=3)
        bottom_border(p, "CCCCCC")
        p = para(d, after=2)
        p.add_run("How to answer: ").bold = True
        p.add_run(how)
        if ex:
            p = para(d, after=2)
            p.add_run("Example: ").bold = True
            p.add_run(ex)
        para(d, "Your answer: ______________________________________________", color=GREY, after=2)
    return d


# ---------------------------------------------------------------- tracker

STATUSES = ["Shortlisted", "Applied", "Recruiter screen", "Interviewing", "Final round", "Offer", "Rejected", "Withdrawn", "Ghosted"]
SOURCES = ["LinkedIn", "Company site", "Referral", "Indeed", "Recruiter reached out", "Job board", "Networking", "Other"]
ACTIVE = ["Recruiter screen", "Interviewing", "Final round", "Offer"]


def build_tracker(path):
    wb = Workbook()
    head_fill = PatternFill("solid", fgColor=ACCENT_HEX)
    head_font = Font(bold=True, color="FFFFFF")
    thin = Side(style="thin", color="DDDDDD")

    # Lists sheet for dropdowns
    ls = wb.active
    ls.title = "Lists"
    ls["A1"], ls["B1"] = "Status", "Source"
    for i, s in enumerate(STATUSES, 2):
        ls[f"A{i}"] = s
    for i, s in enumerate(SOURCES, 2):
        ls[f"B{i}"] = s

    ws = wb.create_sheet("Applications", 0)
    cols = [("Company", 22), ("Role", 30), ("Job link", 28), ("Source", 18), ("Date applied", 13), ("Status", 17),
            ("Contact name", 18), ("Contact email or LinkedIn", 26), ("Last contact", 13), ("Next follow-up", 14),
            ("Days since touch", 10), ("Action", 13), ("TailorScan score", 10), ("Salary range", 16), ("Notes", 40)]
    for i, (name, w) in enumerate(cols, 1):
        c = ws.cell(row=1, column=i, value=name)
        c.fill, c.font = head_fill, head_font
        c.alignment = Alignment(wrap_text=True, vertical="center")
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[1].height = 32
    ws.freeze_panes = "C2"
    N = 500
    examples = [
        ("Northwind", "Senior Marketing Analyst", "https://example.com/job/1", "Referral", "=TODAY()-12", "Recruiter screen", "Sam Lee", "linkedin.com/in/samlee", "=TODAY()-2", None, None, None, 82, "$95K to $115K", "Screen went well. Case study next."),
        ("Bluepeak", "Lifecycle Marketing Manager", "https://example.com/job/2", "LinkedIn", "=TODAY()-9", "Applied", "", "", "", None, None, None, 76, "", "Follow up with hiring manager."),
        ("Acme Co", "Growth Analyst", "https://example.com/job/3", "Company site", "", "Shortlisted", "", "", "", None, None, None, None, "", "Tailor resume: add SQL bullet."),
    ]
    for r in range(2, N + 2):
        ws[f"J{r}"] = (f'=IF(OR(F{r}="",F{r}="Shortlisted",F{r}="Offer",F{r}="Rejected",F{r}="Withdrawn",AND(E{r}="",I{r}="")),"",'
                       f'MAX(E{r},I{r})+IF(F{r}="Applied",7,IF(F{r}="Ghosted",14,3)))')
        ws[f"K{r}"] = f'=IF(AND(E{r}="",I{r}=""),"",TODAY()-MAX(E{r},I{r}))'
        ws[f"L{r}"] = f'=IF(J{r}="","",IF(TODAY()>=J{r},"FOLLOW UP",""))'
        for col in "EIJ":
            ws[f"{col}{r}"].number_format = "mmm d, yyyy"
        for ci in range(1, len(cols) + 1):
            ws.cell(row=r, column=ci).border = Border(bottom=thin)
    for ri, row in enumerate(examples, 2):
        for ci, v in enumerate(row, 1):
            if v is not None:
                ws.cell(row=ri, column=ci, value=v)
    dv_status = DataValidation(type="list", formula1=f"=Lists!$A$2:$A${len(STATUSES) + 1}", allow_blank=True)
    dv_source = DataValidation(type="list", formula1=f"=Lists!$B$2:$B${len(SOURCES) + 1}", allow_blank=True)
    ws.add_data_validation(dv_status)
    ws.add_data_validation(dv_source)
    dv_status.add(f"F2:F{N + 1}")
    dv_source.add(f"D2:D{N + 1}")
    red = PatternFill("solid", fgColor="F8D7DA")
    ws.conditional_formatting.add(f"L2:L{N + 1}", CellIsRule(operator="equal", formula=['"FOLLOW UP"'], fill=red, font=Font(bold=True, color="9B1C2C")))
    for status, color in [("Offer", "C8E6C9"), ("Final round", "DCEDC8"), ("Interviewing", "E3F2FD"), ("Recruiter screen", "E8EAF6"), ("Rejected", "EEEEEE"), ("Ghosted", "EEEEEE")]:
        ws.conditional_formatting.add(f"A2:O{N + 1}", FormulaRule(formula=[f'$F2="{status}"'], fill=PatternFill("solid", fgColor=color)))

    # Dashboard
    db = wb.create_sheet("Dashboard", 1)
    db.column_dimensions["A"].width = 30
    for c in "BCDE":
        db.column_dimensions[c].width = 16
    db["A1"] = "Job Search Dashboard"
    db["A1"].font = Font(bold=True, size=18, color=ACCENT_HEX)
    db["A2"] = "Updates automatically from the Applications sheet."
    db["A2"].font = Font(italic=True, color="777777")
    A = "Applications!"
    rng = lambda col: f"{A}${col}$2:${col}${N + 1}"
    active_arr = "{" + ",".join(f'"{s}"' for s in ACTIVE) + "}"
    kpis = [
        ("Applications sent", f'=COUNT({rng("E")})'),
        ("Shortlisted, not yet applied", f'=COUNTIF({rng("F")},"Shortlisted")'),
        ("In active process", f'=SUM(COUNTIF({rng("F")},{{"Recruiter screen","Interviewing","Final round"}}))'),
        ("Offers", f'=COUNTIF({rng("F")},"Offer")'),
        ("Response rate (screen or beyond)", f'=IFERROR(SUM(COUNTIF({rng("F")},{active_arr}))/B4,0)'),
        ("Follow-ups due today", f'=COUNTIF({rng("L")},"FOLLOW UP")'),
        ("Applications in last 7 days", f'=COUNTIF({rng("E")},">="&(TODAY()-7))'),
        ("Average TailorScan score", f'=IFERROR(AVERAGE({rng("M")}),"")'),
    ]
    for i, (k, f) in enumerate(kpis, 4):
        db[f"A{i}"] = k
        db[f"B{i}"] = f
        db[f"A{i}"].font = Font(bold=True)
        db[f"B{i}"].font = Font(size=13, bold=True)
    db["B8"].number_format = "0%"
    db["B11"].number_format = "0"
    db["A14"] = "Pipeline by status"
    db["A14"].font = Font(bold=True, size=13)
    db["A15"], db["B15"] = "Status", "Count"
    for i, s in enumerate(STATUSES, 16):
        db[f"A{i}"] = s
        db[f"B{i}"] = f'=COUNTIF({rng("F")},A{i})'
    last = 15 + len(STATUSES)
    ch = BarChart()
    ch.type = "bar"
    ch.title = "Pipeline by status"
    ch.style = 10
    ch.legend = None
    ch.add_data(Reference(db, min_col=2, min_row=15, max_row=last), titles_from_data=True)
    ch.set_categories(Reference(db, min_col=1, min_row=16, max_row=last))
    ch.height, ch.width = 8, 16
    db.add_chart(ch, "D4")
    r0 = last + 3
    db[f"A{r0}"] = "Which sources work"
    db[f"A{r0}"].font = Font(bold=True, size=13)
    for j, h in enumerate(["Source", "Applications", "Screens or better", "Response rate"]):
        db.cell(row=r0 + 1, column=1 + j, value=h).font = Font(bold=True)
    for i, s in enumerate(SOURCES, r0 + 2):
        db[f"A{i}"] = s
        db[f"B{i}"] = f'=COUNTIFS({rng("D")},A{i},{rng("E")},"<>")'
        db[f"C{i}"] = f'=SUM(COUNTIFS({rng("D")},A{i},{rng("F")},{active_arr}))'
        db[f"D{i}"] = f"=IFERROR(C{i}/B{i},0)"
        db[f"D{i}"].number_format = "0%"

    # How to use
    hw = wb.create_sheet("How to use", 2)
    hw.column_dimensions["A"].width = 110
    lines = [
        ("How to use this tracker", True),
        ("1. Delete the three example rows on the Applications sheet (rows 2 to 4, columns A to I and M to O only; leave the formulas in J, K, L).", False),
        ("2. Log every role the moment you shortlist it. Set Status from the dropdown.", False),
        ("3. When you apply, enter the Date applied and change Status to Applied.", False),
        ("4. Whenever you hear from or message someone, update Last contact. The tracker recalculates Next follow-up.", False),
        ("5. Rows that need a follow-up show FOLLOW UP in red. Use the scripts in the kit, then update Last contact.", False),
        ("6. Check the Dashboard every Friday. Low response rate means fix the resume. Low screen-to-interview rate means practice answers.", False),
        ("", False),
        ("Follow-up rules built in: 7 days after applying, 3 days after any screen or interview contact, 14 days for Ghosted.", False),
        ("Works in Excel and Google Sheets (File > Import > Upload, then Replace spreadsheet).", False),
    ]
    for i, (t, b) in enumerate(lines, 1):
        hw[f"A{i}"] = t
        hw[f"A{i}"].font = Font(bold=b, size=16 if b else 11, color=ACCENT_HEX if b else "000000")
        hw[f"A{i}"].alignment = Alignment(wrap_text=True)
    wb.active = 0
    wb.save(path)


# ---------------------------------------------------------------- playbook PDF

def build_playbook(path):
    ss = getSampleStyleSheet()
    accent = colors.HexColor("#" + ACCENT_HEX)
    body = ParagraphStyle("b", parent=ss["BodyText"], fontName="Helvetica", fontSize=10.5, leading=15, spaceAfter=7)
    h1 = ParagraphStyle("h1", parent=ss["Heading1"], fontName="Helvetica-Bold", fontSize=19, leading=23, textColor=accent, spaceAfter=10, spaceBefore=4)
    h2 = ParagraphStyle("h2", parent=ss["Heading2"], fontName="Helvetica-Bold", fontSize=13, leading=17, spaceBefore=10, spaceAfter=6)
    bul = ParagraphStyle("bul", parent=body, leftIndent=14, bulletIndent=2)
    box = ParagraphStyle("box", parent=bul, bulletFontName="DejaVu", bulletFontSize=10, leftIndent=18)
    title = ParagraphStyle("t", parent=h1, fontSize=32, leading=38, alignment=TA_CENTER)
    sub = ParagraphStyle("s", parent=body, fontSize=13, leading=18, alignment=TA_CENTER, textColor=colors.HexColor("#555555"))
    cell = ParagraphStyle("c", parent=body, fontSize=9.5, leading=13, spaceAfter=0)

    def p(t, st=body):
        return Paragraph(t.replace("&", "&amp;").replace("<", "&lt;"), st)

    story = [Spacer(1, 2.2 * inch), p("The Tailoring Playbook", title), Spacer(1, 10),
             p("Tailor any resume to any job posting in 15 minutes, without lying and without starting over.", sub),
             Spacer(1, 1.6 * inch), p("Part of The Job Search Kit", sub), PageBreak()]
    for heading, paras in C.PLAYBOOK:
        story.append(p(heading, h1))
        for t in paras:
            if t.startswith("- "):
                story.append(Paragraph(t[2:].replace("&", "&amp;"), bul, bulletText="•"))
            else:
                story.append(p(t))
        story.append(Spacer(1, 6))
    story.append(PageBreak())
    story.append(p("Before and after: weak bullets rewritten", h1))
    rows = [[p("Before", cell), p("After", cell)]] + [[p(a, cell), p(b, cell)] for a, b in C.WEAK_TO_STRONG]
    t = Table(rows, colWidths=[2.6 * inch, 4.2 * inch])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), accent), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                           ("VALIGN", (0, 0), (-1, -1), "TOP"), ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
                           ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F4F8F6")]),
                           ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    rows[0][0].textColor = colors.white
    story += [t, PageBreak(), p("160 action verbs by category", h1),
              p("Start every bullet with one of these. Pick the verb that shows the most ownership you can truthfully claim.")]
    for cat, verbs in C.ACTION_VERBS.items():
        story.append(p(cat, h2))
        story.append(p(verbs))
    story += [PageBreak(), p("The 15-minute checklist", h1), p("Print this page or keep it open next to every application.")]
    for item in ["Posting marked up: must-haves, nice-to-haves, repeated phrases", "Scanned in TailorScan; missing keywords copied",
                 "Target job title in headline or summary", "Summary's first sentence mirrors the top two must-haves",
                 "Every must-have I have appears in Skills AND in one bullet", "Most relevant bullets moved to the top of each role",
                 "40% or more of bullets have a number", "No 'responsible for', 'helped with', or cliches",
                 "Re-scanned: score 75 or higher", "Saved as Firstname-Lastname-Company-Role.pdf",
                 "Logged in tracker with date and source", "Referral or hiring-manager message sent (top roles)"]:
        story.append(Paragraph(item, box, bulletText="\u2610"))
    doc = SimpleDocTemplate(str(path), pagesize=LETTER, leftMargin=0.9 * inch, rightMargin=0.9 * inch, topMargin=0.85 * inch, bottomMargin=0.85 * inch,
                            title="The Tailoring Playbook", author="The Job Search Kit")

    def footer(canvas, d):
        if d.page > 1:
            canvas.setFont("Helvetica", 8)
            canvas.setFillColor(colors.HexColor("#888888"))
            canvas.drawString(0.9 * inch, 0.5 * inch, "The Tailoring Playbook  |  The Job Search Kit")
            canvas.drawRightString(LETTER[0] - 0.9 * inch, 0.5 * inch, str(d.page))
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


START_HERE = """THE JOB SEARCH KIT: START HERE
================================

Thank you for buying the kit. Here is the fastest way to use it.

1. Read 1-Tailoring-Playbook.pdf (20 minutes). It is the system everything else plugs into.
2. Pick one template from 2-Resume-Templates. Move your content in, then delete every "Tip:" line.
   - Classic: traditional, safest for finance, law, healthcare, and government.
   - Modern: clean with a color accent; good for tech, marketing, and startups.
   - Senior: adds a Selected Results block for manager-and-up roles.
3. Open 3-Application-Tracker.xlsx (Excel or Google Sheets) and log every role you apply to.
4. Use 4-Outreach-Scripts.docx for referrals and follow-ups, and 5-Screening-Answers.docx to prepare
   your answers once and reuse them.
5. Before each application, scan your resume against the posting with the free TailorScan scanner.

All Word files open in Microsoft Word, Google Docs (File > Open > Upload), and Apple Pages.

Refunds: if the kit is not useful, email within 30 days for a full refund.
"""


def main():
    if OUT.parent.exists():
        shutil.rmtree(OUT.parent)
    (OUT / "2-Resume-Templates").mkdir(parents=True)
    build_playbook(OUT / "1-Tailoring-Playbook.pdf")
    for i, name in enumerate(STYLES, 1):
        build_resume(name).save(OUT / "2-Resume-Templates" / f"Resume-Template-{i}-{name}.docx")
    build_cover_letter().save(OUT / "2-Resume-Templates" / "Cover-Letter-Template.docx")
    build_tracker(OUT / "3-Application-Tracker.xlsx")
    build_scripts().save(OUT / "4-Outreach-Scripts.docx")
    build_screening().save(OUT / "5-Screening-Answers.docx")
    (OUT / "0-START-HERE.txt").write_text(START_HERE)
    zpath = OUT.parent / "The-Job-Search-Kit.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(OUT.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(OUT.parent))
    print("Built", zpath, f"({zpath.stat().st_size // 1024} KB)")
    for f in sorted(OUT.rglob("*")):
        if f.is_file():
            print("  ", f.relative_to(OUT))


if __name__ == "__main__":
    main()
