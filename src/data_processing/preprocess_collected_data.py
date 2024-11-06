# src/data_processing/preprocess_data.py

import pandas as pd

# Load data
brent_data = pd.read_csv('data/Copy of BrentOilPrices.csv', parse_dates=['Date'], index_col='Date')
gdp_data = pd.read_csv('data/collected_data/gdp/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_261404.csv', skiprows=4)
inflation_data = pd.read_csv('data/collected_data/inflation_rate/API_FP.CPI.TOTL_DS2_en_csv_v2_269369.csv', skiprows=4)
exchange_rate_data = pd.read_csv('data/collected_data/exchange_rate/API_FR.INR.RINR_DS2_en_csv_v2_262777.csv', skiprows=4)

# Reshape each dataset from wide to long format
def reshape_data(data, value_name):
    data_long = data.melt(id_vars=['Country Name', 'Country Code'], 
                          value_vars=[str(year) for year in range(1987, 2023)],
                          var_name='Year', value_name=value_name)
    data_long['Year'] = pd.to_datetime(data_long['Year'], format='%Y')
    data_long.set_index('Year', inplace=True)
    return data_long

# Reshape and filter data
gdp_data = reshape_data(gdp_data, 'GDP Growth Rate').query("`Country Name` == 'United States'")
inflation_data = reshape_data(inflation_data, 'Inflation Rate').query("`Country Name` == 'United States'")
exchange_rate_data = reshape_data(exchange_rate_data, 'Exchange Rate').query("`Country Name` == 'United States'")

# Remove duplicate years and forward-fill the annual data to match daily frequency
gdp_data = gdp_data[~gdp_data.index.duplicated(keep='first')].resample('D').ffill()
inflation_data = inflation_data[~inflation_data.index.duplicated(keep='first')].resample('D').ffill()
exchange_rate_data = exchange_rate_data[~exchange_rate_data.index.duplicated(keep='first')].resample('D').ffill()

# Merge all datasets with Brent oil prices
merged_data = brent_data.join([gdp_data['GDP Growth Rate'], inflation_data['Inflation Rate'], exchange_rate_data['Exchange Rate']], how='left')

# Save merged data
merged_data.to_csv('data/cleaned_BrentOilPrices.csv')
print("Data preprocessing complete. Merged data saved to 'data/cleaned_BrentOilPrices.csv'.")
