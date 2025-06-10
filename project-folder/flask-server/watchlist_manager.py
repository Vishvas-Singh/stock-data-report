import json

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
        elif symbol in watchlist:
            print(f"{symbol} is already in the watchlist.")
        else:
            watchlist.append(symbol)

    with open(filename, 'w') as file:
        json.dump(watchlist, file, indent=4)

    print(f"Updated watchlist: {watchlist}")

if __name__ == "__main__":
    get_stock_watchlist()