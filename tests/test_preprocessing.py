import pandas as pd
from src.preprocessing import calculate_returns


def test_calculate_returns():
    prices = pd.DataFrame({
        "TSLA": [100, 110, 121]
    })

    returns = calculate_returns(prices)

    assert len(returns) == 2
