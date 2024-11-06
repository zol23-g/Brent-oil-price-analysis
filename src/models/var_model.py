# src/models/var_model.py

import pandas as pd
from statsmodels.tsa.api import VAR

# Load processed data
data = pd.read_csv('data/cleaned_BrentOilPrices.csv', parse_dates=['Date'], index_col='Date')
var_data = data[['Price', 'GDP Growth Rate', 'Inflation Rate', 'Exchange Rate']].dropna()

# Fit the VAR model
model = VAR(var_data)
var_result = model.fit(2)  # Lag order can be adjusted
print(var_result.summary())

# Forecast the next 10 days
forecast = var_result.forecast(var_data.values[-2:], steps=10)
forecast_df = pd.DataFrame(forecast, index=pd.date_range(start=var_data.index[-1], periods=10, freq='D'),
                           columns=var_data.columns)
print("VAR Model Forecast:\n", forecast_df)
