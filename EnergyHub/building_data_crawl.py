import time
import random
import requests

def dc_token():
    # 13-stellige "Zufallszahl" (ähnlich Zeitstempel) – reicht als Cache-Buster
    return str(int(time.time() * 1000))[:13]

BASE = "https://webtool.building-typology.eu"
HEADERS = {
    "Referer": "https://webtool.building-typology.eu/",
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

def fetch_matrix(country="de", limit=25):
    url = f"{BASE}/data/matrix/building/{country}/p/0/o/0/l/{limit}/dc/{dc_token()}"
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()

def fetch_building_detail(code, bv=1):
    url = f"{BASE}/data/adv/building/detail/{code}/bv/{bv}/dc/{dc_token()}"
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()

# --- Beispielnutzung ---
# 1) Matrix ziehen und prüfen, ob dein Code enthalten ist
matrix = fetch_matrix("de", limit=1000)  # Limit erhöht, paging wird serverseitig ignoriert
codes = [row.get("code") or row.get("id") for row in matrix.get("data", matrix)]
print("Beispielcodes:", codes[:5])

# 2) Dein Gebäude abrufen (Variante 1 probieren, sonst 2,3 ...)
code = "DE.N.SFH.07.Gen.ReEx.001"
detail = fetch_building_detail(code, bv=1)
print("Titel:", detail.get("title") or detail.get("name"))
print("Keys:", list(detail.keys())[:20])

# 3) Falls bv=1 nicht existiert, nächste Varianten testen
for bv in (1, 2, 3, 4):
    try:
        d = fetch_building_detail(code, bv=bv)
        print(f"Variante {bv} gefunden, relevante Felder:", [k for k in d.keys() if "u-value" in k.lower() or "area" in k.lower()][:10])
        break
    except requests.HTTPError as e:
        if e.response is not None and e.response.status_code in (400,404):
            continue
        else:
            raise
