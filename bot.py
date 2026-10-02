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
        print(f"{site} -> {status