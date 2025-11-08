def sharpe_ratio(returns, risk_free_rate = 0):

    """
    
    Calculates the Sharpe ratio of a return series.

    Args:
        returns: List of returns (as decimals, e.g., 0.01 for 1%)
        risk_free_rate: Risk-free rate *default 0*

        Returns:
            Sharpe ratio (float) 

    """

    if len(returns) == 0:
        return 0
    
    avg_return = sum(returns) / len(returns)

    mean_return = avg_return
    squared_diffs = [(r - mean_return) ** 2 for r in returns]
    variance = sum(squared_diffs) / len(returns)
    std_dev = variance ** 0.5

    if std_dev == 0:
        return 0

    return (avg_return - risk_free_rate) / std_dev
 



# Maximum drawdown


def max_drawdown(account_values):


    """
    
    Calculate the maximum drawdown from a series of account values.

    Returns:
        (max_dd_pct, peak, trough, peak_idx, trough_idx)

    
    """

    if len(account_values) == 0:
        return 0, 0, 0, 0, 0
    
    peak = account_values[0]
    peak_idx = 0
    trough_value = account_values[0]
    max_dd = 0
    max_dd_peak_idx = 0
    max_dd_trough_idx = 0

    for i in range(len(account_values)):
        value = account_values[i]

        if value > peak:
            peak = value
            peak_idx = i

        drawdown = (peak - value) / peak

        if drawdown > max_dd:
            max_dd = drawdown
            max_dd_peak_idx = peak_idx
            max_dd_trough_idx = i
            trough_value = value

    peak_value = account_values[max_dd_peak_idx]
    return max_dd, peak_value, trough_value, max_dd_peak_idx, max_dd_trough_idx
    
equity_curve = [10000, 10500, 10200, 10800, 10600, 11000, 10400, 10900]
dd, peak, trough, peak_day, trough_day = max_drawdown(equity_curve)
print(f"Max_Drawdown: {dd:.2%}")
print(f"From: ${peak:.2f} day {peak_day:.0f} to {trough:.0f} day {trough_day:.2f}")




# Moving Average


def simple_moving_average(prices, window):

    """
    
    Calculates simple moving average.

    Returns:
        Liset of moving averages (starts at index window - 1)
    
    """

    if len(prices) < window:
        return []
    
    mas = []
    for i in range(window - 1, len(prices)):
        window_prices = prices[i - window + 1 : i + 1]
        ma = sum(window_prices) / window
        mas.append(ma)
    return ma

prices = {100, 102, 98, 103, 105, 104, 107}
ma_3 = simple_moving_average(prices, 3)
print(f"3-day MAs: {ma_3}")