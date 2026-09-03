"""
Daily AI Research Digest — Tier 1 "Firehose" automation
Fetches: Hugging Face Trending/Daily Papers, alphaXiv trending papers.
Outputs a single markdown digest, optionally posts to Slack.

Run manually:  python daily_digest.py
Run via cron:  0 7 * * * /usr/bin/python3 /path/to/daily_digest.py
Run via GitHub Actions: see .github/workflows/daily-digest.yml
"""

import requests
import feedparser
from datetime import datetime

HF_RSS_FEED = "https://papers.takara.ai/api/feed"   # community-maintained HF Daily Papers RSS
ALPHAXIV_API = "https://api.alphaxiv.org/v2/papers/trending"  # check docs for exact params
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")  # optional


def fetch_hf_daily_papers(limit=10):
    items = []
    try:
        feed = feedparser.parse(HF_RSS_FEED)
        for entry in feed.entries[:limit]:
            items.append({
                "title": entry.title,
                "link": entry.link,
                "summary": getattr(entry, "summary", "")[:300],
                "source": "HF Daily Papers",
            })
    except Exception as e:
        items.append({"title": f"[HF fetch failed: {e}]", "link": "", "summary": "", "source": "HF"})
    return items


def fetch_alphaxiv_trending(limit=10):
    items = []
    try:
        resp = requests.get(ALPHAXIV_API, params={"limit": limit}, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        for p in data.get("papers", data.get("data", []))[:limit]:
            items.append({
                "title": p.get("title", "Untitled"),
                "link": p.get("url", p.get("link", "")),
                "summary": (p.get("abstract") or "")[:300],
                "source": "alphaXiv Trending",
            })
    except Exception as e:
        items.append({"title": f"[alphaXiv fetch failed: {e}]", "link": "", "summary": "", "source": "alphaXiv"})
    return items


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


def main():
    items = fetch_hf_daily_papers() + fetch_alphaxiv_trending()
    items = dedupe(items)
    digest = build_digest(items)

    with open("digest_latest.md", "w") as f:
        f.write(digest)

    post_to_slack(digest)
    print(digest)


if __name__ == "__main__":
    main()
