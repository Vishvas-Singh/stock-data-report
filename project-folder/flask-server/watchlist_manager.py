import requests
import json
from datetime import datetime

def get_stock_watchlist(filename="watchlist.json"):
    try:
        with open(filename, 'r') as file:
            watchlist = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        watchlist = []

    print("Enter the stock symbols you want to add to your watchlist. Type 'done' when finished.")

    while True:
        symbol = input("Stock: ")

        if symbol == 'done':
            break
        else:
            watchlist.append(symbol)

    with open(filename, 'w') as file:
        json.dump(watchlist, file, indent=4)

    return watchlist

def fetch_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=FZUW66LFY0OSONCO'
    response = requests.get(url)

    if response.status_code == 200:
        raw_data = response.json()

        if 'Time Series (Daily)' not in raw_data:
            print(f"Error: Invalid stock symbol or data unavailable for {symbol}. Please check the symbol and try again.")
            return None
        
        iterator = iter(raw_data['Time Series (Daily)'])
        latest_date = next(iterator)

        latest_data = raw_data['Time Series (Daily)'][latest_date]

        print(f"Today's data for {symbol}: ")
        print(f"Open: {latest_data['1. open']}")
        print(f"Close: {latest_data['4. close']}")
        print(f"High: {latest_data['2. high']}")
        print(f"Low: {latest_data['3. low']}")
    else:
        print(f"Failed to retrieve data {response.status_code}")
        return None

if __name__ == "__main__":
    watchlist = get_stock_watchlist()

    print("Would you like today's stock data? (Y/N): ")
    while True:
        confirmation = input()
        if confirmation == 'Y':
            for symbol in watchlist:
                fetch_stock_data(symbol)
        else:
            break