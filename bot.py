from telegram.ext import Updater, CommandHandler
from config import TELEGRAM_TOKEN
from recommender import get_investment_advice
from scheduler import start_scheduler
from crypto_price import get_dollar_price, get_bitcoin_price

def start(update, context):
    update.message.reply_text("👋 سلام! به بات سرمایه‌گذاری مهدی خوش آمدی. برای دریافت پیشنهاد، /suggest رو بزن.")

def suggest(update, context):
    advice = get_investment_advice()
    update.message.reply_text(advice)

def prices(update, context):
    dollar = get_dollar_price()
    bitcoin = get_bitcoin_price()
    msg = f"💵 قیمت فعلی دلار: {dollar} تومان
₿ قیمت بیت‌کوین: {bitcoin} دلار"
    update.message.reply_text(msg)

updater = Updater(TELEGRAM_TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("suggest", suggest))
dp.add_handler(CommandHandler("prices", prices))

start_scheduler()
updater.start_polling()
updater.idle()