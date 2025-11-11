import time
import requests
from typing import List, Tuple
from ..storage import store

# AwesomeAPI docs: https://docs.awesomeapi.com.br/api-de-moedas
def fetch_pairs(pairs: List[str]) -> List[Tuple[str, float, float, int]]:
    results = []
    now = int(time.time())
    for pair in pairs:
        base, quote = pair.split("-")
        url = f"https://economia.awesomeapi.com.br/json/last/{base}-{quote}"
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            data = r.json()
            key = f"{base}{quote}"
            item = data.get(key) or {}
            bid = float(item.get("bid", 0))
            ask = float(item.get("ask", 0))
            results.append((pair, bid, ask, now))
        except Exception as e:
            # Fallback: store zeros so pipeline não quebra
            results.append((pair, 0.0, 0.0, now))
    return results

def run_fx_pipeline(pairs: List[str]):
    rows = fetch_pairs(pairs)
    store.insert_fx_rows(rows)
    return rows
