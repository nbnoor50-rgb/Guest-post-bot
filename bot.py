import requests
from datetime import datetime

# قیمت راوړل
try:
    r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    price = float(r.json()['price'])
except:
    price = 86410

# هوښیار تحلیل
if price > 86000:
    signal = "گران دی - مه اخله - انتظار وکړه!"
    action = "WAIT"
elif price < 82000:
    signal = "ارزان دی - اخیستل ښه دی!"
    action = "BUY"
else:
    signal = "بازار منځ کې دی - صبر وکړه"
    action = "HOLD"

# رپوټ جوړول
today = datetime.now().strftime("%Y-%m-%d %H:%M")
report = f"""
نور جان رپوټ - {today}

BTC قیمت: ${price}
سگنل: {signal}
عمل: {action}

هوښیار Bot له خوا! 🤖💰
"""

with open("daily_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("هوښیار Bot کار وکړ!")
