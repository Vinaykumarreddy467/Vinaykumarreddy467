"""Refresh the auto-generated sections of the profile README from the GitHub API.

Rewrites the text between <!-- LATEST_SHIPS:START --> / <!-- LATEST_SHIPS:END -->
and <!-- PULSE:START --> / <!-- PULSE:END -->, and syncs the LinkedIn numbers from
data/linkedin.json into the badges and hero SVGs. Run daily by .github/workflows/update-readme.yml.
"""

import json
import os
import re
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

USER = "Vinaykumarreddy467"
ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
LINKEDIN = ROOT / "data" / "linkedin.json"
HERO_SVGS = [ROOT / "assets" / "hero-terminal.svg", ROOT / "assets" / "hero-terminal-mobile.svg"]
SKIP = {USER, "practice", "StudentManagement", "MultiAgents"}
SHIPS = 6


def api(path):
    req = urllib.request.Request(f"https://api.github.com{path}", headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def ago(iso):
    days = (datetime.now(timezone.utc) - datetime.fromisoformat(iso.replace("Z", "+00:00"))).days
    if days == 0:
        return "today"
    if days == 1:
        return "yesterday"
    if days < 30:
        return f"{days} days ago"
    if days < 365:
        return f"{days // 30} mo ago"
    return f"{days // 365} yr ago"


def replace(text, tag, body):
    pattern = re.compile(rf"(<!-- {tag}:START -->).*?(<!-- {tag}:END -->)", re.S)
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(2)}", text)


def main():
    repos = [r for r in api(f"/users/{USER}/repos?per_page=100&type=owner&sort=pushed")
             if not r["fork"] and r["name"] not in SKIP and r["size"] > 0]

    rows = []
    for i, r in enumerate(repos[:SHIPS]):
        dot = "🟢" if i == 0 else "🟣"
        desc = r["description"] or "—"
        if len(desc) > 110:
            desc = desc[:107].rstrip() + "…"
        rows.append(f"- {dot} **[{r['name']}]({r['html_url']})** · `{r['language'] or '—'}` · <sub>pushed {ago(r['pushed_at'])}</sub><br/>"
                    f"<sub>{desc}</sub>")

    langs = Counter(r["language"] for r in repos if r["language"])
    top = " · ".join(f"<code>{name}</code>" for name, _ in langs.most_common(5))
    stars = sum(r["stargazers_count"] for r in repos)
    stamp = datetime.now(timezone.utc).strftime("%d %b %Y")
    li = json.loads(LINKEDIN.read_text(encoding="utf-8"))
    posts, followers = li["posts"], li["followers"]
    for svg in HERO_SVGS:
        svg.write_text(re.sub(r">\d+ posts<", f">{posts} posts<", svg.read_text(encoding="utf-8")), encoding="utf-8")

    pulse = (f"<p align=\"center\"><sub>📦 <b>{len(repos)}</b> original repos &nbsp;·&nbsp; ⭐ <b>{stars}</b> stars "
             f"&nbsp;·&nbsp; ✍️ <b>{posts}</b> LinkedIn posts "
             f"&nbsp;·&nbsp; 🧠 most-used: {top} &nbsp;·&nbsp; 🤖 auto-updated {stamp}</sub></p>")

    text = README.read_text(encoding="utf-8")
    text = replace(text, "LATEST_SHIPS", "\n".join(rows))
    text = replace(text, "PULSE", pulse)
    text = re.sub(r"badge/LinkedIn-[\d,]+_followers", f"badge/LinkedIn-{followers:,}_followers", text)
    text = re.sub(r"badge/✍️_Posts-\d+_on_LinkedIn", f"badge/✍️_Posts-{posts}_on_LinkedIn", text)
    README.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
