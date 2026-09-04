# AI Research Aggregator

A fully automated, two-tier pipeline that surfaces the most relevant AI research and industry news
every day and every week, without manual browsing. Built to keep pace with the AI field's daily
output volume while preserving a weekly, human-curated layer for signal over noise.

## Why This Exists

AI research and news move faster than any single person can track by hand. This project automates
both ends of that problem:

- **Breadth, daily**: a wide net across primary research feeds, community discussion, and lab
  announcements, refreshed automatically.
- **Signal, weekly**: a smaller, curated set of trusted newsletters and lab blogs, reviewed on a
  slower cadence to catch what the daily firehose surfaces but doesn't rank by importance.

## Architecture

### Tier 1 — Daily Firehose (`daily_digest.py`)

Runs on a daily GitHub Actions cron (`.github/workflows/daily-digest.yml`), pulling from:

- **Hugging Face Daily Papers** (official API) — two views: overall trending, and today's papers
  re-ranked client-side by upvotes
- **arXiv** (cs.AI / cs.LG / cs.CL, most recent submissions)
- **Hacker News** (AI/LLM/ML stories from the last 24 hours)
- **Reddit** r/MachineLearning (top daily posts)
- **Lab blogs**: OpenAI, DeepMind, Anthropic, Thinking Machines Lab, Perplexity, NVIDIA (blog +
  technical blog)
- **GitHub Trending** (new AI repos via the Search API, sorted by stars)

Output: `digest_latest.md` (always current), archived daily to `daily_digests/YYYY-MM-DD.md`, with
every source's fetch status logged per run to `logs/run_log.csv`.

### Tier 2 — Weekly Curated (`weekly_curated_digest.py`)

Runs on a weekly GitHub Actions cron (`.github/workflows/weekly-curated-digest.yml`), pulling from
a smaller set of pre-filtered newsletters and blogs rather than raw feeds:

- The Batch (DeepLearning.AI)
- The Rundown AI
- One Useful Thing
- MarkTechPost
- The Academic Digest (flagged manual — no reliable feed, check by hand)

Output: `weekly_curated_digest_latest.md`, archived to `weekly_digests/YYYY-MM-DD.md`, logged to
`logs/weekly_run_log.csv` with per-source status (so a single broken feed never masks failures in
the others).

## Design Principles

- **Fail loud, not silent**: every fetch function returns a status (`ok` / `empty` / `failed`) and
  an error string, logged per source per run. A source going quiet shows up in the log, not just as
  a missing section in the digest.
- **Defensive parsing**: external APIs change shape without notice. Parsers fall back through
  multiple plausible key layouts before giving up, and log the raw response shape when they do.
- **Prefer official APIs over scraped mirrors**: e.g. Hugging Face Daily Papers is pulled from HF's
  own `daily_papers` API rather than an unofficial RSS mirror, so sorting (`trending`, `publishedAt`)
  is accurate rather than whatever order a scraper happened to produce.

## Repo Structure

```
daily_digest.py                  # Tier 1 script
weekly_curated_digest.py         # Tier 2 script
.github/workflows/               # Cron + manual-trigger automation
digest_latest.md                 # Latest daily digest
weekly_curated_digest_latest.md  # Latest weekly digest
daily_digests/                   # Dated daily archives
weekly_digests/                  # Dated weekly archives
logs/                            # Per-run, per-source status logs (CSV)
```

## Running Locally

```bash
pip install requests feedparser
python daily_digest.py
python weekly_curated_digest.py
```

Optional environment variables: `SLACK_WEBHOOK_URL` (posts the digest to Slack), `GITHUB_TOKEN`
(authenticates the GitHub Trending fetch to avoid rate limits).

# Personal References
1. [https://www.paperdigest.org/](https://www.paperdigest.org/)
2. [https://huggingface.co/papers/trending](https://huggingface.co/papers/trending)
3. [https://www.oneusefulthing.org/](https://www.oneusefulthing.org/)
4. [https://github.com/trending](https://github.com/trending)
