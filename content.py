"""Written content for The Job Search Kit. Kept separate from the file builders so it is easy to edit."""

ACTION_VERBS = {
    "Leadership and ownership": "Led, Owned, Directed, Headed, Spearheaded, Championed, Orchestrated, Oversaw, Chaired, Mobilized, Steered, Founded, Established, Pioneered, Instituted, Drove",
    "Building and creating": "Built, Created, Designed, Developed, Launched, Engineered, Architected, Authored, Produced, Introduced, Formulated, Devised, Prototyped, Shipped, Composed, Constructed",
    "Growth and results": "Grew, Increased, Expanded, Accelerated, Boosted, Doubled, Tripled, Generated, Captured, Won, Exceeded, Surpassed, Outperformed, Delivered, Achieved, Secured",
    "Efficiency and savings": "Cut, Reduced, Saved, Streamlined, Automated, Consolidated, Simplified, Eliminated, Shortened, Lowered, Minimized, Standardized, Optimized, Accelerated, Trimmed, Recovered",
    "Improvement and change": "Improved, Transformed, Rebuilt, Redesigned, Overhauled, Revamped, Modernized, Restructured, Reorganized, Upgraded, Refined, Strengthened, Turned around, Revitalized, Migrated, Reengineered",
    "Analysis and insight": "Analyzed, Assessed, Audited, Diagnosed, Evaluated, Forecast, Identified, Investigated, Mapped, Measured, Modeled, Quantified, Researched, Tested, Uncovered, Validated",
    "Collaboration and influence": "Partnered, Aligned, Negotiated, Persuaded, Convinced, Brokered, Coordinated, Facilitated, Mediated, Unified, Rallied, Advised, Consulted, Collaborated, Bridged, Influenced",
    "People development": "Mentored, Coached, Trained, Hired, Recruited, Onboarded, Developed, Promoted, Upskilled, Guided, Enabled, Empowered, Built (a team), Scaled (a team), Grew (a team), Retained",
    "Communication": "Presented, Pitched, Published, Wrote, Edited, Briefed, Documented, Reported, Translated, Articulated, Showcased, Promoted, Marketed, Publicized, Educated, Represented",
    "Execution and operations": "Executed, Implemented, Deployed, Rolled out, Delivered, Managed, Operated, Administered, Maintained, Scheduled, Processed, Resolved, Fulfilled, Coordinated, Organized, Ran",
}

WEAK_TO_STRONG = [
    ("Responsible for managing the company newsletter.", "Grew the company newsletter from 8K to 31K subscribers in 10 months while lifting click rate from 2.1% to 3.4%."),
    ("Helped with the website redesign.", "Led content migration for a 400-page website redesign, launching on schedule with zero broken links and a 22% lift in organic sessions."),
    ("Worked on improving customer onboarding.", "Rebuilt the 5-step onboarding flow after 20 user interviews, cutting time-to-first-value from 9 days to 4."),
    ("Handled social media accounts.", "Ran Instagram and LinkedIn for a B2B brand, growing followers 140% and sourcing 60 demo requests in two quarters."),
    ("Duties included data entry and reporting.", "Automated a weekly sales report in Excel and Power Query, saving the team 6 hours a week and removing manual errors."),
    ("Assisted the sales team with leads.", "Qualified 300+ inbound leads a month for 4 AEs, raising lead-to-meeting conversion from 11% to 19%."),
]

