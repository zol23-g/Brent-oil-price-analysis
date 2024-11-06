# backend/app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for frontend access

# Load the processed data
data = pd.read_csv('../../data/cleaned_BrentOilPrices.csv', parse_dates=['Date'])

@app.route('/api/data', methods=['GET'])
def get_data():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    # Filter data based on request parameters (if provided)
    filtered_data = data
    if start_date and end_date:
        filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]
    
    return jsonify(filtered_data.to_dict(orient='records'))

@app.route('/api/forecast', methods=['GET'])
def get_forecast():
    # Example: Load precomputed forecast data
    forecast_data = pd.read_csv('../../data/forecast.csv', parse_dates=['Date'])
    return jsonify(forecast_data.to_dict(orient='records'))

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    # Example metrics
    metrics = {
        "RMSE": 2.35,
        "MAE": 1.75,
        "MSE": 5.52
    }
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(debug=True)
