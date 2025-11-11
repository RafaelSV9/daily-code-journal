import sqlite3
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

DB_PATH = Path(__file__).resolve().parent.parent / "dataops.db"

def _conn():
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA journal_mode=WAL;")
    return conn

def init_db():
    conn = _conn()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS fx_rates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pair TEXT NOT NULL,
        bid REAL,
        ask REAL,
        ts INTEGER
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS github_activity (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        repo TEXT NOT NULL,
        type TEXT NOT NULL,
        title TEXT,
        url TEXT,
        ts INTEGER
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS insights (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        ts INTEGER
    );
    """)
    conn.commit()
    conn.close()

def insert_fx_rows(rows: List[Tuple[str, float, float, int]]):
    conn = _conn()
    conn.executemany("INSERT INTO fx_rates(pair,bid,ask,ts) VALUES(?,?,?,?)", rows)
    conn.commit()
    conn.close()

def latest_fx(limit: int = 50):
    conn = _conn()
    cur = conn.cursor()
    cur.execute("SELECT pair,bid,ask,ts FROM fx_rates ORDER BY id DESC LIMIT ?", (limit,))
    out = cur.fetchall()
    conn.close()
    return out

def insert_github_events(rows: List[Tuple[str, str, str, str, int]]):
    conn = _conn()
    conn.executemany("INSERT INTO github_activity(repo,type,title,url,ts) VALUES(?,?,?,?,?)", rows)
    conn.commit()
    conn.close()

def latest_github(limit: int = 50):
    conn = _conn()
    cur = conn.cursor()
    cur.execute("SELECT repo,type,title,url,ts FROM github_activity ORDER BY id DESC LIMIT ?", (limit,))
    out = cur.fetchall()
    conn.close()
    return out

def save_insight(text: str, ts: int):
    conn = _conn()
    conn.execute("INSERT INTO insights(content, ts) VALUES(?,?)", (text, ts))
    conn.commit()
    conn.close()

def latest_insight() -> str | None:
    conn = _conn()
    cur = conn.cursor()
    cur.execute("SELECT content FROM insights ORDER BY id DESC LIMIT 1")
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None
