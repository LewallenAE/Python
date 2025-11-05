print("Hello, Quant World!")

# Integers (whole number)
num_trades = 1000
position_size = 50

# Floats (decimal)
stock_price = 152.75
volatility = 0.25

# Strings (text)
ticker = "AAPL"
strategy_name = "momentum"


# Booleans True / False
is_profitable = True
market_open = False

# Printing variables

print("Stock:", ticker)
print("Price:", stock_price)
print("Volatility:", volatility)


# Basic Math

pnl = 1500.50
commission = 12.25
net_pnl = pnl - commission

print("Net P&L:", net_pnl)


# PEMDAS
option_value = 100 * (1.5 + 2.3) / 2
print(option_value)


#Exponents (crucial for compounding returns)
initial_capital = 100000
annual_return = 0.15
years = 5
final_value = initial_capital * (1 + annual_return) ** years
print("Portfolio value:", final_value)


# Modulo (remainder - useful for time calculations)
seconds = 12345
hours = seconds // 3600
remaining = seconds %3600
minutes = remaining // 60
print(f"{hours}h {minutes} m")


# First Quant Calculation -> Expected Value E[X]

# probability of weighted outcomes
prob_win = 0.60
win_amount = 100

prob_lose = 0.40
lose_amount = -80

expected_value = (prob_win * win_amount) + (prob_lose * lose_amount)

print(f"Expected Value: ${expected_value}")
print(f"Decision: {'Play' if expected_value >0 else 'Do NOT play'}")


