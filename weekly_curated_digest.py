"""
Weekly Curated AI Digest — Tier 2 automation
Sources: Import AI (Jack Clark), The Batch (DeepLearning.AI), The Rundown AI —
plus a direct re-check of primary lab blogs (OpenAI, DeepMind, Anthropic, Thinking Machines,
Perplexity, NVIDIA) in case anything was missed during the week.

Intent: this is the curated filtering layer described in the Tier 2 research workflow —
run weekly (not daily), producing a smaller, higher-signal digest than Tier 1's raw firehose.

Run manually:  python weekly_curated_digest.py
Run via GitHub Actions: see .github/workflows/weekly-curated-digest.yml
"""

import os
import csv
import time
import requests
import feedparser
from datetime import datetime, timezone

CURATED_NEWSLETTER_FEEDS = {
    "Import AI (Jack Clark)": "https://importai.substack.com/feed",
    "The Batch (DeepLearning.AI)": "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_the_batch.xml",
    "The Rundown AI": "https://rss.beehiiv.com/feeds/2R3C6Bt5wj.xml",
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


def fetch_feed_group(feed_dict, limit_per_feed=8, source_prefix=""):
    items = []
    any_success = False
    errors = []
    for name, url in feed_dict.items():
        try:
            feed = feedparser.parse(url, request_headers=REQUEST_HEADERS)
            entries = feed.entries[:limit_per_feed]
            if entries:
                any_success = True
            for entry in entries:
                items.append({
                    "title": entry.title,
                    "link": entry.link,
                    "summary": getattr(entry, "summary", "")[:350],
                    "source": f"{source_prefix}{name}",
                })
        except Exception as e:
            errors.append(f"{name}: {e}")
        time.sleep(1)
    status = "ok" if any_success and not errors else ("failed" if not any_success else "partial")
    error = "; ".join(errors)
    return items, status, error


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

    newsletter_items, nl_status, nl_error = fetch_feed_group(
        CURATED_NEWSLETTER_FEEDS, limit_per_feed=8, source_prefix="Newsletter: ")
    time.sleep(2)
    lab_items, lab_status, lab_error = fetch_feed_group(
        LAB_BLOG_FEEDS, limit_per_feed=5, source_prefix="Lab Blog: ")

    log_rows = [
        {"timestamp_utc": timestamp, "source": "Curated Newsletters", "status": nl_status,
         "item_count": len(newsletter_items), "error": nl_error},
        {"timestamp_utc": timestamp, "source": "Lab Blogs (weekly re-check)", "status": lab_status,
         "item_count": len(lab_items), "error": lab_error},
    ]
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
