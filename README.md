# Brent Oil Price Analysis

## Project Overview
This project analyzes the historical Brent oil prices and explores how various economic indicators (GDP growth rate, inflation rate, and exchange rate) impact oil price trends. The analysis includes time series modeling, econometric analysis, and machine learning models to capture complex dependencies and forecast price movements. 

The insights generated here can assist investors, policymakers, and stakeholders in understanding the factors influencing oil prices and making informed decisions in the energy market.


## Data Sources
1. **Brent Oil Prices**: Contains daily oil price data.
2. **Economic Indicators**:
   - **GDP Growth Rate**: Data on GDP growth, sourced from the World Bank.
   - **Inflation Rate**: Annual inflation rates.
   - **Exchange Rate**: Real effective exchange rate index.

## Setup and Installation
To set up the project locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/zol23-g/Brent-oil-price-analysis.git
    cd brent-oil-price-analysis
    ```

2. **Install Dependencies**:
    Create a virtual environment and install dependencies from `requirements.txt`:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Run Tests**:
    To ensure everything is set up correctly, run the test suite:
    ```bash
    pytest tests/
    ```

## Usage

### 1. Data Preprocessing
Clean and preprocess the data:
```bash
python src/data_processing/preprocess_data.py
```

This script handles the initial cleaning and transformation of Brent oil prices and economic indicators, making them suitable for analysis.

### 2. Exploratory Data Analysis (EDA)
The EDA notebook (`notebooks/01_eda.ipynb`) contains initial visualizations and statistical summaries of Brent oil prices and economic indicators. You can use Jupyter to explore trends and correlations.

### 3. Modeling
Several models are provided to analyze and forecast Brent oil prices:
- **VAR (Vector Autoregression)** for multivariate time series analysis.
- **Markov-Switching Model** for regime-switching.
- **LSTM** for capturing complex dependencies.

Run a model with:
```bash
python src/models/var_model.py  # For VAR
python src/models/lstm_model.py  # For LSTM
```

### 4. Forecasting
After fitting a model, you can use it to forecast future prices or analyze factor influences. Forecast results are displayed in the respective modeling script output.

## Model Insights and Results

- **VAR Model**: The Vector Autoregression model showed significant autocorrelation in oil prices, indicating that previous prices strongly predict future prices. Weak relationships with GDP growth and exchange rate suggest other factors may have limited impact on short-term oil price fluctuations.
- **Markov-Switching Model**: This model effectively identified different market regimes, helping to capture shifts in price behavior during periods of volatility.
- **LSTM Model**: The LSTM model demonstrated good predictive performance, effectively capturing non-linear dependencies. However, further tuning is needed for optimized accuracy.

## Future Improvements
- **Incorporate More Indicators**: Consider additional economic or environmental variables, such as crude oil supply, geopolitical factors, and renewable energy production.
- **Enhanced Forecasting Models**: Implement hybrid models (e.g., combining ARIMA with machine learning) for improved predictive performance.
- **Deploy Dashboard**: Create an interactive dashboard to allow stakeholders to explore and visualize forecasted oil prices and related indicators.

---

This project provides a foundation for understanding and predicting Brent oil prices in response to various economic indicators, helping stakeholders make more informed decisions in energy markets.
```

