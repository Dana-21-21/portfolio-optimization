"""
data_loader.py

Utility functions for downloading, loading, and saving
financial market data used throughout the project.
"""

import pandas as pd
import yfinance as yf


def load_market_data(tickers, start_date, end_date):
    """
    Download historical market data from Yahoo Finance.

    Parameters
    ----------
    tickers : list
        List of stock/ETF ticker symbols.
    start_date : str
        Start date in YYYY-MM-DD format.
    end_date : str
        End date in YYYY-MM-DD format.

    Returns
    -------
    pandas.DataFrame
        Downloaded market data.
    """

    try:
        data = yf.download(
            tickers=tickers,
            start=start_date,
            end=end_date,
            auto_adjust=False,
            progress=False,
            group_by="column"
        )

        if data.empty:
            raise ValueError("Downloaded dataset is empty.")

        # Fill missing values if they exist
        if data.isnull().sum().sum() > 0:
            print("Warning: Missing values detected. Filling missing values...")
            data = data.ffill().bfill()

        return data

    except Exception as e:
        raise RuntimeError(f"Failed to download Yahoo Finance data.\n{e}")


def save_processed_prices(prices,
                          filepath="../data/processed/prices.csv"):
    """
    Save processed adjusted closing prices.

    Parameters
    ----------
    prices : pandas.DataFrame
        Adjusted closing prices.
    filepath : str
        Output csv file.
    """

    prices.to_csv(filepath)

    print(f"Processed prices saved to {filepath}")


def load_processed_prices(filepath="../data/processed/prices.csv"):
    """
    Load processed adjusted closing prices.

    Parameters
    ----------
    filepath : str
        Path to processed csv file.

    Returns
    -------
    pandas.DataFrame
    """

    try:

        prices = pd.read_csv(
            filepath,
            index_col=0,
            parse_dates=True
        )

        if prices.empty:
            raise ValueError("The processed prices file is empty.")

        return prices

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Cannot find file:\n{filepath}"
        )

    except Exception as e:
        raise RuntimeError(
            f"Unable to load processed prices.\n{e}"
        )