PLAYBOOK = [
    ("Why most applications get no response", [
        "Most companies use an applicant tracking system (ATS) such as Workday, Greenhouse, Lever, or iCIMS. The ATS parses your resume into fields, and recruiters then search and filter those fields by keyword, title, and location. A resume that does not use the posting's language may never appear in those searches, even when the candidate is qualified.",
        "Then a human reads it, usually for 10 to 30 seconds. They look for three things: the right title, the right tools, and proof of results. Tailoring is how you win both rounds. It does not mean rewriting your resume from scratch for every job. It means adjusting about 20% of it so the posting's must-haves are easy to find.",
        "This playbook gives you a 15-minute routine for doing that, repeatably."
    ]),
    ("Step 1 (3 minutes): Decode the posting", [
        "Read the posting once, then mark it up in three passes:",
        "- Must-haves: anything under Requirements, Qualifications, or What you'll need, and anything with 'required', 'must', or 'minimum'.",
        "- Nice-to-haves: anything under Preferred, Bonus, or 'a plus'.",
        "- Repeated phrases: words or phrases used two or more times. Repetition shows what the hiring manager cares about most.",
        "Paste the posting and your resume into the free TailorScan scanner. It does these three passes for you and returns the missing keywords ranked by priority. Copy the missing list."
    ]),
    ("Step 2 (2 minutes): Match the title and summary", [
        "Recruiters search by job title first. If the posting says 'Lifecycle Marketing Manager' and your resume says 'CRM Specialist' for the same work, add the posting's title to your headline or summary: 'Lifecycle marketing manager with 6 years running CRM programs for consumer apps.'",
        "Never change an official job title in your experience section to one you did not hold. Use the summary and headline to bridge the language instead.",
        "Rewrite the first sentence of your summary to mirror the role's top two must-haves. Keep the summary to 2 to 4 sentences."
    ]),
    ("Step 3 (5 minutes): Close the keyword gaps", [
        "Take the missing keywords from Step 1. For each one you truly have:",
        "- Add it to your Skills section using the posting's exact wording ('Customer.io', not 'customer io'; 'A/B testing', not 'split tests').",
        "- Work it into one bullet that proves you used it, ideally in your most recent role.",
        "For keywords you do not have, leave them out. Every keyword on your resume is fair game in an interview. If a must-have is missing, the honest move is to show the closest adjacent experience: 'Built journeys in Iterable (Braze-equivalent)' is truthful and readable by both the ATS and the recruiter.",
        "Aim to cover every must-have you really have, and most nice-to-haves. Do not paste a block of keywords in white text or in a hidden section. Modern ATS systems and recruiters spot it, and it is an instant rejection."
    ]),
    ("Step 4 (3 minutes): Reorder for relevance", [
        "Within each role, move the bullets that prove the posting's must-haves to the top. Recruiters read the first two bullets of each job and skim the rest.",
        "Cut or shorten bullets that prove nothing this posting asks for. A focused 1-page resume beats an unfocused 2-page resume.",
        "If the role emphasizes one skill heavily (for example SQL), make sure it appears in your most recent role, not only in a job from five years ago."
    ]),
    ("Step 5 (2 minutes): Re-scan and ship", [
        "Paste your updated resume back into the scanner. Target a score of 75 or higher for roles you are qualified for. Past about 85, extra keywords help less than readability.",
        "Check the best-practice list: contact info in plain text, standard section headings, at least 40% of bullets with a number, no 'responsible for'.",
        "Save as PDF with a clear file name, such as Firstname-Lastname-Company-Role.pdf, unless the posting asks for Word. Log the application in your tracker the same minute."
    ]),
    ("The bullet formula", [
        "Every strong bullet answers three questions: What did you do? How? What changed as a result?",
        "Formula: Strong verb + what you did (with which tool or method) + measurable result (with context).",
        "Example: 'Cut onboarding time 30% (10 days to 7) by rebuilding the welcome flow in Braze with behavior-triggered emails.'",
        "If you do not have an exact number, use a defensible estimate and its basis: 'about 20 hours a month', 'roughly 3x', 'from weekly to daily'. You can also use scale (users, budget, team size, accounts) or rank ('#2 of 24 reps').",
        "Numbers that work well: percent change, dollars (revenue, savings, budget), time (hours saved, cycle time), volume (users, tickets, accounts), rank, and frequency."
    ]),
    ("ATS-safe formatting rules", [
        "- Use one column. Two-column layouts are often read left to right across both columns, scrambling your content.",
        "- Use standard headings: Summary, Experience, Education, Skills, Certifications.",
        "- Keep contact details in the document body, not in the Word header or footer.",
        "- No tables, text boxes, icons, images, charts, or skill-rating bars.",
        "- Use common fonts (Calibri, Arial, Helvetica, Georgia, Garamond) at 10 to 12 pt.",
        "- Use the same date format everywhere, for example 'Jan 2023 to Present' or '01/2023 to Present'.",
        "- Export to PDF from Word or Google Docs, not by scanning or printing to image. Test it: if you can select and copy the text, an ATS can read it.",
        "The three templates in this kit follow all of these rules."
    ]),
    ("The weekly system", [
        "Tailored applications beat volume, but you still need volume. A sustainable target for most people is 10 to 15 tailored applications a week plus 5 outreach messages.",
        "- Monday: find and shortlist 15 to 20 roles. Log them in the tracker with status 'Shortlisted'.",
        "- Tuesday to Thursday: tailor and apply to 3 to 5 a day using the 15-minute routine. For your top 5 roles, find a person to message using the outreach scripts.",
        "- Friday: open the tracker dashboard. Send every follow-up the tracker flags as due. Look at your funnel: if applications are not turning into screens, your resume needs work; if screens are not turning into interviews, practice your answers.",
        "A typical funnel for tailored applications with outreach is roughly 10 to 20% to recruiter screen. If you are below 5%, revisit your title alignment and keyword coverage first."
    ]),
]

