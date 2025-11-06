# Problem 1 Profit Calculator



print("\nProblem 1: Profit Calculator\n")
# a total pnl
trades_pnl = [150, -80, 200, -50, 100, -120, 180]

total_pnl = 0

for trades in trades_pnl:
    total_pnl += trades


print(f"a) Total PnL: ${total_pnl}")


# b

winning_trades = 0
losing_trades = 0

for trades in trades_pnl:
    if trades > 0:
        winning_trades += 1
    else:
        losing_trades += 1

print(f"b) Total winning trades: {winning_trades}")
print(f"c) Total losing trades: {losing_trades}")
win_rate = winning_trades / len(trades_pnl)
print(f"d) Win rate percentage: {win_rate:.2%}")

win = 0
loss = 0
win_list = []
loss_list = []

for trades in trades_pnl:
    if trades > 0:
        win += trades
        win_list.append(trades)
    elif trades < 0:
        loss += trades
        loss_list.append(trades)

average_win = win / len(win_list)
average_loss =  loss / len(loss_list)

print(f"e) Average win size: ${average_win:.2f}")
print(f"f) Average loss size: ${average_loss:.2f}\n\n")

# Problem 2 Drawdown Detector

print("Problem 2: Draw Down Detector\n")

account_values = [10000, 10500, 10200, 10800, 10600, 11000, 10400, 10900]

# Calculate:

# a) The maximum account value reached (peak)
peak = max(account_values)
peak_index = account_values.index(peak)
trough = min(account_values[peak_index + 1:])
trough_day = account_values.index(10400)

print(f"a) The peak account value is: ${peak}")

# b) min value AFTER the peak?
print(f"b) The min value after peak is: ${trough}")

# c) Max drawdown 
max_drawdown = peak - trough
print(f"c) Max drawdown is: ${max_drawdown}")

# d) Print when the drawdown occurred
print(f"d) Drawdown occurred on day {trough_day}!\n\n")



# Problem 3 - Signal Generator

print("Problem 3\n")
prices = [100, 102, 98, 103, 105, 104, 107, 106, 110, 108]
window = 3



print(" Price | 3 Day MA")
print("-" * 20)

for i in range(window - 1, len(prices)):
    window_prices = prices[i - window + 1 : i + 1]

    ma = sum(window_prices) / window
    price = prices[i]

    if price > ma:
        print(f"${prices[i]:>5} | {ma:>6.2f} BUY signal")
    elif price < ma:
        print(f"${prices[i]:>5} | {ma:>6.2f} SELL signal")
    elif price == ma:
        print(f"${prices[i]:>5} | {ma:>6.2f} HOLD!")



# Problem 4 - Stop Loss 

"""

Bought stock at $100
stop loss at 5% below entry
what day does stop loss trigger?

"""

print("\n")
print("Problem 4\n")

entry_price = 100
stop_loss_pct = 0.05 # 5%
prices = [100, 102, 99, 98, 96, 94, 95,97]

for price in prices:
    if price <= 100 - ( 100 *0.05):
        print(f"Stop loss triggered at ${price:.2f}! On day # {prices.index(price)}, with a loss amount of ${entry_price - price:.2f}\n\n")
        break
    



# Volatility Calculator


print("Problem 5\n")

returns = [0.02, -0.01, 0.03, -0.005, 0.015, -0.02, 0.01, 0.005, -0.015, 0.025]
avg_return = 0

for ret in returns:
    avg_return += ret

avg_return = avg_return / len(returns)

squares = 0
variance = 0

for square in returns:
    squares += (square - avg_return) ** 2

variance = squares / len(returns)
std_dev = variance ** 0.5


print(f"Step 1: {avg_return:.4%}")
print(f"Step 2: Sum of squares is: {squares:.6f}")
print(f"Step 3: Variance is: {variance:.6f}")
print(f"Step 4: Standard Deviation is: {std_dev:.6f}")
