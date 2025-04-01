from flask import Flask, jsonify, redirect, url_for
import requests
import json
from datetime import datetime

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

# load watchlist
def get_stock_watchlist(filename="watchlist.json"):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# save wathclist
def save_wathclist(watchlist):
    with open("watchlist.json", 'w') as file:
        json.dump(watchlist, file, indent=4)

# Fetch stock data
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

        return {
            "symbol": symbol,
            "date": latest_date,
            "open": latest_data['1. open'],
            "close": latest_data['4. close'],
            "high": latest_data['2. high'],
            "low": latest_data['3. low']
        }
    else:
        return {"error": f"Failed to retrieve data {response.status_code}"}
    
# Home route
@app.route("/", method = ['GET', 'POST'])
def home():
    watchlist = get_stock_watchlist()

    print("Would you like today's stock data? (Y/N): ")
    while True:
        confirmation = input()
        if confirmation == 'Y':
            for symbol in watchlist:
                fetch_stock_data(symbol)
        else:
            break

# Stock data route
@app.route("/stock/<symbol>")
def stock_data(symbol):
    data = fetch_stock_data()

    if data:
        return jsonify(data)
    else:
        return jsonify({"error": f"Stock data for {symbol} not found."})
