# Portfolio Optimization Using Time Series Forecasting

## Overview

This project was completed as part of the GMF Investments portfolio optimization challenge. The objective is to develop forecasting models for Tesla stock prices and use those forecasts to construct an optimized investment portfolio based on Modern Portfolio Theory (MPT).

Historical financial data were collected from Yahoo Finance for three representative assets:

- TSLA (Tesla Inc.)
- SPY (SPDR S&P 500 ETF)
- BND (Vanguard Total Bond Market ETF)

The project combines exploratory data analysis, statistical forecasting, deep learning, portfolio optimization, and strategy backtesting to support investment decision making.

---

## Objectives

- Collect historical financial data using the Yahoo Finance API.
- Perform data cleaning and exploratory data analysis.
- Evaluate stationarity using the Augmented Dickey-Fuller (ADF) test.
- Calculate financial risk metrics.
- Develop ARIMA and LSTM forecasting models.
- Forecast future Tesla prices.
- Construct an optimized investment portfolio.
- Evaluate portfolio performance through historical backtesting.

---

## Project Structure

```
portfolio-optimization/
│
├── .github/
├── .vscode/
├── data/
│   └── processed/
├── notebooks/
│   ├── Task1_EDA.ipynb
│   └── Task2_Modeling.ipynb
├── scripts/
├── src/
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SciPy
- Statsmodels
- pmdarima
- TensorFlow / Keras
- Scikit-Learn
- yfinance

---

## Completed Work (Interim Submission)

### Task 1

- Historical data extraction using Yahoo Finance
- Data cleaning
- Missing value analysis
- Duplicate checking
- Exploratory Data Analysis
- Historical price visualization
- Daily return analysis
- Rolling statistics
- Outlier detection
- Stationarity testing using ADF
- Value at Risk (VaR)
- Sharpe Ratio calculation

### Task 2

Completed:

- Chronological train-test split
- ACF and PACF analysis
- Auto ARIMA parameter selection
- ARIMA model implementation
- Tesla price forecasting
- ARIMA model evaluation (MAE, RMSE, MAPE)
- LSTM data preprocessing
- LSTM architecture design

---

## Results

The exploratory analysis shows that Tesla exhibits substantially higher volatility than SPY and BND. Stationarity tests confirmed that adjusted closing prices are non-stationary, while daily returns are stationary and therefore suitable for time-series modelling.

The ARIMA model was successfully implemented as the initial forecasting model, while the LSTM model architecture has been prepared for training during the final phase of the project.

---

## Next Steps

- Train the LSTM model
- Compare ARIMA and LSTM performance
- Generate future Tesla forecasts
- Optimize the investment portfolio using Modern Portfolio Theory
- Produce the Efficient Frontier
- Perform portfolio backtesting
- Compare the strategy against a benchmark portfolio
- Finalize investment recommendations

---

## Author

GMF Investments Portfolio Optimization Project