SCRIPTS = [
    ("Referral ask (friend or former colleague)", "Subject: Quick favor, {Company} role\n\nHi {Name},\n\nHope you're doing well. I saw that {Company} is hiring a {Role} and it lines up closely with what I've been doing at {Current company}, especially {one specific overlap from the posting}.\n\nWould you be open to referring me, or pointing me to the right person on the team? I've attached my resume and the posting link is here: {Link}. Happy to send a short blurb you can forward.\n\nEither way, thanks, and let me know how things are going with you.\n\n{Your name}"),
    ("Referral ask (weak tie or alumni)", "Hi {Name}, I'm a fellow {school or past company} alum and I'm applying for the {Role} role on your team at {Company}. I've spent {X years} doing {relevant work}, most recently {one-line result}. Would you be open to a 15-minute chat about the team, or to referring me if it seems like a fit? Totally understand if not. Thanks either way."),
    ("Recruiter cold message (LinkedIn, under 300 characters)", "Hi {Name}, I just applied for the {Role} role at {Company}. I've {one-line proof, e.g. 'run lifecycle programs for 2M+ users in Braze and lifted retention 14%'}. Happy to share more if helpful. Thanks for your time!"),
    ("Hiring manager note", "Subject: {Role} application, {one-line proof}\n\nHi {Name},\n\nI applied for the {Role} role and wanted to reach out directly. Your posting mentions {specific priority}. At {Company}, I {specific result that maps to it}.\n\nI'd love to learn what success looks like in the first 90 days and share how I've approached {priority} before. Would a 20-minute call next week work?\n\nThanks,\n{Your name}\n{LinkedIn URL}"),
    ("Follow-up after applying (7 to 10 days later)", "Subject: Following up on {Role} application\n\nHi {Name},\n\nI applied for the {Role} position on {date} and wanted to follow up. I'm still very interested, especially in {specific thing about the team or product}. In my current role I {one relevant result}.\n\nIs there any other information I can share to help with your review?\n\nBest,\n{Your name}"),
    ("Thank-you after an interview (same day)", "Subject: Thank you, {Role} interview\n\nHi {Name},\n\nThank you for the conversation today. I especially enjoyed discussing {specific topic}. It made me even more excited about {what you'd work on}.\n\nYou mentioned {challenge they raised}. One idea I didn't get to share: {brief, concrete idea or relevant example}.\n\nLooking forward to the next steps.\n\nBest,\n{Your name}"),
    ("Follow-up when you have not heard back after an interview", "Subject: Checking in, {Role}\n\nHi {Name},\n\nI wanted to check in on the {Role} process. I'm still very interested and happy to provide anything else that would help, such as references or a work sample.\n\nThanks again,\n{Your name}"),
    ("Salary negotiation (after a written offer)", "Subject: {Role} offer\n\nHi {Name},\n\nThank you for the offer. I'm excited about the role and the team. Before I sign, I'd like to discuss the base salary. Based on {market data source, e.g. 'comparable offers I'm considering' or 'published ranges for this level'} and the scope we discussed, including {specific responsibility}, I was expecting a base closer to {number}.\n\nIf we can get there, I'm ready to accept. Is there flexibility on base, or on {sign-on bonus, equity, or start date} if base is fixed?\n\nThanks,\n{Your name}"),
    ("Withdrawing politely (keeps the door open)", "Hi {Name}, thank you for your time throughout the process. I've decided to accept another offer that's a closer fit for me right now, so I'd like to withdraw my application. I really enjoyed meeting the team and would love to stay in touch for the future."),
]

