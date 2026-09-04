"""
Daily AI Research Digest — Tier 1 "Firehose" automation
Fetches: Hugging Face Trending/Daily Papers, arXiv recent cs.AI/cs.LG submissions.
Outputs a single markdown digest, optionally posts to Slack, and logs every run.

Run manually:  python daily_digest.py
Run via cron:  0 7 * * * /usr/bin/python3 /path/to/daily_digest.py
Run via GitHub Actions: see .github/workflows/daily-digest.yml
"""

import os
import csv
import time
import requests
import feedparser
from datetime import datetime, timezone

HF_RSS_FEED = "https://papers.takara.ai/api/feed"   # community-maintained HF Daily Papers RSS
ARXIV_API = "http://export.arxiv.org/api/query"      # official, no auth required
ARXIV_QUERY = "cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL"
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")  # optional
LOG_FILE = os.path.join("logs", "run_log.csv")
LOG_FIELDS = ["timestamp_utc", "source", "status", "item_count", "error"]

REQUEST_HEADERS = {
    "User-Agent": "ai-research-aggregator/1.0 (personal research digest bot; contact: github.com/GauravAtavale)"
}


def fetch_hf_daily_papers(limit=10):
    items = []
    status, error = "ok", ""
    try:
        feed = feedparser.parse(HF_RSS_FEED, request_headers=REQUEST_HEADERS)
        for entry in feed.entries[:limit]:
            items.append({
                "title": entry.title,
                "link": entry.link,
                "summary": getattr(entry, "summary", "")[:300],
                "source": "HF Daily Papers",
            })
        if not items:
            status = "empty"
    except Exception as e:
        status, error = "failed", str(e)
        items.append({"title": f"[HF fetch failed: {e}]", "link": "", "summary": "", "source": "HF"})
    return items, status, error


def fetch_arxiv_recent(limit=10, max_retries=3):
    items = []
    params = {
        "search_query": ARXIV_QUERY,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": limit,
    }
    last_error = None
    for attempt in range(max_retries):
        try:
            resp = requests.get(ARXIV_API, params=params, headers=REQUEST_HEADERS, timeout=20)
            if resp.status_code == 429:
                wait = 5 * (attempt + 1)
                time.sleep(wait)
                continue
            resp.raise_for_status()
            feed = feedparser.parse(resp.text)
            for entry in feed.entries[:limit]:
                items.append({
                    "title": entry.title.replace("\n", " ").strip(),
                    "link": entry.link,
                    "summary": getattr(entry, "summary", "")[:300].replace("\n", " "),
                    "source": "arXiv (cs.AI/cs.LG/cs.CL, recent)",
                })
            status = "ok" if items else "empty"
            return items, status, ""
        except Exception as e:
            last_error = e
            time.sleep(3)
    items.append({"title": f"[arXiv fetch failed after {max_retries} attempts: {last_error}]", "link": "", "summary": "", "source": "arXiv"})
    return items, "failed", str(last_error)


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
    lines = [f"# AI Research Digest — {today}\n"]
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


def main():
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    hf_items, hf_status, hf_error = fetch_hf_daily_papers()
    time.sleep(3)
    arxiv_items, arxiv_status, arxiv_error = fetch_arxiv_recent()

    log_rows = [
        {"timestamp_utc": timestamp, "source": "HF Daily Papers", "status": hf_status,
         "item_count": len(hf_items), "error": hf_error},
        {"timestamp_utc": timestamp, "source": "arXiv", "status": arxiv_status,
         "item_count": len(arxiv_items), "error": arxiv_error},
    ]
    log_run(log_rows)

    items = dedupe(hf_items + arxiv_items)
    digest = build_digest(items)

    with open("digest_latest.md", "w") as f:
        f.write(digest)

    post_to_slack(digest)
    print(digest)


if __name__ == "__main__":
    main()
