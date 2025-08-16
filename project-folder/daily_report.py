import json
import requests
from email_utils import send_email
from credentials import ALPHA_VANTAGE_API_KEY
from credentials import NEWS_API_KEY

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

def format_stock_data(watchlist):
    stock_section = "📊 Stock Watchlist Summary 📊\n\n"
    
    for symbol in watchlist:
        stock_data = fetch_stock_data(symbol)
        if stock_data:
            stock_section += (
                f"Symbol: {stock_data['symbol']} ({stock_data['date']})\n"
                f"Open: ${stock_data['open']:.2f}\n"
                f"High: ${stock_data['high']:.2f}\n"
                f"Low: ${stock_data['low']:.2f}\n"
                f"Close: ${stock_data['close']:.2f}\n\n"
            )
        else: 
            stock_section += f"⚠️ {symbol}: Data unavailable.\n\n"
    
    return stock_section


def fetch_news():
    url = f'https://newsapi.org/v2/top-headlines?category=business&country=us&pageSize=5&apiKey={NEWS_API_KEY}'

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return None
        
        data = response.json()

        if data['status'] != 'ok' or not data['articles']:
            return None
        
        news_item = []
        for article in data['articles']:
            news_item.append({
                'title': article['title'],
                'source': article['source']['name'],
                'url': article['url'],
                'published': article['publishedAt'][:10]
            })
        return news_item
    except Exception as e:
        print(f"Error fetching news: {e}")
        return None
    
def format_news(news_item):
    if not news_item:
        return "📰 Top Financial News 📰\n News data unavailable.\n\n"
    
    news_section = "📰 Top Financial News 📰\n\n"
    for i, item in enumerate(news_item, 1):
        news_section += (
            f"{i}. {item['title']}\n"
            f"   Source: {item['source']} | {item['published']}\n"
            f"   Link: {item['url']}\n\n"
        )
    
    return news_section


def main():
    with open('watchlist.json', 'r') as file:
        watchlist = json.load(file)

    news_item = fetch_news()

    summary = format_news(news_item)
    summary += "=" * 50 + "\n\n"
    summary += format_stock_data(watchlist)

    send_email("Daily Stock Watchlist Summary", summary)

if __name__ == "__main__":
    main()