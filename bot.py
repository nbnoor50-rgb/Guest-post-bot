import requests
from datetime import datetime

print("🚀 Noor Guest Post Bot Started -", datetime.now())

# ستا هدف سایټونه
sites = [
    "propakistani.pk",
    "hamariweb.com", 
    "techjuice.pk",
    "pakwired.com",
    "techjuice.pk/write-for-us",
    "propakistani.pk/write-for-us"
]

# Guest Post لپاره پیغامونه
message_template = """
Hello {site} Team,

I am Noor from RGB. I want to buy Guest Post on your site.

My budget is $20-$50 per post. I have quality tech/business content.

Can you send me your guest post rates?

WhatsApp: +92-XXX
Email: nbnoor50@gmail.com

Thanks,
Noor
"""

# د هر سایټ لپاره چیک
results = []
for site in sites:
    try:
        url = f"https://{site}" if not site.startswith("http") else site
        # یوازې چیک کوو چې سایټ ژوندی دی
        r = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        status = "LIVE ✅" if r.status_code == 200 else f"Status {r.status_code}"
        print(f"{site} -> {status}")
        results.append(f"{site} | {status} | Ready for outreach")
    except Exception as e:
        print(f"{site} -> Error: {e}")
        results.append(f"{site} | Error | {e}")

# راپور خوندي کول
with open("daily_report.txt", "w", encoding="utf-8") as f:
    f.write(f"Noor Bot Report - {datetime.now()}\n")
    f.write("="*40 + "\n")
    for line in results:
        f.write(line + "\n")
    f.write("\n" + "="*40 + "\n")
    f.write("Next Step: Contact these sites via their contact page\n")
    f.write(message_template)

print("\n✅ Bot Finished! Report saved to daily_report.txt")
print("Ready to buy and sell guest posts!")