# TailorScan distribution plan (no personal accounts)

> **Read FIRST_100_CUSTOMERS.md first.** Personal outreach is the main engine for the first 100 sales. The channels below support it.

Everything here runs under a **TailorScan brand identity**, never your name. Each channel has its own tracking link, so every free download and sale in Gumroad shows where it came from. Claude can pull that breakdown any time you ask it to "check on it".

## Priority order

| # | Channel | Your time | Cost | Expected impact | Why |
| --- | --- | --- | --- | --- | --- |
| 1 | Pinterest | 20 min once | $0 | Slow build, then steady for months | Resume content performs very well there, it needs no face, and 40 pins are ready to bulk-upload |
| 2 | Hacker News (Show HN) | 10 min + replies | $0 | One-day spike, possibly thousands of visits | The privacy and open-source angle is what HN rewards |
| 3 | AlternativeTo listings | 15 min | $0 | Small but high-intent and permanent | People searching "Jobscan alternative" land there |
| 4 | Product Hunt | 20 min | $0 | One-day spike | **Postponed until customer #100**, as a celebration (see FIRST_100_CUSTOMERS.md) |
| 5 | Reddit (brand account) | 15 min a day for 2 weeks | $0 | Medium, steady | Job seekers ask "why no callbacks?" all day |
| 6 | Meta ads (test) | 30 min setup | $70 cap | Measured test only | **On hold until about 25 organic sales**, so the ads can use lookalike audiences of real buyers |

## Step 0: brand identity

