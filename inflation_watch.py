import requests

# بررسی قیمت طلا از یک API نمایشی
def get_gold_price():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        usd_to_irr = response.json()['rates'].get('IRR', 0)
        # فرض: هر گرم طلا 75 دلار است
        gold_price = 75 * usd_to_irr
        return round(gold_price)
    except:
        return None

# بررسی قیمت واحد صندوق درآمد ثابت
def get_fund_nav():
    try:
        # فرض: صندوق از API بانک ارائه می‌شود (نمونه شبیه‌سازی شده)
        # مقدار بازگشتی NAV صندوق فرضی بر حسب هزار تومان
        return 1200
    except:
        return None

# تحلیل ساده شروع شوک تورمی: اگر دلار و طلا با هم افزایش ناگهانی داشته باشند
def is_inflation_shock(dollar_now, dollar_prev, gold_now, gold_prev):
    if not all([dollar_now, dollar_prev, gold_now, gold_prev]):
        return False
    jump_dollar = (dollar_now - dollar_prev) / dollar_prev
    jump_gold = (gold_now - gold_prev) / gold_prev
    return jump_dollar > 0.08 and jump_gold > 0.08  # اگر هر دو >۸٪ رشد کنند => شوک

# هشدار هوشمند شروع شوک تورمی
def inflation_alert(bot, chat_ids, dollar_now, dollar_prev, gold_now, gold_prev):
    if is_inflation_shock(dollar_now, dollar_prev, gold_now, gold_prev):
        for cid in chat_ids:
            bot.send_message(chat_id=cid, text="🔥 هشدار: احتمال شروع شوک تورمی وجود دارد! بررسی بازار دلار و طلا پیشنهاد می‌شود.")