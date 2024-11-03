import pandas as pd

def load_data(file_path):
    """
    Load the Brent oil prices data from a CSV file.
    
    Parameters:
    - file_path (str): The path to the CSV file.
    
    Returns:
    - pd.DataFrame: The loaded data as a pandas DataFrame.
    """
    data = pd.read_csv(file_path, parse_dates=['Date'], dayfirst=True)
    print("Data loaded successfully")
    return data

def check_data(data):
    """
    Check data types and missing values in the Brent oil prices data.
    
    Parameters:
    - data (pd.DataFrame): The raw data.
    
    Returns:
    - None
    """
    # Display data types of each column
    print("Data types:\n", data.dtypes)
    
    # Check for missing values
    missing_values = data.isnull().sum()
    print("\nMissing values in each column:\n", missing_values)

def clean_data(data):
    """
    Clean the Brent oil prices data.
    
    Parameters:
    - data (pd.DataFrame): The raw data.
    
    Returns:
    - pd.DataFrame: The cleaned data.
    """
    # Drop rows with missing values
    data_clean = data.dropna()
    print("Missing values removed")

    # Reset index
    data_clean = data_clean.reset_index(drop=True)
    print("Index reset")
    
    return data_clean

if __name__ == "__main__":
    file_path = '../data/BrentOilPrices.csv'
    data = load_data(file_path)
    check_data(data)
    data_clean = clean_data(data)
    print(data_clean.head())