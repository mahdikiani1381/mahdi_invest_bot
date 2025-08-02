import requests

def get_dollar_price():
    try:
        # API رایگان یا سرور ایرانی دلخواه رو اینجا وارد کن
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        return round(data['rates'].get('IRR', 0))
    except:
        return "❌ خطا در دریافت قیمت دلار"

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        data = response.json()
        return round(data['bitcoin']['usd'])
    except:
        return "❌ خطا در دریافت قیمت بیت‌کوین"