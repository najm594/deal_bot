import os
import requests
from bs4 import BeautifulSoup

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error sending message: {e}")

def scrape_amazon_deals():
    url = "https://www.amazon.de/gp/goldbox"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch page, status code: {response.status_code}")
            return
            
        soup = BeautifulSoup(response.text, 'html.parser')
        deals = soup.select('.Grid-module_grid__C4wdS div.Grid-module_item__AiaGg')
        
        # إرسال رسالة تؤكد نجاح الفحص والتشغيل
        send_telegram_message("🤖 تم تشغيل بوت رادار صفقات أمازون ألمانيا بنجاح ويقوم بفحص العروض الآن!")
    except Exception as e:
        print(f"Error during scraping: {e}")

if __name__ == "__main__":
    scrape_amazon_deals()
