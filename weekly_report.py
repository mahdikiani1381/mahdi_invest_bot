from config import INITIAL_CAPITAL, CRYPTO_PERCENT

def generate_weekly_report():
    crypto_value = INITIAL_CAPITAL * CRYPTO_PERCENT
    fixed_income_value = INITIAL_CAPITAL * 0.5
    local_market_value = INITIAL_CAPITAL - crypto_value - fixed_income_value

    report = f"""
📅 گزارش هفتگی سرمایه‌گذاری:

💰 سرمایه کل: {INITIAL_CAPITAL:,.0f} تومان

📌 ترکیب دارایی پیشنهادی:
- 📉 صندوق درآمد ثابت: {fixed_income_value:,.0f} تومان
- 💵 بازار داخلی (دلار، طلا): {local_market_value:,.0f} تومان
- ₿ کریپتو (BTC/ETH): {crypto_value:,.0f} تومان

📈 تحلیل وضعیت: بازار در فاز تعادل نسبی قرار دارد.
💡 پیشنهاد: وضعیت ترکیب حفظ شود مگر شوک قیمتی رخ دهد.

برای بررسی دقیق‌تر، در طول هفته وضعیت نوسانات را دنبال کنید.
"""
    return report