SCREENING = [
    ("Tell me about yourself.", "Present, past, future in 60 to 90 seconds. Present: your current role and the one result you're proudest of. Past: the 1 or 2 experiences that led here. Future: why this role is the logical next step.", "\"I lead lifecycle marketing at Brightcart, where I own email and push for 2 million users. Last year our onboarding rebuild lifted Day-7 activation 18%. Before that I ran newsletters and reporting at Fernway, which is where I learned to tie every campaign to a revenue number. I'm looking for a role with more ownership of retention strategy, which is why this one stood out.\""),
    ("Why do you want to work here?", "One specific thing about the company (product, mission, or a recent move), one thing about the role, and one way you'd contribute. Avoid generic praise.", "\"Your shift to a subscription model is exactly the problem I've been solving: getting users to a second purchase. The role owns the full lifecycle, and I've built that end to end before.\""),
    ("Why are you leaving your current job?", "Stay positive and forward-looking. Talk about what you are moving toward, not away from.", "\"I've learned a lot, but the team is consolidating around one channel and I want to own the full lifecycle. This role does that.\""),
    ("What are your salary expectations?", "Research the range first. If you must give a number, give a researched range with your target at the bottom. If the posting lists a range, you can anchor to it.", "\"Based on my research for this level in this market, I'm targeting {range}. I'm flexible depending on the full package and scope.\""),
    ("What is your greatest weakness?", "Name a real, non-critical weakness, the specific system you use to manage it, and evidence it's improving.", "\"I used to over-polish analysis before sharing it. Now I share a rough cut at 70% with a clear 'draft' label, which cut my turnaround in half and gets feedback earlier.\""),
    ("Tell me about a time you failed.", "Use STAR (Situation, Task, Action, Result) and spend most of the time on what you learned and changed.", "Pick a real miss, own it in one sentence, then show the process change that came out of it."),
    ("Describe a conflict with a coworker.", "Show that you seek to understand, use data, and preserve the relationship.", "Focus on a disagreement about approach, not personality, and end with the shared outcome."),
    ("Why should we hire you?", "Restate their top 3 must-haves and give one proof point for each.", "\"You need someone who can own Braze, run experiments, and report to execs. I've done all three: {proof 1}, {proof 2}, {proof 3}.\""),
    ("Where do you see yourself in five years?", "Show ambition that fits the company's path, and commitment to the role in front of you.", "\"Deeper in retention strategy, likely leading a small team. This role is the right foundation for that.\""),
    ("Are you authorized to work in {country}?", "Answer accurately and briefly. If you need sponsorship, say so plainly; misstating it can void an offer.", "\"Yes, I'm authorized to work in the US without sponsorship.\" or \"I will need sponsorship for an H-1B transfer.\""),
    ("When can you start?", "Be honest about notice periods. Two weeks is standard in the US.", "\"I'd give my current employer two weeks' notice, so I could start {date}.\""),
    ("Are you willing to relocate or work on-site?", "Answer the actual question and state any constraints up front.", "\"Yes, I'm open to a hybrid schedule three days a week in the Austin office.\""),
    ("How many years of experience do you have with {skill}?", "Give the honest number and a proof point. If short, show depth.", "\"Three years hands-on with SQL, daily. I write the cohort and funnel queries for our retention reporting.\""),
    ("What is a project you are most proud of?", "Pick a project that maps to this role. STAR, with a strong number in the Result.", "Structure: context in one sentence, your specific actions, the measurable result, what you'd do differently."),
    ("How do you prioritize competing deadlines?", "Show a system: impact versus effort, stakeholder alignment, and communication.", "\"I rank work by impact and deadline, confirm the top three with my manager weekly, and flag trade-offs early instead of missing dates quietly.\""),
    ("How do you handle feedback?", "Give a specific example of feedback you acted on and the result.", "Name the feedback, what you changed, and how it improved your work."),
    ("Tell me about a time you used data to make a decision.", "STAR with a clear before-and-after metric.", "Show the question, the analysis, the decision, and the measurable outcome."),
    ("Tell me about a time you led without authority.", "Focus on influence: aligning goals, sharing data, building allies.", "Describe how you got another team to change priorities and what it achieved."),
    ("What do you know about our company?", "Two facts from research (product, customers, recent news) and one connection to your work.", "Mention a recent launch or earnings note and why it matters for this role."),
    ("What questions do you have for us?", "Always ask 2 or 3. Good ones: What does success look like in 90 days? What is the biggest challenge for this team right now? How do you measure this role?", ""),
    ("Describe your ideal manager or work environment.", "Be honest, but describe traits most good companies share.", "\"Clear goals, direct feedback, and room to own outcomes.\""),
    ("Why is there a gap in your resume?", "Short, honest, and forward-looking. One or two sentences, then pivot to readiness.", "\"I took eight months for family caregiving. During that time I completed {course}, and I'm fully ready to return.\""),
    ("Tell me about a time you went above and beyond.", "Choose a story where the extra effort produced a business result, not just long hours.", "Show the initiative, the result, and who benefited."),
    ("How do you stay current in your field?", "Name 2 or 3 specific sources and one thing you applied recently.", "Mention a newsletter, community, or course and the change it led to in your work."),
    ("Is there anything else we should know?", "Restate fit in one sentence and express interest.", "\"Just that I'm genuinely excited about this. The role matches exactly what I've been building toward.\""),
]
