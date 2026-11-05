#!/usr/bin/env python3
"""Creates (or updates) The Job Search Kit on Gumroad through the v2 API.

Reads the token from the GUMROAD_ACCESS_TOKEN environment variable (needs the
edit_products scope). Safe to re-run: if a product with the same permalink
exists, it is updated instead of duplicated.

  python3 scripts/gumroad_publish.py --check     # verify the token only
  python3 scripts/gumroad_publish.py             # upload, create/update, publish
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.gumroad.com/v2"
HERE = Path(__file__).resolve().parent.parent
ZIP = HERE / "dist" / "The-Job-Search-Kit.zip"
COVER_URL = "https://nishu1996builds.github.io/tailorscan/assets/kit-cover.png"
PERMALINK = "job-search-kit"
NAME = "The Job Search Kit: ATS Resume Templates, Tailoring Playbook, Tracker, and Scripts"
PRICE_CENTS = 2900
SUMMARY = "3 ATS-safe resume templates, a 15-minute tailoring playbook, a job tracker with auto follow-ups, outreach scripts, and 25 screening answer frameworks."
TAGS = ["resume", "resume template", "ats", "job search", "career", "cover letter", "job tracker", "interview"]
DESCRIPTION = """<p>Sending applications and hearing nothing back? Usually it's not your experience. It's that your resume doesn't speak the posting's language, and there's no system behind your search.</p>
<h3>What's inside</h3>
<ul>
<li><strong>3 ATS-safe resume templates</strong> (Classic, Modern, Senior). Single-column Word files that parse cleanly in Workday, Greenhouse, Lever, and iCIMS, with guidance built into each section.</li>
<li><strong>The Tailoring Playbook (PDF).</strong> A 15-minute routine to tailor any resume to any job, the bullet formula recruiters respond to, before-and-after rewrites, 160 action verbs, and a printable checklist.</li>
<li><strong>Job Application Tracker</strong> (Excel and Google Sheets). Calculates follow-up dates, flags overdue follow-ups, and charts your funnel and best sources automatically.</li>
<li><strong>9 outreach and follow-up scripts:</strong> referral asks, recruiter and hiring manager messages, follow-ups, thank-yous, and salary negotiation.</li>
<li><strong>25 screening question frameworks</strong>, with a structure and an example for each.</li>
<li><strong>Cover letter template</strong> with 3 opening styles.</li>
</ul>
<p>Before you send each application, check your resume against the posting with the free <a href="https://nishu1996builds.github.io/tailorscan/">TailorScan</a> scanner.</p>
<p>One-time purchase. Instant download. 30-day no-questions refund.</p>"""


def token():
    t = os.environ.get("GUMROAD_ACCESS_TOKEN", "").strip()
    if not t:
        sys.exit("GUMROAD_ACCESS_TOKEN is not set. Add it as an environment secret and start a new session.")
    return t


def call(method, path, fields=None):
    """Form-encoded request. fields is a list of (key, value) pairs so array keys like tags[] can repeat."""
    pairs = [("access_token", token())] + list(fields or [])
    data = urllib.parse.urlencode(pairs).encode()
    url = API + path
    if method == "GET":
        url, data = url + "?" + data.decode(), None
    req = urllib.request.Request(url, data=data, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            body = json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        sys.exit(f"{method} {path} failed: HTTP {e.code}: {body[:500]}")
    if not body.get("success", True):
        sys.exit(f"{method} {path} failed: {json.dumps(body)[:500]}")
    return body


def upload_zip():
    size = ZIP.stat().st_size
    pre = call("POST", "/files/presign", [("filename", ZIP.name), ("file_size", str(size))])
    parts, etags = pre["parts"], []
    blob = ZIP.read_bytes()
    chunk = -(-size // len(parts))  # ceil division; presign decides the part count
    for i, part in enumerate(parts):
        piece = blob[i * chunk:(i + 1) * chunk]
        req = urllib.request.Request(part["presigned_url"], data=piece, method="PUT")
        with urllib.request.urlopen(req, timeout=300) as r:
            etags.append((part["part_number"], r.headers["ETag"]))
    fields = [("upload_id", pre["upload_id"]), ("key", pre["key"])]
    for n, et in etags:
        fields += [("parts[][part_number]", str(n)), ("parts[][etag]", et)]
    done = call("POST", "/files/complete", fields)
    return done["file_url"]


def main():
    me = call("GET", "/user")["user"]
    print("Token OK for Gumroad user:", me.get("name") or me.get("email") or me.get("user_id"))
    if "--check" in sys.argv:
        return
    if not ZIP.exists():
        sys.exit(f"Missing {ZIP}. Run build_kit.py first.")

    existing = next((p for p in call("GET", "/products")["products"]
                     if p.get("custom_permalink") == PERMALINK or PERMALINK in (p.get("short_url") or "")), None)

    policy = call("GET", "/refund_policy").get("refund_policy", {})
    account_policy = bool(policy.get("in_effect"))
    if account_policy and policy.get("refund_period") != "30":
        call("PUT", "/refund_policy", [("refund_period", "30"), ("fine_print", "Email within 30 days for a full refund. No forms, no questions.")])
        print("Account refund policy set to 30 days.")

    print(f"Uploading {ZIP.name} ({ZIP.stat().st_size // 1024} KB)...")
    file_url = upload_zip()

    fields = [("name", NAME), ("description", DESCRIPTION), ("price", str(PRICE_CENTS)),
              ("custom_permalink", PERMALINK), ("custom_summary", SUMMARY), ("files[][url]", file_url)]
    fields += [("tags[]", t) for t in TAGS]
    if not account_policy:
        fields += [("refund_period", "30"), ("refund_fine_print", "Email within 30 days for a full refund. No forms, no questions.")]

    if existing:
        pid = existing["id"]
        product = call("PUT", f"/products/{pid}", fields)
        print("Updated existing product", pid)
    else:
        product = call("POST", "/products", [("native_type", "digital"), ("price_currency_type", "usd")] + fields)
        pid = product["product"]["id"]
        print("Created product", pid)
    if product.get("warning"):
        print("Gumroad warning:", product["warning"])

    p = call("GET", f"/products/{pid}")["product"]
    if not p.get("covers"):
        call("POST", f"/products/{pid}/covers", [("url", COVER_URL)])
        print("Cover attached.")
    if not p.get("published"):
        try:
            call("PUT", f"/products/{pid}/enable")
            print("Published.")
        except SystemExit as e:
            print("Could not publish yet (", e, "). Usually this means the Gumroad email is unconfirmed or no payout method is set.")
    p = call("GET", f"/products/{pid}")["product"]
    print(json.dumps({"id": pid, "short_url": p.get("short_url"), "published": p.get("published"),
                      "price": p.get("price"), "files": len(p.get("files") or []), "covers": len(p.get("covers") or [])}, indent=2))


if __name__ == "__main__":
    main()
