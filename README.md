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

2. Install dependencies
'''pip install requests
''''


