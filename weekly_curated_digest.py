"""
Weekly Curated AI Digest — Tier 2 automation
Sources: The Batch (DeepLearning.AI), The Rundown AI, One Useful Thing (Ethan Mollick),
MarkTechPost — plus a direct re-check of primary lab blogs (OpenAI, DeepMind, Anthropic,
Thinking Machines, Perplexity, NVIDIA) in case anything was missed during the week.

Intent: this is the curated filtering layer described in the Tier 2 research workflow —
run weekly (not daily), producing a smaller, higher-signal digest than Tier 1's raw firehose.

Run manually:  python weekly_curated_digest.py
Run via GitHub Actions: see .github/workflows/weekly-curated-digest.yml

Notes on sources NOT automated:
- Import AI (importai.substack.com): Substack/Cloudflare blocks GitHub Actions' datacenter IPs
  at the network level regardless of User-Agent (confirmed via testing both a custom bot UA and
  a standard browser UA — both 403). Check https://jack-clark.net/ manually instead.
- One Useful Thing is ALSO on Substack, so it carries the same risk. It's included below so the
  per-feed logging can tell us definitively whether Substack blocks vary by publication; if it
  403s the same way, move it to MANUAL_CHECK_REMINDERS.
- The Academic Digest (theacademicdigest.app): a personalized, subscription-based email service
  (you enter keywords, it emails *you* specifically). There is no generic public feed to poll —
  nothing exists to automate. Subscribe directly via email if you want it.
"""

import os
import csv
import time
import requests
import feedparser
from datetime import datetime, timezone

CURATED_NEWSLETTER_FEEDS = {
    "The Batch (DeepLearning.AI)": "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_the_batch.xml",
    "The Rundown AI": "https://rss.beehiiv.com/feeds/2R3C6Bt5wj.xml",
    "One Useful Thing (Ethan Mollick)": "https://www.oneusefulthing.org/feed",
    "MarkTechPost": "https://www.marktechpost.com/feed/",
}

MANUAL_CHECK_REMINDERS = {
    "Import AI (Jack Clark)": "https://jack-clark.net/",
    "The Academic Digest": "https://www.theacademicdigest.app/ (personalized email service, no public feed — subscribe directly if wanted)",
}

# Same primary lab blogs as Tier 1 — re-checked weekly per the original Tier 2 spec
LAB_BLOG_FEEDS = {
    "OpenAI": "https://openai.com/news/rss.xml",
    "DeepMind": "https://deepmind.com/blog/feed/basic",
    "Anthropic (unofficial mirror)": "https://rsshub.bestblogs.dev/anthropic/news",
    "Thinking Machines Lab": "https://thinkingmachines.ai/index.xml",
    "Perplexity (Discover Daily podcast)": "https://feeds.buzzsprout.com/2302487.rss",
    "NVIDIA Blog": "https://blogs.nvidia.com/feed/",
    "NVIDIA Technical Blog": "https://developer.nvidia.com/blog/feed/",
}

SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")
LOG_FILE = os.path.join("logs", "weekly_run_log.csv")
LOG_FIELDS = ["timestamp_utc", "source", "status", "item_count", "error"]
ARCHIVE_DIR = os.path.join("weekly_digests")

REQUEST_HEADERS = {
    "User-Agent": "ai-research-aggregator/1.0 (personal research digest bot; contact: github.com/GauravAtavale)"
}


def fetch_single_feed(name, url, limit, source_prefix, timeout=25):
    """Fetch one feed and return (items, status, error) for that feed alone."""
    items = []
    status, error = "ok", ""
    try:
        resp = requests.get(url, headers=REQUEST_HEADERS, timeout=timeout)
        resp.raise_for_status()
        feed = feedparser.parse(resp.content)
        entries = feed.entries[:limit]
        for entry in entries:
            items.append({
                "title": entry.title,
                "link": entry.link,
                "summary": getattr(entry, "summary", "")[:350],
                "source": f"{source_prefix}{name}",
            })
        if not items:
            status = "empty"
            bozo_reason = getattr(feed, "bozo_exception", None)
            error = f"0 entries parsed (bozo={feed.bozo}, reason={bozo_reason})"
    except Exception as e:
        status, error = "failed", str(e)
    return items, status, error


def fetch_feed_group(feed_dict, log_rows, timestamp, limit_per_feed=8, source_prefix=""):
    all_items = []
    for name, url in feed_dict.items():
        items, status, error = fetch_single_feed(name, url, limit_per_feed, source_prefix)
        all_items.extend(items)
        log_rows.append({"timestamp_utc": timestamp, "source": f"{source_prefix}{name}",
                          "status": status, "item_count": len(items), "error": error})
        time.sleep(1)
    return all_items


def dedupe(items):
    seen = set()
    out = []
    for it in items:
        key = it["title"].strip().lower()
        if key not in seen:
            seen.add(key)
            out.append(it)
    return out


def build_digest(items):
    today = datetime.now().strftime("%Y-%m-%d")
    lines = [f"# Weekly Curated AI Digest — week of {today}\n"]
    lines.append("_Tier 2: curated newsletters + direct lab blog re-check."
                 " Use this to catch anything Tier 1's daily firehose surfaced without enough context,"
                 " or that a curator flagged as genuinely important this week._\n")
    by_source = {}
    for it in items:
        by_source.setdefault(it["source"], []).append(it)
    for source, entries in by_source.items():
        lines.append(f"## {source}")
        for e in entries:
            lines.append(f"- **[{e['title']}]({e['link']})**  \n  {e['summary']}")
        lines.append("")
    if MANUAL_CHECK_REMINDERS:
        lines.append("## ⚠️ Manual Check Needed (not automatable)")
        for name, note in MANUAL_CHECK_REMINDERS.items():
            lines.append(f"- **{name}** — {note}")
        lines.append("")
    return "\n".join(lines)


def post_to_slack(markdown_text):
    if not SLACK_WEBHOOK_URL:
        return
    requests.post(SLACK_WEBHOOK_URL, json={"text": markdown_text[:3900]})


def log_run(rows):
    os.makedirs("logs", exist_ok=True)
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=LOG_FIELDS)
        if not file_exists:
            writer.writeheader()
        for row in rows:
            writer.writerow(row)


def archive_digest(digest_text):
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    with open(os.path.join(ARCHIVE_DIR, f"{today}.md"), "w") as f:
        f.write(digest_text)


def main():
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    log_rows = []

    newsletter_items = fetch_feed_group(
        CURATED_NEWSLETTER_FEEDS, log_rows, timestamp, limit_per_feed=8, source_prefix="Newsletter: ")
    lab_items = fetch_feed_group(
        LAB_BLOG_FEEDS, log_rows, timestamp, limit_per_feed=5, source_prefix="Lab Blog: ")

    log_run(log_rows)

    items = dedupe(newsletter_items + lab_items)
    digest = build_digest(items)

    with open("weekly_curated_digest_latest.md", "w") as f:
        f.write(digest)
    archive_digest(digest)

    post_to_slack(digest)
    print(digest)


if __name__ == "__main__":
    main()
