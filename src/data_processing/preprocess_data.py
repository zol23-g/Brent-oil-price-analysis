import pandas as pd

def load_and_clean_data(file_path):
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'], format='%d-%b-%y')
    data.set_index('Date', inplace=True)
    data = data.dropna()  # Handle missing values
    data = data[data['Price'] > 0]  # Handle any negative prices (outliers)
    return data

if __name__ == '__main__':
    data = load_and_clean_data('data/BrentOilPrices.csv')
    data.to_csv('data/cleaned_BrentOilPrices.csv')
