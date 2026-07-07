# GMF Investments – Portfolio Optimization Using Time Series Forecasting

## Project Overview

This project was completed as part of the 10 Academy Artificial Intelligence Mastery Program.

The objective is to help **GMF Investments**, a personalized portfolio advisory firm, improve investment decision-making by forecasting Tesla (TSLA) stock prices and incorporating those forecasts into a portfolio optimization framework.

The project combines:

- Financial data collection
- Exploratory Data Analysis (EDA)
- Time Series Forecasting (ARIMA & LSTM)
- Portfolio Optimization using Modern Portfolio Theory (MPT)
- Strategy Backtesting

The workflow demonstrates how machine learning forecasts can support portfolio allocation decisions while balancing expected return and investment risk.

---

# Business Objective

GMF Investments provides personalized investment advice to its clients.

As a Financial Analyst, the goal of this project is to translate business requirements into a data-driven investment strategy by:

- Forecasting Tesla stock prices
- Measuring investment risk
- Optimizing portfolio allocation
- Evaluating strategy performance through historical backtesting

The project also acknowledges the **Efficient Market Hypothesis (EMH)**, which suggests that markets rapidly incorporate available information. Therefore, predictive models are evaluated critically rather than assuming they consistently outperform the market.

---

# Repository Structure

```
portfolio-optimization/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── Task1_Data_Preprocessing.ipynb
│   ├── Task2_Forecasting.ipynb
│   ├── Task3_Future_Forecast.ipynb
│   ├── Task4_Portfolio_Optimization.ipynb
│   └── Task5_Backtesting.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── forecasting.py
│   ├── portfolio.py
│   └── backtesting.py
│
├── reports/
│
├── figures/
│
├── requirements.txt
│
└── README.md
```

---

# Dataset

Historical daily prices were downloaded from Yahoo Finance.

Assets:

- Tesla (TSLA)
- SPDR S&P 500 ETF (SPY)
- Vanguard Total Bond Market ETF (BND)

Time Period:

2015 – 2026

---

# Task 1 – Data Preparation & Exploratory Data Analysis

Completed:

- Downloaded historical market data
- Cleaned missing values
- Saved processed dataset
- Visualized historical price movements
- Calculated daily returns
- Conducted stationarity testing using the Augmented Dickey-Fuller (ADF) Test
- Performed volatility analysis
- Calculated Value-at-Risk (VaR)
- Calculated Sharpe Ratio

Key Findings

- Tesla exhibited the highest volatility.
- SPY produced the highest risk-adjusted return.
- BND showed the lowest investment risk.
- Tesla required differencing to achieve stationarity.

---

# Task 2 – Time Series Forecasting

Two forecasting approaches were implemented.

## ARIMA

Model Selection

Auto ARIMA selected:

ARIMA(0,1,0)

Performance

- MAE: 54.44
- RMSE: 70.54
- MAPE: 17.24%

Although statistically appropriate, ARIMA produced nearly flat forecasts because stock prices behaved similarly to a random walk.

---

## LSTM

Architecture

- 2 LSTM layers
- Dropout regularization
- Dense hidden layer
- Output layer

Performance

- MAE: 14.28
- RMSE: 18.16
- MAPE: 3.94%

The LSTM model significantly outperformed ARIMA and was selected as the final forecasting model.

---

# Task 3 – Future Market Forecasting

Using the trained LSTM model:

- Forecasted approximately one year (252 trading days) into the future
- Generated future Tesla price predictions
- Visualized historical prices and forecasts
- Conducted trend analysis

Key Observations

- Forecasts indicated a downward trend over the prediction horizon.
- Forecast uncertainty increases as forecasts extend further into the future.
- Long-term predictions should therefore be interpreted cautiously.

---

# Task 4 – Portfolio Optimization

Modern Portfolio Theory (MPT) was applied using:

Assets:

- TSLA
- SPY
- BND

Expected Returns

- Tesla: LSTM forecast
- SPY: Historical annualized return
- BND: Historical annualized return

Covariance matrix was computed using historical returns.

Portfolio optimization maximized the Sharpe Ratio.

Optimal Portfolio

| Asset | Weight |
|--------|--------|
| TSLA | 0.00% |
| SPY | 44.82% |
| BND | 55.18% |

Portfolio Performance

- Expected Return: 7.59%
- Risk: 8.75%
- Sharpe Ratio: 0.87

The optimizer excluded Tesla because the LSTM forecast projected a negative expected return.

---

# Task 5 – Strategy Backtesting

The optimized portfolio was evaluated over the out-of-sample testing period.

Benchmark Portfolio

- 60% SPY
- 40% BND

Evaluation Metrics

- Cumulative Return
- Annualized Return
- Sharpe Ratio
- Maximum Drawdown

The optimized portfolio was compared against the benchmark to assess whether forecast-driven allocation improved investment performance.

---

# Project Workflow

```
Yahoo Finance
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Stationarity Testing
      │
      ▼
ARIMA & LSTM Forecasting
      │
      ▼
Future Price Prediction
      │
      ▼
Portfolio Optimization
      │
      ▼
Strategy Backtesting
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Statsmodels
- TensorFlow / Keras
- Scikit-learn
- SciPy
- yfinance
- Jupyter Notebook

---

# Key Results

| Model | MAE | RMSE | MAPE |
|------|------:|------:|------:|
| ARIMA | 54.44 | 70.54 | 17.24% |
| LSTM | 14.28 | 18.16 | 3.94% |

The LSTM model produced substantially lower prediction errors and was selected for forecasting and portfolio optimization.

---

# Future Improvements

Potential extensions include:

- Transformer-based forecasting models
- Prophet forecasting
- Additional financial indicators
- Macroeconomic variables
- Monthly portfolio rebalancing
- Transaction cost modeling
- Hyperparameter optimization
- Cross-validation for time series

---

# Author

Prepared for the **10 Academy AI Mastery Program**

Financial Forecasting and Portfolio Optimization Project
