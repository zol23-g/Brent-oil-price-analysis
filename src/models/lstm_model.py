# src/models/lstm_model.py

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from datetime import timedelta

# Load and scale the data
data = pd.read_csv('data/cleaned_BrentOilPrices.csv', parse_dates=['Date'], index_col='Date')
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data['Price'].values.reshape(-1,1))

# Prepare data for LSTM training
X, y = [], []
for i in range(60, len(scaled_data)):
    X.append(scaled_data[i-60:i, 0])
    y.append(scaled_data[i, 0])
X, y = np.array(X), np.array(y)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Build LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=False))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, y, epochs=20, batch_size=32)

# Generate forecast for the next 10 days
forecast_steps = 10
forecast = []

# Start with the last 60 days of known data
last_60_days = scaled_data[-60:]
last_60_days = np.reshape(last_60_days, (1, last_60_days.shape[0], 1))

for _ in range(forecast_steps):
    # Predict the next price
    next_price_scaled = model.predict(last_60_days)
    forecast.append(next_price_scaled[0, 0])  # Store the forecasted price

    # Update the input sequence with the new prediction by reshaping to match dimensions
    last_60_days = np.append(last_60_days[:, 1:, :], np.reshape(next_price_scaled, (1, 1, 1)), axis=1)


# Inverse transform the forecasted prices to the original scale
forecast_prices = scaler.inverse_transform(np.array(forecast).reshape(-1, 1))

# Create a date range for the forecast
last_date = data.index[-1]
forecast_dates = [last_date + timedelta(days=i) for i in range(1, forecast_steps + 1)]

# Create and save the forecast DataFrame
forecast_df = pd.DataFrame({'Date': forecast_dates, 'Price': forecast_prices.flatten()})
forecast_df.to_csv('data/forecast.csv', index=False)
print("Forecast saved to 'data/forecast.csv'")
