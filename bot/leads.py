"""Lead capture to CSV (stdlib csv)."""
import csv
from pathlib import Path
FIELDS = ["name","phone","interest","source"]

def save_lead(path, name, phone, interest, source="telegram"):
    p = Path(path)
    exists = p.exists()
    with p.open("a", newline="", encoding="utf-8") as f:
        wtr = csv.DictWriter(f, fieldnames=FIELDS)
        if not exists:
            wtr.writeheader()
        wtr.writerow({"name":name,"phone":phone,"interest":interest,"source":source})
    return True

def load_leads(path):
    p = Path(path)
    if not p.exists():
        return []
    with p.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
