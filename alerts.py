from telegram import Bot
from crypto_price import get_dollar_price, get_bitcoin_price
from config import TELEGRAM_TOKEN
import time

bot = Bot(token=TELEGRAM_TOKEN)

# لیست چت آیدی‌هایی که هشدار بگیرند
chat_ids = []

# حدود قیمتی برای هشدار
DOLLAR_ALERT_THRESHOLD = 100000  # تومان
BITCOIN_DROP_THRESHOLD = 25000   # دلار

# وضعیت قبلی برای بررسی تغییرات
previous_dollar = None
previous_bitcoin = None

def check_and_send_alerts():
    global previous_dollar, previous_bitcoin

    try:
        dollar = get_dollar_price()
        bitcoin = get_bitcoin_price()

        if isinstance(dollar, int) and (previous_dollar is None or dollar > DOLLAR_ALERT_THRESHOLD > previous_dollar):
            for chat_id in chat_ids:
                bot.send_message(chat_id=chat_id, text=f"🚨 هشدار: قیمت دلار به {dollar:,} تومان رسید!")
        previous_dollar = dollar

        if isinstance(bitcoin, int) and (previous_bitcoin is None or bitcoin < BITCOIN_DROP_THRESHOLD < previous_bitcoin):
            for chat_id in chat_ids:
                bot.send_message(chat_id=chat_id, text=f"⚠️ هشدار: قیمت بیت‌کوین به {bitcoin:,} دلار کاهش یافت!")
        previous_bitcoin = bitcoin

    except Exception as e:
        print(f"❌ خطا در بررسی هشدارها: {e}")

from inflation_watch import get_gold_price, inflation_alert

# بررسی احتمال شوک تورمی همزمان با بررسی قیمت‌ها
def check_inflation_signal():
    global previous_dollar
    global previous_gold
    dollar_now = get_dollar_price()
    gold_now = get_gold_price()

    if previous_dollar and previous_gold and dollar_now and gold_now:
        inflation_alert(bot, chat_ids, dollar_now, previous_dollar, gold_now, previous_gold)
    previous_dollar = dollar_now
    previous_gold = gold_now

# اضافه به هشدارهای دوره‌ای:
def check_and_send_alerts():
    ...
    check_inflation_signal()
