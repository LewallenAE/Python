stock_price = 155.50
buy_threshold = 150.00

if stock_price > buy_threshold:
    print("Price is too high, don't buy!")


stock_price2 = 145.00
buy_threshold2 = 150.00

if stock_price < buy_threshold:
    print("Good price, BUY!")
else:
    print("Price is too high, don't buy!")



sharpe_ratio = 1.8

if sharpe_ratio > 2.0:
    print("Excellent Strategy")
elif sharpe_ratio > 1.0:
    print("Good Strategy")
elif sharpe_ratio > 0:
    print("Mediocre Strategy")
else:
    print("Losing Strategy")        

price = 80
if price == 100:
    print("Exactly $100")
else:
    print("nvm not 100.")

if price != 100:
    print("Ah yes, 100 is too much~!~")

if price > 100:
    print("Over 100")

if price >= 100:
    print("100 or above")

if price > 90 and price < 110:
    print("Price between 90 and 110")

max_drawdown = 0.05

if sharpe_ratio > 1.5 or max_drawdown < 0.10:
    print("Strategu passes our criteria.")
    