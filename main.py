#!/usr/bin/env python3
"""CLI demo. --demo runs sample questions; otherwise reads stdin lines."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from bot.handlers import answer_question

SAMPLE = ["نصب ویندوز چقدر است؟","اسمبل سیستم گیمینگ می‌خوام","نصب بازی PS5 دارید؟","ساعت کاری شما چیه؟","هوا چطوره؟"]

def main():
    if "--demo" in sys.argv:
        for q in SAMPLE:
            print(f"\n❓ {q}\n💬 {answer_question(q)}")
        return 0
    print("Telegram Sales Agent demo (Ctrl-D to exit). Ask in Persian:")
    for line in sys.stdin:
        line=line.strip()
        if line:
            print(answer_question(line))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
