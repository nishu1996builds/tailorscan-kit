#!/usr/bin/env python3
"""Builds the free lead magnet PDF (The 15-Minute Resume Tailoring Checklist) into the public site's assets."""
import sys
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
import content as C
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont("DejaVu", str(__import__("pathlib").Path(__file__).resolve().parent / "fonts" / "DejaVuSans.ttf")))

out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "dist" / "Resume-Tailoring-Checklist.pdf"
out.parent.mkdir(parents=True, exist_ok=True)
ss = getSampleStyleSheet()
A = colors.HexColor("#1F6F5C")
body = ParagraphStyle("b", parent=ss["BodyText"], fontName="Helvetica", fontSize=9.6, leading=12, spaceAfter=2)
h1 = ParagraphStyle("h1", parent=body, fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=A, spaceAfter=2)
h2 = ParagraphStyle("h2", parent=body, fontName="Helvetica-Bold", fontSize=11.5, leading=14, spaceBefore=5, spaceAfter=1)
sub = ParagraphStyle("s", parent=body, textColor=colors.HexColor("#555555"), fontSize=11)
bul = ParagraphStyle("bul", parent=body, leftIndent=16, bulletIndent=2, spaceAfter=3)
box = ParagraphStyle("box", parent=bul, bulletFontName="DejaVu", bulletFontSize=10, leftIndent=18)

steps = [
    ("Decode the posting (3 min)", ["Mark must-haves: anything under Requirements or with 'required', 'must', 'minimum'.",
                                    "Mark nice-to-haves: Preferred, Bonus, 'a plus'.",
                                    "Circle phrases used 2+ times. Repetition shows what the hiring manager cares about.",
                                    "Paste the posting and your resume into the free TailorScan scanner and copy the missing keywords."]),
    ("Match the title and summary (2 min)", ["Put the posting's job title in your headline or summary (never change a past job title).",
                                             "Rewrite your summary's first sentence to mirror the top two must-haves."]),
    ("Close the keyword gaps (5 min)", ["For each missing keyword you truly have: add it to Skills using the posting's exact spelling.",
                                        "Work it into one bullet that proves you used it, ideally in your most recent role.",
                                        "Skip keywords you don't have. Never hide keywords in white text."]),
    ("Reorder for relevance (3 min)", ["Move bullets that prove must-haves to the top of each role.",
                                       "Cut bullets that prove nothing this posting asks for."]),
    ("Re-scan and ship (2 min)", ["Re-scan: aim for 75+ on roles you fit.",
                                  "At least 40% of bullets have a number. No 'responsible for'.",
                                  "Save as Firstname-Lastname-Company-Role.pdf and log it in your tracker."]),
]
story = [Paragraph("The 15-Minute Resume Tailoring Checklist", h1),
         Paragraph("Tailor any resume to any job posting in 15 minutes, without lying and without starting over.", sub), Spacer(1, 6)]
for i, (t, items) in enumerate(steps, 1):
    story.append(Paragraph(f"Step {i}: {t}", h2))
    for it in items:
        story.append(Paragraph(it, box, bulletText="\u2610"))
story += [Paragraph("The bullet formula", h2),
          Paragraph("<b>Strong verb</b> + <b>what you did, with which tool</b> + <b>measurable result</b>.", body),
          Paragraph("<i>Example: Cut onboarding time 30% (10 days to 7) by rebuilding the welcome flow in Braze.</i>", body),
          Paragraph("ATS-safe formatting in 30 seconds", h2)]
for r in ["One column. No tables, text boxes, icons, or skill bars.", "Standard headings: Summary, Experience, Education, Skills.",
          "Contact info in the body, not the Word header or footer.", "Export a text-based PDF. If you can select the text, an ATS can read it."]:
    story.append(Paragraph(r, bul, bulletText="•"))
cta = Table([[Paragraph("<b>Want the full system?</b> The Job Search Kit adds 3 ATS-safe resume templates, the full Tailoring Playbook "
                        "(160 verbs and before-and-after rewrites), an application tracker that schedules your follow-ups, outreach and "
                        "negotiation scripts, and 25 screening answer frameworks.<br/><br/><b>Use code LAUNCH for $10 off:</b> "
                        "nishulegacy.gumroad.com/l/job-search-kit/LAUNCH", body)]], colWidths=[6.7 * inch])
cta.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 1.5, A), ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#E3F1EC")),
                         ("TOPPADDING", (0, 0), (-1, -1), 10), ("BOTTOMPADDING", (0, 0), (-1, -1), 10), ("LEFTPADDING", (0, 0), (-1, -1), 12)]))
story += [Spacer(1, 8), cta, Spacer(1, 4),
          Paragraph("Free scanner: nishu1996builds.github.io/tailorscan", sub)]
SimpleDocTemplate(str(out), pagesize=LETTER, leftMargin=0.85 * inch, rightMargin=0.85 * inch, topMargin=0.55 * inch, bottomMargin=0.5 * inch,
                  title="The 15-Minute Resume Tailoring Checklist", author="TailorScan").build(story)
print("Built", out)
