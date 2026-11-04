# TailorScan: business plan and launch checklist

## The thesis (why this, why now)

- **The demand is real and constant.** Job seekers search "ATS resume checker", "resume keyword scanner", and "[role] resume keywords" every day, and in a tough hiring market they search more.
- **The incumbents charge subscriptions.** The best-known scanners sell monthly plans. People resent paying a subscription for a tool they need for a few weeks.
- **Our wedge is free, private, and instant.** No account, no upload, unlimited scans. That is easy to share in Reddit threads and LinkedIn posts, and it is hard for subscription competitors to match without cannibalizing their own revenue.
- **Our cost is $0.** The site is static on GitHub Pages, all compute runs in the visitor's browser, and there is no customer data to secure. Every sale is almost pure margin after payment fees.
- **The business model is free tool, then paid kit.** The scanner earns the traffic and the trust. The $29 one-time Job Search Kit monetizes the share of visitors who want a system, not just a score.
- **There is a hidden second payoff.** For someone targeting growth and lifecycle roles, a live product with a real funnel, SEO pages, and conversion data is a stronger portfolio piece than any resume bullet.

## Unit economics (be realistic)

| Metric | Conservative | Base | Good |
| --- | --- | --- | --- |
| Monthly scanner visitors | 1,000 | 5,000 | 20,000 |
| Visit to kit page view | 5% | 7% | 9% |
| Kit page to purchase | 3% | 5% | 7% |
| Sales per month | 1 to 2 | 17 to 18 | about 126 |
| Net revenue per sale (after roughly 10% plus per-sale payment fees; check Gumroad's current rates) | ~$25.60 | ~$25.60 | ~$25.60 |
| **Monthly net** | **~$40** | **~$450** | **~$3,200** |

Traffic is the whole game. SEO pages take 3 to 6 months to rank, so the first 90 days depend on launch posts and communities. Treat month one as validation, not income.

**Kill or pivot criteria (day 60):** if fewer than 1,000 visitors a month or no sales after 300 kit page views, test the price ($19), the offer (a "resume review checklist" lead magnet that collects emails), or the channel before building anything new.

## Go-live checklist (about 45 minutes, in order)

1. **Create the public repo.** On GitHub, create an empty public repo named `tailorscan` (no README). Then either ask Claude to push it (it can attach the repo with add_repo), or from this folder run `tailorscan/scripts/publish.sh https://github.com/nishu1996builds/tailorscan.git`.
2. **Turn on Pages.** Repo Settings > Pages > Source: **GitHub Actions**. The first deploy takes about 2 minutes. The site will be at `https://nishu1996builds.github.io/tailorscan/`.
3. **Create the Gumroad product.** Sign up at gumroad.com and create a "Digital product":
   - Name: The Job Search Kit
   - Price: $29
   - File: upload `tailorscan-kit/dist/The-Job-Search-Kit.zip`
   - Cover: `tailorscan-kit/listing/gumroad-cover-1280x720.png`
   - Description: paste from the listing copy below
   - Settings: turn on the 30-day refund policy
4. **Wire the buy button.** Put the Gumroad product URL into `tailorscan/data/site.json` as `kit_url`, and add a `support_email`. Commit and push, and the site redeploys.
5. **Add analytics (free, 5 minutes).** Create a GoatCounter account, put the code in `goatcounter_code`, and push. Scans, uploads, and buy clicks are already tracked as events.
6. **Submit to Google.** Add the site in Google Search Console and submit `sitemap.xml`. Do the same in Bing Webmaster Tools.
7. **Optional: buy a domain** (about $12 a year). Set `custom_domain`, add the DNS records GitHub shows, and push. A real domain ranks and converts better than a github.io URL.

## Launch week (distribution plan)

| Day | Channel | Action |
| --- | --- | --- |
| 1 | LinkedIn | Post the build story (draft below). Your network is job-search-heavy right now. |
| 2 | Reddit | r/resumes and r/jobs: answer 5 to 10 threads where people ask why they get no callbacks, then mention the tool where it helps. Read each subreddit's self-promotion rules first. |
| 3 | Reddit | r/careerguidance, r/cscareerquestions (engineering), r/marketing (marketing pages) |
| 4 | Product Hunt | Launch as a free tool. Free tools do well there. |
| 5 | Hacker News | "Show HN: A resume vs. job description scanner that runs entirely in your browser." The privacy angle is the hook. |
| Ongoing | SEO | Add 5 role pages a week to `data/roles.json` (it takes minutes each). Target "[role] resume keywords". |

### LinkedIn post draft

> I've sent a lot of job applications this year, and I built my own tooling to keep up. One of those tools was a script that compared my resume to each job description and told me exactly which keywords I was missing.
>
> It made a real difference, so I turned it into a free web tool: TailorScan.
>
> Paste your resume and a job posting, and it:
> - scores the match
> - lists missing skills ranked by "required" vs "nice to have"
> - flags the stuff that gets resumes filtered out (no metrics, "responsible for", columns and tables)
>
> It's free, there's no sign-up, and your resume never leaves your browser. There's no server at all.
>
> If you're job searching, or know someone who is, I'd love feedback: {link}

### Reddit comment template (use only where it answers the question)

> A common reason for no callbacks is that the resume doesn't use the posting's exact language, so it never shows up when recruiters search the ATS. Quick fix: for each application, pull the must-have skills from the Requirements section and make sure each one you really have appears in your Skills section and in one bullet with a result. I built a free browser-only tool that does the comparison for you, if that helps: {link}. No sign-up, and nothing gets uploaded.

## Gumroad listing copy

**Title:** The Job Search Kit: ATS Resume Templates, Tailoring Playbook, Tracker, and Scripts

**Summary:** Everything you need to tailor every application in 15 minutes and actually follow up.

**Description:**

> Sending applications and hearing nothing back? Usually it's not your experience. It's that your resume doesn't speak the posting's language, and there's no system behind your search.
>
> **What's inside**
> - **3 ATS-safe resume templates** (Classic, Modern, Senior). Single-column Word files that parse cleanly in Workday, Greenhouse, Lever, and iCIMS, with guidance built into each section.
> - **The Tailoring Playbook (PDF).** A 15-minute routine to tailor any resume to any job, the bullet formula recruiters respond to, before-and-after rewrites, 160 action verbs, and a printable checklist.
> - **Job Application Tracker (Excel and Google Sheets).** Calculates follow-up dates, flags overdue follow-ups, and charts your funnel and best sources automatically.
> - **9 outreach and follow-up scripts.** Referral asks, recruiter and hiring manager messages, follow-ups, thank-yous, and salary negotiation.
> - **25 screening question frameworks** with a structure and an example for each.
> - **Cover letter template** with 3 opening styles.
>
> One-time purchase. Instant download. 30-day no-questions refund.

**Tags:** resume, resume template, ATS, job search, career, cover letter, job tracker, interview

## Pricing and growth levers to test later

1. **Launch discount.** Create a Gumroad offer code `LAUNCH` at $19 for the first two weeks, and mention it in launch posts.
2. **Bundle tier ($49).** Add 10 role-specific resume examples. Built from `tailorscan/data/roles.json`, it is a few hours of work.
3. **Email capture.** Add a "send me the 15-minute checklist" form, using Gumroad's free $0 product or ConvertKit's free tier. Email converts far better than a cold visit.
4. **Affiliate income.** Gumroad supports affiliates, so career coaches and newsletter writers can sell the kit for a 30 to 40% cut.

## Rebuild the kit

```bash
cd tailorscan-kit && python3 build_kit.py
```

Content lives in `content.py`; the file builders are in `build_kit.py`.
