# TailorScan Kit

The paid half of the TailorScan product line: The Job Search Kit ($29 on Gumroad), its brand assets, the Gumroad publish script, and the lead-generation plan that sells it. The free scanner site lives in the public repo `nishu1996builds/tailorscan`. This repo stays private because it holds the buyer download, outreach contact lists and drafted emails.

## Layout

| Path | What it is |
| --- | --- |
| `LAUNCH.md` | Business plan, unit economics, go-live checklist and listing copy. |
| `build_kit.py`, `content.py`, `build_checklist.py` | Build the kit PDFs and the free checklist from source content. |
| `dist/The-Job-Search-Kit.zip` | What buyers download. Rebuild with `python3 build_kit.py`. |
| `listing/` | Gumroad cover images and their HTML sources. |
| `brand/` | Logo, avatar, cover and wordmark for every channel, plus the render script. |
| `scripts/gumroad_publish.py` | Creates or updates the Gumroad product through the API. Needs `GUMROAD_ACCESS_TOKEN`. |
| `marketing/FIRST_100_CUSTOMERS.md` | The plan: personal outreach first, launch later. Read this before anything else in `marketing/`. |
| `marketing/DISTRIBUTION.md` | Channel plan with priorities, tracking links and brand identity rules. |
| `marketing/outreach-tracker.csv` | Every outreach target with its tracking link, send date and status. Update it as emails go out. |
| `marketing/outbox/` | Drafted, researched emails ready to send, one JSON batch per wave. |
| `marketing/pinterest-bulk-upload.csv`, `marketing/ads/` | Pinterest pins and Meta ad creatives. Ads are on hold until about 25 organic sales. |

## Working rhythm

1. Send the next batch from `marketing/outbox/`, then mark each row in `outreach-tracker.csv` as sent with the date.
2. Follow up seven days later. Log replies and listings in the tracker.
3. Check Gumroad for free downloads and sales by tracking link to see which segment converts.
4. Ship kit updates by rebuilding `dist/`, re-running the publish script, and tagging the release.

## History

Extracted from the `tailorscan-kit` folder of `nishu1996builds/ResumeBuildngRepo` (branch `claude/beautiful-curie-5hoj5p`) with commit history preserved. The `tailorscan/` site mirror on that branch was identical to the public repo and was not carried over.
