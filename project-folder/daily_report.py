import json
import requests
from email_utils import send_email
from credentials import ALPHA_VANTAGE_API_KEY

def fetch_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)

    if response.status_code != 200:
        return None
    
    raw_data = response.json()
    if 'Time Series (Daily)' not in raw_data:
        return None

    iterator = iter(raw_data['Time Series (Daily)'])
    latest_date = next(iterator)
    latest_data = raw_data['Time Series (Daily)'][latest_date]

    return {
        'symbol': symbol,
        'date': latest_date,
        'open': float(latest_data['1. open']),
        'high': float(latest_data['2. high']),
        'low': float(latest_data['3. low']),
        'close': float(latest_data['4. close'])
    }

def main ():
    with open('watchlist.json', 'r') as file:
        watchlist = json.load(file)
    
    summary = "📈 Daily Stock Summary 📈\n\n"

    for symbol in watchlist:
        stock_data = fetch_stock_data(symbol)
        if stock_data:
            summary += (
                f"Symbol: {stock_data['symbol']} ({stock_data['date']})"
                f"Open: ${stock_data['open']:.2f}\n"
                f"High: ${stock_data['high']:.2f}\n"
                f"Low: ${stock_data['low']:.2f}\n"
                f"Close: ${stock_data['close']:.2f}\n\n"
            )
        else: 
            summary += f"⚠️ {symbol}: Data unavailable.\n\n"

    send_email("Daily Stock Watchlist Summary", summary)

if __name__ == "__main__":
    main()