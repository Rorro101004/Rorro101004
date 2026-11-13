"""Generate self-hosted GitHub profile metrics as static SVG cards.

Writes dark and light variants of two cards into assets/metrics/:
  - stats-dark.svg / stats-light.svg         (12-month activity summary)
  - languages-dark.svg / languages-light.svg (top languages of owned public repos)

Only the Python standard library is used. Data comes from the GitHub GraphQL API.
Token lookup order: METRICS_TOKEN, GITHUB_TOKEN, GH_TOKEN.

Usage:
    python scripts/generate_metrics.py [--login Rorro101004] [--out assets/metrics]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape

API_URL = "https://api.github.com/graphql"

# Languages that are generated scaffolding, markup or notebook payloads.
# They are excluded so the card reflects hand-written source code.
EXCLUDED_LANGUAGES = {
    "HTML", "CSS", "SCSS", "CMake", "C++", "Swift", "Objective-C", "Roff",
    "Jupyter Notebook", "Makefile", "Batchfile", "Shell", "PowerShell", "Dockerfile",
}

THEMES = {
    "dark": {
        "surface": "#15120F", "border": "#3A322A", "text": "#EFE8DC",
        "muted": "#B9AC9B", "accent": "#C9B497", "track": "#2B241E",
    },
    "light": {
        "surface": "#FAF7F2", "border": "#E3D9CC", "text": "#2B241E",
        "muted": "#5E5246", "accent": "#7A6248", "track": "#EDE5DA",
    },
}

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

QUERY = """
query($login: String!) {
  user(login: $login) {
    login
    followers { totalCount }
    repositories(first: 100, ownerAffiliations: OWNER, privacy: PUBLIC, isFork: false) {
      totalCount
      nodes {
        name
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name } }
        }
      }
    }
    repositoriesContributedTo(first: 25, includeUserRepositories: false, privacy: PUBLIC,
      contributionTypes: [COMMIT, PULL_REQUEST, REPOSITORY]) {
      totalCount
      nodes {
        name
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name } }
        }
      }
    }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      restrictedContributionsCount
      contributionCalendar {
        totalContributions
        weeks { contributionDays { contributionCount } }
      }
    }
  }
}
"""


def fetch(login: str, token: str) -> dict:
    body = json.dumps({"query": QUERY, "variables": {"login": login}}).encode()
    req = urllib.request.Request(
        API_URL,
        data=body,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "profile-metrics-script",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    if payload.get("errors"):
        raise RuntimeError(json.dumps(payload["errors"], indent=2))
    return payload["data"]["user"]


def summarize(user: dict) -> dict:
    repos = user["repositories"]["nodes"]
    cc = user["contributionsCollection"]
    weeks = [
        sum(day["contributionCount"] for day in week["contributionDays"])
        for week in cc["contributionCalendar"]["weeks"]
    ][-52:]

    lang_bytes: dict[str, float] = {}
    for repo in repos:
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            if name in EXCLUDED_LANGUAGES:
                continue
            lang_bytes[name] = lang_bytes.get(name, 0.0) + edge["size"]
    for repo in user["repositoriesContributedTo"]["nodes"]:
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            if name in EXCLUDED_LANGUAGES:
                continue
            lang_bytes[name] = lang_bytes.get(name, 0.0) + edge["size"] * 0.20
    total = sum(lang_bytes.values()) or 1
    top = sorted(lang_bytes.items(), key=lambda kv: kv[1], reverse=True)[:6]

    return {
        "stats": [
            ("Contributions (12 mo)", cc["contributionCalendar"]["totalContributions"]),
            ("Commits", cc["totalCommitContributions"]),
            ("Pull requests", cc["totalPullRequestContributions"]),
            ("Public repositories", user["repositories"]["totalCount"]),
            ("Contributed to", user["repositoriesContributedTo"]["totalCount"]),
            ("Stars earned", sum(r["stargazerCount"] for r in repos)),
        ],
        "weeks": weeks,
        "languages": [(name, size / total) for name, size in top],
    }


def frame(theme: dict, title: str, inner: str, width: int, height: int, stamp: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">\n'
        f"  <title>{escape(title)}</title>\n"
        f'  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="12" '
        f'fill="{theme["surface"]}" stroke="{theme["border"]}"/>\n'
        f'  <text x="24" y="36" font-family="{SANS}" font-size="16" font-weight="600" '
        f'fill="{theme["text"]}">{escape(title)}</text>\n'
        f'  <text x="{width - 24}" y="36" text-anchor="end" font-family="{MONO}" '
        f'font-size="11" fill="{theme["muted"]}">updated {stamp}</text>\n'
        f"{inner}"
        "</svg>\n"
    )


def render_stats(data: dict, theme: dict, stamp: str) -> str:
    width, height = 600, 220
    parts = []
    for i, (label, value) in enumerate(data["stats"]):
        col = i % 3
        row = i // 3
        x = 24 + col * 184
        y = 74 + row * 52
        parts.append(
            f'  <text x="{x}" y="{y}" font-family="{SANS}" font-size="12" '
            f'fill="{theme["muted"]}">{escape(label)}</text>\n'
            f'  <text x="{x}" y="{y + 24}" font-family="{MONO}" font-size="20" '
            f'font-weight="600" fill="{theme["text"]}">{value}</text>\n'
        )

    weeks = data["weeks"] or [0]
    peak = max(weeks) or 1
    chart_x, chart_y, chart_w, chart_h = 24, 160, width - 48, 40
    bar_w = chart_w / len(weeks)
    for i, count in enumerate(weeks):
        h = max(2.0, chart_h * count / peak)
        color = theme["accent"] if count else theme["track"]
        parts.append(
            f'  <rect x="{chart_x + i * bar_w:.1f}" y="{chart_y + chart_h - h:.1f}" '
            f'width="{max(bar_w - 2, 1):.1f}" height="{h:.1f}" rx="1.5" fill="{color}"/>\n'
        )
    parts.append(
        f'  <text x="{chart_x}" y="{chart_y + chart_h + 14}" font-family="{MONO}" '
        f'font-size="10" fill="{theme["muted"]}">weekly contributions, last 52 weeks</text>\n'
    )
    return frame(theme, "GitHub activity", "".join(parts), width, height, stamp)


def render_languages(data: dict, theme: dict, stamp: str) -> str:
    width, height = 600, 220
    parts = []
    langs = data["languages"] or [("n/a", 1.0)]
    for i, (name, share) in enumerate(langs):
        col = i // 3
        row = i % 3
        x = 24 + col * 284
        y = 72 + row * 48
        bar_w = 260
        parts.append(
            f'  <text x="{x}" y="{y}" font-family="{SANS}" font-size="13" '
            f'fill="{theme["text"]}">{escape(name)}</text>\n'
            f'  <text x="{x + bar_w}" y="{y}" text-anchor="end" font-family="{MONO}" '
            f'font-size="12" fill="{theme["muted"]}">{share * 100:.1f}%</text>\n'
            f'  <rect x="{x}" y="{y + 10}" width="{bar_w}" height="6" rx="3" '
            f'fill="{theme["track"]}"/>\n'
            f'  <rect x="{x}" y="{y + 10}" width="{max(bar_w * share, 3):.1f}" height="6" '
            f'rx="3" fill="{theme["accent"]}"/>\n'
        )
    parts.append(
        f'  <text x="24" y="{height - 16}" font-family="{MONO}" font-size="10" '
        f'fill="{theme["muted"]}">source bytes across owned and contributed public repos '
        f"(markup and notebooks excluded)</text>\n"
    )
    return frame(theme, "Most used languages", "".join(parts), width, height, stamp)


def write_if_changed(path: Path, content: str) -> bool:
    """Write only when the payload (ignoring the date stamp) changed."""
    def strip(text: str) -> str:
        return "\n".join(line for line in text.splitlines() if "updated " not in line)

    if path.exists() and strip(path.read_text(encoding="utf-8")) == strip(content):
        return False
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--login", default="Rorro101004")
    parser.add_argument("--out", default="assets/metrics")
    args = parser.parse_args()

    token = os.environ.get("METRICS_TOKEN") or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        print("error: set METRICS_TOKEN, GITHUB_TOKEN or GH_TOKEN", file=sys.stderr)
        return 1

    data = summarize(fetch(args.login, token))
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    changed = 0
    for mode, theme in THEMES.items():
        changed += write_if_changed(out / f"stats-{mode}.svg", render_stats(data, theme, stamp))
        changed += write_if_changed(out / f"languages-{mode}.svg", render_languages(data, theme, stamp))
    print(f"metrics: {changed} file(s) updated in {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
