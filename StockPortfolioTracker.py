stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "AMZN": 130}
total_investment = 0
portfolio = {}

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_investment += stock_prices[stock] * quantity
    else:
        print("Stock not found.")

print("\nPortfolio Summary:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares @ ${stock_prices[stock]} each")

print(f"\nTotal Investment Value: ${total_investment}")

with open("portfolio.txt", "w") as file:
    for stock, qty in portfolio.items():
        file.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} each\n")
    file.write(f"\nTotal Investment Value: ${total_investment}")