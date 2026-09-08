"""
Reads a digest .md file, extracts a given "## Lab Blog: X" section,
opens each link, and asks an OpenRouter LLM to write a <=280-char
X (Twitter) post summarizing it. Saves results to CSV + a markdown draft file.

Usage:
    python summarize_section_for_x.py 2026-09-06.md "Lab Blog: OpenAI"
"""

import os
import re
import sys
import csv
import time
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "nvidia/nemotron-3.5-lightning:free"
MAX_CHARS = 280
REQUEST_TIMEOUT = 20


# ---------- 1. OpenRouter call (your existing function, lightly extended) ----------
def ask(question, model=MODEL, retries=3):
    for attempt in range(retries):
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": question}],
                    "reasoning": {"enabled": True},
                },
                timeout=REQUEST_TIMEOUT,
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            if attempt == retries - 1:
                raise
            time.sleep(30 * (attempt + 1))


# ---------- 2. Parse the markdown digest ----------
def extract_section(md_text, section_title):
    pattern = rf"##\s*{re.escape(section_title)}\s*\n(.*?)(?=\n##\s|\Z)"
    m = re.search(pattern, md_text, re.DOTALL)
    if not m:
        raise ValueError(f"Section '{section_title}' not found in the digest.")
    return m.group(1).strip()


def parse_bullets(section_text):
    items = []
    blocks = re.split(r"\n(?=- \*\*\[)", section_text.strip())
    for b in blocks:
        m = re.match(r"- \*\*\[(.*?)\]\((.*?)\)\*\*\s*\n?(.*)", b.strip(), re.DOTALL)
        if m:
            title, url, rest = m.group(1), m.group(2), m.group(3).strip()
            snippet = re.sub(r"\s*\n\s*", " ", rest)
            items.append({"title": title, "url": url, "snippet": snippet})
    return items


# ---------- 3. Fetch actual page text (falls back to digest snippet on failure) ----------
def fetch_page_text(url, max_chars=12000):
    try:
        r = requests.get(
            url,
            timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": "Mozilla/5.0 (compatible; DigestBot/1.0)"},
        )
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        text = " ".join(soup.get_text(separator=" ").split())
        return text[:max_chars] if text else None
    except Exception:
        return None


# ---------- 4. Build the summarization prompt ----------
def build_prompt(title, url, snippet, page_text):
    source_text = page_text if page_text else snippet
    return f"""You are writing a single X (Twitter) post for an AI researcher's account.

Article title: {title}
URL: {url}
Source content: {source_text}

Write ONE X post that:
- Is STRICTLY <= {MAX_CHARS} characters INCLUDING the URL at the end.
- Leads with the single most interesting/concrete insight, not a generic intro.
- Uses plain, confident, no-hype language a technical audience respects.
- No hashtags, no emojis, no "Exciting news!" filler.
- Ends with the URL on its own so it renders as a link preview.

Output ONLY the post text, nothing else."""


def enforce_length(post_text, url):
    post_text = post_text.strip().strip('"')
    if len(post_text) <= MAX_CHARS:
        return post_text
    # Trim while keeping the URL intact at the end
    if url in post_text:
        body = post_text.replace(url, "").strip()
        budget = MAX_CHARS - len(url) - 1
        body = body[:budget].rsplit(" ", 1)[0] + "…"
        return f"{body} {url}"
    return post_text[: MAX_CHARS - 1] + "…"


# ---------- 5. Main pipeline ----------
def main(md_path, section_title):
    with open(md_path, encoding="utf-8") as f:
        md_text = f.read()

    section = extract_section(md_text, section_title)
    items = parse_bullets(section)
    print(f"Found {len(items)} links in '{section_title}'.")

    results = []
    for i, item in enumerate(items, 1):
        print(f"[{i}/{len(items)}] {item['title']}")
        page_text = fetch_page_text(item["url"])
        prompt = build_prompt(item["title"], item["url"], item["snippet"], page_text)
        try:
            raw_post = ask(prompt)
        except Exception as e:
            print(f"  LLM call failed: {e}")
            raw_post = f"{item['title']} — {item['snippet'][:180]} {item['url']}"

        final_post = enforce_length(raw_post, item["url"])
        results.append(
            {
                "title": item["title"],
                "url": item["url"],
                "post": final_post,
                "char_count": len(final_post),
            }
        )

    # Save CSV (for spreadsheet review / scheduler import)
    csv_path = "x_posts_draft.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "url", "post", "char_count"])
        writer.writeheader()
        writer.writerows(results)

    # Save Markdown (for quick human review)
    md_out_path = "x_posts_draft.md"
    with open(md_out_path, "w", encoding="utf-8") as f:
        f.write(f"# X post drafts — {section_title}\n\n")
        for r in results:
            f.write(f"## {r['title']}\n")
            f.write(f"{r['post']}\n\n")
            f.write(f"_({r['char_count']} chars)_\n\n---\n\n")

    print(f"\nSaved {len(results)} drafts to {csv_path} and {md_out_path}")
    return results


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python summarize_section_for_x.py <digest.md> "Lab Blog: OpenAI"')
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
