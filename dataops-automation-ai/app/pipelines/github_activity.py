import time
import requests
from typing import List, Tuple, Dict
from ..storage import store
from ..utils.config import settings

def _headers():
    h = {"Accept": "application/vnd.github+json"}
    if settings.github_token:
        h["Authorization"] = f"Bearer {settings.github_token}"
    return h

def fetch_activity(repo: str) -> List[Tuple[str,str,str,str,int]]:
    rows = []
    now = int(time.time())
    # events API (pública)
    url = f"https://api.github.com/repos/{repo}/events"
    r = requests.get(url, headers=_headers(), timeout=15)
    if r.status_code != 200:
        return rows
    for ev in r.json()[:20]:
        etype = ev.get("type", "Event")
        title = None
        html_url = None
        # mapeia alguns tipos comuns
        if etype == "IssuesEvent":
            issue = ev.get("payload", {}).get("issue", {})
            title = issue.get("title")
            html_url = issue.get("html_url")
        elif etype in ("PushEvent", "CreateEvent"):
            ref = ev.get("payload", {}).get("ref")
            title = f"{etype} {ref}" if ref else etype
            html_url = f"https://github.com/{repo}"
        elif etype == "PullRequestEvent":
            pr = ev.get("payload", {}).get("pull_request", {})
            title = pr.get("title")
            html_url = pr.get("html_url")
        else:
            title = etype
            html_url = f"https://github.com/{repo}"
        rows.append((repo, etype, title or etype, html_url, now))
    return rows

def run_github_pipeline(repos: List[str]):
    allrows = []
    for repo in repos:
        try:
            rows = fetch_activity(repo)
            if rows:
                store.insert_github_events(rows)
                allrows.extend(rows)
        except Exception:
            continue
    return allrows
