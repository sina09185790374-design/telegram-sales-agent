# Telegram Sales & Support Agent 🤖

A Persian sales/support bot core for small shops — **tiny RAG over your own FAQ, price answers, and lead capture to CSV**. Pure logic, no network in the core, so it's fully testable.

Live pattern from a real computer-services shop in Arak: Windows install, PC assembly, game install — with prices in toman.

## Quick Start
```bash
python3 main.py --demo
echo "نصب ویندوز چقدر است؟" | python3 main.py
python3 -m unittest discover -s tests -v
```
Stdlib only. To deploy: wrap `bot/handlers.answer_question()` in your Telegram framework and set `BOT_TOKEN` from `.env` (never commit it).

## Structure
```
bot/faq.py       keyword-scoring retrieval over knowledge_base.example.json
bot/handlers.py  answer_question(text) -> reply
bot/leads.py     lead capture to CSV
main.py          CLI demo / stdin chat loop
```

## License
MIT

---
## فارسی
هسته چت‌بات فروش و پشتیبانی فارسی برای مغازه‌ها: پاسخ‌گویی از روی دیتای خود کسب‌وکار، اعلام قیمت به تومان و ثبت لید در CSV. بدون اینترنت در هسته اصلی کار می‌کند؛ برای دمو: `python3 main.py --demo`
