from apscheduler.schedulers.background import BackgroundScheduler
from telegram import Bot
from weekly_report import generate_weekly_report
from config import TELEGRAM_TOKEN
from alerts import check_and_send_alerts

bot = Bot(token=TELEGRAM_TOKEN)
chat_ids = []  # آی‌دی کاربران

def send_weekly_report():
    report = generate_weekly_report()
    for chat_id in chat_ids:
        bot.send_message(chat_id=chat_id, text=report)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_weekly_report, 'cron', day_of_week='fri', hour=9)
    scheduler.add_job(check_and_send_alerts, 'interval', minutes=30)  # بررسی هشدار هر ۳۰ دقیقه
    scheduler.start()