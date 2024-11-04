import pandas as pd
import src.data_processing
from src.data_preprocessing import load_data, check_data, clean_data

def test_load_data():
    file_path = '../data/BrentOilPrices.csv'
    data = load_data(file_path)
    assert isinstance(data, pd.DataFrame)
    assert 'Date' in data.columns
    assert 'Price' in data.columns

def test_check_data(capsys):
    data = pd.DataFrame({
        'Date': pd.date_range(start='1/1/2020', periods=4),
        'Price': [30.5, 31.0, None, 32.5]
    })
    check_data(data)
    captured = capsys.readouterr()
    assert "Data types" in captured.out
    assert "Missing values in each column" in captured.out

def test_clean_data():
    data = pd.DataFrame({
        'Date': pd.date_range(start='1/1/2020', periods=4),
        'Price': [30.5, 31.0, None, 32.5]
    })
    cleaned_data = clean_data(data)
    assert cleaned_data.isnull().sum().sum() == 0
    assert len(cleaned_data) == 3