import matplotlib.pyplot as plt

def create_growth_chart():
    months = list(range(1, 13))
    capital = 100_000_000
    monthly_rate = 0.025  # رشد ماهانه ۲.۵٪ تقریبی

    values = [capital * ((1 + monthly_rate) ** m) for m in months]

    plt.figure(figsize=(8, 5))
    plt.plot(months, values, marker='o')
    plt.title("📈 پیش‌بینی رشد سرمایه در ۱۲ ماه")
    plt.xlabel("ماه")
    plt.ylabel("سرمایه (تومان)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("growth_chart.png")