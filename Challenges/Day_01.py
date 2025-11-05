# Problem set 1 - 5

# biased coin 55% heads, 45% tails, $1000 bankroll
# heads = $1 per $1 bet
# tails = $1 per $1 bet

# E[X] of 1
# E[X] of 100
# new BR after one $100 dollar bet if you win.




# Problem 1: Coin Flip Kelly Criterion

# Setup
prob_heads = 0.55
prob_tails = 0.45
bank_roll = 1000
heads_win_per_dollar = 1
tails_loss_per_dollar = -1

# Part a) Expected value of betting $1

bet_a = 1
ev_a =  bet_a * ((prob_heads * heads_win_per_dollar) + (prob_tails * tails_loss_per_dollar))

print(f"Part a) EV of $1 bet: ${ev_a:.2f}")

# part b) Expected value of betting $100
bet_b = 100
ev_b = bet_b * ((prob_heads * heads_win_per_dollar) + (prob_tails * tails_loss_per_dollar))

print(f"Part b) EV of $100 bet: ${ev_b:.2f}")

# part c) Bankroll after one $100 bet if you win.
bet_c = 100 # the amount you bet, + the amount you win, a net gain of 100 dollars. Since you get the money you bet back.
new_bankroll = bank_roll + bet_c

print(f"Part c) Your new bankroll: ${new_bankroll:.2f}")



# Problem 2: Simple Sharpe Ratio
"""
A strategy has:
- Average daily return: 0.15%
- Daily standard deviation: 1.2%
- Risk-free rate: 0.02% per day
Calculate the daily Sharpe ratio: ((return - risk_free) / std_dev)
"""

avg_return = 0.0015
std_dev = 0.012
risk_free_rate = 0.0002

daily_sharpe_ratio = (avg_return - risk_free_rate)/ std_dev

print(f"The daily sharpe ratio: ${daily_sharpe_ratio:.2f}")

# Problem 3: Option Payoff 

"""
You bought a call option on AAPL:
Strike price: $150
Premium paid: $5
Current stock price: $X

Write a program that take X as input
- calculates the profit loss
- Payoff = max(Stock-Strike, 0) - premium
"""
current_stock_price = float(input("Enter a number: "))
strike_price = 150
premium = 5
payoff = max(current_stock_price - strike_price, 0) - premium

print(f"The payoff is: ${payoff:.2f}")


# Problem 4 Compound Returns daily returns over 5 days is [0.02, -0.01, 0.03, 0.015, -0.005]

"""
Calculate
a) The cumulative return
b) the average daily return
c) Which is higher and why?

"""

# cumulative_return = (((1 + 0.02) * (1 + (-0.01)) * ( 1 + 0.03) * (1 + 0.015) * (1 + (-0.005))) - 1)
# print(f"Cumulative return a): ${cumulative_return:.4%}")

daily_returns = [0.02, -0.01, 0.03, 0.015, -0.005]
cumulative_return = 1.0
for r in daily_returns:
    cumulative_return *= (1 + r)
cumulative_return -= 1

print(f"a) Cumulative return: {cumulative_return:.4%}")

average_daily_return = (0.02 + (-0.01) + 0.03 + 0.015 + (-0.005))/5
print(f"Average Daily Return b): ${average_daily_return:.4%}")

print("The cumulative return is higher because it is cumulative or adding 1 to the daily returns, multiplying them together (instead of adding them) and then dividing by the total days.")


# 5 Bid Ask Spread

"""
Bid = $99.95
Ask = $100.05
Need to buy 1000 shares and immediately sell them.
Calculate the total transaction cost.
"""

bid = 99.95
ask = 100.05
shares = 1000
spread = ask - bid
transaction_cost = spread * shares

print(f"For a bid price of ${bid} and an ask price of ${ask}, the spread is ${spread:.2f}, and the total transaction cost is ${transaction_cost:.2f}")


# Problem 4: Compound Returns
daily_returns = [0.02, -0.01, 0.03, 0.015, -0.005]

# a) Cumulative return (geometric)
cumulative_return = 1.0
for r in daily_returns:
    cumulative_return *= (1 + r)
cumulative_return -= 1

print(f"a) Cumulative return: {cumulative_return:.4%}")  # 5.9646%

# b) Average daily return (arithmetic)
average_daily_return = sum(daily_returns) / len(daily_returns)
print(f"b) Average daily return: {average_daily_return:.4%}")  # 1.2000%

# c) Comparison
print(f"\nc) The arithmetic average ({average_daily_return:.2%}) is HIGHER.")
print("If we naively multiply: 1.2% × 5 days = 6.0%")
print(f"But actual compound return is {cumulative_return:.4%} (5.9646%)")
print("\nThis difference is called 'volatility drag':")
print("Losses hurt more than equal-sized gains help when compounding.")
print("The more volatile the returns, the bigger the drag.")
