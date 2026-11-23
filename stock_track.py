stock_price_dictionary = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 170,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks:", list(stock_price_dictionary.keys()))

#stock details
while True:

    
    user_input = input("\nEnter stock name: ").strip().upper()

    
    if user_input not in stock_price_dictionary:
        print("Stock not found. Please enter a valid stock.")
        continue

    
    quantity_input = input("Enter stock quantity: ")

    try:
        quantity = int(quantity_input)

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    
    price = stock_price_dictionary[user_input]
    investment = price * quantity

    portfolio.append([user_input, price, quantity, investment])

    total_investment += investment

    print("Stock added successfully!")
    print("Investment value:", investment)
    
    choice = input("Do you want to add another stock? (yes/no): ").strip().lower()

    if choice != "yes":
        break

print("\n------ STOCK PORTFOLIO SUMMARY ------")

for stock in portfolio:
    print("Stock:", stock[0])
    print("Price:", stock[1])
    print("Quantity:", stock[2])
    print("Investment:", stock[3])
    print("------------------------")

print("Total Investment:", total_investment)
print("Thank you for using Stock Portfolio Tracker!")
