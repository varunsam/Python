import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os
import time

# Headers to mimic a real browser
#'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edg/139.0.3405.102"
}

# List of NSE stocks to track (Moneycontrol URLs)
STOCKS = [
    {"name": "TCS", "url": "https://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS"},
    {"name": "Infosys", "url": "https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT"},
    {"name": "HDFC Bank", "url": "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/hdfcbank/HDF01"},
    {"name": "Reliance", "url": "https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI"},
    {"name": "ICICI Bank", "url": "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/icicibank/ICI02"}
]

# CSV file path
CSV_FILE = "nse_stock_prices_log.csv"

def fetch_price(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        price_tag = soup.find("div", class_="inprice1")
        
        #print(f'Price_tag: {price_tag["rel"]}')
        if price_tag:            
            return price_tag['rel']
    except Exception as e:
        print(f"Error fetching from {url}: {e}")
    return "N/A"

def scrape_and_append():
    records = []
    date = datetime.now().strftime("%d-%m-%Y")
    time_now = datetime.now().strftime("%H:%M:%S")

    print(f"\nFetching stock prices at {date} {time_now}...")

    for stock in STOCKS:
        price = fetch_price(stock["url"])
        print(f"{stock['name']}: Rs. {price}")
        records.append({
            "Stock": stock["name"],
            "Price (₹)": price,
            "Date": date,
            "Time": time_now
        })
        time.sleep(1)  # Be polite!

    df = pd.DataFrame(records)

    # Append to CSV or create if not exists
    file_exists = os.path.isfile(CSV_FILE)
    df.to_csv(CSV_FILE, mode='a', header=not file_exists, index=False)

    print(f"Appended {len(records)} records to '{CSV_FILE}'")

# --- Main Execution ---
if __name__ == "__main__":
    while True:
        scrape_and_append()
        time.sleep(60)
    
