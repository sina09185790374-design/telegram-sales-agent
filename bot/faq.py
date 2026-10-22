"""Tiny Persian RAG: keyword scoring over a JSON knowledge base."""
import json, re
from pathlib import Path

def _norm(text):
    return (text or "").lower().replace("ي","ی").replace("ك","ک").strip()

def load_kb(path=None):
    if path is None:
        path = Path(__file__).resolve().parents[1]/"knowledge_base.example.json"
    return json.loads(Path(path).read_text(encoding="utf-8"))

def score_entry(text, entry):
    t = _norm(text)
    score = 0
    for kw in entry.get("keywords",[]):
        if _norm(kw) in t:
            score += len(kw)  # longer, more specific keywords weigh more
    # token overlap with question as fallback signal
    qwords = set(re.findall(r"\w+", _norm(entry.get("question",""))))
    twords = set(re.findall(r"\w+", t))
    score += len(qwords & twords)
    return score

def find_best(text, kb):
    best, best_score = None, 0
    for e in kb:
        s = score_entry(text, e)
        if s > best_score:
            best, best_score = e, s
    return best if best_score > 0 else None
