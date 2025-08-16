# Daily Stock Watchlist & Financial News Emailer  

📈 **Project Overview**  
This Python project automatically fetches daily stock prices for your personalized watchlist and top business news headlines, formats them into a clear summary, and emails it to you. It's designed for traders, investors, or anyone who wants to stay on top of the market without manually checking multiple sources.  

---

## Features  

- Fetches **latest stock prices** (open, high, low, close) for symbols in a user-defined watchlist.  
- Retrieves **top 5 business news headlines** from the US.  
- Automatically **sends an email** with a neatly formatted summary.  
- Supports an **editable watchlist** via a simple JSON file.  

---

## Tech Stack & Libraries  

- **Python 3.13**  
- `requests` – for API calls  
- `smtplib` & `email.mime.text` – for sending emails  
- APIs: [Alpha Vantage](https://www.alphavantage.co/) for stock data, [NewsAPI](https://newsapi.org/) for business news  

---

## Setup  

1. Clone the repository:  
```bash
git clone <repo-url>
cd <repo-folder>
```
2. Create a credentials.py file with your API keys and email credentials:
   ```bash
   ALPHA_VANTAGE_API_KEY = "<your_alpha_vantage_key>"
   NEWS_API_KEY = "<your_news_api_key>"
   EMAIL_USER = "<your_email>
   EMAIL_PASS = "<your_email_password>
   NOTIFICATION_EMAIL = "<recipient_email>

3. Run the daily report script:
   ```bash
   python daily_report.py

# Example Output
```bash
📰 Top Financial News 📰
1. Stock market hits new highs
   Source: Bloomberg | 2025-08-15
   Link: https://...

📊 Stock Watchlist Summary 📊
Symbol: AAPL (2025-08-14)
Open: $172.50
High: $175.00
Low: $171.00
Close: $174.25```


