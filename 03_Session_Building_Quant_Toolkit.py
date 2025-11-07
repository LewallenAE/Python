# Turn the volatility calculator into a function

# original which requires copy paste
"""
avg_return = sum(returns) /  len(returns)
squares = 0
for ret in returns:
    squares += (ret - avg_return) ** 2
variance = squares / len(returns)
std_dev = variance ** 0.5
"""


# function

def calculate_volatility(returns):
    avg_return = sum(returns) / len(returns)
    squares = 0
    for ret in returns:
        squares += (ret - avg_return) ** 2
    variance = squares / len(returns)
    std_dev = variance ** 0.5
    return std_dev


vol1 = calculate_volatility([0.02, -0.01, 0.03])
print(f"{vol1:.6f}")




# Function basics


# def function_name(parameters):
        # code goes here
    # return result


def calculate_return(initial, final):
    return_pct = (final - initial) / initial
    return return_pct

profit = calculate_return(100, 105)
print(f"Return: {profit:.2%}")



# Parameters are inputs

def option_payoff(stock_price, strike, premium):
    intrinsic = max(stock_price - strike, 0)
    profit = intrinsic - premium
    return profit


payoff1 = option_payoff(160, 150, 5)
print(f"Payoff: ${payoff1:.2f}")


def analyze_trade(entry, exit, shares):
    pnl = (exit - entry) & shares
    return_pct = (exit - entry) / entry
    return pnl, return_pct

profit, return_rate = analyze_trade(100, 105, 500)
print(f"Profit: ${profit}, Return: {return_rate:.2%}")

def calculate_sharpe(returns, risk_free_rate=0.02):
    avg_return = sum(returns) / len(returns)
    vol = calculate_volatility(returns)
    sharpe = (avg_return - risk_free_rate) / vol
    return sharpe

