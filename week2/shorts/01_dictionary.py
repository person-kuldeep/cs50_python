# this program give you the stoks price of company in a dictionary

stocks = {
    "GOOGL": 2929.89,       
    "AMZN": 3344.94,
    "MSFT": 261.60,
    "TSLA": 709.67,
    "FB": 355.64,  }

while True:
    print(f"type the company symbol to get the stock price: {list(stocks.keys())}")   
    company = input("Enter the company symbol (or 'ex' to quit): ").upper()
    if company == 'EX':
        print("Exiting the program.")
        break
    elif company in list(stocks.keys()):
        print(f"The stock price of {company} is ${stocks[company]}")
        continue
    else:
        print("Company symbol not found. Please try again.")
        continue
