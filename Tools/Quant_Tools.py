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