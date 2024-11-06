import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import { fetchData, fetchForecast, fetchMetrics } from '../api';

const Dashboard = () => {
    const [data, setData] = useState([]);
    const [forecast, setForecast] = useState([]);
    const [metrics, setMetrics] = useState({});
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');

    useEffect(() => {
        fetchData(startDate, endDate).then(response => setData(response.data));
        fetchForecast().then(response => setForecast(response.data));
        fetchMetrics().then(response => setMetrics(response.data));
    }, [startDate, endDate]);

    return (
        <div>
            <h1>Brent Oil Price Dashboard</h1>

            <div className="metrics">
                <h3>Model Performance Metrics</h3>
                <p>RMSE: {metrics.RMSE}</p>
                <p>MAE: {metrics.MAE}</p>
            </div>

            <div className="chart-container">
                <h3>Brent Oil Prices</h3>
                <LineChart width={800} height={400} data={data}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="Date" />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <Line type="monotone" dataKey="Price" stroke="#8884d8" />
                    <Line type="monotone" dataKey="GDP Growth Rate" stroke="#82ca9d" />
                    <Line type="monotone" dataKey="Inflation Rate" stroke="#ffc658" />
                </LineChart>
            </div>

            <div className="forecast-chart">
                <h3>Price Forecast</h3>
                <LineChart width={800} height={400} data={forecast}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="Date" />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <Line type="monotone" dataKey="Price" stroke="#82ca9d" />
                </LineChart>
            </div>
        </div>
    );
};

export default Dashboard;
