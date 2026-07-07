import pandas as pd


def annualized_returns(returns):
    """
    Compute annualized expected returns.
    """

    return returns.mean() * 252


def covariance_matrix(returns):
    """
    Compute annualized covariance matrix.
    """

    return returns.cov() * 252
