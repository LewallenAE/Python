

"""

Basic if statement

"""

stock_price = 155.50
buy_threshold = 150.00

if stock_price > buy_threshold:
    print("Price is too high, don't buy!")


"""

If-Else

"""
stock_price2 = 145.00
buy_threshold2 = 150.00

if stock_price < buy_threshold:
    print("Good price, BUY!")
else:
    print("Price is too high, don't buy!")


"""

If-Elif-Else multiple conditions

"""

sharpe_ratio = 1.8

if sharpe_ratio > 2.0:
    print("Excellent Strategy")
elif sharpe_ratio > 1.0:
    print("Good Strategy")
elif sharpe_ratio > 0:
    print("Mediocre Strategy")
else:
    print("Losing Strategy")        


"""

Comparison Operators

"""

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



"""

Real Example: Option Payoff Decision

"""

stock_price = 160
strike_price = 150
premium = 5


intrinsic_value = stock_price - strike_price
profit = intrinsic_value = premium

if profit >0:
    print(f"EXERCISE the option! Profit: ${profit}")
elif profit == 0:
    print("Break even, doesn't matter")
else:
    print(f"Let it expire worthless. Loss ${profit}")


"""

Creating Lists

"""
# Work with time series in Quant

prices = [100, 102, 101, 103, 105]


returns = [0.02, -0.01, 0.03, 0.015, -0.005]

portfolio = ["AAPL", 100, 152.50, "tech"]


"""

Accessing Elements

"""

prices = [100, 102, 101, 103, 105]


first_price = prices[0] # index 0 first value
second_price = prices[1] # index 1 second value
last_price = prices[4]# index 4 fifth value

last_price = prices[-1] # last
second_last = prices[-2]# second to last

print(f"First: ${first_price}, Last: ${last_price}")


"""

List Operations

"""
prices = [100, 102, 101]

num_days =len(prices)

prices.append(103)


total = sum(prices)

lowest = min(prices)
highest = max(prices)

print(f"Average price: ${sum(prices) / len(prices):.2f}")


"""

Slicing: Getting Subsets

"""


prices = [100, 102, 101, 103, 105, 107]


first_three = prices[0:3]

first_three = prices[:3]


last_three = prices[3:]

middle = prices[2:5]



"""

For Loops (Repeating Actions)

"""

# Basic for loop

prices = [100, 102, 101, 103, 105]

for price in prices:
    print(f"Current price: ${price}")



# Loop with index

prices = [100, 102, 101, 103, 105]

for i in range(len(prices)):
    print(f"Day {i}: ${prices[i]}")



# Calculating returns with a loop


prices = [100, 102, 101, 103, 105]


print("Daily Returns")
for i in range(1, len(prices)): # start at second price because you don't have a return from the first day
    previous_price = prices[i-1]
    current_price = prices[i]
    daily_return = (current_price - previous_price) / previous_price
    print(f"Day {i}: {daily_return:.2%}")




# New List with a Loop


prices = [100, 102, 101, 103, 105]
returns = []  # Empty List

for i in range(1, len(prices)):
    ret = (prices[i] - prices[i-1]) / prices[i-1]
    returns.append(ret)

print(f"Returns: {returns}")
print(f"Average return: {sum(returns) / len(returns):.4%}")





# While Loops Conditional Repetition

pnl = 0
target = 100
trades = 0

while pnl < target:

    trade_pnl = 15
    pnl += trade_pnl
    trades += 1
    print(f"Trade {trades}: Pn: = ${pnl}")

print(f"\nHit target after {trades} trades!")



# Combine everything - finding the best entry price

prices = [150, 152, 148, 151, 149, 153, 147, 150]


best_price = prices[0]
best_time = 0

for i in range(len(prices)):
    if prices[i] < best_price:
        best_price = prices[i]
        best_time = i

print(f"Best time to buy: Hour {best_time} at ${best_price}")



# Real Example: Count Profitable Days

returns = [0.02, -0.01, 0.03, -0.005, 0.015, -0.02, 0.01]

profitable_days = 0
losing_days = 0

for ret in returns:
    if ret > 0:
        profitable_days += 1
    elif ret < 0:
        losing_days += 1

win_rate = profitable_days / len(returns)

print(f"Profitable days: {profitable_days}")
print(f"Losing das: {losing_days}")
print(f"Win rate: {win_rate:.1%}")



# Moving average (first real tool)

# Simple Moving Average

prices = [100, 102, 101, 78, 103, 105, 104, 106, 108, 107, 110]
window = 3

print("Price | 3-Day MA")
print("-" * 20)

for i in range(window -1, len(prices)):

    window_prices = prices[i - window + 1 : i + 1]

    ma = sum(window_prices) / window

    print(f"${prices[i]:>5} | ${ma:>6.2f}")



