"""Pure logic handlers - no network. answer_question(text) -> reply str."""
from .faq import load_kb, find_best

FALLBACK = "سلام! 👋 به خدمات کامپیوتری سینا خوش آمدید. درباره نصب ویندوز، اسمبل سیستم یا نصب بازی بپرسید، یا شماره‌تان را بفرستید تا تماس بگیریم."

_KB = None
def _kb():
    global _KB
    if _KB is None:
        _KB = load_kb()
    return _KB

def format_price(price):
    return f"{price:,}".replace(",", "٬") + " تومان" if price else None

def answer_question(text, kb=None):
    kb = kb if kb is not None else _kb()
    entry = find_best(text or "", kb)
    if not entry:
        return FALLBACK
    reply = entry["answer"]
    price = format_price(entry.get("price_toman"))
    if price:
        reply += f"\n💰 قیمت: {price}"
    reply += "\n📞 سفارش: 09185790374"
    return reply