- **Email:** `tailorscan.help@gmail.com` (already on the site's privacy page).
- **Profile image, everywhere:** `../brand/avatar-800.png`.
- **Product Hunt thumbnail:** `../brand/producthunt-240.png`.
- **Facebook Page, Pinterest, or Reddit banner:** `../brand/cover-1640x624.png`.
- **Wordmark, for anything else:** `../brand/wordmark-1200x360.png`. The source vector is `../brand/mark.svg`.
- **Optional domain (recommended):** buy `tailorscan.app` (about $14 a year) at Cloudflare Registrar or Namecheap, then tell Claude. It will set `custom_domain`, and you add the 4 GitHub Pages A records it gives you. Do this **before** uploading the Pinterest CSV if you can, so the pins point at the permanent address and you can claim the domain in Pinterest.

---

## 1. Pinterest (do this first; it compounds)

1. Create a free **Pinterest Business** account with the brand Gmail. Name it **TailorScan: Resume Tips**.
2. Create a board named exactly **Resume Keywords by Job Title**.
3. Go to **Create > Create Pin > Bulk create Pins** (in some accounts this is under **Settings > Bulk create Pins**). Upload `pinterest-bulk-upload.csv` from this folder.
4. The file schedules 2 pins a day for 20 days, starting Nov 6. Every image is already live on the site.

Tracking link used: `?utm_source=pinterest&utm_medium=social&utm_campaign=<role>`

---

## 2. Show HN (Hacker News)

Create an account at news.ycombinator.com with a brand-neutral username. Post on a **Tuesday to Thursday, 8 to 10 am US Eastern**.

**Title:**
```
Show HN: A resume vs. job description keyword scanner that runs entirely in the browser
```

**URL:**
```
https://nishu1996builds.github.io/tailorscan/?utm_source=hackernews&utm_medium=community&utm_campaign=showhn
```

**First comment (post it right after submitting):**
```
Most resume scanners are monthly subscriptions for something people need for a few weeks, so I built a free one.

You paste a resume and a job posting, and it scores the match, lists missing skills ranked by whether the posting puts them under required or preferred, and flags things like unquantified bullets and table layouts that ATS parsers scramble.

Everything runs client-side. PDF and DOCX parsing use pdf.js and mammoth in the browser, and there is no backend at all, so your resume never leaves the page. The scoring engine is about 450 lines of plain JS with a 240-skill taxonomy. Ambiguous names like Go, R, and Excel only match case-sensitively, so "go-to-market" isn't read as the Go language. It also weights requirements sections above company boilerplate, and ignores EEO and benefits text.

Source: https://github.com/nishu1996builds/tailorscan

I'd love feedback on false positives and negatives in the matching. That's the hard part.
```

Reply to every comment in the first 3 hours. If people report bad matches, paste them to Claude and it will fix the engine the same day.

---

## 3. AlternativeTo listings

At alternativeto.net, sign up with the brand Gmail, click **Add application**, and list TailorScan as an alternative to **Jobscan**, **Resume Worded**, and **Teal**.

- **Name:** TailorScan
- **URL:** `https://nishu1996builds.github.io/tailorscan/?utm_source=alternativeto&utm_medium=directory`
- **License:** Free, Open Source
- **Platforms:** Online
- **Tags:** resume, ats, job search, privacy, keyword
- **Description:**
```
Free resume vs. job description scanner. Paste your resume and a posting to get a match score, missing keywords ranked by required vs. preferred, and nine ATS best-practice checks. Runs entirely in your browser: no account, no upload, unlimited scans.
```

---

## 4. Product Hunt

Use a maker account with the brand Gmail, and launch at **12:01 am Pacific** on a Tuesday or Wednesday.

- **Name:** TailorScan
- **Tagline (60 characters max):** `Free, private resume vs. job description keyword scanner`
- **Link:** `https://nishu1996builds.github.io/tailorscan/?utm_source=producthunt&utm_medium=launch`
- **Topics:** Productivity, Hiring, Privacy
- **Images:** the 3 files in `ads/` plus a screenshot of a scan result
- **Maker comment:**
```
Hi Product Hunt! TailorScan compares your resume to a job posting and shows exactly which keywords you are missing, ranked by whether the posting lists them as required or preferred. It also checks the things that get resumes filtered out: no numbers in bullets, "responsible for" phrasing, and table layouts.

It is free and unlimited, and it runs entirely in your browser. There is no sign-up, and your resume never touches a server.

I'd love to hear where the matching gets it wrong for your field.
```

---

## 5. Reddit (brand account, value first)

Reddit bans accounts that show up only to drop links, so follow these rules:

1. Create a brand account (for example `u/TailorScanHelp`) and spend 3 to 4 days writing helpful comments **with no link** in r/resumes, r/jobs, r/jobsearchhacks, and r/careerguidance.
2. After about 10 helpful comments, include the link **only** where someone asks why they get no callbacks or how to tailor a resume. Keep it to 1 link per 5 comments at most.
3. **Never link the paid kit.** Only link the free scanner. The site does the selling.
4. Read each subreddit's rules first. Some ban tool links entirely.

**Comment template:**
```
Most of the time it's not your experience, it's the wording. Recruiters search the ATS by keyword, so if the posting says "stakeholder management" and your resume says "worked with partners," you never show up in the search. Quick fix for each application: pull the must-have skills from the Requirements section, and make sure each one you really have appears in your Skills section AND in one bullet with a number. There's a free browser-only scanner that does the comparison for you if it helps: https://nishu1996builds.github.io/tailorscan/?utm_source=reddit&utm_medium=community (no sign-up, nothing uploaded).
```

---

## 6. Meta (Facebook and Instagram) ads: capped test

### The economics first

| | |
| --- | --- |
| Net per kit sale | about $17 at the $19 launch price, $25.60 at $29 |
| Typical cost per click for job-seeker audiences | about $0.50 to $1.50 |
| Cold visitor to purchase | about 0.5% to 1% |
| **Implied ad spend per sale** | **$50 to $300** |

Ads that push straight to the paid kit will most likely **lose money**. The test is only worth running if ads send people to the **free scanner**, where they can grab the free checklist (that captures an email you can sell to later), and if spending is capped hard.

### Setup

1. Create a **Facebook Page** named TailorScan. A Page shows only the brand name, never your personal profile.
2. In **Meta Ads Manager**, create a campaign with the **Traffic** objective and **Landing page views** as the optimization goal.
3. **Budget:** $10 a day for 7 days, a **$70 lifetime cap**. Set the cap at the campaign level so it cannot overspend.
4. **Audience:** United States, ages 22 to 45. Interests: Job hunting, Indeed, Glassdoor, LinkedIn, Résumé, Career development. Placements: Advantage+.
5. **Creatives:** the three images in `ads/` (ad-score, ad-private, ad-silence), one ad each.
6. **Destination URL:**
   `https://nishu1996builds.github.io/tailorscan/?utm_source=meta&utm_medium=paid&utm_campaign=test1&utm_content={{ad.name}}`

**Primary text (use one per ad):**
```
Applying everywhere and hearing nothing back? Your resume might not use the posting's exact words, so it never shows up when recruiters search. Paste your resume and the job description to see exactly which keywords are missing. Free, no sign-up, and your resume never leaves your browser.
```
```
Most resume scanners charge a monthly subscription. This one is free and unlimited, and it runs entirely in your browser, with nothing uploaded. See your match score and the missing keywords in 30 seconds.
```
```
A 47/100 match score means a recruiter search probably skips you. Find out which skills from the job posting are missing from your resume, ranked by priority. Free.
```

- **Headline:** `See what your resume is missing`
- **Call to action:** Learn More

### Stop rules (decide these now, not mid-test)

- **After $20 per ad:** pause any ad with cost per click above $1.20.
- **At $70 total:** stop the whole test unless it produced at least 1 sale or 15 free checklist downloads.
- **If it passes:** keep the winning ad at $10 a day and re-check weekly. Kill it if cost per sale goes above $17.

Claude can read the results from Gumroad, filtered by `utm_source=meta`, whenever you ask.

---

## Weekly rhythm

- **Monday:** ask Claude to "check on it". It pulls views, downloads, sales, and which channels they came from.
- **Whatever is working:** double it. Whatever isn't after two weeks: drop it.
- **New role pages and pins:** Claude can add 10 a week. After adding roles, run `node render.js` in this folder to make their pins and add them to the CSV.
