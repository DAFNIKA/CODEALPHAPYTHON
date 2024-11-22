import yfinance as yf

# Initialize an empty portfolio
portfolio = {}

def fetch_stock_price(ticker):
    """Fetch the current stock price using yfinance."""
    try:
        stock = yf.Ticker(ticker)
        price = stock.info.get("regularMarketPrice")
        if price is None:
            raise ValueError(f"Price for {ticker} not found.")
        return price
    except Exception as e:
        print(f"Error fetching price for {ticker}: {e}")
        return None

def add_stock(ticker, shares, buy_price):
    """Add a stock to the portfolio."""
    if ticker in portfolio:
        portfolio[ticker]["shares"] += shares
    else:
        portfolio[ticker] = {"shares": shares, "buy_price": buy_price}
    print(f"Added {shares} shares of {ticker} at ${buy_price} per share.")

def remove_stock(ticker):
    """Remove a stock from the portfolio."""
    if ticker in portfolio:
        del portfolio[ticker]
        print(f"Removed {ticker} from the portfolio.")
    else:
        print(f"{ticker} is not in the portfolio.")

def view_portfolio():
    """View the current portfolio performance."""
    if not portfolio:
        print("Your portfolio is empty.")
        return

    total_investment = 0
    total_value = 0
    print("\nPortfolio Summary:\n")
    print(f"{'Ticker':<10} {'Shares':<10} {'Buy Price':<10} {'Current Price':<15} {'Value':<15} {'P/L ($)':<10} {'P/L (%)':<10}")
    print("-" * 70)

    for ticker, data in portfolio.items():
        shares = data["shares"]
        buy_price = data["buy_price"]
        current_price = fetch_stock_price(ticker)
        if current_price is None:
            continue

        value = shares * current_price
        investment = shares * buy_price
        profit_loss = value - investment
        profit_loss_pct = (profit_loss / investment) * 100 if investment > 0 else 0

        total_investment += investment
        total_value += value

        print(f"{ticker:<10} {shares:<10} {buy_price:<10.2f} {current_price:<15.2f} {value:<15.2f} {profit_loss:<10.2f} {profit_loss_pct:<10.2f}")

    total_profit_loss = total_value - total_investment
    total_profit_loss_pct = (total_profit_loss / total_investment) * 100 if total_investment > 0 else 0
    print("-" * 70)
    print(f"Total Investment: ${total_investment:.2f}")
    print(f"Total Value: ${total_value:.2f}")
    print(f"Total Profit/Loss: ${total_profit_loss:.2f} ({total_profit_loss_pct:.2f}%)\n")

def menu():
    """Display the main menu."""
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            ticker = input("Enter stock ticker (e.g., AAPL): ").upper()
            try:
                shares = int(input(f"Enter the number of shares for {ticker}: "))
                buy_price = float(input(f"Enter the buy price for {ticker}: "))
                add_stock(ticker, shares, buy_price)
            except ValueError:
                print("Invalid input. Please enter numeric values for shares and buy price.")
        elif choice == "2":
            ticker = input("Enter stock ticker to remove: ").upper()
            remove_stock(ticker)
        elif choice == "3":
            view_portfolio()
        elif choice == "4":
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the menu
if __name__ == "__main__":
    menu()
