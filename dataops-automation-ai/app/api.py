from fastapi import FastAPI
from .storage import store
from .utils.config import settings

app = FastAPI(title=settings.project_name)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/fx/latest")
def fx_latest(limit: int = 20):
    rows = store.latest_fx(limit=limit)
    return [{"pair": r[0], "bid": r[1], "ask": r[2], "ts": r[3]} for r in rows]

@app.get("/github/activity")
def github_activity(limit: int = 30):
    rows = store.latest_github(limit=limit)
    return [{"repo": r[0], "type": r[1], "title": r[2], "url": r[3], "ts": r[4]} for r in rows]

@app.get("/insights")
def insights():
    text = store.latest_insight()
    return {"insight": text}
