def sharpe_ration(expected_returns: float, standard_deviation: float, risk_free_rate):
    return (expected_returns - risk_free_rate) / standard_deviation