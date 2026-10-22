import sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from bot.handlers import answer_question
from bot.faq import load_kb, find_best
from bot.leads import save_lead, load_leads

class TestFaq(unittest.TestCase):
    def test_windows_price(self):
        r = answer_question("نصب ویندوز چقدر است؟")
        self.assertIn("ویندوز", r)
        self.assertIn("تومان", r)
    def test_assembly_and_game(self):
        self.assertIn("اسمبل", answer_question("اسمبل سیستم می خوام"))
        self.assertIn("بازی", answer_question("نصب بازی کنسول دارید؟"))
    def test_fallback(self):
        r = answer_question("یک سوال کاملا نامربوط درباره فضا")
        self.assertIn("خوش آمدید", r)
    def test_kb_has_prices(self):
        kb = load_kb()
        priced = [e for e in kb if e.get("price_toman")]
        self.assertGreaterEqual(len(priced), 3)
    def test_lead_csv(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"leads.csv"
            save_lead(p, "Ali", "09120000000", "windows")
            leads = load_leads(p)
            self.assertEqual(len(leads), 1)
            self.assertEqual(leads[0]["interest"], "windows")

if __name__ == "__main__":
    unittest.main()
