"""
Daily AI Research Digest — Tier 1 "Firehose" automation
Sources: HF Daily Papers, arXiv (cs.AI/cs.LG/cs.CL), Hacker News, Reddit r/MachineLearning,
lab blogs (OpenAI, DeepMind, Anthropic), GitHub Trending (AI repos via Search API).
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
from datetime import datetime, timezone, timedelta

HF_RSS_FEED = "https://papers.takara.ai/api/feed"
ARXIV_API = "http://export.arxiv.org/api/query"
ARXIV_QUERY = "cat:cs.AI OR cat:cs.LG OR cat:cs.CL"
HN_API = "https://hn.algolia.com/api/v1/search_by_date"
REDDIT_URL = "https://www.reddit.com/r/MachineLearning/top.json"
GITHUB_SEARCH_API = "https://api.github.com/search/repositories"

LAB_BLOG_FEEDS = {
    "OpenAI": "https://openai.com/news/rss.xml",
    "DeepMind": "https://deepmind.com/blog/feed/basic",
    "Anthropic (unofficial mirror)": "https://rsshub.bestblogs.dev/anthropic/news",
}

SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")
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
            items.append({"title": entry.title, "link": entry.link,
                          "summary": getattr(entry, "summary", "")[:300], "source": "HF Daily Papers"})
        if not items:
            status = "empty"
    except Exception as e:
        status, error = "failed", str(e)
        items.append({"title": f"[HF fetch failed: {e}]", "link": "", "summary": "", "source": "HF"})
    return items, status, error


def fetch_arxiv_recent(limit=10, max_retries=3):
    items = []
    params = {"search_query": ARXIV_QUERY, "sortBy": "submittedDate", "sortOrder": "descending", "max_results": limit}
    last_error = None
    for attempt in range(max_retries):
        try:
            resp = requests.get(ARXIV_API, params=params, headers=REQUEST_HEADERS, timeout=20)
            if resp.status_code == 429:
                time.sleep(5 * (attempt + 1))
                continue
            resp.raise_for_status()
            feed = feedparser.parse(resp.text)
            for entry in feed.entries[:limit]:
                items.append({"title": entry.title.replace("\n", " ").strip(), "link": entry.link,
                              "summary": getattr(entry, "summary", "")[:300].replace("\n", " "),
                              "source": "arXiv (cs.AI/cs.LG/cs.CL, recent)"})
            if items:
                return items, "ok", ""
            last_error = f"query returned 0 results (raw response length {len(resp.text)})"
            break
        except Exception as e:
            last_error = e
            time.sleep(3)
    items.append({"title": f"[arXiv fetch returned no results: {last_error}]", "link": "", "summary": "", "source": "arXiv"})
    return items, "failed", str(last_error)


def fetch_hackernews(limit=10, hours_back=24):
    items = []
    status, error = "ok", ""
    try:
        since_ts = int((datetime.now(timezone.utc) - timedelta(hours=hours_back)).timestamp())
        params = {"query": "AI OR LLM OR machine learning", "tags": "story",
                  "numericFilters": f"created_at_i>{since_ts}", "hitsPerPage": limit}
        resp = requests.get(HN_API, params=params, headers=REQUEST_HEADERS, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        for hit in data.get("hits", [])[:limit]:
            title = hit.get("title") or "Untitled"
            link = hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID')}"
            points = hit.get("points", 0)
            items.append({"title": title, "link": link,
                          "summary": f"{points} points, {hit.get('num_comments', 0)} comments",
                          "source": "Hacker News"})
        if not items:
            status = "empty"
    except Exception as e:
        status, error = "failed", str(e)
        items.append({"title": f"[HN fetch failed: {e}]", "link": "", "summary": "", "source": "Hacker News"})
    return items, status, error


def fetch_reddit(limit=10):
    items = []
    status, error = "ok", ""
    try:
        resp = requests.get(REDDIT_URL, params={"limit": limit, "t": "day"}, headers=REQUEST_HEADERS, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        for child in data.get("data", {}).get("children", [])[:limit]:
            post = child.get("data", {})
            title = post.get("title", "Untitled")
            link = "https://reddit.com" + post.get("permalink", "")
            items.append({"title": title, "link": link,
                          "summary": f"{post.get('score', 0)} upvotes, {post.get('num_comments', 0)} comments",
                          "source": "Reddit r/MachineLearning"})
        if not items:
            status = "empty"
    except Exception as e:
        status, error = "failed", str(e)
        items.append({"title": f"[Reddit fetch failed: {e}]", "link": "", "summary": "", "source": "Reddit"})
    return items, status, error


def fetch_lab_blogs(limit_per_blog=5):
    items = []
    status, error = "ok", ""
    any_success = False
    errors = []
    for name, url in LAB_BLOG_FEEDS.items():
        try:
            feed = feedparser.parse(url, request_headers=REQUEST_HEADERS)
            entries = feed.entries[:limit_per_blog]
            if entries:
                any_success = True
            for entry in entries:
                items.append({"title": entry.title, "link": entry.link,
                              "summary": getattr(entry, "summary", "")[:250],
                              "source": f"Lab Blog: {name}"})
        except Exception as e:
            errors.append(f"{name}: {e}")
        time.sleep(1)
    if not any_success:
        status = "failed" if errors else "empty"
        error = "; ".join(errors)
    elif errors:
        error = "partial failures: " + "; ".join(errors)
    return items, status, error


def fetch_github_trending(limit=10, days_back=7):
    items = []
    status, error = "ok", ""
    try:
        since_date = (datetime.now(timezone.utc) - timedelta(days=days_back)).strftime("%Y-%m-%d")
        query = f"topic:artificial-intelligence created:>{since_date}"
        params = {"q": query, "sort": "stars", "order": "desc", "per_page": limit}
        resp = requests.get(GITHUB_SEARCH_API, params=params, headers=REQUEST_HEADERS, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        for repo in data.get("items", [])[:limit]:
            items.append({"title": repo.get("full_name", "Untitled"), "link": repo.get("html_url", ""),
                          "summary": f"★ {repo.get('stargazers_count', 0)} — {(repo.get('description') or '')[:200]}",
                          "source": "GitHub Trending (AI, new repos)"})
        if not items:
            status = "empty"
    except Exception as e:
        status, error = "failed", str(e)
        items.append({"title": f"[GitHub fetch failed: {e}]", "link": "", "summary": "", "source": "GitHub Trending"})
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

    fetchers = [
        ("HF Daily Papers", fetch_hf_daily_papers),
        ("arXiv", fetch_arxiv_recent),
        ("Hacker News", fetch_hackernews),
        ("Reddit", fetch_reddit),
        ("Lab Blogs", fetch_lab_blogs),
        ("GitHub Trending", fetch_github_trending),
    ]

    all_items = []
    log_rows = []
    for name, fn in fetchers:
        result_items, status, error = fn()
        all_items.extend(result_items)
        log_rows.append({"timestamp_utc": timestamp, "source": name, "status": status,
                          "item_count": len(result_items), "error": error})
        time.sleep(3)

    log_run(log_rows)

    items = dedupe(all_items)
    digest = build_digest(items)

    with open("digest_latest.md", "w") as f:
        f.write(digest)

    post_to_slack(digest)
    print(digest)


if __name__ == "__main__":
    main()
