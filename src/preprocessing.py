import pandas as pd


def extract_adjusted_close(data):
    """
    Extract adjusted closing prices.
    """
    return data["Adj Close"]


def calculate_returns(prices):
    """
    Calculate daily percentage returns.
    """
    return prices.pct_change().dropna()


def split_train_test(series, split_date="2024-12-31"):
    """
    Chronological train-test split.
    """

    train = series[:split_date]
    test = series[split_date:]

    return train, test
